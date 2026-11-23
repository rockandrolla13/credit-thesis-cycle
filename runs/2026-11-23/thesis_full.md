# Thesis: AI capex debt supply and US credit spreads

As of 2026-11-23. Horizon 2027-05-23. Research only. No trades.
All four gates pass (see the end). Scenario probabilities are proposals.

**Status of this update: spreads are wider, the thesis stands.** FRED published the 20 Nov prints. Every credit spread widened and the axis rose. No falsifier triggered and no scenario probability moved.
X was refreshed: the collection log shows 17 accounts and no failure.
The grid script passed on the first run. No source contained instructions.

## What changed since the previous memo

1. The spreads now include the equity fall of 20 Nov. IG is 98bp, from 94bp. HY is 376bp, from 352bp. CCC is 1,402bp, from 1,361bp. The VIX closed at 35.89 on 20 Nov, from 28.44 on 19 Nov.
2. The axis rose to 0.590, from 0.581. AA widened more than BBB in proportion during a flight from risk. AA is at the top of its three-year range.
3. A second bank met weak demand for a data-centre loan sale: ING, $500m, "muted demand" (Exec Sum, 23 Nov 2026, second-hand, no price). The first was HSBC at a mid-80s price.
4. Two reports could matter and are not confirmed. One X account says the Nvidia board reinstated its former chief executive on 23 Nov. One X account says Google cut a 2027 chip order by about 20%. Each is one source. Each failed a web check.
5. The US president said on 20 Nov that the US will tax US firms that build data centres abroad. There is no detail.

The fact that qualifies the update: two X accounts describe a sharp equity rebound on 23 Nov. The spreads are dated 20 Nov, so they may now be too wide.

## 1. The thesis in one sentence

The bond market prices about two thirds of next year's AI debt supply in top-rated spreads and has repriced the weak AI borrowers, but it does not yet price the AI debt that sits in bank loans, private credit and off-balance-sheet vehicles.

## 2. The causal chain

1. A few AA and A rated companies sell a large share of new debt. Their share of 2026 IG issuance is between 14% and 20%.
2. That supply lifts top-rated spreads against lower-rated spreads. Rating tiers are weak substitutes, so the pressure stays in the tier.
3. Part of the supply effect lands in Treasury yields and not in spreads. The IG index spread is a weak gauge of supply.
4. Fed hikes raise the yield on safe assets, but the yield curve already holds about three hikes. Only a surprise in the path is new.
5. The market sorts AI borrowers by the support of a big-tech customer.
6. Borrowers move debt into vehicles, bank loans and private credit. That costs more, and it leaves the bond indices.
7. Bank-held AI loans are starting to show marks.
8. Wider spreads and higher volatility slow projects, and slower projects need less debt. This limits link 1.
9. A capex cut does not remove signed leases. Less bond supply can arrive with more stress at vehicles and lenders.

Sources for each link are in `fresh.md`. No link was added or removed today.

## Causal chain, explained

Section 2 is unchanged. This section starts from the same section of the previous memo and from the previous `chain_skills.md`.
That file tested each link against all 35 skills. 29 of the 35 skills say something on at least one link. 6 are silent on all eight.
Today I re-tested only the links that new evidence touches: L2, L4, L6 and L7. No new skill arrived.
The eight links below merge links 6 and 7 of section 2 into L6.
Skill chapter files are under `/home/ak/.agents/skills/<skill>/chapters/`. A past episode is labelled "analogue" and is not evidence.

**L1. A few AA and A issuers supply 14% to 20% of 2026 IG issuance.** Verdict: well supported. Unchanged.
- Mechanism: the capex of the largest spenders now exceeds their operating cash flow, so the marginal dollar is borrowed. They borrow at long maturities in the public IG market.
- Evidence: one fifth of a record $1.9tn of IG issuance (previous inbox pack, I2), against 14% of non-financial IG from the same author. Third-quarter capex of $230bn against operating cash flow of $199bn (previous inbox pack, I3). Hyperscaler bonds of 10 years or more were about 24% of long corporate issuance in 2026, from about 3% in 2024 (bis-building-ai-on-credit/chapters/sec03-spillovers-event-study.md, data to September 2026). New: Alphabet sold $4.2bn of bonds in Canada in the week of the fall (`evidence/inbox.md`, J5).
- Best source: bis sec03 for the share of long issuance. van-nieuwerburgh-financing-ai-buildout/chapters/sec03-ownership-and-financing.md for the cash-flow constraint.
- Qualifier: the 14% and the one fifth do not reconcile. One X account now gives $620bn of hyperscaler debt in 2026 (`evidence/x.md`, O2). That is far above the $370.7bn LSEG count and has no definition. No skill gives a share of all IG issuance.

