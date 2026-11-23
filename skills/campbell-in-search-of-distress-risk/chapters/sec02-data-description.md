# Section 2: Data Description

## Core Idea
The section defines the two failure indicators, the sample, and the ten explanatory variables. It states the outlier rules and the timing lag. Table 2 shows how bankrupt and failed firm-months differ from the rest.

## The event definitions (Sec 2)
- **Bankruptcy indicator**: from Chava and Jarrow (2004). Sources: Wall Street Journal Index, SDC database, SEC filings, CCH Capital Changes Reporter. It equals one in the month a firm files under Chapter 7 or Chapter 11. It is zero otherwise, including when a firm leaves the data through acquisition or delisting. Span: January 1963 to December 1998.
- **Failure indicator**: equals one if a firm "files for bankruptcy, delists, or receives a D rating". Span: January 1963 to December 2003.

## Data sources and sample (Sec 2, Table 2)
- Quarterly accounting data from COMPUSTAT. Monthly and daily equity data from CRSP.
- 1,695,036 firm-months with complete data. 797 bankruptcy months. 1,614 failure months.
- To enter Table 2 a firm-month needs leverage, profitability, excess return and market capitalization. Volatility is not required. (fn 5)
- Quarterly Compustat data are scarce before the early 1970s. Years before 1973 have "very little influence" on the results. (fn 6)
- Every firm-month has equal weight. So small firms dominate the distributions. (Sec 2.1)

## Variable definitions (Sec 2, Table 2 caption; formulas in the Appendix file)
| Variable | Definition as the paper gives it |
|---|---|
| NITA | Net income over book value of total assets (adjusted, see below) |
| NIMTA | Net income over market value of total assets. Market value of total assets = market equity + book value of total liabilities |
| TLTA | Total liabilities over book value of total assets (adjusted) |
| TLMTA | Total liabilities over (market equity + book liabilities) |
| CASHMTA | Cash and short-term investments over market value of total assets. The "liquidity" measure |
| MB | Market-to-book ratio of the firm |
| EXRET | Monthly log excess return on the firm's equity relative to the S&P 500 index |
| SIGMA | Standard deviation of the firm's daily stock return over the past three months, annualized |
| RSIZE | Log ratio of the firm's market capitalization to that of the S&P 500 index |
| PRICE | Log price per share, truncated above at $15 |

## Adjustment and timing rules (Sec 2)
1. **Book asset adjustment**: follow Cohen, Polk and Vuolteenaho (2003). Add 10% of the difference between market and book equity to book total assets. Purpose: raise book values that are very small and "probably mismeasured".
2. **Negative book equity**: where it remains negative after the adjustment, replace it with "small positive values". The paper does not state the value.
3. **Winsorising**: "all variables at the 5th and 95th percentiles of their cross-sectional distributions".
4. **Timing**: align fiscal year to calendar year. Then lag accounting data by **two months**, so the data are available at the start of the month over which failure is measured.
5. **Missing SIGMA**: replace it with the cross-sectional mean. (fn 5)

## Reference Tables

### Table 1: selected years (bankruptcy data end in 1998)
| Year | Active firms | Bankruptcies | (%) | Failures | (%) |
|---|---|---|---|---|---|
| 1963 | 1281 | 0 | 0.00 | 0 | 0.00 |
| 1974 | 4002 | 18 | 0.45 | 18 | 0.45 |
| 1980 | 4342 | 26 | 0.60 | 26 | 0.60 |
| 1986 | 6208 | 95 | 1.53 | 95 | 1.53 |
| 1990 | 6515 | 80 | 1.23 | 82 | 1.26 |
| 1994 | 8067 | 30 | 0.37 | 33 | 0.41 |
| 1997 | 9544 | 44 | 0.46 | 61 | 0.64 |
| 1998 | 9844 | 49 | 0.50 | 150 | 1.52 |
| 1999 | 9675 | . | . | 209 | 2.16 |
| 2000 | 9426 | . | . | 167 | 1.77 |
| 2001 | 8817 | . | . | 324 | 3.67 |
| 2002 | 8242 | . | . | 221 | 2.68 |
| 2003 | 7833 | . | . | 167 | 2.13 |

What the authors read from Table 1: no bankruptcies in 1967-1969. A rise in the early 1970s. A peak of 1.5% in 1986. High through the early 1990s. The failure series tracks bankruptcy until the early 1980s and diverges late in the sample. Failures rise sharply after 1998, which the authors tie to young firms listed in the late-1990s boom.

