# Fresh causal chain (phase A)

Written 2026-11-23, update run. Frozen before any case chapter or the previous `calibration.md` was opened.
Inputs: `readings.json`, `evidence/x.md`, `evidence/inbox.md`, the previous evidence packs, and method chapters only.
Items in the packs that cite past episodes were set aside for `calibration.md`.
Item codes: O and N are in `evidence/x.md`. J is in `evidence/inbox.md`. I is in the previous inbox pack.

## Data note

The credit spreads in `readings.json` are now dated 20 Nov 2026. The previous run had 19 Nov prints.
So the spreads now include the equity fall of 20 Nov. The VIX closed at 35.89 that day (FRED VIXCLS).
The 2-year and 10-year Treasury yields are still dated 19 Nov.
Two X accounts describe a sharp equity rebound on 23 Nov (O3, O4). Today's spreads predate it. Its stated cause is not confirmed.

## Driver

Debt-financed AI capital spending by a few highly rated companies, during a Fed hiking cycle.

## Mechanism

1. **A few top-rated companies issue a large share of new debt.** Hyperscalers are about one fifth of a record $1.9tn of IG issuance this year (JunkBondInvestor, 22 Nov 2026, with an LSEG count found by web search). The same author gave 14% of non-financial IG on 18 Nov. The range is 14% to 20%. Their capex exceeded operating cash flow in the third quarter, $230bn against $199bn (JunkBondInvestor, 22 Nov 2026). Hyperscaler bonds of 10 years or more were about 24% of long corporate issuance in 2026, from about 3% in 2024 (BIS sec03, data to September 2026). Supply continued in the week of the fall: Alphabet sold $4.2bn in Canada (Exec Sum, 23 Nov 2026).

2. **That supply lifts top-rated spreads against lower-rated spreads.** AA spreads are 0.590 of BBB spreads, against a three-year mean of 0.476 (FRED BAMLC0A2CAA, BAMLC0A4CBBB, 20 Nov 2026). AA is at the 100th percentile of its three-year range and AAA at the 99th. BBB is at the 87th and A at the 83rd (`readings.json`). A minus AA is 9bp. In the two days to 20 Nov, AA widened 5bp from 67bp and BBB widened 6bp from 116bp. So AA widened more in proportion, in a risk-off move. Method support: rating groups are weak substitutes, so pressure on one group moves it against the others (Chaudhary sec04: passthrough -0.04 at the coarse rating level). Limit: that paper measures fund flows, not issuance.

3. **Part of the supply effect sits in Treasury yields, not in spreads.** Long AI debt goes to the same buyers as long Treasuries, so supply should show in the term premium (BIS sec03). The 10-year yield is 5.04%, at the 97th percentile (FRED DGS10, 19 Nov 2026). The BIS test found no significant move in the IG index spread on AI news days to September 2026 (BIS sec03, 18 days, an association only). So the IG index spread is a weak gauge of supply. The rating mix is a better one.

4. **Fed hikes raise the yield on safe assets, but the curve already holds them.** The 2-year yield is 4.76% against a 4.00% policy ceiling (FRED DGS2, 19 Nov, and DFEDTARU). A rate path that follows the curve does not move returns. Only the unexpected part does (Shahidi ch03). Markets priced a December hike at about 96% before the fall (previous pack, I22). No source gives the odds after it. A skipped hike, or a faster path, would be the surprise.

5. **The market sorts AI borrowers by support.** Lenders price data-centre debt from the customer's credit (@nodiligence, 16 Nov 2026). Oracle CDS is 341bp (JunkBondInvestor, 22 Nov 2026). CCC spreads are 1,402bp, a new three-year high (FRED BAMLH0A3HYC, 20 Nov 2026). Shocks amplify when borrowers lose access to financing (Hayford and Malliaris ch02).

6. **Moving debt off the balance sheet costs more, and it moves the debt out of the bond indices.** A vehicle's A-rated notes priced about 80bp wider than its parent's own BBB bonds (JunkBondInvestor, 22 Nov 2026). The structures relocate "ownership and leverage" and leave the risk with the tenant (Van Nieuwerburgh sec03). Count lenders outside deposits or the rise in leverage stays hidden (Schulte ch02).

