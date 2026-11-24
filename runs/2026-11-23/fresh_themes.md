# Fresh themes, run 2026-11-23

Universe: US and European corporate credit.
This file was written before the previous `themes.json`, the ledger and any past-episode chapter were opened.
Only method chapters were used. Fact, narrative and attention ids refer to `evidence/streams.md`.
Chapter paths are under `/home/ak/.agents/skills/`.

## Lens cards

### macro

Question: does the borrowing in this universe pay for itself, and where does leverage sit that the totals do not show?

Chapters read (3):
- `dalio-big-debt-crises/chapters/ch01-credit-debt-and-the-big-debt-cycle-template.md`
- `van-nieuwerburgh-financing-ai-buildout/chapters/sec03-ownership-and-financing.md`
- `bis-building-ai-on-credit/chapters/sec02-financing-structures-risk-allocation.md`

Rule applied: the productive-credit test (Dalio ch01). Ask whether the borrowed money generates enough income to service the debt. The same chapter warns against reading only the aggregate debt chart.

Evidence:
- The 2026 capex estimate of five large builders is $800.5bn against operating cash flow of $707.1bn. The chapter says capex passes cash flow for the first time in 2026 (van Nieuwerburgh sec03, Figure 1).
- Loan-to-value on the infrastructure can rise while reported hyperscaler leverage stays low (van Nieuwerburgh sec03).
- Hyperscalers' off-balance sheet commitments "already exceed their reported debt" (BIS sec02, which cites Moody's).
- In this run: a bank met muted demand for a data-centre loan (F8), an asset-backed sale was delayed (F9), and a large private chip debt deal closed (F11).

Finding: the largest borrowers of this cycle now spend more on capex than they earn in operating cash, and the added leverage sits in vehicles, leases, guarantees and bank loans that company balance sheets do not show.

Confidence: supported with a caveat. The two chapters agree, but their numbers are estimates from October 2026. The run holds no revenue or interest-cover series, so the test itself has no answer. The finding covers the US AI build only.

### cycle

Question: which stage are we in, is it secular or cyclical, and who outperforms at this stage?

Chapters read (2):
- `willer-trading-global-macro/chapters/ch03-business-cycle.md`
- `willer-trading-global-macro/chapters/ch11-credit.md`

Rules applied:
- The SLOOS rule (Willer ch11): hold credit only if the last survey shows looser standards. The October print is 1.7, a net tightening, against 0.0 in July (F7). The rule is not met.
- The VIX jump rule (Willer ch11): a jump of 3 points or more matters when HY spreads were already wider. The VIX rose from 24.56 to 35.89 in two days and HY is 376bp against 327bp a month before (F3, F4). The six-month condition cannot be checked from `readings.json`.
- Credit and the Fed (Willer ch11): around the last hike, credit goes sideways against equities with very negative skew.

Evidence: the Fed ceiling is 4.00% and the 2-year yield is 4.76% (F5). A governor leans toward a December hike (F16). The CCC spread is at its three-year maximum (F3). `sweep.md` reports an October ISM of 55.5 from another file, not re-checked today.

Finding: on 20 Nov the Fed was still in a hiking stage, bank standards had turned to net tightening, and both Willer credit rules pointed away from spread risk. This is a late stage of a tightening cycle, and it is cyclical.

Who outperforms at this stage, by the chapter: equities over credit late in the cycle, loans over HY while the Fed hikes, and higher IG tiers over the lowest IG tiers in acute stress (Willer ch11).

Confidence: supported with a caveat. The run holds no ISM, no housing starts and no one-year volatility z-scores. Willer's numbers are backtests, and the index notes that several rules failed in 2022 to 2023.

### policy

Question: what do monetary, fiscal and regulatory conditions already assume, and what would be a surprise?

Chapter read (1):
- `shahidi-balanced-asset-allocation/chapters/ch03-drivers-of-returns.md`

Rule applied: only the unexpected change in cash rates matters (Shahidi ch03). An upward slope means the market expects hikes. A rate path that follows the curve does not move returns.

Evidence:
- The 2-year yield is 4.76% against a policy ceiling of 4.00% (F5). The curve already holds further hikes.
- The 10-year breakeven fell from 2.37% to 2.15%, the 5th percentile of three years. Oil fell from 108.21 to 89.53 (F6).
- A governor says a 50bp move should be on the table (F16).
- A tax on overseas data centres was announced with no detail (F13). Nvidia faces an SEC inquiry (F14).
- One post says the ECB is still hiking and runs off a €250bn corporate bond book (F18).

Finding: rate markets already hold further Fed hikes, while inflation compensation and oil fell over the month. A hike that follows the curve is not a surprise. A pause, a cut or a 50bp move would be.

Confidence: supported with a caveat. The run holds no market-implied hike path and no Fed statement after the equity fall. The fiscal and regulatory evidence is one statement with no detail. The European evidence is one post.

### drivers

Question: what moves cash flow, default rates and supply in this universe now?

Chapters read (3):
- `willer-trading-global-macro/chapters/ch11-credit.md`
- `chaudhary-corporate-bond-multipliers/chapters/sec04-estimation-results.md`
- `bis-building-ai-on-credit/chapters/sec03-spillovers-event-study.md`

Rules applied:
- Endogenous supply (Willer ch11): issuance rises when demand is strong and is pulled when it is weak.
- The aggregation test (Chaudhary sec04): a shock to one coarse rating group moves its price by a multiplier of 3.94, and the passthrough from the rest of IG is -0.04, not different from zero. Rating groups are weak substitutes.
- The flow share (BIS sec03): hyperscaler bonds of 10 years or more were about 24% of corporate issuance at those maturities in 2026, up from about 3% in 2024.

