# Chapter 10: The information horizon - optimal holding period, strategy aggression and model combination in a multi-horizon framework
**Author**: Edward Fishwick | **Book pages**: 215-226 | **Type**: METHOD (a parametric framework with illustrative numbers. The author warns the model values are "typical rather than actual")

## Core Idea
Forecast information loses value over time. Fishwick models that loss as exponential decay of the information coefficient (IC). He then writes annualized after-cost return as a function of holding period and maximizes it. The result: the optimal horizon "is not a matter of choice, but is an intrinsic property of any given model(s) or process" (s. 10.2). Because the optimal horizon moves with aggression and costs, the best weights on sub-models move too. A constant-weight model is "highly unlikely" to be optimal (s. 10.5).

## Frameworks Introduced
- **Period IC versus cumulative IC** (s. 10.1). IC_1 is the cross-sectional IC between forecasts formed at zero and returns from zero to one. IC_t is the IC for returns over period t-1 to t, for information formed at zero. IC_t is "not the same as" the cumulative IC from zero to t, except at t = 1.
- **Exponential information decay** (eq. 10.2). The functional form is unknown. Fishwick assumes exponential decay for "realism and tractability", following Grinold and Kahn (1999).
- **Half-life of a model** (eq. 10.4). The period over which half of a model's value is used up.
- **Two ways to estimate the decay rate b** (s. 10.4).
  1. From realized ICs: measure non-overlapping ICs at horizons +1 to +18 months, then fit OLS in logs (eq. 10.3). Constrain the fit to pass through IC(1).
  2. From signal correlation: measure the cross-sectional correlation of model forecasts 24 months apart, then apply eq. 10.18. This route needs the assumption that the partial IC is zero.
  - Fishwick then uses a "simple combination (rounded average)" of the two estimates (Table 10.8).
- **The six-input return equation** (eq. 10.16). Expected annualized after-cost return depends on: one-period IC, decay rate b, strategy aggression S, transactions costs C, security volatility, and holding period t.
- **Optimal-horizon rule** (s. 10.2). Fix the first five inputs. Choose t to maximize eq. 10.16. Fishwick solves it numerically with the NAG routine nag_opt_simplex.
- **Multi-horizon model combination** (eqs. 10.8-10.12, 10.17). Combine N models using the inverse forecast-correlation matrix and a diagonal decay matrix E. Maximize eq. 10.17 over t. The maximization also defines the sub-model weights at the optimal horizon.
- **Aggression-horizon-weights chain** (s. 10.3, s. 10.5). Higher aggression shortens the optimal horizon. A shorter horizon raises the weight on fast-decay models. So model weights should change along the efficient frontier.

## Formulas

All recovered from PDF, book pp. 215-222. The extraction lost exponents, Phi, Omega and sigma.

    (10.1)  IC_1 > IC_t   for all t > 1

    (10.2)  IC_t = IC_1 * e^(-b t)

- b: the rate of information decay with respect to time.

    (10.3)  Ln(IC_t) = Ln(IC_1) - b t

- The OLS regression used to estimate b.

    (10.4)  Ln(2) / b = t_half-life

- Found by setting IC_1 / IC_t equal to 0.5, as printed.

    (10.5)  IC_{0→t} = IC_1 * (1/t)^0.5 * (1 - e^(-b t)) / (1 - e^(-b))

- IC_{0→t}: the IC of t-period cumulative log-returns. Fishwick calls it an approximation.
- The division by root t reflects two facts. The standard deviation of cumulative returns grows with root t. Their covariance with S(0) grows with t.

    (10.6)  PIC_{t,s(0)} = [ IC_t - PhiS(0)_t * IC_1 ] * ( 1 - (PhiS(0)_t)^2 )^(-1)

- PIC_{t,s(0)}: the partial IC_t with respect to model information at zero, S(0).
- PhiS(0)_t: the correlation between model information (forecasts or scores) at time zero and at time t.
- Meaning: the forecasting power of old information that is not due to new information being correlated with old.

    (10.7)  PhiS(0)_t = e^(-b t)

