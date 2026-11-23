#!/usr/bin/env python3
"""Check that every number in a styled file appears in at least one source file.

Usage: python3 check_numbers.py <styled file> <source file> [<source file> ...]

Prints PASS and exits 0 when every numeric token of the styled file is found.
Prints FAIL with the missing tokens and exits 1 otherwise. Exits 2 on a usage
or file error. Standard library only.

What counts as a token in the styled file: integers, decimals, percentages,
bp values, dollar amounts, ISO dates (2026-11-23) and day-month dates (19 Nov).

How a token is matched:
- By value, not by spelling. "1,361bp" matches 1361.0, "$420bn" matches 420.
- The sign is ignored. "+14bp" matches 14.
- A percentage also matches its fraction. "28%" matches 0.28.
- An ISO date must appear whole in a source.
- "19 Nov" matches "19 Nov", "November 19" or any ISO date "....-11-19".

What is skipped in the styled file, because it is a label and not a quantity:
- A number glued to a letter before it: F1, Q3, BAMLC0A2CAA.
- A dotted label that starts with a letter: H.4.1.
- A list marker at the start of a line: "1." or "2)".

The source side is read loosely on purpose. Every digit run in a source counts,
so a real number is never missed there. Number words ("two thirds") are not
checked.
"""
import re
import sys
from decimal import Decimal, InvalidOperation

MONTHS = {m: i + 1 for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])}
MON = r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\.?"
ISO = re.compile(r"(?<!\d)(\d{4})-(\d{2})-(\d{2})(?!\d)")
DAY_MON = re.compile(r"(?<![\d.,A-Za-z])(\d{1,2})(?:st|nd|rd|th)?\s+(" + MON + r")(?![a-z])")
MON_DAY = re.compile(r"(?<![A-Za-z])(" + MON + r")\s+(\d{1,2})(?:st|nd|rd|th)?(?![\d.,]*\d)")
NUM = r"(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?"
SRC_NUM = re.compile(NUM)
STY_NUM = re.compile(r"(?P<pre>.{0,2})(?<![\d,])(?P<num>" + NUM + r")(?P<suf>%|[A-Za-z]*)", re.S)
LIST_MARK = re.compile(r"(?m)^(\s*(?:[-*>]\s+)?)\d{1,2}[.)](?=\s)")


def norm(s):
    """'1,361' -> Decimal('1361'); '68.0' -> Decimal('68')."""
    try:
        d = Decimal(s.replace(",", ""))
    except InvalidOperation:
        return None
    return d.normalize() + 0  # +0 turns -0 and 1E+2 forms into plain values


def month_of(word):
    return MONTHS.get(word[:3].lower())


def pull_dates(text):
    """Return (iso dates, (month, day) pairs, text with those dates blanked)."""
    isos, mds = set(), set()

    def iso_sub(m):
        isos.add(m.group(0))
        mds.add((int(m.group(2)), int(m.group(3))))
        return " "

    def dm_sub(m):
        mds.add((month_of(m.group(2)), int(m.group(1))))
        return " " + m.group(2) + " "

    def md_sub(m):
        mds.add((month_of(m.group(1)), int(m.group(2))))
        return " " + m.group(1) + " "

    text = ISO.sub(iso_sub, text)
    text = DAY_MON.sub(dm_sub, text)
    text = MON_DAY.sub(md_sub, text)
    return isos, mds, text


def read_source(path):
    text = open(path, encoding="utf-8", errors="replace").read()
    isos, mds, _ = pull_dates(text)
    nums = set()
    for m in SRC_NUM.finditer(text):  # loose: dates and labels count too
        tok = m.group(0)
        for part in {tok} | set(re.findall(r"\d+(?:\.\d+)?", tok)):
            d = norm(part)
            if d is not None:
                nums.add(d)
    return isos, mds, nums


def styled_tokens(path):
    """Yield (line number, shown text, kind, value) for each token to check."""
    raw = open(path, encoding="utf-8", errors="replace").read()
    out = []
    for n, line in enumerate(raw.splitlines(), 1):
        line = LIST_MARK.sub(lambda m: m.group(1) + " ", line)
        isos, _, _ = pull_dates(line)
        for iso in sorted(isos):
            out.append((n, iso, "iso", iso))
        line = ISO.sub(" ", line)
        for rx, mi, di in ((DAY_MON, 2, 1), (MON_DAY, 1, 2)):
            for m in rx.finditer(line):
                out.append((n, m.group(0), "md", (month_of(m.group(mi)), int(m.group(di)))))
        line = DAY_MON.sub(lambda m: " " + m.group(2) + " ", line)
        line = MON_DAY.sub(lambda m: " " + m.group(1) + " ", line)
        pos = 0
        while True:
            m = STY_NUM.search(line, pos)
            if not m:
                break
            pos = m.end("num")
            pre = line[max(0, m.start("num") - 2):m.start("num")]
            if pre[-1:].isalpha() or pre[-1:] == "_":
                continue  # F1, BAMLC0A2CAA
            if pre[-1:] == "." and pre[:-1].isalnum():
                continue  # H.4.1 and the tail of any dotted label
            d = norm(m.group("num"))
            if d is None:
                continue
            kind = "pct" if m.group("suf") == "%" else "num"
            sign = pre[-1:] if pre[-1:] in "+-−$" else ""
            out.append((n, sign + m.group("num") + m.group("suf")[:3], kind, d))
    return out


def main(argv):
    if len(argv) < 3:
        print("usage: check_numbers.py <styled file> <source file> [<source file> ...]")
        return 2
    isos, mds, nums = set(), set(), set()
    readable = 0
    for p in argv[2:]:
        try:
            i, m, s = read_source(p)
        except OSError as e:
            print(f"WARN cannot read source {p}: {e.strerror}")
            continue
        readable += 1
        isos |= i
        mds |= m
        nums |= s
    if not readable:
        print("ERROR no source file could be read")
        return 2
    try:
        tokens = styled_tokens(argv[1])
    except OSError as e:
        print(f"ERROR cannot read styled file {argv[1]}: {e.strerror}")
        return 2
    missing = []
    for line, shown, kind, val in tokens:
        if kind == "iso":
            ok = val in isos
        elif kind == "md":
            ok = val in mds
        else:
            ok = val in nums or (kind == "pct" and (val / 100).normalize() + 0 in nums)
        if not ok:
            missing.append((line, shown))
    if missing:
        print(f"FAIL {len(missing)} of {len(tokens)} numeric tokens are in no source file:")
        for line, shown in missing:
            print(f"  line {line}: {shown}")
        return 1
    words = len(open(argv[1], encoding="utf-8", errors="replace").read().split())
    print(f"PASS {len(tokens)} numeric tokens, all found in the source files. Word count: {words}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