Evidence:
- Top-rated supply continued in the week of the fall (F10). A $20bn raise closed on 4 Nov (F19).
- Lower-quality and structured supply was pulled or met weak demand (F8, F9, F15).
- The AA spread is at the 100th percentile of three years and the AAA spread at the 99th. The BBB spread is at the 87th (`readings.json`). The AA to BBB ratio is 0.59 against a three-year mean of 0.476 (F2).
- The CCC spread is at its three-year maximum (F3). Bank standards tightened (F7), and the chapter says SLOOS leads defaults.

Finding: supply is the driver that changed. Top-rated issuers kept access and kept issuing, the top rating tiers sit at three-year spread highs relative to BBB, and weaker and structured borrowers met buyers who took less paper.

Confidence: supported with a caveat. The deal items are second-hand and one has no price. Chaudhary measures fund-flow shocks, not issuance, and gives no AA or BBB number. The BIS study found no significant IG spread move on 18 AI news days to 18 September 2026 (0.13bp, standard error 0.24). The run holds no default rate and no cash flow series.

## Themes

### Theme A. A volatility shock and wider spreads meet a Fed that still leans toward hiking and banks that have started to tighten.

Lenses: cycle, policy.

Mechanism:
1. The Fed has not stopped hiking. The 2-year yield is 4.76% against a 4.00% ceiling, and a governor leans toward a December hike (F5, F16).
2. Only a rate move beyond the curve changes returns, so a hike on schedule gives no relief and a larger one is a new shock (Shahidi ch03).
3. Equity volatility jumped while HY spreads were already wider than a month before (F3, F4). Willer's rule treats that pair as a warning (Willer ch11).
4. Bank standards turned to net tightening in October (F7). SLOOS leads defaults: tighter standards mean less lending, more rollover risk, then defaults (Willer ch11).
5. Around the last hike, credit goes sideways with very negative skew, and the lowest tiers carry the rollover risk (Willer ch11). The CCC spread is already at its three-year maximum (F3).

Facts: F3, F4, F5, F7, F16. Attention: A1, A5.
Winners: floating-rate leveraged loans relative to HY bonds, by Willer's rule for a hiking Fed. Losers: CCC and B issuers with near maturities. The lowest IG tier in acute stress.
Horizon: cyclical.

### Theme B. Financing of the AI build moved from company cash flow to bank loans, vehicles and asset-backed deals, and it now meets banks and buyers who take less of that paper.

Lenses: macro, drivers, cycle.

Mechanism:
1. Capex of the five large builders passes their operating cash flow in 2026, so the marginal dollar is outside capital (van Nieuwerburgh sec03).
2. Shells, power and chips go into project debt, leases and asset-backed structures. Banks give construction loans and lend to the funds that hold the debt (van Nieuwerburgh sec03, BIS sec02).
3. Supply of this paper depends on buyers. It is pulled when demand is weak (Willer ch11).
4. Buyers took less: one bank loan sale met muted demand and one public asset-backed sale was delayed (F8, F9). Banks tightened standards in the October survey (F7).
5. Loss beyond the capped guarantees falls on insurers, funds and their bank lenders. Recognition is slow because the claims are hard to value (BIS sec02).

Facts: F7, F8, F9. Attention: A2.
Winners: top-rated issuers with direct access to public bond markets. Losers: unrated and below-IG AI infrastructure borrowers, data-centre asset-backed and project debt, and banks that hold unsold data-centre loans.
Horizon: secular. The shift in funding model is structural. The buyer response is cyclical.
Counter-fact inside this run: a $43bn or $44bn private chip debt deal closed (F11).

### Theme C. The top-rated issuers began to fund capex with long bonds, and that supply meets buyers who do not substitute across rating tiers.

Lenses: macro, drivers.

Mechanism:
1. The largest IG issuers of this cycle now need outside capital for capex (van Nieuwerburgh sec03).
2. They issue long-dated bonds. Hyperscaler bonds were about 24% of long corporate issuance in 2026, against about 3% in 2024 (BIS sec03).
3. They kept issuing in the week of the equity fall and in a second currency (F10, F19).
4. Rating groups are weak substitutes. A shock to one coarse rating group moves its own price and does not pass through to the rest of IG (Chaudhary sec04).
5. So the supply shows in the top tiers and not in the index: AA and AAA spreads sit at three-year highs while the BBB spread does not, and the AA to BBB ratio is 0.59 against a mean of 0.476 (F2).

Facts: F2, F10, F19. Attention: A4.
Winners: BBB issuers outside technology, relative to the top tiers. Losers: AAA and AA technology issuers and long-dated high-grade bonds.
Horizon: secular.

## Observations (one lens only, not promoted)

- policy: inflation compensation and oil fell over the month while the Fed still leans toward a hike (F6, F16).
- policy: a tax on overseas data centres was announced with no detail (F13).
- drivers: 10% of European leveraged loans trade below 80 while euro BB bonds are flat on the year. One source (F17).
- policy: the ECB is said to be near the end of its hiking cycle and runs off a €250bn corporate bond book. One source (F18).
- drivers: banks try to place about $2bn of hung software buyout debt in HY at about 85 cents. One source (F15).
- cycle: an author argues that credit pays like a sold equity put, so an equity fall leads credit (N6). This is a narrative, not a fact.
