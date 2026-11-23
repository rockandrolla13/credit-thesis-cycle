# Chapter 16: Non Traditional Assets: Private Assets and Crypto

## Core Idea
Bitcoin behaves like a liquidity-driven tech stock, not like gold, so size it with a required-return test and hold it with a trend rule. Private assets look less special once their smoothed returns are corrected: most carry equity beta, and only infrastructure and real estate add something in stagflation.

## Frameworks Introduced
- **What kind of asset is Bitcoin?**: long-term correlations are most consistently high and positive with (technology) stocks, especially post-COVID. Gold is the second most consistent. The negative correlation with DXY has recently flipped to barely positive. Rates are least stable. Bitcoin falls consistently in equity drawdowns (Table 16.1), unlike gold. The expected graduation to a safe asset has not happened: the equity correlation rose and the gold correlation fell. "Bitcoin is mostly a beneficiary of plentiful liquidity."
- **ETF flow sensitivity**: since spot ETFs were approved, every $1bn of weekly flows has been associated with a 3.5% price increase.
- **Reverse optimization for the Bitcoin weight** (in the spirit of Black-Litterman): historical tests are "riddled with survivorship and hindsight bias". Ask what return is required to justify a weight, given today's volatility and correlations. Calibrate risk aversion on a 59/40/1 portfolio.
  - 1% allocation needs an expected annual return of around 12%.
  - 5% allocation needs just below 25%.
  - Historical result for comparison (from 2014): a 5% allocation taken from equities would have raised the IR of a 60/40 portfolio by 0.26. The benefit was front-loaded. The rolling one-year Sharpe peaked in 2018.
- **Trend rule for Bitcoin**: a 3-month moving average rule lifts the IR from 0.95 to 1.26, with returns almost on par with buy-and-hold.
- **Unsmoothing private returns**: reported private returns have high autocorrelation because of infrequent reporting and uncertain valuations. Adjust using the first-order autocorrelation, blending current returns with the previous period's. Then compare with public assets.
  - Private equity: IR advantage over public equity falls from 0.9 points to 0.17. IR still 0.8.
  - Private credit: advantage falls from 0.7 points to 0.26. IR still 0.97. Caveat: no proper down cycle yet.
  - Venture capital: worse IR than public markets after unsmoothing.
  - Real estate: unsmoothed IR about as poor as venture.
- **Diversification test**: unsmoothed PE, VC and private credit are highly correlated with public equities and with each other, also in the worst equity quarters. Real estate and infrastructure correlate much less. Infrastructure and private credit data start in 2008.
- **Factor exposures**: PE, VC, private debt and real estate load on equities and on the size factor. Value and growth factors also matter. PE's size beta has moved close to zero as PE moved into large caps. VC's has not.
- **Private assets by regime** (forward Sharpe ratios):
  - PE: best in overheating and late recession, then Goldilocks. Poor in early recession. Positive but subpar in stagflation. Private debt has a very similar profile.
  - Infrastructure and, to a lesser extent, real estate: decent Sharpe ratios in overheating and stagflation. Infrastructure index starts in 2007. Many projects have inflation-plus pricing.
- **Manager dispersion**: inter-quartile range of net IRRs by vintage is about 20% for VC. Much narrower for private debt. Put more resources into manager selection in PE and VC.
- **Starting valuation**: PE IRRs by vintage correlate with starting public valuations and with forward 10-year US public equity returns. The authors read this as "a more difficult environment" ahead, with a caveat that fast technological innovation may matter more.

## Key Concepts
- **Crypto winter**: a deep crypto bear market. Bitcoin has survived two.
- **Return smoothing**: understated volatility from appraisal-based marks.
- **Unsmoothing**: removing first-order autocorrelation from a return series.
- **Illiquidity premium**: debated sign. Positive if funds may be needed at short notice, negative if illiquidity prevents panic selling. The authors think it should be positive.
- **Net IRR by vintage**: fund return after fees, grouped by start year.
- **Size factor**: small-cap exposure.
- **Reverse optimization**: solving for the expected return that makes a given weight optimal.
- **Private assets' share**: around 10% of total global market capitalization.

## Mental Models
- Think of Bitcoin as part of the risky-asset budget. It does not compete with safe assets.
- Judge a new asset by the return it must deliver from here, not by what early holders earned.
- Think of PE and private credit as equity beta with lagged marks.
- Use infrastructure as the private-market answer to the stagflation gap of Ch 15.

## Anti-patterns
- **Calling Bitcoin digital gold in a portfolio**: it draws down with equities.
- **Sizing Bitcoin from its history**: survivorship and hindsight bias.
- **Reading reported private volatility at face value**: smoothing flatters it.
- **Expecting PE, VC or private credit to diversify equities**: correlations of 0.49 to 0.66 with the S&P.
- **Buying the average venture fund**: the unsmoothed IR is below public markets and dispersion is wide.

## Reference Tables
Table 16.1, largest S&P drawdown episodes and other assets:

| Start | S&P 500 | US bonds | Gold future | Bitcoin |
|---|---|---|---|---|
| Mar-2020 | -12.6% | 2.6% | 1.4% | -25.5% |
| Sep-2022 | -9.4% | -3.7% | -3.2% | -4.1% |
| Dec-2018 | -9.2% | 2.0% | 4.5% | -6.7% |
| Apr-2022 | -8.7% | -3.1% | -2.2% | -15.8% |
| Feb-2020 | -8.4% | 2.5% | -1.3% | -7.4% |
| Jun-2022 | -8.3% | -0.9% | -2.2% | -41.1% |
| Sep-2011 | -7.0% | 1.7% | -11.4% | -37.3% |
| Oct-2018 | -7.0% | -0.7% | 1.6% | -5.3% |
| May-2019 | -6.6% | 2.1% | 1.5% | 62.0% |
| Dec-2022 | -6.1% | -0.9% | 3.8% | -3.4% |
| Aug-2015 | -6.0% | 0.0% | 3.4% | -19.1% |
| Mean | -8.1% | 0.2% | -0.4% | -9.4% |
| Median | -8.3% | 0.0% | 1.4% | -7.4% |

Table 16.2, correlations of unsmoothed returns:

| | S&P 500 | UST | Commodities | IG excess | PE ex VC | VC | Private debt | Real estate |
|---|---|---|---|---|---|---|---|---|
| S&P 500 | 1.00 | -0.38 | 0.38 | 0.74 | 0.66 | 0.49 | 0.55 | 0.25 |
| US Treasury | -0.38 | 1.00 | -0.37 | -0.45 | -0.36 | -0.29 | -0.32 | -0.22 |
| BBG Commodities | 0.38 | -0.37 | 1.00 | 0.49 | 0.50 | 0.29 | 0.50 | 0.29 |
| IG excess | 0.74 | -0.45 | 0.49 | 1.00 | 0.46 | 0.25 | 0.52 | -0.02 |
| PE ex VC | 0.66 | -0.36 | 0.50 | 0.46 | 1.00 | 0.77 | 0.74 | 0.66 |
| Venture capital | 0.49 | -0.29 | 0.29 | 0.25 | 0.77 | 1.00 | 0.43 | 0.43 |
| Private debt | 0.55 | -0.32 | 0.50 | 0.52 | 0.74 | 0.43 | 1.00 | 0.45 |
| Real estate | 0.25 | -0.22 | 0.29 | -0.02 | 0.66 | 0.43 | 0.45 | 1.00 |

Unsmoothing effect on IR advantage over the public counterpart:

| Asset | Advantage, reported | Advantage, unsmoothed | Unsmoothed IR |
|---|---|---|---|
| Private equity | 0.9 | 0.17 | 0.8 |
| Private credit | 0.7 | 0.26 | 0.97 |
| Venture capital | not stated | negative | below public |
| Real estate | not stated | not stated | "about as poor as" venture |

## Worked Example
*How much Bitcoin belongs in a 60/40 portfolio.*
1. Historical test from 2014: replace 5% of equities with Bitcoin. The portfolio IR rises by 0.26.
2. Check the path. The rolling one-year Sharpe peaked in 2018 and has since been lower, with more time below zero. The gain went to early adopters.
3. Reject the historical test as biased: Bitcoin drew attention because of its early performance.
4. Reverse the question. Calibrate risk aversion on a 59/40/1 portfolio. Use Bitcoin's current volatility and correlations.
5. Result: about 12% expected annual return justifies 1%. Just below 25% justifies 5%. Bonds need little expected return because they are negatively correlated with equities and crypto over the full period.
6. Implementation: whatever the weight, hold it with a 3-month moving average rule, which raised the IR from 0.95 to 1.26 at almost the same return.

## Key Takeaways
1. Treat Bitcoin as a high-beta liquidity asset. It needs a double-digit expected return to earn even 1%.
2. Follow the trend in Bitcoin.
3. Watch spot ETF flows as a price driver.
4. Unsmooth private returns before comparing them with public markets.
5. Expect private equity and private credit to behave like public equity across regimes.
6. Use infrastructure, then real estate, for stagflation.
7. In VC the manager matters more than the asset class.

## Connects To
- **Ch 15**: regimes, stagflation hedges and Table 15.1, where Bitcoin failed once the Fed hiked.
- **Ch 11**: private credit and the 200dma monitor on listed private credit funds.
- **Ch 8**: CAPE and 10-year forward returns, liquidity and tech bubbles.
- **Ch 14**: gold as the comparison asset.

## Extraction Notes
- The chapter title is "Non Traditional Assets: Private Assets and Crypto" in the heading. The Contents and Chapter 1 call it "Nontraditional Assets: Crypto and Private Assets".
- The text says spot ETFs were approved in "February 2024". It is recorded as written.
- The sentence on private equity says the advantage "is smaller after smoothing". From context it means after unsmoothing.
- A stray caption fragment ("Raw returns") sits inside the same sentence in the extraction.
- The 3-month moving average is written "3mma" in the source. Whether it is a 3-month or roughly 66-day window on daily data is not stated.
- Figures 16.1 to 16.10 are charts. Regime Sharpe ratios for private assets and the Black-Litterman required-return curve are available only through the numbers quoted in the text.
- Charts with statistics tables still unread in the PDF: Figure 16.3 Bitcoin in 60/40 (p. 374), Figure 16.5 Bitcoin trend (p. 376), Figure 16.6 private asset IRs (p. 377).
