# Chapter 5: How to Trade Rates: A Framework

## Core Idea
Rates follow the monetary policy cycle, and the whole curve trades with Fed funds to varying degrees. Position by the stage of the Fed cycle: pay about three months before the first hike, stay paid to the last hike, start receiving at the last hike, press three months before the first cut, exit at the last cut.

## Frameworks Introduced
- **Fed cycle clock** (two-year rates, cycles after 1986):

| Stage | Position | Evidence stated |
|---|---|---|
| Last cut to 3 months before first hike | Range trade. Tactical pay just before the first meeting the Fed sits out | Yields start rising about a month after the last cut |
| About 75 to 55 trading days before first hike | Pay | Two-year returns turn poor in this window. The text also says payers should be entered "around 2.5 months before the first hike" |
| First hike to last hike | Stay paid. Do not trade pauses or step-downs | Returns sideways around pauses. After the 2022 and 2023 step-downs two-year yields made new highs |
| Around last hike | Start receiving the front end | Two-year excess returns trough around the last hike. 10th percentile troughs about 30 trading days before |
| 3 months before first cut | Press the receiver | Countertrend sell-offs small in this window. Largest was 21bp in 2001 |
| First cut to last cut | Stay received in a hard landing. Take profit shortly after the first cut in a soft landing | The Fed has typically out-cut what was priced. 2024 was the exception |
| Last cut | Exit | Bond returns strongly positive into the last cut, then sideways |

