# Chapter 12: How to Trade FX: The Framework

## Core Idea
FX is a relative price with a weak link to the global cycle, so single-variable macro rules give low information ratios. Two things work: combining several weak signals that agree (the EUR composite model), and harvesting factors, above all volatility-adjusted carry, with cut-outs for volatility spikes and crowding.

## Frameworks Introduced
- **USD smirk** (the authors' revision of Stephen Jen's USD smile): the USD strengthens when the US goes into recession (risk aversion) and is supposed to strengthen when the US does exceptionally well (rate differentials).
  - Evidence: for manufacturing PMIs below 45 a weak USD is very rare. The right side is weak: the hit ratio of long USD with the PMI above 60 "is not good". Using GDP, relative PMIs, growth changes or quarterly returns does not improve it.
  - "For almost all PMI outcomes, anything is possible in terms of USD returns."
- **Carry vs equity correlation map** (2002 to 2024): high-carry currencies are usually positively correlated with the SPX. The USD is the exception: positive carry and negative SPX correlation, which made it an attractive hedge. JPY and CHF also gain in risk aversion but carry negatively. EUR has the least beta to risk aversion in G10.
  - Not ironclad: it failed for long periods in the 1990s, in 2001 and 2002, and after "liberation day" in 2025. Both later cases were periods when US exceptionalism was under pressure.
- **Left side of the smirk for EUR, two signals**:
  1. BTP-Bund spread below or above its 55dma. "Creates significant alpha", and not only in 2011 and 2012. Risk/reward 0.42.
  2. Eurostoxx vs MSCI US in local terms against its 55dma, two-day lag. Works better than the spread signal (risk/reward 0.50 against 0.02 for long EUR).
- **Right side: relative data momentum**: go long EUR when the Eurozone minus US difference in Citi's data change indexes (CECID) crosses above zero, and the reverse.
  - Data change indexes (releases scored against the previous 12 months) work better than surprise indexes (CESI, scored against consensus), although CESI moves faster.
  - DXY traded only when the differential favours the US: IR 0.84 with CESI negative and 0.63 with CESI positive. Negative in the opposite case (-0.47, -0.41). EUR with the differential favouring the Eurozone: 1.25 and 0.45. Adding CESI adds nothing.
- **Which rate drives EURUSD**:
  - Perfect-foresight test (position by the sign of the realized weekly rate change): differentials beat outright rates. US rates beat European rates. Two-year nominal is highest.
  - Tradable test (rate above or below its 55dma, two-day lag): the US-Germany five-year spread is best, then the two-year spread. IR only 0.40 in the prose (risk/reward 0.44 in the chart). Two-year 0.35, ten-year 0.32, ten-year real -0.18.
- **Curve regimes and the USD** (2s/10s vs 55dma, one-day lag): bear steepening is most USD bullish (active IR 0.86). Bull steepening is most USD bearish (-0.47). Bear flattening is somewhat USD bullish (0.10). Bull flattening is USD bearish (-0.24). Steepening regimes have much stronger IRs than flattening regimes. These regimes are on less often, so the composite uses rate differentials.
- **EUR composite model**: four signals, each +1 or -1: BTP-Bund spread, relative equity performance, relative data change, five-year yield differential.
  - Trade only when all four agree (+4 or -4): active IR 1.75. On about 16% of the time.
  - Trade the aggregate of all four: IR 1.17. On about 66% of the time.
  - Baseline: long EUR carry adjusted, IR 0.02.
  - A related Citi version (Miani et al., 2025) adds terms of trade and works across G10 except Japan.
- **USD in equity bubbles**: building US equity bubbles are typically USD bullish and sometimes turn USD bearish late. The bubble draws portfolio and FDI flows. DXY pullbacks inside the regime can be large, so it is background, not a trading framework.
- **JPY rules**:
  - JPY appreciates with risk aversion, unlike most of G10. Reasons: Japan's large net international investment position (repatriation in crises) and JPY's role as carry funder.
  - Perfect foresight: positioning with the direction of US rates gives a Sharpe ratio above 3 for most curve sectors. US rates alone slightly beat differentials with Japan.
  - Tradable: long USDJPY when two-year US rates are above their 55dma (one-day lag) gives IR 0.24 only. It worked before mid-2012 and from 2021. It failed for almost 10 years under Abe.
  - VIX rule: buy JPY at the next day's close after VIX is x standard deviations above its three-year average, hold five trading days. Since the GFC only moves above 3 standard deviations remain tradable. Full-sample active IR: 0.82 above 2 and 1.63 above 3.
