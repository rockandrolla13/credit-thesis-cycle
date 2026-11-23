# Section 2: Demand Framework (2.1, 2.2)

## Core Idea
Write each investor's demand as a linear function of all bond prices. Market clearing then splits a bond's return into an own-shock term and a substitute-price term. A fully general system cannot be estimated. A two-layer system (close substitutes, distant substitutes) can, and it explains why portfolio multipliers exceed bond multipliers.

## Frameworks Introduced
- **General demand system** (Section 2.1, eq. 1 to 4). Fund i's log quantity vector: `q_{i,t} = Γ p_t + ω_{i,t} + ε_{i,t}`. Γ is an N x N matrix of elasticities. ω is the observed flow-induced demand. ε is unobserved demand. With constant supply, log-linearized market clearing gives
  `Δp_{j,t} = M u_{j,t} + M̃ Δp^{sub}_{j,t} + ν̃_{j,t}` (eq. 4)
  with `M ≡ -1/Γ_{j,j}`, `M̃ ≡ -Σ_{k≠j} Γ_{j,k} / Γ_{j,j}`, and `u_{j,t} ≡ Σ_i S_{i,j,t-1} ω_{i,j,t}`. S is investor i's lagged market share in bond j. The substitute portfolio weights bond k by its cross-elasticity with bond j.
- **Homogeneous substitution** (eq. 5 to 7). `Γ_{j,k} = -γ^o + γ^d w_k` if j = k, and `γ^d w_k` otherwise. Then `M = 1/γ^o`, `M̃ = γ^d/γ^o`, and the substitute portfolio is the market. Estimation: regress returns on the shock with time fixed effects (eq. 7). Logit is the special case `γ^d = γ^o` (footnote 11).
- **Two-layer heterogeneous substitution** (eq. 8 to 11). Add `γ^c w_{k|g}` for bonds in the same close-substitute group g. Then
  `Δp_{j,t} = M u_{j,t} + M̃ Δp_{g(j),t} + time fixed effects + ν̃_{j,t}` (eq. 10, the IV form)
  `Δp_{j,t} = M u_{j,t} + group-by-time fixed effects + ν̃_{j,t}` (eq. 11, the FE form)
  with `M = 1/γ^o` and `M̃ = γ^c/γ^o`.
- **Aggregation result** (eq. 12, derived in Appendix B). For portfolios made of whole close-substitute groups: `M^G = 1/(γ^o - γ^c)` and `M̃^G = γ^d/(γ^o - γ^c)`. "The difference between the portfolio- and bond-level multipliers is exactly the within-group cross-elasticity γ^c." The system needs `γ^o > γ^c` (footnote 16).
- **Shock propagation** (eq. 13). With `γ^c >> γ^d ≈ 0`, the price impact on bond j of a 1 percent shock to bond k in the same group is
  `(γ^c/γ^o) x 1/(γ^o - γ^c) x w_{k|g}  +  (1/γ^o) x 1{j = k}`.
  The first term is group-level. The second is bond-specific.

## Key Concepts
- **Own multiplier M**: price change from the asset's own demand shock, "holding prices of substitutes fixed" (Section 2.1).
- **Substitute passthrough M̃**: spillover coefficient on the substitute portfolio return. Positive for substitutes, negative for complements (Section 2.1).
- **Close substitute group**: baseline is all other bonds in the same detailed rating category. Results are "quantitatively similar" with coarser (IG/HY) or finer (rating and maturity) definitions (Section 2.2).
- **Omitted variable bias (OVB)**: the upward bias in M from leaving out close-substitute returns (Section 2.2).
- **Constant-supply assumption**: made "to simplify the exposition". With elastic supply "the multiplier will be the inverse of a weighted average of supply and demand elasticities" (footnote 9). The authors add that the literature "typically finds low supply elasticities (Siani, 2022)".
- **Other asset classes**: the authors assume the cross-elasticity between corporate bonds and Treasuries or MBS is small, or similar to that with a far corporate substitute (footnote 15).

## Mental Models
- "The total price impact of demand shocks ultimately depends on the structure of the shocks" (Section 2.1). Ask first whether the shock is idiosyncratic or shared across similar bonds.
- A shock to one bond in a highly substitutable group "acts more like a portfolio-level demand shock". It moves the group, with little extra on the bond itself (Section 2.2).
- Policy reading the authors draw: "which bonds the central bank buys matters less than what kind of bonds it buys" (Section 2.2).

## Anti-patterns
- **Controlling only for the market return.** With heterogeneous cross-elasticities this "only captures the weaker average spillover" and over-attributes the price move to the bond's own shock (Section 2.2).
- **Transferring a reduced-form estimate across shock types.** Estimates from correlated fund-flow shocks "may not be very informative" for index inclusion, which is more idiosyncratic (Section 2.1).
- **Treating bond-level orthogonal shocks as enough.** Even then "the total price impact is a reduced-form estimate that combines both the group-level price effect and bond-specific effect" (Section 2.2).

## Reference Tables

| Object | Homogeneous model | Two-layer model, bond level | Two-layer model, group portfolio level |
|---|---|---|---|
| Own multiplier | 1/γ^o | 1/γ^o | 1/(γ^o - γ^c) |
| Passthrough | γ^d/γ^o on the market | γ^c/γ^o on the close group | γ^d/(γ^o - γ^c) on other portfolios |
| Control needed | time fixed effect | group-by-time fixed effect, or instrumented group return | time fixed effect plus the next-wider substitute |
| Equations | 5 to 7 | 8 to 11 | 12 |

## Worked Example
**Scenario** (Section 2.2): a 1 percent demand shock to an Apple AA+ bond. What happens to a Google AA+ bond?
**Application**: scale the shock by the Apple bond's weight in the AA+ group, `w_{k|g}`. Multiply by the portfolio multiplier `1/(γ^o - γ^c)`. Pass it to the Google bond through `γ^c/γ^o`.
**Outcome**: when `γ^c/γ^o ≈ 1`, the portfolio multiplier `M^G` is "a good approximation of the spillover effect on other bonds". The Apple bond gets only the extra `1/γ^o` on top.

Second example (Section 2.2): a shock to one BB+ bond is dampened because investors switch to other BB+ bonds. A shock to the whole BB+ segment is not, because investors "are more reluctant to substitute to bonds of other rating categories".

## Key Takeaways
1. M is defined with substitute prices held fixed. Any estimate needs a stated substitute set.
2. Failing to control close substitutes biases M upward through general equilibrium and correlated shocks.
3. Aggregating a close-substitute group removes γ^c from the own elasticity. That alone raises the multiplier.
4. The framework holds supply constant. It is a demand-shift framework.
5. The FE form identifies M only. The IV form also gives M̃.

## Connects To
- **sec03**: the instrument for the group return in eq. 10.
- **sec04**: estimates of M and M̃ at five aggregation levels.
- **sec07**: Appendix B derivation and Appendix I nested-logit mapping.
