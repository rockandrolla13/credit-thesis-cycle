---
name: fed-rate-hike
description: "Cross-book router for Fed hiking-cycle questions: positioning before the first hike, during the cycle, at pauses, at the last hike, and in the gap between the last hike and the first cut, across rates, curve, equities, credit, FX, commodities and allocation. Use when a question on Fed hikes, tightening cycles, the last hike or the hike-to-cut interval should be answered from several books at once (Willer and Saunders for market rules, Axilrod for how the Fed decides, with Dalio, Cassidy, Eichengreen, Gurevich, Koo and Hayford and Malliaris), or when comparing what those authors say."
---

<!-- argument-hint: [hiking-cycle question, stage name, or asset class] -->

# Fed Rate Hike (topic router)

**Type**: topic skill. It holds no book content. It routes a question to the right
chapters of the book skills, then requires a per-author answer.
**Generated**: 2026-11-22 (five books added the same day)

All paths below are relative to `/home/ak/.agents/skills/`.

**Coverage note.** Two books carry most of this topic. Willer and Saunders give the
market rules: what assets do around hikes. Axilrod gives the policy side: how the Fed
decides to tighten and when it stops. A market-rule answer often rests on Willer and
Saunders alone. Say so when it happens.

## How to Answer With This Skill

1. Place the question on the stage map below. Then pick the asset class.
2. Read the listed chapter files. Read at most five files before the first answer.
3. Answer author by author. Give each claim its author and chapter, for example
   "(Willer and Saunders, ch05)".
4. State where the authors agree. State where they differ. Do not settle a difference.
5. If no listed chapter covers the question, say so. Do not fill the gap from general knowledge.

## Rules

- **Attribute every claim.** No blended statements.
- **Report conflicts, do not resolve them.**
- **Read every Willer and Saunders number as a backtest.** The authors assume zero
  transaction costs, accept small samples and do not separate in-sample from
  out-of-sample. See `willer-trading-global-macro/chapters/ch02-global-macro-rules.md`.
- **Read numbers with care.** A number is checked only when the chapter marks it
  "recovered from PDF p. N" or "checked against PDF p. N".
- **Flag the 2022-2023 cycle.** The authors record several rules that failed in that
  cycle. Always report the failure next to the rule.
- **Keep method and case apart.** Rows marked **(case)** are historical accounts of one
  era or episode. Do not load them for fresh theme reasoning in the creditmacro engine.
  Use them for a historical example, or in the analogue step after fresh reasoning is
  frozen. Unmarked rows are how-to-reason material. Axilrod's era chapters each hold a
  "Frameworks Introduced (general method)" block and a separate "Dated Episodes" block.
  Gurevich mixes method and case. See the Gurevich section below.

## Stage Map

Use these stage names in the answer. They follow the Fed-cycle clock in Willer and
Saunders ch05.

1. **Before the first hike** (from the last cut to the first hike)
2. **First hike**
3. **Inside the cycle** (first hike to last hike, including pauses and step-downs)
4. **Last hike**
5. **Hike-to-cut gap** (last hike to first cut)

## Router by Asset Class

### Rates and the curve

| Question | Read |
|---|---|
| The Fed-cycle clock: when to pay, when to receive, how to treat pauses | `willer-trading-global-macro/chapters/ch05-rates-framework.md` |
| Curve shape in hiking cycles, flatteners, cash versus duration | `willer-trading-global-macro/chapters/ch05-rates-framework.md` |
| Breakevens and TIPS around hikes | `willer-trading-global-macro/chapters/ch05-rates-framework.md` |
| Worked example of the 2022-2023 cycle, which rules held and which broke | `willer-trading-global-macro/chapters/ch05-rates-framework.md` |
| FOMC-day and payroll-day moves inside a hiking cycle | `willer-trading-global-macro/chapters/ch06-rates-tactics.md` |
| Other central banks: leaders, laggards, the BoJ, spread trades by relative policy | `willer-trading-global-macro/chapters/ch07-rates-globalizing.md` |
| Curve inversion during a hiking cycle, the 2022 false signal | `willer-trading-global-macro/chapters/ch03-business-cycle.md` |
| A flat long end during tightening as a sign of weak loan demand | `koo-balance-sheet-recession/chapters/ch01-america-subprime-fiasco.md` |

### Equities

