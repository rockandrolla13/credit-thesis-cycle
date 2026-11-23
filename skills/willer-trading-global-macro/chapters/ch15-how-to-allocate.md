# Chapter 15: How to Allocate

## Core Idea
Asset returns depend on the macro regime, and the 60/40 and risk parity portfolios both have a blind spot in stagflation. Build portfolios that hold up across regimes by adding trend following, carry, quality and real assets, time the equity-bond switch with momentum, not valuation, and scale risk down when volatility rises.

## Frameworks Introduced
- **Limits of the four-quadrant model**: growth and inflation levels give four states. Near trend, the classification can turn on "a rounding error". It ignores transitions and other dimensions. Hidden Markov models are the statistical alternative, but lose intuition and struggle out of sample.
- **Early vs late recession split**: split the low-growth, low-inflation quadrant by whether growth indicators are above or below their 3-month average.
  - Early recession (growth below average and weakening): classic risk-off. Bonds have their strongest returns. The worst regime for risky assets overall.
  - Late recession (recovery): the best regime for equities and credit. Riskier markets like EM do better than developed ones.
  - Stagflation: for US equities even worse than early recession.
  - Overheating: commodities do best. EM tends to outperform.
  - Goldilocks: equities do best. International equities beat the US as the dollar tends to weaken.
- **"Playbook for the future" (nearest-neighbour regimes)** (Saunders and Willer, 2021): describe the environment with seven variables: levels of growth, inflation, financial conditions and risk appetite (implied or realized volatility), plus changes in growth, inflation and financial conditions. Find the historical periods closest to today with a nearest-neighbour algorithm. Read forward returns from those periods.
  - Example reading for September 2025 (60 months of data picked): inflation below its 10-year average after a surge, growth near trend, loose financial conditions, low volatility. Nearest analogues: 1976 to 1977, the mid-1980s, 2010 to 2012. Generally positive for equities.
- **Ten macro clusters** (Saunders et al., 2024a): k-means clustering on the cross-correlations of the macro variables gives 10 clusters with an 80/20 rule. 80% of observations fall in common clusters. 20% are risk or unusual clusters used for stress tests.
  - Named clusters visible in the source: Normal, Goldilocks, Growth shock (maps to early recession), Recovery (maps to late recession), Tightening financial conditions, Stagflation (loose), Stagflation, Inflationary boom, Recession, Financial market shock/crisis.
  - Tightening financial conditions (inflation above average, growth near trend) is the most difficult common cluster: stocks, bonds and credit can all sell off. It can lead to stagflation, as in 2022-2023.
  - Two flavours of stagflation: one where inflation is expected to be transitory, and one where financial conditions must tighten and inflation hedges do not work.
  - Recession cluster: "one of the best times to invest". Leadership changes and momentum strategies reverse violently (financials in March 2009, travel in April 2020).
- **Stock-bond correlation rule**: for US core CPI below 2.5% the equity-bond correlation is predominantly negative. Above 2.5% it is mostly positive. Risk parity needs a negative correlation and cheap leverage.
- **Inflation hedges under a hiking Fed** (Table 15.1): gold, Bitcoin, TIPS and equities worked from January 2021 to March 2022 while the Fed delayed. Once the Fed hiked they stopped working. The USD was the only public asset that worked in both phases. Caveat: the 2022 shock was US-centric.
- **Stagflation hedges among strategies**: trend following and momentum (FX and equities) work. Carry works, especially in fixed income, but FX carry is not profitable in high stagflation. Value works in fixed income and FX, not in equities. Quality works within equities. "CTAs and macro hedge funds are therefore likely the best inflation and stagflation hedges", because inflation-driven bear markets are slow and long.
- **Sources of future inflation shocks**: energy transition costs ("greenflation"), structurally higher defence spending, and socialized risk with already high government debt. Deflationary forces: plain recessions and AI. Conclusion: move a significant part of the bond allocation into inflation hedges.
- **Regime-agnostic strategic allocation** (Saunders et al., 2022): 50% equities (property or other real assets can be included here), 30% bonds, 10% CTAs, 5% quality, 5% carry. Positive in all regimes, barely so in stagflation. Simulated IR 0.68 vs 0.55 for 60/40. Return 5.34% vs 5.28%, with volatility 7.83% vs 9.67% and max drawdown -25.80% vs -32.47%.
- **Equity vs credit allocation**:
  - Ex post optimal Sharpe portfolio on rolling 10 years: credit was at times 100% in the 1970s. Since 2008 it averages 12% and is now near zero.
  - Predictors of volatility-adjusted credit vs equity: a high VIX and recent equity outperformance favour equities. High spreads favour credit. Spread changes are subsumed by equity moves. Inflation favours credit but is not significant.
  - Real-time version: ridge regression, expanding window, positions in proportion to the forecast percentile. Relative performance range-trades except in credit events, when credit underperforms. With CDX the Sharpe is "likely too low to trade".
