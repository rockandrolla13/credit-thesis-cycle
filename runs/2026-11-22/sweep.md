# Skill sweep, 2026-11-23

Question: how much forward AI capex debt supply is priced into US IG and HY spreads.
Chapter files are under `/home/ak/.agents/skills/<skill>/chapters/`. A method-sweep agent read the method chapters. No case chapter was opened before `fresh.md` was frozen.

| Skill | Verdict | What it says for this question | Cite |
|---|---|---|---|
| skill-to-use | Tool | Index. It routed the question to `credit-cycle` and to Willer ch11. | SKILL.md |
| credit-cycle | Relevant, method | Router. It points to the boom, warning-sign and spread chapters used below. | SKILL.md |
| fed-rate-hike | Relevant, method | Router. It points to Willer on credit near the last hike and Axilrod on how the Fed decides. | SKILL.md |
| credit-scenario-grid | Tool | Run on 2026-11-22. 28 rows, 139 scenarios, 20 of 20 reconciliation tests pass. | report.md |
| thesis-builder | Tool | This memo follows its nine steps and four gates. | SKILL.md |
| willer-trading-global-macro | Relevant, method | Supply is endogenous. Issuance rises when demand is strong. Returns correlate -0.12 with same-month supply and +0.22 with supply one month later. "We typically ignore supply forecasts". Near the last hike, credit goes sideways against volatility-matched equities with very negative skew. Private credit behaves as equity beta with lagged marks. To find the next accident, start with the assets that boomed most and ask where the leverage sits. Stated failure: the SLOOS rule failed once when equities dragged credit lower. | ch11-credit.md, ch03-business-cycle.md, ch05-rates-framework.md, ch15-how-to-allocate.md, ch16-private-assets-and-crypto.md |
| axilrod-inside-the-fed | Relevant, method (thin) | The Fed must choose: tighten more than the economy needs, or let imbalances grow. The author says authorities generally chose the second. The neutral rate is "something of a guess". Nothing on spreads. | ch09-concluding-remarks.md |
| dalio-big-debt-crises | Relevant, method | Run the seven-question bubble checklist per market, not per economy. The riskiest debtors miss payments about six months before the economy peaks. More leverage means less tightening is needed to end the boom. The clearest sign is interest paid from new borrowing. Test: does the borrowed money produce income to service the debt? Stated limit: questions, not thresholds. | ch01-credit-debt-and-the-big-debt-cycle-template.md, ch02-deflationary-cycle-early-bubble-top.md |
| dalio-how-countries-go-broke | Not relevant | Sovereign debt arithmetic. Not corporate spreads. | SKILL.md |
| koo-balance-sheet-recession | Relevant, method (narrow) | Classify any banking stress on two axes: local or systemic, loan demand present or absent. | ch01-america-subprime-fiasco.md |
| schularick-taylor-credit-booms | Relevant, method | The danger sign is a credit boom that then slows. Credit that funds investment is not safer. Limit: the measure is bank loans, not bonds. | ch04-credit-booms-and-crisis-prediction.md, ch05-robustness-asset-prices-financial-depth-conclusions.md |
| schulte-credit-driven-economy | Relevant, method (bank side) | Count non-deposit lenders or you miss a "stealth" rise in leverage. Wholesale funding arrives late and leaves together. Loan/deposit ratio is dangerous above 1.2. | ch02-loan-deposit-ratio.md, ch04-tangible-leverage-and-deleveraging-arithmetic.md |
| claessens-financial-globalization | Relevant, method (two rules) | Only a minority of credit booms end in crisis. Aggregate credit can understate a boom that sits in one sector. Separate the catalyst, the trigger and the amplifier. | ch01-commonalities-with-previous-crises.md, ch03-channels-and-mechanisms-of-the-crisis.md |
| hayford-malliaris-asset-prices-crisis | Relevant, method | A bubble lasts while new buyers have both credit access and belief. Shocks amplify when borrowers lose access to financing. Damage scales with how much the financial sector financed the bubble. | ch02-general-characteristics-of-financial-crises.md |
| cassidy-how-markets-fail | Relevant, method | Classify borrowers as hedge, speculative or Ponzi. The mix is the fragility measure, not the total. Herding is rational for managers. | ch16-hyman-minsky-and-ponzi-finance.md, ch14-the-rational-herd.md |
| eichengreen-capital-flows-crises | Not relevant | Cross-border flows and currency crises. | SKILL.md |
| papic-geopolitical-alpha | Relevant, method (tool) | Draw a decision tree. Act only where your probability differs from market pricing. The grid's ordered tests follow this. | ch09-net-assessment.md, ch11-geopolitical-alpha.md |
| simonian-computational-global-macro | Relevant, method (tool) | Write the causal view as a graph. Combine independent causes of one outcome with Noisy-OR. Not applied numerically here. | ch05-causal-inference.md |
| gurevich-trades-of-march-2020 | Relevant, case only | Held for calibration. | see calibration.md |
| christodoulakis-european-periphery-debt-crisis | Not relevant | Sovereign stress in a currency union. | SKILL.md |
| bresciani-turroni-economics-of-inflation | Not relevant | Hyperinflation. | SKILL.md |

Count: 21 skills. 12 relevant as method, 1 case only, 4 not relevant, 4 tools or routers (2 routers also counted as method).

One conflict between books. Willer says to ignore supply forecasts. Dalio and Cassidy (Minsky) treat a debt-financed build-up as the core risk. They measure different things: monthly issuance against returns, versus leverage and borrower quality.
