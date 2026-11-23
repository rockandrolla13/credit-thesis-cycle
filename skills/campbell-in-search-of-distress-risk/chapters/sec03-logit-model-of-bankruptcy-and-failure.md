# Section 3: A Logit Model of Bankruptcy and Failure

## Core Idea
A monthly logit on eight variables beats the Shumway five-variable model. The eight are NIMTAAVG, TLMTA, EXRETAVG, SIGMA, RSIZE, CASHMTA, MB and PRICE. As the horizon grows, the persistent market variables (SIGMA, MB, RSIZE) keep or gain weight. Leverage and past returns fade fast. Distance to default adds almost nothing.

## Frameworks Introduced

### The model form (Sec 3, eq 1)
```
P_{t-1}(Y_it = 1) = 1 / (1 + exp(-α - β·x_{i,t-1}))
```
`Y_it` equals one if firm i goes bankrupt or fails in month t. `x_{i,t-1}` is the predictor vector known at the end of the previous month.

### The long-horizon form (Sec 3.1, eq 4)
```
P_{t-1}(Y_{i,t-1+j} = 1 | Y_{i,t-2+j} = 0) = 1 / (1 + exp(-α_j - β_j·x_{i,t-1}))
```
This is the probability of failure **in month j**, conditional on survival for j-1 months. It is not a cumulative probability. The authors state that the cumulative probability does not have a logit form. They do not compute it.

### The two lag-weighted predictors (Sec 3, eq 2 and 3)
```
NIMTAAVG_{t-1,t-12} = (1-φ^3)/(1-φ^12) · (NIMTA_{t-1,t-3} + ... + φ^9·NIMTA_{t-9,t-12})
EXRETAVG_{t-1,t-12} = (1-φ)/(1-φ^12)   · (EXRET_{t-1} + ... + φ^11·EXRET_{t-12})
φ = 2^(-1/3)
```
- The weight halves each quarter.
- The last NIMTA subscript is printed as `t-9,t-12` in this version. The pattern implies the fourth quarter back.
- Missing lags of NIMTA or EXRET are replaced by their cross-sectional means.
- Why: lags of NIMTA and EXRET enter significantly. Lags of the other variables do not.

### The five changes to the Shumway model (Sec 3)
1. Replace NITA and TLTA with NIMTA and TLMTA (market value of assets).
2. Add lagged profitability and excess returns through NIMTAAVG and EXRETAVG.
3. Add CASHMTA. A firm with high cash "has liquid assets available to make interest payments" and may postpone or avoid bankruptcy.
4. Add MB. It may act as "a correction factor" because the other ratios use market value. There may also be "a modest direct effect of overvaluation".
5. Add PRICE. Both NYSE and Nasdaq have a $1 minimum and commonly delist below it. Price matters below $15, so the authors truncate at $15 before taking the log.

## Reference Tables

### Table 3: logit regressions, one month ahead (absolute z statistics in parentheses)
| | (1) Bankr. 63-98 | (2) Failure 63-98 | (3) Failure 63-03 | (4) Bankr. 63-98 | (5) Failure 63-98 | (6) Failure 63-03 |
|---|---|---|---|---|---|---|
| NITA | -14.05 (16.03) | -13.79 (17.06) | -12.782 (21.26) | | | |
| NIMTAAVG | | | | -32.518 (17.65) | -32.457 (19.01) | -29.672 (23.37) |
| TLTA | 5.378 (25.91) | 4.62 (26.28) | 3.744 (32.32) | | | |
| TLMTA | | | | 4.322 (22.82) | 3.865 (23.39) | 3.36 (27.80) |
| EXRET | -3.297 (12.12) | -2.903 (11.81) | -2.319 (13.57) | | | |
| EXRETAVG | | | | -9.51 (12.05) | -8.819 (12.08) | -7.35 (14.03) |
| SIGMA | 2.148 (16.40) | 2.28 (18.34) | 2.763 (26.63) | 0.92 (6.66) | 1.15 (8.79) | 1.482 (13.54) |
| RSIZE | -0.188 (5.56) | -0.253 (7.60) | -0.374 (13.26) | 0.246 (6.18) | 0.169 (4.32) | 0.082 (2.62) |
| CASHMTA | | | | -4.888 (7.96) | -3.218 (6.59) | -2.401 (8.64) |
| MB | | | | 0.099 (6.72) | 0.095 (6.76) | 0.054 (4.87) |
| PRICE | | | | -0.882 (10.39) | -0.807 (10.09) | -0.937 (14.77) |
| Constant | -15.214 (39.45) | -15.41 (40.87) | -16.576 (50.92) | -7.648 (13.66) | -8.45 (15.63) | -9.079 (20.84) |
| Observations | 1,282,853 | 1,302,564 | 1,695,036 | 1,282,853 | 1,302,564 | 1,695,036 |
| Failures | 797 | 911 | 1614 | 797 | 911 | 1614 |
| Pseudo R2 | 0.260 | 0.258 | 0.270 | 0.299 | 0.296 | 0.312 |

