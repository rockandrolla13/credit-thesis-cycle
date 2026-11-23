# Chapter 13: How to Trade FX: The Tactics

## Core Idea
The USD has a loose link to the Fed cycle except around the first cut, where it weakens beforehand. Intervention only buys time and works when fundamentals turn too. Positioning flows should be faded when volatility rises, and large intraday reversals follow through.

## Frameworks Introduced
- **USD around Fed turning points** (from 1986):
  - First cut: the USD falls by around 4% on average in the three months before. It goes mostly sideways after.
  - First cut in a soft landing: the same weakness going in, then a much stronger rebound. The US avoiding recession and deeper cuts is USD positive. In 1995 and 1998 an EM crisis was running. In 2024 China was weak. "A strong USD is a typical feature of a soft landing."
  - Last cut: the USD trades weaker into it, then stabilizes and rallies slightly, into the first pause.
  - Rule: be short USD into the first cut, and be nimble with USD shorts afterwards if a soft landing looks likely.
- **Intervention framework**:
  - Definition of success: a profitable trade on the announcement over a short horizon.
  - EM vs G10: EM intervenes more, usually against weakness, because weak FX is more inflationary and can hit foreign-currency debt. G10 intervenes more often against strength.
  - Types: bilateral vs multilateral (multilateral presumed more likely to work), sterilized vs non-sterilized (theory says sterilized is extremely unlikely to succeed).
  - From the authors' EM work: short-term outperformance follows intervention. The impact is stronger when buying USD than when selling USD, and size matters.
  - Rule: "only go with the intervention if fundamentals also point in that direction." For policymakers intervention is a bridge to a change in fundamentals. Otherwise it is "a bridge to nowhere".
  - When it works USDJPY moves more than the fundamental driver, because the currency is by then cheap, oversold and positioned the wrong way.
- **Japan's intervention choreography** (Takashima, 2025):
  1. MOF says excessive and disorderly moves are undesirable.
  2. Statements of close monitoring, and a warning of appropriate action if necessary.
  3. The BoJ checks rates.
  4. A last warning of determined action against speculative moves.
  5. Intervention. Confirmation comes only afterwards.
- **Flow rules** (Citi proprietary flows, Saunders et al., 2023):
  - Go with the flow, short horizon: the best trend-following behaviour is the 10-day bank flow, then the 22-day bank flow. Bank flows are somewhat negatively correlated with coincident price action, so following them has a mean-reversion flavour. Five-day leveraged flows work episodically. All versions weakened after COVID. "We would therefore be cautious in using flow data for trend following."
  - Fade the flow, longer horizon: fading the three-month flow of leveraged investors has IR 0.26. With a volatility trigger (combined equity and FX volatility above its 50th or 70th percentile, hold at least five days or until volatility drops below the threshold) the active IR rises to 0.70 and 0.74. This version "is still going strong".
- **Intraday reversal rule** (tested on USDMXN): an intraday sell-off of 2% or more in MXN terms where more than 100% of the move reverses by the close and USDMXN ends lower. Sell USDMXN at the close and hold for up to nine days for a high IR (active IR 1.32 at 4 days, 1.41 at 9). The IR declines but is still tradable at one month (0.81 at 21 days). It is 0.33 at 43 days and 0.12 at 65 days, against 0.31 for holding MXN carry adjusted.
  - Logic: "if USDMXN can not move up on this election result, what can cause a sell-off?"
- **FX basis**: a wider FX OIS basis should in theory be USD positive. On average there is no strong correlation with spot. "For directional trading, focusing on the FX basis is not overly useful."

## Key Concepts
- **Sterilized intervention**: FX intervention whose effect on the money supply is offset.
- **Multilateral intervention**: coordinated with other central banks, as on June 17, 1998.
- **MOF / BoJ**: the Ministry of Finance decides and the Bank of Japan executes.
- **Rate check**: the BoJ asking dealers for quotes, a late-stage warning.
- **Bank flows / leveraged flows / real-money / corporate flows**: Citi's client flow categories.
- **FX OIS basis**: spread between the USD rate implied by FX swaps and the USD OIS rate. A gauge of USD funding demand.
- **Intraday reversal**: a move fully retraced by the close.

## Mental Models
- Think of a US soft landing as someone else's hard landing. Relative US strength then lifts the USD.
- Think of intervention as timing help at an already stretched level, not as a trend maker.
- A market that cannot sell off on bad news has priced the risk.
- Short-horizon flows carry information. Three-month leveraged flows mark crowding, and crowding matters when volatility rises.

## Anti-patterns
- **Chasing intervention on its own**: in 1998 followers "would have lost money chasing it". In April 2024 USDJPY made new highs shortly after.
- **Fading short-term flows**: the weak trend evidence still warns against it.
- **Fading three-month flows in calm markets**: IR 0.26 is too low to trade.
- **Reading the FX basis for USD direction**: no reliable link.
- **Staying short USD after the first cut in a soft landing**: the rebound is strong.

