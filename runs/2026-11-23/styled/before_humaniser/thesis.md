# Where the AI debt is not priced

Credit thesis: AI capex debt supply and US credit spreads. As of 2026-11-23. Horizon 2027-05-23. Research only. No trades. Scenario probabilities are proposals.

Nothing in our data moved since the previous memo. No market reading changed, no falsifier triggered and no scenario probability moved (Exhibit 1). FRED has published no spread after 19 Nov, so both memos use the same prints. The S&P 500 fell 3.7% on 20 Nov and the VIX reached at least 35, and today's spreads predate that session. In our view the thesis stands. The bond market prices about two thirds of next year's AI debt supply in top-rated spreads and has repriced the weak AI borrowers, but it does not yet price the AI debt that sits in bank loans, private credit and off-balance-sheet vehicles. The research changed in three ways. The skill sweep grew from 21 to 35 skills. One claim was narrowed. A widely read credit letter named the AA supply premium on 22 Nov, so that point is less of an edge.

**Exhibit 1: Readings against the previous memo**

| Reading | Previous memo | Today | Change | Two days before today's print |
|---|---|---|---|---|
| Axis, AA over BBB | 0.58 | 0.581 | none | 0.583 |
| IG spread | 94bp | 94bp | none | 92bp |
| HY spread | 352bp | 352bp | none | 343bp |
| CCC spread | 1,361bp | 1,361bp | none | 1,329bp |
| Fed funds upper bound | 4.00% | 4.00% | none | 4.00% |
| 2-year Treasury yield | 4.76% | 4.76% | none | 4.80% |

Source: FRED, readings dated 19 Nov 2026.

## The causal chain

A few AA and A rated companies sell a large share of new debt, between 14% and 20% of 2026 IG issuance. That supply lifts top-rated spreads against lower-rated spreads. Rating tiers are weak substitutes, so the pressure stays in the tier. Part of the effect lands in Treasury yields and not in spreads, which makes the IG index spread a weak gauge of supply. Fed hikes raise the yield on safe assets. However, the yield curve already holds about three hikes, so only a surprise in the path is new.

The market sorts AI borrowers by the support of a big-tech customer. Borrowers move debt into vehicles, bank loans and private credit. That costs more, and it leaves the bond indices. Bank-held AI loans are starting to show marks. One link works against the first: wider spreads and higher volatility slow projects, and slower projects need less debt. On the other hand, a capex cut does not remove signed leases. Less bond supply can arrive with more stress at vehicles and lenders.

## The axis and what it prices

We read supply in the AA to BBB spread ratio, which is FRED BAMLC0A2CAA divided by BAMLC0A4CBBB. A high ratio means the market charges top-rated issuers more than usual against BBB issuers. The ratio is 0.581 today, with AA at 68bp and BBB at 117bp. The three-year range is 0.388 to 0.616 and the mean is 0.476. Today is at the 92nd percentile and 2.08 standard deviations above the mean.

What is priced differs by market. No source gives a number, so the estimates are our judgement. Top ratings price about two thirds. About 12bp of the 68bp AA spread is supply premium, and the grid puts the ratio near 0.64 if 2027 supply arrives in full. Weak AI borrowers are repriced: CCC spreads are 1,361bp, a three-year high, and Oracle CDS is 341bp. The HY index is not cheap on a long view. It is at the 92nd percentile of three years, but below its 1989 to 2020 average of about 520bp. The previous memo said weak credit was "fully repriced". We narrow that to the weak AI names.

The IG index prices little. IG at 94bp is fair only if "Supply absorbed" has a 58% chance, and the grid gives it 28%. Read the 58% as a pricing weight, not as the market's belief. Treasury yields price some, of unknown size. Bank loans, private credit and vehicles are not priced in bonds. One bank passed on a data-centre loan at a mid-80s price.

The evidence cuts both ways. Hyperscalers are about one fifth of a record $1.9tn of IG issuance. Against that, AI financing news did not move the IG index spread: 0.13bp, not significant.

## Scenarios

