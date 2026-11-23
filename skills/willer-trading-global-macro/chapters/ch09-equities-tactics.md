# Chapter 9: How to Trade Equities: The Tactics

## Core Idea
Tactical equity alpha comes "mostly by fading euphoria and buying panic", and buying panic is the easier half. The POLLS index flags tops, the volatility risk premium flags dips to buy, and positioning, surveys, insiders and seasonals add smaller edges.

## Frameworks Introduced
- **POLLS index** (Citi index of Positioning, Optimism, Liquidity, Leverage and Stress, from Altmann and Raute, 2019):
  - Top signal: above 18 for two days or more. Median outcome is a 5% pullback, with the skew sharply to the downside. Above 18 the likelihood of a positive one-month SPX return drops to well below 40%.
  - Bottom signal: below 8. It typically triggers when the bottom is already well in.
  - Why act early: investors resolve to sit through 5% when optimistic, then sell late once the market is actually down 5%.
  - Record since the February 2023 public write-up: July 2023 (slightly early, correct two months later) and July 2024 ("nailed the top").
- **Problem-solution method for bottoms**: identify the problem the market worries about, define the workable fix, and judge the odds that policymakers deliver it soon. A duration problem (March 2023) needs only a less hawkish Fed. A credit problem needs a political consensus for a bailout and takes much longer.
- **VIX facts**:
  - Forward one-month returns beat unconditional only when VIX is near 60 or above.
  - Top VIX decile: median monthly return 3.95% but annualized Sharpe only 0.62, against 0.49 unconditional.
  - Lowest VIX quintile (below 12): Sharpe above 1.
  - Worst Sharpe ratios: VIX between 17.5 and 21.5.
- **Volatility risk premium (VRP) model**: VRP is VIX minus one-month realized volatility. Buy the SPX when the VRP moves above 2 standard deviations (one-year lookback). Hold for one month (22 trading days).
  - Active IR almost 1.1. Comparisons: unconditional 0.49, VIX 2 standard deviation rule 0.58, buying 2 standard deviation SPX price declines 0.66. It also beats buying on VIX curve inversion.
  - The top VRP decile has 2% median one-month returns. Most other buckets are closer to 1%.
  - It can trigger without a dip when an event lifts implied volatility (see Ch 4, elections).
- **The trade after the trade**: after VIX has been above 50 at least intraday, buy when it falls below 35. VIX tends to fall further and the SPX rallies. This does not find the bottom. It finds the point where investors re-engage.
- **AAII bull-bear survey**: readings below -20 go with higher one-month forward returns. Event study with non-overlapping triggers: 44 periods, and -20 is typically the bottom of the pullback. In the worst 10% of cases significant further downside followed. Readings at or below -40 work well and are very rare. The survey is better at bottoms than tops (June 2003 was a terrible sell signal).
- **CFTC positioning as counter-indicator** (3-year z-score of net positions over open interest, 22-day hold, implementation lagged five days):
  - Asset managers below -2: active IR 0.9 vs 0.5 unconditional.
  - Leveraged funds below -2: active IR above 1.3.
  - Long side: asset managers need a z-score of 3 (1% of the time) for negative returns. Leveraged funds above 2 is already a meaningful negative (8% of the time).
  - Leveraged-fund positioning is the more useful series.
- **Insider rule** (Chronert et al., 2024): when more than 2.5% of insiders buy, the SPX is likely to post double-digit returns over the next 12 months. When fewer than 17% of insiders are selling, returns tend to be very strong.
- **Buybacks**: no relevant contemporaneous correlation between quarterly SPX returns and buybacks. SPX returns lead buybacks by a quarter. Blackout periods (two weeks before earnings weeks) have a higher active IR than unconditional (0.56 vs 0.40). Earnings weeks 0.41. The post-earnings regime has the lowest IR (0.32).
- **Seasonal rules**:
  - Halloween: holding the SPX only from end-October to end-April since 1990 gives an active IR of 0.71 vs 0.48 buy-and-hold.
  - Conditional year-end rally (Saunders and Willer, 2023a): be long in November and December if January to October returns exceed 8%. "It is difficult to lose money." Used out of sample for more than five years.
  - Turn-of-year reversal: the correlation of three-month returns into and out of a date is most negative in late February and early March, at more than -20% over 30 years. It also turns negative in July and late September to early October.
  - April tax effect: equities underperform from about April 5 into April 11, much more after a year up 20% or more. The effect unwinds after April 12. In the seven strong up years since 2004 the median return was -65bp through April 14, then recovered to 1.25% by April 19.
  - Momentum factor seasonality: December strongest, January reversal, consistent with tax-loss harvesting. The December effect is gone in data from 2005.
