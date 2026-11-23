"""History backfill helper. No model involved.

  backfill.py plan <months> <batch> [handle ...]   print the next pending search addresses
  backfill.py ingest [--split]                     move saved files in, mark windows done, merge.
                                                   --split: X stopped the batch, so halve the window that failed
  backfill.py status                               print done and pending counts

A window is one account and one calendar month. Newest months come first, for all accounts.
"""
import datetime
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

CY = Path(__file__).resolve().parent
BF = CY / "backfill"
DONE = BF / "done.txt"
SPLIT = BF / "split.txt"        # windows that X stopped; each is replaced by its two halves
LAST = BF / "last_plan.txt"     # windows of the latest plan, in order
DOWNLOADS = Path(os.environ.get("XC_DOWNLOADS", Path.home() / "Downloads"))
NAME = re.compile(r"xc__([A-Za-z0-9_]{1,15})__(\d{4}-\d{2}-\d{2})__(\d{4}-\d{2}-\d{2})(?: \(\d+\))?\.txt")


def handles():
    return (CY / "accounts.txt").read_text().split()


def done():
    return set(DONE.read_text().split()) if DONE.exists() else set()


def split_set():
    return set(SPLIT.read_text().split()) if SPLIT.exists() else set()


def halves(h, a, b):
    da, db = datetime.date.fromisoformat(a), datetime.date.fromisoformat(b)
    mid = (da + (db - da) // 2).isoformat()
    return [(h, mid, b), (h, a, mid)]          # newer half first


def expand(w, sp):
    """A window marked for a split becomes its halves, to any depth."""
    if key(*w) not in sp:
        return [w]
    return [x for half in halves(*w) for x in expand(half, sp)]


def windows(months, only=None):
    first = datetime.date.today().replace(day=1)
    sp, out = split_set(), []
    for _ in range(months):
        nxt = (first + datetime.timedelta(days=32)).replace(day=1)
        for h in only or handles():
            out.extend(expand((h, first.isoformat(), nxt.isoformat()), sp))
        first = (first - datetime.timedelta(days=1)).replace(day=1)
    return out


def key(h, a, b):
    return f"{h.lower()}__{a}__{b}"


def url(h, a, b):
    return f"https://x.com/search?q=from%3A{h}%20since%3A{a}%20until%3A{b}&src=typed_query&f=live"


def plan(months, batch, only):
    d = done()
    todo = [w for w in windows(months, only) if key(*w) not in d]
    for w in todo[:batch]:
        print(url(*w))
    BF.mkdir(parents=True, exist_ok=True)
    LAST.write_text("\n".join(key(*w) for w in todo[:batch]) + "\n")
    return len(todo)


def mark_split(d):
    """X stopped the latest batch. Halve the first planned window that did not finish."""
    for k in (LAST.read_text().split() if LAST.exists() else []):
        if k in d:
            continue
        h, a, b = k.split("__")
        if (datetime.date.fromisoformat(b) - datetime.date.fromisoformat(a)).days >= 2:
            SPLIT.write_text("\n".join(sorted(split_set() | {k})) + "\n")
            print(f"split: {k} -> two halves")
        else:
            print(f"split: {k} is one day; it stays as it is")
        return


def ingest(split=False):
    (BF / "files").mkdir(parents=True, exist_ok=True)
    (BF / "raw").mkdir(parents=True, exist_ok=True)
    known = {h.lower(): h for h in handles()}
    d, moved = done(), 0
    for f in sorted(DOWNLOADS.glob("xc__*.txt")):
        m = NAME.fullmatch(f.name)
        if not m or m.group(1).lower() not in known:
            continue
        h = known[m.group(1).lower()]
        shutil.move(str(f), BF / "files" / f"xc__{h}__{m.group(2)}__{m.group(3)}.txt")
        d.add(key(h, m.group(2), m.group(3)))
        moved += 1
    DONE.write_text("\n".join(sorted(d)) + "\n")
    if split:
        mark_split(d)
    for h in known.values():
        parts = [p.read_text().strip() for p in sorted((BF / "files").glob(f"xc__{h}__*.txt"))]
        parts = [p for p in parts if p and p != "NO POSTS"]
        if parts:
            (BF / "raw" / f"{h}.txt").write_text("\n=====\n".join(parts) + "\n")
    env = dict(os.environ, XC_RAW=str(BF / "raw"))
    subprocess.run([sys.executable, str(CY / "merge_x.py"), str(BF)], env=env, check=False)
    print(f"ingest: {moved} files moved, {len(d)} windows done")
    return moved


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    if cmd == "plan":
        left = plan(int(sys.argv[2]), int(sys.argv[3]), sys.argv[4:] or None)
        print(f"pending {left}", file=sys.stderr)
    elif cmd == "ingest":
        ingest("--split" in sys.argv)
    else:
        d = done()
        left = [w for w in windows(12) if key(*w) not in d]
        print(f"done {len(d)} windows, pending {len(left)}, split {len(split_set())}")