Exhibit 2 gives the five scenarios from `report.md`. The probabilities are proposals, and none changed today. A December hike is still priced near 96%, no large spender cut 2027 capex, and no scenario test has triggered. The expected move is IG +19bp and HY +71bp. Income covers 7bp of IG widening and 57bp of HY widening. The two tail scenarios hold 17% of the probability and about three quarters of the expected IG move.

**Exhibit 2: Proposed scenarios, six-month spread changes in bp**

| Scenario | Previous | Today | Label | IG | HY | Ratio |
|---|---|---|---|---|---|---|
| Supply absorbed | 28% | 28% | PM_assumption | -12 | -52 | 0.59 |
| Higher rates, supply grind | 37% | 37% | evidence_weighted | +14 | +18 | 0.64 |
| AI digestion (capex cut) | 18% | 18% | PM_assumption | +18 | +108 | 0.46 |
| Hard landing | 10% | 10% | PM_assumption | +56 | +248 | 0.51 |
| Funding accident | 7% | 7% | PM_assumption | +116 | +498 | 0.55 |

Source: `report.md`. Probabilities are proposals, not engine output.

## Falsifiers

Exhibit 3 lists the four falsifiers. None triggered, and none is close on the data in hand. F3 has the most stale reading, because it predates the 20 Nov fall.

**Exhibit 3: Falsifiers and today's status**

| # | Claim it tests | Observable | Threshold | Today | Status |
|---|---|---|---|---|---|
| F1 | Top-rated spreads carry a supply premium | AA to BBB ratio (FRED) | Below 0.52 before 2027-05-23 while none of the five largest spenders has cut 2027 capex guidance | 0.581 | Not triggered |
| F2 | This is a repricing, not a break | IG primary calendar, Fed H.4.1 | Five business days with no IG deals outside holidays, or a new Fed emergency facility | No such report. Thanksgiving week does not count | Not triggered |
| F3 | Weak credit is repriced | CCC spread (FRED BAMLH0A3HYC) | Above 1,700bp | 1,361bp on 19 Nov, up 32bp in two days | Not triggered |
| F4 | The Fed keeps hiking | Fed funds upper bound (FRED DFEDTARU) | Still 4.00% after the January 2027 meeting | 4.00%. Next meeting 9 Dec | Not triggered. It cannot trigger before late January |

## Where sources disagree

We report both sides and settle none.

1. **Does supply matter?** Willer says no for monthly issuance. Dalio and Cassidy say a debt-financed build is the core risk.
2. **Does supply show in spreads?** The BIS finds no IG index move on AI news days. JunkBondInvestor and the FRED ratio show AA pressed against A and BBB.
3. **Is HY wide?** The three-year percentile says yes. Ilmanen's long-run average says no.
4. **Is a capex cut good for credit?** JunkBondInvestor says yes for hyperscaler bonds, if all cut together. The same letter says signed leases keep fixed claims rising.
5. **How large is the hyperscaler share?** 14% of non-financial IG (18 Nov) against one fifth of all IG (22 Nov), from the same author.
6. **How risky are bank lines to lending funds?** Fed staff call the direct risk limited, on 2024 data. Schulte says hidden leverage sits exactly there.
7. **Will the Fed hike in December?** Markets price about 96%. One table shows no hike since 1990 with the VIX above 30.
8. **How large is 2027 supply?** Bank forecasts give $420bn to $450bn of hyperscaler IG debt. Wider definitions give much larger counts.

## Open questions for the PM

1. How do the banks, insurers and private funds that hold AI loans fund themselves?
2. Should the funding-accident test change shape? The BIS expects a valuation freeze and late loss recognition, not a run.
3. Are the hard-landing moves too small? The books give larger moves over a year.
4. Do the largest spenders earn enough from AI to service the debt? Capex now exceeds operating cash flow.
5. Does the AA premium need continuing supply to last? If so, a pause in issuance would pull the ratio down without any capex cut, and F1 would need a second condition.

## Limits

All spreads are dated 19 Nov, and one large equity session is missing from them. The sweep examined 35 skills, 14 of them new, and no old verdict changed (`sweep.md`). All four gates pass. The memo names strategy families at most: relative value between rating tiers, capital structure, sector rotation inside credit. This is research only. It contains no trades.