- **Good news / bad news regimes** (Saunders and Willer, 2023b): combine the sign of CESI with the sign of the correlation between changes in CESI and SPX returns. Implementation lagged one day.

| Regime | CESI | Correlation | SPX IR |
|---|---|---|---|
| Good news is good news | above 0 | above 0 | 0.84 |
| Bad news is good news | below 0 | below 0 | 0.72 |
| Good news is bad news | above 0 | below 0 | 0.20 (worst) |
| Bad news is bad news | below 0 | above 0 | 0.32 |
| CESI above 0 only | above 0 | any | 0.61 |
| CESI below 0 only | below 0 | any | 0.47 |
| Unconditional | | | 0.55 |

  - The correlation is lower on average during hiking cycles.
- **FOMC effect**: mean SPX return on FOMC days is 0.16% vs 0.03% on all days. Hit ratio 54.9% vs 51.1%. A 2 standard deviation move in two-year yields on the day tells little about later equity returns. When the SPX sells off on FOMC day it tends to recover over the next 10 to 12 sessions. "Fade downside momentum on FOMC day but, on balance, go with momentum after positive FOMC days."

## Key Concepts
- **POLLS**: Citi's composite of positioning, optimism, liquidity, leverage and stress.
- **VRP**: implied minus realized volatility, read as fear in excess of what prices are doing.
- **Blackout period**: the two weeks before earnings when companies suspend buybacks.
- **Tax-loss harvesting**: selling losers before year-end to crystallize losses.
- **Halloween indicator**: invest from October 31 to April 30.
- **Active IR**: IR over the days a rule is invested.
- **CESI**: Citi economic surprise index.

## Mental Models
- Use an indicator more readily when it works at both tops and bottoms (POLLS).
- Think of a high VIX as a state where a constant drip of bad news is needed to prevent a relief rally.
- Think of data reactions as a window into the market's view of the Fed reaction function.
- Trust a seasonal pattern more when it has a rationale (taxes, flows).
- Prefer market measures to surveys, with AAII as a useful exception.

## Anti-patterns
- **Buying just because VIX is high**: returns are wider, Sharpe ratios are not compelling.
- **Buying while VIX is above 50**: being one day early can be costly. Wait for the fall below 35.
- **Trading the SPX on buybacks or avoiding blackout periods**: not supported.
- **Using AAII bullish extremes to sell**: unreliable.
- **Using CESI level alone**: the improvement is "potentially mostly noise".
- **Chasing a hawkish FOMC-day sell-off in equities**: it tends to reverse.
- **Momentum trades in Q1**: trends tend to change early in the year.

## Reference Tables
Buy-the-dip rule comparison (hold 22 trading days):

| Rule | Active IR |
|---|---|
| VRP above 2 standard deviations | almost 1.1 |
| SPX price decline of 2 standard deviations | 0.66 |
| VIX move above 2 standard deviations | 0.58 |
| Unconditional | 0.49 |

Sentiment and positioning thresholds:

| Indicator | Buy threshold | Sell threshold |
|---|---|---|
| POLLS | below 8 | above 18 for 2+ days |
| VIX | falls below 35 after 50+ | none given |
| AAII bull-bear | below -20, strong at -40 or below | not reliable |
| CFTC asset managers z-score | below -2 | 3 |
| CFTC leveraged funds z-score | below -2 | above 2 |
| Insider buyers share | above 2.5% | none given |
| Insider sellers share | below 17% | none given |

Figure 9.8, SPX by CFTC positioning z-score, 22-day hold (recovered from PDF p. 220). Supports the positioning rule. Active IR, with % of time in brackets:

| Z-score bucket | Asset managers | Leveraged funds |
|---|---|---|
| Below -2 | 0.92 (5.78%) | 1.37 (8.90%) |
| -2 to -1 | 0.34 (29.40%) | 0.59 (25.36%) |
| -1 to 1 | 0.53 (83.92%) | 0.49 (78.38%) |
| 1 to 2 | 0.48 (31.14%) | 0.52 (35.87%) |
| Above 2 | 0.40 (10.90%) | -0.80 (8.08%) |
| Above 3 | -0.44 (1.12%) | -2.01 (1.20%) |
| Buy and hold | 0.50 | 0.50 |

