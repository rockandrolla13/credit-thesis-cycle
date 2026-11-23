# Chapter 9: Cross-sectional stock returns in the UK market: the role of liquidity risk
**Authors**: Soosung Hwang and Chensheng Lu | **Book pages**: 191-213 | **Type**: METHOD (an empirical test design with its results. The sample is UK stocks, 1987-2004, so every number is dated)

## Core Idea
The authors test whether liquidity explains cross-sectional stock returns in the UK. They build a size-free liquidity measure and a liquidity factor from it. A CAPM with that liquidity factor added removes the significant alpha of the UK value premium (Table 9.7). In this sample liquid stocks beat illiquid stocks, which is the reverse of the usual illiquidity premium (s. 9.3.3). The authors conclude that liquidity "could be a useful component in forecasting expected returns" (abstract).

## Frameworks Introduced
- **Two hypotheses on hedge portfolios** (s. 9.2.1).
  1. Size proxies liquidity, so the small-minus-big return spread may reflect different liquidity risk.
  2. Low-volume stocks look like value stocks (Lee and Swaminathan, 2000), so the value-minus-growth spread "should contain the differences in the liquidity risk".
  - Test for both: the liquidity loading in eq. 9.1 must be significant, and the alpha must become insignificant once liquidity is included.
- **Alpha test design** (s. 9.2.1). Step 1: regress a long-short hedge portfolio on the market factor only. A significant intercept means the CAPM fails or an anomaly exists. Step 2: add LIQ (eq. 9.1). If liquidity is a missing factor, the intercept should lose significance.
- **Hedge portfolios at three breakpoints** (s. 9.2.1). The authors form decile, quintile and 30th/70th percentile portfolios on size and on book-to-market. Labels: S-B_d, S-B_q, S-B_p for small minus big. H-M_d, H-M_q, H-M_p in the text and H-L_D, H-L_Q, H-L_P in the tables for high minus low book-to-market.
- **Amihud's illiquidity measure** (eq. 9.2). The ratio of absolute daily return to dollar volume, averaged over the month. The authors like it because it needs only return and volume data.
- **Relative (size-adjusted) liquidity measure** (eq. 9.3). The authors' own change to Amihud: replace dollar volume with turnover rate, and take the natural log. It answers two stated flaws of Amihud's measure (see Anti-patterns).
- **Mimicking liquidity factor LIQ** (s. 9.2.2). "A similar method to that in Fama and French (1993)". Steps:
  1. Compute the monthly liquidity measure for every stock.
  2. At each year end, split stocks into two portfolios at the median liquidity.
  3. The return difference of the two portfolios over the next 12 months is LIQ_t.
  4. Rebalance at each year end.
  5. Do this once with eq. 9.2 (factor LIQ_AMIHUD) and once with eq. 9.3 (factor LIQ).
- **UK SMB and HML with UK breakpoints** (s. 9.2.2). The authors follow Dimson et al. (2003b). Size breakpoint: the 70th percentile of ranked size. Book-to-market breakpoints: the 40th and 60th percentiles. Fama and French (1993) use the 50th, and the 30th and 70th. Reason given: UK large caps cluster in low book-to-market and small caps in high book-to-market, so wider groups keep the corner portfolios diversified.
- **Robustness ladder** (s. 9.3.4-9.3.5). The authors add in turn: a distress factor (Agarwal and Taffler, 2005, z-score based), five macro variables, then SMB, HML and a momentum factor (WML).

## Formulas

All three recovered from PDF, book pp. 194-195. The extraction lost every Greek letter.

    (9.1)  P_{L,t} - P_{S,t} = alpha_i + beta_{i,1} (Rm_t - R_f) + beta_{i,2} LIQ_t + epsilon_{i,t}

