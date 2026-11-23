#!/usr/bin/env python3
"""Build the one-page view of a credit thesis run. Standard library only.

Usage:
  build_view.py <run_dir> <out.html>   write the page
  build_view.py --check <run_dir>      validate the inputs, print PASS or FAIL, exit 0 or 1

Inputs in <run_dir>:
  readings.json        market readings (fred_pull.py)
  scenarios.json       the scenario grid. The grid script computes every probability and expected move.
  report.md            the grid report. The check compares the chart numbers with it.
  view.json            the text that only the analysis can supply. Schema: view_schema.md
  readings_month.json  optional. Used for the one-month move when readings.json has no month_before.

Every number on the page comes from readings.json, scenarios.json or the grid script.
A missing or invalid view.json does not stop the build. The page then shows the data-driven
diagrams and one line that says the text sections were not updated.
"""
import datetime
import html
import importlib.util
import json
import math
import os
import re
import sys

GRID_SCRIPT = os.environ.get(
    "SCENARIO_GRID_SCRIPT", "/home/ak/.agents/skills/credit-scenario-grid/scripts/scenario_grid.py")
LH = 17
SPREADS = ("IG", "AAA", "AA", "A", "BBB", "HY", "BB", "B", "CCC")
RATES = ("fed_upper", "ust2y", "ust10y", "breakeven10y")
AXIS = "axis_AA_over_BBB"
MON = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
WORDS = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
         10: "ten", 11: "eleven", 12: "twelve"}
SRC_LABEL = {"PM_assumption": "PM assumption", "evidence_weighted": "evidence weighted"}
STATUS = {"not_triggered": ("Not triggered", ""), "close": ("Close", " chip-close"),
          "triggered": ("TRIGGERED", " chip-trig")}
DEST_STATUS = {"priced": "priced", "repriced": "repriced", "not_priced": "notp"}
TRADE = re.compile(r"\b(hedge ratio|notional|position size|stop[- ]loss|dv01|entry level|exit level|go long|go short)\b", re.I)
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[A-Za-z]{2,}")
TOKEN = re.compile(r"\{([A-Za-z0-9_]+)\}")


class InputError(Exception):
    pass


# ---------------------------------------------------------------- small helpers
def esc(s):
    return html.escape(str(s), quote=True)


def day(iso, year=False):
    d = datetime.date.fromisoformat(iso)
    return f"{d.day} {MON[d.month - 1]}" + (f" {d.year}" if year else "")


def word(n):
    return WORDS.get(n, str(n))


def ordinal(n):
    n = int(n)
    suf = "th" if 10 <= n % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suf}"


def signed(v, nd=0, unit=""):
    """+19bp, −3bp, 0bp. A real minus sign, and no sign on zero."""
    r = round(v, nd)
    if r == 0:
        return f"{0:.{nd}f}{unit}"
    return ("+" if r > 0 else "−") + f"{abs(r):,.{nd}f}{unit}"


def bp(v):
    return f"{v:,.0f}bp"


def share_words(x):
    for f, w in ((0.25, "a quarter"), (1 / 3, "one third"), (0.5, "half"), (2 / 3, "two thirds"), (0.75, "three quarters")):
        if abs(x - f) <= 0.03:
            return "about " + w
    return f"{x:.0%}"


def wrap(s, n):
    out, cur = [], ""
    for w in str(s).split():
        if cur and len(cur) + 1 + len(w) > n:
            out.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    out = out + [cur] if cur else out
    if len(out) == 2:  # balance two lines, so that neither ends on a stray word
        ws, best = str(s).split(), None
        for i in range(1, len(ws)):
            a, b = " ".join(ws[:i]), " ".join(ws[i:])
            if len(a) <= n and len(b) <= n and (best is None or max(len(a), len(b)) < max(map(len, best))):
                best = [a, b]
        out = best or out
    return out


# ---------------------------------------------------------------- svg helpers
def T(x, y, s, cls="t", anchor="start", lh=LH):
    lines = s if isinstance(s, list) else [s]
    return "".join(
        f'<text x="{x:.1f}" y="{y + i * lh:.1f}" class="{cls}" text-anchor="{anchor}">{esc(l)}</text>'
        for i, l in enumerate(lines))


def arrow(x1, y1, x2, y2, cls="ln"):
    a = math.atan2(y2 - y1, x2 - x1)
    L, w = 8, 4
    bx, by = x2 - L * math.cos(a), y2 - L * math.sin(a)
    p1 = (bx - w * math.sin(a), by + w * math.cos(a))
    p2 = (bx + w * math.sin(a), by - w * math.cos(a))
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{bx:.1f}" y2="{by:.1f}" class="{cls}"/>'
            f'<polygon points="{x2:.1f},{y2:.1f} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" class="ah"/>')


def rect(x, y, w, h, cls="box", rx=0, tip=""):
    t = f"<title>{esc(tip)}</title>" if tip else ""
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{max(w, 0):.1f}" height="{h:.1f}" rx="{rx}" class="{cls}">{t}</rect>'


def line(x1, y1, x2, y2, cls="ln"):
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="{cls}"/>'


def svg(W, H, body, label, mode):
    # One element per line, so that a reader with a line limit can read the file in parts.
    body = body.replace("/><", "/>\n<").replace("</text><", "</text>\n<").replace("</rect><", "</rect>\n<")
    return (f'<svg class="dg dg-{mode}" viewBox="0 0 {W} {H:.0f}" role="img" aria-label="{esc(label)}" '
            f'preserveAspectRatio="xMidYMid meet">\n{body}\n</svg>\n')


def both(fn, label, *a):
    return fn(720, label, "wide", *a) + fn(358, label, "narrow", *a)


# ---------------------------------------------------------------- data
def load_json(path):
    with open(path) as f:
        return json.load(f)


def load_data(run):
    """Readings, the grid as the grid script computes it, and the derived numbers."""
    D = {"run": run}
    name = os.path.basename(os.path.normpath(run))
    try:
        R = load_json(os.path.join(run, "readings.json"))
    except (OSError, ValueError) as e:
        raise InputError(f"readings.json: {e}")
    try:
        g = load_json(os.path.join(run, "scenarios.json"))
    except (OSError, ValueError) as e:
        raise InputError(f"scenarios.json: {e}")
    try:
        spec = importlib.util.spec_from_file_location("scenario_grid", GRID_SCRIPT)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    except Exception as e:
        raise InputError(f"cannot load the grid script {GRID_SCRIPT}: {e}")
    msgs = mod.check(g)
    fails = [m for l, m in msgs if l == "FAIL"]
    if fails:
        raise InputError("scenarios.json fails the grid script: " + " / ".join(fails[:3]))
    for k in ("IG", "HY", AXIS):
        if not isinstance(R.get(k), dict) or "value" not in R[k]:
            raise InputError(f"readings.json has no '{k}' reading")
    try:
        RM = load_json(os.path.join(run, "readings_month.json"))
    except (OSError, ValueError):
        RM = {}
    rows = {r["id"]: r for r in g["rows"]}
    for k in ("IG", "HY"):
        if k not in rows:
            raise InputError(f"scenarios.json has no '{k}' row")
    D.update(R=R, RM=RM, g=g, rows=rows, spine=g["spine"], ids=[s["id"] for s in g["spine"]],
             P={s["id"]: s["p"] for s in g["spine"]}, rel=mod.relations(g), mod=mod,
             date=name if re.fullmatch(r"\d{4}-\d{2}-\d{2}", name) else g["as_of"], dirname=name)
    D["ratio_rel"] = next((x for x in D["rel"] if x[0]["op"] == "ratio" and x[0]["a"].endswith("AA")
                           and x[0]["b"].endswith("BBB")), None)
    return D


def month_move(D, key):
    """(move, from date, to date) for one reading, or None. Prefers readings.json."""
    for src in (D["R"], D["RM"]):
        r = src.get(key)
        if isinstance(r, dict) and r.get("month_before") is not None and r.get("month_before_date"):
            return r["value"] - r["month_before"], r["month_before_date"], r["date"]
    return None


def tokens(D):
    R, t = D["R"], {}
    for k in SPREADS:
        r = R.get(k)
        if not isinstance(r, dict):
            continue
        ch = r["value"] - r["two_days_before"]
        t[k] = bp(r["value"])
        t[k + "_date"] = day(r["date"])
        t[k + "_pctile"] = ordinal(r["percentile_3y"])
        t[k + "_chg2d"] = "unchanged" if round(ch) == 0 else f"{'up' if ch > 0 else 'down'} {abs(ch):,.0f}bp"
    a = R[AXIS]
    t.update(axis=f"{a['value']:.3f}", axis_date=day(a["date"]), axis_pctile=ordinal(a["percentile_3y"]),
             axis_min=f"{a['min_3y']:.3f}", axis_max=f"{a['max_3y']:.3f}")
    if "mean_3y" in a:
        t.update(axis_mean=f"{a['mean_3y']:.3f}", axis_z=f"{abs(a['z_3y']):.2f}")
    for k in RATES:
        if isinstance(R.get(k), dict):
            t[k] = f"{R[k]['value']:.2f}%"
    if isinstance(R.get("vix"), dict):
        t["vix"] = f"{R['vix']['value']:.2f}"
    t.update(print_date=day(R["IG"]["date"]), run_date=D["date"], horizon=D["g"]["horizon"],
             grid_rows=str(len(D["g"]["rows"])), grid_scenarios=str(sum(len(r["scenarios"]) for r in D["g"]["rows"])))
    for sid in D["ids"]:
        t["p_" + sid] = f"{D['P'][sid]:.0%}"
        if D["ratio_rel"]:
            t["ratio_" + sid] = f"{D['ratio_rel'][2][sid]:.2f}"
    for k in ("IG", "HY"):
        t["exp_" + k] = signed(D["rows"][k]["_exp"], 0, "bp")
        if "_be" in D["rows"][k]:
            t["carry_" + k] = bp(D["rows"][k]["_be"])
    return t


