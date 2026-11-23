#!/usr/bin/env bash
# History backfill for the X corpus. Resumable. Safe to stop and start again.
# Usage: backfill.sh [--months 12] [--minutes 240] [--batch 1] [handle ...]
# Keep --batch 1. Chrome permits one automatic download for each tab, so a larger batch loses files.
# It uses the same lock as run_cycle.sh, so the two never use the browser together.
# Log: ~/.local/state/credit-thesis-cycle/backfill.log
set -uo pipefail
CY="$HOME/.local/share/credit-scenario-grid/cycle"
STATE="$HOME/.local/state/credit-thesis-cycle"
mkdir -p "$STATE" "$CY/backfill"
export PATH="$HOME/.local/bin:/usr/bin:/bin"

MONTHS=12; MINUTES=240; BATCH=1; HANDLES=()
while [ $# -gt 0 ]; do
  case "$1" in
    --months) MONTHS="$2"; shift 2 ;;
    --minutes) MINUTES="$2"; shift 2 ;;
    --batch) BATCH="$2"; shift 2 ;;
    *) HANDLES+=("$1"); shift ;;
  esac
done

exec 9>"$STATE/lock"
if ! flock -w 1800 9; then echo "$(date -Iseconds) lock busy; exit" >>"$STATE/backfill.log"; exit 0; fi
exec >>"$STATE/backfill.log" 2>&1
END=$(( $(date +%s) + MINUTES * 60 ))
echo "=== $(date -Iseconds) backfill start (months=$MONTHS minutes=$MINUTES batch=$BATCH)"
EMPTY=0
while [ "$(date +%s)" -lt "$END" ]; do
  URLS=$(/usr/bin/python3 "$CY/backfill.py" plan "$MONTHS" "$BATCH" "${HANDLES[@]}" 2>/dev/null)
  [ -z "$URLS" ] && { echo "all windows done"; break; }
  PROMPT=$(/usr/bin/python3 - "$CY/backfill_prompt.md" "$URLS" <<'PY'
import sys
urls = "\n".join("   - " + u for u in sys.argv[2].split())
print(open(sys.argv[1]).read().replace("{{URLS}}", urls))
PY
)
  OUT=$(timeout 2400 claude -p "$PROMPT" --chrome --settings "$CY/backfill-settings.json" \
        --permission-mode dontAsk --output-format text 2>&1)
  echo "--- $(date -Iseconds) batch result"; echo "$OUT" | tail -n $((BATCH + 4))
  SPLIT=""
  echo "$OUT" | grep -qE "RATELIMIT|NOT SAVED" && SPLIT="--split"
  ING=$(/usr/bin/python3 "$CY/backfill.py" ingest $SPLIT 2>&1)
  echo "$ING" | grep -v "0 new" | tail -n 12
  MOVED=$(echo "$ING" | sed -n 's/^ingest: \([0-9]*\) files.*/\1/p')
  if echo "$OUT" | grep -q "STOPPED: LOGIN"; then echo "X is logged out; exit"; break; fi
  if [ "${MOVED:-0}" = 0 ] || echo "$OUT" | grep -q "STOPPED"; then
    EMPTY=$((EMPTY + 1))
    [ "$EMPTY" -ge 5 ] && { echo "five batches in sequence with a stop or no files; exit"; break; }
    echo "pause 16 minutes (rate limit or no files)"; sleep 960
  else
    EMPTY=0
  fi
done
echo "=== $(date -Iseconds) backfill end; $(/usr/bin/python3 "$CY/backfill.py" status)"