- P_{L,t}: return on the long leg (small stocks, or high book-to-market stocks).
- P_{S,t}: return on the short leg (big stocks, or low book-to-market stocks).
- Rm_t - R_f: market excess return. The tables use the FTSE All-Share return minus the UK one-month Treasury bill rate.
- LIQ_t: the mimicking liquidity factor.
- beta_{i,2}: the liquidity loading. It "should be significant" if liquidity effects are present.
- alpha_i: the intercept. It should not differ from zero if liquidity is the missing factor.

Amihud's measure, for stock i in month m:

    (9.2)  gamma_{i,m} = - (1 / D_{i,m}) * SUM_{t=1}^{D_{i,m}}  |r_{i,m,d}| / v_{i,m,d}

- D_{i,m}: number of days with data for stock i in month m.
- r_{i,m,d}: return on stock i on day d of month m. The text below the equation writes it as R_{i,m,d}.
- v_{i,m,d}: dollar trading volume for stock i on day d of month m.

The authors' relative liquidity measure:

    (9.3)  psi_{i,m} = - (1 / D_{i,m}) * SUM_{t=1}^{D_{i,m}}  ln( |r_{i,m,d}| / Turnover_{i,m,d} )

- Turnover_{i,m,d}: turnover rate for stock i on day d of month m. The authors describe it as dollar volume scaled by the stock's market capitalization.
- Both equations carry a leading minus sign as printed. Values are negative in Table 9.1, and the authors read lower values as less liquid.
- As printed, the sum runs over an index t while the summand is indexed by d. The source does not reconcile the two.

## Key Concepts
- **Liquidity**: "a broad and elusive concept, which is not directly observed" (s. 9.1). It needs a proxy.
- **Liquidity proxies listed** (s. 9.2.2): bid-ask spread, price impact of signed order flow (Brennan and Subrahmanyam, 1996), absolute return over dollar volume (Amihud, 2002), and return reversal after high volume (Pastor and Stambaugh, 2003).
- **Value premium / value anomaly**: excess return of high book-to-market stocks over low book-to-market stocks (s. 9.1).
- **Hedge portfolio**: long one extreme portfolio, short the other, written P_L - P_S (s. 9.2.1).
- **Market illiquidity**: the average of individual stocks' illiquidity, value-weighted or equally weighted (s. 9.3.2).
- **Turnover**: "a canonical measure of trading activity", citing Lo and Wang (2000) (s. 9.2.2).
- **Distress factor**: a mimicking factor for distress risk built from a z-score, supplied by Agarwal and Taffler (s. 9.3.4).
- **WML**: a "six by six" momentum factor as in Jegadeesh and Titman (1993) (Table 9.10 note).
- **Newey-West errors**: all regressions are adjusted for heteroscedasticity and autocorrelation of unknown form (table notes).

## Mental Models
- A characteristic spread can be a liquidity spread in disguise. Test it by adding a liquidity factor and watching the alpha (s. 9.2.1).
- A volume-based liquidity proxy carries size inside it. Scale by market capitalization before you compare it with a size factor (s. 9.2.2).
- Market liquidity drops line up with crises. The authors name the 1997 Asian crisis, the 1998 Russian default and LTCM, and 11 September 2001 (s. 9.3.2).
- US results may not travel. The authors quote Dimson et al. (2003a): "It would be dangerous for investors to extrapolate into future from the US experience" (footnote 2).
- The sign of a premium is an empirical matter. Theory says illiquid stocks should earn more. In this UK sample they earned less (s. 9.3.3).

## Anti-patterns
The authors' stated criticisms:
- **Using the bid-ask spread as the illiquidity measure.** It is noisy, because many large trades occur outside the spread and many small trades inside it (s. 9.2.2, citing Brennan and Subrahmanyam).
- **Using dollar volume in the denominator.** It ties liquidity to size, and liquidity "appears to increase" as share prices rise even when it has not changed (s. 9.2.2).
- **Leaving outliers in.** The ratio explodes when volume is near zero. The authors take logs (s. 9.2.2).
- **Assuming liquidity is subsumed by size and book-to-market.** The authors set their result against Fama and French (1992) (s. 9.1).
- **Reading HML as a distress premium.** The distress factor loadings are all insignificant in this sample (Table 9.8a).
- **Using the early sample.** Fewer than 200 stocks had volume data before 1991, so regressions start in 1991 (s. 9.3.1).
- **Small samples.** Fama and French (1998) found a UK value premium of 4.62% from about 185 stocks on average (footnote 6).

