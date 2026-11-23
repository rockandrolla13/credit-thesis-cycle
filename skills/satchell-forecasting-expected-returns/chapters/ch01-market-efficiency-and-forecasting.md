# Chapter 1: Market efficiency and forecasting
**Author**: Wayne Ferson | **Book pages**: 1-15 | **Type**: METHOD (a literature review of stock return predictability and of the statistical traps in testing it. It has no new data)

## Core Idea
Two views of return predictability compete. One says predictability is an exploitable inefficiency. The other says predictability is the natural result of required returns that vary over time. Ferson reviews the evidence by information set and then lists the statistical problems that make the evidence hard to read. His verdict: the evidence for weak-form predictability is "more fragile and less compelling" than the evidence for semi-strong form predictability (s. 1.7).

## Frameworks Introduced
- **Fama's three information sets** (s. 1.1). Weak form uses past stock prices. Semi-strong form uses variables that are "obviously publicly available". Strong form uses anything else. The chapter covers the first two.
- **Two views of predictability** (s. 1.1).
  1. *Exploitable inefficiencies*: frictions (trading costs, taxes, information costs) or cognitive imperfections block price-correcting trades. An investor who avoids the friction or bias can profit.
  2. *Efficient markets*: required expected returns vary with interest rates, risk or risk aversion. Then there may be "no abnormal trading profits" and no incentive to exploit the pattern.
- **Return decomposition** (s. 1.1). Return equals conditional expected return plus an unexpected part with zero conditional mean. In the efficient view, all predictability sits in the first term.
- **The joint hypothesis in stochastic discount factor form** (s. 1.2, eq. 1.1). A test needs (a) a model of equilibrium, which is a choice of m, and (b) a statement that the predictor Z lies in the market's information set. A rejection cannot say which part failed.
- **Martingale as a special case** (s. 1.2). If m is constant over time, eq. 1.1 implies a constant conditional expected return. Then no information predicts returns.
- **Weak-form autoregression** (s. 1.3, eq. 1.2). Regress the H-period return on the previous H-period return. Group studies by horizon H.
- **Relative predictability** (s. 1.3). One group of stocks has predictably higher returns than another. A long-short trader can profit even if both groups rise or fall. Past winners that keep winning are "momentum". Past winners that then lose are "reversals".
- **Variance decomposition test for time-varying expected returns** (s. 1.3, Ferson et al. 2005). Unconditional variance equals expected conditional variance plus the variance of the conditional mean. Estimate the first from high-frequency returns inside each month. Subtract. The difference is the variance of the monthly expected return.
- **Semi-strong predictive regression** (s. 1.4, eq. 1.3). Regress the H-period return on lagged public variables Z.
- **Three categories of predictor** (s. 1.4): valuation ratios, calendar and seasonal effects, and "other" variables.
- **Why valuation ratios should predict** (s. 1.4). With P = c/R, the cash flow yield c/P equals the expected return. With Gordon growth, c/P = R - g. So a moving dividend/price ratio must forecast returns, cash flow growth, or both.
- **Three ways to estimate the long-horizon slope** (s. 1.5). See the reference table.
- **Sophisticated versus naive data mining** (s. 1.5). The sophisticated kind counts the number of searches when it judges significance. The naive kind does not.

## Formulas
Eqs 1.1-1.3 and footnote 1 were recovered from the PDF (book pp. 2, 3, 5). PDF page = book page + 9 in this chapter. The text extraction lost every Greek letter.

    (s. 1.1)  R = E(R | Omega) + u ,   E(u | Omega) = 0

- Omega: the information at the beginning of the period. u: the unexpected return.

    (1.1)  E{ m_t (1 + r_t) | Omega_(t-1) } = 1

- m_t: stochastic discount factor. r_t: rate of return of a financial asset. Omega_(t-1): the information set of economic agents at the beginning of the period.

    (s. 1.3)  r(t, t+H) = SUM_(j=1..H) R_(t+j)
    (1.2)     r(t, t+H) = a_H + rho_H r(t-H, t) + epsilon(t, t+H)

- R_t: continuously compounded return over the shortest measurement interval ending at t. H: return horizon.

    (fn 1) Variance ratio = Var{ r(t, t+H) } / ( H Var(R_t) )

    (s. 1.3) Var(R) = E{ Var(R | Omega) } + Var{ E(R | Omega) }

- Reconstructed from the damaged text and the surrounding prose. Not re-read on the PDF page (book p. 4).

    (1.3)  r(t, t+H) = alpha_H + beta_H' Z_t + v(t, t+H)

- Z_t: vector of variables publicly available by time t. beta_H: the slope whose significance the studies test.

    (s. 1.4) P = c / R            so  R = c / P
             P = c / (R - g)      so  c / P = R - g