### Table 2: summary statistics
| | NITA | NIMTA | TLTA | TLMTA | EXRET | RSIZE | SIGMA | CASHMTA | MB | PRICE |
|---|---|---|---|---|---|---|---|---|---|---|
| **All: mean** | -0.001 | 0.000 | 0.506 | 0.445 | -0.011 | -10.456 | 0.562 | 0.084 | 2.041 | 2.019 |
| All: median | 0.007 | 0.006 | 0.511 | 0.427 | -0.009 | -10.570 | 0.471 | 0.045 | 1.557 | 2.474 |
| All: st. dev. | 0.034 | 0.023 | 0.252 | 0.280 | 0.117 | 1.922 | 0.332 | 0.097 | 1.579 | 0.883 |
| All: min | -0.102 | -0.069 | 0.083 | 0.036 | -0.243 | -13.568 | 0.153 | 0.002 | 0.358 | -0.065 |
| All: max | 0.039 | 0.028 | 0.931 | 0.923 | 0.218 | -6.773 | 1.353 | 0.358 | 6.471 | 2.708 |
| **Bankruptcy: mean** | -0.054 | -0.040 | 0.796 | 0.763 | -0.115 | -12.416 | 1.061 | 0.044 | 2.430 | 0.432 |
| Bankruptcy: median | -0.054 | -0.047 | 0.872 | 0.861 | -0.171 | -12.876 | 1.255 | 0.021 | 1.018 | -0.065 |
| Bankruptcy: st. dev. | 0.043 | 0.030 | 0.174 | 0.210 | 0.148 | 1.345 | 0.352 | 0.062 | 2.509 | 0.760 |
| **Failure: mean** | -0.059 | -0.044 | 0.738 | 0.731 | -0.105 | -12.832 | 1.167 | 0.072 | 2.104 | 0.277 |
| Failure: median | -0.066 | -0.062 | 0.821 | 0.842 | -0.179 | -13.568 | 1.353 | 0.029 | 0.751 | -0.065 |
| Failure: st. dev. | 0.043 | 0.030 | 0.228 | 0.239 | 0.162 | 1.168 | 0.303 | 0.099 | 2.389 | 0.643 |

Observations: 1,695,036 (all), 797 (bankruptcy), 1,614 (failure). The min and max rows are the winsorising bounds. NITA and NIMTA are quarterly.

## Worked Example: the profile of a firm one month before bankruptcy (Sec 2.1)
The authors read the bankruptcy panel of Table 2 like this.
1. **Losses**: mean loss 4.0% of market assets per quarter, "16%" at an annual rate. Median loss 4.7% per quarter, "almost 19%" annual.
2. **Leverage**: average TLMTA "almost 80%". Median "exceeds 87%".
3. **Recent return**: mean -11.5% over the month. Median -17%.
4. **Volatility**: mean annualized 106%. Median 126%.
5. **Size**: "about 7 times smaller" than other firms on average, "10 times smaller" at the median.
6. **Cash**: "about half as much" cash and short-term investments relative to market assets.
7. **Market-book**: slightly higher mean, much higher standard deviation. Some firms fail after losses cut book value. Others fail after bad news cuts market value. So bankruptcy goes with a **wide spread** in MB, not a low or a high level.
8. **Price**: mean "just over $1.50". Median "slightly below $1".

Failed firms versus bankrupt firms: losses more extreme, volatility higher, price lower, size "considerably smaller". Leverage is less extreme and cash is higher.

## Key Concepts
- **Trends in the cross-section**: SIGMA and TLMTA trended up since 1963. NIMTA trended down. The authors cite more conservative accounting and earlier listing of unprofitable firms.
- **Median NIMTA**: 0.6% per quarter or 2.4% annual. The mean is near zero because profitability is negatively skewed.
- **Mean EXRET of -1.1% per month**: reflects small-stock underperformance and the use of a geometric (log) average. The value-weighted mean is "almost exactly zero".
- **Mean SIGMA**: 56% annualized.
- **Spike above zero in NIMTA and NITA**: noted in fn 7 with the earnings-management debate.

## Anti-patterns
- **Reading Table 2 as value-weighted**: it is equal-weighted by firm-month. Value-weighted distributions "look quite different".
- **Using unadjusted book assets as a denominator**: tiny book values create outliers.
- **Treating low MB as the distress signal**: bankrupt firms show both extremes.

## Key Takeaways
1. The market-valued ratios (NIMTA, TLMTA) have "stronger explanatory power" than the book ratios. The authors' guess: market prices absorb news faster or reflect intangibles.
2. Lag accounting data two months. Winsorise at 5/95.
3. Failures and bankruptcies are the same series until about 1997. After that, failures are a much larger set.

## Connects To
- **Appendix**: formulas for each ratio, the SIGMA estimator and the Compustat items.
- **Sec 3**: these ten variables enter the logit.
