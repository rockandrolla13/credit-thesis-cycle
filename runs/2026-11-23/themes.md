# Step 1 themes, 2026-11-23

Universe: US and European corporate credit.
Three themes passed the rule. A theme needs two lenses that agree and one mechanism.
The rank is the number of facts minus the number of attention signals.
This is the first run, so every theme has the status `born`.
Fact and attention ids refer to `evidence/streams.md`. Chapter paths are under `/home/ak/.agents/skills/`.

## Ranked themes

### 1. T1. A volatility shock and wider spreads meet a Fed that still leans toward hiking and banks that have started to tighten.

- Lenses: cycle, policy.
- Facts 5 (F3, F4, F5, F7, F16). Attention 2 (A1, A5). Score 3.
- Mechanism: the Fed has not stopped hiking. The 2-year yield is 4.76% against a 4.00% ceiling (`readings.json`, 19 and 23 Nov). A hike on schedule gives no relief, because only a move beyond the curve changes returns (Shahidi ch03). Volatility jumped while HY was already wider, and banks turned to net tightening, which the chapter links to rollover risk and then defaults in the weakest tiers (Willer ch11).
- Winners and losers, as segments: floating-rate leveraged loans relative to HY bonds may hold up better, by Willer's rule for a hiking Fed. CCC and B issuers with near maturities, and the lowest IG tier, are exposed.
- Falsifier: the Fed ceiling (DFEDTARU) and the HY spread (BAMLH0A0HYM2) on the verdict date. The theme is false if the ceiling is below 4.00%. It is also false if the ceiling is above 4.00% and the HY spread is at or below 327bp, its level of 21 Oct.
- Proposed measure: the CCC spread less the BB spread (BAMLH0A3HYC minus BAMLH0A1HYBB), read next to DRTSCILM.
- Verdict date: 2027-02-26.
- Strongest objection: equities look ahead only about three months, and a bear market without a recession does not need a Fed cut to end. `sweep.md` reports an October ISM of 55.5, far from the recession zone below 45. On that reading the shock is noise and the default chain does not start. Source: `willer-trading-global-macro/chapters/ch03-business-cycle.md`. It weakens links 3, 4 and 5.

### 2. T2. Financing of the AI build moved from company cash flow to bank loans, vehicles and asset-backed deals, and it now meets banks and buyers who take less of that paper.

- Lenses: macro, drivers, cycle.
- Facts 3 (F7, F8, F9). Attention 1 (A2). Score 2.
- Mechanism: capex of five large builders passes their operating cash flow in 2026, so the marginal dollar is outside capital (van Nieuwerburgh sec03). That capital comes through project debt, leases, asset-backed deals and bank loans (BIS sec02). In the week to 23 Nov one bank loan sale met muted demand and one public asset-backed sale was delayed (inbox J1 and J2, Exec Sum, 23 Nov). Banks also tightened standards in October (`readings.json`).
- Winners and losers, as segments: top-rated issuers with direct access to public bond markets keep funding. Unrated and below-IG AI infrastructure borrowers, data-centre asset-backed and project debt, and banks that hold unsold data-centre loans are exposed.
- Falsifier: DRTSCILM in the next survey print. The theme is false if the print is at or below 0.0. It is also false if dated reports show that both the ING loan sale and the Zayo public sale were completed.
- Proposed measure: DRTSCILM. There is no public series yet for prices of bank sales of data-centre loans.
- Verdict date: 2027-02-26.
- Strongest objection: hyperscalers generate large cash flows from non-AI segments, and most of the debt is long term, so a run appears less likely. Two deals are a small sample, and a $43bn or $44bn private chip debt deal closed in the same week (F11). Source: `bis-building-ai-on-credit/chapters/sec02-financing-structures-risk-allocation.md`. It weakens links 4 and 5.

### 3. T3. The top-rated issuers began to fund capex with long bonds, and that supply meets buyers who do not substitute across rating tiers.