- c: expected cash flow or dividend. R: expected rate of return. g: future growth rate.

    (s. 1.5) Cov{ SUM_(j=1..H) R_(t+j) , Z_t } = Cov{ R_t , SUM_(j=1..H) Z_(t-j) }     (if covariance stationary)

- Reconstructed from the damaged text. Not re-read on the PDF page (book p. 9).

## Key Concepts
- **Stochastic discount factor (m)**: the scalar random variable that prices all assets through eq. 1.1. Each asset pricing model implies a different m. The CAPM implies m is linear in the market return (s. 1.2).
- **Joint hypothesis**: any efficiency test also tests a model of equilibrium expected returns (s. 1.2).
- **Non-synchronous trading / bid-ask bounce**: data effects that create serial dependence in daily returns. They "do not represent predictability that can be exploited" (s. 1.3).
- **Momentum**: high-past-return stocks repeat over 3- to 12-month horizons (Jegadeesh and Titman 1993) (s. 1.3).
- **Mean reversion**: negative serial dependence at 4- to 5-year horizons (Fama and French 1988). It fits both views of predictability (s. 1.3).
- **Biased self attribution**: traders think their private information is better than it is, so they under-react to public news (Daniel et al. 1998) (s. 1.3).
- **Disposition effect**: traders hold losers too long (Grinblatt and Han 2003) (s. 1.3).
- **Valuation ratio**: a cash flow measure divided by price. Examples: dividend/price, book/price, payout including repurchases, consumption/wealth (s. 1.4).
- **"Federal Reserve Model"**: Malkiel's (2004) label. It models the market price/earnings ratio on producer prices, Treasury yields and other variables. Malkiel finds it does not beat buy-and-hold (s. 1.4).
- **Stambaugh bias**: finite-sample bias in the slope when shocks to the predictor correlate with the return shock, as with a dividend/price ratio (s. 1.5).
- **Spurious regression**: a "significant" slope between independent persistent series. For returns the risk comes from a persistent expected-return component (s. 1.5).
- **Conditional asset pricing / Conditional Performance Evaluation**: models that let expected returns, risk and volatility vary over time, and their use to judge portfolio managers (s. 1.7).

## Mental Models
- **Returns are expected return plus noise.** Expected returns are more persistent than returns. So their variance accumulates faster with horizon, and R-squared rises with horizon (s. 1.4).
- **Small R-squared can still matter.** Stocks are long-duration assets. A small change in expected return gives a large change in value (s. 1.4).
- **An ARMA signature.** If expected returns are autoregressive, returns are autoregressive plus white noise. The AR and MA coefficients should have opposite signs, because a rise in expected return lowers price today (s. 1.3, Conrad and Kaul).
- **Slicing invites stories.** "For each approach to slicing and dicing the data there is a clever story" (s. 1.6).
- **A spurious predictor has a life cycle.** It appears in the literature and then fails on fresh data. "To some extent, the literature has evolved in this way" (s. 1.6).

## Anti-patterns
- **Reading daily serial dependence as predictability.** It can come from bid-ask bounce or non-synchronous trading (s. 1.3).
- **Naive data mining.** Examine 100 independent variables and expect five to be "significant" at the 5% level with no true relation (s. 1.5).
- **Ignoring publication selection.** "No one knows how many insignificant regressions were run" (s. 1.5).
- **Testing many horizons and reporting the best.** Of 20 independent horizons, one is expected to be significant at 5% under the null. The U-shape of Fama and French (1988) is "likely to be observed by chance" (Richardson 1993) (s. 1.5).
- **Overlapping returns with ordinary standard errors.** Overlap induces a moving average of order H - 1 in the errors. Returns are also conditionally heteroscedastic (s. 1.5).
- **Trusting a persistent predictor.** Data mining and spurious regression "reinforce each other", because persistent series are more likely to be found significant (Ferson et al. 2003) (s. 1.5).
- **Treating an out-of-sample failure as proof of no predictability.** A variable can have real predictive power and still fail to beat a naive benchmark out of sample (s. 1.5).
- **Ignoring trading costs.** Lesmond et al. (2004) and Korajczyk and Sadka (2004) conclude that costs consume the apparent excess returns of momentum strategies (s. 1.3).

## Reference Tables

**Weak-form evidence by horizon (s. 1.3)**

| Horizon | Finding as reported | Caveat as reported |
|---|---|---|
| Daily, intra-day | Small, statistically significant serial dependence | Bid-ask bounce, non-synchronous trading. Not exploitable |
| Weekly | AR coefficient on portfolios positive, near 0.5. It explains up to 25% of small-firm portfolio variation (Conrad and Kaul). Some reversals (Lehman 1990) | Index futures show little weekly predictability (Boudoukh et al. 1994) |
| Monthly | Sparse evidence. Some reversals (Jegadeesh 1990) | Ferson et al. (2005): predictability before 1962, little in modern data, none after 1992 for the market |
| 3-12 months | Momentum. Top 20% winners over 6 months beat losers by about 1% per month for the next 6 months (Jegadeesh and Titman 1993, US 1927-1989, focus 1965-89) | Risk adjustment mostly fails to explain it. Trading costs may consume it |
| 4-5 years | Mean reversion (Fama and French 1988). Long-run reversals (DeBondt and Thaler 1985) | Statistical criticism. Reversals sit mainly in January and in high idiosyncratic risk stocks |