| Question | Read |
|---|---|
| Equities around the first hike and the last hike, the Fed put, real-yield rises | `willer-trading-global-macro/chapters/ch08-equities-framework.md` |
| Hikes as a condition for a bubble peak, the internet-bubble example | `willer-trading-global-macro/chapters/ch08-equities-framework.md` |
| Bear markets that end while the Fed is still hiking | `willer-trading-global-macro/chapters/ch03-business-cycle.md` |

### Credit

| Question | Read |
|---|---|
| Credit around the last hike, loans versus HY while the Fed hikes | `willer-trading-global-macro/chapters/ch11-credit.md` |
| Bank lending standards during a tightening cycle, the 2021-2023 example | `willer-trading-global-macro/chapters/ch11-credit.md` |

For the wider credit cycle, use the `credit-cycle` topic skill.

### FX, commodities and allocation

| Question | Read |
|---|---|
| FX volatility and carry late in a hiking cycle | `willer-trading-global-macro/chapters/ch12-fx-framework.md` |
| The USD around Fed events | `willer-trading-global-macro/chapters/ch13-fx-tactics.md` |
| Commodity returns over hiking cycles, gold once the Fed hikes | `willer-trading-global-macro/chapters/ch14-commodities.md` |
| Inflation hedges under a hiking Fed, the "tightening financial conditions" regime | `willer-trading-global-macro/chapters/ch15-how-to-allocate.md` |
| Bitcoin once the Fed hikes | `willer-trading-global-macro/chapters/ch16-private-assets-and-crypto.md` |

### How the Fed decides to tighten, and when it stops

| Question | Read |
|---|---|
| How policy is managed: the chairman, the FOMC, the staff, independence | `axilrod-inside-the-fed/chapters/ch01-overview-policy-management-and-managers.md` |
| The Fed's credibility and how it communicates | `axilrod-inside-the-fed/chapters/ch08-fed-and-its-image.md` |
| Axilrod's scorecard of chairmen, the neutral rate as a guess, the asset-bubble dilemma | `axilrod-inside-the-fed/chapters/ch09-concluding-remarks.md` |
| Chronology of chairmen, indicator charts 1960-2009 (values read by eye) | `axilrod-inside-the-fed/chapters/ch10-appendices-chronology-and-indicators.md` |
| **(case)** Martin: rate control versus money control, timing asymmetry | `axilrod-inside-the-fed/chapters/ch02-in-bill-martins-time.md` |
| **(case)** Burns: tightening too little, the real funds rate test | `axilrod-inside-the-fed/chapters/ch03-arthur-burns-struggle-against-inflation.md` |
| **(case)** Miller | `axilrod-inside-the-fed/chapters/ch04-miller-interlude.md` |
| **(case)** Volcker: the 1979 change of procedure, sticking to it | `axilrod-inside-the-fed/chapters/ch05-paul-volcker-victory-over-inflation.md` |
| **(case)** Greenspan: forward guidance, the Greenspan put, asset inflation | `axilrod-inside-the-fed/chapters/ch06-greenspan-years-stability-to-crisis.md` |
| **(case)** Bernanke: crisis stages and exit tools | `axilrod-inside-the-fed/chapters/ch07-bernanke-great-credit-crisis.md` |

### Hikes inside the long debt cycle

| Question | Read |
|---|---|
| Tightening as the trigger at the top of a bubble | `dalio-big-debt-crises/chapters/ch02-deflationary-cycle-early-bubble-top.md` |
| Rate policy (MP1) and when it stops working | `dalio-big-debt-crises/chapters/ch04-beautiful-deleveraging-pushing-on-a-string-normalization.md` |
| Raising rates to defend a currency | `dalio-big-debt-crises/chapters/ch05-inflationary-depressions-and-currency-crises.md` |
| Policy regimes MP0 to MP3, where rate hikes sit | `dalio-how-countries-go-broke/chapters/ch01-big-debt-cycle-in-a-nutshell.md` |
| Tight versus easy money matrix, the real yield anchor | `dalio-how-countries-go-broke/chapters/ch10-big-debt-cycle-1945-to-now.md` |
| **(case)** 1971 to 2008: the interest-rate-driven era, the dollar squeeze | `dalio-how-countries-go-broke/chapters/ch12-1971-to-2008-fiat-interest-rate-driven.md` |
| **(case)** The 1937 tightening | `dalio-big-debt-crises/chapters/ch08-case-us-debt-crisis-and-adjustment-1928-1937.md` |
| **(case)** A rate-shock stress test for the Bank of Japan | `dalio-how-countries-go-broke/chapters/ch16-japanese-case-and-lessons.md` |

### Effects abroad

