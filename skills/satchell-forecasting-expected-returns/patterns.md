# Patterns: Forecasting Expected Returns in the Financial Markets (Satchell, ed.)

Each pattern is the chapter authors' method, not this library's advice.

## Predictability audit (Ferson)
**When to use**: before you trust any "variable X predicts returns" claim. (Ch 1)
**How**: (1) Name the information set: past prices or public variables. (2) State the equilibrium model, because the test is a joint hypothesis. (3) Count the searches behind the result. (4) Check predictor persistence for spurious regression and Stambaugh bias. (5) Check overlap and the number of horizons tested. (6) Ask for step-ahead evidence, other countries and other periods. (7) Net out trading costs.
**Trade-offs**: an honest audit rejects most weak-form claims. A real predictor can still fail out of sample.

## Variance decomposition for time-varying expected returns
**When to use**: testing for predictability without choosing a predictor. (Ch 1, s. 1.3)
**How**: estimate each month's conditional variance from high-frequency returns. Average it. Subtract from the unconditional monthly variance. The remainder is the variance of the conditional mean.
**Trade-offs**: indirect. It says predictability exists, not what predicts.

## Reverse optimization to a neutral start
**When to use**: you need expected returns that do not blow up an optimizer. (Ch 2, eq. 2.1)
**How**: lambda = (E(r) - r_f)/sigma^2. Pi = lambda Sigma w_mkt. With no views, hold the market.
**Trade-offs**: needs market weights and a covariance estimate. "CAPM returns" from regression betas give a different vector.

## Black-Litterman blend
**When to use**: combining a manager's views with equilibrium returns. (Ch 2 eq. 2.3, Ch 3 Theorem 1)
**How**: build P (which assets), Q (view returns), Omega (view uncertainty). E[R] = [(tau Sigma)^-1 + P'Omega^-1 P]^-1 [(tau Sigma)^-1 Pi + P'Omega^-1 Q]. Then w = (lambda Sigma)^-1 E[R], or pass E[R] to a constrained optimizer.
**Trade-offs**: tau and Omega are hard to set. An absolute view breaks the sum-to-one of weights. Ch 5 warns that the posterior covariance is not real asset risk.

## Idzorek confidence calibration (seven steps)
**When to use**: the user can state confidence as 0% to 100% but cannot state a variance. (Ch 2, s. 2.4.2)
**How**: for each view alone, compute the 100%-confidence weights, take the departure from market weights, scale by the confidence, and solve for the omega_k whose weights best match that target. Assemble Omega and run the blend.
**Trade-offs**: one numeric search per view. The chapter prints no worked output for it.

## Tilt-direction check
**When to use**: before stating a relative view. (Ch 2, s. 2.3.2)
**How**: compute the return difference that equilibrium already implies. A view below it tilts toward the nominal underperformer. A view above it tilts toward the outperformer.
**Trade-offs**: for multi-asset views, compare against cap-weighted mini-portfolios.

## Scenario-probability update
**When to use**: a manager holds several scenarios for one view and wants a consistency check. (Ch 3, eq. 3.3)
**How**: give each scenario a prior probability. Update with the likelihood of equilibrium returns under each. Raise omega for scenarios the data make unlikely.
**Trade-offs**: in the worked case the posteriors barely move (10.07% to 9.90% from a 10% prior).

## Centroid portfolio from a sort
**When to use**: you know the order of expected returns but not the values. (Ch 4)
**How**: (1) Write beliefs as inequalities, D r >= 0. (2) Compute the centroid c: Blom formula for a complete sort, Monte Carlo sorting otherwise. (3) Maximize w'c under a risk constraint, which is mean-variance with c as the return vector. (4) For two conflicting sorts, average their centroids by probability.
**Trade-offs**: the authors' gain comes only when the covariance matrix is used. Their backtest has no costs and unrealistic lags. A badly wrong order erodes the edge.

