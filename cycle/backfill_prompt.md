You collect older posts from X for a private research corpus. This run is unattended.

Rules, in force for the whole run:
1. Read only. You cannot click or type, and you must not try.
2. You never see post text. The scripts return a status word and a count only.
3. If a script returns `LOGIN`, `RATELIMIT` or `UNSURE`, do not call SAVE. Close the tab, print "STOPPED: <word>" and stop all work.

Steps:
1. Call `mcp__claude-in-chrome__tabs_context_mcp` with `createIfEmpty: true`. Use the tab id it returns. Do not use any other tab.
2. For each address in this list, one at a time, in this order:
{{URLS}}
   a. Call `mcp__claude-in-chrome__navigate` with the tab id and the address, unchanged.
   b. Call `mcp__claude-in-chrome__javascript_tool` with `action: "javascript_exec"`, the tab id, and `text: "SCROLL"`. Send exactly that word. A hook replaces it with the script.
   c. If the result starts with `MORE`, do step b again. Do step b at most 30 times for one address.
   d. If the result starts with `DONE`, or you reached 30 calls, call the same tool with `text: "SAVE"`.
   e. If SAVE returns `NOT SAVED`, continue with the next address.
3. Close the tab with `mcp__claude-in-chrome__tabs_close_mcp`.
4. Print one line per address: the account, the first date, then the SAVE result. Then stop.
