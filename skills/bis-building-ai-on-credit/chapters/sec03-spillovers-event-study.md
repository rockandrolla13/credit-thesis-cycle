# Section 3: Spillovers from AI Borrowing to Broader Bond Markets
Source: BIS Bulletin No 140, pp 4-6 (Graph 3, footnote 7) and the online annex (Tables A1 and A2). Dated 27 October 2026.

## Core Idea
AI debt is long-dated and goes to the same investors that hold long Treasuries and investment-grade bonds. More supply should raise the price of duration risk. An event study on 18 news days in 2026 finds a term premium rise of about 1.5 basis points that reverses within two trading days, and no significant move in investment-grade spreads. The authors warn that sustained issuance could change this.

## Frameworks Introduced

### The duration-supply channel (pp 4-5)
1. Hyperscalers and project vehicles issue long-dated debt.
2. NBFIs buy it. The same NBFIs hold long-dated government and investment-grade corporate bonds.
3. A larger supply of long-dated bonds "tends to raise the compensation these investors require for bearing duration risk" (Greenwood and Vayanos (2014)).
4. Treasury yields are the benchmark for mortgages and corporate bonds, and they influence long-term rates in other economies.
5. So AI borrowing can raise borrowing costs for borrowers "with no direct link to AI".

### Why the term premium is the test variable (p 5)
- The 10-year yield equals expected short-term rates over the decade plus a term premium.
- AI-financing news "should have little direct effect on expected policy rates".
- So a supply effect "should appear mainly in the term premium".
- A higher term premium "tightens financial conditions regardless of the stance of monetary policy".

### The event-study method (p 5, Graph 3 footnotes, annex Table A1)
1. **Pick the event days.** 18 sessions in 2026 when AI-financing-related news reached markets. Four types: hyperscaler results, jumbo bond deals, chip vendor results, chip vendor financing.
2. **Date them.** Releases after the 16:00 ET close go to the next session. Jumbo bond deals are issues of $20 billion or more.
3. **Pick the dependent variable.** The daily change in the Adrian, Crump and Moench (2013) 10-year term premium, in basis points.
4. **Regress** the daily change on an AI news day indicator.
5. **Control** for the daily change in the two-year yield and for FOMC statement days. The six FOMC days are 28 January, 18 March, 29 April, 17 June, 29 July and 16 September.
6. **Standard errors**: Newey-West with four lags (three in the short sample).
7. **Sample**: the annex says 5 January to 18 September 2026. The Graph 3 footnote says 6 January. 179 daily observations.
8. **Path around the event** (Graph 3.A): average cumulative change in the adjusted premium on AI news days relative to other days, from session -1 to +5. The confidence interval uses standard errors of the difference in mean cumulative changes.
9. **Curve test** (Graph 3.B): repeat the regression at each maturity of the zero coupon curve (Gürkaynak, Sack and Wright (2007)), with the same controls.
10. **Credit test** (Table A1, column 5): replace the dependent variable with the daily change in the ICE BofA US corporate investment-grade option-adjusted spread.

## Reference Tables

### Table A1: AI financing news and the 10-year term premium (daily changes, basis points)

| | (1) Baseline | (2) 17 Jun-18 Sep 2026 | (3) Financing news only | (4) Additional controls | (5) Corporate spreads |
|---|---|---|---|---|---|
| Dependent variable | Term premium | Term premium | Term premium | Term premium | IG spread |
| AI news day coefficient | 1.53*** | 2.88*** | 2.15*** | 1.80*** | 0.13 |
| Standard error | (0.46) | (0.64) | (0.43) | (0.54) | (0.24) |
| Change in two-year yield | Yes | Yes | Yes | Yes | Yes |
| FOMC statement day | Yes | Yes | Yes | Yes | Yes |
| Day after FOMC, long Treasury auction, change in VIX | No | No | No | Yes | No |
| AI news days | 18 | 8 | 9 | 18 | 18 |
| Observations | 179 | 65 | 179 | 179 | 179 |
| R-squared | 0.11 | 0.09 | 0.11 | 0.19 | 0.04 |

*** is significance at the 1% level. Column 3 counts only jumbo bond deals and the chip vendor's financing announcements. Column 4 adds the session after an FOMC statement, days with a 10-, 20- or 30-year Treasury auction or reopening, and the daily change in the VIX.

### Table A2: the 18 AI financing news sessions in 2026

| Session | Type | Event |
|---|---|---|
| 29 Jan | Hyperscaler results | Microsoft and Meta, quarter to December 2025 |
| 2 Feb | Jumbo bond deal | Oracle, $25 billion |
| 5 Feb | Hyperscaler results | Alphabet. 2026 capex guidance $175-185 billion |
| 6 Feb | Hyperscaler results | Amazon. 2026 capex guidance about $200 billion |
| 9 Feb | Jumbo bond deal | Alphabet, $20 billion in US dollars |
| 26 Feb | Chip vendor results | NVIDIA, quarter to January 2026 |
| 10 Mar | Jumbo bond deal | Amazon, $37 billion |
| 30 Apr | Hyperscaler results and jumbo bond deal | Alphabet, Amazon, Meta, Microsoft results. Meta, $25 billion |
| 21 May | Chip vendor results | NVIDIA, quarter to April 2026 |
| 15 Jun | Jumbo bond deal | NVIDIA, $25 billion |
| 7 Jul | Jumbo bond deal | Amazon, $25 billion |
| 23 Jul | Hyperscaler results | Alphabet. 2026 capex guidance raised to $195-205 billion |
| 30 Jul | Hyperscaler results | Meta and Microsoft. Meta 2026 capex guidance narrowed to $130-145 billion from $125-145 billion |
| 31 Jul | Hyperscaler results | Amazon, quarter to June 2026 |
| 6 Aug | Jumbo bond deal | Alphabet, $25 billion |
| 10 Aug | Chip vendor financing | NVIDIA platforms with six investment firms, target above $500 billion |
| 17 Aug | Chip vendor financing | NVIDIA guarantees of up to $105 billion for data centre leases of an OpenAI affiliate |
| 27 Aug | Chip vendor results | NVIDIA, quarter to July 2026 |