All coefficients are significant at 1%. Columns 1-3 are the Shumway model. Columns 4-6 are the authors' "best model".

### Table 4: the best model at each horizon (failure, 1963-2003)
| Lag (months) | 0 | 6 | 12 | 24 | 36 |
|---|---|---|---|---|---|
| NIMTAAVG | -29.672 (23.37) | -23.915 (21.82) | -20.264 (18.09) | -13.232 (10.50) | -14.061 (9.77) |
| TLMTA | 3.36 (27.80) | 2.057 (22.63) | 1.416 (16.23) | 0.917 (9.85) | 0.643 (6.25) |
| EXRETAVG | -7.35 (14.03) | -7.792 (15.97) | -7.129 (14.15) | -5.607 (10.14) | -2.564 (4.14) |
| SIGMA | 1.482 (13.54) | 1.268 (14.57) | 1.411 (16.49) | 1.515 (16.92) | 1.334 (13.54) |
| RSIZE | 0.082 (2.62) | 0.047 (2.02)* | -0.045 (2.09)* | -0.132 (6.19) | -0.18 (8.03) |
| CASHMTA | -2.401 (8.64) | -2.397 (9.77) | -2.132 (8.53) | -1.37 (5.09) | -1.414 (4.61) |
| MB | 0.054 (4.87) | 0.047 (4.22) | 0.075 (6.33) | 0.108 (7.92) | 0.125 (8.17) |
| PRICE | -0.937 (14.77) | -0.468 (10.36) | -0.058 (1.40) n.s. | 0.212 (4.96) | 0.279 (6.00) |
| Constant | -9.079 (20.84) | -8.069 (25.00) | -9.164 (30.89) | -10.233 (34.48) | -10.534 (33.53) |
| Observations | 1,695,036 | 1,642,006 | 1,565,634 | 1,384,951 | 1,208,610 |
| Failures | 1614 | 2008 | 1968 | 1730 | 1467 |
| Pseudo R2 | 0.312 | 0.188 | 0.114 | 0.061 | 0.044 |

`*` = significant at 5% only. `n.s.` = not significant. All others are significant at 1%. The 12-month column is the model used to sort stocks in Sec 4.

### Table 5: distance to default (DD) against the best model (failure, 1963-2003)
| Lag (months) | 0 | 12 | 36 |
|---|---|---|---|
| DD alone: coefficient | -0.883 (39.73) | -0.345 (33.73) | -0.165 (20.88) |
| DD added to best model: coefficient | 0.048 (2.62) | -0.091 (7.52) | -0.09 (8.09) |
| In-sample R2 (1963-2003): DD only | 0.159 | 0.066 | 0.026 |
| In-sample R2: best model | 0.312 | 0.114 | 0.044 |
| In-sample R2: DD in best model | 0.312 | 0.117 | 0.045 |
| Out-of-sample R2 (1981-2003): DD only | 0.156 | 0.064 | 0.025 |
| Out-of-sample R2: best model | 0.310 | 0.108 | 0.039 |

## The one-standard-deviation impact ranking (Sec 3)
The authors start a firm at sample mean values. They raise one predictor by one standard deviation. They report the proportional change in failure probability.

| Predictor | Change in failure probability |
|---|---|
| Leverage | +156% |
| Volatility | +64% |
| Price per share | -56% |
| Profitability | -44% |
| Past excess return | -28% |
| Cash holdings | -21% |
| Market capitalization | +17% |
| Market-book ratio | +9% |

Their reading: leverage, volatility, price per share and profitability matter more than market capitalization, cash or market-book. The magnitudes "roughly line up with the t statistics" in Table 3. The text does not say which Table 3 column these figures use.

## Key Concepts
- **McFadden's pseudo R2**: `1 - L1/L0`. L1 is the log likelihood of the model. L0 is that of a constant-only model.
- **Improvement over Shumway**: pseudo R2 rises from 0.26 to 0.30 for bankruptcies or failures over 1963-1998, and from 0.27 to 0.31 for failures over 1963-2003.
- **RSIZE sign flip at short horizon**: RSIZE correlates strongly with PRICE. Once PRICE is in, RSIZE takes a weak positive coefficient, "probably as an ad hoc correction".
- **Persistent attributes**: market capitalization, market-book and volatility. They "become increasingly important measures of financial distress at long horizons".
- **Short-term signals**: leverage and past excess returns. Their coefficients "decay particularly rapidly".
- **Intermediate**: profitability and cash holdings.
- **Distance to default (DD)**: the Merton-based measure of the gap between asset value and the face value of debt, scaled by asset volatility. Built as in Hillegeist, Keating, Cram and Lunstedt (2004). Formula in the Appendix file.
- **Frailty**: the effect of shocks correlated across firms, cited to Das, Duffie, Kapadia and Saita (2005) and Duffie, Eckner, Horel and Saita (2006).

