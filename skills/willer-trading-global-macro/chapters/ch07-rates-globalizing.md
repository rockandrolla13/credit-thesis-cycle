# Chapter 7: How to Trade Rates: Globalizing

## Core Idea
Global bond markets decouple from US Treasuries only to a limited extent, and more at the front end than at the back end. The same Fed-cycle rules, plus one FX-hedged carry rule, carry over to spreads against Bunds, gilts and JGBs. In a global easing cycle, receive the leaders, not the laggards.

## Frameworks Introduced
- **Front end local, back end global**: front ends follow local central banks. Back ends also price the spread to UST, which drives investment flows and term premium. Weekly-change correlation with the US runs from 0.06 (China) to 0.59 (Canada) at 2 years and from 0.10 (Brazil) to 0.79 (Canada) at 10 years.
- **Leaders vs laggards in a Fed easing cycle** (Willer et al., 2024g): proxy market pricing by the one-year swap minus the floating rate, measured one month before the first Fed cut. Track the change in the one-year rate until three months after the first Fed cut.
  - 2001: one-year yields fell everywhere. Slight edge to leaders.
  - 2007: 6 of 18 markets priced hikes, and in 5 of those 6 rates were higher three months after the first Fed cut. US stress took longer than expected to spread.
  - 2019: receiving mostly worked. Tight relationship between priced dovishness and subsequent moves.
  - 2024: good for receivers in most countries. Japan and Brazil, the two laggards, sold off meaningfully.
  - Rule: "investors should chase the leaders rather than the laggards." A Fed cycle alone is not sufficient reason to receive the rest of the world.
  - Caveat stated: the study shows rate changes, not receiver P&L. Receiving inverted curves has negative carry.
- **Close-neighbour reversal** (Sweden/Norway, Australia/New Zealand, Canada/US): trigger when the five-year spread is at its most extreme value in a 1,000-day lookback. Reversals exist but are weak. Australia/New Zealand stabilizes first and reverses later in the median case. The other two pairs keep diverging for about two more months. Use the trigger as a prompt to look for a fundamental catalyst.
- **Spread trading by relative policy** (UST vs Bunds, UST vs gilts): front-end spreads follow leads and lags in central bank action, and back-end spreads follow front-end spreads. Apply the outright rules to the spread: pay the spread slightly before relative tightening starts, stay paid until shortly before the last differential hike, then receive. Example: the US-UK spread peaked in November 2018 and the last differential hike was December 2018.
- **FX-hedged carry at extremes** (duration-matched or volatility-adjusted, FX hedged):

| Pair | Top-percentile pickup: IR | Bottom percentile: IR | Unconditional IR |
|---|---|---|---|
| UST vs Bunds | 0.60 (UST outperform, spread in top 90th percentile) | -0.79 (Bunds outperform, bottom 10th) | -0.13 |
| Gilts (FX-hedged yield differential) | 0.63 (top 10th percentile) | -0.56 (bottom 10th) | 0.07 |
| Long JGBs vs short UST (pickup percentile over last 12 months) | 0.72 | -0.81 | -0.16 |

  - Failure mode: the UST-Bund version has gone largely sideways since 2020. The authors' reason: it is a fixed-income carry strategy, and carry does poorly in a bond bear market.
- **Periphery rule (Italy)**: peripheral bonds carry a monetary policy component and a credit component. The best environment is strong growth in the periphery and weak growth in the core.
  - Backtest on Citi data surprise indexes, Italian spread returns: active IR moves from 0.30 to 1.21 when German surprises are negative and Italian surprises are positive. In the reverse case it is 0.19. Both positive gives 0.76. Negative surprises for both is the worst combination at -0.38.
  - Reading: the credit component matters more than the rates component.
- **BTP vs corporate credit bands** (Bansal, 2025): the BTP asset swap spread trades with European credit. After the European crisis a spread above the IBOXX EUR non-sovereign BBB Z-spread signalled cheap. A spread on par with the A Z-spread signalled expensive. Italy's credit improvement has recently shifted the lower bound to the AA spread. Sharp spikes can trigger an ECB response (PEPP in 2020), so fade them.
- **Japan rules**:
  - The BoJ structurally hikes late, after the Fed is done, and historically has not got far once the Fed turned.
  - USDJPY is a crucial driver of Japanese inflation. Fed cuts weaken USDJPY and take pressure off Japanese inflation.
  - JGB performance when US rates are below their 55dma has an active IR of 0.9 against 0.28 otherwise.
  - Position for a BoJ cycle at the front end. Flatteners often work in a hawkish BoJ cycle unless fiscal worries dominate. Be more careful with Japan payers after Fed cuts begin, mainly in a US hard landing.
  - Front-end timing: rates start to sell off less than a year before the first BoJ hike and peak around the last hike, sometimes with longer lags than in the US (2005 peak, 2015 low).