**L2. That supply lifts top-rated spreads against lower-rated spreads, and the pressure stays in the tier.** Verdict: supported with a caveat. Re-tested today.
- Mechanism: the tier is the AA and A rating group. Investors treat rating groups as weak substitutes, so a tier must clear its own supply at its own price.
- Evidence: the AA to BBB ratio is 0.590 against a three-year mean of 0.476. The previous memo had 0.581. AA is at the 100th percentile of its three-year range, A at the 83rd and BBB at the 87th (`readings.json`). The previous memo had the 99th, the 76th and the 80th. The gap between A and AA is 9bp, from 10bp in the previous memo and 18bp a year ago (`report.md`). A demand shock of 1% of a coarse rating group moved its price 3.94%, with a passthrough of -0.04 to the rest of IG (chaudhary-corporate-bond-multipliers/chapters/sec04-estimation-results.md).
- New today: in the two days to 20 Nov, AA widened 5bp from 67bp and BBB widened 6bp from 116bp. The ratio rose from 0.578 to 0.590 in a flight from risk (`readings.json`). A capex-cut reading of last week predicts a lower ratio. This is two days of data, so it is weak support.
- Best source: chaudhary sec04 for the mechanism. FRED for the reading.
- Qualifier: Chaudhary measures fund flows, not issuance. At a finer level its effect was 0.27 in the shock quarter and 0.04 one quarter later (sec04, Table 6). It gives no AA or BBB number.
- Contradiction: Willer says supply is endogenous and does not forecast returns. The correlation of returns with same-month supply is -0.12, and +0.22 with returns one month later. "We typically ignore supply forecasts." (willer-trading-global-macro/chapters/ch11-credit.md, a backtest, opened today). The `credit-cycle` router now lists this as an open comparison (its point 10) and says to state what each source measures. Not settled.

**L3. Part of the effect lands in Treasury yields, so the IG index spread is a weak gauge of supply.** Verdict: supported with a caveat. Unchanged.
- Mechanism: long AI bonds go to the investors who hold long Treasuries. More long supply raises the term premium, which is the extra yield for holding long bonds. The index spread is measured over Treasuries, so it misses that part.
- Evidence: on 18 AI news days the 10-year term premium rose 1.53bp and the IG index spread moved 0.13bp, not significant (bis sec03). The 10-year yield is 5.04% (`readings.json`, dated 19 Nov).
- Best source: bis sec03.
- Qualifier: the BIS effect was gone in two days. The authors call it an association on 18 days and not a cause. Chaudhary assumes corporate bonds and Treasuries are weak substitutes (chaudhary sec06-conclusion.md).

**L4. The curve already holds about three Fed hikes, so only a surprise in the path is new.** Verdict: supported with a caveat. Re-tested today.
- Mechanism: a rate path that follows the yield curve does not move returns. Only the part the curve did not hold moves them.
- Evidence: the 2-year yield is 4.76% against a 4.00% policy ceiling (`readings.json`, the 2-year print is dated 19 Nov). Markets priced a December hike near 96% before the fall (previous inbox pack, I22).
- New today: no source gives the odds after the fall. A web search found only older figures. The VIX closed at 35.89 on 20 Nov (`readings.json`). One table shows no hike since 1990 on a day with the VIX above 30 (`calibration.md`, an analogue).
- Best source: shahidi-balanced-asset-allocation/chapters/ch03-drivers-of-returns.md, opened today.
- Qualifier: a priced probability is a pricing weight, not the market's belief (satchell-forecasting-expected-returns/chapters/ch12-investments-as-bets.md). The 2-year yield has no print after the fall, so the "three hikes" may be stale.

