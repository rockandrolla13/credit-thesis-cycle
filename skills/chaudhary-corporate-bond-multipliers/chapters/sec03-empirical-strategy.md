# Section 3: Empirical Strategy (3.1, 3.2, 3.3)

## Core Idea
The demand shock is flow-induced trading by US bond mutual funds. Funds are assumed to invest flows in proportion to their existing holdings. Identification does not need the flows to be exogenous. It needs the funds' lagged holding shares to be unrelated to the bond's unobserved demand shocks. This is a Bartik, or shift-share, design.

## Frameworks Introduced
- **Three-step shock construction** (Section 3.2):
  1. *Flow-induced trading (FIT).* Fund i reinvests dollar flow `F_{i,t}` at lagged weights. The percent trade in each bond equals the fund flow `f_{i,t} ≡ F_{i,t} / AUM_{i,t-1}`. This assumes one-to-one passthrough of flows to demand.
  2. *Remove predictable flow.* Estimate `f_{i,t} = ρ_{i,0} + Σ_{k=1..L} ρ_{i,k} f_{i,t-k} + δ_i t + f⊥_{i,t}` with L = 3 and a fund-specific trend (eq. 14). The fund-level shock is the cumulative trade the innovation predicts: `ω_{i,t} = f⊥_{i,t} / (1 - Σ_k ρ_{i,k})`.
  3. *Aggregate to bonds.* `u_{j,t} = Σ_{i∈MF} S_{i,j,t-1} ω_{i,t}`, where S is the share of bond j held by fund i last quarter (eq. 15).
- **Two estimating equations** (Section 3.3):
  - IV: `Δp_{j,t} = M u_{j,t} + M̃ Δp_{g(j),t} + time FE + β'X_{j,t} + ν̃_{j,t}`
  - FE: `Δp_{j,t} = M u_{j,t} + FE_{g,t} + β'X_{j,t} + ν̃_{j,t}`
  The instrument for the group return is the group shock `u^{sub}_{j,t} ≡ Σ_{k≠j, k∈g(j)} w_{k|g(j),t-1} u_{k,t}` (eq. 16).
- **Assumption 1 (share exogeneity)**: for every fund and period, the fund's lagged holding share in bond j is orthogonal to the bond's unobserved demand shock, given controls. It is sufficient for the FE estimate of M (proof in Appendix A.2).
- **Assumption 1' (group share exogeneity)**: the same condition at the close-substitute group level. It is needed for M̃. Footnote 24 says it can fail when unobserved demand correlates with other bonds' lagged shares in the group.
- **Pooled exposure design**: each fund's flow is one exposure experiment. The method pools many of them (Section 3.3).

## Key Concepts
- **Morningstar sample** (Section 3.1): US open-end mutual funds. USD funds and USD securities. At least $10 million of bonds. Bonds between 50% and 120% of portfolio AUM. 1,071 unique funds, 2002Q1 to 2021Q3, about 4.8 million bond-fund-quarter observations. Quarterly frequency.
- **Return sample** (Section 3.1): WRDS Bond Returns built from TRACE. Quarterly return is the cumulative end-of-month return. Bonds with under one quarter to maturity are dropped. S&P rating of CCC- or better. Convertible, putable and exchangeable bonds are excluded. 367,966 bond-quarter observations. WRDS winsorizes returns at the top and bottom 1% (footnote 17).
- **Shock size**: "a fat-tailed distribution centered around zero, with larger shocks being around 1% of the total outstanding amount". Magnitude is similar over time except 2008 and 2020 (Section 3.2).
- **Flow innovation**: the part of a fund's flow not predicted by its own lags and trend. Forward-looking investors trade ahead of predictable flow, so only the innovation counts (Section 3.2).
- **Correlation of own and group shocks**: 0.38 at the bond level (footnote 26), 0.44 at the baseline portfolio level (footnote 28).

## Mental Models
- "Even if the flows are endogenous" the design can work, because the identifying variation is the cross-section of exposure (Section 1, Section 3.3).
- If passthrough from flows to demand is below one, the shock is overstated and the multiplier is understated (Section 3.2). The bias has the same sign in every specification, so it cannot explain the gap between the homogeneous and heterogeneous estimates.
- Mandates help. The part of lagged holdings fixed by mandate "is naturally orthogonal to demand shocks" (footnote 22).

## Anti-patterns
- **Using raw FIT as the shock.** Flows are predictable from return chasing (Section 3.2). The authors do note that the main results "are also robust to using the raw flows" (footnote 18).
- **Ignoring style funds.** A fund that specializes in a priced factor makes shares correlate with factor-driven returns. Assumption 1 then fails (Section 3.3).

## Reference Tables

Threats to share exogeneity and the authors' responses (Section 3.3).

| Threat | Response | Where |
|---|---|---|
| Managers time bond-specific returns | Rebuild shocks with holding shares lagged one year | Appendix D.3 |
| Shares and returns load on common factors | Control for return factors with bond-specific loadings (eq. 17) | Appendix E.2 |
| Flows load on common factors | Purge factors from flows. First factor explains about 8% of flow variation | Appendix IA.A.1, D.2 |
| Passthrough below one | Bound M using realized-trade passthrough | Appendix D.1 |
| Passthrough differs by liquidity | Split by bond size | Appendix D.1 |

## Worked Example
**Scenario** (Section 3.3): a fund held 10% of bond A and 5% of bond B last quarter. It receives an inflow equal to 10% of its AUM.
**Application**: the fund buys at old weights. Demand for bond A rises by 10% x 10% = 1% of bond A outstanding. Demand for bond B rises by 0.5%.
**Outcome**: if last quarter's shares are orthogonal to the unobserved shocks, the extra demand for A relative to B "will be as good as randomly assigned".

## Key Takeaways
1. The shock is a secondary-market demand shock from mutual fund flows, in percent of amount outstanding, at quarterly frequency.
2. Identification rests on lagged holding shares, not on exogenous flows.
3. The FE estimate of M needs only Assumption 1. The IV estimate of M̃ needs the stronger Assumption 1'.
4. Typical large shocks are about 1% of outstanding. The estimates describe shocks of that scale.
5. Two crisis windows are outliers in shock size and are dropped in most specifications.

## Connects To
- **sec02**: equations 10 and 11 that these regressions estimate.
- **sec07**: Appendix A proofs, Appendix D shock robustness.
- **sec08**: two alternative identifications that do not rely on share exogeneity alone.
