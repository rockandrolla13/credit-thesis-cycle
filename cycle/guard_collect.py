"""PreToolUse hook for the collect stage. The rules live here, outside the model.

- navigate: only https://x.com/<handle>, or the fixed search address for one handle and
  one date window (history backfill), for a handle in accounts.txt.
- javascript_tool: the model sends one word: COLLECT, SCROLL or SAVE. This hook replaces
  the word with the fixed script of that name. No other script can run.
A post can try to instruct the model. This check cannot be talked out of.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SEARCH = (r"https://x\.com/search\?q=from%3A([A-Za-z0-9_]{1,15})%20since%3A\d{4}-\d{2}-\d{2}"
          r"%20until%3A\d{4}-\d{2}-\d{2}&src=typed_query&f=live")
SCRIPTS = {"COLLECT": "collect.js", "SCROLL": "backfill_scroll.js", "SAVE": "backfill_save.js"}
HANDLES = {h.strip().lower() for h in (HERE / "accounts.txt").read_text().split() if h.strip()}


def block(reason):
    print(f"BLOCKED by guard_collect.py: {reason}", file=sys.stderr)
    sys.exit(2)


def main():
    event = json.load(sys.stdin)
    name = event.get("tool_name", "")
    args = event.get("tool_input") or {}
    if name.endswith("__navigate"):
        url = str(args.get("url", ""))
        m = re.fullmatch(r"https://x\.com/([A-Za-z0-9_]{1,15})", url) or re.fullmatch(SEARCH, url)
        if not m or m.group(1).lower() not in HANDLES:
            block("navigation is limited to listed accounts: the profile or the fixed search address")
        return
    if name.endswith("__javascript_tool"):
        word = str(args.get("text", "")).strip()
        if word not in SCRIPTS:
            block("the only allowed script text is one word: COLLECT, SCROLL or SAVE")
        new = dict(args)
        new["text"] = (HERE / SCRIPTS[word]).read_text()
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
                                                 "permissionDecision": "allow",
                                                 "updatedInput": new}}))
        return


if __name__ == "__main__":
    main()
