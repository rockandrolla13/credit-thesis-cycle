# Chapter 12: Global Macro: A Fund of Hedge Fund's Perspective

**Authors**: Omar Kodmani and Andrew Rozanov, Permal Group (pp. 211-243)

## Core Idea
This is the book's main data chapter. Using index data from 1994 to mid-2012, the authors argue three things. Discretionary macro had top-tier risk-adjusted returns with near-normal tails. Managed futures had modest returns and the best crisis behaviour. Many higher-Sharpe strategies were "short volatility" in disguise. The authors then show that no "typical" macro experience exists, because two macro indexes diverged by about 50 points over the same period. Permal sells funds of macro funds. The authors use public indexes and not their own fund, and say so.

## Frameworks Introduced
- **Why institutions avoided macro before 2007** (p. 213):
  1. Asset-class-based, bottom-up strategies were easier to place.
  2. The "Great Moderation" seemed to leave little for top-down trading.
  3. Macro and CTAs looked riskier on volatility alone. The authors call this "largely an illusion".
- **Short-volatility signature test** (pp. 213, 217): read skewness and kurtosis together. "Strongly negative skewness and large kurtosis is often indicative of a 'short volatility' type strategy": steady returns, then dramatic losses. Illiquid holdings add "artificial smoothing", which understates volatility and overstates Sharpe.
- **Four-statistic comparison** (Tables 12.1 and 12.2): rank strategies on Sharpe ratio, skewness, excess kurtosis and correlation to global equities. No single column is enough.
- **North-west plot** (Figure 12.2): annualised return against equity correlation. The further "north-western" a strategy plots, the better for an equity-heavy portfolio.
- **Post-dislocation event study** (pp. 221-222):
  - Method: take eight dislocation dates. Measure one-, two- and three-year annualised returns from each, including the event month. Average across events. Rank strategies. Repeat on a second index family (HFRX, five crises) as a robustness check.
  - The eight dates: February 1994 (bond rout after the Fed's surprise hike), December 1994 (Tequila Crisis), July 1997 (Asian crisis), August 1998 (Russia and LTCM), March 2000 (technology collapse), September 2001, June 2002 ("fallen angels" after accounting frauds and corporate defaults), August 2007 (global financial crisis).
  - Result: both macro types beat other strategies in year one. "In years two and three, however, on average it pays to reallocate assets away from trend-following CTA managers to discretionary macro managers."
- **Building a portfolio of macro funds** (pp. 224-225):
  1. Diversify across sub-strategies, styles and horizons.
  2. Strategic weight: discretionary to systematic at "2-to-1 is a good starting point". The reason: discretionary gives the best long-run return, systematic gives de-correlation and convexity in crises.
  3. Add satellites: commodities, foreign exchange, volatility, emerging market specialists.
  4. Diversify inside each sleeve. Discretionary: long-term thematic and short-term tactical. Systematic: long-term trend, short-term trend, non-trend.
- **Three drifts to police** (p. 228). In macro, style drift is "built into the strategy", so test for these three:
  1. *Competence drift*: moving into markets without the expertise or infrastructure.
  2. *Liquidity drift*: moving into esoteric, illiquid markets.
  3. *Discretionary overrides* of a systematic model becoming the rule.
- **Two statistical limits on manager selection** (p. 229):
  - Low correlation between discretionary managers means it takes "a much larger statistical sample" to tell two of them apart. Lean more on qualitative review when the record is short.
  - Standard risk factors (equity beta, duration, credit, style, size, momentum, carry) explain "only a small part" of macro returns, even with time-varying exposures. So alpha is hard to prove.
- **Three reasons hedge fund indexes diverge** (pp. 232-233): different reporting managers, different construction and weighting, and the trade-off between investability and representation.
- **Benchmark rules** (pp. 233-234): compare like with like (for example a custom 70/30 index for a mandate with a 30% systematic minimum). Adjust index returns for backfill and survivorship bias. Deduct the cost of running the allocation.

## Key Concepts
- **FoHF**: fund of hedge funds.
- **Convexity (of a CTA)**: outperformance accelerates as risk assets fall (p. 239).
- **Managed account**: a separate account with the underlying manager.
- **Investable index**: an index built only from open funds with capacity (HFRX). A representative index includes closed funds (Dow Jones Credit Suisse).
- **Backfill and survivorship bias**: index biases that "flatter index performance".
- **Greenwich Roundtable 2006 guide**: "Best Practices in Hedge Fund Investing: Due Diligence for Global Macro and Managed Futures Strategies". The authors recommend it as the question template (p. 227).

## Mental Models
- Think of a macro allocation "also as an insurance policy" that pays for itself over time. Trend-following CTAs are the tail-mitigation part (p. 224).
- In a crisis the liquid sleeve becomes the whole portfolio's source of cash. Macro profits "can be quickly monetised" to meet redemptions or buy distress.
- "Listen to the market" at the allocator level: the managers' own unease in late 2006 and early 2007 was a signal.
- A high Sharpe ratio with fat left tails and high equity correlation is not diversification.

## Anti-patterns
- **Judging macro by one index or a few famous funds.**
- **Ranking by Sharpe alone**: distressed and event-driven top the Sharpe table and have "some of the worst risk profiles" in the higher moments.
- **Counting on equity long/short for diversification**: its equity correlation is 0.71, the highest of any strategy.
- **Dedicated short bias as a hedge**: best crisis return, but "prohibitively expensive". It lost almost 52% from 1994 to mid-2012.
- **Fund-of-funds failures the authors list** (p. 234): a second fee layer for mere access, off-the-shelf backward-looking portfolio construction, investing with fraudulent managers, and liquidity mismatch between holdings and investor terms.
- **Comparing own results with an unadjusted index.**

## Worked Example
*1. Long-run statistics, Dow Jones Credit Suisse indexes, January 1994 to June 2012* (Table 12.1). Sharpe ratios use a 3.12% risk-free rate.

| Strategy | Ann. return | Volatility | Sharpe | Skew | Kurtosis | Equity corr. |
|---|---|---|---|---|---|---|
| Global macro | 11.7% | 9.7% | 0.88 | 0.02 | 3.89 | 0.22 |
| Managed futures | 6.3% | 11.7% | 0.27 | 0.03 | -0.02 | -0.04 |
| Hedge Fund Index | 8.6% | 7.6% | 0.72 | -0.18 | 2.47 | 0.59 |
| Convertible arbitrage | 7.5% | 6.9% | 0.63 | -2.68 | 16.16 | 0.43 |
| Event-driven | 9.0% | 6.3% | 0.93 | -2.22 | 10.59 | 0.68 |
| Distressed | 10.0% | 6.6% | 1.03 | -2.14 | 10.76 | 0.65 |
| Fixed income arbitrage | 4.8% | 6.0% | 0.28 | -3.81 | 24.26 | 0.46 |
| Equity long/short | 9.2% | 10.0% | 0.61 | -0.01 | 3.18 | 0.71 |
| Equity market-neutral | 5.4% | 10.3% | 0.22 | -11.86 | 162.63 | 0.30 |
| Dedicated short bias | -2.5% | 17.0% | -0.33 | 0.66 | 1.37 | -0.74 |
| MSCI World | 6.9% | 15.7% | 0.24 | -0.73 | 1.45 | 1.00 |

Cumulative: global macro 686.4%, managed futures 181.3%, MSCI World 182.1%. The equity market-neutral row is distorted by one month, a −40.5% loss in November 2008. The authors suspect a data issue. With that month set to 0% its Sharpe is 1.16, with skew −0.98 and kurtosis 5.11.

*2. The crisis window, August 2007 to February 2009* (p. 220). Equities halved. All but four strategies lost between 14% and 41%. Risk arbitrage was flat. Positive: dedicated short bias +24.4%, managed futures +21.8%, global macro +5.3%. On HFRX: Systematic Diversified CTA +41.2%, Macro/CTA +10.0%, merger arbitrage +5.7%.

*3. Event study averages, eight crises* (Figure 12.5, Table 12.3).

| Horizon | Global macro | Managed futures | Hedge Fund Index | MSCI World |
|---|---|---|---|---|
| 1 year | 12.40% | 10.02% | 5.35% | -0.01% |
| 2 years | 11.80% | 6.37% | 7.80% | 3.72% |
| 3 years | 13.02% | 6.50% | 9.23% | 3.56% |

Managed futures rank second of eleven in year one and ninth in years two and three. HFRX, five crises: Macro/CTA 11.35%, 8.47%, 7.39% against MSCI World −7.27%, −2.79%, −3.47%.

*4. Two macro experiences, January 2009 to June 2012* (pp. 230-232).
- HFRX Macro/CTA: lost money in each of 2009, 2010, 2011 and the first half of 2012. Cumulative −16.3%.
- Dow Jones Credit Suisse Global Macro: almost +35%.
- A synthetic 50/50 of the Dow Jones Credit Suisse Global Macro and Managed Futures indexes: +16%.
- Same label, same period, a gap of 32 to 51 points.

*5. The allocator's tactical sequence around 2007-09* (pp. 225-226), as the authors describe a skilled manager.
1. Late 2006 to early 2007: raise systematic and trend-following weight. Cut net-long directional commodity specialists. Move from relative-value volatility funds to net-long volatility and tail protection. Review the liquidity of discretionary managers that had drifted to multi-strategy or private-equity-type holdings.
2. 2009: return to 2-to-1. Add net-long commodity exposure. Go back to relative-value volatility.
3. 2011-12: shift to short-term tactical traders and short-term or non-trend systems for the choppy risk-on/risk-off market. The 2012 example is the 10-year US Treasury yield moving from 1.8% to 2.4% and back below.
The authors note that not all of these shifts "would have necessarily worked out".

Industry size, June 2012, per HFR (pp. 226-227): about 7,700 hedge funds and US$2,100 billion. Macro broadly defined: about 1,800 funds and US$460 billion. Macro's share of industry assets: about 40% in the early 1990s, 15.4% at end-2007, 22% by Q3 2011 (notes 1, 2, 12).

## Key Takeaways
1. Read skew, kurtosis and equity correlation beside the Sharpe ratio.
2. Trend following earned its place in year one after a dislocation. Discretionary macro earned it over the full cycle.
3. Name the index before you quote "macro returns".
4. The 2-to-1 weight is the authors' rule of thumb from experience. The chapter does not derive it.
5. Index data flatter. Real allocations bear costs and mistakes that indexes do not show.

## Connects To
- **Ch 1**: the history that these statistics support.
- **Ch 4**: overrides and style drift from the manager's side.
- **Ch 10**: the short-option return profile.
- **Ch 13**: an asset owner repeats parts of this analysis with different data.