## Mixture-of-normals forecast container
**When to use**: merging forecasts from different model types into one distribution. (Ch 5)
**How**: define regimes. Give each a multivariate normal and a probability. Check that inputs are independent, or enter dependent items as a joint distribution. Sample to a Monte Carlo set. Apply payoff functions for non-linear assets.
**Trade-offs**: needs many more scenarios than assets. The chapter has no data test.

## Mean-CVaR by linear programming
**When to use**: optimizing on a non-normal forecast. (Ch 5, s. 5.5)
**How**: on the Monte Carlo set, add two dummy variables per scenario for distance above and below the threshold hyperplane. Minimize the sum of distances below.
**Trade-offs**: the authors reject VaR as the objective. The chapter gives no formulas for the risk measures.

## Pool historical and implied volatility
**When to use**: forecasting an option price one day ahead. (Ch 7)
**How**: implied volatility is the prior, with weight t'. Historical standard deviation is the sample, with weight t - 1. Forecast with the mean of the predictive density, which also treats tomorrow's underlying price as random. Trade only past a 2% filter.
**Trade-offs**: the authors' traders warned that real spreads and illiquidity exceed the cost assumptions.

## Forecast-error constrained optimization
**When to use**: alphas with an uneven track record. (Ch 8, eqs 8.4-8.9)
**How**: maximize active return subject to three quadratic constraints: tracking error, squared mean forecast error, forecast-error variance. Write the last two against initial weights to get "smart turnover" limits. Solve by interior point methods.
**Trade-offs**: a formulation only. The chapter reports no data and no results.

## Maximin across scenarios or experts
**When to use**: you cannot put probabilities on rival models. (Ch 8, s. 8.4)
**How**: compute expected utility under each scenario for each weight. Take the lower envelope. Choose the weight at its maximum.
**Trade-offs**: hard to compute for large portfolios. The maximin portfolio is not the worst-case-scenario portfolio.

## Liquidity-augmented alpha test
**When to use**: asking whether a long-short spread is an anomaly or a liquidity effect. (Ch 9)
**How**: (1) Build a size-free liquidity measure (eq. 9.3). (2) Split at the median each year end to form LIQ. (3) Regress the spread on the market factor. (4) Add LIQ. (5) Check that the LIQ loading is significant and the alpha is not. (6) Add distress, macro, SMB, HML and momentum factors as robustness.
**Trade-offs**: UK stocks, regressions from 1991 to 2004. The liquidity premium there has the opposite sign to the usual one.

## Optimal horizon from IC decay
**When to use**: choosing holding period and turnover for a forecasting model. (Ch 10 eq. 10.16, Ch 11 eq. 11.7)
**How**: estimate IC_1 and decay b two ways (log-OLS on realized ICs, and 24-month signal correlation). Set aggression, cost and volatility. Maximize annualized after-cost return over t. For several models, maximize eq. 10.17 and read the sub-model weights at the optimum.
**Trade-offs**: decay estimates are noisy and the two methods disagree. Ch 11 doubts the multi-model weighting.

## Kelly bet against risk-neutral odds
**When to use**: sizing a binary position when your probability q differs from the market's risk-neutral p. (Ch 12)
**How**: split wealth between Up and Down in proportion to your own probabilities. Wealth becomes W (q/p)(1 + r) for the state that occurs. Replicate with calls: theta_c = (q_u - p_u)/(1 - p_u). Or with puts: theta_p = (p_u - q_u)/p_u.
**Trade-offs**: one-step binomial world. Log utility only. Stating q of 0 or 1 risks ruin.

## Price from heterogeneous forecasts
**When to use**: reasoning about how a shift in forecasts, not in true odds, moves a price. (Ch 13)
**How**: compute each agent's optimism h_i. Power utility demand follows eq. 13.11. Sum wealth-weighted demands to get the price (eq. 13.12).
**Trade-offs**: one period, two states, interest rate taken as given. With a prospect theorist, more optimism need not raise the price.