## Reference Tables

### Sample and data (s. 9.3.1)
| Item | Value |
|---|---|
| Source | DataStream. Daily returns and dollar volume for the liquidity measures |
| Full period | January 1987 to December 2004. Volume data do not exist before 1987 |
| Portfolio tables | January 1988 to December 2004 (Tables 9.2a, 9.3a, 9.4) |
| Regression period | January 1991 to December 2004 |
| Stocks | 945 in 1987, rising to 2306 in 2004 |
| Stocks with volume data | 96 in 1987, 184 in 1990, 576 in 1991, 1459 in 2004 (Table 9.1) |
| Filters | Negative book-to-market stocks deleted. Delisted stocks kept, to control survivorship bias |

### Table 9.1: market liquidity, annual average (recovered from PDF, book p. 197)
| Year | 1987 | 1988 | 1989 | 1990 | 1991 | 1992 | 1993 | 1994 | 1995 |
|---|---|---|---|---|---|---|---|---|---|
| gamma, value weighted | -0.16 | -0.38 | -0.13 | -0.29 | -0.65 | -0.62 | -0.39 | -0.56 | -0.43 |
| gamma, equally weighted | -0.18 | -0.43 | -0.18 | -2.06 | -2.01 | -1.88 | -1.06 | -1.18 | -0.67 |
| psi | -2.79 | -2.90 | -2.81 | -3.06 | -3.11 | -3.04 | -2.83 | -3.16 | -3.12 |
| No. of stocks | 96 | 179 | 183 | 184 | 576 | 577 | 712 | 826 | 832 |

| Year | 1996 | 1997 | 1998 | 1999 | 2000 | 2001 | 2002 | 2003 | 2004 |
|---|---|---|---|---|---|---|---|---|---|
| gamma, value weighted | -0.42 | -0.50 | -0.75 | -0.46 | -0.67 | -1.46 | -0.51 | -0.38 | -0.38 |
| gamma, equally weighted | -0.47 | -0.91 | -1.22 | -0.88 | -0.87 | -1.81 | -1.56 | -1.13 | -0.68 |
| psi | -3.18 | -3.28 | -3.44 | -3.22 | -3.31 | -3.22 | -3.06 | -2.57 | -2.45 |
| No. of stocks | 798 | 974 | 1003 | 1060 | 1118 | 1325 | 1367 | 1382 | 1459 |

Authors' reading: value-weighted gamma makes 2001 the most illiquid year and 1998 the second. Psi makes 1998 the most illiquid year. Monthly correlation of psi with value-weighted (equally weighted) gamma is 0.29 (0.25). Psi has first- and second-order autocorrelations of 0.83 and 0.72, both significant at 1% (s. 9.3.2).

### Decile portfolios, 1988-2004, percent (Tables 9.2a, 9.3a, 9.4a, 9.4b)
Deciles run 1 to 10 in the order of each table's header.