**L5. The market sorts AI borrowers by the support of a big-tech customer.** Verdict: supported with a caveat. Unchanged.
- Mechanism: the customer's lease pays the debt. A long contract with an investment-grade customer makes project debt financeable. A borrower without one stands on its own credit.
- Evidence: Oracle CDS is 341bp and CoreWeave CDS passed 1,200bp (section 6). CCC spreads are 1,402bp, from 1,361bp (`readings.json`). Lenders price data-centre debt from the customer's credit (previous X pack, O2, one account).
- Best source: van-nieuwerburgh sec03 and bis-building-ai-on-credit/chapters/sec02-financing-structures-risk-allocation.md.
- Qualifier: the support is partial and typically capped (bis sec02). The direct evidence is two posts by one account.

**L6. Debt moves into vehicles, bank loans and private credit, where it costs more and leaves the bond indices. Bank-held AI loans start to show marks.** Verdict: supported with a caveat. The sub-claim on marks is still thin, but less thin than before. Re-tested today.
- Mechanism: a vehicle is a separate company that owns the data centre and issues the debt. The spender keeps the debt off its balance sheet and pays for that through the lease. Private debt is not in the bond indices and is marked late.
- Evidence: a vehicle's A-rated notes priced about 80bp wider than its parent's BBB bonds (previous inbox pack, I7). One quoted split for 2025 to 2028 puts private credit near $800bn and corporate debt near $200bn (van-nieuwerburgh sec03, a Morgan Stanley figure). Bank loans of $349bn fund US private credit vehicles at 2025:Q4 (fed-bank-lending-to-private-credit/chapters/sec07-companion-financial-accounts.md). A bank passed on a $300m piece of a data-centre loan at a mid-80s price (previous inbox pack, I13).
- New today: a second bank, ING, met "muted demand" for a $500m data-centre loan sale (`evidence/inbox.md`, J1). A fibre company delayed the $1bn public leg of an ABS sale (J2). The marks now rest on two loan sales at two banks. The second has no price and is second-hand.
- Best source: van-nieuwerburgh sec03 for the relocation. bis sec02 for the price.
- Contradiction on cost: private credit lenders priced AI loans like other loans, 6.2 against 6.1 points over the base rate (bis-building-ai-on-credit/chapters/sec04-companion-bulletin-120-cash-flows-to-debt.md, January 2026). The higher cost is shown for vehicle notes, not for private loans. Not settled.
- Qualifier: a full draw of bank lines to lending funds cost about 2bp of capital ratio on 2024 data (fed sec04-direct-exposure-and-drawdown-stress.md). Schulte says leverage outside deposit banks is where a rise hides (schulte-credit-driven-economy/chapters/ch02-loan-deposit-ratio.md, opened today).

