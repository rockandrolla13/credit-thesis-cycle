# view.json: the text of the one-page view

`build_view.py` builds the page of a run. It takes every number from `readings.json`, `scenarios.json` and the grid script.
`view.json` supplies only the text that the analysis must write. Put the file in the run directory.

Check it with: `python3 /home/ak/.local/share/credit-scenario-grid/cycle/build_view.py --check <run_dir>`

A full example is `/home/ak/.local/share/credit-scenario-grid/runs/2026-11-23/view.json`. Copy its form, never its content.

## Rules for every text

- Use only facts that are in `thesis_full.md` of the same run.
- Plain text. No HTML, no markdown, no angle brackets. The builder escapes every character.
- Sentences of 25 words at most. Active voice. No semicolons. No em dashes.
- Research only. No trades, legs, sizes, hedge ratios, stops, entry levels or exit levels.
- No email addresses. X handles such as `@name` are allowed.
- Never type a market reading or a grid number. Write a token. The builder fills it from the data.
- A number that is not a reading stays as text. Examples: a falsifier threshold, a date, a count of accounts.
- Respect each length limit. The limits keep the labels inside the diagrams. A limit counts the text after the tokens are filled.

## Tokens

Write a token in braces, for example `{CCC}`. An unknown token fails the check.

| Token | Gives | Example |
|---|---|---|
| `{IG}` `{HY}` `{AAA}` `{AA}` `{A}` `{BBB}` `{BB}` `{B}` `{CCC}` | the spread today | `1,361bp` |
| `{CCC_date}` (any spread name) | the date of that print | `19 Nov` |
| `{CCC_chg2d}` (any spread name) | the change over two days | `up 32bp`, `down 4bp`, `unchanged` |
| `{HY_pctile}` (any spread name) | the three-year percentile | `92nd` |
| `{axis}` | the AA to BBB ratio today | `0.581` |
| `{axis_date}` `{axis_pctile}` `{axis_mean}` `{axis_z}` `{axis_min}` `{axis_max}` | axis statistics | `19 Nov`, `92nd`, `0.476`, `2.08`, `0.388`, `0.616` |
| `{fed_upper}` `{ust2y}` `{ust10y}` `{breakeven10y}` | rates | `4.00%` |
| `{vix}` | the VIX | `28.44` |
| `{print_date}` | the date of the IG print | `19 Nov` |
| `{run_date}` `{horizon}` | the run date and the horizon date | `2026-11-23`, `2027-05-23` |
| `{p_S1}` to `{p_S5}` | scenario probability | `28%` |
| `{ratio_S1}` to `{ratio_S5}` | the axis in that scenario | `0.64` |
| `{exp_IG}` `{exp_HY}` | expected six-month move | `+19bp` |
| `{carry_IG}` `{carry_HY}` | widening that income covers | `7bp` |
| `{grid_rows}` `{grid_scenarios}` | size of the grid | `28`, `139` |

## Fields

All fields are required unless marked optional. The number in brackets is the length limit in characters.

- `schema`: the number 1.
- `run_date`: optional. The run date. It must equal the run directory name.
- `question`: optional [90]. The standing question above the title.
- `view` [200]: the view in one sentence of 25 words at most. It becomes the page title.
- `lede` [320]: two to four short sentences under the title. Say what changed in this update.
- `chain`: the causal chain diagram.
  - `source` and `supply`: each has `title` [24], `detail` [68, two lines of 34] and `detail_short` [52, the phone version].
  - `verb` [10]: the word on the arrow between them.
  - `destinations`: 3 to 5 places where the debt goes. Each has `name` [28], `shows_in` [44], `status` (`priced`, `repriced` or `not_priced`), `status_text` [13] and `status_sub` [17].
  - `caption` [220]: one sentence that says what the diagram shows.
  - `note` [420]: the paragraph under the diagram.
- `axis`: `caption` [220], and `note` (optional) [220]. The builder writes the levels, the range and the standard deviations.
- `scenarios`: optional. The builder takes names, probabilities and moves from the grid.
  - `labels`: optional. A longer display name for a spine id [34].
  - `short`: optional. A short name for the axis scale [13].
  - `note`: optional [220]. One sentence, for example whether a probability changed.
- `falsifiers`:
  - `items`: 1 to 6 falsifiers. Each has `id` [4], `claim` [70], `observable` [90], `threshold` [170], `today` [150] and `status` (`not_triggered`, `close` or `triggered`).
  - `meter`: optional, inside an item. `reading` is `axis` or a spread name. `threshold` is a number. `side` is `above` or `below`. The builder draws the reading against the threshold. The item with `"reading": "axis"` also puts its line on the axis scale.
  - `note`: optional [220]. One sentence on the overall status.
- `disagreements`: `groups`, a list. Each group has `title` [60] and `items`. Each item has `question` [90], `a_who` [60], `a` [200], `b_who` [60], `b` [200] and `why` (optional) [200]. Give both sides. Settle none.
- `attention`: the grid of fact strength against attention.
  - `boxes`: the keys `strong_quiet`, `strong_crowded`, `thin_quiet` and `thin_crowded`. A box is `null` when no claim sits there. A filled box has `title` [44], `text` [48] and `trend` (optional) [28], a note on rising attention.
  - `caption` [220] and `note` (optional) [220].
- `pipeline`: what fed the run.
  - `inputs`: 1 to 4 items with `title` [16] and `text` [22]. Give the counts of this run, and say if X was not refreshed.
  - `stages`: 2 to 4 items with `title` [16] and `text` [34]. Each part of `text` between commas has 17 characters at most.