def fill(s, tok, missing=None):
    def sub(m):
        if m.group(1) in tok:
            return tok[m.group(1)]
        if missing is not None:
            missing.append(m.group(1))
        return m.group(0)
    return TOKEN.sub(sub, str(s))


def fill_all(o, tok, missing):
    if isinstance(o, str):
        return fill(o, tok, missing)
    if isinstance(o, list):
        return [fill_all(x, tok, missing) for x in o]
    if isinstance(o, dict):
        return {k: fill_all(x, tok, missing) for k, x in o.items()}
    return o


# ---------------------------------------------------------------- view.json validation
def sentences(s):
    return [x for x in re.split(r"(?<=[.!?])\s+(?=[A-Z\"“@$\d])", s) if x.strip()]


def validate_view(v, D, tok):
    """Return (errors, warnings). Errors make the view unusable."""
    E, Wn = [], []
    if not isinstance(v, dict):
        return ["view.json is not a JSON object"], Wn

    def need(o, path, key, typ=str, maxlen=None, opt=False):
        x = o.get(key) if isinstance(o, dict) else None
        if x is None:
            if not opt:
                E.append(f"{path}.{key} is missing")
            return None
        if not isinstance(x, typ) or (typ is str and not x.strip()):
            E.append(f"{path}.{key} must be a non-empty {typ.__name__}")
            return None
        if maxlen and typ is str and len(fill(x, tok)) > maxlen:
            E.append(f"{path}.{key} is {len(fill(x, tok))} characters after tokens, the limit is {maxlen}: \"{x[:50]}\"")
        return x

    def lines(x, path, n, k):
        if x and len(wrap(fill(x, tok), n)) > k:
            E.append(f"{path} needs more than {k} lines of {n} characters. Shorten it: \"{x[:50]}\"")

    if v.get("run_date") not in (None, D["date"]):
        E.append(f"run_date is {v.get('run_date')}, the run is {D['date']}")
    need(v, "view", "question", opt=True, maxlen=90)
    s = need(v, "view", "view", maxlen=200)
    if s and len(fill(s, tok).split()) > 25:
        E.append(f"view.view has {len(fill(s, tok).split())} words, the limit is 25")
    need(v, "view", "lede", maxlen=320)
    need(v, "view", "limits", maxlen=420)

    c = need(v, "view", "chain", dict) or {}
    for k in ("source", "supply"):
        b = need(c, "chain", k, dict) or {}
        need(b, f"chain.{k}", "title", maxlen=24)
        lines(need(b, f"chain.{k}", "detail", maxlen=68), f"chain.{k}.detail", 34, 2)
        need(b, f"chain.{k}", "detail_short", maxlen=52)
    need(c, "chain", "verb", maxlen=10)
    need(c, "chain", "caption", maxlen=220)
    need(c, "chain", "note", maxlen=420)
    ds = need(c, "chain", "destinations", list) or []
    if ds and not 3 <= len(ds) <= 5:
        E.append(f"chain.destinations has {len(ds)} items, need 3 to 5")
    nch = int((720 - 9 * (max(len(ds), 3) - 1)) / max(len(ds), 3) / 7.6)
    for i, d in enumerate(ds):
        p = f"chain.destinations[{i}]"
        lines(need(d, p, "name", maxlen=28), p + ".name", nch, 2)
        lines(need(d, p, "shows_in", maxlen=44), p + ".shows_in", nch + 2, 2)
        if (d.get("status") if isinstance(d, dict) else None) not in DEST_STATUS:
            E.append(f"{p}.status must be one of {sorted(DEST_STATUS)}")
        need(d, p, "status_text", maxlen=13)
        need(d, p, "status_sub", maxlen=17)

    a = need(v, "view", "axis", dict) or {}
    need(a, "axis", "caption", maxlen=220)
    need(a, "axis", "note", maxlen=220, opt=True)

    sc = need(v, "view", "scenarios", dict, opt=True) or {}
    for k, lim in (("labels", 34), ("short", 13)):
        m = sc.get(k, {})
        if not isinstance(m, dict):
            E.append(f"scenarios.{k} must be an object")
            continue
        for sid, name in m.items():
            if sid not in D["P"]:
                E.append(f"scenarios.{k} names '{sid}', which is not a spine id")
            elif not isinstance(name, str) or not name or len(name) > lim:
                E.append(f"scenarios.{k}.{sid} must be text of at most {lim} characters")
    need(sc, "scenarios", "note", maxlen=220, opt=True)

    f = need(v, "view", "falsifiers", dict) or {}
    items = need(f, "falsifiers", "items", list) or []
    if items and not 1 <= len(items) <= 6:
        E.append(f"falsifiers.items has {len(items)} items, need 1 to 6")
    for i, x in enumerate(items):
        p = f"falsifiers.items[{i}]"
        need(x, p, "id", maxlen=4)
        need(x, p, "claim", maxlen=70)
        need(x, p, "observable", maxlen=90)
        need(x, p, "threshold", maxlen=170)
        need(x, p, "today", maxlen=150)
        if (x.get("status") if isinstance(x, dict) else None) not in STATUS:
            E.append(f"{p}.status must be one of {sorted(STATUS)}")
        m = x.get("meter") if isinstance(x, dict) else None
        if m is not None:
            if not isinstance(m, dict) or m.get("side") not in ("above", "below") \
                    or not isinstance(m.get("threshold"), (int, float)) or isinstance(m.get("threshold"), bool):
                E.append(f"{p}.meter needs reading, a numeric threshold and side 'above' or 'below'")
            elif m.get("reading") != "axis" and m.get("reading") not in SPREADS:
                E.append(f"{p}.meter.reading must be 'axis' or one of {list(SPREADS)}")
            elif m["reading"] != "axis" and not isinstance(D["R"].get(m["reading"]), dict):
                E.append(f"{p}.meter.reading '{m['reading']}' is not in readings.json")
    need(f, "falsifiers", "note", maxlen=220, opt=True)

    dg = need(v, "view", "disagreements", dict) or {}
    groups = need(dg, "disagreements", "groups", list) or []
    for gi, grp in enumerate(groups):
        p = f"disagreements.groups[{gi}]"
        need(grp, p, "title", maxlen=60)
        its = need(grp, p, "items", list) or []
        for i, x in enumerate(its):
            q = f"{p}.items[{i}]"
            need(x, q, "question", maxlen=90)
            for k in ("a_who", "b_who"):
                need(x, q, k, maxlen=60)
            for k in ("a", "b"):
                need(x, q, k, maxlen=200)
            need(x, q, "why", maxlen=200, opt=True)

    at = need(v, "view", "attention", dict) or {}
    bx = need(at, "attention", "boxes", dict) or {}
    for k in bx:
        if k not in ("strong_quiet", "strong_crowded", "thin_quiet", "thin_crowded"):
            E.append(f"attention.boxes has an unknown key '{k}'")
        elif bx[k] is not None:
            p = f"attention.boxes.{k}"
            lines(need(bx[k], p, "title", maxlen=44), p + ".title", 22, 2)
            lines(need(bx[k], p, "text", maxlen=48), p + ".text", 24, 2)
            need(bx[k], p, "trend", maxlen=28, opt=True)
    need(at, "attention", "caption", maxlen=220)
    need(at, "attention", "note", maxlen=220, opt=True)

    pl = need(v, "view", "pipeline", dict) or {}
    for k, lo, hi in (("inputs", 1, 4), ("stages", 2, 4)):
        its = need(pl, "pipeline", k, list) or []
        if its and not lo <= len(its) <= hi:
            E.append(f"pipeline.{k} has {len(its)} items, need {lo} to {hi}")
        for i, x in enumerate(its):
            p = f"pipeline.{k}[{i}]"
            need(x, p, "title", maxlen=16)
            sub = need(x, p, "text", maxlen=22 if k == "inputs" else 34)
            if sub and k == "stages" and any(len(part) > 17 for part in stage_lines(fill(sub, tok))):
                E.append(f"{p}.text: each part between commas must be at most 17 characters")

    # rules for every string
    missing, flat = [], []

    def walk(o, path):
        if isinstance(o, str):
            flat.append((path, o))
        elif isinstance(o, list):
            for i, x in enumerate(o):
                walk(x, f"{path}[{i}]")
        elif isinstance(o, dict):
            for k, x in o.items():
                walk(x, f"{path}.{k}" if path else k)
    walk(v, "")
    values = {tok[k] for k in ("IG", "HY", "CCC", "axis") if k in tok}
    for path, raw in flat:
        s = fill(raw, tok, missing)
        if ";" in s or "—" in s:
            E.append(f"{path}: no semicolons and no em dashes")
        if "<" in s or ">" in s:
            E.append(f"{path}: no angle brackets. Text is plain, not HTML")
        if EMAIL.search(s):
            E.append(f"{path}: contains an email address")
        m = TRADE.search(s)
        if m:
            E.append(f"{path}: trade word '{m.group(0)}'. This page is research only")
        for sen in sentences(s):
            if len(sen.split()) > 25:
                E.append(f"{path}: a sentence has {len(sen.split())} words, the limit is 25: \"{sen[:60]}\"")
        for val in values:
            if re.search(r"(?<![\d.,])" + re.escape(val) + r"(?![\d])", raw):
                Wn.append(f"{path}: the market reading {val} is typed in. Use a token, so that it follows readings.json")
    for m in sorted(set(missing)):
        E.append(f"unknown token {{{m}}}. Allowed tokens are listed in view_schema.md")
    return E, Wn