| Sort (decile 1 → 10) | Row | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | Factor |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Size, small → big | MV share | 0.06 | 0.16 | 0.30 | 0.49 | 0.81 | 1.32 | 2.24 | 4.05 | 9.29 | 81.29 | SMB |
| | Annual return | 1.31 | 0.89 | 0.50 | 0.81 | 2.60 | 2.50 | 2.34 | 2.79 | 4.00 | 7.05 | -4.08 |
| | Monthly SD | 3.32 | 3.52 | 3.51 | 3.81 | 4.07 | 3.89 | 4.00 | 3.91 | 4.04 | 3.90 | 2.72 |
| Book-to-market, low → high | MV share | 17.28 | 14.56 | 17.30 | 16.53 | 9.96 | 7.74 | 5.53 | 4.07 | 3.13 | 3.90 | HML |
| | Annual return | 2.08 | 1.34 | 6.08 | 7.49 | 4.22 | 6.93 | 6.12 | 8.02 | 9.62 | 12.27 | 3.87 |
| | Monthly SD | 3.83 | 4.48 | 3.93 | 4.21 | 4.36 | 4.68 | 5.46 | 5.03 | 4.83 | 4.94 | 2.50 |
| Amihud gamma, illiquid → liquid | MV share | 0.74 | 0.78 | 1.07 | 1.36 | 1.73 | 2.34 | 3.17 | 5.15 | 11.19 | 72.47 | LIQ_AMIHUD |
| | Annual return | -13.74 | -2.67 | -3.44 | 1.76 | 1.75 | -0.03 | 1.88 | 7.03 | 3.64 | 8.74 | -7.85 |
| | Monthly SD | 6.86 | 5.65 | 5.45 | 5.23 | 5.36 | 5.20 | 5.19 | 5.03 | 5.29 | 4.45 | 2.92 |
| Relative psi, illiquid → liquid | MV share | 9.01 | 6.57 | 9.26 | 10.79 | 13.48 | 15.80 | 13.08 | 10.87 | 8.59 | 2.56 | LIQ |
| | Annual return | -6.55 | -0.98 | 3.58 | 4.11 | 6.01 | 9.10 | 7.27 | 6.80 | 11.96 | 11.37 | -7.53 |
| | Monthly SD | 6.09 | 4.98 | 4.69 | 5.16 | 4.85 | 4.63 | 4.37 | 5.07 | 5.18 | 7.03 | 2.02 |

Table notes: the liquidity factor in both Table 9.4 panels is the average return of the most illiquid 50% minus the most liquid 50%.

### Table 9.5: factor correlations and properties (204 monthly observations)
| | LIQ | LIQ_AMIHUD | RM | HML | SMB |
|---|---|---|---|---|---|
| LIQ | 1 | | | | |
| LIQ_AMIHUD | 0.01 | 1 | | | |
| RM | -0.08 | -0.12 | 1 | | |
| HML | -0.24 | 0.03 | 0.20 | 1 | |
| SMB | -0.08 | 0.75 | -0.33 | 0.02 | 1 |
| Monthly mean | -0.65% | -0.68% | 0.80% | 0.32% | -0.35% |
| Monthly SD | 2.02% | 2.92% | 4.20% | 2.50% | 2.72% |
| Historical Sharpe ratio | -0.65 | -0.46 | 0.03 | 0.01 | -0.31 |

### UK versus US factors, monthly (Tables 9.2b, 9.3b)
| | SMB_US | SMB_UK | HML_US | HML_UK |
|---|---|---|---|---|
| Mean | 0.20% | -0.35% | 0.30% | 0.32% |
| Median | 0.20% | -0.40% | 0.30% | 0.20% |
| SD | 3.70% | 2.70% | 3.40% | 2.50% |
| t-test of zero mean | 0.66 | -0.25 | 4.42 | 4.52 |

UK-US correlation of SMB: 0.70 annual, 0.33 monthly. Of HML: 0.24 annual, 0.15 monthly (s. 9.3.3).

### Table 9.6a: hedge portfolios, monthly (recovered from PDF, book p. 206)
| | S-B_D | S-B_Q | S-B_P | H-L_D | H-L_Q | H-L_P | ILLIQ-LIQ_D | ILLIQ-LIQ_Q | ILLIQ-LIQ_P |
|---|---|---|---|---|---|---|---|---|---|
| Mean | -0.271% | -0.257% | -0.251% | 0.819% | 0.756% | 0.544% | -0.914% | -1.243% | -1.462% |
| SD | 3.809% | 3.397% | 3.108% | 4.366% | 3.266% | 2.670% | 3.223% | 4.082% | 6.408% |
| t-test | -0.922 | -0.980 | -1.046 | 2.431 | 3.001 | 2.641 | -3.259 | -4.349 | -4.048 |

