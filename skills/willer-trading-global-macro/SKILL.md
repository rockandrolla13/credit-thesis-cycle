---
name: willer-trading-global-macro
description: "Knowledge base from \"Trading Global Macro Markets\" by Dirk Willer and Alex Saunders. Use when applying Willer and Saunders' frameworks for Fed-cycle rates trading, business-cycle and recession playbooks, credit spread rules, FX carry, commodities, regime-based asset allocation, studying the book, or referencing its concepts."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# Trading Global Macro Markets
**Author**: Dirk Willer and Alex Saunders | **Pages**: ~397 | **Chapters**: 16 | **Generated**: 2026-11-21

## How to Use This Skill

- **Without arguments** — load core frameworks for reference
- **With a topic** — ask about `fallen angels`, `first cut`, or another indexed topic; I find and read the relevant chapter
- **With chapter** — ask for `ch11`; I load that specific chapter
- **Browse** — ask "what chapters do you have?" to see the full index

When you ask about a topic not covered in Core Frameworks below, I will read
the relevant chapter file before answering.

---

## Core Frameworks & Mental Models

**Read every number as the authors' backtest.** They state that they typically assume zero transaction costs, accept small samples, do not require statistical significance and do not separate in-sample from out-of-sample (Ch 1, Ch 2). Returns are excess over T-bills. "Active IR" is the information ratio while a rule holds a position.

**Method (Ch 2).** Establish the base rate from history, then ask what differs this time. Markets trade two or three stories at once and rarely look more than a few months ahead. Default signal parameter: the 55-day moving average, lagged one day.

**Business cycle (Ch 3).** Use five regimes: Goldilocks, overheating, stagflation, early recession, late recession. Risky assets do worst in early recession and stagflation, best in late recession.
- Leading: manufacturing ISM (below 45 is recession, 45 to 50 a correction), housing starts below 1.1m, market prices, curve inversion.
- Lagging: claims, the Sahm rule, the first negative payroll. Do not trade equities on them. Use the 200dma instead.
- Recession playbook: avoid equities two to three months before and for the first half. Fed cuts are necessary for a bottom. Median SPX drawdown 34%, IG widening 124bp, HY about 785bp.
- Inversion forecasts cuts, not recession. Median lag to the first cut is 18 months, and longer when inflation is high.
- Reduce risk when soft-data momentum falls below hard-data momentum (SPX IR 0.55 to 1.04, data from 2004).

**Geopolitics and elections (Ch 4).** Fade geopolitical shocks fast unless oil is affected. Even oil spikes last a median 38 days. Hedge with energy, then gold. Buy election-driven equity weakness days before the vote and follow the election-day closing move. Treasuries dislike unified governments.

**Rates: the Fed-cycle clock (Ch 5).** Pay about three months before the first hike. Stay paid to the last hike and ignore pauses. Start receiving at the last hike (not if inflation is high). Press receivers three months before the first cut. Exit at the last cut. In a soft landing take profit shortly after the first cut. A strong SPX at the first cut means few cuts.
- Best receive signals: short-leg inversions (6m/2s, 3m/10s), FF6 minus FF1 below -12.5bp. Not 2s/10s.
- Supply belongs in swap spreads, not the curve. Valuation adds little. Trend works with short averages (22d, 55d).
- Trade breakevens, not TIPS, for inflation. TIPS vs nominals when copper is above its 55dma: IR 0.81.

**Rates tactics and global (Ch 6, Ch 7).** Yield peaks pay faster than troughs. Two-year breakevens and 5s/30s lead the 10-year peak. FOMC-day moves of 2 standard deviations follow through. Use CESI as a trend signal (below -25 receive, above 75 pay). Global back ends follow the US. Receive the leaders in a global easing cycle. Trade UST against Bunds, gilts and JGBs only at extremes of FX-hedged pickup. Own FX-hedged EM local when US rates and DXY are both below their 55dma (active IR 2.47).

**Equities (Ch 8 to Ch 10).** Default long. Drawdowns above 20% come from recessions, deflating bubbles, stagflation and accidents.
- 200dma: SPX IR 0.44 to 0.69, half the maximum drawdown. Momentum beats value. CAPE does not time.
- Buy the first Fed pause after the last cut and after the last hike. A monthly rise above 14bp in real yields or 10bp in term premium hurts. Bull flattening is the best curve regime (active IR 0.99), bear flattening the worst (-0.12).
- Fed put: about 25% off the high, 20% with low inflation.
- Earnings revisions (global ERI): long when positive (active IR 0.87 vs 0.17 when negative), buy hard below the 5th percentile (0.73 to 0.83 vs 0.38).
- Bank reserves rising (4-week average): SPX active IR 1.01 vs 0.01 when falling.
- Bubbles: buy on entry (price two standard deviations above real trend), exit when the fourth "general" breaks its 200dma.
- Tactics: POLLS above 18 for two days is the sell signal. The volatility risk premium above 2 standard deviations is the best dip signal (active IR almost 1.1). Fade leveraged CFTC extremes (active IR 1.37 below -2, -0.80 above 2). Hold November to April (0.71 vs 0.48).
- Country selection expresses macro views: Japan for the cycle, higher rates and a weak JPY. Strong USD favours Japan and the UK. Weak USD favours EM.

