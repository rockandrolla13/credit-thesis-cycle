# Thesis: AI capex debt supply and US credit spreads

As of 2026-11-22. Horizon 2027-05-22. Written 2026-11-23. Research only. No trades.
All four gates pass (see the end).

## 1. The thesis in one sentence

The bond market prices about two thirds of next year's AI debt supply in top-rated spreads and has fully repriced weak AI credit, but it does not price the AI debt that sits in bank loans and private credit.

## 2. The causal chain

1. A few AA and A rated companies sell a large share of new debt.
2. That supply lifts top-rated spreads against lower-rated spreads.
3. Fed hikes raise the yield on safe assets, so buyers need less weak credit.
4. The market sorts AI borrowers by support from big tech.
5. Borrowers without support lose the bond market and use bank loans and private credit.
6. Wider spreads slow projects, and slower projects need less debt. This limits step 1.
7. Two delayed risks remain: bank loans must become bonds later, and one large issuer sits one notch above junk.

Sources for each link are in `fresh.md`.

## 3. The operational axis

**AA to BBB spread ratio.** FRED BAMLC0A2CAA divided by BAMLC0A4CBBB. Daily history from November 2023.

- Today: 0.58 (AA 68bp, BBB 117bp, 19 Nov 2026).
- Three-year range: 0.39 to 0.62. Mean 0.48.
- Today is at the 92nd percentile. The peak was on 2 Sep 2026.

A high ratio means the market charges top-rated issuers more than usual against BBB issuers. That is what heavy top-rated supply does.

## 4. What the market already prices

- **Top ratings: about two thirds.** About 12bp of the 68bp AA spread is supply premium. The grid puts the ratio near 0.64 if 2027 supply arrives in full. This is a judgement, not a measurement.
- **Weak AI credit: fully repriced.** CCC spreads are 1,361bp, a three-year high. HY is at the 92nd percentile.
- **The IG index: not much.** IG is 94bp. That level is fair only if "Supply absorbed" has a 58% chance. The grid gives it 28%.
- **Bank loans and private credit: not priced in bonds.** Private AI loans paid 0.1 point more than other private loans (BIS, via Social Capital, 15 Oct 2026).
- No source gives a number for this question. The estimate above is mine.

## 5. Scenarios

From `report.md`. Probabilities are proposals. Moves are six-month spread changes.

| Scenario | Probability | Label | IG | HY | Ratio |
|---|---|---|---|---|---|
| Supply absorbed | 28% | PM_assumption | -12 | -52 | lower |
| Higher rates, supply grind | 37% | evidence_weighted | +14 | +18 | about 0.64 |
| AI digestion (capex cut) | 18% | PM_assumption | +18 | +108 | about 0.46 |
| Hard landing | 10% | PM_assumption | +56 | +248 | n/a |
| Funding accident | 7% | PM_assumption | +116 | +498 | n/a |

Expected move: IG +19bp, HY +71bp. Income covers 7bp of IG widening and 57bp of HY widening.
The two tail scenarios hold 17% of the probability and about three quarters of the expected IG move.
A capex cut helps the debt of the large spenders and hurts those who lent against the build.

## 6. Evidence

**Observations for**
- Hyperscalers are about 14% of non-financial IG issuance, from about 2% (@junkbondinvest, 18 Nov 2026).
- Tech spreads are the widest against other IG debt since 2003 (@lisaabramowicz1, 3 Nov 2026).
- Oracle CDS is 341bp, close to the HY index (@junkbondinvest, 21 Nov 2026).
- CoreWeave CDS passed 1,200bp, from about 450bp in June (Fixed + Floating, 17 Nov 2026).
- Debt with no big-tech contract weakened most (@nodiligence, 21 Nov 2026).
- Order books on AI debt deals fell from 5 times to 2 times (Fintech Blueprint, 30 Oct 2026, preview only).

**Observations against**
- AI data-centre bond spreads narrowed after 9 Nov (WSJ, 19 Nov 2026). The note predates the 20 Nov fall.
- Amazon data-centre bonds trade 146bp over Amazon bonds, from 180bp in September (DEBT SERIOUS, 21 Nov 2026).
- New AI deals still came to market in mid-November (email pack, item 9).
- Company debt fell from 50.8% to 48.2% of GDP in three years (Fed Z.1).
- Monthly AI debt issuance fell from $113bn in June to $23bn in September (FT, via AI Supremacy, 21 Oct 2026).