def load_view(D, tok):
    """Return (view with tokens filled, or None; errors; warnings)."""
    path = os.path.join(D["run"], "view.json")
    try:
        v = load_json(path)
    except OSError:
        return None, ["view.json is missing"], []
    except ValueError as e:
        return None, [f"view.json is not valid JSON: {e}"], []
    E, Wn = validate_view(v, D, tok)
    if E:
        return None, E, Wn
    return fill_all(v, tok, []), [], Wn


def report_check(D):
    """Compare the numbers the page uses with report.md. Return a list of mismatches."""
    try:
        text = open(os.path.join(D["run"], "report.md")).read()
    except OSError as e:
        return [f"report.md: {e}"]
    cells = {}
    for ln in text.splitlines():
        if ln.startswith("| "):
            c = [x.strip() for x in ln.strip().strip("|").split("|")]
            cells.setdefault(c[0], c)
    bad, n = [], len(D["ids"])
    for rid in ("IG", "HY", "IG.AA", "IG.BBB", "HY.CCC"):
        r = D["rows"].get(rid)
        if not r:
            continue
        c = cells.get(rid)
        if not c or len(c) < n + 3:
            bad.append(f"report.md has no summary line for {rid}")
            continue
        mine = [f"{r['_sdx'][k]:+.0f}" for k in D["ids"]] + [f"{r['_exp']:+.0f}"]
        if mine != c[2:n + 3]:
            bad.append(f"{rid}: the grid script gives {mine}, report.md says {c[2:n + 3]}")
    if D["ratio_rel"]:
        d, now, per, ex = D["ratio_rel"]
        c = cells.get(d["name"])
        mine = [f"{now:.2f}"] + [f"{per[k]:.2f}" for k in D["ids"]] + [f"{ex:.2f}"]
        if not c or mine != c[1:n + 3]:
            bad.append(f"{d['name']}: the grid script gives {mine}, report.md says {c[1:n + 3] if c else 'nothing'}")
    return bad


# ---------------------------------------------------------------- diagram: flow
def flow(W, label, mode, c):
    ds = c["destinations"]
    n = len(ds)
    b = ""
    if mode == "wide":
        b += rect(70, 1, 250, 80) + T(86, 25, c["source"]["title"], "t tb")
        b += T(86, 47, wrap(c["source"]["detail"], 34), "ts tmu")
        b += arrow(320, 41, 400, 41) + T(360, 33, c["verb"], "tm", "middle")
        b += rect(400, 1, 250, 80) + T(416, 25, c["supply"]["title"], "t tb")
        b += T(416, 47, wrap(c["supply"]["detail"], 34), "ts tmu")
        gap = 9
        cw = (720 - gap * (n - 1)) / n
        nch = int(cw / 7.6)
        cx = [i * (cw + gap) + cw / 2 for i in range(n)]
        b += line(525, 81, 525, 112) + line(cx[0], 112, max(cx[-1], 525), 112)
        b += T(cx[0] + 10, 104, "WHERE THE DEBT GOES", "tm")
        for i, d in enumerate(ds):
            x = i * (cw + gap)
            b += arrow(cx[i], 112, cx[i], 136)
            b += rect(x, 136, cw, 150)
            b += T(x + 10, 160, wrap(d["name"], nch), "t tb")
            b += line(x, 198, x + cw, 198, "hair")
            b += T(x + 10, 218, "SHOWS IN", "tm")
            b += T(x + 10, 238, wrap(d["shows_in"], nch + 2), "ts")
            b += rect(x, 294, cw, 50, "st-" + DEST_STATUS[d["status"]], 4)
            b += T(x + cw / 2, 315, d["status_text"], "t tb", "middle") + T(x + cw / 2, 332, d["status_sub"], "ts", "middle")
        H = 346
    else:
        b += rect(1, 1, 356, 62) + T(14, 24, c["source"]["title"], "t tb")
        b += T(14, 45, c["source"]["detail_short"], "ts tmu")
        b += arrow(40, 63, 40, 93) + T(52, 83, c["verb"], "tm")
        b += rect(1, 93, 356, 62) + T(14, 116, c["supply"]["title"], "t tb")
        b += T(14, 137, c["supply"]["detail_short"], "ts tmu")
        y0, rh, gap = 190, 88, 10
        last_mid = y0 + (n - 1) * (rh + gap) + rh / 2
        b += line(14, 155, 14, last_mid) + T(30, 177, "WHERE THE DEBT GOES", "tm")
        for i, d in enumerate(ds):
            y = y0 + i * (rh + gap)
            b += arrow(14, y + rh / 2, 30, y + rh / 2)
            b += rect(30, y, 327, rh)
            b += T(42, y + 23, d["name"], "t tb")
            b += T(42, y + 43, "SHOWS IN", "tm")
            b += T(42, y + 61, wrap(d["shows_in"], 30), "ts", lh=16)
            b += rect(240, y + 18, 108, 52, "st-" + DEST_STATUS[d["status"]], 4)
            b += T(294, y + 40, d["status_text"], "t tb", "middle") + T(294, y + 57, d["status_sub"], "ts", "middle")
        H = y0 + n * (rh + gap) - gap + 2
    return svg(W, H, b, label, mode)


# ---------------------------------------------------------------- diagram: axis gauge
def axis_domain(D, thr=None):
    a = D["R"][AXIS]
    vals = [a["min_3y"], a["max_3y"], a["value"]] + ([thr] if thr is not None else [])
    if D["ratio_rel"]:
        vals += list(D["ratio_rel"][2].values())
    return math.floor((min(vals) - 0.015) * 50) / 50, math.ceil((max(vals) + 0.015) * 50) / 50


def axis_falsifier(view):
    for x in (view or {}).get("falsifiers", {}).get("items", []):
        m = x.get("meter")
        if m and m.get("reading") == "axis":
            return x["id"], m["threshold"], m["side"]
    return None


def short_name(D, view, sid):
    return ((view or {}).get("scenarios", {}).get("short", {}).get(sid)) or f"Scenario {D['ids'].index(sid) + 1}"


def gauge(W, label, mode, D, view):
    a = D["R"][AXIS]
    fz = axis_falsifier(view)
    lo, hi = axis_domain(D, fz[1] if fz else None)
    X = lambda v: 18 + (v - lo) / (hi - lo) * (W - 36)
    b = ""
    xt, xmin, xmax = X(a["value"]), X(a["min_3y"]), X(a["max_3y"])
    b += rect(xmin, 68, xmax - xmin, 16, "range")
    if fz:
        xthr = X(fz[1])
        if fz[2] == "below":
            b += rect(X(lo), 86, xthr - X(lo), 5, "zone")
        else:
            b += rect(xthr, 86, X(hi) - xthr, 5, "zone")
    b += line(X(lo), 76, X(hi), 76, "hair")
    if "mean_3y" in a:
        xmean = X(a["mean_3y"])
        b += line(xmean, 64, xmean, 88, "lnm") + T(xmean, 58, f"mean {a['mean_3y']:.3f}", "tm", "middle")
    if fz:
        b += line(xthr, 56, xthr, 136, "thr") + line(xthr, 172, xthr, 198, "thr")
        left = xthr > W * 0.45
        b += T(xthr - 8 if left else xthr + 8, 128, f"{fz[0]} triggers {fz[2]} {fz[1]:.2f}", "t tb", "end" if left else "start")
    b += line(xt, 44, xt, 90, "tod") + line(xt, 172, xt, 198, "tod")
    b += f'<circle cx="{xt:.1f}" cy="76" r="6.5" class="dot-today"/>'
    tx, anchor = xt, "middle"
    if xt + 100 > W:
        tx, anchor = W - 2, "end"
    elif xt < 100:
        tx, anchor = 2, "start"
    b += T(tx, 18, f"Today {a['value']:.3f}", "tl", anchor)
    b += T(tx, 36, f"{ordinal(a['percentile_3y'])} percentile of three years", "ts tmu", anchor)
    b += T(xmin, 104, f"low {a['min_3y']:.3f}", "tm", "middle")
    peak = f"peak {a['max_3y']:.3f}"
    if mode == "wide" and a.get("max_date"):
        peak += f" on {day(a['max_date'], True)}"
    b += T(xmax, 104, peak, "tm", "middle")
    if D["ratio_rel"]:
        b += T(X(lo), 162, f"{word(D['g']['horizon_months']).upper()}-MONTH RATIO IN EACH SCENARIO, PROPOSALS", "tm")
        b += line(X(lo), 190, X(hi), 190, "ln")
        per = D["ratio_rel"][2]
        for row, sid in enumerate(sorted(per, key=per.get)):
            v, x = per[sid], X(per[sid])
            ty = 216 if row % 2 == 0 else 254
            if row % 2:
                b += line(x, 196, x, 240, "lnm")
            b += f'<circle cx="{x:.1f}" cy="190" r="5" class="dot"/>'
            anchor, tx = "middle", x
            if x + 42 > W:
                anchor, tx = "end", W - 2
            elif x < 42:
                anchor, tx = "start", 2
            b += T(tx, ty, short_name(D, view, sid), "ts tb", anchor) + T(tx, ty + 16, f"{v:.2f}, {D['P'][sid]:.0%}", "tm", anchor)
    return svg(W, 280 if D["ratio_rel"] else 112, b, label, mode)