19 events cover 18 sessions because 30 April holds two. The 10 August news was reported during the session, before the official release after the close.

### Results in the text (pp 5-6)

| Finding | Value | Status |
|---|---|---|
| Term premium on AI news days | Up about 1.5 bp relative to other days | Authors' estimate, Table A1 column 1 |
| Normal daily move in the term premium | About 3.5 bp | Authors' statement |
| Persistence | Reversed "within two trading days" | Authors' estimate, Graph 3.A |
| Investment-grade spreads | "did not change significantly" (0.13 bp, s.e. 0.24) | Authors' estimate, column 5 |
| Yield curve | Yields rose more at longer maturities. The 90% band excludes zero from 8 to 30 years. | Authors' estimate, Graph 3.B |
| Hyperscaler bonds of 10 years or more, share of corporate issuance at those maturities | About 24% in 2026, up from about 3% in 2024 | Authors' calculation, Graph 3.C |
| Same, share of gross Treasury issuance | About 13% in 2026, up from about 1.5% in 2024 | Authors' calculation, Graph 3.C |

Graph 3.C cut-off dates: 2026 runs through August for US government bonds, 22 September for hyperscalers and 21 September for US corporate bonds. Corporate issuance comes from Dealogic.

### Chart readings (approximate, not stated in the text)
- Graph 3.A mean path: about -1 at session -1, about +1.5 at session 0, about +0.5 at +1, about -1 from +2 to +4, about -0.5 at +5. The 90% band is wide and includes zero after session 0.
- Graph 3.B: the effect starts near zero at 2 years, reaches about 1 bp near 10 years and flattens near 1.1 bp from 20 to 30 years.

## Key Concepts
- **Term premium**: compensation for bearing duration risk. Here the Adrian, Crump and Moench (2013) estimate.
- **AI-financing-related news day**: one of the 18 sessions in Table A2.
- **Jumbo bond deal**: an issue of $20 billion or more.
- **Adjusted premium**: the daily change after removing the fitted constant, FOMC statement days and the change in the two-year yield.
- **Duration investors**: the concentrated group of NBFIs that must absorb the long-dated supply.
- **Correlated exposures**: the claims these investors absorb share the same underlying AI risk.

## Mental Models
- Use the term premium, not the yield, when the shock is supply. Policy-rate expectations are controlled out through the two-year yield.
- Think of each news day as a small test of how much more duration the market can take. A reversal in two days says the market absorbed it.
- Read the flow share (24% of long corporate issuance) as the pressure gauge. The event study measures the response so far. The share measures how the load is changing.

## Anti-patterns
- **Reading the estimate as causal**: "The estimates are event-day associations, not causal effects." Some news "may be partly anticipated or coincide with other market-moving developments".
- **Reading the curve pattern as proof**: it "is consistent with higher compensation for duration risk but is not causal evidence".
- **Extrapolating "small so far"**: the authors say sustained issuance at the current pace "could make them larger and more persistent".
- **Ignoring sample size**: 18 event days in under nine months. Column 2 rests on 8 days and column 3 on 9.

## Worked Example: reading Table A1 the way the authors do
1. Baseline: an AI news day adds 1.53 bp to the term premium. A normal day moves it about 3.5 bp. So the day "stands out only modestly".
2. Check the later sample. From 17 June the coefficient is 2.88 bp on 8 news days. The text does not comment on this rise. It is consistent with the warning that pressure is growing, but the source does not draw that link.
3. Check pure financing news. With only jumbo deals and chip vendor financing (9 days) the coefficient is 2.15 bp.
4. Add controls for the post-FOMC session, long Treasury auctions and the VIX. The coefficient is 1.80 bp.
5. Switch to credit. The IG spread moves 0.13 bp with a standard error of 0.24. Not significant.
6. Check persistence in Graph 3.A. The relative rise is gone within two trading days.
7. Conclusion in the text: immediate spillovers "appear limited, but the potential pressure is growing".

## The forward warning (p 6)
If supply expands at the current rate, "a concentrated group of duration investors will need to absorb a larger stock of claims with correlated exposures". This could put greater pressure on long-term yields. Where leverage moves into opaque vehicles, it could add to financial stability risks. Off-balance sheet vehicles "add further long-dated claims" on top of the 24% and 13% shares.

## Key Takeaways
1. So far the measured spillover is about 1.5 bp on the 10-year term premium and it fades in two days.
2. Investment-grade spreads show no significant response on AI news days.
3. The response is larger at long maturities, significant from 8 to 30 years.
4. The share of long corporate issuance taken by five firms rose from about 3% in 2024 to about 24% in 2026.
5. The estimates are associations on 18 days. They are not causal.
6. The source gives no threshold at which the spillover becomes large.

## Extraction Notes
- Graph 3 is an image. Values marked as chart readings are approximate.
- The annex is a separate two-page PDF. Both tables are reproduced in full above.
- The main text says the sample starts on 6 January. The annex says 5 January.

## Connects To
- **Section 2**: the same NBFIs hold the vehicle debt.
- **Section 5 (Quarterly Review box)**: CDS spreads of lower-rated hyperscalers had already risen by March 2026.
- **Greenwood and Vayanos (2014)**: the bond supply and excess return framework that the authors cite.