_D, _Q, _P are decile, quintile and "30%/40%/30%" breakpoints (table note).

### Table 9.6b: CAPM on the hedge portfolios, 1991-2004 (t-statistics in brackets)
| | S-B_D | S-B_Q | S-B_P | H-L_D | H-L_Q | H-L_P | ILLIQ-LIQ_D | ILLIQ-LIQ_Q | ILLIQ-LIQ_P |
|---|---|---|---|---|---|---|---|---|---|
| C | -0.001 (-0.346) | -0.001 (-0.443) | -0.001 (-0.508) | 0.008 (2.028) | 0.008 (2.402) | 0.005 (1.956) | -0.010 (-2.183) | -0.010 (-3.405) | -0.007 (-3.123) |
| RM-Tbill | -0.546 (-7.988) | -0.439 (-6.807) | -0.395 (-6.659) | 0.047 (0.382) | 0.004 (0.036) | 0.068 (0.862) | -0.461 (-3.446) | -0.330 (-3.567) | -0.276 (-3.981) |
| R-squared | 0.348 | 0.282 | 0.273 | 0.002 | 0.000 | 0.011 | 0.114 | 0.126 | 0.135 |

### Table 9.7: liquidity-augmented CAPM (eq. 9.1)
| | S-B_D | S-B_Q | S-B_P | H-L_D | H-L_Q | H-L_P |
|---|---|---|---|---|---|---|
| C | -0.003 (-1.146) | -0.003 (-1.151) | -0.003 (-1.307) | 0.005 (1.503) | 0.005 (1.609) | 0.003 (1.083) |
| RM-Tbill | -0.586 (-8.315) | -0.474 (-6.957) | -0.432 (-7.170) | -0.006 (-0.051) | -0.053 (-0.498) | 0.014 (0.184) |
| LIQ | -0.358 (-2.502) | -0.321 (-2.061) | -0.343 (-2.664) | -0.489 (-2.859) | -0.511 (-4.073) | -0.488 (-4.994) |
| Wald test of LIQ (F) | 6.261 | 4.246 | 7.095 | 8.176 | 16.591 | 24.937 |
| R-squared | 0.381 | 0.315 | 0.318 | 0.049 | 0.091 | 0.136 |

LIQ here is the factor from the size-adjusted measure psi (table note).

### Tables 9.8a, 9.8b, 9.9: robustness of the H-L result
| Model | Row | H-L_D | H-L_Q | H-L_P |
|---|---|---|---|---|
| 9.8a CAPM + distress | C | 0.009 (1.954) | 0.008 (2.349) | 0.006 (2.026) |
| | Distress_factor | -0.096 (-0.468) | 0.137 (0.871) | 0.184 (1.451) |
| | R-squared | 0.005 | 0.007 | 0.028 |
| 9.8b CAPM + LIQ + distress | C | 0.006 (1.369) | 0.005 (1.563) | 0.003 (1.193) |
| | LIQ | -0.543 (-3.150) | -0.520 (-3.970) | -0.480 (-4.791) |
| | Distress_factor | -0.173 (-0.914) | 0.064 (0.477) | 0.117 (1.109) |
| | Wald test of LIQ (F) | 9.922 | 15.761 | 22.952 |
| | R-squared | 0.059 | 0.094 | 0.143 |
| 9.9 CAPM + LIQ + macro | C | 0.013 (1.664) | 0.015 (2.753) | 0.005 (1.051) |
| | LIQ | -0.343 (-1.878) | -0.332 (-2.440) | -0.389 (-3.580) |
| | Industrial production | -0.191 (-0.382) | 0.260 (0.743) | 0.116 (0.412) |
| | CPI | 1.225 (0.782) | 0.582 (0.495) | 0.400 (0.444) |
| | Term spread | 7.261 (1.113) | 3.514 (0.645) | 2.147 (0.440) |
| | Corporate spread | -0.538 (-0.612) | -0.186 (-0.296) | 0.271 (0.590) |
| | Money supply (M2) | -1.084 (-1.344) | -1.206 (-1.964) | -0.358 (-0.613) |
| | Wald test of LIQ (F) | 3.527 | 5.953 | 12.816 |
| | R-squared | 0.051 | 0.106 | 0.118 |