# ---------------------------------------------------------------- diagram: scenario bar
def tail(D):
    """The two least likely scenarios: (positions, total probability, share of the expected IG move or None)."""
    order = sorted(range(len(D["ids"])), key=lambda i: D["P"][D["ids"][i]])[:2]
    ig = D["rows"]["IG"]
    p = sum(D["P"][D["ids"][i]] for i in order)
    part = sum(D["P"][D["ids"][i]] * ig["_sdx"][D["ids"][i]] for i in order)
    share = part / ig["_exp"] if ig["_exp"] > 0 and part > 0 else None
    return sorted(order), p, share


def scenbar(W, label, mode, D):
    b = T(0, 12, f"PROPOSALS, {word(D['g']['horizon_months']).upper()} MONTHS TO {D['g']['horizon']}", "tm")
    n = len(D["ids"])
    gap = 2
    avail = W - gap * (n - 1)
    x, xs = 0, []
    for i, sid in enumerate(D["ids"]):
        p = D["P"][sid]
        w = avail * p
        xs.append((x, w))
        b += rect(x, 42, w, 44, f"s{i + 1}", 4, f"Scenario {i + 1}: {p:.0%}")
        b += T(x + w / 2, 34, str(i + 1), "tm", "middle")
        if w >= 22:
            b += T(x + w / 2, 69, f"{p:.0%}", f"t tb s{i + 1}t", "middle")
        x += w + gap
    order, p, share = tail(D)
    if order[1] - order[0] == 1:
        bx0, bx1 = xs[order[0]][0], xs[order[1]][0] + xs[order[1]][1]
        b += f'<path d="M{bx0:.1f} 92 V98 H{bx1:.1f} V92" class="ln"/>'
    note = [f"The two tail scenarios hold {p:.0%} of the probability"]
    if share is not None:
        note.append(f"and {share_words(share)} of the expected IG move")
    b += T(W, 118, note, "ts", "end")
    return svg(W, 142, b, label, mode)


# ---------------------------------------------------------------- diagram: expected move against the last month
def ev_rows(D):
    """Three groups of rows. Each row: name, now label, month move, expected move, scenario parts."""
    R, out = D["R"], {"index": [], "ratio": [], "tiers": []}

    def spread_row(rid, key, name):
        r = D["rows"][rid]
        return dict(key=key, name=name, now=f"{bp(R[key]['value'])} on {day(R[key]['date'])}", month=month_move(D, key),
                    exp=r["_exp"], parts=[D["P"][k] * r["_sdx"][k] for k in D["ids"]], nd=0, unit="bp")
    out["index"] = [spread_row("IG", "IG", "IG index spread"), spread_row("HY", "HY", "HY index spread")]
    if D["ratio_rel"]:
        d, now, per, ex = D["ratio_rel"]
        a = R[AXIS]
        out["ratio"] = [dict(key=AXIS, name="AA to BBB ratio, the axis", now=f"{a['value']:.3f} on {day(a['date'])}",
                             month=month_move(D, AXIS), exp=ex - now, parts=[D["P"][k] * (per[k] - now) for k in D["ids"]],
                             nd=3, unit="", level=ex)]
    tiers = [("IG.AA", "AA", "AA spread"), ("IG.BBB", "BBB", "BBB spread"), ("HY.CCC", "CCC", "CCC spread")]
    if all(rid in D["rows"] and isinstance(R.get(k), dict) for rid, k, _ in tiers):
        out["tiers"] = [spread_row(*t) for t in tiers]
    return out


def evgroup(W, mode, title, rows, words, label, compact=False):
    wide = mode == "wide"
    x0, x1 = (150, W - 132) if wide else (2, W - 2)
    lo = hi = 0.0
    for r in rows:
        pos = sum(v for v in r["parts"] if v > 0)
        neg = sum(v for v in r["parts"] if v < 0)
        vals = [pos, neg, r["exp"]] + ([r["month"][0]] if r["month"] else [])
        lo, hi = min(lo, *vals), max(hi, *vals)
    if hi <= 0:
        hi = -lo * 0.25 or 1.0
    room = 0.16 if wide else 0.24  # the zero line never sits closer than this to the left edge
    lo = min(lo, -room * hi / (1 - room))
    X = lambda v: x0 + (v - lo) / (hi - lo) * (x1 - x0)
    Z = X(0)
    bh, sh = (10, 14) if compact else (14, 18)
    b = T(0, 12, title, "tm")
    b += T(Z - 8, 32, "← " + words[0], "tm", "end") + T(Z + 8, 32, words[1] + " →", "tm")
    y = 42

    def fm(r, v):
        return signed(v, r["nd"], r["unit"])

    def bar(r, y, lab, v, cls, txt, tip):
        nonlocal b
        if wide:
            b += T(x0 - 12, y + bh / 2 + 4, lab, "tm", "end")
            if v is None:
                b += T(Z + 8, y + bh / 2 + 4, "no data", "ts tmu")
            else:
                b += rect(min(X(v), Z), y, max(abs(X(v) - Z), 1.5), bh, cls, 2, tip)
                b += (f'<text x="{max(X(v), Z) + 8:.1f}" y="{y + bh / 2 + 4:.1f}"><tspan class="t tb">{esc(fm(r, v))}</tspan>'
                      f'<tspan class="ts tmu" dx="6">{esc(txt)}</tspan></text>')
            return y + bh + 10
        b += T(0, y + 11, lab, "tm")
        if v is None:
            b += T(W, y + 11, "no data", "ts tmu", "end")
        else:
            b += (f'<text x="{W}" y="{y + 11}" text-anchor="end"><tspan class="ts tmu">{esc(txt)}</tspan>'
                  f'<tspan class="t tb" dx="6">{esc(fm(r, v))}</tspan></text>')
            b += rect(min(X(v), Z), y + 18, max(abs(X(v) - Z), 1.5), bh, cls, 2, tip)
        b += line(Z, y + 15, Z, y + 21 + bh, "ln")
        return y + 18 + bh + 10

    for r in rows:
        b += f'<text x="0" y="{y + 14}"><tspan class="t tb">{esc(r["name"])}</tspan><tspan class="ts tmu" dx="10">{esc(r["now"])}</tspan></text>'
        y += 26
        top = y - 4
        m = r["month"]
        y = bar(r, y, "Last month", m[0] if m else None, "mo", f"{day(m[1])} to {day(m[2])}" if m else "",
                f"{r['name']}: {fm(r, m[0])} from {day(m[1])} to {day(m[2])}" if m else "")
        y = bar(r, y, "Expected, 6 months", r["exp"], "ex", "proposal", f"{r['name']}: expected move {fm(r, r['exp'])}, a proposal")
        if wide:
            b += T(x0 - 12, y + sh / 2 + 4, "By scenario", "tm", "end")
        else:
            b += T(0, y + 11, "By scenario, probability times move", "tm")
            y += 18
        xp = xn = Z
        for i, v in enumerate(r["parts"]):
            w = abs(X(v) - Z)
            if w < 0.3:
                continue
            xa = xp if v > 0 else xn - w
            if v > 0:
                xp += w
            else:
                xn -= w
            g = 2 if w > 4 else 0
            b += rect(xa + (g if v > 0 else 0), y, w - g, sh, f"seg s{i + 1}", 2, f"Scenario {i + 1}: {fm(r, v)}")
            if w - g >= 15:
                b += T(xa + (g if v > 0 else 0) + (w - g) / 2, y + sh / 2 + 4, str(i + 1), f"tm s{i + 1}t", "middle")
        y += sh
        b += line(Z, top if wide else y - sh - 3, Z, y + 4, "ln")
        y += 20
        kx, step = (x0, (W - x0) / len(r["parts"])) if wide else (0, W / len(r["parts"]))
        for i, v in enumerate(r["parts"]):
            b += rect(kx + i * step, y - 10, 10, 10, f"seg s{i + 1}", 2)
            b += (f'<text x="{kx + i * step + 14:.1f}" y="{y}"><tspan class="tm">{i + 1}</tspan>'
                  f'<tspan class="ts" dx="5">{esc(fm(r, v))}</tspan></text>')
        y += 26
    return svg(W, y - 14, b, label, mode)