- **China rule**: CGBs follow the local cycle because of the closed capital account. Yields are unlikely to trough before the last interest rate cut or RRR cut. Pauses in the cutting cycle can cause large pullbacks.
- **EM local regime grid** (FX-hedged EM local, DXY and US rates each above or below their 55dma, lagged one day):
  - US rates and DXY both below: active IR 2.47. Both above: -1.5.
  - US rates matter more than the USD. Low yields with a strong USD (3.15) beats high yields with a weak USD (0.07).
  - Higher rates without a stronger USD occurs 21% of the time. EM local hedged is still positive there, with a very low IR.
  - Unhedged: only the both-below case is strong, at 1.39 (the prose rounds to 1.4).
- **One-way traffic**: US rates drive global rates, not the reverse. Japan holds just below 15% of outstanding Treasuries. Japanese investors bought Treasuries with deeply negative hedged pickup in 2019 and 2023. They buy late in Fed hiking cycles, through easing cycles and holds, and sell early in hiking cycles. Treasuries generally perform well after BoJ hikes.

## Key Concepts
- **Leader / laggard**: a market that already prices meaningful cuts, or does not, when the Fed starts.
- **Global shock in a trench coat**: a local shock in a large economy that becomes global with a delay (the US housing bust in 2007).
- **FX-hedged pickup**: yield advantage after hedging currency. The hedge removes front-end carry, so the spread is roughly symmetric around zero.
- **LDI funds**: leveraged gilt holders used by UK pension funds. Margin calls on them forced selling in 2022.
- **Asset swap spread (ASW)**: bond yield against swaps. Used to compare BTPs with corporate credit.
- **PBoC toolkit**: MLF rate, 7-day reverse repo rate, RRR, open market operations.
- **Bond vigilantes**: investors who sell bonds to force fiscal change.

## Mental Models
- Think of only the US, the Eurozone and China as able to generate a shock that goes global.
- Think of peripheral bonds, like EM bonds, as rates plus credit. A cut driven by a deep recession can help the rates part and hurt the credit part.
- In G10 the causality runs from rate spreads to FX. In EM, FX also drives rate spreads.
- Japanese buyers of Treasuries trade the Fed cycle for capital gains, not the carry.
- "It is always reassuring when the same rules work across multiple assets without any tweaks."

## Anti-patterns
- **Receiving everywhere because the Fed cuts**: failed in 2007.
- **Receiving laggards to catch up**: laggards performed less consistently.
- **Expecting BoJ policy to move Treasuries**: little evidence.
- **Owning EM local unhedged as a default**: FX adds most of the volatility without matching return.
- **Reading the Truss episode as a pure fiscal verdict**: the authors blame misunderstood leverage.

## Reference Tables
Correlation of weekly yield changes with the US (Tables 7.1 and 7.2):

| Market | 2-year | 10-year |
|---|---|---|
| Canada | 0.59 | 0.79 |
| Germany | 0.51 | 0.71 |
| UK | 0.43 | 0.66 |
| Mexico | 0.42 | 0.47 |
| Japan | 0.18 | 0.28 |
| Brazil | 0.08 | 0.10 |
| China | 0.06 | 0.16 |

Other pairs: Germany-UK 0.55 (2y) and 0.79 (10y). Mexico-Brazil 0.20 (2y) and 0.32 (10y).

Figure 7.10, Italian spread returns by German (DE) and Italian (IT) data surprise sign (recovered from PDF p. 162). Supports the periphery rule:

| | DE + / IT + | DE + / IT - | DE - / IT + | DE - / IT - | Buy and hold |
|---|---|---|---|---|---|
| Return | 0.67% | 0.22% | 1.11% | -0.58% | 1.42% |
| Volatility | 2.24% | 3.21% | 2.28% | 3.99% | 6.04% |
| Max DD | -6.94% | -11.48% | -8.30% | -21.30% | -20.21% |
| Active IR | 0.76 | 0.19 | 1.21 | -0.38 | 0.30 |
| % on | 15.43% | 13.32% | 16.40% | 15.04% | 60.19% |

