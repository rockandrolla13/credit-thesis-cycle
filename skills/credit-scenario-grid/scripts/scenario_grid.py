#!/usr/bin/env python3
"""Check a credit scenario grid and render it as markdown. Standard library only.

Usage: scenario_grid.py grid.json [--md report.md]
Exit code 1 when any hard check fails. The script owns every probability:
authors write fractions of spine scenarios, never sector probabilities.
"""
import argparse
import json
import math
import re
import sys

TRADE = re.compile(
    r"\b(buy|sell|go long|go short|hedge ratio|notional|position size|stop[- ]loss|dv01)\b", re.I)
SOURCES = {"evidence_weighted", "PM_assumption"}


def strings(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for k, v in o.items():
            if not str(k).startswith("_"):
                yield from strings(v)
    elif isinstance(o, list):
        for v in o:
            yield from strings(v)


def tilt(ps, xs, target=0.0):
    """Max-entropy tilt q_s ~ p_s*exp(lam*x_s) with sum(q*x) = target. None if infeasible."""
    if not (min(xs) < target < max(xs)):
        return None
    scale = max(abs(x - target) for x in xs)
    zs = [(x - target) / scale for x in xs]

    def mean(lam):
        w = [p * math.exp(lam * z) for p, z in zip(ps, zs)]
        return sum(wi * z for wi, z in zip(w, zs)) / sum(w)

    lo, hi = -60.0, 60.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if mean(mid) > 0:
            hi = mid
        else:
            lo = mid
    w = [p * math.exp((lo + hi) / 2 * z) for p, z in zip(ps, zs)]
    return [wi / sum(w) for wi in w]


def check(g):
    msgs = []
    F = lambda m: msgs.append(("FAIL", m))
    W = lambda m: msgs.append(("WARN", m))
    for k in ("as_of", "horizon", "horizon_months", "spine", "rows"):
        if k not in g:
            F(f"missing top-level field '{k}'")
    if msgs:
        return msgs
    sp = g["spine"]
    if not 4 <= len(sp) <= 5:
        F(f"spine has {len(sp)} scenarios, need 4 or 5")
    if len({s.get("id") for s in sp}) != len(sp):
        F("spine ids are not unique")
    tot = sum(s.get("p", 0) for s in sp)
    if abs(tot - 1) > 1e-6:
        F(f"spine probabilities sum to {tot:.4f}, not 1")
    for s in sp:
        sid = s.get("id")
        if not 0 < s.get("p", 0) < 1:
            F(f"{sid}: probability must be strictly between 0 and 1")
        if not s.get("name") or not s.get("test"):
            F(f"{sid}: needs a name and a decision test")
        obs = s.get("observables") or []
        if not obs or any(not o.get("series") or not o.get("threshold") for o in obs):
            F(f"{sid}: needs at least one observable with a series and a threshold")
        if s.get("p_source") not in SOURCES:
            F(f"{sid}: p_source must be one of {sorted(SOURCES)}")
        if s.get("p_source") == "evidence_weighted" and not s.get("evidence"):
            F(f"{sid}: evidence_weighted needs at least one evidence reference")
    if any(l == "FAIL" for l, _ in msgs):
        return msgs
    P = {s["id"]: s["p"] for s in sp}
    rows = {}
    for r in g["rows"]:
        rid = r.get("id")
        if rid in rows:
            F(f"duplicate row id {rid}")
        rows[rid] = r
        if not r.get("axis") or not r.get("driver"):
            F(f"{rid}: needs an axis and a driver")
        sc = r.get("scenarios", [])
        if not 4 <= len(sc) <= 5:
            F(f"{rid}: has {len(sc)} scenarios, need 4 or 5")
        cover = {k: 0.0 for k in P}
        sdx = {k: 0.0 for k in P}
        for s in sc:
            p = num = 0.0
            split = False
            for sid, f in s.get("from", {}).items():
                if sid not in P:
                    F(f"{rid}: unknown spine id {sid}")
                    continue
                fr, dx = (1.0, float(f)) if isinstance(f, (int, float)) else (f["frac"], f["dx"])
                split = split or fr < 1
                p += P[sid] * fr
                num += P[sid] * fr * dx
                cover[sid] += fr
                sdx[sid] += fr * dx
            if p <= 0:
                F(f"{rid}: scenario '{s.get('name')}' draws no probability")
                continue
            s["_p"], s["_dx"] = p, num / p
            if not s.get("name") or not s.get("why"):
                F(f"{rid}: every scenario needs a name and a why")
            if split and not s.get("observable"):
                F(f"{rid}: split scenario '{s.get('name')}' needs its own observable")
        for sid, c in cover.items():
            if abs(c - 1) > 1e-6:
                F(f"{rid}: fractions drawn from {sid} sum to {c:.2f}, not 1")
        r["_sdx"] = sdx
        done = [s for s in sc if "_p" in s]
        ps, xs = [s["_p"] for s in done], [s["_dx"] for s in done]
        r["_exp"] = sum(P[k] * sdx[k] for k in P)
        r["_pw"] = sum(p for p, x in zip(ps, xs) if x > 0)
        up = sum(p * x for p, x in zip(ps, xs) if x > 0)
        dn = -sum(p * x for p, x in zip(ps, xs) if x < 0)
        r["_ratio"] = up / dn if dn > 0 else None
        if up == 0 or dn == 0:
            W(f"{rid}: every scenario moves the same way")
        r["_q"] = tilt(ps, xs) if len(ps) > 1 else None
        if r.get("now") and r.get("spread_duration"):
            r["_be"] = r["now"] * g["horizon_months"] / 12 / r["spread_duration"]
    groups = {}
    for r in g["rows"]:
        if r.get("parent"):
            groups.setdefault((r["parent"], r.get("group", "sector")), []).append(r)
    recon = []
    for (par, grp), kids in groups.items():
        if par not in rows:
            F(f"parent {par} of group {grp} is not a row")
            continue
        if any("weight" not in k for k in kids):
            W(f"{par}/{grp}: a row has no weight, reconciliation skipped")
            continue
        wt = sum(k["weight"] for k in kids)
        if abs(wt - 1) > 0.03:
            W(f"{par}/{grp}: weights sum to {wt:.2f}")
        base = rows[par].get("recon_tol_bp", 5)
        for sid in P:
            avg = sum(k["weight"] * k["_sdx"][sid] for k in kids) / wt
            tgt = rows[par]["_sdx"][sid]
            ok = abs(avg - tgt) <= max(base, 0.2 * abs(tgt))
            recon.append((par, grp, sid, tgt, avg, ok))
            if not ok:
                W(f"{par}/{grp} {sid}: children average {avg:+.0f}bp, parent says {tgt:+.0f}bp")
    g["_recon"] = recon
    for t in strings(g):
        m = TRADE.search(t)
        if m:
            F(f"trade word '{m.group(0)}' in text: \"{t[:70]}\"")
    return msgs


def relations(g):
    P = {s["id"]: s["p"] for s in g["spine"]}
    rows = {r["id"]: r for r in g["rows"]}
    out = []
    for rel in g.get("relations", []):
        a, b = rows.get(rel["a"]), rows.get(rel["b"])
        if not a or not b or a.get("now") is None or b.get("now") is None:
            continue
        op = (lambda x, y: x - y) if rel["op"] == "diff" else (lambda x, y: x / y)
        per = {k: op(a["now"] + a["_sdx"][k], b["now"] + b["_sdx"][k]) for k in P}
        out.append((rel, op(a["now"], b["now"]), per, sum(P[k] * per[k] for k in P)))
    return out


def render(g, msgs):
    sp = g["spine"]
    ids = [s["id"] for s in sp]
    bp = lambda x: f"{x:+.0f}"
    L = [f"# Credit scenario grid, as of {g['as_of']}", "",
         f"Horizon: {g['horizon']} ({g['horizon_months']} months). Moves are spread changes in basis points.",
         "", "**These are proposed scenarios, not engine output.** Probabilities are judgement unless marked "
         "`evidence_weighted`. This grid stops before trades.", ""]
    for key, title in (("findings", "Findings"), ("limits", "Limits")):
        if g.get(key):
            L += [f"## {title}", ""] + [f"{i}. {t}" for i, t in enumerate(g[key], 1)] + [""]
    L += ["## Spine: the shared macro scenarios", "",
          "Apply the tests in order. The first test that is true names the scenario.", "",
          "| Id | Scenario | Probability | Source | Test | Observable and threshold |", "|---|---|---|---|---|---|"]
    for s in sp:
        obs = " / ".join(f"{o['series']}: {o['threshold']}" for o in s["observables"])
        L.append(f"| {s['id']} | {s['name']} | {s['p']:.0%} | {s['p_source']} | {s['test']} | {obs} |")
    L += ["", "Evidence used for the probabilities:", ""]
    for s in sp:
        for e in s.get("evidence", []):
            L.append(f"- {s['id']}: {e}")
    L += ["", "## Summary: spread change by scenario", "",
          "| Row | Now | " + " | ".join(ids) + " | Expected | Chance wider | Wide/tight ratio |",
          "|---|---|" + "---|" * (len(ids) + 3)]
    for r in g["rows"]:
        now = f"{r['now']:.0f}" if r.get("now") is not None else "n/a"
        ratio = f"{r['_ratio']:.1f}" if r.get("_ratio") else "n/a"
        L.append(f"| {r['id']} | {now} | " + " | ".join(bp(r["_sdx"][k]) for k in ids)
                 + f" | {bp(r['_exp'])} | {r['_pw']:.0%} | {ratio} |")
    rel = relations(g)
    if rel:
        L += ["", "## Relations between rows", "",
              "| Relation | Now | " + " | ".join(ids) + " | Expected |", "|---|---|" + "---|" * (len(ids) + 1)]
        for d, now, per, ex in rel:
            fm = (lambda x: f"{x:.0f}") if d["op"] == "diff" else (lambda x: f"{x:.2f}")
            L.append(f"| {d['name']} | {fm(now)} | " + " | ".join(fm(per[k]) for k in ids) + f" | {fm(ex)} |")
    L += ["", "## Each row in detail", ""]
    for r in g["rows"]:
        L += [f"### {r['id']}", "", f"Axis: {r['axis']}. Driver: {r['driver']}", "",
              "| Scenario | Drawn from | Probability | Change | Level | Why | Own observable |", "|---|---|---|---|---|---|---|"]
        for s in r["scenarios"]:
            src = ", ".join(k if isinstance(f, (int, float)) or f["frac"] == 1 else f"{f['frac']:.0%} of {k}"
                            for k, f in s["from"].items())
            lvl = f"{r['now'] + s['_dx']:.0f}" if r.get("now") is not None else "n/a"
            L.append(f"| {s['name']} | {src} | {s['_p']:.0%} | {bp(s['_dx'])} | {lvl} | {s['why']} | {s.get('observable', 'spine test')} |")
        line = f"Expected change {bp(r['_exp'])}bp. Chance of wider spreads {r['_pw']:.0%}."
        if "_be" in r:
            line += f" Carry covers {r['_be']:.0f}bp of widening over the horizon."
        L += ["", line]
        if r.get("level") == "asset_class" and r.get("_q"):
            q = ", ".join(f"{s['name']} {qi:.0%} (mine {s['_p']:.0%})" for s, qi in zip(r["scenarios"], r["_q"]))
            L.append(f"Weights that make today's spread fair, given these outcomes: {q}.")
        L.append("")
    L += ["## Checks", ""]
    L += [f"- {lvl}: {m}" for lvl, m in msgs] or ["- All hard checks passed. No warnings."]
    if g.get("_recon"):
        bad = [x for x in g["_recon"] if not x[5]]
        L.append(f"- Reconciliation: {len(g['_recon']) - len(bad)} of {len(g['_recon'])} parent-versus-children tests inside tolerance.")
    if g.get("calibration"):
        L += ["", "## Calibration anchors (case memory, used only for magnitudes)", ""] + [f"- {c}" for c in g["calibration"]]
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("grid")
    ap.add_argument("--md")
    a = ap.parse_args()
    g = json.load(open(a.grid))
    msgs = check(g)
    for lvl, m in msgs:
        print(f"{lvl}: {m}")
    failed = any(l == "FAIL" for l, _ in msgs)
    if not failed:
        print(f"OK: {len(g['rows'])} rows, {sum(len(r['scenarios']) for r in g['rows'])} scenarios, "
              f"{sum(1 for l, _ in msgs if l == 'WARN')} warnings")
        if a.md:
            open(a.md, "w").write(render(g, msgs))
            print(f"wrote {a.md}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
