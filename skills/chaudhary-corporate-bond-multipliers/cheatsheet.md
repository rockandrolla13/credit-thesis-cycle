# Cheatsheet: Corporate Bond Multipliers (Chaudhary, Fu, Li)

**Definition**: the multiplier M is the percent price change from a 1 percent demand shock to an asset, with all other asset prices held fixed. It is about one over the own-price demand elasticity. (footnote 1)

**Unit of the shock**: percent of the asset's amount outstanding, from mutual fund flow innovations, per quarter. Larger shocks are about 1%. (Section 3.2)

**Unit of the response**: percent of price (a return). Not a spread. The paper gives no spread or duration conversion.

## Multiplier by level (Table 5, crisis dropped)
| Asset | M | Passthrough M̃ | Implied elasticity | N |
|---|---|---|---|---|
| Single bond | 0.04 (not significant) | 1.11 | 25 | 284,323 |
| Detailed rating x quarter to maturity | 0.29 | 0.99 | not stated | 72,217 |
| Coarse rating x 3 maturity groups | 1.33 | 0.77 | not stated | 1,407 |
| Coarse rating x 2 maturity groups | 1.71 | 0.56 | not stated | 938 |
| Coarse rating | 3.94 | -0.04 (not significant) | under 0.25 | 469 |

Bond level with the FE specification: 0.06, implied elasticity 16.6 (Table 1 column 4). Upper bound 0.08 (Appendix D.1). Without substitute controls: 0.41 (Table 1 column 1).

## Persistence (Table 6, baseline portfolio only)
| T | T+1 | T+2 | T+3 |
|---|---|---|---|
| 0.27** | 0.04 | -0.01 | -0.16 |

## Heterogeneity (Section 5.2, baseline portfolio)
| Group | M |
|---|---|
| Investment grade, pooled | close to 0 |
| High yield, pooled | around 0.6 |
| Short maturity (0 to 5y) | close to 0 |
| Medium and long (5y+) | around 0.3 to 0.5, difference not significant |
| Per standard deviation of arbitrage risk | +0.43 |

## Decision rules
- When someone quotes a bond multiplier, ask which substitutes were held fixed. (Section 2.2)
- When the shock hits one bond, expect little own effect and near one-for-one co-movement with its rating peers. (Table 1)
- When the shock hits a whole rating bucket, expect a large own effect and little spillover to other buckets. (Table 5)
- When the question is about the whole corporate bond market, this paper has no number. (footnote 30)
- When the question is about a crisis quarter, this paper has no number. (footnote 25)
- When the shock is new issuance, this paper has no estimate. Its shocks are fund flows, PIMCO outflows and index rebalancing. (Section 3, Appendix H)
- When the horizon is beyond one quarter, the baseline-level effect is statistically zero. (Table 6)

## Formulas
- `Δp_j = M u_j + M̃ Δp_sub + ν̃` (eq. 4)
- Bond level: `M = 1/γ^o`, `M̃ = γ^c/γ^o` (eq. 10)
- Group portfolio: `M^G = 1/(γ^o - γ^c)`, `M̃^G = γ^d/(γ^o - γ^c)` (eq. 12)
- Shock: `u_j = Σ_i S_{i,j,t-1} ω_i`, `ω_i = f⊥_i / (1 - Σ_k ρ_{i,k})` (eq. 14, 15)
- Passthrough bound: `M ∈ [M̂, M̂/β̃]`, β̃ = 0.75 to 0.85 (Appendix D.1)
- Sharpe ratio: `M x Mean(|u|) / Mean(ArbRisk)` (eq. 20)
- Two-asset model: `M = γ σ_A² (1 - ρ²)` (Appendix IA.E)

## Sample
1,071 US bond mutual funds. 2002Q1 to 2021Q3. Quarterly. USD corporate bonds rated CCC- or better. 367,966 bond-quarters. (Section 3.1)