- **FX factor set** (Table 12.1): carry to vol, time-series momentum, cross-sectional momentum, PPP value, economic surprises. Combination IR 1.20 before transaction costs.
- **Carry construction** (the authors' favourite):
  1. Rank currencies by implied yield over implied volatility.
  2. Long the top five, short the bottom five.
  3. Size each currency by its volatility over the previous three months.
  - Why sizing matters: volatility weighting usually leaves a net long USD notional position, which protects in risk aversion and adds carry.
  - Works better in EM than G10. G10 low-yielders (JPY, CHF) rally in risk-off and hurt the short leg. EM low-yielders sell off.
- **Carry timing conditions**:
  - USDJPY: owning the carry basket only when USDJPY is below its 55dma gives IR 4.9 (no lag, no costs). Above: -3.5. For the SPX the split is 2.15 above its 55dma and -0.81 below, and SPX timing "has essentially stopped working post-COVID".
  - Level of carry: once basket carry falls below 400bp returns are much less attractive.
  - Volatility: the late hiking cycle and Fed pauses are attractive because rates and FX volatility fall.
  - Max-volatility cut-out (same measure as Ch 11): cutting when the maximum z-score rises above 2 lifts the active IR from 0.89 to 1.30. The 2 to 4 range still has IR 0.32. Outright negative needs a spike to 4, about 3% of the sample.
  - Crowding (Citi flow data): when leveraged-account inflows were above the 60th percentile in the previous month, forward Sharpe ratios fall significantly but stay positive.
  - Worst outcomes: a volatility spike when positioning is heavy.
  - Default: "have the trade on".
- **Value (PPP)**: rank deviation from PPP, z-score, position in proportion to rank. 22 countries, World Bank data. IR 0.48. Balassa-Samuelson adjustment makes it much less effective. Crowding hurts: one-month forward Sharpe is above 1 when leveraged inflows were in the lower 60th percentile and negative above.
- **Momentum**: cross-sectional (three-month total return, ranked, volatility adjusted, weekly) worked until 2009 and has been noisy since. Sharpe 0.96 since 2022. Time-series (sign of three-month return vs USD) has been more consistent and carries a large net USD position.
- **Economic surprise factor**: sort currencies by CESI level. IR 0.56. It did well during carry drawdowns.

## Key Concepts
- **USD smile / smirk**: USD strength at both growth extremes, or in the authors' version mainly at the weak extreme.
- **CECID**: Citi data change index. Data vs its own previous 12 months.
- **CESI**: Citi economic surprise index. Data vs consensus.
- **Carry to vol**: implied yield divided by implied volatility.
- **PPP**: purchasing power parity, the value anchor.
- **Time-series vs cross-sectional momentum**: own trend vs USD, or rank against other currencies.
- **Net international investment position**: external assets minus liabilities. Large and positive for Japan.
- **Abenomics**: three arrows (monetary easing, flexible fiscal policy, structural reform) from late 2012.
- **Perfect-foresight test**: a non-tradable test that uses realized changes to find which driver matters.

## Mental Models
- Think of FX as needing agreement across weak signals. No single macro driver has a tradable IR.
- Models work better on baskets than on single pairs, because idiosyncratic shocks wash out.
- Think of the USD as the rare currency that pays carry and hedges equities, until US exceptionalism is questioned.
- A regime change that breaks a quant rule (Abe) can be the best time for discretionary macro: strong trends with a fundamental story.
- Use USDJPY, not the SPX, as the risk gauge for carry.

## Anti-patterns
- **Trading the right side of the USD smile**: strong US growth does not reliably lift the USD.
- **Trading USDJPY on a simple rates rule**: IR 0.24.
- **Equal-notional carry baskets**: lose the USD cushion.
- **Ranking on carry to vol without sizing by volatility**: IR falls to 0.66.
- **Mean-reversion bets on volatility**: it can stay depressed for a long time.
- **Complicating PPP**: little extra alpha.
- **Expecting mid-2000s momentum returns to come back**: data and access are too widely available.

## Reference Tables
Table 12.1, FX factors:

| | Carry to vol | Eco surprises | Cross-sectional mom | TS mom | PPP | Combination |
|---|---|---|---|---|---|---|
| Return | 2.0% | 0.8% | 1.3% | 2.5% | 1.7% | 1.7% |
| Volatility | 2.2% | 1.5% | 2.1% | 3.4% | 3.1% | 1.5% |
| Risk/reward | 0.89 | 0.56 | 0.64 | 0.71 | 0.55 | 1.20 |
| Max drawdown | -5.1% | -4.8% | -8.3% | -5.9% | -7.7% | -2.6% |

Carry basket variants (global basket, EM and DM):

| Ranking | Sizing | IR |
|---|---|---|
| Carry | Equal | 0.74 |
| Carry | Volatility | 0.71 |
| Carry to vol | Equal | 0.66 |
| Carry to vol | Volatility | 0.89 |

Figure 12.20, forward Sharpe of volatility-adjusted carry by percentile of prior leveraged inflows (recovered from PDF p. 302). Supports the crowding rule:

| Flow percentile | 1m flows | 3m flows | 6m flows |
|---|---|---|---|
| 0-20 | 1.34 | 0.66 | 1.26 |
| 20-40 | 1.82 | 2.71 | 0.05 |
| 40-60 | 1.67 | 1.11 | 1.47 |
| 60-80 | 0.14 | 0.49 | 1.38 |
| 80-100 | 0.55 | 0.57 | 0.79 |
| below 80 | 1.17 | 1.17 | 1.09 |
| Unconditional | 1.04 | 1.03 | 1.02 |

Forward Sharpe of PPP value by percentile of prior leveraged inflows (Figure 12.22 data):

| Flow percentile | 1m flows | 3m flows | 6m flows |
|---|---|---|---|
| 0-20 | 0.97 | 0.96 | 0.52 |
| 20-40 | 1.03 | 0.24 | 0.68 |
| 40-60 | 1.19 | -0.05 | -0.12 |
| 60-80 | -0.37 | 0.49 | 0.35 |
| 80-100 | -0.60 | -0.02 | 0.21 |
| below 80 | 0.58 | 0.39 | 0.33 |
| Unconditional | 0.32 | 0.31 | 0.30 |

Figure 12.4, EUR traded on risk-aversion signals (recovered from PDF p. 286). Supports the left side of the smirk:

| | BTP-Bunds signal | Relative equity signal | Long EUR carry adjusted |
|---|---|---|---|
| Return | 3.82% | 4.55% | 0.16% |
| Volatility | 9.12% | 9.12% | 9.13% |
| Risk/reward | 0.42 | 0.50 | 0.02 |
| Max DD | -20.62% | -28.78% | -45.26% |

Figure 12.5, data change (CECID) and surprise (CESI) differentials (recovered from PDF p. 287). Supports the relative data momentum rule. Panel (a) is long DXY on US minus rest-of-world spreads. Panel (b) is long EUR on Eurozone minus US spreads:

| | CESI > 0, CECID > 0 | CESI > 0, CECID < 0 | CESI < 0, CECID > 0 | CESI < 0, CECID < 0 |
|---|---|---|---|---|
| DXY: return | 1.44% | -0.69% | 1.11% | -0.96% |
| DXY: active IR | 0.63 | -0.47 | 0.84 | -0.41 |
| DXY: % on | 29.18% | 19.91% | 16.23% | 30.69% |
| EUR: return | 1.45% | -0.83% | 1.63% | -2.55% |
| EUR: active IR | 0.45 | -0.61 | 1.25 | -0.79 |
| EUR: % on | 33.63% | 15.62% | 17.33% | 33.40% |

Figure 12.7, EURUSD on US-Germany rate differentials vs 55dma (recovered from PDF p. 289). Supports the choice of the five-year spread:

| | 2-year | 5-year | 10-year | 10-year real |
|---|---|---|---|---|
| Return | 3.21% | 3.98% | 2.88% | -1.65% |
| Risk/reward | 0.35 | 0.44 | 0.32 | -0.18 |
| Max DD | -27.34% | -32.63% | -28.02% | -55.67% |

Figure 12.8, long USD by 2s/10s regime (recovered from PDF p. 290). Supports the curve regime rule:

| | Bull flatten | Bear flatten | Twist flatten | Bull steepen | Bear steepen | Twist steepen | Buy and hold |
|---|---|---|---|---|---|---|---|
| Return | -0.47% | 0.15% | 0.38% | -0.83% | 1.36% | -0.04% | 0.66% |
| Volatility | 4.11% | 3.60% | 2.30% | 3.99% | 3.60% | 2.16% | 8.30% |
| Max DD | -35.35% | -29.70% | -14.48% | -43.04% | -14.36% | -14.06% | -56.70% |
| Active IR | -0.24 | 0.10 | 0.55 | -0.47 | 0.86 | -0.07 | 0.08 |
| % on | 23.46% | 19.52% | 9.03% | 19.15% | 19.26% | 6.37% | 100.00% |

Figure 12.12, buying JPY for five days after VIX is x standard deviations above its three-year average (recovered from PDF p. 293). Supports the JPY VIX rule:

| | VIX > 0 | VIX > 1 | VIX > 1.5 | VIX > 2 | VIX > 3 |
|---|---|---|---|---|---|
| Return | -0.91% | 0.58% | 0.72% | 1.10% | 1.27% |
| Volatility | 6.78% | 5.46% | 4.88% | 4.39% | 3.67% |
| Max DD | -40.96% | -17.16% | -17.41% | -16.39% | -8.03% |
| Active IR | -0.21 | 0.24 | 0.40 | 0.82 | 1.63 |
| % on | 40.45% | 19.20% | 13.61% | 9.42% | 4.53% |

Figure 12.23, FX momentum (recovered from PDF p. 304): cross-sectional return 1.32%, volatility 2.05%, risk/reward 0.64, max DD -8.34%. Time-series return 2.45%, volatility 3.44%, risk/reward 0.71, max DD -5.93%. These match Table 12.1.

## Worked Example
*"The Reign of Abe": when the one-factor JPY model broke.*
1. Late 2012: Abenomics begins. In early 2013 the BoJ under Kuroda launches QQE, buying JGBs and equity ETFs.
2. The monetary base grows from around 125trn JPY in late 2012 to 360trn in early 2016. Ten-year JGB yields fall from around 75bp to around -25bp.
3. USDJPY rallies from around 80 to 125 in 2015. JPY becomes a popular carry funder. This still fits a rates story, but on the Japanese side. US rates were stuck at zero, so the US-rates rule had nothing to trade.
4. Late 2015: JPY turns stronger. Risk aversion takes over (China slowdown, falling oil, recession fears). USDJPY starts to track the Topix more than rates.
5. January 2016: the BoJ moves to negative rates on excess reserves. JPY does not weaken. The market doubts how much policy room is left.
Lesson: the simple rule covers two regimes (pre-2012, post-2021). In between, local policy and risk aversion dominated, and the opportunity was discretionary.

## Key Takeaways
1. Trade EUR only when spread, relative equities, relative data and five-year differential agree.
2. Use data change indexes, not surprise indexes, for the cycle leg.
3. Keep volatility-adjusted EM carry on by default. Size up with high carry, a quiet Fed and light positioning.
4. Cut carry when USDJPY falls, volatility spikes above 2 standard deviations, or both volatility and crowding hit together.
5. Add PPP value and surprises to carry and trend. The combination has the best IR.
6. Buy JPY on VIX spikes only at 3 standard deviations or more.

## Connects To
- **Ch 13**: Fed-cycle timing for the USD, intervention, flows.
- **Ch 11**: the same maximum-volatility cut-out for credit.
- **Ch 5**: rates volatility over the Fed cycle.
- **Ch 8**: bubble definition used for the USD in bubbles.
- **Ch 10**: FX sensitivity of equity markets, Topix and USDJPY.
- **Willer et al. (2020)**: EM carry.

## Extraction Notes
- The text says the BTP-Bund spread "captures more general risk aversion, i.e., the right side of the USD smile". Elsewhere risk aversion is the left side. The source is inconsistent.
- The extracted table for Figure 12.20 had the 1m values merged into the label column. It was checked against PDF p. 302 and the re-aligned table is correct in every cell.
- Figure 12.22's table has stray label fragments ("Percentile", "Flows", "Leveraged") from a rotated axis title. They are dropped above.
- The text says forward Sharpe falls when inflows are above the 60th percentile. The tables also give a "below 80" summary row. Both are in the source.
- The monetary base figure reads "125rn JPY" in the source. It is read as 125trn.
- Sample periods for the composite model and factor table are not stated in the text. The "twist" flattening and steepening regimes in Figure 12.8 are not defined in the prose.
- Charts with statistics tables still unread in the PDF: Figure 12.9 composite model (p. 291), 12.13 USDJPY vs US rates (p. 294), 12.15 carry variants (p. 297), 12.16 and 12.17 carry by EM, USDJPY and SPX (pp. 298-299), 12.19 carry by volatility (p. 301), 12.21 PPP (p. 303), 12.24 surprises and combination (p. 305). Their headline IRs are in the prose.