def ev_caption(G):
    ig, hy = G["index"]
    if not ig["month"] or not hy["month"]:
        return "The chart has no one-month data in this run, so it shows only the expected six-month moves and their scenario parts."

    def relation(r):
        e, m = r["exp"], r["month"][0]
        if round(m) != 0 and round(e) != 0 and (e > 0) != (m > 0):
            return "opposite"
        return "larger than" if abs(round(e)) > abs(round(m)) else "smaller than" if abs(round(e)) < abs(round(m)) else "equal to"
    a, c = relation(ig), relation(hy)
    top = sorted(range(len(ig["parts"])), key=lambda i: -abs(ig["parts"][i]))[:2]
    lead = f"scenarios {min(top) + 1} and {max(top) + 1} add the most to IG"
    if "opposite" in (a, c):
        who = "IG and HY" if a == c else "IG" if a == "opposite" else "HY"
        return f"For {who} the expected six-month move points the other way from last month's move, and {lead}."
    if a == c:
        return f"For IG and HY the expected six-month move is {a} last month's move, and {lead}."
    return f"The expected six-month move is {a} last month's move for IG and {c} it for HY, and {lead}."


def ev_table(D, G):
    n = len(D["ids"])
    hd = "".join(f"<th>{i + 1}</th>" for i in range(n))
    body = ""
    for r in G["index"] + G["ratio"] + G["tiers"]:
        m = r["month"]
        f = lambda v: esc(signed(v, r["nd"], r["unit"]))
        body += (f'<tr><th scope="row">{esc(r["name"])}</th><td>{esc(r["now"])}</td>'
                 f'<td>{f(m[0]) + " from " + esc(day(m[1])) if m else "no data"}</td><td>{f(r["exp"])}</td>'
                 + "".join(f"<td>{f(v)}</td>" for v in r["parts"]) + "</tr>\n")
    return (f'<details class="tbl"><summary>Show the numbers as a table</summary><div class="scroll"><table>'
            f'<thead><tr><th scope="col">Row</th><th scope="col">Now</th><th scope="col">Last month</th>'
            f'<th scope="col">Expected</th>{hd}</tr></thead><tbody>{body}</tbody></table></div></details>')


def ev_section(D):
    G = ev_rows(D)
    months = word(D["g"]["horizon_months"])
    fig = ""
    groups = [("INDEX SPREADS, BP, ONE SCALE", G["index"], ("TIGHTER", "WIDER"), False,
               "Bars for the index spreads in basis points, on one scale."),
              ("THE AXIS, AA SPREAD OVER BBB SPREAD", G["ratio"], ("LOWER", "HIGHER"), False,
               "Bars for the AA to BBB spread ratio."),
              ("IG RATING TIERS, BP, THEIR OWN SCALE", G["tiers"][:2], ("TIGHTER", "WIDER"), True,
               "Bars for two IG rating tiers in basis points, on a scale of their own."),
              ("WEAKEST HY TIER, BP, ITS OWN SCALE", G["tiers"][2:], ("TIGHTER", "WIDER"), True,
               "Bars for the CCC spread in basis points, on a scale of its own.")]
    for title, rows, words, compact, alt in groups:
        if not rows:
            continue
        lab = alt + " " + " ".join(
            f"{r['name']}: now {r['now']}. "
            + (f"Last month {signed(r['month'][0], r['nd'], r['unit'])}. " if r["month"] else "")
            + f"Expected {months}-month move {signed(r['exp'], r['nd'], r['unit'])}, a proposal. By scenario: "
            + ", ".join(signed(v, r["nd"], r["unit"]) for v in r["parts"]) + "." for r in rows)
        fig += evgroup(720, "wide", title, rows, words, lab, compact) + evgroup(358, "narrow", title, rows, words, lab, compact)
    ratio_note = ""
    if G["ratio"]:
        r = G["ratio"][0]
        ratio_note = f" The grid puts the expected ratio at {r['level']:.2f}."
    return f"""
  <section>
    <h2>Expected move against the last month</h2>
    <p>Each row compares one month of actual change with the expected change over the next {months} months. The expected move is the sum of probability times move over the {word(len(D['ids']))} scenarios.</p>
    <p class="key"><span><i class="sw-mo"></i>Last month, actual</span><span><i class="sw-ex"></i>Expected, a proposal</span><span><i class="sw-sc"></i>Scenario parts, numbered as in the list above</span></p>
    <figure>
      {fig}
      <figcaption>{esc(ev_caption(G))}</figcaption>
    </figure>
    <p>The expected values are proposals, because every probability and every scenario move is a judgement.{ratio_note} A part left of the zero line comes from a scenario that pulls the reading down.</p>
    {ev_table(D, G)}
  </section>
"""


# ---------------------------------------------------------------- diagram: attention 2x2
def quad(W, label, mode, at):
    x0, x1, y0, y1 = 30, W - 2, 6, 282
    xm, ym = (x0 + x1) / 2, (y0 + y1) / 2
    b = rect(x0, y0, xm - x0, ym - y0, "range")
    b += rect(x0, y0, x1 - x0, y1 - y0, "frame")
    b += line(xm, y0, xm, y1, "hair") + line(x0, ym, x1, ym, "hair")
    b += T(x0, 302, "LITTLE ATTENTION", "tm") + T(x1, 302, "CROWDED", "tm", "end")
    b += f'<text transform="translate(16 {y0 + 4}) rotate(-90)" class="tm" text-anchor="end">STRONG FACTS</text>'
    b += f'<text transform="translate(16 {y1}) rotate(-90)" class="tm" text-anchor="start">THIN FACTS</text>'
    cells = {"strong_quiet": (x0, y0, False), "strong_crowded": (xm, y0, True),
             "thin_quiet": (x0, ym, False), "thin_crowded": (xm, ym, True)}
    for k, (cx, cy, crowded) in cells.items():
        bx = at["boxes"].get(k)
        if not bx:
            b += T(cx + 12, cy + 26, "No claim named here", "ts tmu")
            continue
        tl, xl = wrap(bx["title"], 22), wrap(bx["text"], 24)
        b += T(cx + 12, cy + 26, tl, "t tb")
        ty = cy + 26 + 17 * len(tl) + 2
        b += T(cx + 12, ty, xl, "ts", lh=16)
        dy = ty + 16 * (len(xl) - 1) + 23
        cls = "dot-today" if bx.get("trend") else "dot"
        dx = (xm if not crowded else x1) - 26 if crowded else cx + 20
        b += f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="6" class="{cls}"/>'
        if bx.get("trend") and not crowded:
            b += arrow(dx + 10, dy, dx + 72, dy)
            tw = [bx["trend"]] if mode == "wide" else wrap(bx["trend"], 16)
            b += T(cx + 12, dy + 24, tw, "tm", lh=15)
    return svg(W, 310, b, label, mode)


# ---------------------------------------------------------------- diagram: pipeline
def stage_lines(s):
    return s.split(", ") if len(s) > 17 else [s]


