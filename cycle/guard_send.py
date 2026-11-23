"""PreToolUse hook for the send stage. Blocks (exit 2) any Gmail send that
addresses anyone outside recipients.txt, uses cc or bcc, sends a draft,
carries an attachment, or is the second send of the run."""
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ALLOWED = {a.strip().lower() for a in (HERE / "recipients.txt").read_text().split() if a.strip()}
STATE = HERE / "state"


def block(reason):
    print(f"BLOCKED by guard_send.py: {reason}", file=sys.stderr)
    sys.exit(2)


def main():
    event = json.load(sys.stdin)
    if not event.get("tool_name", "").endswith("__send_message"):
        return
    args = event.get("tool_input") or {}
    if args.get("cc") or args.get("bcc"):
        block("cc and bcc are not allowed")
    if args.get("draftId") or args.get("attachments") or args.get("replyThreadId") or args.get("replyToMessageId"):
        block("drafts, attachments and replies are not allowed")
    to = {a.strip().lower() for a in args.get("to") or []}
    if not to or not to <= ALLOWED:
        block("a recipient is missing or not in recipients.txt")
    counter = STATE / f"sends-{os.environ.get('CYCLE_RUN_ID', 'manual')}.count"
    if counter.exists():
        block("this run already sent its one email")
    counter.write_text("1")


if __name__ == "__main__":
    main()
