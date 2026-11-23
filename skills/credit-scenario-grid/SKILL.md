---
name: credit-scenario-grid
description: "Builds 4 to 5 scenarios for US credit at three levels: the asset classes (investment grade, high yield, and the rating tiers between them), and every sector inside investment grade and high yield. Use when the user asks for credit scenarios, a scenario grid, sector scenarios, spread outcomes by scenario, what is priced into IG or HY spreads, or how a theme such as AI capex supply or a Fed hiking cycle would move credit sectors."
---

# Credit Scenario Grid

Proposes scenarios for credit spreads, then lets a script check them.
You write the stories and the spread moves. The script owns every probability.

## What It Produces

- **A spine.** 4 or 5 macro scenarios. Exactly one is true at the horizon. Probabilities sum to 1.
- **Asset-class rows.** IG, HY, and the rating tiers AA, A, BBB, BB, B, CCC.
- **Sector rows.** Ten IG sectors and ten HY sectors, each with 4 or 5 scenarios.
- **Relations.** HY minus IG, BB minus BBB, and the quality curve inside IG.
- **A report.** One markdown file with every table and every check.

## Steps

1. **Fix the frame.** Write the as-of date and the horizon. Default horizon is 6 months.
2. **Pull today's spreads.** Use the FRED series named in `sectors.md`. Record each as `now`.
3. **Name the drivers.** Pick the two or three forces that matter most now. Cite evidence for each.
4. **Build the spine as a decision tree.** Write an ordered list of tests on observable data. The first true test names the scenario. This makes the scenarios exclusive by construction.
5. **Assign spine probabilities.** Label each `evidence_weighted` or `PM_assumption`. The first label needs an evidence reference.
6. **Write the asset-class rows.** Give a spread change in basis points for each spine scenario.
7. **Write the sector rows.** Read the sector's card in `sectors.md`. Keep the spine as is, or merge and split under the rules there.
8. **Run the script.** `python3 scripts/scenario_grid.py grid.json --md report.md`. Fix every FAIL. Explain every WARN.
9. **Report.** Lead with at most three findings. Put the tables in the file.

Start from `template.json`. Save runs under `~/.local/share/credit-scenario-grid/runs/<date>/`.

## How Sector Probabilities Work

A sector scenario never gets its own free probability.
It draws a stated fraction of one or more spine scenarios.
The script multiplies the fractions by the spine probabilities.
The fractions drawn from each spine scenario must sum to 1 inside a row.
This keeps every sector on the same probability space, so rows can be compared and added up.

## What the Script Checks

- Spine: 4 or 5 scenarios, probabilities sum to 1, each has a test and an observable with a threshold.
- Rows: 4 or 5 scenarios, fractions cover each spine scenario exactly once.
- Splits: every split scenario has its own observable.
- Reconciliation: the weighted average of child rows sits near the parent row, per spine scenario.
- No-trade lint: the grid fails if any text names a trade action, a size or a stop.

## What the Script Computes

- **Expected change.** The probability-weighted spread move.
- **Chance wider.** The summed probability of scenarios with a positive move.
- **Wide/tight ratio.** Probability-weighted widening divided by probability-weighted tightening. Above 1 means the skew points wider.
- **Carry cover.** How much widening the spread income absorbs over the horizon. Needs `now` and `spread_duration`.
- **Fair-value weights.** The scenario weights closest to yours that make today's spread fair. It is the same exponential tilt the creditmacro engine uses. Read it as "what the market must believe", given your outcomes.

## Rules

- **Proposals only.** Say so at the top of every report. The creditmacro engine does not accept invented scenarios. A human must adopt them first.
- **Stop before trades.** No legs, sizes, hedge ratios or stops. Strategy families at most.
- **Keep method and case apart.** Build the spine and the stories from drivers, current data and method material. Use past episodes only to size the moves, and list them under `calibration`.
- **Never state a sector spread level without data.** Free sources do not carry sector spreads. Use changes.
- **Do not hand-edit computed numbers.** Change the inputs and run the script again.
- **Report disagreement.** If a book rule from `willer-trading-global-macro` or another skill conflicts with the grid, say so.

## Scope and Limits

US dollar corporate credit only. No loans, no emerging markets, no European credit.
Spread moves are judgement. The script checks that they are coherent, not that they are right.
The fair-value weights assume today's spread equals the expected future spread. That ignores the risk premium.
Related skills: `willer-trading-global-macro` (credit rules), `credit-cycle`, `fed-rate-hike`, `skill-to-use`.
