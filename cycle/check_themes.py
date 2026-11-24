"""Check, record and print the step 1 themes of one run. No model involved.

  check_themes.py <run_dir>                    validate <run_dir>/themes.json. Prints PASS or FAIL with reasons.
  check_themes.py <run_dir> --ledger <file>    validate, then append one line for each theme to the ledger (JSON lines).
  check_themes.py <run_dir> --email <file>     validate, then insert a plain-text block of themes into the email file.

The model proposes the themes. This script decides whether they meet the step 1 rules.
"""
import datetime
import json
import re
import sys
from pathlib import Path

LENSES = ["macro", "cycle", "policy", "drivers"]
STATUS = {"born", "stronger", "unchanged", "crowded", "falsified", "retired"}
CONF = {"well supported", "supported with a caveat", "thin"}
# Step 1 holds no prices and no trades.
BANNED_KEYS = {"probability", "probabilities", "priced_in", "scenario", "scenarios", "size", "sizing", "hedge_ratio", "stop", "entry", "exit"}
BANNED_TEXT = re.compile(r"\b(stop[- ]loss|hedge ratio|notional of|position size|buy protection|sell protection|go long|go short|entry level|exit level)\b", re.I)
LAST_LINE = "This is research only. It contains no trades."
MARK = "STEP 1 THEMES"


def text(v):
    return isinstance(v, str) and v.strip() != ""


def walk_keys(o):
    if isinstance(o, dict):
        for k, v in o.items():
            yield k
            yield from walk_keys(v)
    elif isinstance(o, list):
        for v in o:
            yield from walk_keys(v)


def score(t):
    return len(t.get("facts") or []) - len(t.get("attention") or [])


def validate(run):
    errs = []
    p = run / "themes.json"
    try:
        d = json.loads(p.read_text())
    except (OSError, ValueError) as e:
        return None, [f"cannot read themes.json: {e}"]
    try:
        as_of = datetime.date.fromisoformat(d.get("as_of", ""))
    except ValueError:
        as_of = None
        errs.append("as_of is not a date")

    lenses = {l.get("id"): l for l in d.get("lenses") or [] if isinstance(l, dict)}
    for lid in LENSES:
        l = lenses.get(lid)
        if not l:
            errs.append(f"lens {lid} is missing")
            continue
        if not text(l.get("question")):
            errs.append(f"lens {lid}: no question")
        if text(l.get("finding")):
            m = l.get("method") or {}
            if not (text(m.get("rule")) and text(m.get("skill")) and text(m.get("chapter"))):
                errs.append(f"lens {lid}: a finding needs a method with rule, skill and chapter")
            elif not (Path("/home/ak/.agents/skills") / m["chapter"].replace("/home/ak/.agents/skills/", "")).exists():
                errs.append(f"lens {lid}: chapter file does not exist: {m['chapter']}")
            if not l.get("series"):
                errs.append(f"lens {lid}: a finding needs at least one series")
            if l.get("confidence") not in CONF:
                errs.append(f"lens {lid}: confidence must be one of {sorted(CONF)}")
        elif not text(l.get("no_data")):
            errs.append(f"lens {lid}: no finding, so no_data must say what was missing")
    with_finding = {lid for lid, l in lenses.items() if text(l.get("finding"))}

    themes = d.get("themes")
    if not isinstance(themes, list):
        errs.append("themes is not a list")
        themes = []
    if len(themes) > 6:
        errs.append(f"{len(themes)} themes, the limit is 6")
    seen = set()
    for t in themes:
        tid = t.get("id", "?")
        if tid in seen:
            errs.append(f"{tid}: duplicate id")
        seen.add(tid)
        if not text(t.get("sentence")):
            errs.append(f"{tid}: no sentence")
        ls = t.get("lenses") or []
        if len(set(ls)) < 2:
            errs.append(f"{tid}: rests on {len(set(ls))} lens, the rule needs two or more")
        for lid in ls:
            if lid not in LENSES:
                errs.append(f"{tid}: unknown lens {lid}")
            elif lid not in with_finding:
                errs.append(f"{tid}: lens {lid} has no finding")
        mech = t.get("mechanism") or []
        if len(mech) < 2 or not all(isinstance(m, dict) and text(m.get("link")) and text(m.get("source")) for m in mech):
            errs.append(f"{tid}: the mechanism needs two or more links, each with a source")
        f = t.get("falsifier") or {}
        if not (text(f.get("observable")) and text(f.get("threshold"))):
            errs.append(f"{tid}: the falsifier needs an observable and a threshold")
        if not text(t.get("proposed_measure")):
            errs.append(f"{tid}: no proposed_measure (write 'none yet' if there is none)")
        try:
            vd = datetime.date.fromisoformat(t.get("verdict_date", ""))
            if as_of and not (as_of < vd <= as_of + datetime.timedelta(days=366)) and t.get("status") not in ("retired", "falsified"):
                errs.append(f"{tid}: verdict_date must be after as_of and at most 12 months later")
        except ValueError:
            errs.append(f"{tid}: verdict_date is not a date")
        if not isinstance(t.get("facts"), list) or not t.get("facts"):
            errs.append(f"{tid}: no facts listed")
        if not isinstance(t.get("attention"), list):
            errs.append(f"{tid}: attention must be a list (it may be empty)")
        if t.get("horizon_type") not in ("secular", "cyclical"):
            errs.append(f"{tid}: horizon_type must be secular or cyclical")
        if t.get("status") not in STATUS:
            errs.append(f"{tid}: status must be one of {sorted(STATUS)}")
        if not (t.get("winners") or t.get("losers")):
            errs.append(f"{tid}: names no winners and no losers")
        so = t.get("strongest_objection") or {}
        if not (text(so.get("text")) and text(so.get("source"))):
            errs.append(f"{tid}: the strongest objection needs text and a source")
        if not text(t.get("if_wrong")):
            errs.append(f"{tid}: no if_wrong paragraph")
    live = [t for t in themes if t.get("status") not in ("falsified", "retired")]
    keys = [(-score(t), -len(t.get("facts") or [])) for t in live]
    if keys != sorted(keys):
        errs.append("themes are not in rank order (facts minus attention, highest first)")
    if not d.get("blind_spots"):
        errs.append("blind_spots is empty")
    bad = sorted(set(walk_keys(d)) & BANNED_KEYS)
    if bad:
        errs.append(f"step 1 holds no prices and no trades, remove the keys: {bad}")
    m = BANNED_TEXT.search(json.dumps(d))
    if m:
        errs.append(f"trade wording found: '{m.group(0)}'")
    return d, errs


