# Section 5: Arbitrage Risk (5, 5.1, 5.2)

## Core Idea
The authors ask why the price gaps survive. Trading an asset against its substitute portfolio earns little per unit of risk. Portfolios whose risk cannot be hedged with the substitute have larger multipliers. High-yield and longer-maturity portfolios have both more of this risk and larger multipliers. The authors call the evidence "suggestive".

## Frameworks Introduced
- **Substitute-convergence strategy** (Section 5): sell the more expensive of asset j and its close-substitute portfolio, buy the cheaper, and unwind next quarter. Expected return is `M x Mean(|u_{j,t}|)`.
- **Arbitrage risk** (eq. 19): `ArbRisk_j ≡ std(ν̃_{j,t} + M u_{j,t})`. It includes non-flow shocks and next quarter's unpredictable flow shock.
- **Sharpe ratio** (eq. 20): `SR = M x Mean(|u_{j,t}|) / Mean(ArbRisk_j)`.
- **Interaction test** (eq. 21): `Δp_{j,t} = M_0 u_{j,t} + M_1 u_{j,t} x ArbRisk_j + M̃ Δp^{sub}_{j,t} + ε_{j,t}`. ArbRisk is standardized across portfolios.

## Key Concepts
- **Limit to arbitrage**: arbitrage risk is "the part of the risk that cannot be hedged away by constructing the substitute portfolio" (Section 5.1, citing Wurgler and Zhuravskaya 2002).
- **Segmentation assumption**: the Sharpe ratios assume the arbitrageur trades one bond or portfolio at a time. No diversification across submarkets is counted (footnote 31).
- **Shorting costs**: not included. The Sharpe ratios are before those costs (Section 5).
- **Investor segmentation and clientele effects**: other candidate causes the authors name for rating and maturity differences (Section 5.2).

## Mental Models
- A larger multiplier does not mean a better trade. "While the multipliers are larger for more aggregated portfolios, the arbitrage risks also tend to be larger" (Section 5).
- Large shocks do not help either. "Large shocks are accompanied by large noises as well" (footnote 32).
- Appendix IA.E gives the mechanism in a two-asset CARA model: M rises with risk aversion and with the residual risk the substitute cannot hedge.

## Anti-patterns
- **Reading the price gap as free money.** The authors call it "a near-arbitrage opportunity as the trade contains some risk" (Section 5).
- **Treating arbitrage risk as the proven cause.** The authors say it "may contribute" and "leave the quantification of this channel to future research" (Section 6).

## Reference Tables

**Table 7. Arbitrage risk and Sharpe ratio by aggregation level.** Crisis periods dropped.

| Level | M | Arbitrage risk | Annualized Sharpe ratio |
|---|---|---|---|
| Detailed rating x quarter to maturity | 0.29 | 0.06 | 0.02 |
| Coarse rating x short/medium/long | 1.33 | 0.05 | 0.11 |
| Coarse rating x short/long | 1.71 | 0.07 | 0.11 |
| Coarse rating | 3.94 | 0.34 | 0.04 |

**Table 8. Interaction with arbitrage risk, baseline portfolio.** t statistics in parentheses.

| | (1) | (2) |
|---|---|---|
| Shock | 0.29** (2.75) | 0.18 (1.66) |
| ArbRisk x Shock | | 0.43* (2.13) |
| N | 76,521 | 76,521 |

**Heterogeneity, baseline portfolio (Section 5.2). Values come from the text. Figures 3, 4 and 5 carry the detail and did not survive extraction.**

| Split | Multiplier |
|---|---|
| Pooled investment grade | "close to 0" |
| Pooled high yield | "around 0.6" |
| All portfolios | 0.3 |
| Short maturity (0 to 5 years) | "close to 0" |
| Medium (5 to 10) and long (10+) | "around 0.3-0.5" |

**Chart readings (recovered from PDF pages 51 and 53, paper pages 49 and 51). These are read off the plots by eye and are approximate.**
- Figure 3: multiplier relative to the lowest arbitrage-risk quartile is about 0, 0.4, 0.7 and 1.4 for quartiles 1 to 4. The quartile 4 interval does not overlap zero.
- Figure 4a: each detailed IG rating sits near the pooled IG estimate. Each detailed HY rating sits above it. The pooled HY line is roughly 0.7 above pooled IG.
- Figure 4b: median arbitrage risk is low and similar from AAA to BB. It is higher for B and several times higher for CCC.

The maturity difference "is not statistically significant" (Section 5.2). Across arbitrage-risk quartiles the pattern is "almost monotone", and the authors reject no heterogeneity at the 95% level (Figure 3 note).

## Worked Example
**Scenario**: is the coarse-rating price gap worth trading, by the authors' own measure?
**Application**: use Table 7. The rating-level multiplier is 3.94, the largest. Its arbitrage risk is 0.34, also the largest.
**Outcome**: annualized Sharpe ratio 0.04. The highest Sharpe ratio in the table is 0.11, at the two intermediate levels. The authors conclude that "the risks of engaging in these arbitrages are high relative to the average gain".

## Key Takeaways
1. Annualized Sharpe ratios of the convergence trade run from 0.02 to 0.11 across levels.
2. A one-standard-deviation rise in arbitrage risk raises the baseline portfolio multiplier by 0.43.
3. Pooled IG multiplier is near 0. Pooled HY multiplier is about 0.6. Both are at the baseline portfolio level.
4. Longer maturities show higher point estimates, without statistical significance.
5. The effect is "particularly strong among the high-yield bonds" (Section 5.1).

## Connects To
- **sec04**: the multipliers that enter the Sharpe ratio.
- **sec09**: Appendix IA.E, the two-asset model.
