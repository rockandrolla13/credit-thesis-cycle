# Section 4: Risks and Average Returns on Distressed Stocks

## Core Idea
Sort stocks each January on the 12-month-ahead failure probability. From 1981 to 2003 the most distressed stocks earned low average returns while carrying high volatility, high market beta and high HML and SMB loadings. Risk adjustment makes the underperformance larger, not smaller. The authors call this "discouraging for the view that distress risk is positively priced in the US stock market".

## Frameworks Introduced

### The portfolio construction method (Sec 4)
1. Each January from 1981 through 2003, re-estimate the 12-month-ahead model (Table 4) on historically available data only. This removes look-ahead bias.
2. Rank stocks by fitted failure probability.
3. Form ten **value-weighted** portfolios at percentiles 0-5, 5-10, 10-20, 20-40, 40-60, 60-80, 80-90, 90-95, 95-99 and 99-100. The uneven cut gives more attention to the tails.
4. Drop stocks priced under $1 at formation.
5. Hold for one year. Let weights drift. Do not rebalance monthly.
6. Build long-short portfolios: long the safest 10% (or 20%), short the most distressed 10% (or 20%). Labels: LS1090 and LS2080.

### Delisting treatment (Sec 4)
- Use the CRSP delisting return where it exists. The sample has 6,481 of them.
- Otherwise use the last full-month CRSP return. The authors say this "imparts an upward bias to the returns on distressed-stock portfolios".
- Reinvest proceeds across the remaining stocks by weight.
- Treat a failed firm as delisted, even if CRSP still reports returns.
- Exclude a stock after its first delisting.

### The explanations the authors weigh (Sec 4.1)
| Explanation | Test or evidence | The authors' verdict |
|---|---|---|
| Valuation error on future earnings | Three-day earnings announcement windows (Table 9) | Not supported. The most distressed stocks "actually outperform" at announcements. Alphas outside the windows are "almost identical". |
| Only the "sophisticated" predictors are mispriced | Fama-MacBeth regressions on each predictor (Table 10) | Not supported. Standard variables such as profitability also predict returns. |
| It is just momentum or just volatility | Carhart four-factor alpha, Table 10 | Not the whole story. Momentum cuts the alpha roughly in half. It stays significant. |
| Investors cannot tell distressed stocks apart | Correlation with VIX changes (Figure 5) | Rejected. The stocks move with risk aversion as risky stocks should. |
| Preference for positive skewness (Barberis and Huang) | Skewness in Table 6 Panel C | Possible. Distressed stocks and portfolios are positively skewed. |
| Private benefits of control (von Kalckreuth) | None | Possible. "No direct evidence." |
| Limits to arbitrage | None | Reluctance to short and limited arbitrage capital matter more than shorting cost. |
| Unexpected in-sample developments | Institutional share of ownership (Figure 6) | Suggestive. Debtholders may have become more adept at forcing bankruptcy. Institutions prefer safe stocks. |

## Reference Tables

### Table 6 Panel A: returns in excess of the market, annualized percent (absolute t in parentheses)
| Portfolio | 0005 | 0510 | 1020 | 2040 | 4060 | 6080 | 8090 | 9095 | 9599 | 9900 | LS1090 | LS2080 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mean excess return | 3.39 (1.45) | 2.36 (1.08) | 1.25 (1.06) | 0.93 (1.02) | 0.50 (0.34) | -0.16 (0.07) | -4.44 (1.26) | -8.07 (1.72) | -6.63 (1.24) | -16.30 (1.98)* | 10.20 (1.90) | 6.72 (1.53) |
| CAPM alpha | 2.74 (1.17) | 2.04 (0.92) | 1.40 (1.17) | 1.50 (1.69) | 0.46 (0.31) | -1.53 (0.68) | -6.67 (1.95) | -10.96 (2.40)* | -9.45 (1.79) | -18.71 (2.27)* | 12.60 (2.36)* | 8.98 (2.08)* |
| 3-factor alpha | 5.70 (2.95)** | 5.30 (2.85)** | 2.65 (2.34)* | 0.76 (0.95) | -2.13 (1.72) | -5.77 (3.26)** | -12.73 (4.64)** | -18.15 (5.75)** | -16.13 (3.93)** | -24.25 (3.35)** | 22.89 (6.15)** | 17.43 (5.41)** |
| 4-factor alpha | 2.37 (1.19) | 2.66 (1.37) | 1.49 (1.24) | 2.01 (2.42)* | 0.65 (0.53) | -1.21 (0.70) | -5.80 (2.16)* | -10.01 (3.26)** | -8.19 (1.96) | -20.39 (2.64)** | 12.18 (3.45)** | 8.19 (2.68)** |