- Lenses: macro, drivers.
- Facts 3 (F2, F10, F19). Attention 1 (A4). Score 2.
- Mechanism: the largest IG issuers now need outside capital and issue long bonds. Hyperscaler bonds were about 24% of long corporate issuance in 2026, against about 3% in 2024 (BIS sec03). Rating groups are weak substitutes, so a shock to one group moves its own price and does not spread to the rest of IG (Chaudhary sec04). The AA spread sits at the 100th percentile of three years and the BBB spread at the 87th (`readings.json`, 20 Nov).
- Winners and losers, as segments: BBB issuers outside technology, relative to the top tiers. AAA and AA technology issuers and long-dated high-grade bonds are exposed.
- Falsifier: the ratio of the AA spread to the BBB spread on the verdict date. The theme is false if the ratio is at or below 0.476, its three-year mean, while top-rated issuance continues. The ratio is 0.59 now.
- Proposed measure: BAMLC0A2CAA / BAMLC0A4CBBB.
- Verdict date: 2027-05-21.
- Strongest objection: supply is endogenous, and the chapter concludes "we typically ignore supply forecasts". The BIS event study found no significant IG spread move on 18 AI news days (0.13bp, standard error 0.24). Source: `willer-trading-global-macro/chapters/ch11-credit.md`. It weakens links 4 and 5.

## Lens cards

| Lens | Rule applied | Finding | Confidence |
|---|---|---|---|
| macro | Productive-credit test (Dalio ch01) | The largest borrowers now spend more on capex than they earn in operating cash. The added leverage sits in vehicles, leases, guarantees and bank loans. | Supported with a caveat. No revenue or interest-cover series, so the test itself has no answer. |
| cycle | SLOOS rule and VIX jump rule (Willer ch11) | On 20 Nov the Fed was still hiking, banks had turned to net tightening, and both rules pointed away from spread risk. Late stage, cyclical. | Supported with a caveat. No ISM or volatility z-scores in the run. |
| policy | Only the unexpected rate change matters (Shahidi ch03) | Rate markets already hold further Fed hikes, while inflation compensation and oil fell over the month. | Supported with a caveat. No market-implied path. Fiscal evidence is one statement. |
| drivers | Aggregation test (Chaudhary sec04), endogenous supply (Willer ch11) | Supply is the driver that changed. Top-rated issuers kept issuing, and weaker and structured borrowers met buyers who took less paper. | Supported with a caveat. Deal items are second-hand. No default or cash flow series. |

## Observations

One lens only. None is promoted to a theme.

- policy: inflation compensation and oil fell over the month while the Fed still leans toward a hike. The 10-year breakeven is 2.15%, the 5th percentile of three years (F6, F16).
- policy: the US president announced a tax on US firms that build data centres abroad, with no detail (F13).
- drivers: 10% of European leveraged loans trade below 80 while euro BB bonds are flat on the year. One source (F17).
- policy: the ECB is said to be near the end of its hiking cycle and runs off a €250bn corporate bond book. One source (F18).
- drivers: banks try to place about $2bn of hung software buyout debt in HY at about 85 cents. One source (F15).
- cycle: an author argues that credit pays like a sold equity put, so an equity fall leads credit. A narrative, not a fact (N6).

## Blind spots

- Lenses: no lens was empty, but each has gaps. Macro has no revenue or interest-cover series. Cycle has no ISM, housing starts or default rate. Policy has no market-implied rate path. Drivers has no issuance, fund-flow or earnings series.
- Regions: Europe has almost no evidence. `readings.json` holds US series only, and all European items come from one X account. No theme covers Europe.
- Sectors: no evidence on energy, health care, consumer, autos, utilities, US real estate, or financials other than bank loan sales. Almost all evidence is about technology and the AI build.
- Source bias: all 17 X accounts come from one person's follow list. The inbox search used theme terms about AI debt, so it finds AI items by design. Most deal items are second-hand from one newsletter.
- Timing: the spread readings are dated 20 Nov and predate the equity rebound of 23 Nov. Three claims failed a web check and were not counted (F23).
- Missing inputs: the previous evidence pack (inbox I1 to I26 and the older X pack) was not an input of this run. There is no previous `themes.json` and no ledger.
- Skills not relevant: dalio-how-countries-go-broke, eichengreen-capital-flows-crises, christodoulakis-european-periphery-debt-crisis, bresciani-turroni-economics-of-inflation, suria-event-driven-edge, dalio-changing-world-order. Case-only skills were not opened.
- Skills that fit but were not opened, because each card reads at most three chapters: schularick-taylor-credit-booms, schulte-credit-driven-economy, fed-bank-lending-to-private-credit, campbell-in-search-of-distress-risk, cassidy-how-markets-fail, koo-balance-sheet-recession, axilrod-inside-the-fed.
- Instructions in sources: none found. One post states its author's own trade levels and they are not relayed.

This is research only. It contains no trades and no prices.
