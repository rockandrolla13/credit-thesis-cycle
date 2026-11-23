# Skill sweep, 2026-11-23 (update run)

Question: how much forward AI capex debt supply is priced into US IG and HY spreads, six months from 2026-11-23.
Start point: the previous `sweep.md` (35 rows). The index `skill-to-use/SKILL.md` lists the same 35 skills. No row is new.
Chapter files are under `/home/ak/.agents/skills/<skill>/chapters/`.
Opened in this run, before `fresh.md`: the index, `thesis-builder`, `credit-scenario-grid`, `credit-cycle` (SKILL.md), Willer ch11, Ilmanen ch04, Shahidi ch03 and Schulte ch02. All are method files.
No case chapter was opened before `fresh.md` was written.

## Table

| Skill | Verdict | What it says for this question | Cite | Status |
|---|---|---|---|---|
| skill-to-use | Tool | Index of 35 skills. Routes this question to `credit-cycle`, Willer ch11 and the BIS, Van Nieuwerburgh and Chaudhary papers. | SKILL.md | unchanged |
| credit-cycle | Relevant, method | Router to the boom, warning-sign and spread chapters. It now compares eight of the sources added on 23 Nov. Its "Points to Compare" 10 sets Willer, Chaudhary and the BIS side by side on "does supply move spreads" and says to state what each one measures. Point 11 does the same for private credit. | SKILL.md, Points to Compare 10 and 11 | changed: the router now compares the new sources. The verdict is the same. It adds no new claim |
| fed-rate-hike | Relevant, method | Router to Willer on credit near the last hike and Axilrod on how the Fed decides. It does not yet compare the new sources. | SKILL.md | unchanged |
| credit-scenario-grid | Tool | Re-run today on new "now" spreads and unchanged spine probabilities. See `report.md`. | report.md | changed: the 20 Nov prints replace the 19 Nov prints |
| thesis-builder | Tool | This memo follows its nine steps and four gates. | SKILL.md | unchanged |
| willer-trading-global-macro | Relevant, method | Supply is endogenous, so "we typically ignore supply forecasts". Near the last hike, credit goes sideways with very negative skew. Numeric rules checked today, see below. | ch11-credit.md, ch03-business-cycle.md, ch05-rates-framework.md, ch15-how-to-allocate.md, ch16-private-assets-and-crypto.md | unchanged. ch11 opened and its thresholds checked against today's readings |
| axilrod-inside-the-fed | Relevant, method (thin) | The Fed must choose between tightening more than the economy needs and letting imbalances grow. Nothing on spreads. | ch09-concluding-remarks.md | unchanged |
| dalio-big-debt-crises | Relevant, method | Run the bubble checklist per market. The riskiest debtors miss payments about six months before the economy peaks. Test: does borrowed money earn enough to service the debt? | ch01-credit-debt-and-the-big-debt-cycle-template.md, ch02-deflationary-cycle-early-bubble-top.md | unchanged |
| dalio-how-countries-go-broke | Not relevant | Sovereign debt arithmetic. | SKILL.md | unchanged |
| koo-balance-sheet-recession | Relevant, method (narrow) | Classify banking stress as local or systemic, and loan demand as present or absent. | ch01-america-subprime-fiasco.md | unchanged |
| schularick-taylor-credit-booms | Relevant, method | The danger sign is a credit boom that then slows. Limit: the measure is bank loans. | ch04-credit-booms-and-crisis-prediction.md, ch05-robustness-asset-prices-financial-depth-conclusions.md | unchanged |
| schulte-credit-driven-economy | Relevant, method (bank side) | Count non-deposit lenders or you miss a "stealth rise" in leverage. A loan/deposit ratio above 1.2 is the danger zone. | ch02-loan-deposit-ratio.md, ch04-tangible-leverage-and-deleveraging-arithmetic.md | unchanged. ch02 opened. The 1.2 threshold cannot be checked: `readings.json` has no loan/deposit ratio |
| claessens-financial-globalization | Relevant, method (two rules) | Only a minority of booms end in crisis. A boom in one sector can hide in the aggregate. Separate catalyst, trigger and amplifier. | ch01-commonalities-with-previous-crises.md, ch03-channels-and-mechanisms-of-the-crisis.md | unchanged |
| hayford-malliaris-asset-prices-crisis | Relevant, method | A bubble lasts while buyers have credit and belief. Shocks amplify when borrowers lose financing. | ch02-general-characteristics-of-financial-crises.md | unchanged |
| cassidy-how-markets-fail | Relevant, method | The mix of hedge, speculative and Ponzi borrowers is the fragility measure. Herding is rational for managers. | ch16-hyman-minsky-and-ponzi-finance.md, ch14-the-rational-herd.md | unchanged |
| eichengreen-capital-flows-crises | Not relevant | Cross-border flows and currency crises. | SKILL.md | unchanged |
| papic-geopolitical-alpha | Relevant, method (tool) | Draw a decision tree. Act only where your probability differs from the price. | ch09-net-assessment.md, ch11-geopolitical-alpha.md | unchanged. Today's tax threat on overseas data centres is a policy item, but it has no detail to test |
| simonian-computational-global-macro | Relevant, method (tool) | Write the causal view as a graph. Not applied numerically. | ch05-causal-inference.md | unchanged |
| gurevich-trades-of-march-2020 | Relevant, case only | Held for calibration. | see calibration.md | unchanged |
| christodoulakis-european-periphery-debt-crisis | Not relevant | Sovereign stress in a currency union. | SKILL.md | unchanged |
| bresciani-turroni-economics-of-inflation | Not relevant | Hyperinflation. | SKILL.md | unchanged |
| bis-building-ai-on-credit | Relevant, method | The nearest source to the question. Method: test supply news on the term premium, with the IG spread as a second test. Dated result to 18 Sep 2026: term premium +1.53bp on 18 AI news days, gone in two days. IG spread +0.13bp, not significant. Hyperscaler bonds of 10 years or more were about 24% of long corporate issuance in 2026. Loss map: vehicle, then capped guarantee, then insurers and funds, then their banks. A 2008-style run "appears less likely". Trust: 18 days, an association, no threshold. | sec03-spillovers-event-study.md, sec02-financing-structures-risk-allocation.md, sec05-companion-qr-box-on-off-balance-sheet.md | unchanged |
| van-nieuwerburgh-financing-ai-buildout | Relevant, method. sec04 and sec09 are case only | Supply sizing method. Announced capacity is not supply: 43.2% of capacity never completes in the author's scenario. Aggregate leverage hides asset-level leverage in vehicles. Fixed debt service amplifies a modest shortfall. Quoted third-party split for 2025 to 2028: private credit about $800bn, corporate debt about $200bn. Trust: a working paper with no spread model. | sec02-physical-capital-boom.md, sec03-ownership-and-financing.md, sec05-risks.md | unchanged |
| chaudhary-corporate-bond-multipliers | Relevant, method (with a hard limit) | Rating groups are weak substitutes. A demand shock of 1% of a coarse rating group moves its price 3.94%, with no measurable spillover to other IG groups (-0.04). At the fine level the effect is 0.27 on impact and 0.04 a quarter later. Limits: fund flows, not issuance. No AA or BBB number. | sec04-estimation-results.md | unchanged |
| fed-bank-lending-to-private-credit | Relevant, method (bank link) | A way to size bank lines to lending funds and to stress them. A full drawdown costs about 2bp of capital ratio at the largest banks. Bank loans of $349bn fund US private credit vehicles (2025:Q4). The open risk is correlated drawdowns. Trust: the two notes disagree on the size of bank loans. | sec04-direct-exposure-and-drawdown-stress.md, sec07-companion-financial-accounts.md | unchanged |
| campbell-in-search-of-distress-risk | Relevant, method (narrow, issuer level) | For listed weak borrowers, leverage and past share returns are the short-horizon failure signals. Not used for the index-level answer. | sec03-logit-model-of-bankruptcy-and-failure.md | unchanged |
| ilmanen-investing-amid-low-expected-returns | Relevant, method | Turns a spread into expected excess return. IG earned 75bp of a 132bp average spread from 1989 to 2020. HY earned about 2.8% of 5.2%. Default break-even is 15 to 25bp for IG and 200 to 250bp for HY. Check against today: IG 98bp and HY 376bp are both below those long-run averages. | ch04-liquid-asset-class-premia.md | unchanged. ch04 opened and its numbers checked against today's readings |
| shahidi-balanced-asset-allocation | Relevant, method ("priced in" test) | A rate path that follows the yield curve does not move returns. Only the unexpected change does. Check against today: the 2-year yield is 4.76% against a 4.00% policy ceiling. | ch03-drivers-of-returns.md, ch08-other-asset-classes.md | unchanged. ch03 opened. The 2-year print is still dated 19 Nov |
| satchell-forecasting-expected-returns | Relevant, method (tool) | Risk-neutral probabilities are pricing weights, "not the market's beliefs". | ch12-investments-as-bets.md | unchanged |
| rozanov-global-macro-theory-practice | Relevant, method (process) | Scenario grid with joint probabilities. Focus on "vulnerability and consequences", not triggers. Downside risk is highest "when risky assets are rich and volatility levels are low". Not today's state: the VIX is 35.89, at the 99th percentile. | ch06-emerging-markets.md, ch14-gtaa-and-macro-for-long-term-investors.md | unchanged |
| drobny-inside-the-house-of-money | Relevant, case only | Interviews from 2004 and 2005. Held for calibration. | see calibration.md | unchanged |
| drobny-invisible-hands | Relevant, case only (one method line) | Interviews from 2009. One method line: credit "is really just a slice of the equity risk premium". A newsletter author made the same point today (inbox JN1). | ch14-the-pensioner.md, see calibration.md | unchanged |
| suria-event-driven-edge | Not relevant | Equity special situations. | SKILL.md | unchanged |
| cowen-risk-and-business-cycles | Relevant, method | Cheaper finance shifts investment to long, risky projects. Higher volatility of funding cuts long-term investment at once, "without any prior boom". Trust: no model, evidence ends 1997. | ch02-risk-based-theory-real-terms.md, ch03-risk-based-theory-monetary-terms.md | unchanged |
| dalio-changing-world-order | Not relevant | Reserve currencies, empires and internal order. | SKILL.md | unchanged |

