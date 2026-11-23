# Chapter 13: The Case for Global Macro in Institutional Portfolios

**Author**: Arjan Berkelaar, KIMC U.S. Inc (pp. 245-265)

## Core Idea
An asset owner tests the macro case with standard quantitative tools. The method is careful: unsmooth the returns, equalise Sharpe ratios so only correlation and tail behaviour drive the answer, and optimise on expected tail loss as well as variance. The result: managed futures earn large weights as a diversifier. Discretionary macro has the best history but is the least explained by known risk factors. The author states the limits of his own evidence.

## Frameworks Introduced
- **Summary statistics to compute** (p. 248): mean, volatility, Sharpe, maximum drawdown, skewness, excess kurtosis, 95% VaR, 95% expected tail loss, one-month serial correlation.
- **Expected tail loss (ETL, also CVaR)**: the average loss given that the loss exceeds VaR. Example: developed equities have a monthly 95% VaR of 7.96%. In the worst 5% of months the average loss was 10.7%.
- **Serial correlation as an illiquidity test** (p. 248, note 5): correlation of returns with their one-month lag. High values signal return smoothing. Then "annualised volatilities tend be underestimated, while Sharpe ratios tend to be overestimated", and volatility can no longer be annualised with the square root of 12.
- **Three adjustments before optimising** (p. 250):
  1. *Unsmooth* hedge fund returns (Conner 2003. Getmansky, Lo and Makarov 2004). The "true" series has the same mean, with higher volatility and higher equity correlation (note 6).
  2. Use *mean/expected tail loss* optimisation beside mean/variance, to capture skew and kurtosis. It can be written as a linear programme (Rockafellar and Uryasev 2000).
  3. *Equalise Sharpe ratios* across assets (0.3 for asset classes, 0.5 for hedge fund strategies). Then "optimal portfolios will therefore solely be driven by correlation effects and tail risk". Using history would "heavily bias the results in favour of global macro".
- **Why ETL and not VaR** (note 7): VaR "is not sub-additive" (Artzner et al. 1999), so diversification can raise measured VaR. The author notes the Basel Committee proposed on 3 May 2012 to move to expected shortfall.
- **Tail-hedge tests** (pp. 253-256):
  1. Returns in named drawdown windows where developed or emerging equities fell more than 15%.
  2. Average annualised return across all equity-down months against all equity-up months.
  3. Scatter of strategy returns on equity returns with a fitted polynomial. A *concave* fit means more equity exposure in falling markets. A *convex* fit means protection.
