# Online Appendix IA.A to IA.E

## Core Idea
Five supporting exercises. Flows have a weak factor structure. Large shocks give the same multipliers. Dropping bonds near maturity changes nothing. Rating is the substitute dimension that matters most. Stocks show the same bias in a much weaker form. A two-asset model links the multiplier to unhedgeable risk.

## Frameworks Introduced
- **Parametric flow factor model** (IA.A.2): `f⊥_{i,t} = δ_t + C'_{i,t}(λ η_t) + u_{i,t}`. Loadings are linear in fund characteristics: lagged log AUM, high-yield share, average duration. Estimate with a panel regression with time-varying coefficients. Winsorize innovations at 5% for estimating coefficients only. Recover the shock from the unwinsorized innovation, because "outliers are also valid idiosyncratic shocks to demand".
- **Two-asset CARA model** (IA.E). With risk aversion γ and correlation ρ between assets A and B:
  `p_A = γ σ_A² (1 - ρ²) u_A + (ρ σ_A/σ_B) p_B + constant + error` (IA.E.9).
  So `M = γ σ_A² (1 - ρ²)`. The term `σ_A²(1 - ρ²)` is the variance of A that B cannot hedge.

## Key Concepts
- **Weak flow factor structure**: the first factor explains "around 8%" of flow variation. The panel is missing 49.8% of observations relative to a balanced one. In five-fold cross-validation, more factors make out-of-sample fit worse (IA.A.1).
- **Large-shock subsample**: shocks above the median in absolute size (IA.A.3).
- **Number of detailed rating groups**: 21 (IA.D).

## Mental Models
- Stocks "do not have clear close substitutes", so the homogeneous assumption "is also not far off" there (IA.D).
- Rating is the dominant substitute dimension. The own multiplier "remains quantitatively similar as long as we control for the substitute return based on ratings" (IA.C).

## Anti-patterns
- **Fitting principal components to a half-empty panel.** "There is a risk that the factor model is simply fitting noise" (IA.A.1).

## Reference Tables

**Tables IA.A.1 and IA.A.2. Large shocks only.**

| Level | Homogeneous OLS | FE columns | 2SLS M | 2SLS M̃ |
|---|---|---|---|---|
| CUSIP | 0.38*** (0.05) | 0.06, 0.04, 0.04 | 0.04 (0.04) | 1.21*** (0.06) |
| Baseline portfolio | 0.89*** (0.11) | 0.29**, 0.25**, 0.25** | 0.27** (0.10) | 1.02*** (0.06) |

**Tables IA.B.1 and IA.B.2. Excluding bonds under one year to maturity.** The printed coefficients equal those of Tables 1 and 2.

**Table IA.C.1. Several substitute groups at once.**

| Level | M | Rating substitute | Maturity substitute | Size substitute |
|---|---|---|---|---|
| CUSIP | 0.04 to 0.05, not significant | 0.99*** to 1.11*** | 0.97 to 1.09, not significant | 1.04, not significant |
| Baseline portfolio | 0.29** to 0.34** | 0.95*** to 0.98*** | 1.19*** to 1.26*** | -0.33, not significant |

**Table IA.D.1. Stocks.** CRSP universe, 2003Q1 to 2020Q4.

| | No group control | Fama-French 3-factor groups (27) | GICS industry groups (27) |
|---|---|---|---|
| M | 0.380*** (0.086) | 0.254*** (0.040) | 0.252*** (0.072) |

The stock multiplier falls 34% with the control. The authors set this against "an almost 90% drop" for bonds.

## Worked Example
**Scenario** (IA.E): two risky assets, A and B, and a demand shock to A.
**Application**: the multiplier is `γ σ_A² (1 - ρ²)`. Regress A's price on B's price. The residual variance is `σ_A²(1 - ρ²)`.
**Outcome**: if B hedges A well (ρ near 1), the multiplier is near zero. If B hedges A poorly, the multiplier rises. Higher risk aversion raises it in proportion.

## Key Takeaways
1. Above-median shocks give the same multipliers, so nonlinearity is not visible at this scale.
2. Rating is the substitute dimension that must be controlled. Maturity matters as well at the portfolio level.
3. The substitute correction cuts the stock multiplier by 34% and the bond multiplier by about 90%.
4. In the model, M equals risk aversion times unhedgeable variance.

## Connects To
- **sec05** for the empirical arbitrage-risk tests. **sec07** for the other robustness tables.