Macro definitions (Table 9.9 note): growth rate of UK industrial production volume, change in UK CPI, ten-year government bond yield minus one-month T-bill, Merrill Lynch UK BBB minus AAA bond index return, growth rate of broad money.

### Table 9.10: factor models for ILLIQ-LIQ_D
| | CAPM | + SMB, HML | + distress | + WML | + distress + WML |
|---|---|---|---|---|---|
| C | -0.010 (-2.183) | -0.012 (-2.543) | -0.014 (-2.622) | -0.0147 (-2.702) | -0.016 (-2.846) |
| RM-Tbill | -0.461 (-3.446) | -0.614 (-4.845) | -0.552 (-4.506) | -0.5595 (-3.844) | -0.504 (-3.730) |
| SMB | | -0.478 (-3.776) | -0.361 (-2.499) | -0.4354 (-2.933) | -0.338 (-2.109) |
| HML | | 0.401 (2.216) | 0.444 (2.443) | 0.4119 (2.2824) | 0.452 (2.497) |
| Distress_factor | | | -0.227 (-0.973) | | -0.145 (-0.583) |
| WML | | | | 0.1566 (1.091) | 0.179 (1.134) |
| R-squared | 0.114 | 0.190 | 0.198 | 0.197 | 0.207 |

Column headings are this file's labels. The printed table has no column headings.

## Worked Example
The chapter's own test of the value premium, decile case, 1991-2004.
1. **Form the hedge portfolio.** At each December, sort stocks into book-to-market deciles. Hold for 12 months. H-L_D is the top decile minus the bottom decile. Its mean is 0.819% a month, t = 2.431 (Table 9.6a).
2. **Run the CAPM.** Alpha is 0.008 a month with t = 2.028. Market beta is 0.047 with t = 0.382. R-squared is 0.002. The CAPM does not explain the spread (Table 9.6b).
3. **Add LIQ.** Alpha falls to 0.005 with t = 1.503. The LIQ loading is -0.489 with t = -2.859. The Wald F-statistic is 8.176. R-squared rises to 0.049 (Table 9.7).
4. **Add the distress factor alone.** Alpha is 0.009 with t = 1.954. The distress loading is -0.096 with t = -0.468 (Table 9.8a).
5. **Add LIQ and distress together.** Alpha is 0.006 with t = 1.369. LIQ is -0.543 with t = -3.150 (Table 9.8b).
6. **Add LIQ and five macro variables.** Alpha is 0.013 with t = 1.664. LIQ is -0.343 with t = -1.878 (Table 9.9).
7. **Authors' verdict.** "A liquidity-augmented CAPM can successfully explain the observed value anomaly" (s. 9.4).

