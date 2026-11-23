# Chapter 6: Style Premia

## Core Idea
Four long/short styles have earned positive long-run rewards in many asset classes: value, momentum (with trend), carry, and defensive. Each has bad decades. Combining them and spreading them across asset classes is the author's preferred return source after asset class premia. The sourcing is "quite AQR-centric" by his own note.

## Frameworks Introduced
- **Admission test for a style**: persistent (in and out of sample), pervasive (many asset classes), robust (many specifications), with a sound economic rationale and realistic implementation.
- **The quartet and its splits**: value and reversal, momentum and trend, carry and volatility selling, low risk and quality. Size is excluded (Box 6.1).
- **Section template the author uses for each style**: flagship strategy, economic rationale, historical performance, consistency and extensions, other contexts, risks and pitfalls, current outlook.
- **Value** (6.1): sort assets by fundamental value over price, long cheap, short rich.
  - Design choices that matter most: the indicator and sector neutrality (note 7).
  - Measures by asset class: B/P or CAEY for equity indices, real yield for bonds, purchasing power parity for currencies, five-year price reversal for commodities.
  - Why it pays: rich stocks do grow faster, but the valuation gap discounts "even wider" growth differences than later appear.
  - **"Contrarian strategies are inherently short a structural change."**
  - **Value spread**: ratio of cheap-side to rich-side valuation. Cheap stocks sit near 1.3 times the median, rich near 0.7.
- **Momentum and trend** (6.2): cross-sectional momentum is long past-12-month winners and short losers, skipping the last month. Trend following takes each asset's own 12-month sign.
  - Why both value and momentum pay: assets trend up to one year and mean-revert over several years. "The sweet spot" is cheap and recently improving.
  - Value and momentum correlate near -0.5, so the best blend is near 50/50.
  - **Trend "smile"**: profits in large moves either way, like a long straddle. Weak in choppy markets.
  - **Risk of a bang versus risk of a whimper**: momentum crashes at sharp turns (summer 1932, spring 2009, November 2020). Trend bleeds in whipsaws (the 2010s).
- **Carry** (6.3): "an asset's return in unchanged capital market conditions". Carry is an unknown blend of expected market change and required risk premium.
  - Yield overstates expected return for risky bonds (high yield "by about a half"). Dividend yield understates it for equities.
  - **Carry is not earned in isolation. It reflects the underlying asset's beta risk.** Credit carry buys riskier bonds. Dividend-yield stock carry buys safer firms.
  - **1/price effect**: any required premium lowers price against a fundamental anchor.
- **Defensive** (6.4): within an asset class, low-risk assets earn better risk-adjusted returns. The security market line is too flat (Figure 6.12). With geometric means it is inverted.
  - Two explanations: leverage constraints and lottery preferences.
  - **BAB** (bet against beta): long low-beta levered up, short high-beta levered down, ex-ante beta zero. Example: long $2 of a 0.5-beta portfolio, short $0.67 of a 1.5-beta portfolio.
  - **QMJ** (quality minus junk): 16 metrics in profitability, growth and safety. Dollar-neutral, so net negative beta.
  - Dollar-neutral defensive strategies are truly defensive in sell-offs. Market-neutral BAB is about 50/50.

## Evidence table (gross of costs and fees unless stated)
| Item | Value | Where |
|---|---|---|
| Value SR, multi-metric industry-neutral, 1984 to June 2021 | US large 0.50, US small 0.79, ex-US large 0.73, ex-US small 0.99 | Table 6.2 |
| Value SR, raw B/P, same universes | 0.15, 0.16, 0.35, 0.30 | Table 6.2 |
| Worst US B/P value drawdowns | -63% (2007-2020), -59% (1890-1904), -53% (1926-32), -35% (1998-2000) | 6.1 |
| Short-term reversal SR since the 1930s | 0.77 on paper, "arbitraged away by the mid-2000s" | 6.1 |
| Trend composite SR 1926-2020, 12-month with one-month lag | 0.89 | note 18 |
| Same with correlations, no lag, three windows | 0.96, then 1.27, then 1.67 | note 18 |
| Trend SR by asset class | 0.44 (currencies) to 0.62 (bonds) | 6.2 |
| Multi-asset carry SR since 1927 | 0.8, double currency carry | 6.3 |
| Currency carry equity correlation | from near zero to above 0.5 | Figure 6.11 |
| BAB: CAPM alpha, SR, information ratio | 9%, 0.73, 0.80 (90 years) | 6.4 |
| QMJ: CAPM alpha, SR, information ratio | 6%, 0.54, 0.91 (64 years) | 6.4 |
| BAB / QMJ marginal alpha over other factors | 3-4%, significant | 6.4 |
| BAB SR large / small cap | 0.38 / 0.85 | 6.4 |
| Global BAB / QMJ SR 1990-2020 | 0.98 / 0.70 | 6.4 |
| BAB across maturities in US Treasuries and credits | SR 0.8-1.0 in earlier studies | 6.4 |
| Dollar-neutral defensive betas | -0.3 to -0.8 | Table 6.3 prose |

