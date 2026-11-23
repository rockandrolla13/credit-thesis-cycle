# Appendix: Variable Construction and Distance to Default

## Core Idea
The Appendix gives the formulas for the size, return and accounting ratios, the outlier adjustment, the volatility estimator and the distance-to-default calculation. Use it to rebuild the predictors.

## Reference Formulas (Appendix)

### Size, return and accounting ratios
```
RSIZE_it   = log( Firm Market Equity_it / Total S&P 500 Market Value_t )
EXRET_it   = log(1 + R_it) - log(1 + R_S&P500,t)
NITA_it    = Net Income_it / Total Assets(adjusted)_it
TLTA_it    = Total Liabilities_it / Total Assets(adjusted)_it
NIMTA_it   = Net Income_it / (Firm Market Equity_it + Total Liabilities_it)
TLMTA_it   = Total Liabilities_it / (Firm Market Equity_it + Total Liabilities_it)
CASHMTA_it = Cash and Short Term Investments_it / (Firm Market Equity_it + Total Liabilities_it)
```
COMPUSTAT quarterly items: Data44 for total assets, Data69 for net income, Data54 for total liabilities. The Appendix gives no item number for cash and short-term investments.

### Outlier adjustment
```
Total Assets(adjusted)_it = TA_it + 0.1 * (BE_it - ME_it)
```
- Book equity (BE) is "as defined in Davis, Fama and French (2000)" and detailed in Cohen, Polk and Vuolteenaho (2003).
- **Sign conflict in the source**: the formula prints `BE - ME`. Section 2 says the authors "add 10% of the difference between market and book equity to the book value of total assets, thereby increasing book values that are extremely small". The words imply `ME - BE`. This file records both and does not resolve it.
- After the adjustment, "each of the seven explanatory variables is winsorized using a 5/95 percentile interval". Section 2 says "all variables".

### Volatility
```
SIGMA_{i,t-1,t-3} = ( 252 * 1/(N-1) * Σ_{k in {t-1,t-2,t-3}} r_ik^2 )^(1/2)
```
- `r_ik` is a daily return. The sum runs over the days of the past three months.
- The estimator is "centered around zero rather than the rolling three-month mean".
- SIGMA is missing if there are "fewer than five non-zero observations" in the three months.
- Missing SIGMA is replaced by the cross-sectional mean. A dummy for missing SIGMA is not significant.
- The same replacement applies to missing lags of NIMTA and EXRET inside NIMTAAVG and EXRETAVG.

### Variables with no Appendix formula
- **MB**: Section 2 says only "each firm's market-to-book ratio". Section 3 says MB is the relative value placed on the firm's equity "by stockholders and by accountants".
- **PRICE**: log price per share, truncated above at $15 (Sec 2 and Sec 3). The Table 2 maximum of 2.708 equals log 15.
- **NIMTAAVG, EXRETAVG**: defined in Section 3 (eq 2 and 3). See the Section 3 file.

### Distance to default (DD)
Solve two equations for asset value `TA_DD` and asset volatility `SIGMA_DD`.
```
ME    = TA_DD * N(d1) - BD * exp(-R_BILL * T) * N(d2)
d1    = ( log(TA_DD / BD) + (R_BILL + 0.5 * SIGMA_DD^2) * T ) / ( SIGMA_DD * sqrt(T) )
d2    = d1 - SIGMA_DD * sqrt(T)
SIGMA = N(d1) * (TA_DD / ME) * SIGMA_DD          ("optimal hedge equation")
DD    = ( -log(BD / TA_DD) + 0.06 + R_BILL - 0.5 * SIGMA_DD^2 ) / SIGMA_DD
```
- `ME` is market equity. `BD` is the face value of debt maturing at T. `R_BILL` is the Treasury bill rate.
- `T = 1`.
- `BD` = short-term debt plus one half of long-term book debt. Reason given: long-term debt "may not mature until after the horizon".
- Starting values: `TA_DD = ME + BD` and `SIGMA_DD = SIGMA * (ME / (ME + BD))`. Iterate to consistency.
- `0.06` is "an empirical proxy for the equity premium". The authors prefer a common expected return to "a noisily estimated stock-specific number".
- Missing data rules (fn 17): if BD is missing, use `median(BD/TL) * TL` from the whole data set. If BD is zero, use the same rule with the median taken over small non-zero values (0 < BD < 0.01). Winsorise `BD/(ME+BD)` and SIGMA "at the 0.5% level" before solving.
- The d1 formula is rebuilt here from a two-line layout in the extraction. Check it against the PDF before coding it.

## Worked Example: building the eight best-model inputs for one firm-month
1. Take the latest quarterly net income, total liabilities and cash. Lag them two months (Sec 2).
2. Take market equity from CRSP. Form market assets = market equity + total liabilities.
3. Compute NIMTA, TLMTA and CASHMTA with market assets as the denominator.
4. Compute NIMTAAVG from the last four quarterly NIMTA values with weights that halve each quarter (Sec 3, eq 2).
5. Compute EXRET for each of the last 12 months as the log return minus the S&P 500 log return. Weight them with φ = 2^(-1/3) to get EXRETAVG (Sec 3, eq 3).
6. Compute SIGMA from three months of squared daily returns, annualized with 252.
7. Compute RSIZE as log of firm market equity over total S&P 500 market value.
8. Compute MB with the adjusted book value. Compute PRICE as log of min(price, $15).
9. Winsorise each variable at the 5th and 95th cross-sectional percentiles.
10. Apply the Table 4 coefficients for the chosen horizon inside the logit (Sec 3, eq 4).

## Anti-patterns
- **Using a stock-specific drift in DD**: the authors reject it as noisy.
- **Dropping firm-months with missing SIGMA**: it loses failures of thinly traded firms.
- **Demeaning daily returns in SIGMA**: the paper's estimator is centred on zero.

## Key Takeaways
1. Market assets means market equity plus book total liabilities. It is not enterprise value net of cash.
2. Leverage is total liabilities, not debt.
3. The DD face value of debt is the only place where debt maturity enters the paper.

## Connects To
- **Sec 2**: the prose version of these definitions.
- **Sec 3**: the lag-weighted variables and the DD comparison.
