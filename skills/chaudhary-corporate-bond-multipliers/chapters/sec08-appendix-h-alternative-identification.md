# Appendix H: Alternative Identifications (H.1 PIMCO, H.2 Index Rebalancing)

## Core Idea
Two other demand shocks give the same pattern. Controlling for close substitutes cuts the bond-level estimate. The cut is large for the correlated PIMCO outflow shock and smaller for index-weight changes, which are more bond-specific.

## Frameworks Introduced
- **PIMCO event design** (H.1, following Zhu 2021). A difference-in-differences with continuous treatment. The shock is `u^{PIMCO}_{j,t} = Σ_i S_{i,j,t-1} f_{i,t} x 1{i ∈ PIMCO}` (H.44). It uses raw flows because the event was not anticipated (footnote 40). Pre-period 2014Q2. Treated periods 2014Q3 and 2014Q4. CUSIP fixed effects.
- **Index rebalancing design** (H.2, following Dick-Nielsen and Rossi 2019 and Koont et al. 2024). Regress monthly returns on the percent change in the bond's weight in the Bloomberg US Corporate Index. Convert with `M̂ ≈ β / average passive ownership` (H.49).
- **Index demand shock identity**: `u^{weight}_{j,t} = passive ownership_{j,t-1} x Δw_{j,t}/w_{j,t-1}`.

## Key Concepts
- **PIMCO event**: Bill Gross left on 26 September 2014. PIMCO held over $240 billion of corporate bonds in late 2013. More than 25% of its AUM left in the last two quarters of 2014 (H.1).
- **Rebalancing lag**: the index rebalances at month end. The triggering event happens during the month. The delay separates demand from news (H.2).
- **Index sample**: weights from September 2017 to January 2021. The index covers US investment-grade corporate bonds (footnote 42).
- **Passive ownership**: about 5% of the investment-grade corporate market over the sample, from Bretscher et al. (2023) (H.2).

## Mental Models
- The PIMCO check complements the baseline. The baseline relies on exogenous shares. Here "the flows are plausibly exogenous".
- The size of the omitted-variable bias depends on how correlated the shock is across similar bonds. Index weight changes are "often bond-specific with low correlation across bonds", so the bias "is attenuated" (H.2).

## Anti-patterns
- **Treating passive ownership as well measured.** Active funds benchmarked to the index may also trade mechanically, so the authors regress on the weight change directly and convert afterwards (H.2).

## Reference Tables

**Table H.1. PIMCO shock.** Standard errors clustered by bond.

| | (1) | (2) | (3) | (4) |
|---|---|---|---|---|
| PIMCO flows x Post | 0.512** (0.178) | 0.118 (0.161) | 0.480** (0.186) | 0.049 (0.168) |
| Quarter x group FE | No | Yes | No | Yes |
| Controls | No | No | Yes | Yes |
| N | 15,688 | 15,688 | 14,232 | 14,232 |

**Table H.2. Index rebalancing.** Monthly. Return in percent on weight change in percent.

| | (1) | (2) | (3) | (4) |
|---|---|---|---|---|
| ΔWeight | 0.011*** (0.002) | 0.007*** (0.002) | 0.010*** (0.002) | 0.006*** (0.002) |
| Month x group FE | No | Yes | No | Yes |
| Controls | No | No | Yes | Yes |
| N | 187,548 | 187,547 | 176,999 | 176,998 |

## Worked Example
**Scenario** (H.2): turn the index coefficient into a multiplier.
**Application**: column 4 gives 0.006% of price per 1% weight change. Passive ownership is about 5%. So M̂ ≈ 0.006 / 0.05.
**Outcome**: about 0.12, "at a similar scale as the baseline CUSIP-level results in Table 1".

## Key Takeaways
1. PIMCO outflows: 0.51 without group controls, 0.12 and insignificant with them.
2. Index rebalancing: 1.1 basis points per 1% weight change without group controls, 0.7 with them.
3. Implied bond-level multiplier from index rebalancing: about 0.12.
4. Both shocks are secondary-market demand shocks. Neither is issuance.
5. H.1 is the paper's one historical episode. The library should file it as CASE material.

## Connects To
- **sec03** for the baseline shock. **sec04** Table 1 for the comparison.
