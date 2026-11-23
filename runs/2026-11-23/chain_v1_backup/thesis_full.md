# Thesis: AI capex debt supply and US credit spreads

As of 2026-11-23. Horizon 2027-05-23. Research only. No trades.
All four gates pass (see the end). Scenario probabilities are proposals.

**Status of this update: no material change.** No market reading changed, no falsifier triggered, and no scenario probability moved.
X was refreshed: the collection log shows 17 accounts and no failure.

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

Sources for each link are in `fresh.md`. Links 3, 4, 6, 7 and 9 are new today.

## 3. The operational axis

**AA to BBB spread ratio.** FRED BAMLC0A2CAA divided by BAMLC0A4CBBB. Daily history from November 2023.

- Today: 0.581 (AA 68bp, BBB 117bp, reading dated 19 Nov 2026). Two days earlier: 0.583.
- Three-year range: 0.388 to 0.616. Mean 0.476.
- Today is at the 92nd percentile and 2.08 standard deviations above the mean. The peak was on 2 Sep 2026.

A high ratio means the market charges top-rated issuers more than usual against BBB issuers. That is what heavy top-rated supply does.

**Readings against the previous memo**

| Reading | Previous memo | Today | Change | Two days before today's print |
|---|---|---|---|---|
| Axis, AA over BBB | 0.58 | 0.581 | none | 0.583 |
| IG spread | 94bp | 94bp | none | 92bp |
| HY spread | 352bp | 352bp | none | 343bp |
| CCC spread | 1,361bp | 1,361bp | none | 1,329bp |
| Fed funds upper bound | 4.00% | 4.00% | none | 4.00% |
| 2-year Treasury yield | 4.76% | 4.76% | none | 4.80% |

FRED has published no spread after 19 Nov. Both memos use the same prints.
The S&P 500 fell 3.7% on 20 Nov and the VIX reached at least 35 (inbox pack, I19 and I20). Today's spreads predate that session.

## 4. What the market already prices

- **Top ratings: about two thirds.** About 12bp of the 68bp AA spread is supply premium. The grid puts the ratio near 0.64 if 2027 supply arrives in full. AA is at the 99th percentile of its own three-year range. This is a judgement, not a measurement.
- **Treasury yields: some, of unknown size.** The BIS measured about 1.5bp on the 10-year term premium on AI news days, gone in two days (bis sec03, to September 2026). Its authors warn that the effect may grow.
- **Weak AI borrowers: repriced.** CCC spreads are 1,361bp, a three-year high. Oracle CDS is 341bp.
- **The HY index: not cheap on a long view.** HY is at the 92nd percentile of three years. It is below its 1989 to 2020 average of about 520bp (ilmanen ch04). The previous memo said weak credit was "fully repriced". I narrow that to the weak AI names.
- **The IG index: not much.** IG is 94bp. That level is fair only if "Supply absorbed" has a 58% chance. The grid gives it 28%. Read the 58% as a pricing weight, not as the market's belief (satchell ch12).
- **Bank loans, private credit and vehicles: not priced in bonds.** One bank passed on a data-centre loan at a mid-80s price (Bloomberg, via DEBT SERIOUS, 21 Nov 2026). That is a first mark, not a market.
- No source gives a number for this question. The estimates above are mine.

## 5. Scenarios

From `report.md`. The script passed on the first run: 28 rows, 139 scenarios, no warnings.
Probabilities are proposals. Moves are six-month spread changes. No probability changed today.

| Scenario | Previous | Today | Label | IG | HY | Ratio |
|---|---|---|---|---|---|---|
| Supply absorbed | 28% | 28% | PM_assumption | -12 | -52 | 0.59 |
| Higher rates, supply grind | 37% | 37% | evidence_weighted | +14 | +18 | 0.64 |
| AI digestion (capex cut) | 18% | 18% | PM_assumption | +18 | +108 | 0.46 |
| Hard landing | 10% | 10% | PM_assumption | +56 | +248 | 0.51 |
| Funding accident | 7% | 7% | PM_assumption | +116 | +498 | 0.55 |

Expected move: IG +19bp, HY +71bp. Income covers 7bp of IG widening and 57bp of HY widening.
The two tail scenarios hold 17% of the probability and about three quarters of the expected IG move.
A capex cut helps the debt of the large spenders and hurts those who lent against the build.

Why nothing moved: the new evidence fits the existing scenarios. A December hike is still priced near 96%. No large spender cut 2027 capex. No scenario test has triggered.

## 6. Evidence

