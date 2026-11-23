# Chapter 6: How to Trade Rates: The Tactics

## Core Idea
Peaks in yields pay faster than troughs because rates retrace quickly from peaks. A handful of indicators help time them, and event-day price action (FOMC first, payrolls second) tends to follow through. Data surprises work as a trend signal, not as a contrarian one.

## Frameworks Introduced
- **Anatomy of a 10-year sell-off**: peaks after sell-offs of more than 70bp since 2000 (dates from Plata-Vazquez and Mathai, 2023). Range 70bp to 214bp. Median 120bp over about 135 days.
  - Leading for the peak: two-year breakevens start to fall about a month before the 10-year peak. 5s/30s peaks "meaningfully earlier" than 10s because 30s lag the sell-off. That flattening reverses after the peak.
  - Coincident: 2s/10s, DXY, WTI. In the median case oil rallied more than 20% in the three months into the yield peak, so "a big break in oil would likely also result in a peak in rates."
  - Coincident warnings: real estate vs S&P trades poorly through the sell-off and bottoms on the day of the rates peak. Cyclicals vs defensives peaks with rates (slightly lagging in the median case).
  - Not happening: the SPX does not fall. It trades sideways to moderately higher.
  - Exception: 2023, which was supply-driven.
- **Cyclicals vs defensives rule**: if returns of cyclicals vs defensives are below their 55-day moving average, go long the 10-year future with a one-day lag.
  - Result: active IR 0.85 vs unconditional 0.48. The gain comes mostly from lower volatility when the rule is out of the market.
  - When to use: growth-driven cycles. "We would therefore disregard this ratio during high-inflation scenarios." It protected only very partially in 2022.
- **FOMC momentum rule**: score the meeting by the two-year move on FOMC day. Act when the move is at least 2 standard deviations of trailing one-month data. Receive after a dovish move, pay after a hawkish one.
  - Dovish side: median returns "very positive and persistent". Even the worst 10th percentile is not losing money 20 days later. Follow-through exists during hiking cycles but is smaller. Events while the Fed is on hold go mostly sideways.
  - Hawkish side: also follows through, and more clearly in easing cycles (two data points only: the last cut of 2003 and the March 2008 cut).
- **Nonfarm payroll rules** (10-year bonds in excess of cash, 2 standard deviation moves on NFP day):
  - Bullish days: 45 events in 660 months. Small follow-through over the next days. With 3 standard deviation moves (13 events) median returns exceed 1% over the next 20 sessions. Rallies in easing cycles are meaningfully larger. Treat large NFP-day rallies in hiking cycles carefully. Use them as entry points in easing cycles.
  - Bearish days: 53 events at 2 standard deviations and 25 at 3. Less follow-through. "Even during hiking cycles, bearish NFP prints are not a good signal to pay."
  - First negative NFP after one year of positive prints: 12 instances since 1974. Median Treasury returns are positive after some choppiness. Bottom 25th percentile close to flat, 75th percentile nearly 4%.
- **CESI trend rule** (five-year US swaps): receive when Citi's economic surprise index has fallen below -25. Pay when it has risen above 75.
  - Result: IR rises from 0.26 to 1.01. Active only 25% of the time with similar annualized returns.
  - Symmetric +/-75 gave equivalent results but triggered rarely.
  - CESI extremes as a counter-indicator "did not result in much of a tradable strategy".
- **When safety backfires**: events with VIX above 35 and daily US rate sell-offs of more than 15bp (1998 LTCM, 2008 Lehman, 2020 COVID, a few others). Rates eventually often trade significantly lower, because the Fed acts when market functioning is threatened.
- **Bond seasonals** (10-year rolling seasonals on bond futures for the US, Canada, UK, Japan and European markets):
  - Absolute version: long or short a market when the month's median is above or below the 12-month median. Gross leverage 100%. Adds no value vs equal-weight long-only.
  - Relative value version: overweight markets with the higher seasonal median, fully invested. Adds modest IR improvement.