- **Earnings yield gap (EYG)**: E/P (earnings lagged three months) minus the 10-year yield, as a rolling three-year z-score, one-year hold. It mean-reverts but fails as a timing tool. Use it as "a risk gauge, not a trading signal".
- **200dma equity-bond switch**: if equities are above their 200dma, hold equities. If not and bonds are above their 200dma, hold bonds scaled to equity risk. If neither, hold T-bills. IR 0.59 vs SPX 0.46 and 60/40 0.53. Max drawdown -28.39% vs -60.75% for the SPX.
- **Structural case against government bonds**: debt market capitalization jumps in each crisis while equity net issuance is negative. Cap-weighted bond indexes overweight the biggest borrowers. Equity indexes add winners.
- **Volatility targeting**:
  - Sort months by realized volatility over the last 22 sessions into quintiles. Volatility persists. Equity returns do not rise enough to compensate, so IRs fall as volatility rises. "It pays to reduce positions when volatility strikes."
  - Bonds: the highest volatility quintile has well below par returns. The second most volatile quintile has the highest IR. Data from 1988.
  - Targeting long-run volatility month by month helps in equities (most in the US, also Germany, not Japan) and fixed income. It detracts in credit spread returns and commodity futures.
  - Side effect: when equity volatility falls from high levels there is a persistent bid as investors re-lever.
- **CTA positioning model**: use the 22-, 66-, 200- and 252-day moving averages. Each one crossed adds one unit, from -4 (max short) to +4 (max long). This approximates CTA index P&L better than regressions on futures.
  - Finding: trend following works. Commodities: max short bucket very negative, max long positive. FX and bonds: lowest returns in max short. Equities: no clear pattern. CTA positioning has "extremely limited" value as a counter-indicator.
- **CFTC positioning by asset class** (z-score of 2 or above is max long, 0.5 to 2 long, below -0.5 short, below -2 max short, month-end): fading extremes works for equities. Bonds and commodities show follow-through. FX is neither.

## Key Concepts
- **Risk parity**: allocating equal risk, with leverage on bonds.
- **Minsky**: stability breeds instability, because lower perceived risk invites leverage.
- **Regime-agnostic portfolio**: one that performs acceptably in every regime.
- **Earnings yield gap**: equity earnings yield minus the bond yield.
- **Volatility targeting**: scaling exposure inversely to recent realized volatility.
- **CTA**: commodity trading advisor, mostly trend following on futures. About 360 billion under management as of mid-2024 (BarclayHedge).
- **Quality factor**: equity style that performs well in stagflation.
- **Greenflation**: inflation from the energy transition.
- **k-means / nearest neighbour**: the two statistical tools used for regimes.

## Mental Models
- Ask "which past periods look like today?" before forecasting returns.
- Think of bonds as deflation hedges. If inflation shocks are more likely, the 40% needs inflation hedges too.
- Think of valuation as a warning flag at expensive extremes. Bullish value signals tend to arrive during earnings deterioration.
- Go with CTAs, not against them.
- The trend rule is the fallback, and the bottom-buying rules of Ch 9 are the way to re-enter before the 200dma.

## Anti-patterns
- **Treating 60/40 or risk parity as all-weather**: both ignored the 1970s.
- **Buying gold, TIPS or Bitcoin as inflation hedges once the Fed is hiking**: they fell in 2022.
- **Timing equities vs bonds on the earnings yield gap**: IR similar to or below buy-and-hold. Cheap signals came too early in 2000 and 2007.
- **Fading CTA positioning**: trend works.
- **Volatility targeting credit spread returns or commodity futures**: detracts value.
- **Holding cap-weighted government bond indexes without thought**: they overweight the weakest credits.
- **Relying on FX carry in high stagflation**: not profitable there.

## Reference Tables
Table 15.1, inflation hedges around the 2022 hiking cycle (cumulative returns, checked against PDF p. 357):

| Date | CPI | Fed funds | Gold | Bitcoin | TIPS | DXY | CTA | SPX |
|---|---|---|---|---|---|---|---|---|
| Jan-21 | 1.3 | 0.25 | | | | | | |
| Mar-22 | 7.9 | 0.50 | 3.7% | 36.4% | 2.7% | 8.0% | 6.9% | 25.9% |
| Jul-22 | 8.4 | 2.50 | -6.0% | -31.0% | 0.1% | 16.9% | 13.3% | 13.4% |

Figure 15.6 data, risk parity vs 60/40 (recovered from PDF p. 357):

| | Risk parity | 60/40 |
|---|---|---|
| Return | 6.21% | 5.15% |
| Volatility | 10.53% | 10.51% |
| Risk/reward | 0.59 | 0.49 |
| Max DD | -31.38% | -34.73% |

Figure 15.13 data, equities vs bonds on the earnings yield gap z-score:

| | z below -2 | z above 2 | Buy and hold |
|---|---|---|---|
| Return | -0.03% | 1.47% | 5.45% |
| Volatility | 9.01% | 12.48% | 19.50% |
| Max DD | -60.71% | -72.19% | -75.11% |
| Active IR | -0.01 | 0.24 | 0.28 |
| % on | 20.60% | 23.18% | 100.00% |

Allocation rule scorecard:

| Portfolio or rule | IR |
|---|---|
| SPX | 0.46 |
| 60/40 | 0.53 (0.55 in the SAA comparison) |
| 200dma equity-bond-bills switch | 0.59 |
| Regime-agnostic 50/30/10/5/5 | 0.68 |

Best asset by regime (text of section 15.1):

| Regime | Best | Worst |
|---|---|---|
| Early recession | Bonds | Risky assets |
| Late recession | Equities, credit, EM | Bonds fade |
| Stagflation | Trend, carry, quality, USD in 2022 | US equities, most public assets |
| Overheating | Commodities, EM | not stated |
| Goldilocks | Equities, international over US | not stated |

Figure 15.9, regime-agnostic ("regime stable") portfolio (recovered from PDF p. 361). Supports the 50/30/10/5/5 allocation:

| | S&P 500 | US Treasury | 60/40 | Regime stable |
|---|---|---|---|---|
| Return | 7.55% | 1.87% | 5.28% | 5.34% |
| Volatility | 15.41% | 5.11% | 9.67% | 7.83% |
| Risk/reward | 0.49 | 0.37 | 0.55 | 0.68 |
| Max DD | -56.50% | -24.11% | -32.47% | -25.80% |

Figure 15.14, equity-bond-cash switch on the 200d MA (recovered from PDF p. 365). Supports the 200dma switch:

| | Eq / Bond / Cash 200d MA | S&P 500 | US 7-10 year bond | 60/40 |
|---|---|---|---|---|
| Return | 6.79% | 8.04% | 2.25% | 5.72% |
| Volatility | 11.53% | 17.55% | 7.47% | 10.77% |
| Risk/reward | 0.59 | 0.46 | 0.30 | 0.53 |
| Max DD | -28.39% | -60.75% | -37.49% | -33.54% |

## Worked Example
*Which inflation hedges survived 2022.*
1. January 2021: CPI 1.3%, Fed funds 0.25%.
2. January 2021 to March 2022, inflation rising and the Fed waiting: gold +3.7%, Bitcoin +36.4%, TIPS +2.7%, DXY +8.0%, CTAs +6.9%, SPX +25.9%. Every hedge worked.
3. March 2022: CPI 7.9%, first hike.
4. By July 2022 (CPI 8.4%, Fed funds 2.50%) the cumulative figures were gold -6.0%, Bitcoin -31.0%, TIPS +0.1%, SPX +13.4%. DXY rose to +16.9% and CTAs to +13.3%.
5. Reading: once the central bank addresses inflation, assets that depend on easy money fail. Only the USD and trend followers kept working.
6. Allocation consequence: hold CTAs and macro strategies as the stagflation sleeve. Treat the USD as a hedge that depended on a US-centric shock.

## Key Takeaways
1. Identify the regime with more than growth and inflation levels: add financial conditions, volatility and the changes.
2. Split recessions into early (own bonds) and late (own equities and credit).
3. Expect a positive stock-bond correlation with core CPI above 2.5%.
4. Add about 10% CTAs and 5% each of quality and carry to a 50/30 equity-bond core.
5. Switch between equities, bonds and bills on the 200dma.
6. Cut size when realized volatility rises in equities and bonds.
7. Fade CFTC extremes only in equities.

## Connects To
- **Ch 3**: the five-regime cycle.
- **Ch 5**: Treasuries, TIPS and breakevens.
- **Ch 8, Ch 9**: valuation vs momentum, CFTC positioning, VIX.
- **Ch 11**: credit vs equities and the credit canary.
- **Ch 12**: carry and the volatility cut-out.
- **Ch 16**: Bitcoin and private assets in the allocation.

## Extraction Notes
- Table 15.1's header reads "Returns since Jan 2001" in the source and on the PDF page. The rows start in Jan-21, so 2021 is almost certainly meant.
- The text says gold, Bitcoin "and SPX all had meaningfully negative returns" between March and June 2022, then says "Equities did well between the start of Fed hikes and peak inflation". Both are in the source. The table shows the SPX cumulative return falling from 25.9% to 13.4%.
- The text says TIPS had negative returns in the hiking phase. The table shows cumulative TIPS at 2.7% then 0.1%.
- A sentence on the regime-agnostic IR is garbled: "now 0.68, up from (also fixes 0.61 to 0.68). 0.55 for the 60/40 portfolio". It is read as 0.68 vs 0.55. Section 15.5 quotes 60/40 at 0.53.
- Regime Sharpe ratios by asset (Figures 15.2 and 15.5), cluster z-scores (15.4), the stock-bond correlation scatter (15.7), factor performance in stagflation (15.8) and the volatility quintile results (15.16 to 15.18) are bar charts with no printed numbers. The ten cluster names above are taken from chart legends on PDF p. 356.
- The text refers to "(see also 9 using a daily signal)". Chapter 9 is meant.
- In Figure 15.14 the column headers are stacked on the page. The pairing above follows the IRs the prose states (switch 0.59, SPX 0.46, 60/40 0.53).
- Charts with statistics tables still unread in the PDF: Figure 15.11 credit vs equity model (p. 363), Figures 15.16 and 15.17 volatility quintiles (pp. 367-368).