**Observations for**
- Hyperscalers are about one fifth of a record $1.9tn of IG issuance (JunkBondInvestor, 22 Nov 2026. A web search on 23 Nov found the same LSEG count through a secondary site).
- AA spreads sit nearly on top of single-A spreads (JunkBondInvestor, 22 Nov 2026). FRED shows a 10bp gap on 19 Nov.
- Hyperscaler capex exceeded operating cash flow in the third quarter, $230bn against $199bn (JunkBondInvestor, 22 Nov 2026).
- A vehicle's A-rated notes priced about 80bp wider than its parent's BBB bonds (JunkBondInvestor, 22 Nov 2026).
- Oracle CDS is 341bp (JunkBondInvestor, 22 Nov 2026). CoreWeave CDS passed 1,200bp (Fixed + Floating, 17 Nov 2026).
- A bank passed on a $300m piece of a data-centre loan at a mid-80s price (Bloomberg, via DEBT SERIOUS, 21 Nov 2026).

**Observations against**
- AI financing news did not move the IG index spread: 0.13bp, not significant (bis sec03, 18 days to September 2026).
- In the week to 13 Nov, AI bonds moved with Treasuries, yield for yield (@nodiligence, 17 Nov 2026).
- Amazon data-centre bonds trade 146bp over Amazon bonds, from 180bp in September (Bloomberg, via DEBT SERIOUS, 21 Nov 2026).
- None of a $500bn chip-financing pledge has been deployed, so that supply has not arrived (WSJ, via DEBT SERIOUS, 21 Nov 2026).
- Funding markets show no stress (second-hand digest, 23 Nov 2026).
- Company debt fell from 50.8% to 48.2% of GDP in three years (Fed Z.1, previous pack).

**Narratives**
- A capex slowdown helps hyperscaler bonds, but only if all cut together (JunkBondInvestor, 22 Nov 2026).
- Break camp and repricing camp are unchanged from the previous memo.
- "Most of the build is in short bank loans, not bonds" (@nodiligence, 10 and 11 Nov 2026). Still one source.

**Consensus signals**
- "AI bubble deflating" is now a headline (The Information, 22 Nov 2026).
- Fund managers made the largest cut to tech overweights since 2006 (BofA survey, via @lisaabramowicz1, 17 Nov 2026).
- Weekend letters argue about buying the fall (Not_Mr Risk, 22 Nov 2026).

**Evidence against attention**
- Crowded: "AI debt is a problem". Many posts, and weak credit already shows it.
- Changed today: the AA supply premium. The previous memo found no source that named it. One widely read credit letter now does. The facts are strong and attention is rising from zero.
- Little attention, thin facts: the bank-loan and vehicle store of AI debt. One account, one loan sale and the BIS loss map.

**Web checks on 23 Nov 2026 (4 searches)**
- IG issuance of $1.88tn to 4 Nov and a hyperscaler share near one fifth: found, through a secondary site.
- A report of 70% odds for a December hike: found, but dated about 6 Nov. It is older than the 96% figure.
- A 2027 capex cut by any of the five largest spenders: not found. A bank forecast of 8 Nov kept $1.32tn for the five.
- The VIX level on 20 Nov: not confirmed by search. It rests on two letters.

## 7. Skill sweep

35 skills examined. 23 give a method, 3 are case only, 6 are not relevant, 3 are tools. 14 rows are new. No old verdict changed. Cites and trust notes are in `sweep.md`.

| Skill | Verdict | What it says |
|---|---|---|
| skill-to-use | Tool | Index of 35 skills |
| credit-scenario-grid | Tool | Re-run today, same probabilities |
| thesis-builder | Tool | Nine steps, four gates |
| credit-cycle | Relevant, method | Router to boom and spread chapters |
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
| bis-building-ai-on-credit (new) | Relevant, method | No IG index response to AI news. Loss map. Run less likely than a freeze |
| van-nieuwerburgh-financing-ai-buildout (new) | Relevant, method | Announced capacity is not supply. Leverage hides in vehicles |
| chaudhary-corporate-bond-multipliers (new) | Relevant, method | Rating tiers are weak substitutes. Flows, not issuance |
| fed-bank-lending-to-private-credit (new) | Relevant, method | Bank lines to lending funds: small direct risk, open correlated risk |
| campbell-in-search-of-distress-risk (new) | Relevant, method | Issuer failure signals. Not used at index level |
| ilmanen-investing-amid-low-expected-returns (new) | Relevant, method | Spread against default break-even and long-run average |
| shahidi-balanced-asset-allocation (new) | Relevant, method | Only the rate surprise matters |
| satchell-forecasting-expected-returns (new) | Relevant, method | Pricing weights are not beliefs |
| rozanov-global-macro-theory-practice (new) | Relevant, method | Scenario grid practice. Watch vulnerability, not triggers |
| cowen-risk-and-business-cycles (new) | Relevant, method | Funding volatility cuts long projects at once |
| gurevich-trades-of-march-2020 | Relevant, case only | Calibration |
| drobny-inside-the-house-of-money (new) | Relevant, case only | Calibration: a tight-credit view was two years early |
| drobny-invisible-hands (new) | Relevant, case only | Calibration: IG went from 35bp to almost 300bp |
| dalio-how-countries-go-broke | Not relevant | Sovereign debt |
| eichengreen-capital-flows-crises | Not relevant | Currency crises |
| christodoulakis-european-periphery-debt-crisis | Not relevant | Euro-area sovereigns |
| bresciani-turroni-economics-of-inflation | Not relevant | Hyperinflation |
| suria-event-driven-edge (new) | Not relevant | Equity special situations |
| dalio-changing-world-order (new) | Not relevant | Reserve currencies and empires |

