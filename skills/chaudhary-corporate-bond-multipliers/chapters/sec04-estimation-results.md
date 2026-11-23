# Section 4: Estimation Results (4.1, 4.2, 4.3)

## Core Idea
Three results. First, the bond-level multiplier falls from 0.41 to roughly 0.04 to 0.06 once close substitutes are controlled. Second, the multiplier rises step by step with aggregation, to 3.94 for coarse rating portfolios, while the substitute passthrough falls from about 1 to about 0. Third, at the baseline portfolio level the cumulative price effect is gone by the quarter after the shock.

## Frameworks Introduced
- **Five aggregation levels** (Table 4). Each level has its own substitute portfolio. All bonds are market-value weighted.
- **Micro-to-macro spectrum** (Section 4.2). "Micro multipliers typically refer to the multiplier on an individual security, whereas macro multipliers refer to the multiplier when we treat a whole asset class as one." The estimate "can lie anywhere in between" depending on the portfolio definition.
- **Dynamic regression** (eq. 18): `Δp_{j,t:t+h} = M_h u_{j,t} + FE_{g,t+h} + ε_{j,t+h}`, for h = 0, 1, 2, 3 quarters, at the baseline portfolio level.

## Key Concepts
- **Baseline portfolio**: bonds with the same detailed rating and the same quarter to maturity (Section 4.1).
- **Implied elasticity**: the inverse of the multiplier. 0.41 implies about 2.4. 0.06 implies about 16.6. 0.04 implies 25. 3.94 implies "less than 0.25" (Sections 4.1, 4.2).
- **Controls**: bid-ask spread, log amount outstanding, maturity, age, coupon, detailed rating fixed effects. Bond-level regressions add Fama-French 48 industry fixed effects (Table 1 notes).
- **Crisis periods**: 2008Q3 to 2008Q4 and 2020Q1 to 2020Q2 (Table 7 notes). Dropped in most columns.
- **Units**: "a 1% demand shock leads to 30 bps increase in price" at the baseline portfolio level (Section 4.1). The left-hand variable is a return, not a spread change.

## Mental Models
- "Demand elasticities naturally depend on what we define as an asset" (Section 4.2).
- Inelastic demand at the portfolio level is what makes the bond-level estimate possible. The first stage "relies on portfolio prices responding to demand shocks" (Section 4.2).
- For central bank purchases: at the bond level, the type of bond matters more than the specific bond. At the baseline portfolio level, "the maturity and rating of bonds that the central bank chooses to purchase matter for the distribution of price impact" (Section 4.2). The authors leave the quantitative analysis to future work.

## Anti-patterns
- **Quoting one "corporate bond multiplier".** The pooled 0.3 "masks significant heterogeneity" (Section 5.2), and the level of aggregation changes the number by two orders of magnitude (Table 5).
- **Extrapolating to the asset class.** "Our identification strategy does not allow us to uncover the macro elasticity for the corporate bond market as an asset class" (footnote 30).
- **Extrapolating to crises.** "We cannot rule out the possibility that multipliers differ in crisis periods" (footnote 25).

## Reference Tables

**Table 1. Security (CUSIP) level.** Standard errors in parentheses, clustered at substitute group x time.

| Column | Specification | Shock (M) | Substitute return (M̃) | N |
|---|---|---|---|---|
| 1 | Homogeneous OLS, quarter FE | 0.41*** (0.06) | | 301,775 |
| 2 | Group x quarter FE | 0.01 (0.05) | | 301,775 |
| 3 | Same, crisis dropped | 0.04 (0.04) | | 284,323 |
| 4 | Adds short/long maturity x quarter FE | 0.06 (0.04) | | 284,323 |
| 5 | First stage: group shock 2.89*** (0.28) | | | 284,323 |
| 6 | 2SLS | 0.04 (0.05) | 1.11*** (0.06) | 284,323 |

First-stage F = 102.36. Coefficient on the market return, when included, is -0.06 (0.09) (Table G.1).