def pipe(W, label, mode, pl):
    ins, sts = pl["inputs"], pl["stages"]
    b = ""
    if mode == "wide":
        iw, ih, ig = 150, 46, 8
        sw, sg = 120, 18
        H = max(len(ins) * ih + (len(ins) - 1) * ig + 2, 72)
        mid = H / 2
        off = (H - (len(ins) * ih + (len(ins) - 1) * ig)) / 2
        for i, x in enumerate(ins):
            y = off + i * (ih + ig)
            b += rect(1, y, iw, ih) + T(12, y + 20, x["title"], "t tb") + T(12, y + 37, x["text"], "ts tmu")
            b += line(iw + 1, y + ih / 2, iw + 12, y + ih / 2)
        b += line(iw + 12, off + ih / 2, iw + 12, H - off - ih / 2)
        x = iw + 12
        for i, s in enumerate(sts):
            sx = iw + 36 + i * (sw + sg)
            b += arrow(x, mid, sx, mid)
            b += rect(sx, mid - 34, sw, 68)
            b += T(sx + 10, mid - 8, s["title"], "t tb")
            b += T(sx + 10, mid + 11, stage_lines(s["text"]), "ts tmu", lh=15)
            x = sx + sw
    else:
        iw, ih = 174, 48
        for i, x in enumerate(ins):
            px = 1 + (i % 2) * (iw + 8)
            y = 1 + (i // 2) * (ih + 8)
            b += rect(px, y, iw, ih) + T(px + 10, y + 21, x["title"], "t tb") + T(px + 10, y + 38, x["text"], "ts tmu")
        nrow = (len(ins) + 1) // 2
        y = 1 + nrow * ih + (nrow - 1) * 8
        if len(ins) > 1:
            b += line(88, y, 88, y + 14) + line(270, y, 270, y + 14) + line(88, y + 14, 270, y + 14)
        else:
            b += line(88, y, 88, y + 14) + line(88, y + 14, 179, y + 14)
        y += 14
        for s in sts:
            b += arrow(179, y, 179, y + 26)
            y += 26
            b += rect(1, y, 356, 48) + T(14, y + 21, s["title"], "t tb") + T(14, y + 38, s["text"], "ts tmu")
            y += 48
        H = y + 2
    return svg(W, H, b, label, mode)


# ---------------------------------------------------------------- falsifier meters, tiles, disagreements
def meter(D, m):
    if m["reading"] == "axis":
        r, fmt = D["R"][AXIS], (lambda v: f"{v:.3f}")
        lo, hi = axis_domain(D, m["threshold"])
        fthr = f"{m['threshold']:.2f}"
    else:
        r, fmt = D["R"][m["reading"]], bp
        vals = [r["min_3y"], r["max_3y"], r["value"], m["threshold"]]
        pad = (max(vals) - min(vals)) * 0.1
        lo, hi = min(vals) - pad, max(vals) + pad * 2
        fthr = bp(m["threshold"])
    thr, today, side = m["threshold"], r["value"], m["side"]
    W = 300
    X = lambda v: 8 + (v - lo) / (hi - lo) * (W - 16)
    b = ""
    if side == "below":
        b += rect(X(lo), 24, X(thr) - X(lo), 10, "zone")
    else:
        b += rect(X(thr), 24, X(hi) - X(thr), 10, "zone")
    b += line(X(lo), 29, X(hi), 29, "hair")
    b += line(X(thr), 16, X(thr), 42, "thr")
    b += f'<circle cx="{X(today):.1f}" cy="29" r="6" class="dot-today"/>'
    b += T(min(max(X(today), 40), W - 40), 14, f"today {fmt(today)}", "tm tk", "middle")
    lthr = f"triggers {side} {fthr}"
    if side == "above":
        b += T(X(hi), 56, lthr, "tm", "end")
    else:
        b += T(max(X(thr), 70), 56, lthr, "tm", "middle")
    name = "ratio" if m["reading"] == "axis" else f"{m['reading']} spread"
    label = f"The {name} is {fmt(today)} today. The falsifier triggers {side} {fthr}."
    return f'<svg class="meter" viewBox="0 0 {W} 60" role="img" aria-label="{esc(label)}">{b}</svg>'


VS = ('<svg class="vs" viewBox="0 0 40 20" role="img" aria-label="against"><line x1="9" y1="10" x2="31" y2="10" class="ln"/>'
      '<polygon points="2,10 10,6 10,14" class="ah"/><polygon points="38,10 30,6 30,14" class="ah"/></svg>')
RING = '<svg viewBox="0 0 10 10" aria-hidden="true"><circle cx="5" cy="5" r="3.5"/></svg>'


def dis(x):
    w = f'<p class="why">{esc(x["why"])}</p>' if x.get("why") else ""
    return (f'<article class="dis"><h3>{esc(x["question"])}</h3><div class="sides">'
            f'<div class="side"><span class="who">{esc(x["a_who"])}</span><p>{esc(x["a"])}</p></div>{VS}'
            f'<div class="side"><span class="who">{esc(x["b_who"])}</span><p>{esc(x["b"])}</p></div></div>{w}</article>\n')


def tile(D, x):
    text, cls = STATUS[x["status"]]
    extra = meter(D, x["meter"]) if x.get("meter") else ""
    return (f'<article class="tile"><div class="hd"><span class="id">{esc(x["id"])}</span>'
            f'<span class="chip{cls}">{RING}{text}</span></div><h3>{esc(x["claim"])}</h3>{extra}'
            f'<dl><dt>Observable</dt><dd>{esc(x["observable"])}</dd><dt>Threshold</dt><dd>{esc(x["threshold"])}</dd>'
            f'<dt>Today</dt><dd>{esc(x["today"])}</dd></dl></article>\n')


def scen_items(D, view):
    R = D["R"]
    labels = (view or {}).get("scenarios", {}).get("labels", {})
    verb = lambda v: "holds" if round(v) == 0 else f"{'widens' if v > 0 else 'tightens'} {abs(v):,.0f}bp"
    out = ""
    for i, s in enumerate(D["spine"], 1):
        sid = s["id"]
        ig, hy = D["rows"]["IG"]["_sdx"][sid], D["rows"]["HY"]["_sdx"][sid]
        move = f"IG {verb(ig)} and HY {verb(hy)}."
        if D["ratio_rel"]:
            v, now = D["ratio_rel"][2][sid], R[AXIS]["value"]
            how = "stays near" if abs(v - now) < 0.015 else "rises to" if v > now else "falls to"
            move += f" The ratio {how} {v:.2f}."
        out += (f'<li><span class="sw" style="background:var(--s{i});color:var(--s{i}t)">{i}</span>'
                f'<span class="nm">{esc(labels.get(sid, s["name"]))}<span class="lb">{esc(SRC_LABEL.get(s["p_source"], s["p_source"]))}</span></span>'
                f'<span class="pp">{s["p"]:.0%}</span><span class="mv">{esc(move)}</span></li>\n')
    return out


# ---------------------------------------------------------------- page
CSS = """
/* Layout: one column readout. The view first, then the diagrams in a fixed order. Diagrams sit on the page ground, tiles only for the falsifiers. */
:root {
  --bg: #f2f5f2; --surface: #fbfcfb; --ink: #16211c; --muted: #56655d; --line: #d3dbd5;
  --accent: #0f6b54; --accent-soft: #dcece6; --warn: #8a5200; --warn-soft: #f6ead3;
  --no: #a23a2a; --no-soft: #f6e1dc;
  --s1: #f1e2c4; --s2: #e2c48a; --s3: #c99a4a; --s4: #9a6a17; --s5: #5e3d05;
  --s1t: #16211c; --s2t: #16211c; --s3t: #16211c; --s4t: #ffffff; --s5t: #ffffff;
  --display: "Bricolage Grotesque", "IBM Plex Sans", system-ui, sans-serif;
  --body: "IBM Plex Sans", system-ui, -apple-system, "Segoe UI", sans-serif;
  --mono: "IBM Plex Mono", ui-monospace, Menlo, monospace;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #111815; --surface: #18211d; --ink: #e5ece7; --muted: #9baba2; --line: #2c3a33;
    --accent: #62cdae; --accent-soft: #1d332c; --warn: #e2ad52; --warn-soft: #33290f;
    --no: #ef8f7d; --no-soft: #3a1f1a;
    --s1: #3a2d12; --s2: #5c4514; --s3: #7d5a17; --s4: #c08f35; --s5: #ecc880;
    --s1t: #f3ece0; --s2t: #f3ece0; --s3t: #ffffff; --s4t: #16110a; --s5t: #16110a;
    color-scheme: dark;
  }
}
:root[data-theme="dark"] {
  --bg: #111815; --surface: #18211d; --ink: #e5ece7; --muted: #9baba2; --line: #2c3a33;
  --accent: #62cdae; --accent-soft: #1d332c; --warn: #e2ad52; --warn-soft: #33290f;
  --no: #ef8f7d; --no-soft: #3a1f1a;
  --s1: #3a2d12; --s2: #5c4514; --s3: #7d5a17; --s4: #c08f35; --s5: #ecc880;
  --s1t: #f3ece0; --s2t: #f3ece0; --s3t: #ffffff; --s4t: #16110a; --s5t: #16110a;
  color-scheme: dark;
}
* { box-sizing: border-box; }
body { background: var(--bg); color: var(--ink); font-family: var(--body); font-size: 16px; line-height: 1.6; }
.wrap { max-width: 820px; margin: 0 auto; padding-block: 40px 72px;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px));
  display: flex; flex-direction: column; gap: 48px; }
h1, h2, h3, p, ol, ul, figure { margin: 0; }
h1 { font-family: var(--display); font-weight: 700; font-size: clamp(1.65rem, 5vw, 2.35rem); line-height: 1.12; letter-spacing: -0.02em; text-wrap: balance; }
h2 { font-family: var(--display); font-weight: 500; font-size: 1.35rem; padding-bottom: 8px; border-bottom: 2px solid var(--ink); text-wrap: balance; }
h3 { font-family: var(--body); font-weight: 600; font-size: 1rem; }
.eyebrow { font-family: var(--mono); font-size: 0.75rem; letter-spacing: 0.08em; text-transform: uppercase; color: var(--accent); margin-bottom: 12px; }
.lede { color: var(--muted); margin-top: 14px; max-width: 62ch; }
.asof { font-family: var(--mono); font-size: 0.82rem; margin-top: 18px; padding: 8px 12px; border: 1px solid var(--ink); display: inline-block; }
.terms { font-size: 0.88rem; color: var(--muted); max-width: 68ch; margin-top: 14px; }
section { display: flex; flex-direction: column; gap: 16px; min-width: 0; }
p { max-width: 68ch; }
figure { display: flex; flex-direction: column; gap: 12px; min-width: 0; }
figcaption, .cap { font-size: 0.9rem; color: var(--muted); max-width: 68ch; }
.note { background: var(--warn-soft); color: var(--warn); padding: 10px 14px; max-width: 68ch; font-size: 0.93rem; }
header .note { margin-top: 14px; }

/* diagrams */
svg.dg { display: block; width: 100%; height: auto; }
svg.dg-wide { display: none; }
svg.dg-narrow { max-width: 460px; }
@media (min-width: 752px) { svg.dg-wide { display: block; } svg.dg-narrow { display: none; } }
svg text { font-family: var(--body); font-size: 13px; fill: var(--ink); }
svg .ts { font-size: 12px; }
svg .tm { font-family: var(--mono); font-size: 12px; fill: var(--muted); letter-spacing: 0.02em; }
svg .tmn { letter-spacing: -0.02em; }
svg .tk { fill: var(--ink); }
svg .tb { font-weight: 600; }
svg .tmu { fill: var(--muted); }
svg .tl { font-family: var(--display); font-size: 17px; font-weight: 700; }
svg .ln { stroke: var(--ink); stroke-width: 1.5; fill: none; }
svg .lnm { stroke: var(--muted); stroke-width: 1; fill: none; }
svg .hair { stroke: var(--line); stroke-width: 1; fill: none; }
svg .ah { fill: var(--ink); stroke: none; }
svg .box { fill: var(--surface); stroke: var(--line); stroke-width: 1; }
svg .frame { fill: none; stroke: var(--line); stroke-width: 1; }
svg .range { fill: var(--accent-soft); stroke: none; }
svg .zone { fill: var(--no-soft); stroke: none; }
svg .thr { stroke: var(--no); stroke-width: 1.5; stroke-dasharray: 5 4; fill: none; }
svg .tod { stroke: var(--accent); stroke-width: 1.5; fill: none; }
svg .dot { fill: var(--ink); stroke: var(--bg); stroke-width: 2; }
svg .dot-today { fill: var(--accent); stroke: var(--bg); stroke-width: 2; }
svg .st-priced { fill: var(--accent-soft); stroke: var(--accent); stroke-width: 1.5; }
svg .st-repriced { fill: var(--warn-soft); stroke: var(--warn); stroke-width: 1.5; }
svg .st-notp { fill: none; stroke: var(--no); stroke-width: 1.5; stroke-dasharray: 5 4; }
svg .s1 { fill: var(--s1); } svg .s2 { fill: var(--s2); } svg .s3 { fill: var(--s3); } svg .s4 { fill: var(--s4); } svg .s5 { fill: var(--s5); }
svg .s1t { fill: var(--s1t); } svg .s2t { fill: var(--s2t); } svg .s3t { fill: var(--s3t); } svg .s4t { fill: var(--s4t); } svg .s5t { fill: var(--s5t); }

/* expected move chart */
svg .mo { fill: var(--muted); }
svg .ex { fill: var(--accent); }
svg .seg { stroke: var(--muted); stroke-width: 0.75; }
.key { display: flex; flex-wrap: wrap; gap: 6px 18px; font-size: 0.88rem; color: var(--muted); max-width: none; }
.key span { display: inline-flex; align-items: center; gap: 7px; }
.key i { width: 14px; height: 10px; border-radius: 2px; display: inline-block; }
.key .sw-mo { background: var(--muted); }
.key .sw-ex { background: var(--accent); }
.key .sw-sc { width: 28px; background: linear-gradient(90deg, var(--s1) 0 20%, var(--s2) 20% 40%, var(--s3) 40% 60%, var(--s4) 60% 80%, var(--s5) 80%); outline: 0.75px solid var(--muted); }
.tbl summary { cursor: pointer; font-size: 0.9rem; color: var(--accent); width: fit-content; }
.tbl summary:focus-visible { outline: 2px solid var(--accent); outline-offset: 3px; }
.tbl .scroll { overflow-x: auto; margin-top: 10px; }
.tbl table { border-collapse: collapse; font-size: 0.85rem; font-variant-numeric: tabular-nums; white-space: nowrap; }
.tbl th, .tbl td { padding: 6px 12px 6px 0; border-bottom: 1px solid var(--line); text-align: right; font-weight: 400; }
.tbl thead th { font-family: var(--mono); font-size: 0.75rem; color: var(--muted); }
.tbl th:first-child, .tbl td:nth-child(2), .tbl td:nth-child(3) { text-align: left; }
.tbl tbody th { font-weight: 600; }

/* scenario list */
.scen { list-style: none; padding: 0; display: flex; flex-direction: column; }
.scen li { display: grid; grid-template-columns: 28px 1fr auto; column-gap: 12px; row-gap: 2px; padding: 10px 0; border-bottom: 1px solid var(--line); align-items: baseline; }
.scen .sw { width: 28px; height: 22px; border-radius: 4px; font-family: var(--mono); font-size: 0.8rem; font-weight: 500; display: grid; place-items: center; align-self: start; }
.scen .nm { font-weight: 600; min-width: 0; }
.scen .pp { font-family: var(--mono); font-size: 0.9rem; font-variant-numeric: tabular-nums; }
.scen .mv { grid-column: 2 / -1; color: var(--muted); font-size: 0.93rem; }
.scen .lb { font-family: var(--mono); font-size: 0.75rem; color: var(--muted); font-weight: 400; margin-left: 6px; white-space: nowrap; }

/* falsifier tiles */
.tiles { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 320px), 1fr)); gap: 12px; }
.tile { background: var(--surface); border: 1px solid var(--line); padding: 16px; display: flex; flex-direction: column; gap: 10px; min-width: 0; }
.tile .hd { display: flex; justify-content: space-between; align-items: center; gap: 8px; flex-wrap: wrap; }
.tile .id { font-family: var(--mono); font-size: 0.82rem; color: var(--accent); }
.chip { font-family: var(--mono); font-size: 0.75rem; border: 1px solid var(--accent); color: var(--accent); background: var(--accent-soft); padding: 2px 8px; display: inline-flex; align-items: center; gap: 6px; }
.chip svg { width: 10px; height: 10px; }
.chip circle { fill: none; stroke: currentColor; stroke-width: 2; }
.chip-close { border-color: var(--warn); color: var(--warn); background: var(--warn-soft); }
.chip-trig { border-color: var(--no); color: var(--no); background: var(--no-soft); font-weight: 500; }
.chip-trig circle { fill: currentColor; }
.tile dl { margin: 0; display: grid; grid-template-columns: 6.2em 1fr; gap: 6px 10px; font-size: 0.92rem; }
.tile dt { font-family: var(--mono); font-size: 0.72rem; letter-spacing: 0.06em; text-transform: uppercase; color: var(--muted); padding-top: 3px; }
.tile dd { margin: 0; min-width: 0; }
svg.meter { display: block; width: 100%; max-width: 360px; height: auto; }

/* disagreements */
.group { font-family: var(--mono); font-size: 0.75rem; letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); margin-top: 8px; }
.dislist { display: flex; flex-direction: column; }
.dis { padding: 14px 0; border-bottom: 1px solid var(--line); display: flex; flex-direction: column; gap: 8px; }
.sides { display: grid; grid-template-columns: 1fr 40px 1fr; gap: 12px; align-items: start; }
.side { min-width: 0; border-top: 2px solid var(--ink); padding-top: 6px; }
.side p { font-size: 0.95rem; }
.who { font-family: var(--mono); font-size: 0.78rem; color: var(--accent); display: block; overflow-wrap: anywhere; }
svg.vs { width: 40px; height: 20px; display: block; margin-top: 12px; }
.why { font-size: 0.88rem; color: var(--muted); }
@media (max-width: 600px) {
  .sides { grid-template-columns: 1fr; gap: 6px; }
  svg.vs { transform: rotate(90deg); margin: 4px 0 4px 8px; }
}
.foot { max-width: none; border-top: 2px solid var(--ink); padding-top: 14px; font-size: 0.9rem; color: var(--muted); display: flex; flex-direction: column; gap: 8px; }
"""

FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;'
         '12..96,700&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap">')