- **Regime returns** (UST index excess over T-bills): average monthly returns are negative only in active hiking cycles. They are positive in easing, positive on hold after cuts, and positive on hold after hikes for post-1986 cycles. In the 1970s high-inflation cycles the hold after hikes was not positive. "The end of a hiking cycle is a dangerous time for receivers if inflation is high, but not otherwise."
- **Cycle labelling algorithm** (pre-1986): a hiking (easing) month has a policy rate above (below) the previous two months, and the rate in the following quarter is higher (lower). The look-ahead excludes fine-tuning. Because it uses future data the authors use the long sample for description only and base rules on post-1986 data.
- **Pay into the last cut**: at the final cut or a pause of six months or more, the market already priced hikes one year out in 7 of 11 cases (median 50bp, rising to 66bp six months later). "If we expect the Fed to be on hold for at least six months, we should pay into the last cut." Caveat: the median gap from last cut to first hike is long, so hikes priced one year out are on average exaggerated. Medium-term payers should start only when a hike is expected within three months.
- **One-year swap vs floating rule** (from the authors' EM work): start receiving when the one-year swap breaks below the floating leg, meaning the market starts pricing cuts one year out. Carry at entry is about zero in theory. Cut the receiver if the one-year trades back above the fix. Results improve significantly with that exit. Misfire: the 2023 US banking crisis.
- **FF6 minus FF1 rule**: when six-month Fed funds futures invert against one-month by more than 12.5bp (half a chance of a cut), cuts followed or at least no hikes occurred in the next six months. Exception: March 2023 (Table 5.6).
- **Which inversion to trade** (receive 10-year on inversion, Tables 5.7 and 5.8): the best signals have a short leg of three or six months. Six months works faster. 6m/2s is best on 1m and 3m returns and on cut-prediction hit ratios (58% at 6m, 74% at 12m). When the short leg is 5 or 10 years returns tend to be negative. The widely quoted 2s/10s scores poorly.
- **SPX as cut predictor**: SPX deviation from its 200dma on the day before the first cut predicts the number of cuts in the next 12 months (ignoring 1987). Strong SPX means few cuts (1995). Weak SPX means aggressive cuts (2001). "Whenever the market is pricing a hard landing type of easing cycle, but the SPX is strong, investors should be cautious." Sample extremely small.
- **Curve rules (2s/10s)**:
  - The back end trades with the front end with beta below 1. 10-year vs the fifth SOFR contract, March 2022 to March 2025: R² just below 91%, daily beta 0.9.
  - Hiking cycles bear flatten. Easing cycles bull steepen. DV01-neutral flatteners are profitable from about 50 trading days before the first hike (data from 2000).
  - Steepeners into the first cut are messier. In the median case the trend starts well after the easing cycle begins. In forward space the steepening comes earlier.
  - Without leverage: 30-year bonds are the best instrument in easing cycles for the same cash, because DV01 more than compensates for the steepening. "Cash rules during hiking cycles."
  - Bull steepening and bear flattening explain only 64% of moves (two-year moves above 2bp, two-year above 1%). The other 36% are bull flatteners or bear steepeners.
- **Supply rule**: supply explains swap spreads much better than curve shape. Supply fears "seem to matter mostly when the curve is inverted and the Fed is not close to cutting interest rates."
- **Valuation (Ilmanen, 1997, style)**: curve slope, real rate level (yields minus lagged CPI) and SPX deviation from its 200dma forecast next-month bond returns. The t-statistics are consistently positive for slope and real rates. The IR is only slightly above buy-and-hold (0.46 vs 0.40) because volatility rises with returns. "Use sparingly."
- **Trend following in bonds** (US 7-10 year): 22dma and 55dma raise the active IR by 0.13 and 0.26. The 252dma only breaks even with buy-and-hold (active IR 0.47 vs 0.42). The chart also shows a 200d version at 0.58, which the prose does not mention. Reason given: higher stock prices are self-reinforcing, higher rates are self-limiting.
- **TIPS and breakeven rules**:
  - TIPS are duration products. Real rates usually peak exactly when nominal rates peak. Switching to TIPS does not fully protect in an inflation spike (2022).
  - For inflation protection trade breakevens. Breakevens fall sharply into deep recessions and bounce when markets sense the end. They rise well before the first hike and into the early hiking cycle, then fall when the Fed hikes in earnest. They widen in easing cycles into a soft landing (2024).
  - Illiquidity of linkers helps the breakeven short in hard landings: real rates spike while nominals rally.
  - Trading rule: long TIPS index vs nominal index has IR 0.23 (since 1998). Overweight TIPS only when oil is above its 55dma (lagged one day): IR 0.63. Same rule with copper: IR 0.81.
- **Rates volatility and the cycle**: rate volatility spikes around the first cut, the last cut, the first hike and accelerations. It is typically well-behaved in the final part of the hiking cycle and the pause before the first cut. Useful for EM carry.
- **Oil and yields**: rising oil first means higher yields. Rates rarely look through an oil rally, though they can peak slightly ahead of oil. A major spike ends with a growth hit that reverses much of the move.
- **Cyclicals vs defensives**: by the time US 10-year yields peak, cyclicals vs defensives are down almost 5% over the prior two months on average. Use only when a cycle peak is plausible. It did not protect in 2022.

## Key Concepts
- **Payer / receiver**: paying or receiving the fixed rate in a swap. Short or long duration.
- **Bear flattening / bull steepening**: the normal curve moves in hiking and easing cycles, led by the front end.
- **Bear steepening**: back-end yields rise more. Linked to a Fed seen as behind the curve, or to fiscal fears.
- **Fair value for the 10-year real yield**: the pre-GFC view put it near long-term potential GDP growth. The authors say post-COVID rates are back in line with it.
- **Breakeven**: nominal yield minus real yield.
- **Swap spread**: the instrument the authors prefer for expressing supply.
- **Taylor rule**: the authors found no specification that gives high out-of-sample Sharpe ratios. They rely on Fed speeches and data instead.
- **Term premium**: in practice changes in term premium estimates are very similar to changes in the slope.

## Mental Models
- Think of 10s and 30s as trading like 2s. The 10-year usually peaks around the last hike, at or above Fed funds.
- Think of easing cycles as short and sharp and hiking cycles as long and slow. Markets move faster than inflation, and "everyone likes a dove".
- Markets underprice both hiking and easing cycles once they are under way. But the market often prices hikes that never come.
- Use real-yield cushion as the long-term test for duration: 10-year ex post real returns depend strongly on the real yield at purchase.

## Anti-patterns
- **Trading Fed pauses or step-downs inside a hiking cycle**: not shown to add alpha. "It may be best to remain paid."
- **Receiving at the last hike when inflation is high**: failed in 2023. The 10-year peaked in October 2023, three months after the last hike.
- **Using 2s/10s inversion as the receive signal**: negative 10-year returns and 33% to 40% hit ratios.
- **Holding receivers to the last cut when the terminal rate is already priced**: the 2024 lesson, especially with a plausible soft landing.
- **Expressing supply views through the curve**: weak historical relationship.
- **Long-window trend following in bonds**: the 252dma adds nothing.
- **Hiding in TIPS during a hiking cycle**: still loses money except at the very short end.

## Reference Tables
Long-run UST returns (index from 1973):

| Measure | Value |
|---|---|
| Average annualized return | 6.3% (6.1% geometric) |
| Information ratio (nominal) | 1.1 |
| Drawdowns over 5% | 8 |
| Ex post real return, IR | 3%, 0.54 |
| Excess over T-bills, IR | 1.66% (1.46% geometric), 0.3 |
| Years with UST and SPX both down (nominal) | 1994, 2022 |

Table 5.1, UST drawdowns in excess of 3m T-bills:

| Peak | Trough | Drawdown | Days to trough | FF change to high | CPI peak |
|---|---|---|---|---|---|
| 1973-02-02 | 1974-09-27 | -7.4% | 602 | 3.0% | 12.2% |
| 1977-01-03 | 1981-09-30 | -25.5% | 1731 | 8.8% | 14.6% |
| 1986-09-01 | 1987-10-29 | -9.1% | 423 | 3.9% | 5.3% |
| 1993-11-01 | 1994-11-21 | -9.0% | 385 | 3.0% | 3.1% |
| 1998-10-06 | 2000-01-12 | -10.2% | 463 | 1.2% | 3.8% |
| 2008-12-19 | 2009-06-10 | -7.3% | 173 | 0.0% | 2.8% |
| 2016-07-11 | 2018-11-08 | -7.4% | 850 | 2.0% | 2.9% |
| 2020-08-05 | 2023-10-19 | -23.1% | 1170 | 5.2% | 9.0% |
| Median | | -9.0% | 532 | 3.0% | 4.5% |

Cycle statistics after 1986 (Tables 5.3 and 5.4):

| | Hiking cycles | Easing cycles |
|---|---|---|
| Median length | 12 months | 8 months |
| Median number of moves | 8 | 4 |
| Median average move | 0.29% | -0.37% |
| Median total | 2.62% | -2.25% |
| Median pause afterwards | 8 months (to first cut) | 14 months (to first hike) |

Table 5.6, dates when FF6 minus FF1 priced more than 12.5bp of easing:

| Date | FF6-FF1 (bp) | Actual 3m FF change | Actual 6m FF change |
|---|---|---|---|
| 05-24-1995 | -19 | -25 | -25 |
| 02-13-1998 | -13 | 0 | 0 |
| 08-20-1998 | -13 | -75 | -75 |
| 09-19-2000 | -15 | 0 | -100 |
| 10-04-2006 | -15 | 0 | 0 |
| 02-27-2007 | -17 | 0 | 0 |
| 07-26-2007 | -19 | -50 | -100 |
| 05-13-2019 | -16 | -25 | -75 |
| 03-13-2023 | -34 | 50 | 75 |
| 11-29-2023 | -13 | 0 | 0 |
| 05-01-2024 | -16 | 0 | -50 |

Tables 5.7 and 5.8, receiving 10-year after each inversion (inversion of at least 12.5bp for the cut hit ratios):

| Curve | 1m ret | 3m ret | 6m ret | 3m hit | Cut within 6m | Cut within 12m | Avg months to cut | Max months to cut |
|---|---|---|---|---|---|---|---|---|
| 3m10s | 0.26% | 1.11% | 1.03% | 58% | 39.1% | 52.2% | 10.3 | 23.4 |
| 6m10s | -0.16% | 0.34% | 0.24% | 47% | 39.1% | 56.5% | 11.0 | 26.6 |
| 6m2s | 0.78% | 1.71% | 0.48% | 70% | 57.9% | 73.7% | 12.0 | 54.1 |
| 6m5s | 0.45% | 0.76% | 1.66% | 65% | 45.8% | 66.7% | 8.7 | 26.3 |
| 2s5s | 0.23% | 0.14% | 0.55% | 56% | 53.3% | 73.3% | 7.7 | 26.9 |
| 2s10s | -0.79% | -1.74% | -2.15% | 33% | 50.0% | 57.1% | 11.4 | 30.1 |
| 2s30s | -0.53% | -1.63% | -1.09% | 38% | 41.7% | 66.7% | 9.4 | 26.6 |
| 5s10s | -1.16% | -1.21% | -0.01% | 43% | 40.0% | 63.3% | 10.8 | 32.4 |
| 5s30s | -1.43% | -1.27% | -1.49% | 39% | 35.3% | 58.8% | 11.7 | 30.1 |
| 10s30s | -1.19% | -1.58% | -0.38% | 32% | 55.6% | 72.2% | 8.4 | 24.3 |

Table 5.9, curve-segment correlations (daily, 1965 to 2024): 2s10s with 2s5s 0.82, with 2s30s 0.88, with 5s10s 0.63, with 5s30s 0.47, with 1s2s -0.01, with 10s30s 0.09.

Late-cycle bear steepening of 2s/10s: 2006 36bp, 2007 28bp, 2023 93bp. The 2006 and 2023 moves stopped when the Fed turned dovish. Weaker equities ended the 2007 move.

Table 5.5, what the market priced at the final cut or at a pause of six months or more (recovered from PDF p. 105). Supports the rule "pay into the last cut". ED5-ED1 is the hikes (+) or cuts (-) priced one year out, in bp:

| Date | Type | Fed funds | ED5-ED1 (or FF) | Six months later | Change |
|---|---|---|---|---|---|
| 1988-02-10 | Final cut | 6.50% | 99 | 66 | -33 |
| 1989-12-19 | Pause | 8.25% | 17 | 42 | 25 |
| 1992-09-04 | Final cut | 3.00% | 79 | 99 | 20 |
| 1996-01-31 | Final cut | 5.25% | -42 | 55 | 97 |
| 1998-11-17 | Final cut | 4.75% | -20 | 72 | 91 |
| 2001-12-11 | Pause | 1.75% | 188 | 187 | -1 |
| 2002-11-06 | Pause | 1.25% | 95 | 39 | -55 |
| 2003-06-25 | Final cut | 1.00% | 59 | 130 | 71 |
| 2008-12-16 | Final cut | 0.25% | 50 | 94 | 44 |
| 2020-03-16 | Final cut | 0.25% | -53 | -6 | 47 |
| 2024-12-18 | Pause | 4.50% | -47 | -84 | -37 |
| Mean | | 3.34% | 39 | 63 | 24 |
| Median | | 3.00% | 50 | 66 | 25 |

Figure 5.26b, valuation model on bonds (recovered from PDF p. 126). Supports "use valuation sparingly":

| | Regression forecast | Long/short | Buy and hold |
|---|---|---|---|
| Return | 3.07% | 1.23% | 2.51% |
| Volatility | 6.75% | 3.45% | 6.31% |
| Max DD | -19.33% | -9.25% | -27.48% |
| Active IR | 0.46 | 0.70 | 0.40 |
| % on | 100.00% | 26.15% | 100.00% |

Figure 5.27, trend following on the US 7-10 year bond (recovered from PDF p. 127). Supports "trend following only in the short term":

| | 22d | 55d | 200d | 252d | Buy and hold |
|---|---|---|---|---|---|
| Return | 1.82% | 2.41% | 2.21% | 1.84% | 2.59% |
| Volatility | 4.56% | 4.68% | 4.84% | 4.91% | 6.29% |
| Risk/reward | 0.41 | 0.52 | 0.46 | 0.37 | 0.41 |
| Max DD | -16.53% | -13.35% | -19.05% | -19.19% | -27.48% |
| Active IR | 0.55 | 0.68 | 0.58 | 0.47 | 0.42 |
| % on | 55.15% | 57.46% | 61.41% | 62.14% | 100.00% |

## Worked Example
*The 2022 to 2024 cycle against the rules.*
1. Payers began to work in December 2021, about three months before the first hike in March 2022. Rule held.
2. The 10-year range-traded in late 2022 as the Fed stepped down to 50bp and then 25bp. A later sell-off took it to the cycle high in October 2023, three months after the last hike in July 2023. Rule broke: normally the 10-year peaks near the last hike.
3. The 10-year peaked well below Fed funds. The market priced cuts much earlier than usual and never sold off as much as in earlier cycles.
4. Rates rallied hard in the last three months before the first cut in September 2024. Rule held.
5. Because the earlier sell-off had been small, that rally left the cuts priced one year forward at the most aggressive level on record on the day of the first cut. After the initial 50bp cut rates sold off aggressively as the soft-landing narrative met that pricing.
6. Supply sub-plot: on July 31, 2023 the Treasury raised its quarterly borrowing estimate by 280bn USD. 2s/10s bear steepened 93bp. The fears faded after the November 1, 2023 refunding announcement, which coincided with a dovish turn by Powell.
7. The Fed kept hiking for a year after inflation peaked in June 2022. The authors' reasons: the hiking cycle started very late, and with extremely high inflation hikes can coincide with falling inflation.

Authors' conclusions: paying three to six months before the first hike still works. Receiving three months before the first cut still works. Receiving at the last hike failed. Be tactical about how much is priced once the easing cycle starts. More macro capital chasing front-end trades may mean less risk premium is left in the forwards.

## Key Takeaways
1. Trade the Fed cycle, not the business cycle, when trading rates.
2. Receivers need to go on earlier (last hike) than payers (about three months before the first hike).
3. In a soft landing take profit on receivers shortly after the first cut.
4. Check the SPX against its 200dma before trusting hard-landing pricing.
5. Use short-leg inversions (3m or 6m) as receive signals, and condition on inflation.
6. Use short moving averages (22d, 55d) for bond trend. Give valuation little weight.
7. Trade breakevens with oil or copper trend for inflation views. Trade TIPS as duration.

## Connects To
- **Ch 3**: inversion as an easing-cycle forecast and the inflation conditioning.
- **Ch 6**: tactical rules for rate sell-offs, FOMC and payroll days, and the cyclicals vs defensives study (Figure 6.6).
- **Ch 7**: how far other rates markets can diverge from the Fed.
- **Ch 15**: Treasuries in a portfolio, bond vs equity correlation.

## Extraction Notes
- The "## CHAPTER 5" heading did not extract as a heading. The chapter starts at the title line "How to Trade Rates: A Framework" after a bare "CHAPTER 5" line.
- Table 5.5 was checked against PDF p. 105 and every cell matches. The printed page itself sets the 1988 row one column to the left of the others ("Final Cut" sits beside the date). The table in Reference Tables puts that row back under the right headers.
- The text says "all three episodes" still pricing cuts were final cuts. The table shows four negative readings (1996, 1998, 2020, 2024). The text treats 2024 separately as the exception among the pauses.
- The text cites "Figure 5.12" for the inversion return study. The data are in Table 5.7.
- Table 5.2 dates the 1986 drawdown trough at 09-30-1987 and recovery at 08-29-1991. Table 5.1 gives 10-29-1987 and 07-28-1989. The two tables disagree in the source.
- Figures 5.1 to 5.33 are charts. Regime returns (Figure 5.3) and the SPX vs cuts scatter (Figure 5.15) are not available as numbers.
- Charts with statistics tables still unread in the PDF: Figure 5.12 (p. 111), Figure 5.28 TIPS vs nominals (p. 128), Figure 5.32 TIPS with oil and copper (p. 131). Their headline IRs are in the prose.
