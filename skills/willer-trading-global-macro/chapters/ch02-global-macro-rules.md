# Chapter 2: Global Macro Rules

## Core Idea
Macro funds earned lower returns than the S&P but a much better return per unit of risk, and four conditions favour them now: expensive equities, the end of QE, rates well above zero, and positive cash yields. The chapter also fixes the measurement conventions for the whole book.

## Frameworks Introduced
- **Return attribution of macro funds** (rolling 18m regression of BarclayHedge macro returns on equities, bonds, commodities, DXY and the Barclay CTA index):
  - R² ranges from 5% to 95%, average 70%.
  - CTA index: the only "reasonably stable" beta, almost always positive, explains about 20% of returns on average.
  - Equities: average univariate explanatory power 36%. The beta swings between positive and negative.
  - Bonds: average R² 8%. The beta also swings sign. Monthly data may miss tactical rates trading.
  - DXY: the only asset class with an insignificant coefficient over 1997 to 2024, but highly time-varying. Average absolute rolling t-statistic above 2.
  - Commodities: add to returns, "tend to be traded from the long side".
- **Four reasons for a "bright future"**:
  1. *Equities are expensive.* CAPE is near its dot-com peak. Expected long-term returns are "typically negative" near such extremes. CAPE is hard to use as a real-time timing tool.
  2. *Volatility rises during QT.* QE suppressed volatility and rate dispersion. Average rolling annual macro returns were markedly lower post-GFC.
  3. *Rates bets have the highest Sharpe ratio and work better with rates above zero.* Proxy: long or short by the 200d MA, positions volatility adjusted, each asset class targeted at 10% ex ante volatility. Fixed income delivered the strongest risk-adjusted returns but was less profitable when US rates were at zero.
  4. *Cash cushion.* Managers hold large T-bill balances because futures and swaps need little margin. In the highest quintile of 3m T-bill yields average annualized macro fund returns were over 12%. In the post-GFC zero-rate period they were "barely 2%".
- **Base-rate method**: establish the typical path under common circumstances, then analyze why this time may differ, or segment history to the specific scenario.
  - Why it works: a framework raises the ability to withstand drawdowns. Trades made on predictions without a framework get second-guessed as soon as prices move against them.

## Key Concepts
- **Excess return over cash**: returns over US T-bills. This is the default return measure. It mimics a leveraged investor who finances near the risk-free rate.
- **Information ratio (IR)**: excess return divided by volatility. The authors treat it as very similar to the Sharpe ratio.
- **Active information ratio**: IR calculated only over the periods when the strategy holds a position. Used for short-holding-period strategies.
- **Risk/reward**: annualized return over volatility (no cash deduction).
- **Positive convexity of macro funds**: macro funds do much better in relative terms when equities fall. They may lag very strong equity months.
- **55d moving average**: the authors' consistent default parameter, chosen to limit overfitting.

## Mental Models
- Think of the market as trading "two or three stories at a time", and often one. A one- or two-variable framework is therefore useful despite omitted variables.
- Use the framework to set priors. Kahneman's base-rate point: get the prior right before reasoning about specifics.
- Use T-bill income as drawdown cushion: high cash yields keep risk appetite high.

## Anti-patterns
- **"Every time is different"**: a specialist's view that misses the forest for the trees.
- **Using CAPE to time the market**: the authors call it difficult in real time, partly because an AI bubble may still be running.
- **Demanding statistical significance**: the authors do not. They accept small samples if the result matches economic logic. Treat their numbers accordingly.

## Reference Tables
Macro hedge fund index (BarclayHedge) vs S&P, 1997 to mid-2025:

| Measure | Macro funds | S&P |
|---|---|---|
| Annual geometric return | 6.8% | 9.4% |
| Risk/reward (return / volatility) | 1.23 | 0.65 |
| Excess over T-bills / volatility | 0.83 | 0.51 |
| Beta to SPX (monthly) | 0.17 | n/a |

The authors note BarclayHedge may understate returns because some of the largest funds are not in the index.

Backtest conventions (section 2.8):

| Convention | Authors' choice |
|---|---|
| Transaction costs | typically not adjusted |
| In-sample vs out-of-sample | not formally distinguished |
| Risk management overlays | none |
| Statistical significance | not required |
| Skew and kurtosis adjustments (Lo, 2002) | "little difference in practical applications" |

## Worked Example
How to proxy macro returns by asset class (section 2.5). Take each asset class. Go long above the 200d MA and short below it. Scale positions by volatility. Target 10% ex ante volatility for each asset-class strategy. Compare the cumulative lines. The fixed-income line is the strongest over time, and it flattens in the period when US rates were at zero. The authors read this as evidence that rates trading needs rates away from zero.

## Key Takeaways
1. Judge every strategy in the book on excess return over cash and on IR.
2. A macro book has low but positive equity beta (0.17) and gains relative ground when equities fall.
3. Trend following (CTA beta) is the one stable component of macro fund returns.
4. Expect better macro returns with QE absent and cash yields high.
5. "History rules, but flexibility dominates": the authors expect some of their strategies to break.

## Connects To
- **Ch 5**: rates as the highest-Sharpe macro bet.
- **Ch 8**: CAPE and valuation as a poor timing tool.
- **Ch 15**: CTAs, positioning and allocation.

## Extraction Notes
- The chapter summary says macro funds had "a strong information ratio of 1.23". Section 2.1 gives 1.23 as return over volatility and 0.83 as the excess-over-T-bills ratio. The source uses the two labels inconsistently.
- Figures 2.1 to 2.7 are charts. Only captions survive.