**Credit (Ch 11).** Trade spread returns separately from duration. Credit is equity-like with capped upside and negative skew.
- Hold spread risk when the maximum cross-asset volatility z-score is below 2 (IR 1.11 vs 0.42) and when the last SLOOS showed loosening (IR 1.10 vs 0.46).
- Credit does not rally into the first cut and is unattractive late cycle.
- Spread level predicts returns in HY, barely in IG. HY beats IG risk-adjusted when the ISM is above 50.
- Ba has the best IR because of fallen angels. Buy them. Rising stars are done by the upgrade.
- Ignore supply forecasts. Loans beat HY in hiking cycles. EM credit beats US IG when DXY is below its 55dma.
- Credit warns for equities: spreads are tightest about 12 months before a recession, the SPX peaks about 6 months before. A VIX jump with already-wider HY spreads is the cut signal (active IR 0.94).

**FX (Ch 12, Ch 13).** The USD "smile" is a smirk: reliable strength only when growth is weak. Single drivers have low IRs. Bear steepening is the most USD-bullish curve regime (active IR 0.86). Trade EUR when BTP-Bund spread, relative equities, relative data change and the five-year differential all agree (active IR 1.75). Keep volatility-adjusted EM carry on by default (IR 0.89). Cut it on a falling USDJPY or a volatility spike with crowded positioning. The USD falls about 4% in the three months before the first cut and rebounds in soft landings. Intervention works only when fundamentals turn.

**Commodities (Ch 14).** Not buy-and-hold. Long in hiking cycles and unaddressed inflation, short into recessions. Copper follows global data momentum (active IR 1.06). Gold follows the Fed and the USD, not CPI (CPI filters give active IR 0.16 to 0.21 vs 0.15). Oil needs ISM, curve shape, OPEC-day price action and positioning together. Carry (backwardation) and trend both work.

**Allocation (Ch 15, Ch 16).** 60/40 and risk parity fail in stagflation. The stock-bond correlation turns positive with core CPI above 2.5%. Once the Fed hikes, gold, TIPS and Bitcoin stop hedging inflation. CTAs, carry and quality hold up. A 50/30/10/5/5 mix (equities, bonds, CTAs, quality, carry) has IR 0.68 vs 0.55 for 60/40. Switch equities, bonds and bills on the 200dma. Do not fade CTA positioning. Bitcoin is a liquidity-driven tech proxy. Unsmoothed private equity and credit are mostly equity beta.

---

## Chapter Index

| # | Title | Key Frameworks |
|---|-------|----------------|
| [ch01](chapters/ch01-introduction.md) | Introduction | Method creates conviction, markets not forward-looking, chapter map |
| [ch02](chapters/ch02-global-macro-rules.md) | Global Macro Rules | Macro fund attribution, four reasons for a bright future, backtest conventions |
| [ch03](chapters/ch03-business-cycle.md) | It's the Business Cycle, Stupid | Five regimes, leading vs lagging indicators, recession playbook, financial accident trigger |
| [ch04](chapters/ch04-geopolitics-and-politics.md) | Temporary Turmoil: Markets and (Geo)Politics | GPR spikes, oil test, tariff playbook, election rules |
| [ch05](chapters/ch05-rates-framework.md) | How to Trade Rates: A Framework | Fed-cycle clock, inversion signals, curve rules, supply, TIPS and breakevens |
| [ch06](chapters/ch06-rates-tactics.md) | How to Trade Rates: The Tactics | Anatomy of a sell-off, FOMC and NFP momentum, CESI trend rule |
| [ch07](chapters/ch07-rates-globalizing.md) | How to Trade Rates: Globalizing | Leaders vs laggards, FX-hedged carry, periphery rule, EM local grid |
| [ch08](chapters/ch08-equities-framework.md) | How to Trade Equities: A Framework | Drawdown taxonomy, Fed turning points, ERI, reserves, bubbles, generals rule |
| [ch09](chapters/ch09-equities-tactics.md) | How to Trade Equities: The Tactics | POLLS, VRP model, positioning, insiders, seasonals, news regimes |
| [ch10](chapters/ch10-equities-globalizing.md) | How to Trade Equities: Globalizing | Cyclicality and FX sensitivity, Japan, Germany, UK, China, EM rules |
| [ch11](chapters/ch11-credit.md) | How to Trade Credit | SLOOS rule, max-volatility cut-out, fallen angels, supply fallacy, credit canary |
| [ch12](chapters/ch12-fx-framework.md) | How to Trade FX: The Framework | USD smirk, EUR composite model, JPY, carry construction, value, momentum |
| [ch13](chapters/ch13-fx-tactics.md) | How to Trade FX: The Tactics | USD around Fed events, intervention, flows, intraday reversals |
| [ch14](chapters/ch14-commodities.md) | How to Trade Commodities | Roll yield, carry and trend, supply checklist, copper, gold, oil rules |
| [ch15](chapters/ch15-how-to-allocate.md) | How to Allocate | Regime clusters, stagflation hedges, regime-agnostic SAA, 200dma switch, volatility targeting |
| [ch16](chapters/ch16-private-assets-and-crypto.md) | Non Traditional Assets: Private Assets and Crypto | Bitcoin reverse optimization, trend rule, unsmoothing private returns |