- **Two risk-factor regressions** (pp. 257-262):
  - *Set 1*: MSCI Barra equity factors plus a rates factor (10-year government bonds over three-month bills) and a credit factor (US investment-grade corporates over governments, duration-adjusted). January 1998 to April 2012.
  - *Set 2*: Fama-French global factors (equity premium, value, size), equity momentum, change in the 10-year Treasury yield, change in the credit spread (Moody's BAA yield minus 10-year Treasury), and five Fung-Hsieh trend-following factors (bonds, currencies, commodities, interest rates, equities) built from look-back straddles. January 1994 to June 2011.
- **Three qualitative points** (pp. 262-263):
  1. Due diligence matters more because macro is more opaque. For discretionary funds: the outlook, how it becomes trades, implementation, risk control. For systematic funds: the theory behind the algorithms, their development history, the team's modelling experience, and the embedded risk tools.
  2. Build a diversified set of macro managers. Return dispersion is wide and hedge fund performance shows a "typical lack of performance persistence".
  3. Be patient with discretionary macro. A "relatively small number of big bets" brings volatility and large drawdowns.

## Key Concepts
- **Unsmoothing**: removing positive serial correlation caused by stale pricing.
- **Sub-additivity**: the property that a portfolio's risk is no greater than the sum of its parts.
- **Look-back straddle**: the option structure Fung and Hsieh use to model a trend follower's payoff.
- **Concavity / convexity to equities**: the shape of a strategy's return against the equity return.
- **Backfill and survivorship bias**: acknowledged for the indexes used (p. 246).

## Mental Models
- Use equalised Sharpe ratios when the question is "does this diversify?" and not "has this done well?".
- Think of a low regression R-squared in two ways. It is evidence that the strategy is distinct. It also means the factor loadings deserve little weight.
- Managed futures look like a tail hedge. The author warns that the convexity is "driven by only a few extreme observations" and that he "cannot assign a high confidence to this phenomenon repeating".
- Endowments suit discretionary macro better than pension funds because they can be patient, and a few manager relationships can strengthen their own top-down process (p. 263).

## Anti-patterns
- **Optimising on raw hedge fund returns**: smoothing inflates the weight of illiquid strategies.
- **Using historical means in the optimiser.**
- **Reading correlation as tail protection**: "Correlations only tell part of the story."
- **Over-reading sparse factor loadings** when R-squared is low.
- **Avoiding macro only because it is opaque**: not "a compelling enough reason".

## Worked Example
*1. Asset class statistics, December 1993 to April 2012* (Table 13.1). Risk-free rate 3.15%.

| | Dev. equities | EM equities | Commodities | Fixed income | Global macro | Managed futures |
|---|---|---|---|---|---|---|
| Ann. mean | 7.61% | 9.01% | 7.17% | 6.14% | 11.83% | 6.40% |
| Ann. volatility | 15.7% | 24.5% | 15.9% | 3.7% | 9.7% | 11.7% |
| Sharpe | 0.28 | 0.24 | 0.25 | 0.80 | 0.89 | 0.28 |
| Max drawdown | -53.7% | -61.4% | -54.3% | -5.1% | -26.8% | -17.7% |
| Skewness | -0.73 | -0.71 | -0.61 | -0.28 | 0.01 | 0.02 |
| Excess kurtosis | 1.54 | 1.75 | 2.34 | 1.01 | 3.88 | 0.00 |
| 95% VaR (monthly) | -7.96% | -10.50% | -6.36% | -1.34% | -2.89% | -4.82% |
| 95% ETL (monthly) | -10.7% | -16.4% | -9.9% | -2.0% | -6.0% | -6.3% |
| Serial correlation | 0.19 | 0.19 | 0.09 | 0.05 | 0.17 | 0.06 |

For contrast, serial correlation is 0.55 for the fixed income arbitrage index and 0.51 for the multi-strategy index (note 5). Fixed income's 0.80 Sharpe reflects 20 years of falling rates. Over 1952-2012 it is "closer to 0.3" (note 8).

Correlations (Table 13.2): global macro with developed equities 0.23, emerging equities 0.28, commodities 0.25, fixed income 0.28. Managed futures with developed equities −0.03, emerging 0.01, commodities 0.25, fixed income 0.18. Macro with managed futures 0.30.

*2. Optimisation results.*
- Across asset classes (pp. 250-252): the ETL frontier puts less in commodities and discretionary macro and more in managed futures than the variance frontier. Even under mean/variance the optimiser prefers managed futures to discretionary macro, for diversification against equities and commodities. The equalised 0.3 Sharpe "heavily penalised" discretionary macro against its history.
- Inside a hedge fund portfolio targeting Libor + 500 basis points (Figure 13.7):

  | Strategy | Minimum variance | Minimum 95% ETL |
  |---|---|---|
  | Managed futures | 30% | 36% |
  | Global macro | 8% | 11% |
  | Long/short equity | 7% | 20% |
  | Fixed income arbitrage | 17% | 4% |
  | Distressed | 14% | 6% |
  | Multi-strategy | 11% | 5% |
  | Convertible arbitrage | 8% | 6% |
  | Equity market-neutral | 5% | 4% |
  | Event-driven | 0% | 5% |
  | Cash | 2% | not shown |

  Macro plus managed futures: 38% against 47%. The pie labels were recovered from loose text. The ETL column sums to 97%, so a small slice is missing.

*3. Tail tests.* Seven drawdown windows (note 11): October 1994 to February 1995, September 1997 to September 1998, March 2000 to March 2001, March 2002 to September 2002, October 2007 to March 2008, July 2008 to February 2009, April 2011 to September 2011. Macro, managed futures and fixed income "held up relatively well". The bar values are in a lost chart. Polynomial fits: global macro is concave with R² = 0.0688. Managed futures are convex with R² = 0.0206.

*4. Factor regressions.* Adjusted R² by strategy:

| | L/S equity | Event-driven | Distressed | Multi-strategy | Equity mkt-neutral | FI arb | Convertible arb | Global macro | Managed futures |
|---|---|---|---|---|---|---|---|---|---|
| Set 1 | 78.6% | 67.2% | 64.8% | 55.3% | 41.8% | 49.7% | 58.6% | 25.4% | 7.7% |
| Set 2 | 78.8% | 60.9% | 51.0% | 38.7% | 33.3% | 52.1% | 45.2% | 14.9% | 26.0% |

What the text states (p. 259). Set 1: global macro has an equity beta of 0.26, plus momentum and value exposure and negative size and liquidity exposure. Managed futures load only on value and the term premium. Set 2: managed futures load mostly on the Fung-Hsieh trend factors. Set 2 equity betas: long/short equity 0.51, global macro 0.16, managed futures 0.14. Set 2 monthly intercepts: global macro 1.01%, managed futures 0.70%.

Tables 13.3 and 13.4 show only significant coefficients, so their rows are sparse. Extraction lost the column positions. Other coefficients, including the credit-spread loadings, cannot be assigned to a strategy from the text. Do not quote them.

## Key Takeaways
1. Unsmooth before you compare. Illiquid strategies look safer than they are.
2. With Sharpe ratios equalised, managed futures get the largest hedge fund weight under both risk measures.
3. Switching from variance to tail loss moves weight out of fixed income arbitrage, distressed and multi-strategy.
4. Standard factors explain about 79% of equity long/short returns and 8% to 26% of macro and managed futures returns.
5. The tail-hedge evidence rests on few observations. The author says so.

## Connects To
- **Ch 12**: the same indexes, a different method, the same direction of result.
- **Ch 7**: VaR's place and limits.
- **Ch 10**: smooth returns as a short-option profile.
- **Ch 14**: an asset owner that runs macro in-house.