QUESTION = "How much AI debt supply do US credit spreads price?"
STALE = "The text sections were not updated in this run. The diagrams below use this run's data."


def build(D, view):
    R, g, a = D["R"], D["g"], D["R"][AXIS]
    months, date, e = word(g["horizon_months"]), D["date"], esc
    asof = f"As of {date}. Research only. Scenario probabilities are proposals."
    ig, hy = D["rows"]["IG"], D["rows"]["HY"]
    order, tp, share = tail(D)
    pmax = max(D["P"].values())
    top = max(D["P"], key=D["P"].get)

    # header
    if view:
        head = (f'<p class="eyebrow">{e(view.get("question", QUESTION))}</p><h1>{e(view["view"])}</h1>'
                f'<p class="lede">{e(view["lede"])}</p><p class="asof">{asof}</p>')
    else:
        head = (f'<p class="eyebrow">{QUESTION}</p><h1>Credit scenario view for {date}</h1>'
                f'<p class="note">{STALE}</p><p class="asof">{asof}</p>')
    head += (f'<p class="terms">Terms. Capex is capital spending. A spread is the extra yield that a bond pays over Treasuries. '
             f'IG means investment grade, and HY means high yield. AA, A and BBB are rating tiers inside IG, and CCC is the weakest '
             f'HY tier. One bp is one hundredth of a percentage point. The horizon is {g["horizon"]}.</p>')

    # chain
    chain = ""
    if view:
        c = view["chain"]
        lab = (f"{c['source']['title']}: {c['source']['detail']}. {c['supply']['title']}: {c['supply']['detail']}. The debt goes to "
               f"{word(len(c['destinations']))} places. "
               + " ".join(f"{d['name']}: {d['status_text'].lower()}, {d['status_sub']}." for d in c["destinations"]))
        chain = f"""
  <section>
    <h2>The causal chain</h2>
    <figure>
      {both(flow, lab, c)}
      <figcaption>{e(c["caption"])}</figcaption>
    </figure>
    <p>{e(c["note"])}</p>
  </section>
"""

    # axis
    per = D["ratio_rel"][2] if D["ratio_rel"] else {}
    fz = axis_falsifier(view)
    lo, hi = axis_domain(D, fz[1] if fz else None)
    lab = (f"Scale of the AA to BBB spread ratio from {lo:.2f} to {hi:.2f}. Three-year range {a['min_3y']:.3f} to {a['max_3y']:.3f}"
           + (f", mean {a['mean_3y']:.3f}" if "mean_3y" in a else "") + f". Today {a['value']:.3f}."
           + (f" Falsifier line {fz[1]:.2f}." if fz else "")
           + (" Scenario ratios: " + ", ".join(f"{per[k]:.2f}" for k in D["ids"]) + "." if per else ""))
    axis_p = "The axis is the AA spread divided by the BBB spread, from FRED."
    if isinstance(R.get("AA"), dict) and isinstance(R.get("BBB"), dict):
        axis_p += f" Today the AA spread is {bp(R['AA']['value'])} and the BBB spread is {bp(R['BBB']['value'])}."
    axis_n = "The green band is the three-year range."
    if "z_3y" in a:
        axis_n += f" Today is {abs(a['z_3y']):.2f} standard deviations {'above' if a['z_3y'] >= 0 else 'below'} the mean."
    if view and view["axis"].get("note"):
        axis_n += " " + view["axis"]["note"]
    axis_c = view["axis"]["caption"] if view else (
        f"The ratio is at the {ordinal(a['percentile_3y'])} percentile of its own three years.")
    axis = f"""
  <section>
    <h2>The operational axis</h2>
    <p>{axis_p}</p>
    <figure>
      {both(gauge, lab, D, view)}
      <figcaption>{e(axis_c)}</figcaption>
    </figure>
    <p>{e(axis_n)}</p>
  </section>
"""

    # scenarios
    n = len(D["ids"])
    lab = (f"Stacked bar of {word(n)} proposed scenario probabilities: "
           + ", ".join(f"{D['P'][k]:.0%}" for k in D["ids"]) + f". The two least likely hold {tp:.0%} of the probability.")
    cap = "No scenario has a majority" if pmax <= 0.5 else f"Scenario {D['ids'].index(top) + 1} has a majority"
    if share is not None and share > 0.5:
        cap += ", and the two least likely scenarios drive most of the expected IG widening."
    elif share is not None:
        cap += f", and the two least likely scenarios drive {share_words(share)} of the expected IG widening."
    else:
        cap += "."
    sp = f"Moves are {months}-month spread changes. The expected move is IG {signed(ig['_exp'], 0, 'bp')} and HY {signed(hy['_exp'], 0, 'bp')}."
    if "_be" in ig and "_be" in hy:
        sp += f" Income covers {bp(ig['_be'])} of IG widening and {bp(hy['_be'])} of HY widening."
    if view and view.get("scenarios", {}).get("note"):
        sp += " " + view["scenarios"]["note"]
    scen = f"""
  <section>
    <h2>{word(n).capitalize()} scenarios</h2>
    <figure>
      {both(scenbar, lab, D)}
      <figcaption>{cap}</figcaption>
    </figure>
    <ol class="scen">
      {scen_items(D, view)}
    </ol>
    <p>{e(sp)}</p>
  </section>
"""

    rest = ""
    if view:
        f = view["falsifiers"]
        fnote = f'<p class="cap">{e(f["note"])}</p>' if f.get("note") else ""
        rest += f"""
  <section>
    <h2>{word(len(f["items"])).capitalize()} falsifier{"s" if len(f["items"]) != 1 else ""}</h2>
    <div class="tiles">
      {"".join(tile(D, x) for x in f["items"])}
    </div>
    {fnote}
  </section>
"""
        groups = "".join(f'<p class="group">{e(x["title"])}</p>\n<div class="dislist">{"".join(dis(i) for i in x["items"])}</div>'
                         for x in view["disagreements"]["groups"])
        rest += f"""
  <section>
    <h2>Where the sources disagree</h2>
    <p class="cap">The sources still disagree on these points, and this page does not settle them.</p>
    {groups}
  </section>
"""
        at = view["attention"]
        names = {"strong_quiet": "Strong facts and little attention", "strong_crowded": "Strong facts and crowded",
                 "thin_quiet": "Thin facts and little attention", "thin_crowded": "Thin facts and crowded"}
        lab = "Two by two grid of fact strength against attention. " + " ".join(
            f"{names[k]}: {at['boxes'][k]['title']}." for k in names if at["boxes"].get(k))
        anote = f"<p>{e(at['note'])}</p>" if at.get("note") else ""
        rest += f"""
  <section>
    <h2>Evidence against attention</h2>
    <figure>
      {both(quad, lab, at)}
      <figcaption>{e(at["caption"])}</figcaption>
    </figure>
    {anote}
  </section>
"""
        pl = view["pipeline"]
        lab = (", ".join(x["title"] for x in pl["inputs"]) + " feed these steps in order: "
               + ", ".join(x["title"] for x in pl["stages"]) + ".")
        rest += f"""
  <section>
    <h2>What feeds the view</h2>
    <figure>
      {both(pipe, lab, pl)}
      <figcaption>The same inputs feed a new memo and a new email every two days.</figcaption>
    </figure>
    <p class="note">Limits. {e(view["limits"])}</p>
  </section>
"""
    else:
        rest = f"""
  <section>
    <p class="note">{STALE} The falsifiers, the disagreements, the attention grid and the limits are in the memo of this run.</p>
  </section>
"""

    return f"""<title>AI Debt Pricing View</title>
<meta name="claude:viewport-fit-sides" content="cover">
{FONTS}
<style>{CSS}</style>

<div class="wrap">
  <header>
    {head}
  </header>
{chain}{axis}{scen}{ev_section(D)}{rest}
  <p class="foot"><span>{asof}</span><span>Source: the thesis run of {date}, its scenario grid, its FRED readings and its X account summary.</span></p>
</div>
"""