**Semi-strong predictors named (s. 1.4)**

| Category | Variables named |
|---|---|
| Valuation ratios | Detrended price, dividend/price, book/price, payout with repurchases, consumption/wealth, the "Federal Reserve Model" |
| Calendar and seasonal | Season, January, time of month, holidays, Monday, time of day, sunlight, geomagnetic storms |
| Other: rates and spreads | Short-term Treasury yield (negative coefficient, read as expected inflation by Fama and Schwert 1977). Yield spread of low-quality over high-quality bonds (Keim and Stambaugh 1986). Short-term Treasury spreads (Campbell 1987) |
| Other: volatility | Conditional market variance. Early results weak or negative. Positive once Merton's extra risk factors are added (Scruggs 1998) |
| Other: recent | Equity share in new issues, firms' investment plans, average idiosyncratic volatility, corporate cash holdings, dividend initiation rate, share issuance, political party in office |

**R-squared by horizon (s. 1.4)**: "say 10-15% or less" for monthly to annual horizons. "Up to 40% or more" for 4- to 5-year horizons.

**Three estimators of the long-horizon slope (s. 1.5)**

| Approach | How | Cost |
|---|---|---|
| Overlapping regression | H-period return on Z_t, observed every period | MA(H-1) errors, heteroscedasticity |
| Reverse the sum (Hodrick 1992, Cochrane 1988) | One-period return on the H-period sum of lagged Z | Needs covariance stationarity. Efficiency gain depends on the process |
| Vector autoregression (Kandel and Stambaugh 1990, Campbell 1993) | Model one-period data, infer the H-period slope | Wrong if the VAR is misspecified |

**Momentum's reported concentration (s. 1.6)**: by industry, in large stocks, in shares priced above $5. Absent before 1940. Stronger after 1968. Stronger in expansions than contractions.

## Worked Example
**Duration of equity (s. 1.4).** Gordon model with dividend c = kE.
1. Price/earnings ratio P/E = 15. Payout ratio k = 0.6. Growth g = 3%. Expected return R = 7%.
2. Check: c/P = k / (P/E) = 0.6 / 15 = 4% = R - g.
3. Shock the expected return by 1%, all else equal.
4. Ferson's result: "approximately a 20% change in the asset value".
5. His caveat: this overstates the effect if the shock also changes expected cash flows.

## Key Takeaways
- Ferson gives reasons for scepticism: the random walk logic, data mining, selection bias, sample-specific patterns, and a "host of statistical issues" (s. 1.6).
- He gives reasons for belief: theory expects some predictability, time-varying risk premiums explain much of it, momentum held in 1990-1998 and outside the US, and semi-strong predictors work in other countries and for bonds and futures (s. 1.6).
- Predictability "may be that [it] was never really there, or that it was 'real' when first publicized, but diminished as traders attempted to exploit it" (s. 1.6).
- Firm-specific predictors show no weakening in recent subperiods (Ferson et al. 2005). They may be less data-mined (s. 1.6).
- Campbell and Shiller find market dividend/price ratios do not predict cash flow growth. Cochrane argues they must then predict returns (s. 1.4).
- The interaction of statistical biases with data mining is the open research area Ferson names (s. 1.7).

## Source Defects
- The text extraction dropped Greek letters, the information-set symbol, braces and summation signs. Eqs 1.1, 1.2, 1.3 and footnote 1 were recovered from the PDF (book pp. 2, 3, 5).
- Two identities were rebuilt from damaged text and were not re-read on the page: the variance decomposition (book p. 4) and the covariance identity (book p. 9). The Formulas section marks both.
- The prose, citations and numbers extracted cleanly.
- The Gordon example extracted as "k = 0 6". This file reads it as 0.6. The arithmetic check in step 2 supports that reading.
- The reference list (book pp. 12-15) is not reproduced.

## Connects To
- **ch09-uk-liquidity-risk**: one empirical test of a cross-sectional predictor, with the alpha-test design this chapter's cautions apply to.
- **ch10-information-horizon** and **ch11-optimal-forecasting-horizon**: the choice of horizon H, treated as an optimization.
- **ch05-choices-in-forecast-construction**: regime shifts and non-stationary parameters, which this chapter lists as a statistical issue.
- **ch04-portfolios-from-ordering-information**: a reversal backtest, one of the weak-form effects reviewed here.