## Key Takeaways
1. **Size.** UK big stocks beat small stocks. The largest decile returned 7.05% a year and the smallest 1.31%, a gap the text gives as 5.7% (Table 9.2a). SMB averaged -0.35% a month and does not differ from zero (t = -0.25, Table 9.2b). The CAPM explains the size hedge portfolios, with no significant alpha (Table 9.6b).
2. **Value.** The value premium is significant. The decile spread is "over 10%" a year. Monthly HML is 0.32% with t = 4.52 (Table 9.3b). All three CAPM alphas are significant per the authors (Table 9.6b).
3. **Liquidity sign.** Liquid stocks beat illiquid stocks. The decile spread is "over 22%" a year on Amihud's measure and "almost 18%" on the relative measure (s. 9.3.3). The most illiquid 30% of stocks on Amihud's measure had negative average annual returns.
4. **Size contamination.** LIQ_AMIHUD correlates 0.75 with SMB. LIQ from the relative measure correlates -0.08 with SMB and 0.01 with LIQ_AMIHUD (Table 9.5a).
5. **Liquidity and value.** With LIQ added, all three H-L intercepts become insignificant, and all LIQ loadings are significant at the 99% level per the authors (Table 9.7).
6. **Liquidity and size.** LIQ loadings on the three S-B portfolios are significant at the 95% level. The authors say liquidity risk "partly explains the excess return of big over small stocks" (s. 9.3.4).
7. **Liquidity premium survives.** The ILLIQ-LIQ_D alpha stays between -0.010 and -0.016 a month, with t from -2.183 to -2.846, across five factor models (Table 9.10).
8. **Sharpe ratios.** LIQ and LIQ_AMIHUD have the largest absolute Sharpe ratios. The authors say investors can be rewarded for "buying liquid and selling illiquid stocks" (s. 9.3.3). Long big and short small ranks third.
9. **Open questions the authors leave.** Is liquidity a systematic risk? Is it linked to beta? An unreported result gives beta 1.36 for the most liquid decile and 0.90 for the most illiquid (s. 9.4).
10. **Dated sample.** One market, 14 years of regressions, and a period that includes the 1998 and 2001 liquidity shocks. Treat the signs and magnitudes as findings for that sample.

## Source Defects
- **Recovered from PDF.** Eqs. 9.1 to 9.3 (book pp. 194-195). The extraction dropped alpha, beta, epsilon, gamma and psi and broke the fractions. Tables 9.1, 9.4a, 9.4b, 9.6a and 9.6b were checked on the page. The extraction replaced decimal points after minus signs with spaces. Tables 9.2, 9.3, 9.5 and 9.7 to 9.10 were also checked against the page.
- **Page offset.** PDF page = book page + 5 in this chapter, not + 12.
- **Source inconsistencies, recorded and not corrected.**
  - Section 9.2.2 defines LIQ as the return difference "of the liquid and illiquid portfolios". The table notes define it as illiquid minus liquid. The negative means in Table 9.5b fit the table notes.
  - The text calls gamma an "illiquidity measure" and a "liquidity measure". The printed formula has a leading minus sign.
  - Eq. 9.2 and 9.3 sum over t but index by d. The text writes R where the formula writes r.
  - Hedge-portfolio labels differ: H-M in s. 9.2.1, H-L in the tables. The third breakpoint is "thirtieth/seventieth percentile" in the text and "30%/40%/30%" in the table notes.
  - Table 9.6 headers print "aILLIQ-LIQ". No note explains the "a".
  - Tables 9.6 and 9.10 do not say which liquidity measure sorts the ILLIQ-LIQ portfolios. The ILLIQ-LIQ_D mean in Table 9.6a (-0.914% a month) is smaller than the decile spreads the text quotes from Table 9.4.
  - Table 9.5b prints a "Historical Sharpe ratio" of -0.65 for LIQ, equal to its monthly mean in percent. The chapter does not give the Sharpe formula.
  - Table 9.9: the H-L_Q intercept has t = 2.753 and the H-L_D LIQ loading has t = -1.878. The text still calls the result robust and does not discuss these cells.
  - Table 9.2a covers 1988-2004. The text calls it "this entire 17-year period". The data start in 1987.
  - Footnote 9 says the macro data come from the OECD. The Table 9.9 note says Datastream.
- **Not recoverable.** Figures 9.1 to 9.4 are charts. Only their captions and axis ranges are in the text.

## Connects To
- **ch01-market-efficiency-and-forecasting**: this chapter treats a factor alpha as evidence against a pricing model. Chapter 1 frames what such evidence means for forecasting.
- **ch05-choices-in-forecast-construction**: the breakpoint, weighting and sample choices here are forecast-construction choices.
- **ch10-information-horizon**: value-type signals reappear there as slow-decay information with long horizons.
- **ch12-investments-as-bets**: the hedge portfolios here are long-short bets with stated means and standard deviations.
