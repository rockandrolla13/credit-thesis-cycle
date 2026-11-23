# Appendices A to G and I: Identification, Aggregation, Robustness, Logit Link

## Core Idea
These appendices prove the identification claims, derive the aggregation formula, and test the estimates against changes in shock construction, share lags, factor controls, substitute definitions and issuer-level grouping. The bond-level and baseline-portfolio multipliers move little.

## Frameworks Introduced
- **Identification proofs** (Appendix A.2, A.3). The moment condition `E[u_{j,t} ν̃_{j,t} | X] = 0` follows from Assumption 1 by iterated expectations. The fund-level shock ω can be pulled out of the within-fund expectation. "Notice that here we do not assume orthogonal flows." The passthrough needs share exogeneity at the group level, `S_{i,g} ⊥ ν̃_g`.
- **Aggregation derivation** (Appendix B). Order bonds by group so Γ is block-structured. Sum within a group using `w_i = w_{i|g} w_g`. The own response is `q_g = -(γ^o - γ^c - γ^d w_g) p_g`. The cross response is `γ^d w_{g2} p_{g2}`. Result (B.37): `Γ^G_{g1,g2} = γ^d w_{g2} - 1{g1 = g2} x (γ^o - γ^c)`.
- **Passthrough bound** (Appendix D.1). If true passthrough from flows to demand is β in [0,1], the regression estimates `M̂ = Mβ`. Regress realized holding changes on flows to get β̃. Since funds buy less when prices rise, β̃ understates β. So `M ∈ [M̂, M̂/β̃]`.
- **Heterogeneous passthrough** (Appendix D.1). With bond-specific β_j the pooled estimate is a passthrough-weighted average of multipliers. A liquidity pecking order would put more weight on liquid bonds.
- **Nested logit mapping** (Appendix I). In a Koijen-Yogo nested logit with group parameter λ, the estimating equation has the same form as eq. 10. When λ = 1 the system is plain logit and M̃ = 0. "Our estimates of M̃ strongly reject this assumption." The reduced form is more flexible than nested logit because it does not restrict the passthrough coefficients (footnote 43).

## Key Concepts
- **Davis-Haltiwanger change**: `2(Q_t - Q_{t-1})/(Q_t + Q_{t-1})`. Used for holdings and flows in the passthrough regression. Symmetric and free of small-base outliers (footnote 34).
- **Factor-purged shock**: the flow innovation with common factors removed (Appendix D.2, IA.A.2).
- **Issuer-level portfolio**: bonds grouped by gvkey (Appendix F).

## Mental Models
- Passthrough rises with aggregation by construction, because a fund can shift demand among bonds inside the same portfolio (footnote 35).
- Realized-trade passthrough is not demand passthrough. A wide bid-ask bond may show low realized passthrough because its price moves more (footnote 36).

## Anti-patterns
- **Trusting non-parametric factor extraction on an unbalanced panel.** See sec09 (Appendix IA.A.1).

## Reference Tables

**Table D.1. Passthrough from flows to holdings, CUSIP level.**

| | All, no FE | All, time and fund FE | Inflows | Outflows |
|---|---|---|---|---|
| β̃ | 0.846 (0.055) | 0.750 (0.038) | 0.584 (0.061) | 1.127 (0.096) |

The authors conclude that estimated multipliers "are at most 25% lower than the true multipliers" and that the true CUSIP multiplier "could be as high as 0.08".

**Table D.2. Passthrough heterogeneity.** Each one-notch downgrade lowers passthrough by 0.018 (significant). One standard deviation more log amount outstanding raises it by 0.072 (significant). Bid-ask spread: -0.009, not significant.

**Table D.3. Multiplier by bond size.**

| | CUSIP small | CUSIP large | Portfolio small | Portfolio large |
|---|---|---|---|---|
| M | 0.07 (0.04) | -0.00 (0.07) | 0.32** (0.10) | 0.30* (0.15) |

**Table D.4. Shock construction, baseline portfolio.** M ranges from 0.17 to 0.33 across nine variants (AR lags 1 to 3, with and without trend, factor-purged, raw flows, past-return control). The raw-flow variant gives 0.20 (0.21), not significant. The benchmark is 0.27** (0.10).

**Tables D.5 and D.6. Holding shares lagged one year.**

| Level | Homogeneous OLS | FE | 2SLS M | 2SLS M̃ | F |
|---|---|---|---|---|---|
| CUSIP | 0.38*** (0.08) | -0.04 (0.06), 0.00 (0.05) | 0.00 (0.06) | 1.10*** (0.06) | 83.63 |
| Baseline portfolio | 1.03*** (0.15) | 0.26*, 0.27*, 0.30** | 0.28* (0.12) | 1.03*** (0.05) | 66.75 |

**Table E.1. CUSIP robustness.** M is 0.01 to 0.08 with financial issuers included. It is 0.14 to 0.16 and significant with financial issuers excluded. The authors explain that most financial bonds are investment grade, "which tend to exhibit smaller price impacts".

**Table E.2. Return factor controls.** Portfolio M: 0.277, 0.286, 0.199 (all significant). CUSIP M: 0.035, 0.083 (significant at 5%), 0.033.

**Table F.1. Issuer level.** FE estimates 0.19** and 0.18**. Size-weighted or IV estimates are -0.01 and -0.12 and not significant. Excluding financials: 0.31***, 0.27***, 0.17, 0.25. Issuer-level M̃ is 1.06 to 1.08.

**Tables G.1 and G.2. Market return included and instrumented.**

| Level | M | Near-substitute M̃ | Market (far substitute) |
|---|---|---|---|
| CUSIP | 0.04 (0.05) | 1.11*** (0.06) | -0.06 (0.09) |
| Baseline portfolio | 0.30** (0.10) | 0.93*** (0.06) | 0.31* (0.12) |

## Worked Example
**Scenario** (Appendix D.1): how wrong can the bond-level multiplier be if funds do not pass flows through one for one?
**Application**: the estimate is M̂ = 0.06. The realized passthrough with fixed effects is β̃ = 0.75. The upper bound is 0.06 / 0.75 = 0.08.
**Outcome**: the true bond-level multiplier lies between 0.06 and 0.08. That is still far below the 0.41 from the homogeneous specification.

## Key Takeaways
1. Share exogeneity alone identifies M. Flows may be endogenous.
2. The one-to-one passthrough assumption costs at most about 25% of the multiplier.
3. Outflows pass through more than inflows (1.13 against 0.58).
4. Excluding financial issuers raises the bond-level multiplier to about 0.15.
5. Far-substitute passthrough is about zero for single bonds and about 0.3 for baseline portfolios.

## Connects To
- **sec03** for the assumptions being tested. **sec04** for the baseline tables. **sec09** for the online appendix.
