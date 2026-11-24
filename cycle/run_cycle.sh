#!/usr/bin/env bash
# Credit thesis cycle: collect X posts, update the corpus, update the thesis, mail it.
# Run by cron every 2 days. Log: ~/.local/state/credit-thesis-cycle/run.log
#
# Usage: run_cycle.sh [--no-send] [--no-collect] [--only-collect] [handle ...]
# Separate Claude runs, each with its own narrow permissions:
#   collect : browser read only, fixed script, writes cycle/raw/        (no mail, no shell)
#   analyse : reads files, Gmail read only, writes the run directory     (no browser, no send)
#   themes  : reads files, writes themes.json in the run directory           (no browser, no mail, no web)
#   send    : reads email.txt, sends one mail to recipients.txt          (nothing else)
# A fourth run is optional and OFF unless the file cycle/publish.enabled exists:
#   publish : reads view.html, updates one published page                (no shell, no mail)
set -uo pipefail

BASE="$HOME/.local/share/credit-scenario-grid"
CY="$BASE/cycle"
STATE="$HOME/.local/state/credit-thesis-cycle"
mkdir -p "$STATE" "$CY/raw" "$CY/state"
export PATH="$HOME/.local/bin:/usr/bin:/bin"

SEND=1; COLLECT=1; ONLY_COLLECT=0; HANDLES=()
for a in "$@"; do
  case "$a" in
    --no-send) SEND=0 ;;
    --no-collect) COLLECT=0 ;;
    --only-collect) ONLY_COLLECT=1 ;;
    *) HANDLES+=("$a") ;;
  esac
done
[ ${#HANDLES[@]} -eq 0 ] && mapfile -t HANDLES < "$CY/accounts.txt"

exec 9>"$STATE/lock"
if ! flock -w 2400 9; then echo "$(date -Iseconds) another job held the lock for 40 minutes; exit" >>"$STATE/run.log"; exit 0; fi
exec >>"$STATE/run.log" 2>&1
echo "=== $(date -Iseconds) start (send=$SEND collect=$COLLECT handles=${#HANDLES[@]})"

DATE=$(date +%F)
export CYCLE_RUN_ID="$DATE-$$"
RUN="$BASE/runs/$DATE"
PREV=$(ls -d "$BASE"/runs/*/ 2>/dev/null | sed 's#/$##' | grep -v "/$DATE\$" | while read -r d; do [ -f "$d/thesis.md" ] && echo "$d"; done | sort | tail -1)
# A test may name the previous run itself: CYCLE_PREV=<dir with thesis.md> run_cycle.sh ...
[ -n "${CYCLE_PREV:-}" ] && [ -f "$CYCLE_PREV/thesis.md" ] && PREV="$CYCLE_PREV"
mkdir -p "$RUN/evidence"

render() { sed -e "s|{{DATE}}|$DATE|g" -e "s|{{RUN}}|$RUN|g" -e "s|{{PREV}}|$PREV|g" -e "s|{{HANDLES}}|${HANDLES[*]}|g" "$1"; }

# 1. Collect. Needs Chrome open, with the Claude extension, logged in to X. A failure is not fatal.
rm -f "$CY"/raw/*.txt
if [ "$COLLECT" = 1 ]; then
  timeout 2700 claude -p "$(render "$CY/collect_prompt.md")" --chrome \
    --settings "$CY/collect-settings.json" --permission-mode dontAsk --output-format text \
    >"$RUN/collect.log" 2>&1
  echo "collect exit $? ; raw files: $(ls "$CY"/raw/*.txt 2>/dev/null | wc -l)"
else
  echo "collect skipped by flag" >"$RUN/collect.log"
fi
[ -n "$(ls "$CY"/raw/*.txt 2>/dev/null)" ] || echo "FAILED: no posts collected. Chrome may be closed or X may be logged out." >>"$RUN/collect.log"

# 2. Merge into the corpus. Plain Python.
/usr/bin/python3 "$CY/merge_x.py" "$RUN" || echo "WARN merge_x.py failed"
[ "$ONLY_COLLECT" = 1 ] && { echo "=== $(date -Iseconds) end (only collect)"; exit 0; }

# 3. Market readings. Plain Python.
/usr/bin/python3 "$CY/fred_pull.py" "$RUN/readings.json" || echo "WARN fred_pull.py failed"

# 4. Analyse. Needs a previous thesis to update.
if [ -z "$PREV" ]; then echo "FAIL no previous run with thesis.md; build the baseline first"; exit 1; fi
[ -f "$RUN/scenarios.json" ] || cp "$PREV/scenarios.json" "$RUN/scenarios.json"
timeout 4500 claude -p "$(render "$CY/analyse_prompt.md")" \
  --settings "$CY/analyse-settings.json" --permission-mode dontAsk --output-format text \
  >"$RUN/analyse.log" 2>&1
echo "analyse exit $?"

# 4b. Step 1 themes. A separate run with its own narrow permissions. A failure is not fatal.
#     The model proposes themes.json. check_themes.py decides, writes the ledger and adds the block to the email.
if [ -f "$CY/themes_prompt.md" ] && [ ! -f "$CY/themes.disabled" ]; then
  timeout 2400 claude -p "$(render "$CY/themes_prompt.md")" \
    --settings "$CY/themes-settings.json" --permission-mode dontAsk --output-format text \
    >"$RUN/themes.log" 2>&1 < /dev/null
  echo "themes exit $?"
  if /usr/bin/python3 "$CY/check_themes.py" "$RUN" --ledger "$CY/ledger/themes.jsonl"; then
    [ -s "$RUN/email.txt" ] && /usr/bin/python3 "$CY/check_themes.py" "$RUN" --email "$RUN/email.txt" | tail -n 1
  else
    echo "WARN themes failed the check; the email goes out without the themes block"
  fi
fi

# 5. Build the one-page view. Plain Python. A failure is a warning, never fatal.
rm -f "$RUN/view.html"
/usr/bin/python3 "$CY/build_view.py" "$RUN" "$RUN/view.html" || echo "WARN build_view.py failed; this run has no view.html"

# 6. Publish the page. OFF unless cycle/publish.enabled exists. A failure is not fatal.
if [ -f "$CY/publish.enabled" ] && [ -s "$RUN/view.html" ]; then
  timeout 300 claude -p "$(render "$CY/publish_prompt.md")" \
    --settings "$CY/publish-settings.json" --permission-mode dontAsk --output-format text
  echo "publish exit $?"
elif [ -f "$CY/publish.enabled" ]; then
  echo "WARN publish is on, but there is no view.html; nothing published"
else
  echo "publish skipped (no publish.enabled file)"
fi

# 7. Send one email. Only if the analysis wrote it.
if [ "$SEND" = 1 ] && [ -s "$RUN/email.txt" ]; then
  timeout 300 claude -p "$(render "$CY/send_prompt.md")" \
    --settings "$CY/send-settings.json" --permission-mode dontAsk --output-format text
  echo "send exit $?"
elif [ "$SEND" = 1 ]; then
  echo "FAIL no email.txt; nothing sent"
else
  echo "send skipped by flag"
fi
rm -f "$CY/state/sends-$CYCLE_RUN_ID.count"
echo "=== $(date -Iseconds) end"
