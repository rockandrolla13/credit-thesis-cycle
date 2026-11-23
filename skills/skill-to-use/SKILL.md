---
name: skill-to-use
description: "Index of the macro and credit book library. Use when the user asks which skill, book or author to use for a question, asks what the library covers, or asks a macro, credit, Fed, currency, sovereign-debt, inflation or geopolitics question without naming a skill. Routes to two topic skills (credit-cycle, fed-rate-hike) twenty-five book skills and five paper skills."
---

# Skill to Use

This skill holds no book content. It picks the skill that answers the question.

## How to Use

1. Read the user's question.
2. Match it to one row in "Pick by Question".
3. Name the skill, and say in one sentence why it fits.
4. If the user asked a real question, load that skill and answer from it.
5. If two rows fit, prefer the topic skill. It compares the authors for you.
6. If no row fits, say the library does not cover the question. Do not answer from general knowledge under a book's name.

## Three Rules of Thumb

- **Several authors, one topic** -> a topic skill (`credit-cycle` or `fed-rate-hike`).
- **One author's method, in depth** -> that author's book skill.
- **A past episode as an example** -> a book marked "case". Do not load case material for fresh theme reasoning.

## Pick by Question

| The question is about | Use | Why |
|---|---|---|
| Credit booms, warning signs, busts, deleveraging, spreads through the cycle | `credit-cycle` | Compares twenty-one sources by cycle phase |
| Fed hikes: first hike, last hike, pause, hike-to-cut gap, by asset class | `fed-rate-hike` | Compares market rules with how the Fed decides |
| A trade rule for rates, curve, FX carry, commodities, or allocation by regime | `willer-trading-global-macro` | Backtested rules by business-cycle stage |
| How the Fed sets policy, operating targets, chairman and FOMC behaviour | `axilrod-inside-the-fed` | Insider account, Martin to Bernanke |
| Where a country sits in a debt cycle, deflationary or inflationary route | `dalio-big-debt-crises` | Archetype template plus 48 cases |
| Whether a government's debt is sustainable, monetisation, devaluation | `dalio-how-countries-go-broke` | Debt arithmetic and nine-stage sequence |
| Private sector paying down debt, zero rates not working, Japan | `koo-balance-sheet-recession` | Balance sheet recession framework |
| Predicting a crisis from credit growth, long-run statistics | `schularick-taylor-credit-booms` | 1870-2008 panel and early-warning model |
| Bank funding stress, loan/deposit ratio, bank leverage | `schulte-credit-driven-economy` | Simple bank balance-sheet gauges |
| Why 2007-09 happened across countries, contagion channels | `claessens-financial-globalization` | Cross-country causes |
| Bubbles, the financial accelerator, should the central bank lean or clean | `hayford-malliaris-asset-prices-crisis` | Theory and policy survey |
| Why markets misprice, herding, Minsky, incentives | `cassidy-how-markets-fail` | Market-failure logic and the subprime chain |
| Currency crises, capital flows, sudden stops, capital controls, contagion | `eichengreen-capital-flows-crises` | Emerging-market and EMS evidence |
| Euro-area sovereign stress, Greece and Ireland, restructuring | `christodoulakis-european-periphery-debt-crisis` | Periphery crisis in detail |
| Hyperinflation, currency collapse, stabilisation | `bresciani-turroni-economics-of-inflation` | Germany 1914-1931 |
| Elections, wars, policy constraints, political forecasting | `papic-geopolitical-alpha` | Constraint-based framework |
| Game theory, causal models, machine learning for macro views | `simonian-computational-global-macro` | Quantitative methods |
| Trading through a panic, option structures, sizing and drawdown rules | `gurevich-trades-of-march-2020` | A trader's log of March 2020 |
| Who owns, lends to and loses on AI data-centre debt; how AI debt news moved Treasury yields and IG spreads | `bis-building-ai-on-credit` | BIS loss map and the only event study, October 2026 |
| Size of AI investment and debt supply, campus cost, leases, special-purpose vehicles, vendor financing, revenue the build needs | `van-nieuwerburgh-financing-ai-buildout` | Supply arithmetic and one worked deal, October 2026 |
| How far a bond price moves when demand or supply shifts, one bond against a rating group, how long it lasts | `chaudhary-corporate-bond-multipliers` | Measured price multipliers at five levels |
| Size of private credit, bank credit lines to lending funds, loss if the lines are drawn | `fed-bank-lending-to-private-credit` | Fed data, method and stress arithmetic |
| Which issuer variables predict failure, and at what horizon | `campbell-in-search-of-distress-risk` | Tested failure model with coefficients |
| What a credit spread pays after defaults; whether private or illiquid assets pay more; limits of market timing | `ilmanen-investing-amid-low-expected-returns` | Expected-return arithmetic by asset class |
| What an asset class or portfolio bets on (growth, inflation); whether a rate move is already in the curve | `shahidi-balanced-asset-allocation` | Growth and inflation bias grid |
| Whether a signal really predicts returns; turning views or rankings into expected returns | `satchell-forecasting-expected-returns` | Predictability tests and Black-Litterman |
| Macro scenarios, reading a central bank, leverage and stop-loss rules, strategies that hide loss risk | `rozanov-global-macro-theory-practice` | Practitioner chapters, 2012 |
| Crowded positions, forced sellers, carry as hidden loss risk, in managers' own words | `drobny-inside-the-house-of-money` | Interviews from 2004-2005 |
| Lessons of 2008 for a large portfolio: liquidity, hidden leverage, cheap protection, a credit-bubble test | `drobny-invisible-hands` | Interviews from 2009 |
| Issuer warning signs from equity filings; merger, insider, buyback and spin-off signals | `suria-event-driven-edge` | Event base rates and screens |
| Whether cheap money caused bad or riskier investment | `cowen-risk-and-business-cycles` | Lists what the claim needs to hold |
| Reserve-currency decline, conflict between the US and China, political breakdown inside a country | `dalio-changing-world-order` | Long-cycle template, 2020 draft |