Count by verdict: 35 skills. 23 relevant as method (2 of them are routers), 3 case only, 6 not relevant, 3 tools.
No verdict changed. Two rows changed in content: `credit-cycle` and `credit-scenario-grid`.

## Numeric rules checked against today's readings

| Rule | Source | Today's reading | Result |
|---|---|---|---|
| Hold credit only if the last SLOOS loosened | Willer ch11 | DRTSCILM +1.7 (October), net tightening | Rule says do not hold spread risk. Same as the previous run |
| Cut credit when the largest one-year volatility z-score is above 2 | Willer ch11 | VIX 35.89 on 20 Nov, from 24.56 two days before. 99th percentile of three years. HY spread at the 96th percentile | Not computable. `readings.json` has no one-year z-scores and no MOVE or OVX. The earlier judgement that it is triggered is carried, unverified. Today's VIX print makes that judgement more likely, not less |
| Cut equity risk when the VIX jumps 3 points and HY was already wider | Willer ch11 | The VIX rose 11.33 points in two days. HY was 327bp a month before and 376bp now | An equity rule. The six-month HY condition cannot be checked from `readings.json` |
| Prefer HY to IG when the ISM is above 50 | Willer ch11 | No ISM in `readings.json`. October ISM was 55.5 in the grid | Not re-checked today |
| Loan/deposit ratio above 1.2 is dangerous | Schulte ch02 | No reading | Not checkable |
| Spread against default break-even | Ilmanen ch04 | IG 98bp against 15 to 25bp. HY 376bp against 200 to 250bp | Both spreads cover break-even. Both are below their 1989 to 2020 averages of 132bp and about 520bp |
| Only the rate move beyond the curve matters | Shahidi ch03 | 2-year 4.76% (19 Nov), Fed ceiling 4.00% | Hikes to about 4.75% are in the curve. A December hike alone is not a surprise |

## Conflicts between sources

1. Willer says to ignore supply forecasts. Dalio and Cassidy treat a debt-financed build as the core risk. Unchanged.
2. The BIS finds no significant IG spread move on AI financing news days. The thesis reads a supply premium in the AA to BBB ratio. Unchanged. `credit-cycle` now lists this as an open comparison and does not settle it.
3. Ilmanen's long-run averages say HY at 376bp is not wide. The three-year percentile (96th) says it is. The windows differ.
4. The Fed staff arithmetic says bank lines to lending funds are a small direct risk. Schulte says leverage outside deposits is where a rise hides. Unchanged.