### Table 6 Panel B: three-factor loadings
| Portfolio | 0005 | 0510 | 1020 | 2040 | 4060 | 6080 | 8090 | 9095 | 9599 | 9900 | LS1090 | LS2080 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RM | -0.083 | -0.111 | -0.058 | -0.028 | 0.103 | 0.334 | 0.479 | 0.476 | 0.431 | 0.254 | -0.563 | -0.553 |
| HML | -0.474 | -0.499 | -0.176 | 0.122 | 0.379 | 0.613 | 0.849 | 0.918 | 0.831 | 0.608 | -1.396 | -1.183 |
| SMB | 0.212 | 0.037 | -0.117 | -0.091 | 0.121 | 0.263 | 0.591 | 1.466 | 1.538 | 1.964 | -1.394 | -0.833 |

The returns are in excess of the market. So a negative RM loading means a raw beta below one.

### Table 6 Panel C: portfolio characteristics
| Portfolio | 0005 | 0510 | 1020 | 2040 | 4060 | 6080 | 8090 | 9095 | 9599 | 9900 |
|---|---|---|---|---|---|---|---|---|---|---|
| Portfolio SD | 0.112 | 0.105 | 0.057 | 0.044 | 0.071 | 0.111 | 0.169 | 0.225 | 0.257 | 0.394 |
| Portfolio skewness | 1.112 | 0.327 | 0.425 | -0.262 | -0.130 | -0.275 | 1.040 | 1.749 | 2.393 | 1.856 |
| Individual SD | 0.360 | 0.351 | 0.304 | 0.288 | 0.306 | 0.370 | 0.508 | 0.684 | 0.777 | 0.941 |
| Individual skewness | 0.633 | 0.754 | 0.584 | 0.991 | 1.056 | 0.838 | 1.560 | 3.742 | 1.751 | 2.480 |
| Mean RSIZE | -7.786 | -7.479 | -7.236 | -7.172 | -7.371 | -7.803 | -8.744 | -10.000 | -10.584 | -11.273 |
| Mean MB | 2.648 | 3.089 | 2.945 | 2.499 | 2.117 | 1.989 | 2.256 | 2.611 | 3.114 | 3.783 |
| Mean Phat | 0.011% | 0.014% | 0.018% | 0.024% | 0.036% | 0.057% | 0.11% | 0.19% | 0.34% | 0.80% |

Portfolio SD for LS1090 is 0.258 and for LS2080 is 0.211. Phat is the fitted failure probability from the 12-month-ahead model. The table does not state its time unit.

### Table 7 and Table 8: long-short (safest minus most distressed quintile) within each size and book-to-market quintile
| Row | Size sort: mean excess return (Table 7A) | Size sort: 3-factor alpha (7B) | BM sort: mean excess return (8A) | BM sort: 3-factor alpha (8B) |
|---|---|---|---|---|
| Top row (Large / High BM) | 3.02 (0.77) | 11.60 (4.07)** | 9.53 (1.67) | 20.14 (4.89)** |
| 2 | 3.05 (0.78) | 11.58 (4.06)** | 6.42 (1.29) | 15.08 (3.60)** |
| 3 | 4.23 (1.25) | 11.98 (5.03)** | 7.02 (1.84) | 14.90 (4.58)** |
| 4 | 8.60 (2.91)** | 15.19 (7.07)** | 5.98 (1.24) | 15.01 (3.58)** |
| Bottom row (Small / Low BM) | 10.78 (3.05)** | 17.42 (5.80)** | 14.44 (3.02)** | 25.34 (6.81)** |

Annualized percent. See the source-defect note below before using any other cell of Table 7 Panel A.

### Table 9: earnings announcement returns
| Portfolio | 0005 | 0510 | 1020 | 2040 | 4060 | 6080 | 8090 | 9095 | 9599 | 9900 |
|---|---|---|---|---|---|---|---|---|---|---|
| Panel A: 3-day excess return (t-1 to t+1) | 0.413 (7.37)** | 0.104 (1.89) | 0.024 (0.64) | 0.034 (1.29) | -0.010 (0.37) | 0.101 (3.16)** | 0.146 (2.61)** | 0.424 (4.39)** | 0.197 (1.53) | 0.111 (0.34) |

Panel A returns are in excess of the equally weighted market index. Panel B (announcement windows replaced by factor portfolios): LS1090 mean excess return 10.49 (2.03)*, CAPM alpha 12.88 (2.54)*, 3-factor alpha 22.79 (6.51)**, 4-factor alpha 12.27 (3.90)**. LS2080: 5.65 (1.31), 7.84 (1.87), 16.10 (5.29)**, 7.03 (2.56)*.

### Table 10 Panel A: Fama-MacBeth return prediction, 1981-2003 (coefficients in percent, absolute t)
| Predictor | (1) Observed at start of year | (2) Observed at start of month | Sign in failure model (12-month) |
|---|---|---|---|
| NIMTAAVG | 14.55 (4.09)** | 38.99 (11.02)** | negative |
| TLMTA | 0.58 (2.76)** | 0.74 (3.65)** | positive |
| EXRETAVG | 11.50 (6.78)** | 0.88 (0.40) | negative |
| SIGMA | -0.96 (2.68)** | -2.05 (5.85)** | positive |
| RSIZE | 0.02 (0.48) | -0.02 (0.45) | negative |
| CASHMTA | 2.93 (8.49)** | 4.33 (11.42)** | negative |
| MB | -0.19 (6.61)** | -0.05 (1.59) | positive |
| PRICE | -0.62 (5.41)** | -0.80 (6.64)** | negative (n.s. at 12 months) |