## Pick by Type of Help

| You want | Use |
|---|---|
| A rule you can test on data | `willer-trading-global-macro`, `schularick-taylor-credit-booms`, `schulte-credit-driven-economy`, `campbell-in-search-of-distress-risk`, `chaudhary-corporate-bond-multipliers`, `ilmanen-investing-amid-low-expected-returns`, `satchell-forecasting-expected-returns`, `suria-event-driven-edge` |
| A framework for reasoning about cause | `dalio-big-debt-crises`, `koo-balance-sheet-recession`, `cassidy-how-markets-fail`, `papic-geopolitical-alpha`, `hayford-malliaris-asset-prices-crisis`, `van-nieuwerburgh-financing-ai-buildout`, `cowen-risk-and-business-cycles`, `shahidi-balanced-asset-allocation`, `rozanov-global-macro-theory-practice`, `dalio-changing-world-order` |
| A historical analogue (case memory) | `gurevich-trades-of-march-2020`, `bresciani-turroni-economics-of-inflation`, `christodoulakis-european-periphery-debt-crisis`, `axilrod-inside-the-fed` ch02-07, `eichengreen-capital-flows-crises` ch02 and ch07-09, `drobny-inside-the-house-of-money`, `drobny-invisible-hands`, `dalio-changing-world-order` ch04-07, `van-nieuwerburgh-financing-ai-buildout` sec04 and sec09 |
| A view from the central bank's side | `axilrod-inside-the-fed`, `hayford-malliaris-asset-prices-crisis`, `bis-building-ai-on-credit`, `fed-bank-lending-to-private-credit` |
| A disagreement between authors | `credit-cycle` or `fed-rate-hike`, section "Points to Compare" |

## Tools, Not Books

| You want | Use |
|---|---|
| 4 to 5 scenarios for IG, HY, each rating tier and each sector | `credit-scenario-grid` |
| One thesis memo from all evidence and every skill | `thesis-builder` |

## Trust Notes

- `bresciani-turroni-economics-of-inflation` is a scan. Trust only tables marked "checked against PDF".
- The Dalio and Cassidy skills lost most charts. Trust the text, not chart readings.
- `koo-balance-sheet-recession` and `schulte-credit-driven-economy` are single-chapter excerpts.
- Willer and Saunders' numbers are backtests. Several rules failed in the 2022-2023 cycle.
- Each skill added on 2026-11-23 has its own "Method or Case" and "Trust Notes" sections in its SKILL.md. Read them before you cite a chapter. Use only METHOD chapters for fresh reasoning.
- The nine books added on 2026-11-23 lost all or most charts and several tables. Trust the text.
- `dalio-changing-world-order` is the 2020 draft. The last chapter and the country ratings are absent.
- `satchell-forecasting-expected-returns` lost Greek letters and many decimals. Check a formula against the book.
- `rozanov-global-macro-theory-practice` ch08 gives claims without proof. Do not use it as method.
- `drobny-inside-the-house-of-money` and `drobny-invisible-hands` are interviews. A manager's rule is that manager's opinion.
- `bis-building-ai-on-credit` tests 18 days and reports an association, not a cause.
- `chaudhary-corporate-bond-multipliers` measures fund-flow shocks, not issuance. It gives no AA or BBB multiplier.
- `campbell-in-search-of-distress-risk` is the 2006 working paper. Its sample ends in 2003.
- `fed-bank-lending-to-private-credit` holds two notes that disagree on bank loans to lending funds. Do not join the series.

## Scope and Limits

The library is strong on credit cycles, Fed tightening, sovereign debt and currency crises.
Five papers cover AI debt financing, private credit, bond price pressure and issuer failure, up to October 2026.
It is thin on quantitative tightening, equity valuation and China. No book covers anything after March 2025.
`credit-cycle` compares eight of the sources added on 2026-11-23. `fed-rate-hike` does not compare them yet.
All skills live in `/home/ak/.agents/skills/`.