| Question | Read |
|---|---|
| US and global financial conditions as a driver of capital flows to borrowers | `eichengreen-capital-flows-crises/chapters/ch02-a-century-of-capital-flows.md` |
| **(case)** Rising rates in the lending centre and the Baring and Mexican crises | `eichengreen-capital-flows-crises/chapters/ch07-baring-crisis-in-a-mexican-mirror.md` |

### Policy background

| Question | Read |
|---|---|
| Fed overtightening as a recession cause, history of recession causes | `willer-trading-global-macro/chapters/ch03-business-cycle.md` |
| The asymmetric Fed response to asset prices (Greenspan doctrine) | `hayford-malliaris-asset-prices-crisis/chapters/ch01-introduction-great-moderation.md` |
| The Taylor rule as a policy guide | `hayford-malliaris-asset-prices-crisis/chapters/ch04-policies-and-conclusions.md` |
| Taylor's claim that easy money caused the housing bubble | `hayford-malliaris-asset-prices-crisis/chapters/ch03-financial-crisis-2007-09.md` |
| Monetarism, the natural rate, Friedman and Schwartz | `cassidy-how-markets-fail/chapters/ch06-the-evangelist.md` |
| **(case)** Greenspan's choices, cheap money, the Taylor rule critique | `cassidy-how-markets-fail/chapters/ch17-greenspan-shrugs.md` |

## Gurevich: method and case

`gurevich-trades-of-march-2020` is a trading diary. Two chapters bear on hikes.

**General claims about Fed behaviour** (usable as method, attributed to Gurevich):

- The Fed's consistent response system, the six-step cycle-end script, the short
  hike-to-ease interval, and the claim that the Fed surprises with eases and not hikes:
  `gurevich-trades-of-march-2020/chapters/ch02-the-pivot.md`
- The inflation-fear regime and late-cycle indicators:
  `gurevich-trades-of-march-2020/chapters/ch01-the-fateful-contract.md`

**His own positions and outcomes** in the same chapters are case memory. Do not load
them for fresh theme reasoning in the creditmacro engine. Use them only when the user
asks for a historical example, or in the analogue step after fresh reasoning is frozen.

## Points to Compare

Read both sides before answering. These are open questions, not conclusions.

1. **How long is the hike-to-cut gap?** Willer and Saunders ch05 give a median pause.
   Gurevich ch02 gives a table of last hike to first ease. Report both, with ranges.
2. **Receive at the last hike?** Willer and Saunders ch05 state the rule and record that
   it failed in 2023 with high inflation. Gurevich ch02 argues the market is slow to
   price the first cut. Check whether the two agree on timing.
3. **Hikes that the market prices but the Fed never delivers.** Compare Willer and
   Saunders ch05 on the market pricing hikes that do not come with Gurevich ch02 on
   fading a small priced chance of a hike.
4. **Does inversion during a hiking cycle mean recession?** Willer and Saunders ch03
   treat inversion as a forecast of cuts and record the 2022 failure. Koo ch01 offers a
   different reading of a flat long end.
5. **What makes the Fed stop hiking?** Axilrod (ch01, ch09 and the era chapters) describes
   the decision from inside. Willer and Saunders ch05 infer it from market history.
   Gurevich ch02 gives a six-step script. Report all three.
6. **Should the Fed hike against asset prices?** Compare Axilrod ch09, Dalio (Big Debt
   Crises ch02, ch12), Cassidy ch17 and Hayford and Malliaris ch04.
7. **Is a hike the cause of the bust or only the trigger?** Dalio (Big Debt Crises ch02)
   treats tightening as what pops the bubble. Compare with Willer and Saunders ch03 on
   recession causes.
8. **Do hikes end bubbles?** Compare Willer and Saunders ch08 on peak conditions with
   Hayford and Malliaris ch01 and ch04 on whether policy should respond to asset prices.

## Scope and Limits

- This skill covers hiking cycles. Easing cycles appear only as the end point of the
  hike-to-cut gap. Willer and Saunders ch05 covers easing in full.
- The chapter notes say little about balance sheet policy (QT). Do not infer it. The nearest material is bank reserves and equities in Willer and Saunders ch08.
- The sources are US-centred. Other central banks appear only in Willer and Saunders ch07.
- It is an index. If a book skill changes, check that the paths here still exist.
- Full extracted text sits at `/home/ak/.local/share/book-to-skill/fulltext/<book-skill>/full_text.txt`.
  Search it when a chapter file is too thin.
- Related topic skill: `credit-cycle`.