## 8. Where sources disagree

1. **Does supply matter?** Willer says no for monthly issuance. Dalio and Cassidy say a debt-financed build is the core risk. They measure different things.
2. **Does supply show in spreads?** The BIS finds no IG index move on AI news days. JunkBondInvestor and the FRED ratio show AA pressed against A and BBB. The first tests single days on the index. The second reads the rating mix over a year.
3. **Is HY wide?** The three-year percentile says yes. Ilmanen's long-run average says no.
4. **Is a capex cut good for credit?** JunkBondInvestor says yes for hyperscaler bonds, if all cut together. The same letter says signed leases keep fixed claims rising. PIMCO expects slower building to cut issuance.
5. **How large is the hyperscaler share?** 14% of non-financial IG (18 Nov) against one fifth of all IG (22 Nov), from the same author. Vanguard had 11% to July.
6. **How risky are bank lines to lending funds?** Fed staff call the direct risk limited, on 2024 data. Schulte says hidden leverage sits exactly there.
7. **Will the Fed hike in December?** Markets price about 96%. One table shows no hike since 1990 with the VIX above 30.
8. **How large is 2027 supply?** Unchanged from the previous memo: $420bn to $450bn of hyperscaler IG debt in bank forecasts, against much larger counts on wider definitions.

## 9. Falsifiers

| # | Claim it tests | Observable | Threshold | Today | Status |
|---|---|---|---|---|---|
| F1 | Top-rated spreads carry a supply premium | AA to BBB ratio (FRED) | Below 0.52 before 2027-05-23 while none of the five largest spenders has cut 2027 capex guidance | 0.581 | Not triggered |
| F2 | This is a repricing, not a break | IG primary calendar, Fed H.4.1 | Five business days with no IG deals outside holidays, or a new Fed emergency facility | No such report. Thanksgiving week does not count | Not triggered |
| F3 | Weak credit is repriced | CCC spread (FRED BAMLH0A3HYC) | Above 1,700bp | 1,361bp on 19 Nov, up 32bp in two days | Not triggered |
| F4 | The Fed keeps hiking | Fed funds upper bound (FRED DFEDTARU) | Still 4.00% after the January 2027 meeting | 4.00%. Next meeting 9 Dec | Not triggered. It cannot trigger before late January |

None is close on the data in hand. F3 has the most stale reading, because it predates the 20 Nov fall.

## 10. Open questions for the PM

1. How do the banks, insurers and private funds that hold AI loans fund themselves? Carried. The new BIS loss map names them but gives no sizes.
2. Should the funding-accident test change shape? The BIS expects a valuation freeze and late loss recognition, not a run. The current test looks for a bank failure, a Fed facility or a shut primary market.
3. Are the hard-landing moves too small? Carried. The books give larger moves over a year.
4. Do the largest spenders earn enough from AI to service the debt? Carried. Capex now exceeds operating cash flow.
5. Does the AA premium need continuing supply to last? One paper finds flow effects fade within a quarter at a finer level. If so, a pause in issuance would pull the ratio down without any capex cut, and F1 would need a second condition.

## Limits

- All spreads are dated 19 Nov. One large equity session is missing from them.
- The 17 X accounts come from one person's follow list. Most "new" posts are weeks old.
- Only one inbox item added material facts. Three digests are second-hand summaries.
- GBrain and OMEGA memory were not available in this run. No prior notes were consulted beyond the previous run directory.
- The volatility rule could not be recomputed from `readings.json`.
- Sector spread levels are not in free data. Spread durations are assumptions.
- No source contained instructions.

## Gates

1. The axis is a named, computable series: pass.
2. The memo states what is priced: pass.
3. At least one falsifier has an observable and a threshold: pass (four).
4. Strategy families at most: pass. Families named: relative value between rating tiers, capital structure, sector rotation inside credit.

Files: `fresh.md` (hash in `fresh.sha256`), `calibration.md`, `sweep.md`, `report.md`, `scenarios.json`, `evidence/x.md`, `evidence/inbox.md`.