- Holds only if PIC_{t,s(0)} is set to zero. Then the decay term is the correlation between scores at zero and at horizon t.

    (10.8)  P = [Omega]^(-1) . B

- P: vector, length N, of partial ICs.
- Omega: the N x N correlation matrix of model forecasts.
- B: vector, length N, of univariate one-step-ahead IC_1 values.

    (10.9)  IC_{1,comp} = (P' . B)^0.5

- The one-step-ahead IC of the composite model.

    (10.10)  MHP = [Omega]^(-1) E . B

- MHP: vector, length N, of multi-horizon partial ICs to horizon t.
- E: the N x N diagonal decay matrix.

    (10.11)  E_mm = (1/t)^0.5 * (1 - e^(-b_m t)) / (1 - e^(-b_m))

- b_m: the information decay beta specific to model m, m = 1, ..., N.

    (10.12)  IC_{t,comp} = ( B' . E . [Omega]^(-1) . E B )^0.5

- The composite IC to any horizon t.

    (10.13)  E[R] = IC_1 * S(0) * sigma

- S(0): the model score, zero mean and unit standard deviation.
- sigma: standard deviation of return. Expected return equals volatility x score x IC.

    (10.14)  E[R_{0→1}]_0 = IC_1 * S(0) * sigma_1M

- The same rule with the time unit fixed at one month.

    (10.15a) E[R_{0→t}]_0 = IC_1 * (1/t)^0.5 * (1 - e^(-b t)) / (1 - e^(-b)) * S(0) * sigma_1M * (t)^0.5

    (10.15b) E[R_{0→t}]_0 = IC_1 * (1 - e^(-b t)) / (1 - e^(-b)) * S(0) * sigma_1M

    (10.16)  E[AR_{0→t}]_0 = IC_1 * [ (1 - e^(-b t)) / (1 - e^(-b)) ] * S(0) * sigma_1M * (T/t) - C * (T/t)

- AR: annualized return.
- C: two-way transactions costs.
- T: number of time increments in one year. T = 12 for months.
- Derivation: multiply eq. 10.15b by T/t, then subtract annualized cost C(T/t). Returns are assumed additive because sigma is measured in logs.

    (10.17)  [R_{0→t}]_0 = S' . [Omega]^(-1) E B . sigma_1M (T/t) - C (T/t)

- S: the score vector, a 1 x N row vector with elements S(0)_m.
- The N-model version of eq. 10.16.

    (10.18)  b = ln( 1 / PhiS(0)_t ) * t^(-1)

- Eq. 10.7 rearranged. It turns a forecast correlation at lag t into a decay rate.

## Key Concepts
- **Information coefficient (IC)**: the cross-sectional correlation between model forecasts and later returns (s. 10.1).
- **Information decay**: the fall of IC_t as the horizon t increases (eq. 10.1).
- **Decay beta (b, b_m)**: the exponential decay rate. A high value means a short half-life.
- **Half-life**: Ln(2)/b. A decay rate of 0.12 gives "a little under 6 months" (s. 10.2).
- **Partial IC**: forecasting power of old information beyond its correlation with new information (eq. 10.6).
- **Strategy aggression**: the model score S. A score of 1.0 "implies an expected return of +1 standard deviation to the investment horizon" (s. 10.2).
- **Optimal horizon / holding period**: the t that maximizes annualized after-cost return. It is "equivalent to" an optimal level of turnover.
- **Decay matrix E**: the diagonal matrix that scales each model's IC to the chosen horizon (eq. 10.11).
- **Deadweight**: mentioned but not defined. Turnover figures are quoted "ignoring deadweight" (s. 10.2, s. 10.5).
- **Constant weight model**: a returns model with fixed weights on its sub-components across the whole efficient frontier (s. 10.5).

## Mental Models
- A model has a natural speed. Trade faster or slower than that and after-cost return falls (s. 10.2).
- Momentum information is worth more in the short term. Value information stays valuable longer. Momentum forecasts "become worthless quite quickly" (s. 10.4).
- If old information forecasts better than its correlation with new information implies, the partial IC is positive. Fishwick finds that for the value models. He finds it negative for MOMENT and COMPOS (s. 10.4).
- Fishwick notes this pattern is "consistent with" markets that overreact to momentum-type information and underreact to value-type information. He does not explore it further (s. 10.4).
- Moving out along the efficient frontier raises tracking error, turnover and the weight on fast information all at once (s. 10.5).
- The same strategy has different risk at different holding periods. Short-period value investing differs from intermediate-period value investing (s. 10.1).

## Anti-patterns
- **Treating the horizon as a free choice.** Fishwick says it is set by the model's decay rate and the strategy parameters (s. 10.2).
- **Using the single-period rule E[R] = IC x score x volatility at every horizon.** In the single-period framework you cannot ask what the optimal horizon is (s. 10.2).
- **Confusing IC_t with the cumulative IC.** They match only at t = 1 (s. 10.1).
- **Fixed model weights across all risk levels.** Above the one point where they are right, they overweight slow-decay information. Below it, they overweight fast-decay information (s. 10.5).
- **Ignoring costs when comparing horizons.** Annualizing returns from different horizons implies different transaction levels (s. 10.2).
- **Trusting one decay estimate.** The two methods give the same ranking but "materially different" half-lives (s. 10.4).
- **Assuming the partial IC is zero without checking.** Eq. 10.7 depends on it, and the data suggest it may fail (s. 10.4).

## Reference Tables

All tables below were recovered from PDF (book pp. 216-225). The extraction dropped their decimal points.

### Table 10.1: decay parameter and half-life
| Time decay parameter b | Approximate half-life (months) |
|---|---|
| 0.04 | 17 |
| 0.08 | 9 |
| 0.12 | 6 |
| 0.16 | 4 |
| 0.35 | 2 |

### Default parameter values (s. 10.2)
| Input | Default | Author's comment |
|---|---|---|
| One-period IC_1 | 0.04 | A monthly IC "within the range of observed ICs in practice" |
| Decay rate b | 0.12 | Half-life a little under 6 months |
| Aggression (score) | 1.0 | Expected return of +1 standard deviation |
| Transactions costs | 0.80 | Two-way. The text later gives the cost range in percent |
| Security volatility | 7.20 | Monthly. Equates to 24.95 annualized, about the median for the Russell 1000 from 89.12 to 97.12 |

### Table 10.2: direction of effects on the optimal horizon
| Parameter raised | Holding period | Return |
|---|---|---|
| Information decay | Negative relationship | Negative relationship |
| Strategy aggression | Negative relationship | Positive relationship |
| Transactions costs | Positive relationship | Negative relationship |

### Tables 10.3, 10.4, 10.5: single-model sensitivity
| Varied input | Value | Optimal holding (months) | Return (p.a.) |
|---|---|---|---|
| Decay b (half-life) | 0.04 (17) | 14.0 | 2.06 |
| | 0.08 (9) | 10.7 | 1.57 |
| | 0.12 (6) | 9.5 | 1.23 |
| | 0.16 (4) | 8.8 | 0.96 |
| | 0.20 (3) | 8.4 | 0.75 |
| Score | 0.4 | 24.5 | 0.07 |
| | 0.6 | 14.8 | 0.36 |
| | 1.0 | 9.6 | 1.15 |
| | 1.4 | 7.5 | 2.06 |
| | 1.8 | 6.3 | 3.04 |
| Costs | 0.2 | 3.9 | 2.28 |
| | 0.5 | 6.5 | 1.58 |
| | 0.8 | 9.6 | 1.15 |
| | 1.2 | 13.4 | 0.72 |
| | 1.8 | 21.1 | 0.29 |

### Tables 10.6, 10.7, 10.8: decay estimates for the four models
| Model | IC_1 (10.6) | Decay beta (10.6) | Half-life (10.6) | PhiS(0)_24 (10.7) | Implied decay beta (10.7) | Implied half-life (10.7) | IC (10.8) | Decay beta (10.8) | Half-life (10.8) |
|---|---|---|---|---|---|---|---|---|---|
| VALUE1 (value) | 0.024 | 0.02 | 34.6 | 0.27 | 0.05 | 13.07 | 0.020 | 0.03 | 23.0 |
| VALUE2 (cash flow) | 0.016 | 0.03 | 27.5 | 0.21 | 0.06 | 10.99 | 0.015 | 0.04 | 17.0 |
| MOMENT (momentum) | 0.030 | 0.19 | 3.6 | 0.07 | 0.12 | 5.91 | 0.032 | 0.17 | 4.0 |
| COMPOS (combined) | 0.037 | 0.17 | 4.2 | 0.12 | 0.09 | 7.54 | 0.039 | 0.14 | 5.0 |

Half-lives are in months. Table 10.6 uses realized multi-horizon ICs. Table 10.7 uses 24-month signal correlation. Table 10.8 is the rounded average that Fishwick carries forward.

### Table 10.9: COMPOS optimal horizon in months
| | Costs 0.6 | Costs 0.8 | Costs 1.0 | Costs 1.2 |
|---|---|---|---|---|
| Score = 0.6 | 12 | 15 | 19 | 26 |
| Score = 1.0 | 8 | 10 | 12 | 14 |
| Score = 1.4 | 6 | 7 | 9 | 10 |
| Score = 1.8 | 5 | 6 | 7 | 8 |

### Table 10.10: optimal horizon and implied sub-model weights (costs 1%)
| Score | Optimal horizon (months) | % VALUE1 | % VALUE2 | % MOMENT |
|---|---|---|---|---|
| 0.42 | 24 | 56 | 10 | 34 |
| 0.60 | 16 | 52 | 9 | 39 |
| 1.00 | 10 | 48 | 7 | 45 |
| 1.40 | 8 | 45 | 7 | 48 |
| 1.80 | 7 | 44 | 5 | 51 |
| 2.20 | 6 | 43 | 4 | 53 |

Forecast correlations used to form Omega (rounded): VALUE1/VALUE2 = 0.45, VALUE1/MOMENT = -0.05, VALUE2/MOMENT = 0.15 (s. 10.5).

### Table 10.11: average decile ranking mapped to average score
| Average decile ranking | 0.5 | 1.0 | 1.5 | 2.0 | 2.5 | 3.0 | 3.5 | 4.0 | 4.5 |
|---|---|---|---|---|---|---|---|---|---|
| Average score | 2.11 | 1.78 | 1.41 | 1.16 | 0.97 | 0.80 | 0.65 | 0.50 | 0.35 |

## Worked Example
Fishwick's three-model case (s. 10.4-10.5).
1. **Data.** Quintile spreads of real-time ex ante forecasts from VALUE1, VALUE2, MOMENT and the composite COMPOS. Top 1000 US stocks, 89.12 to 97.12. The spreads are converted to ICs.
2. **Estimate decay, method 1.** Fit eq. 10.3 to ICs at +1 to +18 months. VALUE1 gets b = 0.02 and MOMENT gets b = 0.19 (Table 10.6).
3. **Estimate decay, method 2.** Measure forecast correlation 24 months apart over four non-overlapping periods. Apply eq. 10.18. VALUE1 gets b = 0.05 and MOMENT gets b = 0.12 (Table 10.7).
4. **Combine.** Take the rounded average. VALUE1: IC 0.020, b 0.03. VALUE2: IC 0.015, b 0.04. MOMENT: IC 0.032, b 0.17 (Table 10.8).
5. **Single-model horizon.** For COMPOS (IC 0.039, b 0.14), maximize eq. 10.16. At score 1.0 the horizon runs from 8 months at costs of 0.6 to 14 months at costs of 1.2 (Table 10.9).
6. **N-model horizon and weights.** Form Omega from the three correlations. Set costs at 1%. Maximize eq. 10.17 (Table 10.10).
7. **Low aggression.** An average decile ranking of about 4.3 gives a 24-month horizon. That implies 50% turnover a year. Weights: VALUE1 56%, MOMENT 34%, VALUE2 10%.
8. **Higher aggression.** An average decile ranking of 2.4 gives a 10-month horizon and 120% turnover. Weights: MOMENT 45%, VALUE1 48%, VALUE2 7%.
9. **Reading.** As aggression rises the slow-decay models are "de-weighted in favour of the faster information".

## Key Takeaways
1. Faster information decay gives a shorter optimal holding period and a lower return (Table 10.2).
2. Higher aggression gives a shorter optimal holding period and a higher return. Score 0.4 implies about 2 years and 50% active turnover. Score 1.8 implies about 6 months and 200% turnover (s. 10.2).
3. Higher transactions costs give a longer optimal holding period and a lower return (Table 10.2).
4. Holding period is not proportional to half-life. With a 17-month half-life the optimal hold is shorter than the half-life. With a 3-month half-life it is nearly three times the half-life (s. 10.2).
5. Cost cuts matter most for high-turnover strategies. Cutting costs from 1.8 to 1.2 adds 43 basis points. Cutting from 0.8 to 0.2 adds 113 basis points (Table 10.5).
6. Model weights in a composite must depend on aggression and costs, because both move the horizon (s. 10.3).
7. Rising aggression tilts the optimal mix toward high-decay-beta (short half-life) models. Falling aggression tilts it toward long half-life models (s. 10.3).
8. A constant-weight model is optimal at most at one point on the frontier. For N = 2 such a point must exist. For N > 2 it occurs only by chance (s. 10.5).
9. The wider the range of b_m and IC_1 across models, the larger the gain from optimizing to horizon. Fishwick suggests building models with "a wide array of b_m values" (s. 10.5).
10. The decay estimates are noisy and probably time-varying. Fishwick doubts the Table 10.8 values can be bettered with the data at hand (s. 10.4).

## Source Defects
- **Recovered from PDF.** Eqs. 10.1 to 10.18 and Tables 10.1 to 10.11 (book pp. 215-225). The extraction dropped exponents, Phi, Omega, sigma and most decimal points. For example it gave "140 206" for 14.0 and 2.06.
- **Page offset.** PDF page = book page + 4 in this chapter, not + 12.
- **Source inconsistencies, recorded and not corrected.**
  - Table 10.3 gives 9.5 months and 1.23 at the default b = 0.12. Tables 10.4 and 10.5 give 9.6 months and 1.15 at the same default inputs.
  - Table 10.1 pairs half-life 2 with b = 0.35. Table 10.3 uses b = 0.20 with half-life 3 as its last row.
  - The text calls 89.12 to 97.12 a "7-year period".
  - Notation for the partial IC varies: PIC_{t,s(0)}, PIC_{t,ss(0)}, PIC_{t,S(0)} and, once, "PIC_1". The text also prints "1C1" for IC_1.
  - The text says eq. 10.7 follows from "using equation (10.6) in equation (10.2)".
  - The text describes the partial IC as a coefficient "in a regression of S(0) on returns". Recorded as printed.
  - The half-life text says "setting IC_1/IC_t equal to 0.5".
  - Table 10.6 half-lives do not all equal Ln(2) over the printed, rounded decay beta. The chapter gives no unrounded betas.
  - Section 10.5 calls the VALUE1/MOMENT correlation the "value/growth" correlation, though MOMENT is introduced as momentum.
  - The text prints "below risk = 25" in the extraction. The page reads 2.5.
- **Units.** The chapter does not state units for return, cost and volatility in one place. Costs are later given as 0.2% to 1.8%, and cost-driven return changes are quoted in basis points. Read "Return (p.a.)" as percent on that basis.
- **Illustrative data.** Fishwick calls the funds "apocryphal" and the values "typical rather than actual". Treat Tables 10.6 to 10.10 as illustration, not as measured results.

## Connects To
- **ch11-optimal-forecasting-horizon**: the next chapter also asks which horizon a forecast should target.
- **ch05-choices-in-forecast-construction**: horizon, scoring and combination are forecast-construction choices.
- **ch02-black-litterman-step-by-step** and **ch03-black-litterman-demystified**: alternative ways to turn several views into one set of expected returns.
- **ch09-uk-liquidity-risk**: value-type signals studied there are the slow-decay information here. Transaction costs here link to liquidity there.
- **ch12-investments-as-bets**: aggression and score here relate to bet size there.