Figure 7.17, EM local bonds by DXY and US 10-year regime, each vs its 55dma (recovered from PDF p. 169). Supports the EM local regime grid:

| | DXY high, 10y high | DXY high, 10y low | DXY low, 10y high | DXY low, 10y low |
|---|---|---|---|---|
| FX hedged: return | -1.04% | 2.01% | 0.03% | 1.29% |
| FX hedged: volatility | 1.31% | 1.29% | 1.03% | 1.06% |
| FX hedged: max DD | -18.21% | -3.27% | -6.89% | -2.88% |
| FX hedged: active IR | -1.50 | 3.15 | 0.07 | 2.47 |
| Unhedged: return | -2.88% | 1.10% | 0.38% | 2.50% |
| Unhedged: volatility | 4.47% | 5.02% | 3.75% | 3.66% |
| Unhedged: max DD | -40.67% | -14.96% | -19.45% | -8.11% |
| Unhedged: active IR | -1.22 | 0.44 | 0.23 | 1.39 |
| % on | 27.93% | 25.23% | 20.55% | 24.41% |

## Worked Example
*"A Loss of Truss", September to October 2022.*
1. September 23: the mini-budget proposed GBP 45bn of unfunded tax cuts plus energy subsidies. Extra borrowing of GBP 72bn over six months, almost 3% of GDP. Inflation was high and the BoE was hiking.
2. Gilts sold off by more than 100bp in one week. The curve first flattened (market expected more BoE hikes), then steepened aggressively (fiscal fear). GBP fell, although higher rates are normally currency-positive in developed markets.
3. September 28: the BoE announced temporary gilt purchases of up to GBP 65bn, to run to October 14. Yields pulled back. October 3: one tax cut was reversed. Yields retested the highs days later.
4. October 14: the chancellor was replaced and the remaining tax cuts were reversed. Gilts rallied 100bp. October 20: the prime minister resigned.
5. Authors' reading: LDI margin calls caused forced selling, so "the problem was misunderstood pockets of leverage, rather than the fiscal announcement by itself." The BoE stabilized the market while still hiking because the purchases were limited in time and size. They call it "a partial validation of the bond vigilantes at best".

## Key Takeaways
1. Express local central bank views at the front end. Expect the back end to follow the US.
2. Receive the markets that already price cuts when the Fed starts.
3. Trade UST against Bunds, gilts or JGBs on FX-hedged pickup only at the extremes.
4. Own Italian spread when German data disappoint and Italian data beat.
5. Own JGBs when US yields are below their 55dma.
6. Own FX-hedged EM local when both US rates and DXY are below their 55dma.
7. Look for pockets of leverage when judging whether a fiscal scare will force policy.

## Connects To
- **Ch 5**: the US Fed-cycle clock applied here to spreads.
- **Ch 3**: Europe as a follower, the ECB lagging the Fed.
- **Ch 12, Ch 13**: JPY, carry and the FX leg of EM local.
- **Willer et al. (2020)**: CGBs and EM rates in detail.

## Extraction Notes
- The chapter summary says "when FX-hedged UST yields fall below Bunds, they outperform." The body says UST outperform when the FX-hedged spread is in the top 90th percentile and Bunds outperform in the bottom 10th. The two statements do not obviously agree. Both are in the source.
- For gilts and JGBs the text does not say which side the "yield differential" is measured from in every case. The table above keeps the source wording.
- The China passage says "rates bottom when the first hike is relatively close and then rally throughout the easing cycle", "just like in the case of the United States". The figure caption says CGBs peak after the last hike and trough after the last RRR cut. The sentence may be garbled.
- A sentence in section 7.8 has a stray caption fragment inside it ("seems to be UST returns around hawkish BoJ events the stage of the Fed cycle").
- Sample periods for the carry and surprise backtests are not stated. Figures 7.1 to 7.19 are charts.
- In the Figure 7.17a table the max DD and active IR rows are interleaved in the PDF text layer. The cells above pair each value with its column by order (drawdown, then IR, per column).
- The prose says the 10y-high, DXY-low case occurs 21% of the time. The chart shows 20.55%.
- Charts with statistics tables still unread in the PDF: Figure 7.5 UST vs Bunds (p. 156), Figure 7.8 gilts (p. 158), Figures 7.13 and 7.14 JGBs (p. 165). Their IRs are in the prose.