## Key Concepts
- **CESI**: Citi economic surprise index, a summary of data momentum versus expectations, originally weighted for FX reactions.
- **Scoring an FOMC by price**: use the front-end move, not the statement text.
- **Active information ratio**: IR measured only while the rule holds a position.
- **Two-year breakeven**: front-end inflation compensation. It leads the nominal 10-year peak.
- **Instant gratification**: the authors' phrase for the fast retracement after yield peaks.

## Mental Models
- Use Chapter 5 to decide whether a cycle peak is plausible. Use this chapter to time the entry.
- Think of one or more coincident indicators rolling over during a sharp sell-off as a sign the move is mature.
- Think of payrolls as the labour series that flips first: NFP has turned negative with the unemployment rate still at or near its 12-month low.
- A risk-off bond sell-off in the US is a liquidity or fiscal scare. Expect the Fed to end it.

## Anti-patterns
- **Fading CESI extremes**: not tradable in the authors' test.
- **Paying on a weak-bond payroll day**: little follow-through.
- **Outright seasonal bond trades**: no added value.
- **Using cyclicals vs defensives in an inflation shock**: the rule breaks down.
- **Waiting for the SPX to fall as a sign of a rates peak**: equities do not sell off into rate peaks.

## Reference Tables
Table 6.1, 10-year sell-offs of more than 70bp:

| Start | End | Days | Sell-off (pp) | FF change (pp) |
|---|---|---|---|---|
| 03-23-2001 | 05-15-2001 | 53 | 0.70 | -1.00 |
| 11-07-2001 | 04-01-2002 | 145 | 1.22 | -0.25 |
| 06-13-2003 | 09-02-2003 | 81 | 1.48 | -0.25 |
| 03-16-2004 | 05-13-2004 | 58 | 1.15 | 0.00 |
| 06-01-2005 | 11-04-2005 | 156 | 0.75 | 1.00 |
| 01-17-2006 | 06-28-2006 | 162 | 0.91 | 0.75 |
| 03-02-2007 | 06-12-2007 | 102 | 0.74 | 0.00 |
| 03-17-2008 | 06-16-2008 | 91 | 0.91 | -1.00 |
| 12-30-2008 | 06-10-2009 | 162 | 1.87 | 0.00 |
| 10-07-2010 | 02-08-2011 | 124 | 1.34 | 0.00 |
| 05-02-2013 | 09-05-2013 | 126 | 1.32 | 0.00 |
| 01-30-2015 | 06-26-2015 | 147 | 0.81 | 0.00 |
| 07-08-2016 | 03-13-2017 | 248 | 1.25 | 0.25 |
| 09-07-2017 | 10-05-2018 | 393 | 1.18 | 1.00 |
| 08-04-2020 | 03-31-2021 | 239 | 1.22 | 0.00 |
| 12-03-2021 | 06-14-2022 | 193 | 2.14 | 0.75 |
| 08-01-2022 | 10-24-2022 | 84 | 1.65 | 0.75 |
| 05-03-2023 | 10-04-2023 | 154 | 1.35 | 0.50 |
| 02-01-2024 | 04-25-2024 | 84 | 0.83 | 0.00 |
| 09-16-2024 | 01-13-2025 | 119 | 1.16 | -1.00 |
| Mean | | 146.05 | 1.20 | 0.07 |
| Median | | 135.50 | 1.20 | 0.00 |

Table 6.2, first negative NFP of a cycle vs unemployment:

| Date | NFP (k) | Unemployment rate | Prior 12m low | Gap |
|---|---|---|---|---|
| March-1980 | -140 | 6.3 | 5.6 | 0.7 |
| June-1986 | -89 | 7.2 | 6.7 | 0.5 |
| July-1990 | -219 | 5.5 | 5.2 | 0.3 |
| April-1995 | -9 | 5.8 | 5.4 | 0.4 |
| March-1998 | -36 | 4.7 | 4.6 | 0.1 |
| September-1999 | -8 | 4.2 | 4.2 | 0.0 |
| September-2005 | -35 | 5.0 | 4.9 | 0.1 |
| August-2007 | -4 | 4.6 | 4.4 | 0.2 |
| September-2017 | -33 | 4.3 | 4.3 | 0.0 |
| March-2020 | -701 | 4.4 | 3.5 | 0.9 |