## Worked Example: what happens to each signal as the horizon moves from 0 to 36 months (Sec 3.1, Table 4)
1. **Fit falls**: pseudo R2 goes 0.312, 0.188, 0.114, 0.061, 0.044. "Even at three years, however, almost all the variables remain statistically significant."
2. **Leverage decays fast**: TLMTA goes from 3.36 to 0.643.
3. **Past return decays, mostly after 12 months**: EXRETAVG is -7.35 at lag 0, -7.129 at 12 and -2.564 at 36.
4. **Profitability and cash decay more slowly**: NIMTAAVG -29.672 to -14.061. CASHMTA -2.401 to -1.414.
5. **Volatility holds**: SIGMA is 1.482 at lag 0 and 1.334 at lag 36. The t statistic is 13.54 at both.
6. **Market-book rises**: MB goes from 0.054 to 0.125.
7. **Size switches sign**: RSIZE goes from +0.082 to -0.18, "the expected negative sign".
8. **Price switches sign**: PRICE goes from -0.937 to +0.279. The authors put this down to its correlation with market capitalization.
9. **Conclusion**: "market-based variables become more important relative to accounting variables as we increase the forecast horizon." The authors find very similar results with annual accounting data.

## Out-of-sample and accuracy tests (Sec 3.2, Table 5)
- **The test that exists**: pseudo R2 computed out of sample for 1981-2003. Each year from 1981 the coefficients come from data "up to but not including that year".
- **Result**: out-of-sample R2 is close to in-sample R2 (0.310 against 0.312 at lag 0, 0.108 against 0.114 at 12 months, 0.039 against 0.044 at 36 months).
- **The authors' reason**: most failures occur late in the sample, when the rolling and full-sample coefficients are very similar.
- **DD result**: DD alone reaches an R2 of 16% at short horizon. The reduced-form model "almost doubles this number". Adding DD to the best model moves R2 very little.
- **DD sign**: inside the best model DD is positive at lag 0. The authors' reason: the model already holds volatility and leverage, the two main DD inputs. DD turns negative and significant at one and three years.
- **Not in this version**: no classification-accuracy table, no decile hit rates and no ROC-type statistic. The only fit measures are pseudo R2, z statistics and Figure 1.

## Time-series and cross-section checks (Sec 3.3)
- **Aggregate fit (Figure 1)**: average the fitted probabilities across firms to predict the aggregate failure rate. The model catches the long rise in the 1980s and spikes in the early 1990s and early 2000s. It "somewhat overpredicts failures in 1974-5, underpredicts for much of the 1980's, and then overpredicts in the early 1990's".
- **Year dummies**: the authors reject the hypothesis that time effects can be dropped. The model still captures "a large share" of the time variation in bankruptcies.
- **Macro interactions (fn 11)**: "the AAA-BAA credit spread and the Treasury term spread interact with firms' size and leverage to predict bankruptcy". Adding such terms further reduces the time effects. No coefficients are reported.
- **Industry**: the Shumway specification behaves differently in finance, insurance and real estate (lower intercept, more negative profitability coefficient). The best model shows "no strong evidence of sector effects".
- **Interactions with size and leverage**: "no clear evidence that such interactions are important."
- **Working capital ratios (fn 8)**: the current ratio and the acid test ratio are "slightly less effective predictors than CASHMTA".
- **Firm age**: excluded. Shumway found it insignificant.
- **Missing-SIGMA dummy**: not significant (Appendix).

## Anti-patterns
- **Reading the j-month coefficient as a cumulative default probability**: eq 4 is a marginal probability conditional on survival.
- **Comparing R2 across horizons without care**: observations and failure counts differ by horizon. The authors rerun on a common subset and get "very similar results".
- **Using only DD**: "it is clearly better to use a reduced-form econometric approach that allows volatility and leverage to enter with free coefficients and that includes other relevant variables."
- **Trusting the RSIZE or PRICE sign in isolation**: the two are collinear and trade signs with the horizon.

## Key Takeaways
1. Use market-valued leverage and profitability, with a 12-month weighted profitability and return history.
2. For a one-month view, leverage dominates. For a one-to-three-year view, volatility, market-book and size carry more of the signal.
3. A structural DD measure is useful but is dominated once leverage and volatility enter freely.
4. The model has time effects left over. Aggregate credit conditions matter beyond the firm variables.

## Connects To
- **Sec 2 and Appendix**: variable construction.
- **Sec 4**: the 12-month model drives the portfolio sorts. Table 10 compares these coefficients with return-prediction coefficients.
