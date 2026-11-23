# Cheatsheet: In Search of Distress Risk (Campbell, Hilscher, Szilagyi)

**One line**: failure is predicted best by market-valued leverage and profitability, past returns, volatility, cash, market-book, size and price. Stocks with high failure risk earned low returns in 1981-2003.

## Which signal for which horizon (Table 4, failure, 1963-2003)
| Signal | 1 month | 12 months | 36 months | Rule |
|---|---|---|---|---|
| TLMTA (leverage) | 3.36 | 1.416 | 0.643 | Short-term signal. Decays fast. |
| EXRETAVG (past return) | -7.35 | -7.129 | -2.564 | Holds for a year, then fades. |
| NIMTAAVG (profitability) | -29.672 | -20.264 | -14.061 | Intermediate. |
| CASHMTA (cash) | -2.401 | -2.132 | -1.414 | Intermediate. |
| SIGMA (volatility) | 1.482 | 1.411 | 1.334 | Persistent. Use at every horizon. |
| MB (market-book) | 0.054 | 0.075 | 0.125 | Grows with horizon. |
| RSIZE (size) | 0.082 | -0.045 | -0.18 | Sign flips. Useful at long horizon. |
| PRICE | -0.937 | -0.058 n.s. | 0.279 | Short-horizon signal. Flips. |
| Pseudo R2 | 0.312 | 0.114 | 0.044 | |

## Decision rules (the authors' findings, stated as rules)
- When the horizon is one month, weight leverage, volatility, price per share and profitability most. (Sec 3)
- When the horizon is one to three years, weight volatility, market-book and size more, and leverage less. (Sec 3.1)
- When choosing denominators, use market value of assets over book value. (Sec 2, Sec 3)
- When one quarter's loss or one month's return is the signal, replace it with the 12-month weighted history. (Sec 3)
- When a working-capital ratio is on hand, prefer cash over market assets. The current and acid test ratios were slightly worse. (fn 8)
- When a DD measure is on hand, expect it to add little once leverage and volatility are in. (Sec 3.2)
- When reading a j-month coefficient, treat the output as a marginal probability, not a cumulative one. (Sec 3.1)
- When a price is under $15, the price level itself carries information. Under $1, delisting rules bind. (Sec 3)
- When a model fits firms well, still test year effects. Here they stay significant. (Sec 3.3)
- When a stock looks cheap because it is distressed, do not assume a premium. In this sample there was none. (Sec 4)
- When adjusting distressed returns for risk, expect the gap to widen under CAPM and three-factor models and to halve under momentum. (Sec 4)

## Thresholds and defaults
| Item | Value | Where |
|---|---|---|
| Winsorising | 5th and 95th percentiles | Sec 2 |
| Accounting lag | 2 months | Sec 2 |
| Lag weight | φ = 2^(-1/3) | Sec 3 |
| Price truncation | $15 | Sec 2, Sec 3 |
| Exchange minimum price | $1 | Sec 3 |
| SIGMA window | 3 months of daily returns, x252 | Appendix |
| SIGMA minimum data | 5 non-zero observations | Appendix |
| DD horizon and drift | T = 1, 0.06 + T-bill rate | Appendix |
| DD debt face value | short-term + half of long-term | Appendix |
| Portfolio formation | each January, 1981-2003, hold 1 year | Sec 4 |
| Portfolio price filter | drop stocks under $1 | Sec 4 |

## Tells: a firm one month before bankruptcy (Table 2 medians)
- Quarterly loss of 4.7% of market assets.
- Total liabilities above 86% of market assets.
- Past-month excess return of -17%.
- Annualized volatility of 126%.
- Share price slightly under $1.
- Cash at 2.1% of market assets, against 4.5% for all firms.

## Return facts to quote (Table 6, annualized, in excess of the market, 1981-2003)
| Bucket | Mean excess | 3-factor alpha | Portfolio SD | Phat |
|---|---|---|---|---|
| Safest 5% | 3.39 | 5.70 | 0.112 | 0.011% |
| 80-90 | -4.44 | -12.73 | 0.169 | 0.11% |
| 95-99 | -6.63 | -16.13 | 0.257 | 0.34% |
| Top 1% | -16.30 | -24.25 | 0.394 | 0.80% |
| LS1090 | 10.20 | 22.89 | 0.258 | |

- Correlation of LS1090 with the change in VIX: 0.23. (Sec 4.1)
- Correlation of LS1090 with the change in institutional ownership share: 0.31. (Sec 4.1)

## What the paper does not test
Interest coverage. Debt maturity or refinancing need (outside the DD debt proxy). Floating-rate share. Coupon terms. Net debt to earnings. Margins. Cost structure. Customer concentration. Bond or CDS spreads at firm level. Recovery rates.