Rule scorecard:

| Rule | Baseline IR | Rule IR | Note |
|---|---|---|---|
| Cyclicals vs defensives below 55dma, long 10-year future | 0.48 | 0.85 (active) | weak in inflation shocks |
| CESI below -25 receive, above 75 pay | 0.26 | 1.01 | on 25% of the time |
| Seasonal RV across bond markets | 0.52 | 0.66 (risk/reward) | absolute version 0.50 |

Figure 6.13, CESI rule on the five-year swap (recovered from PDF p. 146). Supports the CESI trend rule:

| | Receive below -25, pay above 75 | Five-year swap returns |
|---|---|---|
| Return | 1.28% | 1.20% |
| Volatility | 2.40% | 4.57% |
| Max DD | -5.54% | -19.33% |
| Active IR | 1.01 | 0.26 |
| % on | 27.49% | 100.00% |

Figure 6.15, bond seasonals across markets (recovered from PDF p. 148). Supports the seasonal rule:

| | Seasonals absolute | Seasonals RV | Long-only |
|---|---|---|---|
| Return | 1.81% | 3.44% | 2.57% |
| Volatility | 3.65% | 5.17% | 4.90% |
| Risk/reward | 0.50 | 0.66 | 0.52 |
| Max DD | -15.09% | -16.80% | -20.12% |

## Worked Example
*Checking whether a sell-off is mature.* Suppose the 10-year has sold off more than 70bp over several months and the Fed cycle makes a peak plausible. Run the checklist the chapter implies:
1. Have two-year breakevens been falling for about a month?
2. Has 5s/30s stopped steepening and started to flatten?
3. Has oil, which typically rallied more than 20% into such peaks, broken lower?
4. Has real estate vs the S&P stopped underperforming? Are cyclicals vs defensives below their 55dma?
5. Is inflation the driver? If yes, discount step 4.
6. Wait for a trigger day: a two-year rally of 2 standard deviations or more on an FOMC day, or a large payroll-day rally in an easing cycle.
The authors do not combine these into one model. Each item is reported as a separate regularity.

## Key Takeaways
1. Hunt for yield peaks, not troughs.
2. Watch two-year breakevens and 5s/30s for early warning. Oil and DXY only confirm.
3. Take FOMC-day price action seriously in both directions.
4. Trust payroll-day rallies more than payroll-day sell-offs, and more in easing cycles.
5. Trade data surprises with the trend, with asymmetric thresholds (-25 and 75).
6. Buy Treasuries after a VIX-above-35 day with a 15bp sell-off. Such episodes are short.

## Connects To
- **Ch 5**: the strategic Fed-cycle clock these tactics refine.
- **Ch 3**: negative payroll prints and recession timing for equities.
- **Ch 9**: FOMC effect and good-news-is-bad-news regimes in equities.
- **Ch 12, Ch 13**: economic surprises in FX.

## Extraction Notes
- The text says "we find 18 examples" with a median sell-off of 120bp. Table 6.1 lists 20 rows, and its median row shows 1.20. The count is inconsistent in the source.
- A symbol in "3 /u1D70E moves" is a garbled sigma. It is read as 3 standard deviations.
- The sample period for the cyclicals vs defensives rule and the CESI rule is not stated in the text.
- Figures 6.1 to 6.15 are charts. Return paths around FOMC and NFP days are available only as prose.
- The prose says the CESI rule is active "25% of the time". The chart table shows 27.49%.
- Chart with a statistics table still unread in the PDF: Figure 6.6, cyclicals vs defensives rule (p. 140). Its IRs are in the prose.