# ---------------------------------------------------------------- entry points
def check(run):
    try:
        D = load_data(run)
    except InputError as e:
        print(f"FAIL\n- {e}")
        return 1
    tok = tokens(D)
    E, Wn = [], []
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", D["dirname"]) and D["g"]["as_of"] != D["dirname"]:
        E.append(f"scenarios.json as_of is {D['g']['as_of']}, the run directory is {D['dirname']}")
    E += report_check(D)
    for rid, key in (("IG", "IG"), ("HY", "HY"), ("IG.AA", "AA"), ("IG.BBB", "BBB"), ("HY.CCC", "CCC")):
        r = D["rows"].get(rid)
        if r and isinstance(D["R"].get(key), dict) and r.get("now") is not None and abs(r["now"] - D["R"][key]["value"]) > 0.5:
            E.append(f"{rid}: the grid 'now' is {r['now']}, readings.json says {D['R'][key]['value']}")
    for k in ("IG", "HY", AXIS):
        if not month_move(D, k):
            Wn.append(f"no month_before for {k}. The chart will show no one-month move")
    view, ve, vw = load_view(D, tok)
    E += ve
    Wn += vw
    if not E:
        try:
            page = build(D, view)
            if EMAIL.search(re.sub(r"<style>.*?</style>", "", page, flags=re.S)):
                E.append("the page contains an email address")
        except Exception as ex:  # a failed render is a failed check, with the reason
            E.append(f"the page does not render: {type(ex).__name__}: {ex}")
    for w in Wn:
        print(f"WARN: {w}")
    if E:
        print("FAIL")
        for m in E:
            print(f"- {m}")
        return 1
    print("PASS")
    return 0


def main(argv):
    if len(argv) == 3 and argv[1] == "--check":
        return check(argv[2])
    if len(argv) != 3 or argv[1].startswith("-"):
        print(__doc__)
        return 2
    run, out = argv[1], argv[2]
    try:
        D = load_data(run)
    except InputError as e:
        print(f"build_view: cannot build, {e}", file=sys.stderr)
        return 1
    view, E, Wn = load_view(D, tokens(D))
    for m in E:
        print(f"build_view: view.json not used: {m}", file=sys.stderr)
    for m in report_check(D):
        print(f"build_view: WARN {m}", file=sys.stderr)
    try:
        page = build(D, view)
    except Exception as ex:
        if view is None:
            raise
        print(f"build_view: view.json not used, the text sections failed to render: {type(ex).__name__}: {ex}", file=sys.stderr)
        page = build(D, None)
    tmp = out + ".tmp"
    with open(tmp, "w") as f:
        f.write(page)
    os.replace(tmp, out)
    print(f"wrote {out} ({len(page)} bytes, text sections {'updated' if view else 'NOT updated'})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