Figure 9.11, SPX by earnings-calendar regime (recovered from PDF p. 223). Supports "do not avoid blackout periods":

| | Earnings weeks | Blackout | Post earnings | Buy and hold |
|---|---|---|---|---|
| Return | 1.99% | 2.84% | 2.96% | 7.79% |
| Volatility | 9.67% | 9.94% | 13.64% | 19.45% |
| Max DD | -22.59% | -46.73% | -38.49% | -60.75% |
| Active IR | 0.41 | 0.56 | 0.32 | 0.40 |
| % on | 25.37% | 26.29% | 46.64% | 100.00% |

Figure 9.12, Halloween rule from 1990 (recovered from PDF p. 224):

| | Hold Nov-Apr ("sell in May") | Hold May-Oct ("buy in May") | Buy and hold |
|---|---|---|---|
| Return | 6.34% | 2.30% | 8.64% |
| Volatility | 12.86% | 12.63% | 18.02% |
| Max DD | -37.85% | -52.51% | -60.75% |
| Active IR | 0.71 | 0.26 | 0.48 |
| % on | 48.59% | 49.45% | 100.00% |

Figure 9.19, SPX by news regime (recovered from PDF p. 230). Supports the good news / bad news rule:

| | Unconditional | CESI < 0 | CESI > 0 | CESI < 0, corr < 0 | CESI < 0, corr > 0 | CESI > 0, corr < 0 | CESI > 0, corr > 0 |
|---|---|---|---|---|---|---|---|
| Return | 10.18% | 4.21% | 5.97% | 2.48% | 1.73% | 0.67% | 5.30% |
| Risk/reward | 0.54 | 0.31 | 0.45 | 0.29 | 0.17 | 0.09 | 0.48 |
| Max DD | -56.59% | -39.15% | -35.79% | -31.90% | -30.30% | -24.42% | -34.05% |
| Active IR | 0.55 | 0.47 | 0.61 | 0.72 | 0.32 | 0.20 | 0.84 |

## Worked Example
*Why the conditional year-end rule works, as the authors test it.*
1. Rule: long SPX in November and December when January to October is up more than 8%.
2. Hypothesis one, institutions chase returns into year-end. Tested with investor surveys. No relationship between January to October returns and increased allocations. Rejected.
3. Hypothesis two, retail chases. Ten years of data show stronger mutual fund and ETF inflows in November and December in up years. Some support.
4. Hypothesis three, tax-loss harvesting. The momentum factor (12-2, Ken French data) is strongest in December and reverses in January. Losers get sold to crystallize losses and bounce in the new year. In strong years there are fewer losers to sell, so less selling pressure in December. Supported.
5. Check: the December momentum effect has faded since 2005, yet the conditional rule kept working out of sample.

## Key Takeaways
1. Cut risk when POLLS holds above 18. Do not wait for the first 5%.
2. Buy when the VRP spikes above 2 standard deviations. It is the authors' favourite dip model.
3. After a VIX spike above 50, add on the break below 35.
4. Fade extreme leveraged-fund positioning in either direction.
5. Hold November to April. Be long year-end when the year is already up more than 8%.
6. Know the news regime before a data release.
7. Ignore buybacks as a timing input.

## Connects To
- **Ch 3**: financial accident trigger, where the VRP model times the dip.
- **Ch 4**: VRP triggers into elections.
- **Ch 6**: FOMC-day momentum in rates, which does follow through.
- **Ch 8**: strategic framework, 200dma, ERI.
- **Ch 15**: CTA positioning and allocation.

## Extraction Notes
- The AAII figure caption says "falling below 20". The text says -20.
- A garbled sigma ("2 /u1D70E") is read as 2 standard deviations.
- The prose rounds the asset-manager figure to 0.9 and says leveraged funds are "more than 1.3". The chart gives 0.92 and 1.37. The -1 to 1 and 1 to 2 buckets overlap in their "% on" figures as printed.
- The volatility row of Figure 9.19 is misaligned in the PDF text layer and is left out.
- The caption of Figure 9.18 is garbled in the source.
- Sample periods for POLLS, VRP and CFTC tests are not fully stated (CFTC disaggregated data starts 2008).
- Figures 9.1 to 9.21 are charts.
- PDF p. 218 (Figure 9.7, AAII) was opened and carries no statistics table.
- Charts with statistics tables still unread in the PDF: Figure 9.1 POLLS (p. 212), Figure 9.5 VRP vs VIX (p. 216). Their IRs are in the prose.