**Table 2. Detailed rating x quarter-to-maturity portfolios.**

| Column | Specification | Shock (M) | Substitute return (M̃) | N |
|---|---|---|---|---|
| 1 | Homogeneous OLS | 0.96*** (0.12) | | 76,521 |
| 2 | Group x quarter FE | 0.27** (0.10) | | 76,521 |
| 3 | Same, crisis dropped | 0.28** (0.09) | | 72,217 |
| 4 | Adds short/long x quarter FE | 0.30** (0.09) | | 72,217 |
| 5 | First stage: group shock 3.18*** (0.34) | | | 72,217 |
| 6 | 2SLS | 0.29** (0.10) | 0.99*** (0.05) | 72,217 |

First-stage F = 86.69.

**Table 3. Alternative close-substitute definitions, baseline portfolio.** M is 0.29, 0.29, 0.27 and 0.24 across four definitions. With both a detailed-rating and an IG/HY substitute, the passthroughs are 0.90*** (0.16) and 0.12 (0.19). That column's first-stage F is 3.89.

**Tables 4 and 5. Aggregation.** IV specification (eq. 10), crisis dropped.

| Level | Asset | Substitute portfolio | M | M̃ | N | F |
|---|---|---|---|---|---|---|
| 1 | Single bond | Same detailed rating | 0.04 (0.05) | 1.11*** (0.06) | 284,323 | 102.36 |
| 2 | Detailed rating x quarter to maturity | Same detailed rating | 0.29** (0.10) | 0.99*** (0.05) | 72,217 | 86.69 |
| 3 | Coarse rating x 3 maturity groups [0,4), [4,10), [10,∞) | Same coarse rating | 1.33* (0.63) | 0.77*** (0.13) | 1,407 | 43.21 |
| 4 | Coarse rating x 2 maturity groups [0,10), [10,∞) | Same coarse rating | 1.71* (0.84) | 0.56** (0.17) | 938 | 21.86 |
| 5 | Coarse rating | Same investment-grade category | 3.94*** (0.93) | -0.04 (0.30) | 469 | 21.32 |

**Table 6. Dynamics, baseline portfolio.** Cumulative return on the shock, group x quarter FE.

| Horizon | T | T+1 | T+2 | T+3 |
|---|---|---|---|---|
| M_h | 0.27** (0.10) | 0.04 (0.14) | -0.01 (0.20) | -0.16 (0.19) |
| N | 76,521 | 59,278 | 51,262 | 46,247 |

## Worked Example
**Scenario**: a demand shock equal to 1% of amount outstanding. Compare three targets using Table 5.
**Application**:
1. One bond. Own price effect 0.04%, not distinguishable from zero. Its rating peers move almost one for one with it (M̃ = 1.11).
2. One detailed rating x quarter-to-maturity portfolio. Own price effect 0.29%. Rating peers still pass through at 0.99.
3. One coarse rating bucket, for example all BBB. Own price effect 3.94%. Passthrough from the rest of investment grade is -0.04, not different from zero.
**Outcome**: the on-impact effect differs by a factor of about 100 between cases 1 and 3. Table 6 measures persistence only for case 2: 0.27 on impact, 0.04 one quarter later.

## Key Takeaways
1. Bond level: M about 0.04 to 0.06 and insignificant. M̃ about 1.1.
2. Baseline portfolio: M about 0.3 and significant. M̃ about 1.
3. Coarse rating bucket: M = 3.94. M̃ about 0. This rests on 469 observations and a first-stage F of 21.
4. The homogeneous specification overstates M at both the bond level (0.41) and the baseline portfolio level (0.96).
5. The price effect "almost fully reverts in the following quarter". The paper tests persistence at the baseline portfolio level only.
6. Issuer-level portfolios also show larger multipliers than single bonds (Table F.1).

## Connects To
- **sec02**: eq. 12 predicts the aggregation pattern.
- **sec05**: why multipliers differ across ratings and maturities.
- **sec07**, **sec09**: robustness tables behind these estimates.