- `limits` [420]: the limits line. The builder writes the word "Limits." before it.

## What the check does

The check fails when a field is missing, a text is too long, a token is unknown, or a text breaks a rule above.
It also fails when the grid numbers differ from `report.md`, or when the grid date differs from the run directory.
It warns when a market reading is typed in and no token is used.
When the check fails, the builder still writes a page. That page has the data diagrams and no text sections.

## One filled example

This example is complete and passes the check for the run of 2026-11-23. The full file has more disagreements.

```json
{
 "schema": 1,
 "run_date": "2026-11-23",
 "question": "How much AI debt supply do US credit spreads price?",
 "view": "Bond spreads price about two thirds of next year's AI debt supply, but not the debt in bank loans, private credit and off-balance-sheet vehicles.",
 "lede": "Top-rated spreads carry the priced part. The market already repriced the weak AI borrowers. This update found no material change.",
 "chain": {
  "source": {"title": "AI capex", "detail": "$230bn in the third quarter, against $199bn operating cash flow", "detail_short": "Q3: $230bn, against $199bn operating cash flow"},
  "verb": "borrows",
  "supply": {"title": "Debt supply", "detail": "A few AA and A companies sell 14% to 20% of 2026 IG issuance", "detail_short": "A few AA and A companies, 14% to 20% of IG issuance"},
  "destinations": [
   {"name": "Public IG bonds", "shows_in": "AA to BBB ratio, {axis} today", "status": "priced", "status_text": "Priced", "status_sub": "about two thirds"},
   {"name": "High yield and weak AI names", "shows_in": "CCC spread {CCC}, a three-year high", "status": "repriced", "status_text": "Repriced", "status_sub": "weak AI names"},
   {"name": "Bank loans", "shows_in": "One loan sale at a mid-80s price", "status": "not_priced", "status_text": "Not priced", "status_sub": "first mark only"}
  ],
  "caption": "The priced part sits in top-rated bond spreads, and the debt in loans is not priced in bonds.",
  "note": "The IG index spread, at {IG}, shows little of the supply effect. Wider spreads also slow projects, and slower projects need less debt."
 },
 "axis": {
  "caption": "The ratio is high against its own three years, and it sits above the 0.52 falsifier line.",
  "note": "The grid puts the ratio near {ratio_S2} if 2027 supply arrives in full."
 },
 "scenarios": {
  "labels": {"S3": "AI digestion (capex cut)"},
  "short": {"S1": "Absorbed", "S2": "Rates grind", "S5": "Accident"},
  "note": "No probability changed in this update."
 },
 "falsifiers": {
  "items": [
   {"id": "F1", "claim": "Top-rated spreads carry a supply premium", "observable": "AA to BBB ratio, FRED",
    "threshold": "Below 0.52 before {horizon}", "today": "{axis}", "status": "not_triggered",
    "meter": {"reading": "axis", "threshold": 0.52, "side": "below"}},
   {"id": "F3", "claim": "Weak credit is repriced", "observable": "CCC spread, FRED",
    "threshold": "Above 1,700bp", "today": "{CCC} on {CCC_date}, {CCC_chg2d} in two days", "status": "not_triggered",
    "meter": {"reading": "CCC", "threshold": 1700, "side": "above"}},
   {"id": "F4", "claim": "The Fed keeps hiking", "observable": "Fed funds upper bound, FRED",
    "threshold": "Still 4.00% after the January 2027 meeting", "today": "{fed_upper}. The next meeting is 9 Dec.", "status": "not_triggered"}
  ],
  "note": "No falsifier is triggered or close."
 },
 "disagreements": {
  "groups": [
   {"title": "In the memo", "items": [
    {"question": "Is HY wide?", "a_who": "Three-year percentile", "a": "Yes. HY at {HY} is at the {HY_pctile} percentile.",
     "b_who": "Ilmanen's long-run average", "b": "No. The 1989 to 2020 average is about 520bp."}
   ]},
   {"title": "Between the X accounts", "items": [
    {"question": "Is credit cheap?", "a_who": "@ZeGoodTrader", "a": "Spreads are back to fair.",
     "b_who": "@deerpointmacro and @Bruce_Markets", "b": "The weakest borrowers still get worse.",
     "why": "The accounts look at different borrowers."}
   ]}
  ]
 },
 "attention": {
  "boxes": {
   "strong_quiet": {"title": "AA supply premium", "text": "One credit letter now names it", "trend": "attention rising from zero"},
   "strong_crowded": {"title": "AI debt is a problem", "text": "Many posts. Weak credit already shows it"},
   "thin_quiet": {"title": "Bank-loan and vehicle store of AI debt", "text": "One account, one loan sale, the BIS loss map"},
   "thin_crowded": null
  },
  "caption": "The AA supply premium has strong facts and little attention, but one widely read letter named it on 22 Nov.",
  "note": "The point is less of an edge once others watch it."
 },
 "pipeline": {
  "inputs": [
   {"title": "17 X accounts", "text": "no collection failure"},
   {"title": "FRED readings", "text": "prints of {print_date}"}
  ],
  "stages": [
   {"title": "35 skills", "text": "23 give a method"},
   {"title": "Scenario grid", "text": "{grid_rows} rows, {grid_scenarios} scenarios"},
   {"title": "Memo", "text": "four gates, all pass"},
   {"title": "Email", "text": "every two days"}
  ]
 },
 "limits": "All spreads are dated {print_date}. The S&P 500 fell 3.7% on 20 Nov, so these spreads may be too low."
}
```