## Reference Tables
Figure 13.7 data, following flows:

| | Bank 10d flow | Bank 22d flow | Leveraged 5d flow |
|---|---|---|---|
| Return | 1.39% | 0.84% | 0.46% |
| Volatility | 1.65% | 1.68% | 1.68% |
| Risk/reward | 0.85 | 0.50 | 0.27 |
| Max DD | -2.59% | -4.09% | -6.09% |

Figure 13.8 data, fading the three-month leveraged flow:

| | Always | Volatility above 50th percentile | Volatility above 70th percentile |
|---|---|---|---|
| Return | 0.70% | 0.87% | 0.56% |
| Volatility | 2.72% | 1.94% | 1.57% |
| Max DD | -10.62% | -4.22% | -4.30% |
| Active IR | 0.26 | 0.70 | 0.74 |
| % on | 100.00% | 42.04% | 23.31% |

Japanese JPY-buying interventions:

| Episode | What happened | Fundamental that turned |
|---|---|---|
| Nov and Dec 1997 | Little success. December 17 was a one-day move | none |
| April 9, 1998 | Two-day impact, with repeat intervention and a fiscal package | none |
| June 17, 1998 | Joint with the US. USDJPY fell more than 5% in a day, then returned above pre-intervention levels for one day | none yet |
| August 12, 1998 | Verbal. Marked the peak | SPX fell after the Russian default on August 17. First leg down around 23% |
| September 2022 | Not tradable | none |
| October 21 to 24, 2022 | Tradable | US rates turned lower |
| Late April 2024 | Short-lived. New highs after | none |
| July 11, 2024 | Local peak. USDJPY fell 13% in a bit more than two months | US rates fell after a very weak July NFP |

Figure 13.9, long MXN after a full intraday reversal, by holding period (recovered from PDF p. 315). Supports the intraday reversal rule:

| | 4 days | 9 days | 21 days | 43 days | 65 days | MXN carry adjusted, always |
|---|---|---|---|---|---|---|
| Return | 0.36% | 0.58% | 0.62% | 0.41% | 0.20% | 3.61% |
| Volatility | 2.79% | 3.12% | 3.95% | 4.77% | 5.44% | 11.62% |
| Max DD | -11.53% | -11.53% | -11.53% | -22.19% | -26.13% | -39.33% |
| Active IR | 1.32 | 1.41 | 0.81 | 0.33 | 0.12 | 0.31 |
| % on | 0.95% | 1.75% | 3.67% | 6.72% | 9.61% | 100.00% |

## Worked Example
*USDMXN after the 2024 US election.*
1. On the day after the election USDMXN spiked intraday, then reversed the entire move and closed lower. This met the reversal condition.
2. The reading (Willer et al., 2024a): enough Trump risk was already priced into MXN.
3. Follow-through in USDMXN lasted only one day, because the broad USD was very strong. Selling EURMXN worked on a 10-day horizon.
4. Fourteen days later a tweet about 25% tariffs on Mexico produced another one-day spike that quickly reversed.
5. The election-day intraday high in USDMXN "was not conclusively taken out in this cycle".
The example shows the rule and its caveat: check the broad USD trend and consider a cross that removes it.

## Key Takeaways
1. Sell the USD in the three months before the first Fed cut. Reassess at the cut.
2. Expect a stronger USD after the first cut if the landing is soft, and after the last cut.
3. Trade with intervention only when rates or equities confirm.
4. Fade three-month leveraged flows when equity and FX volatility is above its median.
5. Follow full intraday reversals for about nine days.
6. Do not use the FX basis for direction.

## Connects To
- **Ch 12**: structural FX framework, JPY and US rates, carry and crowding.
- **Ch 4**: elections, risk premium and the 2016 USDMXN contrast.
- **Ch 5**: dating first and last cuts.
- **Ch 8**: equities around the same Fed events.
- **Willer et al. (2020)**: EM intervention study.

## Extraction Notes
- The text first lists JPY purchase episodes in "October 21 to 24, 2022", then also mentions a first intervention in September 2022 that was not tradable. Both are in the source.
- The intraday rule is worded as "intraday sell-offs of 2% or more" where "USDMXN ends the day lower". The context is an intraday spike higher in USDMXN (a sell-off in MXN) that reverses. The wording in the source is ambiguous.
- Sample periods for the flow studies and the reversal study are not stated in the text.
- A stray "20" sits in the 1997-1998 sentence in the source. Figures 13.1 to 13.10 are charts.
- The reversal rule is in the market under 1% of the time at the four-day hold, so the sample of events is small.
- Figures 13.1 to 13.6 and 13.10 are path charts with no statistics table. No chart with a statistics table remains unread in this chapter.