## Topic Index

- **200dma / moving averages** → ch03, ch08, ch15
- **Allocation, 60/40, risk parity** → ch15
- **Backtest conventions** → ch01, ch02
- **Bank reserves and liquidity** → ch08
- **Bitcoin** → ch16, ch15
- **Breakevens and TIPS** → ch05, ch06
- **Bubbles and the generals rule** → ch08, ch12
- **Bunds, gilts, JGBs** → ch07
- **Carry (FX)** → ch12
- **Carry (commodities, fixed income)** → ch14, ch07
- **CESI / data surprises** → ch06, ch09, ch12
- **China** → ch03, ch07, ch10, ch14
- **Copper and copper/gold** → ch14, ch05
- **Credit spreads, IG vs HY** → ch11, ch03
- **Credit as equity warning or hedge** → ch11, ch15
- **CTAs and positioning** → ch15, ch09, ch02
- **Curve (flatteners, steepeners, inversion)** → ch05, ch03, ch12
- **Defaults and SLOOS** → ch11
- **Earnings revisions (ERI)** → ch08, ch10
- **Elections** → ch04
- **EM rates, credit, equities, FX** → ch07, ch11, ch10, ch12
- **Fallen angels and rising stars** → ch11
- **Fed cycle (first/last hike, first/last cut)** → ch05, ch08, ch11, ch13, ch14
- **Fed put** → ch08
- **Financial accidents** → ch03
- **FOMC-day and payroll-day rules** → ch06, ch09
- **Geopolitics and tariffs** → ch04
- **Gold** → ch14, ch04, ch15
- **Inflation hedges and stagflation** → ch15, ch14, ch16
- **Intervention (FX)** → ch13
- **ISM / PMI rules** → ch03, ch08, ch10, ch11, ch14
- **Japan and JPY** → ch07, ch10, ch12, ch13
- **Leveraged loans and private credit** → ch11, ch16
- **Oil and OPEC** → ch14, ch04, ch05
- **POLLS, VRP, VIX, sentiment** → ch09
- **Private assets** → ch16
- **Recession playbook** → ch03, ch08, ch11, ch14
- **Regimes (macro)** → ch03, ch15
- **Seasonals** → ch09, ch06, ch10
- **Soft vs hard landing** → ch03, ch05, ch08, ch13
- **Supply (bonds, credit)** → ch05, ch11
- **USD frameworks** → ch12, ch13
- **Valuation vs momentum** → ch08, ch15, ch05
- **Volatility cut-out and targeting** → ch11, ch12, ch15

## Supporting Files

- [glossary.md](glossary.md) — all key terms with definitions
- [patterns.md](patterns.md) — all techniques and design patterns
- [cheatsheet.md](cheatsheet.md) — quick reference tables and decision guides
- Full text: `/home/ak/.local/share/book-to-skill/fulltext/willer-trading-global-macro/full_text.txt` — grep it for depth the chapter files omit (local extraction, not shipped)

---

## Scope & Limits

This skill covers the book content only. For hands-on implementation in your codebase,
combine with project-specific tools. For topics beyond this book, check related skills
or ask the agent directly.

The extraction has 318 image placeholders. Most are charts, and many charts carry a small statistics table (return, volatility, active IR) that did not extract. About 58 PDF pages were used to recover them: all of Chapter 11, and the charts where a stated rule lacked its number in Chapters 5 to 10 and 12 to 15. Each recovered table is marked with its PDF page. The charts still unread are listed in each chapter's Extraction Notes, and their headline figures come from the prose. Each chapter file ends with Extraction Notes listing gaps, garbled passages and places where the source contradicts itself.