def ledger(d, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as f:
        for rank, t in enumerate(d["themes"], 1):
            f.write(json.dumps({"as_of": d["as_of"], "id": t["id"], "rank": rank, "sentence": t["sentence"], "status": t["status"],
                                "status_reason": t.get("status_reason", ""), "lenses": t["lenses"], "facts": len(t["facts"]),
                                "attention": len(t["attention"]), "proposed_measure": t["proposed_measure"],
                                "falsifier": t["falsifier"], "verdict_date": t["verdict_date"]}) + "\n")


def first(s, limit=38):
    """First sentence of s, cut to a word limit."""
    s = " ".join(str(s).split())
    s = re.split(r"(?<=[.!?])\s", s, maxsplit=1)[0].rstrip(".")
    w = s.split()
    return " ".join(w[:limit]) + (" ..." if len(w) > limit else "")


def email_block(d):
    out = [MARK, "", "Step 1 forms themes from four inputs: macro fundamentals, the business cycle, policy and asset class drivers.",
           "A theme needs two inputs that agree. The rank is facts minus attention. Nothing here is priced.", ""]
    for rank, t in enumerate(d["themes"], 1):
        f = t["falsifier"]
        out += [f"{rank}. {t['sentence']}",
                f"   Inputs: {', '.join(t['lenses'])}. Facts {len(t['facts'])}, attention {len(t['attention'])}. Status: {t['status']}.",
                f"   False if: {first(f['threshold'])}. Verdict by {t['verdict_date']}.",
                f"   Measure for step 2: {first(t['proposed_measure'], 24)}.", ""]
    out += ["Blind spots:"] + [f"- {first(b, 24)}." for b in d["blind_spots"][:3]] + ["The full cards are in themes.md of this run.", ""]
    return "\n".join(out)


def into_email(d, path):
    s = path.read_text()
    if MARK in s:
        s = s[:s.index(MARK)].rstrip("\n") + "\n\n" + LAST_LINE + "\n"
    body = s.rstrip("\n")
    tail = ""
    if body.endswith(LAST_LINE):
        body, tail = body[: -len(LAST_LINE)].rstrip("\n"), LAST_LINE
    path.write_text(body + "\n\n" + email_block(d) + (tail + "\n" if tail else ""))


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    run = Path(argv[1])
    d, errs = validate(run)
    if errs:
        print(f"FAIL {len(errs)} problems in {run / 'themes.json'}:")
        for e in errs:
            print("  " + e)
        return 1
    print(f"PASS {len(d['themes'])} themes, {len(d.get('observations') or [])} observations, {len(d['blind_spots'])} blind spots")
    if "--ledger" in argv:
        ledger(d, Path(argv[argv.index("--ledger") + 1]))
        print("ledger updated")
    if "--email" in argv:
        into_email(d, Path(argv[argv.index("--email") + 1]))
        print("email updated")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