## Worked Example: reading the decile long-short portfolio (Sec 4, Table 6)
1. **Raw**: LS1090 earns 10.20% a year (Table 6) with a standard deviation of 26%. The text says its Sharpe ratio is "comparable to that of the aggregate stock market".
2. **CAPM**: alpha rises to 12.60% (Table 6). Distressed stocks have higher market beta, so the risk adjustment hurts them.
3. **Fama-French**: alpha rises to 22.89%. Distressed stocks load heavily on HML and SMB, and the model expects a premium for that.
4. **Carhart**: alpha falls to 12.18%. Distressed stocks have negative momentum. The alpha stays strongly significant.
5. **Where it starts**: under the three-factor model "all portfolios beyond the 60th percentile of the failure risk distribution have statistically significant negative alphas".
6. **When it was earned (Figure 4)**: raw returns are concentrated in the late 1980s and late 1990s, "with negative returns in the last few years". The alphas are "much more consistent over time".
7. **Text against table**: the text quotes 10.0% (t 1.9), 12.4% (t 2.3), 22.7% (t 6.1) and 12.0%. Table 6 prints 10.20 (1.90), 12.60 (2.36), 22.89 (6.15) and 12.18 (3.45). The text also quotes -17.0% for the top 1% where the table prints -16.30. Both are recorded as found.

## Key Concepts
- **Failure probability spread**: the safest 5% average "about 1 basis point". The riskiest 5% (the 95-99 bucket) are at 34 basis points. The riskiest 1% are at 80 basis points.
- **Volatility does not diversify**: individual-stock SD is almost 80% in the 95-99 bucket and 95% in the top 1%. Portfolio SD is 11% for the safest 5%, 26% for the 95-99 bucket and almost 40% for the top 1%. There are slightly under 500 stocks per 10% of the distribution (fn 14).
- **Size**: the value-weighted average size of the safest 5% is "over 16 times larger" than that of the most distressed 5%. Equal-weighted, about 9 times.
- **Market-book is U-shaped**: high at both extremes, lower in the middle. Distressed stocks have "the market-book ratios of growth stocks, but the factor loadings of value stocks".
- **Size interaction (Table 7)**: the raw return gap between safest and most distressed quintiles is "three times larger" in the smallest size quintile than in the largest. The three-factor alpha gap is "about 50% greater".
- **Value interaction (Table 8)**: raw underperformance is more extreme among growth stocks. The difference disappears under the three-factor model.
- **DD sort**: sorting on distance to default also gives low returns for distressed stocks, "contrary to the findings of Vassalou and Xing (2004)".
- **VIX link (Figure 5)**: the monthly correlation between the LS1090 return and the change in VIX is 0.23, over the period since 1990. Investors "flee to quality". The authors note this is consistent with the positive correlation between credit spreads and the VIX in the bond and CDS literature.
- **Institutional link (Figure 6)**: the correlation between the LS1090 raw excess return and the change in the institutional ownership share is 0.31. Safe stocks beat distressed stocks most in the late 1980s, when institutional ownership grew fast.

## Mental Models
- Think of leverage as the one "salient" variable. In Table 10 it predicts failure **and** higher returns. The authors suggest even unsophisticated investors price it.
- Think of the other failure predictors as unpriced. Low profitability, low past return, high volatility, low cash and high market-book each predict failure and **lower** returns.
- Use the VIX correlation as a test of whether the market recognises a risk, separate from whether it pays for it.

## Anti-patterns
- **Treating the value or size premium as a distress premium**: the paper's central negative result.
- **Dropping delisting returns**: it biases distressed-stock returns upward.
- **Monthly rebalancing with sub-$1 stocks**: bid-ask bounce and turnover costs distort returns.
- **Reading the anomaly as permanent**: the authors say it may be "an in-sample phenomenon". It "could disappear or even reverse if institutional ownership stabilizes" (Sec 5).

## Source-defect note
In Table 7 Panel A the "Small" row prints 3.72, -0.32, -3.44, -6.09 and -10.72. Table 8 Panel A prints the same five numbers in its "Low" row. In Table 7 these numbers do not reproduce the printed Low - High value of 10.78 or the printed Large - Small row. In Table 8 they do reproduce the printed 14.44. So the five cells in the Table 7 "Small" row look like a copy error in this working paper version. Do not use them. The Low - High column of Table 7 is reported above as printed.

## Key Takeaways
1. From 1981 to 2003, higher fitted failure risk went with lower stock returns, almost monotonically.
2. Standard risk models make the result stronger. The momentum factor halves it.
3. The effect holds in every size and book-to-market quintile. It is strongest in small stocks.
4. Earnings surprises do not explain it.
5. Equity investors did recognise these stocks as risky (the VIX test). They were still not paid for it in this sample.

## Connects To
- **Sec 3**: the 12-month model that defines the sort.
- **Sec 5**: the authors' ranking of explanations.