7. **Bank-held AI loans are starting to show marks.** HSBC sold a $300m piece of a data-centre loan at a mid-80s price (Bloomberg, via DEBT SERIOUS, 21 Nov 2026). New: ING met "muted demand" for a $500m data-centre loan sale (Exec Sum, 23 Nov 2026, second-hand, no price). A fibre company delayed the $1bn public leg of an ABS sale (same source). That is two loan sales at two banks. The loss order runs from the vehicle to a capped guarantee, then to insurers and funds, then to their banks (BIS sec02).

8. **Wider spreads and higher volatility slow projects, and slower projects need less debt.** This is the balancing loop. Supply follows returns (Willer ch11). Higher volatility of funding cuts long-term investment at once (Cowen ch02, ch03). Announced capacity overstates supply (Van Nieuwerburgh sec02). New and unconfirmed: one account reports that Google cut a 2027 chip order by about 20% (O5). A web search did not find it. A data-centre company paused a US share listing (J4). No large spender has cut 2027 capex guidance in any source.

9. **A capex cut does not remove the fixed claims.** About $1.3tn of signed leases have not started (JunkBondInvestor, 22 Nov 2026). Fixed debt service turns a modest shortfall into a large loss for the junior claims (Van Nieuwerburgh sec05). So less bond supply can arrive together with more stress in vehicles and lenders.

A new policy item sits outside the chain for now. The US president said the US will tax US firms that build data centres abroad (J7, 20 Nov). It has no detail. It could move building, or cut it.

## Operational axis

AA to BBB option-adjusted spread ratio: FRED BAMLC0A2CAA divided by BAMLC0A4CBBB. Daily history from November 2023.
Level 0.590 on 20 Nov 2026 (AA 72bp, BBB 122bp). Two days earlier 0.578. A month earlier 0.578.
Three-year range 0.388 to 0.616. Mean 0.476.
The level is 2.25 standard deviations above the mean and at the 94th percentile. The peak was on 2 Sep 2026.

## What is priced, from the axis and the method

- **Top ratings.** Supply premium in AA today: (0.590 - 0.476) x 122bp = about 14bp of the 72bp AA spread. The share of the full-supply case that is priced depends on the grid's ratio for that case. The grid is run after this file. The previous grid gave 0.64, which would put the share near 0.114 / 0.164, about 70%. This is a judgement, not a measurement.
- **Treasury yields.** Some supply is priced there and not in spreads. I cannot size it.
- **Weak credit.** CCC is at its three-year high. HY at 376bp is at the 96th percentile of three years. But HY is below its 1989 to 2020 average of about 520bp (Ilmanen ch04). So weak AI names are repriced. The HY index as a whole is not cheap on a long view.
- **The IG index.** 98bp, at the 87th percentile of three years and below a 132bp long-run average (Ilmanen ch04).
- **Not visible in bond prices.** Debt held as bank loans, private credit and vehicle notes. A second loan sale with weak demand appeared today (link 7).

## Change against the previous fresh chain

- Every credit spread moved wider with the 20 Nov print. IG is 98bp from 94bp. HY is 376bp from 352bp. CCC is 1,402bp from 1,361bp. The axis is 0.590 from 0.581.
- The axis rose in a risk-off move. If the AA premium were only a calm-market supply effect, a flight from risk should have lowered the ratio. It did not. This is one day, so it is weak support.
- Link 7 has a second loan sale. Link 8 has one unconfirmed report of a cut order.
- The driver, the axis and the links are unchanged.

## Open tests the method asks for

- Dalio's test: does the borrowed money earn enough to service the debt? Still unmeasured.
- Cassidy's test: what share of borrowers must roll debt to pay interest? Still unmeasured.

## Strategy families (names only)

Relative value between rating tiers. Capital structure (secured against unsecured). Sector rotation inside credit.
