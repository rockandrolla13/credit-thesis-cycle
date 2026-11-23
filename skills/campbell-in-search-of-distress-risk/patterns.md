# Patterns: In Search of Distress Risk (Campbell, Hilscher, Szilagyi)

## Define the failure event before modelling
**When to use**: any default or distress study. (Sec 1, Sec 2)
**How**: pick between bankruptcy (Chapter 7 or 11 filing) and failure (bankruptcy, delisting, or a D rating). State the sample span for each.
**Trade-offs**: the wide definition catches out-of-court workouts and performance delistings. It also swells after 1998 (150 failures against 49 bankruptcies in that year).

## Market-valued ratios
**When to use**: building profitability, leverage and liquidity predictors. (Sec 2, Sec 3)
**How**: divide net income, total liabilities and cash by market equity plus book total liabilities. Lag accounting data two months. Winsorise at 5/95.
**Trade-offs**: needs a listed equity price. The authors find these beat book-valued ratios.

## Geometric lag weighting
**When to use**: a single quarter's loss or a single month's return is too noisy. (Sec 3, eq 2 and 3)
**How**: weight the last four quarters of NIMTA and the last 12 months of EXRET with φ = 2^(-1/3), so the weight halves each quarter. Fill missing lags with the cross-sectional mean.
**Trade-offs**: lags of the other variables did not enter significantly, so do not extend this to them on the paper's evidence.

## Horizon-specific logit
**When to use**: you need a 6, 12, 24 or 36 month view, not a one-month view. (Sec 3.1)
**How**: regress failure in month t-1+j on predictors at t-1, conditional on survival to t-2+j. Estimate a separate coefficient set for each j.
**Trade-offs**: the output is a marginal probability for month j. It is not a cumulative probability. Fit falls from a pseudo R2 of 0.312 at lag 0 to 0.044 at 36 months.

## One-standard-deviation impact ranking
**When to use**: comparing predictors with different units. (Sec 3)
**How**: set a firm at sample means. Raise one predictor by one standard deviation. Report the proportional change in failure probability.
**Trade-offs**: depends on the starting point. The paper reports it once, without naming the column.

## Structural benchmark test
**When to use**: checking whether a Merton-type measure adds information. (Sec 3.2)
**How**: run DD alone, the reduced-form model alone, and both together. Compare coefficients and pseudo R2 in sample and out of sample.
**Trade-offs**: DD inside a model that already holds leverage and volatility can take the wrong sign at short horizon.

## Rolling out-of-sample fit
**When to use**: guarding against look-ahead. (Sec 3.2, Sec 4)
**How**: each year from 1981, estimate coefficients on data up to but not including that year. Score that year's observations.
**Trade-offs**: in this paper the out-of-sample and in-sample R2 are close because most failures fall late in the sample.

## Aggregate failure-rate check
**When to use**: testing whether firm variables explain the cycle in defaults. (Sec 3.3)
**How**: average fitted probabilities across firms each year. Compare with the realised failure rate. Then add year dummies and test whether they can be dropped.
**Trade-offs**: here they cannot be dropped. Credit-spread and term-spread interactions with size and leverage shrink them (fn 11, no numbers).

## Failure-probability portfolio sort
**When to use**: asking whether the market paid for failure risk. (Sec 4)
**How**: sort each January on the 12-month Phat. Use tail-heavy percentile buckets. Value-weight. Drop sub-$1 stocks. Hold a year. Use delisting returns. Compute alphas under CAPM, three-factor and four-factor models.
**Trade-offs**: 1981-2003 only. Without a delisting return the result is biased in favour of distressed stocks.

## Announcement-window test for mispricing
**When to use**: testing whether an anomaly is an earnings-expectation error. (Sec 4.1, Table 9)
**How**: measure three-day returns around earnings announcements. Then recompute alphas with those windows replaced by factor portfolios.
**Trade-offs**: a null result does not rule out other kinds of valuation error.

## Predictor-by-predictor return attribution
**When to use**: finding which failure predictors the market misprices. (Sec 4.1, Table 10)
**How**: run Fama-MacBeth cross-sectional regressions of returns on all predictors. Compare each sign with its sign in the failure model. Opposite sign means the variable adds to the anomaly.
**Trade-offs**: results shift with the observation date. Lagged return is significant when observed at the start of the year and not at the start of the month.
