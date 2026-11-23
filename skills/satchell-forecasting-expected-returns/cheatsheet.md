# Cheatsheet: Forecasting Expected Returns in the Financial Markets (Satchell, ed.)

All rules are the chapter authors' own. Notation differs by chapter.

## Decision rules
- When a predictor is persistent and was found by search, suspect spurious regression. The two effects "reinforce each other". (Ch 1)
- When 100 variables are tried, expect 5 "significant" at 5% by chance. With 20 horizons, expect 1. (Ch 1)
- When R-squared is small, do not dismiss it. A 1% change in expected return moved value about 20% in Ferson's example. (Ch 1)
- When you have no view, hold the market portfolio. (Ch 2)
- When a relative view is smaller than the equilibrium-implied difference, expect a tilt toward the "underperformer". (Ch 2)
- When the ex ante information ratio exceeds 2.0, lower the weight on views (Bevan and Winkelmann, cited in Ch 2).
- When assets in a view differ in size, weight P by market capitalization, not equally. (Ch 2)
- When you know only the order of returns, use the centroid with the covariance matrix. Without covariance the centroid adds little. (Ch 4)
- When two sorts conflict, keep both. Average their centroids by probability. (Ch 4)
- When new information depends on what you already used, enter both as a joint distribution. Do not update sequentially. (Ch 5)
- When the forecast is non-normal, do not use mean-variance. It fits "the nearest normal". Use mean-CVaR. (Ch 5)
- When forecasting an option price, let the underlying price be random too. Pool implied and historical volatility. (Ch 7)
- When lambda is hard to set, constrain tracking error instead. You then know feasibility in advance. (Ch 8)
- When alphas have erratic past errors, constrain forecast-error mean and variance. (Ch 8)
- When measuring liquidity, scale by turnover, not dollar volume. Dollar volume imports size. (Ch 9)
- When aggression rises, shorten the horizon and shift weight to fast-decay models. When costs rise, lengthen it. (Ch 10, Ch 11)
- When reading risk-neutral probabilities, do not treat them as the market's beliefs. (Ch 12)
- When beliefs differ across agents, do not infer risk aversion from a representative agent. (Ch 13)

## Thresholds and numbers the authors state
| Item | Value | Source |
|---|---|---|
| Predictive R-squared, monthly to annual | "10-15% or less" | Ch 1, s. 1.4 |
| Predictive R-squared, 4-5 years | "up to 40% or more" | Ch 1, s. 1.4 |
| Momentum: top 20% winners vs losers, 6 months | about 1% per month | Ch 1, s. 1.3 |
| Tau | 0.01-0.05 (Lee), "often 1" (Satchell and Scowcroft), 0.025 in the example | Ch 2, Ch 3 |
| Maximum anticipated information ratio | 2.0 | Ch 2, s. 2.3.5 |
| Centroid test, N = 500, K = 5, lag 0: information ratio | 2.97 linear, 3.22 centroid, 5.82 optimized linear, 6.88 optimized centroid | Ch 4, Table 4.1 |
| Blom alpha fit | A = 0.4424, B = 0.1185, beta = 0.21 | Ch 4, App. B |
| Option trade filter | 2% | Ch 7, eq. 7.23 |
| Bayesian option agents, return per trade before costs | 6.6% and 6.2% (t 2.52, 2.22) | Ch 7, Table 7.3 |
| UK value spread alpha, CAPM then + LIQ | 0.008 (t 2.028) then 0.005 (t 1.503) | Ch 9, Tables 9.6b, 9.7 |
| Half-life from decay b | Ln(2)/b. b = 0.12 gives about 6 months | Ch 10, eq. 10.4 |
| Fishwick defaults | IC 0.04, b 0.12, score 1.0, cost 0.80, monthly vol 7.20 | Ch 10, s. 10.2 |
| Score 0.4 vs 1.8 | 24.5 vs 6.3 months optimal hold | Ch 10, Table 10.4 |
| Kelly example | q 0.9 vs p 0.6 gives wealth 50% above bonds | Ch 12, s. 12.4.1 |
| Position limits, u 10%, d 0%, r_f 5% | "± 2100%" of investible wealth | Ch 13, s. 13.3 |

## Direction of effects on the optimal holding period (Ch 10 Table 10.2, Ch 11)
| Raise this | Holding period | After-cost return |
|---|---|---|
| Information decay b | Shorter (Ch 10). Sign ambiguous under power decay (Ch 11) | Lower |
| Aggression S(0) | Shorter | Higher |
| Transactions costs C | Longer | Lower |
| IC(0) or volatility | Shorter (Ch 11, elasticity -1/(1-alpha)) | n/a |

## Which chapter for which input
| You have | Use | Chapter |
|---|---|---|
| Numeric views with confidence | Black-Litterman, Idzorek calibration | 2, 3 |
| Several scenarios for one view | Scenario-probability update | 3 |
| A ranking only | Centroid portfolio | 4 |
| Forecasts from mixed model types | Mixture of normals, then mean-CVaR | 5 |
| Historical and implied volatility | Bayesian pooled option forecast | 6, 7 |
| Alphas with a track record of errors | Forecast-error constraints | 8 |
| Rival models, no probabilities | Maximin expected utility | 8 |
| A long-short anomaly to explain | Liquidity-augmented alpha test | 9 |
| Models with different decay speeds | Optimal horizon and horizon-dependent weights | 10, 11 |
| Your probability vs the market's | Kelly bet at risk-neutral odds | 12 |
| Dispersed forecasts across investors | Hidden binomial equilibrium | 13 |

## Tells and smells
- A pattern that "retreats into subsets of stocks, subperiods of time". Suspect data mining. (Ch 1)
- An optimizer that puts 1144% in one asset. The inputs are historical means. (Ch 2)
- A backtest with an information ratio near 5 before costs. The authors say such strategies can still lose money. (Ch 4)
- A linear factor model with fixed coefficients. It failed on the late-1990s Internet factor. (Ch 5)
- A composite model with one fixed set of weights at every risk level. It is right at one point at most. (Ch 10)