## Worked Example: the 2018-2020 value loss, hypothesis by hypothesis (6.1)
The author lists explanations and what the evidence did to each.
1. FAMAG outperformance: "only a small part".
2. A US-only problem: no. Losses hit all regions and most industries.
3. A book/price problem: no. Other metrics lost almost as much.
4. Tech, mega-caps or the priciest names: excluding them leaves the dislocation as large. More came from the cheap side.
5. Falling bond yields: "a weak long-run empirical link". A small fraction at most.
6. Crowding: no sign of rising value overweights in holdings data.
7. Intangibles: adjusted B/P "would not have saved" value.
His reading: the market priced disruptive growth more richly with little change in measured fundamentals. "Another case of bubble and irrational exuberance." The flipside is a value spread at or near record wide in 2020-2021 (Figure 6.3), wider still outside the US. The drawdown troughed in late 2020. He names no single catalyst and says timing "was always difficult".

## Key Concepts
- **Smart beta**: long-only portfolio with style tilts. **Alternative risk premia (ARP)**: the long/short form.
- **HML**: Fama-French high-minus-low B/P portfolio. Top 30% against bottom 30%, yearly rebalance.
- **Momentum crash**: sharp loss just after a market turn.
- **Macro momentum**: favour markets with improving growth, soft inflation, easy policy, better terms of trade. About 0.4 correlated with trend.
- **Crisis alpha**: trend's gains in protracted bear markets.
- **Uncovered interest parity / pure expectations hypothesis**: the zero-premium theories that carry profits contradict.
- **Long-shot bias**: the low-risk effect in sports betting.

## Mental Models
- Read the decade charts as a forest, not trees. Value was negative in several asset classes in the 1920s, 1950s and 2010s. All were positive over the century.
- Bear markets are usually gradual because of early underreaction and later feedback selling. That is why trend tends to help. Fast drawdowns are its "Achilles' heel".
- Flow momentum only works if you can name a subset worth following. Net flows sum to zero.
- For commodities, cumulative carry far exceeds cumulative return. For equity, bond and currency country strategies the two align (Figure 6.10).
- Low-rate, reach-for-yield conditions may bid the carry premium toward zero "at least temporarily".
- Central banks curtailed trends in the 2010s. Larger, gradual inflation moves "may thus well suit trend-following".

## Anti-patterns
- **Abandoning a style after a bad decade**: "such capitulations may make a long recovery even more likely".
- **Tinkering with trend and momentum overlays**: raises overfitting risk.
- **Timing momentum, trend or defensive on valuation**: "little evidence" it works.
- **Naive yield seeking**: hyperinflation currencies, near-default debt, structured notes with embedded short options.
- **Calling BAB defensive**: it is market-neutral, not protective.
- **Treating size as a rewarded factor**: no premium beyond beta outside untradeable micro-caps.

## Key Takeaways
1. Value-based issuer selection in corporate bonds has "an especially good track record", using a fair value model and not a simple ratio.
2. Short-maturity bonds have higher risk-adjusted returns than long ones in both Treasuries and credit. Capturing that needs leverage.
3. Credit, currency carry and volatility selling carry negative skew and lose in equity drawdowns. Other carry strategies are more benign. The puzzle is why those are paid.
4. Tactical carry timing on risk aversion worked into late 2008 and gave false alarms through the 2010s.
5. Defensive stocks looked rich on value spreads for over a decade and still performed.

## Extraction Notes
- Table 6.1 (correlation matrix of premia) and Table 6.3 (defensive strategy statistics) did not survive. Prose values are recorded.
- Table 6.2 survived in full.
- Figures 6.1 to 6.13 are images.

## Connects To
- **Ch 4**: fallen angels and front-end credit as defensive and liquidity effects.
- **Ch 8**: rationales and who is on the other side.
- **Ch 9**: sticking with styles through bad times.
- **Ch 11**: what low correlations among styles do to the Sharpe ratio.
- **Ch 13**: trend as a tail hedge, with drawdown numbers.
- **Ch 16**: contrarian factor timing.