**Narratives**
- Break camp: El-Erian, Matt King, Felder, Citrini, @biancoresearch.
- Repricing camp: CreditSights, PIMCO, WSJ, @dampedspring.
- "Most of the build is in short bank loans, not bonds" (@nodiligence, 10 Nov 2026, one source).

**Consensus signals**
- Attention is high. About 114 Substack posts in 60 days cover AI capex debt.
- Hedge funds sold tech at the fastest pace in a decade (Not_Mr Risk, 20 Nov 2026).
- 3% of fund managers expect a recession (BofA survey, via WSJ, 20 Nov 2026).

**Evidence against attention**
- Crowded: "AI debt is a problem". Many posts, and weak credit already shows it.
- Little attention, with facts: the AA to BBB ratio. No source mentions it.
- Little attention, thin facts: the bank-loan store of AI debt. One account, plus the ETF holdings and BIS figures.

**Checks made on 23 Nov 2026**
- The SEC accounting inquiry at Nvidia is a Reuters report of 20 Nov. The shares are about 48% below the October record.
- The $680bn figure is a Fed count of all advanced-computing debt to October. It is not the same as hyperscaler debt.

## 7. Skill sweep

21 skills examined. 12 give a method, 1 is case only, 4 are not relevant, 4 are tools or routers. The full table is in `sweep.md`.

The four that matter most:
- **Willer and Saunders** (ch11): supply follows returns, so "we typically ignore supply forecasts". Near the last hike, credit has flat returns and very negative skew.
- **Dalio** (ch02): the riskiest debtors fail about six months before the economy peaks.
- **Cassidy** (ch16): the share of borrowers who must roll debt is the measure of fragility.
- **Schulte** (ch02): count lenders outside banks, or the rise in leverage stays hidden.

## 8. Where sources disagree

1. **Does supply matter?** Willer says no for monthly issuance. Dalio and Cassidy say a debt-financed build is the core risk. They measure different things.
2. **Repricing or break?** See the two camps above. The past cases lean slightly to repricing for now (`calibration.md`).
3. **How large is 2027 supply?** Goldman: $440bn of hyperscaler debt plus $300bn of project debt. BofA: $685bn of all AI credit. Dalio: $1.4 trillion of all net company debt. SemiAnalysis says most debt behind 2026 leases is already raised. PIMCO expects delays to cut issuance.
4. **The Fed.** @biancoresearch says policy is too easy. Morgan Stanley's Tirupattur says hyperscaler spending ignores rates. El-Erian frames December as 25bp against 50bp.

## 9. Falsifiers

| # | Claim it tests | Observable | Threshold |
|---|---|---|---|
| F1 | Top-rated spreads carry a supply premium | AA to BBB ratio (FRED) | Below 0.52 before 2027-05-22 while none of the five largest spenders has cut 2027 capex guidance |
| F2 | This is a repricing, not a break | IG primary calendar, Fed H.4.1 | Five business days with no IG deals outside holidays, or a new Fed emergency facility |
| F3 | Weak credit is fully repriced | CCC spread (FRED BAMLH0A3HYC) | Above 1,700bp |
| F4 | The Fed keeps hiking | Fed funds upper bound (FRED DFEDTARU) | Still 4.00% after the January 2027 meeting |

Status on 2026-11-23: none triggered.

## 10. Open questions for the PM

1. How do the banks, insurers and private funds that hold AI loans fund themselves? The past cases turn on this.
2. How large is the bank-loan store of AI debt, and when must it become bonds?
3. Are the hard-landing moves in the grid too small? The books give larger moves over a year (`calibration.md`).
4. Do the largest spenders earn enough from AI to service the debt? No pack measures it.
5. What would an Oracle downgrade to junk force holders to sell?

## Limits

- 27 of 59 Substack posts were previews. Several email sources were teasers.
- The eight X accounts came from one person's follow list. They are not independent.
- Sector spread levels are not in free data. Spread durations are assumptions.
- Scenario probabilities are proposals. The creditmacro engine has not adopted them.

## Gates

1. Axis is a named, computable series: pass.
2. The memo states what is priced: pass.
3. At least one falsifier with an observable and a threshold: pass (four).
4. Strategy families at most: pass. Families named: relative value between rating tiers, capital structure, sector rotation inside credit.

Files: `fresh.md` (hash in `fresh.sha256`), `calibration.md`, `sweep.md`, `report.md`, `scenarios.json`, `evidence/`.