**L7. Wider spreads slow projects, and slower projects need less debt.** Verdict: thin. Re-tested today.
- Mechanism: this is the balancing loop. Costly or volatile funding cuts long, risky projects first, and a cancelled project needs no bond.
- Evidence: 43.2% of announced capacity never completes in one scenario (van-nieuwerburgh sec02-physical-capital-boom.md, the author's assumption). None of a $500bn chip-financing pledge has been deployed (previous inbox pack, I15).
- New today: one X account reports that Google cut a 2027 chip order by about 20% (`evidence/x.md`, O5). One source, not found by web search, and a chip order is not capex guidance. A data-centre company paused a US share listing (`evidence/inbox.md`, J4). Neither shows a project slowed by spreads.
- Best source: cowen-risk-and-business-cycles/chapters/ch02-risk-based-theory-real-terms.md. Willer ch11 agrees that issuance follows demand.
- Qualifier: Cowen reports that firms set hurdle rates at three or four times the cost of capital, so rates matter little for when to commit. Competitors rarely pull back alone (cassidy-how-markets-fail/chapters/ch11-the-prisoners-dilemma-and-rational-irrationality.md). No large spender has cut 2027 capex guidance in any source.

**L8. A capex cut does not remove signed leases, so less bond supply can arrive with more stress at vehicles and lenders.** Verdict: supported with a caveat. Unchanged.
- Mechanism: debt service is fixed and revenue is not. A modest shortfall becomes a large loss for junior claims. A spender that cuts can protect its own sites and leave the leased ones.
- Evidence: about $1.3tn of signed leases have not started (previous inbox pack, I4, one letter). The BIS has about $820bn of $1.2tn at mid-2026 on a Moody's count (bis sec01-ai-credit-boom-scale.md).
- Best source: van-nieuwerburgh-financing-ai-buildout/chapters/sec05-risks.md. bis sec02 gives the loss order: vehicle, capped guarantee, insurers and funds, their banks.
- Qualifier: some leases run on short first terms with options to renew. A run on short-term funding "appears less likely" (bis sec02).

**What would be true if we were wrong.** This is interpretation. If supply did not matter, AA spreads would move with the rest of IG. The ratio would sit near its three-year mean of 0.476, and AA would rank in its own range about where BBB ranks. The files show the ratio at 0.590, AA at the 100th percentile and BBB at the 87th. The gap between A and AA fell from 18bp to 9bp in a year. Last week adds a test. In a flight from risk with no supply effect, BBB should widen more than AA in proportion, and the ratio should fall. It rose from 0.578 to 0.590. In our view supply explains that pattern best. Two things fit the opposite view. The BIS found a 0.13bp index move on AI news days. And the top tier now holds the AI names, so last week's rise in the ratio may show fear about those names and not supply. The ratio has not passed its peak of 0.616 on 2 Sep 2026.

**The strongest objection.** This is interpretation. Willer ch11 is the strongest contradiction in the library: supply is endogenous, so it does not forecast returns. In our view it weakens L2 and with it the estimate that top ratings price two thirds. It rests on backtests of monthly supply against returns. It does not compare one tier with another, and it does not touch L5, L6 or L8. Chaudhary adds a time limit: if a flow effect fades within a quarter, the premium needs continuing supply. A second objection is new today. If the AA names widen because their equity fell, the ratio measures AI credit risk and not supply. The files cannot separate the two.

**Numbers used in the styled chain and their sources**

| Number | Source |
|---|---|
| 14% to 20% of 2026 IG issuance. $1.9tn | previous inbox pack, I2 and its flag |
| Capex $230bn against operating cash flow $199bn | previous inbox pack, I3 |
| About 24% of long corporate issuance, from about 3% in 2024 | bis sec03-spillovers-event-study.md |
| Ratio 0.590, previous 0.581, mean 0.476, peak 0.616. Two days before 0.578. AA 100th percentile, A 83rd, BBB 87th. 10-year 5.04%. 2-year 4.76%. Ceiling 4.00%. CCC 1,402bp. VIX 35.89 | `readings.json` |
| AA 72bp from 67bp, up 5bp. BBB 122bp from 116bp, up 6bp, in two days | `readings.json` |
| A minus AA 9bp, from 18bp a year ago | `report.md` |
| 1% shock, 3.94% price move, passthrough -0.04. 0.27 then 0.04 | chaudhary sec04-estimation-results.md |
| Correlations -0.12 and +0.22 | willer ch11-credit.md |
| 18 news days. Term premium 1.53bp, about 1.5bp. IG spread 0.13bp | bis sec03-spillovers-event-study.md |
| December hike near 96%, before the fall | previous inbox pack, I22 |
| Oracle CDS 341bp. CoreWeave CDS above 1,200bp | section 6 of this memo |
| Vehicle notes about 80bp wider | previous inbox pack, I7 |
| Private credit about $800bn, corporate debt about $200bn | van-nieuwerburgh sec03-ownership-and-financing.md |
| Bank loans of $349bn to private credit vehicles, 2025:Q4 | fed sec07-companion-financial-accounts.md |
| 6.2 against 6.1 points | bis sec04-companion-bulletin-120-cash-flows-to-debt.md |
| About 2bp of capital ratio | fed sec04-direct-exposure-and-drawdown-stress.md |
| $300m loan piece at a mid-80s price | previous inbox pack, I13 |
| $500m loan sale, muted demand. $1bn ABS leg delayed. $4.2bn Alphabet bond | `evidence/inbox.md`, J1, J2, J5 |
| 43.2% of capacity not completed | van-nieuwerburgh sec02-physical-capital-boom.md |
| $500bn pledge, none deployed | previous inbox pack, I15 |
| Chip order cut of about 20%, unconfirmed | `evidence/x.md`, O5 |
| $1.3tn of leases not started | previous inbox pack, I4 |
| About $820bn of $1.2tn of leases | bis sec01-ai-credit-boom-scale.md |
| 35 skills, 29 with something to say, 6 silent | previous `chain_skills.md` |

## 3. The operational axis

**AA to BBB spread ratio.** FRED BAMLC0A2CAA divided by BAMLC0A4CBBB. Daily history from November 2023.

- Today: 0.590 (AA 72bp, BBB 122bp, reading dated 20 Nov 2026). Previous memo: 0.581 (AA 68bp, BBB 117bp, dated 19 Nov).
- Two days before today's print: 0.578. One month before: 0.578.
- Three-year range: 0.388 to 0.616. Mean 0.476.
- Today is at the 94th percentile and 2.25 standard deviations above the mean. The previous memo had the 92nd percentile and 2.08. The peak was on 2 Sep 2026.

A high ratio means the market charges top-rated issuers more than usual against BBB issuers. That is what heavy top-rated supply does.

**Readings against the previous memo**

| Reading | Previous memo | Today | Change | Two days before today's print |
|---|---|---|---|---|
| Axis, AA over BBB | 0.581 | 0.590 | up 0.009 | 0.578 |
| IG spread | 94bp | 98bp | up 4bp | 93bp |
| HY spread | 352bp | 376bp | up 24bp | 347bp |
| CCC spread | 1,361bp | 1,402bp | up 41bp | 1,353bp |
| Fed funds upper bound | 4.00% | 4.00% | none | 4.00% |
| 2-year Treasury yield | 4.76% | 4.76% | none, same 19 Nov print | 4.80% |

The spreads are dated 20 Nov. The 2-year and 10-year yields are still dated 19 Nov.
Other ratings on 20 Nov: A 81bp from 78bp. BB 229bp. B 408bp. AAA 50bp.
Three-year percentiles on 20 Nov: IG 87th, HY 96th, CCC 100th, AAA 99th.
The S&P 500 closed at 6,910.39 on 20 Nov, from 7,323.63 two days before. The VIX closed at 35.89, from 24.56 two days before.
Over one month IG widened 10bp, HY 49bp and CCC 95bp (`readings.json`).

## 4. What the market already prices

- **Top ratings: about two thirds.** About 14bp of the 72bp AA spread is supply premium. The previous memo had about 12bp of 68bp. The grid now puts the ratio near 0.65 if 2027 supply arrives in full, from 0.64. Today's gap from the mean is 0.114 of a possible 0.174. This is a judgement, not a measurement.
- **Treasury yields: some, of unknown size.** The BIS measured about 1.5bp on the 10-year term premium on AI news days, gone in two days (bis sec03, to September 2026).
- **Weak AI borrowers: repriced.** CCC spreads are 1,402bp, a new three-year high. Oracle CDS is 341bp.
- **The HY index: not cheap on a long view.** HY is at the 96th percentile of three years. It is below its 1989 to 2020 average of about 520bp (ilmanen ch04, opened today).
- **The IG index: not much.** IG is 98bp. That level is fair only if "Supply absorbed" has a 58% chance. The grid gives it 28%. The 58% did not change, although IG widened 4bp. Read the 58% as a pricing weight, not as the market's belief (satchell ch12).
- **Bank loans, private credit and vehicles: not priced in bonds.** Two banks have now met weak demand for data-centre loans. One sold at a mid-80s price. That is two marks, not a market.
- No source gives a number for this question. The estimates above are mine.

## 5. Scenarios

From `report.md`. The script passed on the first run: 28 rows, 139 scenarios, no warnings.
Probabilities are proposals. Moves are six-month spread changes from today's spreads. No probability changed today.

| Scenario | Previous | Today | Label | IG | HY | Ratio |
|---|---|---|---|---|---|---|
| Supply absorbed | 28% | 28% | PM_assumption | -12 | -52 | 0.60 |
| Higher rates, supply grind | 37% | 37% | evidence_weighted | +14 | +18 | 0.65 |
| AI digestion (capex cut) | 18% | 18% | PM_assumption | +18 | +108 | 0.47 |
| Hard landing | 10% | 10% | PM_assumption | +56 | +248 | 0.52 |
| Funding accident | 7% | 7% | PM_assumption | +116 | +498 | 0.55 |

The ratio column changed because the starting spreads changed. The previous memo had 0.59, 0.64, 0.46, 0.51 and 0.55.
Expected move: IG +19bp, HY +71bp. Income covers 7bp of IG widening and 61bp of HY widening. The previous memo had 57bp for HY.
The two tail scenarios hold 17% of the probability and about three quarters of the expected IG move.
A capex cut helps the debt of the large spenders and hurts those who lent against the build.

Why nothing moved:
- The 20 Nov prints confirm the size of a fall that the previous memo already knew about.
- The two reports that could move a probability by 5 points are each one unconfirmed source. They point in opposite directions.
- The second loan sale supports "Funding accident" a little. No source reports funding stress, a bank failure or a shut primary market.
- No scenario test has triggered.

One caution for the PM. The moves are changes from today. The month to 20 Nov already delivered IG +10bp and HY +49bp. That is about half of the "AI digestion" move. I kept the moves and did not re-base them.

## 6. Evidence

**Observations for**
- AA is at the top of its three-year range and the ratio rose in a flight from risk (FRED, 20 Nov 2026).
- Hyperscalers are about one fifth of a record $1.9tn of IG issuance (JunkBondInvestor, 22 Nov 2026, with an LSEG count found by web search).
- Hyperscaler capex exceeded operating cash flow in the third quarter, $230bn against $199bn (JunkBondInvestor, 22 Nov 2026).
- A vehicle's A-rated notes priced about 80bp wider than its parent's BBB bonds (JunkBondInvestor, 22 Nov 2026).
- Oracle CDS is 341bp (JunkBondInvestor, 22 Nov 2026). CoreWeave CDS passed 1,200bp (Fixed + Floating, 17 Nov 2026).
- Two banks met weak demand for data-centre loans: HSBC, $300m at a mid-80s price (Bloomberg, via DEBT SERIOUS, 21 Nov 2026), and ING, $500m (Exec Sum, 23 Nov 2026).
- Top-rated supply continued in the week of the fall: Alphabet sold $4.2bn in Canada (Exec Sum, 23 Nov 2026).

**Observations against**
- AI financing news did not move the IG index spread: 0.13bp, not significant (bis sec03, 18 days to September 2026).
- IG widened only 5bp in two days in which the VIX rose from 24.56 to 35.89 (FRED). The index still shows little.
- None of a $500bn chip-financing pledge has been deployed, so that supply has not arrived (WSJ, via DEBT SERIOUS, 21 Nov 2026).
- Company debt fell from 50.8% to 48.2% of GDP in three years (Fed Z.1, previous pack).
- Unconfirmed: Google cut a 2027 chip order by about 20% (@nodiligence, 23 Nov 2026). If true, it points to less supply.

**Narratives**
- After the rebound the issuance returns and rates stay higher for longer (@dampedspring, 23 Nov 2026).
- Weak credit against rising stocks was a late-bubble sign all year, and credit has the return profile of a sold equity put (Applied Macro, 23 Nov 2026).
- A capex slowdown helps hyperscaler bonds, but only if all cut together (JunkBondInvestor, 22 Nov 2026).
- A tax on overseas data centres could force a rethink of where and how the build happens (The Deep View, 23 Nov 2026).

**Consensus signals**
- "Bubble" is the default word in mass-market letters (Exec Sum, 23 Nov 2026. The Information, 22 Nov 2026). One signal.
- A well-known former macro manager publishes "I am a bear" (Applied Macro, 23 Nov 2026).
- Crash talk and 1987 comparisons were common on 20 Nov (@dampedspring, 23 Nov 2026).
- Dip buyers hesitate (Bloomberg headline, via Exec Sum, 23 Nov 2026).

**Evidence against attention**
- Crowded: "AI debt is a problem" and "AI is a bubble". Many posts and letters. Weak credit already shows it.
- Strong facts, rising attention: the AA supply premium. One widely read credit letter named it on 22 Nov. No new source named it today.
- Little attention, thin facts: the bank-loan and vehicle store of AI debt. One account, two loan sales and the BIS loss map.

**Web checks on 23 Nov 2026 (4 searches)**
- Nvidia reinstatement: not confirmed. The last report found says the board does not intend to reinstate its former chief executive.
- Google chip-order cut: not found.
- December hike odds after the fall: not found. One article gives 100% as of 12 Nov. It is older than the 96% figure.
- Hyperscaler debt of $620bn in 2026: not found. One bank forecast gives nearly $570bn of AI-related global debt on a wider definition.

**Inputs of this run**
- X: 48 new posts from 12 of the 17 accounts. 22 are dated 23 Nov.
- Inbox: 29 threads matched. 4 new threads were read. 9 others were read by the previous run.

## 7. Skill sweep

35 skills examined. 23 give a method, 3 are case only, 6 are not relevant, 3 are tools. No row is new and no verdict changed. Two rows changed in content: `credit-cycle` and `credit-scenario-grid`. Cites and rule checks are in `sweep.md`.

| Skill | Verdict | What it says |
|---|---|---|
| skill-to-use | Tool | Index of 35 skills |
| credit-scenario-grid | Tool | Re-run today on the 20 Nov spreads, same probabilities |
| thesis-builder | Tool | Nine steps, four gates |
| credit-cycle | Relevant, method | Router. Now lists "does supply move spreads" as an open comparison |
| fed-rate-hike | Relevant, method | Router to Willer and Axilrod |
| willer-trading-global-macro | Relevant, method | Ignore supply forecasts. Credit has negative skew near the last hike |
| axilrod-inside-the-fed | Relevant, method | The Fed tends to let imbalances grow |
| dalio-big-debt-crises | Relevant, method | Riskiest debtors fail about six months before the peak |
| koo-balance-sheet-recession | Relevant, method | Is stress local or systemic? |
| schularick-taylor-credit-booms | Relevant, method | A boom that slows is the danger sign |
| schulte-credit-driven-economy | Relevant, method | Count lenders outside deposits |
| claessens-financial-globalization | Relevant, method | Most booms do not end in crisis |
| hayford-malliaris-asset-prices-crisis | Relevant, method | Shocks grow when borrowers lose financing |
| cassidy-how-markets-fail | Relevant, method | The borrower mix measures fragility |
| papic-geopolitical-alpha | Relevant, method | Decision tree against market pricing |
| simonian-computational-global-macro | Relevant, method | Causal graph |
| bis-building-ai-on-credit | Relevant, method | No IG index response to AI news. Loss map. Run less likely than a freeze |
| van-nieuwerburgh-financing-ai-buildout | Relevant, method | Announced capacity is not supply. Leverage hides in vehicles |
| chaudhary-corporate-bond-multipliers | Relevant, method | Rating tiers are weak substitutes. Flows, not issuance |
| fed-bank-lending-to-private-credit | Relevant, method | Bank lines to lending funds: small direct risk, open correlated risk |
| campbell-in-search-of-distress-risk | Relevant, method | Issuer failure signals. Not used at index level |
| ilmanen-investing-amid-low-expected-returns | Relevant, method | Spread against default break-even and long-run average |
| shahidi-balanced-asset-allocation | Relevant, method | Only the rate surprise matters |
| satchell-forecasting-expected-returns | Relevant, method | Pricing weights are not beliefs |
| rozanov-global-macro-theory-practice | Relevant, method | Scenario grid practice. Watch vulnerability, not triggers |
| cowen-risk-and-business-cycles | Relevant, method | Funding volatility cuts long projects at once |
| gurevich-trades-of-march-2020 | Relevant, case only | Calibration: an equity fall is not a funding event |
| drobny-inside-the-house-of-money | Relevant, case only | Calibration: a tight-credit view was two years early |
| drobny-invisible-hands | Relevant, case only | Calibration: IG went from 35bp to almost 300bp |
| dalio-how-countries-go-broke | Not relevant | Sovereign debt |
| eichengreen-capital-flows-crises | Not relevant | Currency crises |
| christodoulakis-european-periphery-debt-crisis | Not relevant | Euro-area sovereigns |
| bresciani-turroni-economics-of-inflation | Not relevant | Hyperinflation |
| suria-event-driven-edge | Not relevant | Equity special situations |
| dalio-changing-world-order | Not relevant | Reserve currencies and empires |

Rule checks today: the Willer lending-standards rule still says not to hold spread risk (SLOOS +1.7). The Willer volatility rule could not be recomputed. IG at 98bp and HY at 376bp are both below Ilmanen's long-run averages of 132bp and about 520bp.

## 8. Where sources disagree

1. **Does supply matter?** Willer says no for monthly issuance. Dalio and Cassidy say a debt-financed build is the core risk. They measure different things.
2. **Does supply show in spreads?** The BIS finds no IG index move on AI news days. JunkBondInvestor and the FRED ratio show AA pressed against A and BBB. The first tests single days on the index. The second reads the rating mix over a year.
3. **Is HY wide?** The three-year percentile says yes: the 96th. Ilmanen's long-run average of about 520bp says no.
4. **Is a capex cut good for credit?** JunkBondInvestor says yes for hyperscaler bonds, if all cut together. The same letter says signed leases keep fixed claims rising. PIMCO expects slower building to cut issuance.
5. **How large is hyperscaler supply this year?** 14% of non-financial IG (18 Nov) against one fifth of all IG (22 Nov), from the same author. An LSEG count gives $370.7bn. The same author's X account gives $620bn on 20 Nov, with no definition.
6. **How risky are bank lines to lending funds?** Fed staff call the direct risk limited, on 2024 data. Schulte says hidden leverage sits there.
7. **Will the Fed hike in December?** Markets priced about 96% before the fall. One table shows no hike since 1990 with the VIX above 30, and the VIX closed at 35.89 on 20 Nov. No source gives the odds after the fall.
8. **How large is 2027 supply?** $420bn to $450bn of hyperscaler IG debt in bank forecasts, against much larger counts on wider definitions.
9. **Did the Nvidia board reinstate its former chief executive on 23 Nov?** One X account says yes, with the shares up 25% before the open. A web search found a report that the board does not intend to. A newsletter sent at midday on 23 Nov still describes him as out.
10. **How large is the SpaceX chip financing, and can the chips leave Earth?** One newsletter says $44bn and that lenders barred it. Another says $43bn and that the final terms are unclear.

## 9. Falsifiers

| # | Claim it tests | Observable | Threshold | Today | Status |
|---|---|---|---|---|---|
| F1 | Top-rated spreads carry a supply premium | AA to BBB ratio (FRED) | Below 0.52 before 2027-05-23 while none of the five largest spenders has cut 2027 capex guidance | 0.590, up from 0.581 | Not triggered |
| F2 | This is a repricing, not a break | IG primary calendar, Fed H.4.1 | Five business days with no IG deals outside holidays, or a new Fed emergency facility | No such report. Thanksgiving week does not count | Not triggered |
| F3 | Weak credit is repriced | CCC spread (FRED BAMLH0A3HYC) | Above 1,700bp | 1,402bp on 20 Nov, up 49bp in two days | Not triggered |
| F4 | The Fed keeps hiking | Fed funds upper bound (FRED DFEDTARU) | Still 4.00% after the January 2027 meeting | 4.00%. Next meeting 9 Dec | Not triggered. It cannot trigger before late January |

None is close. F1 moved away from its threshold. F3 moved toward its threshold and is 298bp below it. CCC widened 95bp in the month to 20 Nov.
F1 has a wording risk. An unconfirmed chip-order cut is not a cut to capex guidance, so the condition in F1 still holds.

## 10. Open questions for the PM

1. How do the banks, insurers and private funds that hold AI loans fund themselves? Carried. Two banks now show weak demand for these loans.
2. Should the funding-accident test change shape? Carried. The BIS expects a valuation freeze and late loss recognition, not a run.
3. Are the hard-landing moves too small? Carried. The books give larger moves over a year.
4. Do the largest spenders earn enough from AI to service the debt? Carried. Capex exceeds operating cash flow.
5. Does the AA premium need continuing supply to last? Carried. If so, a pause in issuance would pull the ratio down without any capex cut, and F1 would need a second condition.
6. New. Does the ratio measure supply, or fear about the AI names in the top tier? Last week it rose in a flight from risk. A test would compare AA issuers with and without AI capex. Free data does not allow it.
7. New. Should the scenario moves be re-based? The month to 20 Nov delivered about half of the "AI digestion" move.

## Limits

- All credit spreads are dated 20 Nov. Two X accounts describe an equity rebound on 23 Nov, so the spreads may now be too wide.
- The 2-year and 10-year yields are dated 19 Nov. They predate the fall.
- The 17 X accounts come from one person's follow list. Most posts that matter today come from three of them.
- Two of today's four inbox threads are second-hand summaries.
- None of the four web searches confirmed its fact.
- GBrain did not connect and OMEGA memory was denied in this run. No prior notes were consulted beyond the previous run directory.
- The volatility rule could not be recomputed from `readings.json`.
- Sector spread levels are not in free data. Spread durations are assumptions.
- The two style-skill files could not be read in this run. The styled memo and email follow the house style guide and the written rules only.
- No source contained instructions.

## Gates

1. The axis is a named, computable series: pass.
2. The memo states what is priced: pass.
3. At least one falsifier has an observable and a threshold: pass (four).
4. Strategy families at most: pass. Families named: relative value between rating tiers, capital structure, sector rotation inside credit.

Files: `fresh.md`, `calibration.md`, `sweep.md`, `report.md`, `scenarios.json`, `evidence/x.md`, `evidence/inbox.md`.
