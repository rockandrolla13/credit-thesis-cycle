# Patterns: Corporate Bond Multipliers (Chaudhary, Fu, Li)

## Name the asset and its substitutes before quoting a multiplier
**When to use**: any time a price-impact number is cited for bonds. (Sections 2.2, 4.2)
**How**: (1) State the unit of the asset: one bond, a rating-and-maturity bucket, or a rating bucket. (2) State the substitute set held fixed. (3) Pick the matching row of Table 5. (4) State the passthrough for that row.
**Trade-offs**: there are only five rows. Anything between them is interpolation the paper does not do.

## Flow-induced demand shock (three steps)
**When to use**: building a bond-level demand shock from mutual fund data. (Section 3.2)
**How**: (1) Compute fund flow over lagged AUM. (2) Regress each fund's flow on three own lags and a fund trend. Scale the residual by `1/(1 - Σρ)`. (3) Sum across funds, weighting by each fund's lagged share of the bond's amount outstanding.
**Trade-offs**: assumes one-to-one passthrough from flows to demand. Realized passthrough is 0.75 to 0.85, so the multiplier may be understated by up to 25% (Appendix D.1).

## Group-by-time fixed effect regression (FE)
**When to use**: you want M only, with the fewest assumptions. (eq. 11, Section 3.3)
**How**: regress returns on the shock, bond controls, and close-substitute-group x quarter fixed effects. Cluster at group x time.
**Trade-offs**: needs only Assumption 1. Gives no passthrough estimate.

## Instrumented substitute return (IV)
**When to use**: you also want the passthrough M̃. (eq. 10, eq. 16)
**How**: add the value-weighted return of the close-substitute group, excluding the asset itself. Instrument it with the value-weighted shock to the same group. Keep time fixed effects for the market.
**Trade-offs**: needs Assumption 1'. Check the first-stage F. It falls from 102 at the bond level to 21 at the rating level (Table 5).

## Aggregation ladder
**When to use**: testing whether substitution is heterogeneous in a market. (Section 4.2, Table 4)
**How**: re-estimate the IV specification at successively wider asset definitions. At each step widen the substitute set by one level. Plot M and M̃ against the level.
**Trade-offs**: sample size collapses. The paper goes from 284,323 observations to 469.

## Passthrough bound
**When to use**: the shock assumes mechanical trading and you doubt it. (Appendix D.1)
**How**: (1) Regress the Davis-Haltiwanger change in fund holdings on fund flow, weighted by lagged holding value. (2) Call the slope β̃. (3) Report `M ∈ [M̂, M̂/β̃]`.
**Trade-offs**: β̃ is itself biased down, so the upper bound is conservative. Realized trades are not demand.

## Share-exogeneity stress tests
**When to use**: defending a shift-share design on holdings. (Section 3.3, Appendices D.2, D.3, E.2, IA.A)
**How**: (1) Lag the shares by one year. (2) Add return factors with asset-specific loadings. (3) Purge common factors from flows using fund characteristics. (4) Re-run on above-median shocks.
**Trade-offs**: each test addresses one threat. None proves exogeneity.

## Dynamic price-effect regression
**When to use**: asking whether a demand-driven price move lasts. (eq. 18, Table 6)
**How**: regress the cumulative return from t to t+h on the shock at t, with group x time fixed effects, for h = 0 to 3 quarters.
**Trade-offs**: the paper runs it at the baseline portfolio level only. Standard errors widen with h.

## Convergence-trade Sharpe ratio
**When to use**: judging whether a demand-driven price gap is large relative to the risk of trading it. (Section 5, eq. 19, eq. 20)
**How**: expected return is M times the mean absolute shock. Risk is the standard deviation of the residual plus M times the shock. Annualize.
**Trade-offs**: assumes one position at a time, no diversification, no shorting cost (footnote 31, Section 5).

## Arbitrage-risk interaction
**When to use**: testing whether hard-to-hedge assets move more per unit of demand. (eq. 21, Table 8)
**How**: standardize ArbRisk across portfolios. Interact it with the shock in the baseline IV regression. Or sort into quartiles and estimate M by quartile.
**Trade-offs**: the authors call the evidence suggestive. Segmentation and clientele effects are not separated out.

## Index-rebalancing back-of-envelope
**When to use**: converting an index-weight coefficient to a multiplier. (Appendix H.2)
**How**: regress monthly returns on percent weight change with bond and group x month fixed effects. Divide the slope by average passive ownership.
**Trade-offs**: passive ownership is hard to measure. Active benchmarked funds trade too.

## Anti-patterns
- **Time fixed effects only.** Gives 0.41 at the bond level against 0.04 to 0.06 with group controls (Table 1).
- **One multiplier for "corporate bonds".** Table 5 spans 0.04 to 3.94.
- **Carrying a flow-shock estimate to a different shock type.** The total effect depends on how correlated the shock is across similar bonds (Section 2.1, Appendix H.2).
- **Reading the on-impact number as permanent.** Table 6: 0.27 at T, 0.04 at T+1.
- **Applying the estimates to crisis quarters.** They are dropped (footnote 25).
- **Applying the estimates to the whole asset class.** Not identified (footnote 30).
