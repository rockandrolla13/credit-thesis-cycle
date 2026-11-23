---
name: credit-cycle
description: "Cross-book router for credit-cycle questions: credit booms, crisis warning signs, crisis mechanics, deleveraging and balance sheet recessions, policy response, the bank-sovereign loop, and trading credit spreads through the cycle. Use when a question on credit booms, busts, leverage or spreads should be answered from several books at once (Schularick and Taylor, Koo, Schulte, Hayford and Malliaris, Claessens, Willer and Saunders, Christodoulakis, Dalio, Cassidy, Eichengreen, Axilrod, Bresciani-Turroni, Cowen, Ilmanen, Campbell, Chaudhary, the BIS and Van Nieuwerburgh on AI debt, the Fed on private credit), or when comparing what those authors say."
---

<!-- argument-hint: [credit-cycle question, phase name, or "compare <author> vs <author>"] -->

# Credit Cycle (topic router)

**Type**: topic skill. It holds no book content. It routes a question to the right
chapters of twenty-one book and paper skills, then requires a per-author answer.
**Generated**: 2026-11-22 (six books added the same day). Eight sources added 2026-11-23.

All paths below are relative to `/home/ak/.agents/skills/`.

## How to Answer With This Skill

1. Match the question to a phase in the Router below. A question may match two phases.
2. Read the listed chapter files. Read at most five files before the first answer.
3. Answer author by author. Give each claim its author and chapter, for example
   "(Schularick and Taylor, ch04)".
4. State where the authors agree. State where they differ. Do not settle a difference.
5. If no listed chapter covers the question, say so. Do not fill the gap from general knowledge.

## Rules

- **Attribute every claim.** No blended statements such as "the literature says".
- **Report conflicts, do not resolve them.** The disagreement is the useful output.
- **Read numbers with care.** A number is checked only when the chapter marks it
  "recovered from PDF p. N". Other numbers may carry digit errors from extraction.
- **Read each chapter's Extraction Notes** before quoting a table from it.
- **Respect the source type.** Schularick and Taylor is an empirical paper. Koo, Schulte
  and Claessens are single chapters of larger books. Willer and Saunders report
  backtests with zero transaction costs assumed. The five papers added on 2026-11-23
  use `secNN` files, not `chNN`. Chaudhary measures fund-flow shocks, not new issuance.
  The BIS, Van Nieuwerburgh and Fed sources hold dated numbers on one live episode.
- **Keep method and case apart.** Rows marked **(case)** are historical case studies of
  one episode. Do not load them for fresh theme reasoning in the creditmacro engine. Use
  them for a historical example, or in the analogue step after fresh reasoning is frozen.
  Unmarked rows are how-to-reason material. Each book skill's "Scope & Limits" gives its
  own split. The Gurevich diary is case memory and is listed at the end.

## Router

### Phase 1. The boom: how credit builds up

| Question | Read |
|---|---|
| Does credit growth cause crises, or only spread them? The three views | `schularick-taylor-credit-booms/chapters/ch01-introduction-three-views-research-questions.md` |
| How bank balance sheets changed over the long run, leverage, wholesale funding | `schularick-taylor-credit-booms/chapters/ch02-data-and-two-eras-of-finance-capitalism.md` |
| Minsky's five stages, the leverage cycle, collateral, the financial accelerator | `hayford-malliaris-asset-prices-crisis/chapters/ch02-general-characteristics-of-financial-crises.md` |
| What 2007-09 shared with earlier booms: credit booms, house prices, lending standards | `claessens-financial-globalization/chapters/ch01-commonalities-with-previous-crises.md` |
| The loan/deposit ratio through the cycle, its link to the current account | `schulte-credit-driven-economy/chapters/ch02-loan-deposit-ratio.md` |
| Why standard economic models missed credit | `schulte-credit-driven-economy/chapters/ch01-credit-blind-spot.md` |
| The euro-area build-up: imbalances and spreads | `christodoulakis-european-periphery-debt-crisis/chapters/ch01-genesis-eurozone-sovereign-debt-crisis.md` |
| Dalio's template: productive credit test, the seven stages, the bubble checklist | `dalio-big-debt-crises/chapters/ch02-deflationary-cycle-early-bubble-top.md` |
| How credit and debt drive the cycle, the two types of crisis | `dalio-big-debt-crises/chapters/ch01-credit-debt-and-the-big-debt-cycle-template.md` |
| Minsky's hedge, speculative and Ponzi finance | `cassidy-how-markets-fail/chapters/ch16-hyman-minsky-and-ponzi-finance.md` |
| Why rational lenders join a boom: herding, limits to arbitrage | `cassidy-how-markets-fail/chapters/ch14-the-rational-herd.md` |
| Rational irrationality and the prisoner's dilemma | `cassidy-how-markets-fail/chapters/ch11-the-prisoners-dilemma-and-rational-irrationality.md` |
| Cross-border lending booms over a century, what drives capital inflows | `eichengreen-capital-flows-crises/chapters/ch02-a-century-of-capital-flows.md` |
| A boom as a rational move to riskier, longer projects when risk gets cheaper | `cowen-risk-and-business-cycles/chapters/ch02-risk-based-theory-real-terms.md` |
| How new money and easier finance shift the mix of investment toward risk | `cowen-risk-and-business-cycles/chapters/ch03-risk-based-theory-monetary-terms.md` |
| What the "cheap money causes overinvestment" claim must assume | `cowen-risk-and-business-cycles/chapters/ch04-traditional-austrian-critique.md` |
| The long-term debt cycle: credit is stimulative when given, depressing when repaid | `dalio-changing-world-order/chapters/ch02-money-credit-debt-cycle.md` |
| An investment boom that moves from cash flow to debt: the pricing gap test, the boom comparison | `bis-building-ai-on-credit/chapters/sec04-companion-bulletin-120-cash-flows-to-debt.md` |
| Sizing a physical capital boom from the rack up, as a share of GDP | `van-nieuwerburgh-financing-ai-buildout/chapters/sec02-physical-capital-boom.md` |
| The capital-stack map: who owns the assets, who carries the leverage | `van-nieuwerburgh-financing-ai-buildout/chapters/sec03-ownership-and-financing.md` |
| When opening the capital account helps or hurts, sequencing | `eichengreen-capital-flows-crises/chapters/ch04-when-does-liberalization-help.md` |
| **(case)** The US housing boom | `cassidy-how-markets-fail/chapters/ch18-the-lure-of-real-estate.md` |
| **(case)** Scale of the AI credit boom, as of October 2026 | `bis-building-ai-on-credit/chapters/sec01-ai-credit-boom-scale.md` |
| **(case)** Canals, railroads, telecom and AI as capex over GDP | `van-nieuwerburgh-financing-ai-buildout/chapters/sec09-appendix-c-historical-booms.md` |

### Phase 2. Warning signs: what predicts the turn

| Question | Read |
|---|---|
| Crisis prediction model, credit versus money as predictor, out-of-sample test | `schularick-taylor-credit-booms/chapters/ch04-credit-booms-and-crisis-prediction.md` |
| Do asset prices, investment booms or financial depth add information? | `schularick-taylor-credit-booms/chapters/ch05-robustness-asset-prices-financial-depth-conclusions.md` |
| Trigger levels for the loan/deposit ratio and tangible leverage | `schulte-credit-driven-economy/chapters/ch04-tangible-leverage-and-deleveraging-arithmetic.md` |
| Bank share prices as an indicator, the Rule of 1 and 20 | `schulte-credit-driven-economy/chapters/ch05-bailouts-public-debt-rule-of-1-and-20.md` |
| Credit spreads as a warning for equities ("credit canary"), lending-survey rule | `willer-trading-global-macro/chapters/ch11-credit.md` |
| Leading versus lagging recession indicators, where to look for the next accident | `willer-trading-global-macro/chapters/ch03-business-cycle.md` |
| Bank leverage ratio and distance-to-default | `christodoulakis-european-periphery-debt-crisis/chapters/ch12-solving-europes-financial-issues.md` |
| Dalio's bubble checklist and conditions at the top | `dalio-big-debt-crises/chapters/ch02-deflationary-cycle-early-bubble-top.md` |
| Vulnerability checklist for an inflationary (currency) crisis | `dalio-big-debt-crises/chapters/ch05-inflationary-depressions-and-currency-crises.md` |
| Sovereign debt indicators and the debt-dynamics equations | `dalio-how-countries-go-broke/chapters/ch03-mechanics-in-numbers-and-equations.md` |
| Stage markers and flight behaviours in a government debt crisis | `dalio-how-countries-go-broke/chapters/ch05-private-sector-and-government-debt-crisis.md` |
| Defining and predicting a currency crisis: exchange market pressure index | `eichengreen-capital-flows-crises/chapters/ch05-exchange-market-mayhem.md` |
| Leverage versus VAR, the pro forma stress test (stated inside a case chapter) | `dalio-big-debt-crises/chapters/ch09-case-us-debt-crisis-and-adjustment-2007-2011.md` |
| Disaster myopia and other biases that hide risk | `cassidy-how-markets-fail/chapters/ch15-psychology-returns-to-economics.md` |
| A firm-level failure model: eight variables, by horizon, against distance to default | `campbell-in-search-of-distress-risk/chapters/sec03-logit-model-of-bankruptcy-and-failure.md` |
| Exact formulas for the failure predictors | `campbell-in-search-of-distress-risk/chapters/sec06-appendix-variable-construction.md` |
| Hidden leverage: the loss-allocation map, three-layer transformation, four risks | `bis-building-ai-on-credit/chapters/sec02-financing-structures-risk-allocation.md` |
| Off-balance sheet "shadow borrowing" and the three shock transmission channels | `bis-building-ai-on-credit/chapters/sec05-companion-qr-box-on-off-balance-sheet.md` |
| Where leverage sits and how contracts allocate a loss | `van-nieuwerburgh-financing-ai-buildout/chapters/sec05-risks.md` |
| Bank exposure to private credit: concentration, similarity, full-drawdown stress test | `fed-bank-lending-to-private-credit/chapters/sec04-direct-exposure-and-drawdown-stress.md` |
| Public quarterly series for private credit balance sheets | `fed-bank-lending-to-private-credit/chapters/sec07-companion-financial-accounts.md` |
| **(case)** Hyperion: about 90% project leverage off the tenant's balance sheet | `van-nieuwerburgh-financing-ai-buildout/chapters/sec04-financial-architecture-hyperion.md` |

### Phase 3. The break: crisis mechanics

| Question | Read |
|---|---|
| Catalyst, trigger and amplification. Phases of spillover | `claessens-financial-globalization/chapters/ch03-channels-and-mechanisms-of-the-crisis.md` |
| What was new in 2007-09: opacity, common lenders, the leverage loop, households | `claessens-financial-globalization/chapters/ch02-new-dimensions-of-the-crisis.md` |
| Causes of 2007-09, the bank capital channel | `hayford-malliaris-asset-prices-crisis/chapters/ch03-financial-crisis-2007-09.md` |
| Four types of banking crisis, credit crunch versus balance sheet recession | `koo-balance-sheet-recession/chapters/ch01-america-subprime-fiasco.md` |
| Multiple equilibria in sovereign debt, lender of last resort | `christodoulakis-european-periphery-debt-crisis/chapters/ch06-economic-theories-karlsruhe-judges.md` |
| Solvency versus cash flow, the first actions in a depression | `dalio-big-debt-crises/chapters/ch03-deflationary-depression-and-the-four-levers.md` |
| How currency crises spread between countries: contagion channels | `eichengreen-capital-flows-crises/chapters/ch06-contagious-currency-crises.md` |
| Hidden information, moral hazard, why banks run | `cassidy-how-markets-fail/chapters/ch12-hidden-information-and-the-market-for-lemons.md` |
| Loss spirals, mark-to-market, runs | `cassidy-how-markets-fail/chapters/ch22-london-bridge-is-falling-down.md` |
| The nine stages of a government and central bank debt crisis | `dalio-how-countries-go-broke/chapters/ch04-archetypical-sequence.md` |
| Why busts cluster: entrepreneurs forecast the same variables and err together | `cowen-risk-and-business-cycles/chapters/ch02-risk-based-theory-real-terms.md` |
| How a financing structure transmits and amplifies an asset loss | `van-nieuwerburgh-financing-ai-buildout/chapters/sec05-risks.md` |
| Bank links to private credit other than loans: stakes, partnerships, risk transfer | `fed-bank-lending-to-private-credit/chapters/sec05-other-bank-interactions.md` |
| **(case)** The subprime chain and structured credit | `cassidy-how-markets-fail/chapters/ch19-the-subprime-chain.md` |
| **(case)** United States 2007-2011 read against Dalio's template | `dalio-big-debt-crises/chapters/ch09-case-us-debt-crisis-and-adjustment-2007-2011.md` |
| **(case)** Asia 1997 | `eichengreen-capital-flows-crises/chapters/ch09-understanding-asias-crisis.md` |
| **(case)** The Baring crisis of 1890 and Mexico 1994 | `eichengreen-capital-flows-crises/chapters/ch07-baring-crisis-in-a-mexican-mirror.md` |

### Phase 4. The aftermath: deleveraging and balance sheet recession

| Question | Read |
|---|---|
| Output, money and credit after a crisis | `schularick-taylor-credit-booms/chapters/ch03-event-analysis-after-financial-crises.md` |
| Four-stage post-bubble process, why rate cuts stop working, fiscal design | `koo-balance-sheet-recession/chapters/ch01-america-subprime-fiasco.md` |
| Yin and yang phases, fallacy of composition across countries | `koo-balance-sheet-recession/chapters/ch04-global-yin-yang-framework.md` |
| How long deleveraging takes, banking collapse to political change | `schulte-credit-driven-economy/chapters/ch03-political-chaos-and-deleveraging-timeline.md` |
| Arithmetic of deleveraging: raise capital or shrink assets | `schulte-credit-driven-economy/chapters/ch04-tangible-leverage-and-deleveraging-arithmetic.md` |
| Debt deflation and the fiscal versus competitiveness trade-off | `christodoulakis-european-periphery-debt-crisis/chapters/ch02-fiscal-vs-competitiveness-adjustment.md` |
| The four levers, beautiful deleveraging, pushing on a string | `dalio-big-debt-crises/chapters/ch04-beautiful-deleveraging-pushing-on-a-string-normalization.md` |
| How debt burdens fall: attribution, asset returns in devaluations | `dalio-how-countries-go-broke/chapters/ch07-new-equilibrium-and-new-cycle.md` |
| The inflationary route: spiral to hyperinflation | `dalio-big-debt-crises/chapters/ch06-hyperinflation-spiral-war-economies-summary.md` |
| **(case)** Japan and the lessons of monetization | `dalio-how-countries-go-broke/chapters/ch16-japanese-case-and-lessons.md` |
| **(case)** United States 1928-1937 | `dalio-big-debt-crises/chapters/ch08-case-us-debt-crisis-and-adjustment-1928-1937.md` |
| **(case)** Germany 1918-1924 | `dalio-big-debt-crises/chapters/ch07-case-german-debt-crisis-and-hyperinflation-1918-1924.md` |
| **(case)** 48 short country cases in two tables | `dalio-big-debt-crises/chapters/ch10-compendium-method-glossary-domestic-currency-cases.md` |

### Phase 5. Policy response and the bank-sovereign loop

| Question | Read |
|---|---|
| Forms of government intervention, distortions, exit | `claessens-financial-globalization/chapters/ch04-government-interventions-and-exit.md` |
| Moral hazard, micro and macro-prudential rules | `hayford-malliaris-asset-prices-crisis/chapters/ch04-policies-and-conclusions.md` |
| The Greenspan doctrine and why it broke | `hayford-malliaris-asset-prices-crisis/chapters/ch01-introduction-great-moderation.md` |
| Bailouts and public debt after crises | `schulte-credit-driven-economy/chapters/ch05-bailouts-public-debt-rule-of-1-and-20.md` |
| Banking union, bail-in, the three loops | `christodoulakis-european-periphery-debt-crisis/chapters/ch13-european-banking-union.md` |
| Sovereign debt restructuring, no-bailout rules | `christodoulakis-european-periphery-debt-crisis/chapters/ch10-sovereign-debt-restructuring-framework.md` |
| Corporate funding when banks and the sovereign are stressed | `christodoulakis-european-periphery-debt-crisis/chapters/ch11-corporate-funding-risks-periphery.md` |
| Macroprudential tools | `dalio-big-debt-crises/chapters/ch12-appendix-macroprudential-policies.md` |
| When the crisis reaches the central bank's own balance sheet | `dalio-how-countries-go-broke/chapters/ch06-crisis-spills-over-to-central-bank.md` |
| Capital controls: prudential versus emergency | `eichengreen-capital-flows-crises/chapters/ch10-capital-controls-idea-or-folly.md` |
| Managing capital flows, the Chilean tax, international responses | `eichengreen-capital-flows-crises/chapters/ch11-taming-capital-flows.md` |
| The Fed's rescue doctrine and credibility | `axilrod-inside-the-fed/chapters/ch08-fed-and-its-image.md` |
| Asset bubbles as a central bank dilemma | `axilrod-inside-the-fed/chapters/ch09-concluding-remarks.md` |
| Cassidy's reform programme | `cassidy-how-markets-fail/chapters/ch24-conclusion.md` |
| **(case)** The 2008 rescues: too interconnected to fail | `cassidy-how-markets-fail/chapters/ch23-socialism-in-our-time.md` |
| **(case)** Bernanke and the credit crisis, seen from inside the Fed | `axilrod-inside-the-fed/chapters/ch07-bernanke-great-credit-crisis.md` |

### Phase 6. Trading credit through the cycle

| Question | Read |
|---|---|
| When to hold spread risk, IG versus HY, fallen angels, supply, credit around Fed turns | `willer-trading-global-macro/chapters/ch11-credit.md` |
| Recession playbook: spreads and equities around recessions | `willer-trading-global-macro/chapters/ch03-business-cycle.md` |
| Credit inside an asset allocation, regimes | `willer-trading-global-macro/chapters/ch15-how-to-allocate.md` |
| Private credit and leveraged loans | `willer-trading-global-macro/chapters/ch16-private-assets-and-crypto.md` |
| Spread decomposition: default loss plus premium. The credit premium in numbers | `ilmanen-investing-amid-low-expected-returns/chapters/ch04-liquid-asset-class-premia.md` |
| Illiquidity premia, smoothed returns, what the book says on private credit | `ilmanen-investing-amid-low-expected-returns/chapters/ch05-illiquidity-premia.md` |
| How far a demand shock moves one bond, and a whole rating group | `chaudhary-corporate-bond-multipliers/chapters/sec04-estimation-results.md` |
| Why the price gaps survive: arbitrage risk, HY and long bonds | `chaudhary-corporate-bond-multipliers/chapters/sec05-arbitrage-risk.md` |
| How long the price effect lasts, and the limits of the estimates | `chaudhary-corporate-bond-multipliers/chapters/sec06-conclusion.md` |
| Does new long-dated debt supply move the term premium and IG spreads? Event-study design | `bis-building-ai-on-credit/chapters/sec03-spillovers-event-study.md` |
| Returns on the most distressed stocks (the numbers are one sample, US 1981-2003) | `campbell-in-search-of-distress-risk/chapters/sec04-risks-and-returns-on-distressed-stocks.md` |

### Phase 7. The inflationary route: when the debt is inflated away

| Question | Read |
|---|---|
| Dalio's inflationary depression: vulnerability checklist, stages, currency defense | `dalio-big-debt-crises/chapters/ch05-inflationary-depressions-and-currency-crises.md` |
| The spiral to hyperinflation | `dalio-big-debt-crises/chapters/ch06-hyperinflation-spiral-war-economies-summary.md` |
| Exchange-rate theory under inconvertible paper money | `bresciani-turroni-economics-of-inflation/chapters/ch02a-appendix-foreign-exchanges-under-inconvertible-paper.md` |
| Bresciani-Turroni's general conclusions on inflation | `bresciani-turroni-economics-of-inflation/chapters/ch11-conclusion.md` |
| **(case)** Germany: budget deficit and note issue versus the balance-of-payments theory | `bresciani-turroni-economics-of-inflation/chapters/ch02-national-finances-inflation-and-depreciation.md` |
| **(case)** Germany: internal versus external value of the mark | `bresciani-turroni-economics-of-inflation/chapters/ch03-divergence-internal-and-external-value.md` |
| **(case)** Germany: velocity, the flight from the mark, the real value of the circulation | `bresciani-turroni-economics-of-inflation/chapters/ch04-total-value-and-quantity-of-paper-money.md` |
| **(case)** Germany: share prices under inflation | `bresciani-turroni-economics-of-inflation/chapters/ch07-industrial-share-prices-under-inflation.md` |
| **(case)** Germany: the 1923 monetary reform | `bresciani-turroni-economics-of-inflation/chapters/ch09-monetary-reform-of-november-1923.md` |
| **(case)** Germany: the stabilization crisis and credit shortage after it | `bresciani-turroni-economics-of-inflation/chapters/ch10-the-stabilization-crisis.md` |
| **(case)** Germany 1918-1924 in Dalio's template | `dalio-big-debt-crises/chapters/ch07-case-german-debt-crisis-and-hyperinflation-1918-1924.md` |

## Points to Compare

Read both sides before answering. These are open questions, not conclusions.

1. **Do rate cuts end the downturn?** Willer and Saunders ch03 treat Fed cuts as a
   necessary condition for a market bottom in a recession. Koo ch01 argues that after a
   bubble, asset prices do not respond to rate cuts until they reach DCF value.
2. **What is the best warning signal?** Schularick and Taylor ch04 use credit growth.
   Schulte ch02 and ch04 use the loan/deposit ratio and tangible leverage. Willer and
   Saunders ch11 use spreads, volatility and the bank lending survey.
3. **Did monetary policy cause 2007-09?** Compare Hayford and Malliaris ch03 with
   Claessens ch01. Check how each treats easy money and global imbalances.
4. **Is the level of spreads useful?** Willer and Saunders ch11 separate IG from HY on
   this. Compare with the spread models in Christodoulakis ch01 and ch04, which cover
   sovereign spreads, not corporate ones.
5. **Is a crisis a credit event or a currency event?** Dalio (Big Debt Crises ch01,
   ch05) splits crises by the currency of the debt. Eichengreen ch05 defines a crisis by
   exchange market pressure. Schularick and Taylor ch03 date banking crises. Say which
   definition an answer uses.
6. **Do capital inflows cause the boom?** Compare Eichengreen ch02 and ch04 with
   Claessens ch01 and Schulte ch02.
7. **Why do booms happen at all?** Cassidy ch11, ch14 and ch16 explain them by incentives
   and herding. Dalio (Big Debt Crises ch02) explains them by the mechanics of credit.
   Schularick and Taylor ch01 treat the question as empirical.
8. **How long does the aftermath last?** Compare Schularick and Taylor ch03, Schulte ch03
   and Koo ch01. They measure different things, so say what each one measures.
9. **What caused the German inflation?** Bresciani-Turroni ch02 sets the budget deficit
   and note issue against the balance-of-payments theory. Dalio (Big Debt Crises ch07)
   reads the same episode through his template. Report where the two readings differ.
10. **Does supply move spreads?** Willer and Saunders ch11 call supply endogenous and say
    to ignore supply forecasts. Chaudhary sec04 finds a small price effect for one bond
    and a large one for a rating group, gone after about a quarter (sec06). It measures
    fund flows, not issuance. BIS sec03 tests AI debt news days and separates the term
    premium from the IG spread. Say what each one measures.
11. **How risky is private credit?** The Fed sec04 stress test gives a small effect on
    bank capital. BIS sec04 names a warning sign: lenders price AI loans like any other
    loan. Willer and Saunders ch16 note that the data hold no proper down cycle. Ilmanen
    ch05 says the data are too short and too dubious for a conclusion.
12. **Is distance to default a good gauge?** Campbell sec03 finds it adds almost nothing
    to a failure model for listed firms. Christodoulakis ch12 uses it to judge banks.
    The two test different entities.
13. **Is a boom an error?** Cowen ch02 derives the boom from rational choice under
    cheaper risk, and ch04 lists what the error view must assume. Compare Cassidy ch16
    (Minsky) and Dalio (Big Debt Crises ch02).
14. **How large is the AI boom against history?** BIS sec04 puts it near the US shale
    boom and at half the 1990s IT rise. Van Nieuwerburgh sec09 puts its scenario above
    every earlier episode. Check the measure, the period and realised against projected.
15. **Is spread risk paid?** Ilmanen ch04 reports a long-run credit premium over a matched
    stock and Treasury mix. Willer and Saunders ch11 give conditions for holding spread
    risk. Campbell sec04 finds low returns on the most distressed stocks.

## Case Memory (not for fresh theme reasoning)

`gurevich-trades-of-march-2020` is a diary of real trades. Use it only when the user asks
for a historical example, or in the analogue step after fresh reasoning is frozen.

- Funding stress in March 2020: `gurevich-trades-of-march-2020/chapters/ch06-week-3-the-dark-days.md`
- Real money funds in 2008 (interviews): `drobny-invisible-hands/chapters/ch01-rethinking-real-money.md`
- Dollar shortage, repo, collateral: `gurevich-trades-of-march-2020/chapters/ch05-week-2-the-loss-of-innocence.md`

## Scope and Limits

- This skill covers twenty-one sources. Bresciani-Turroni on the German inflation is linked from Phase 7 only. That book is a scan: trust only tables marked as checked against the PDF. It does not cover CDS
  mechanics, structured credit or CLOs. Its one default model is Campbell's, for listed firms.
- The other six skills added on 2026-11-23 (Shahidi, Satchell, Rozanov, Suria and the two
  Drobny books) hold portfolio and trading method, not credit-cycle content. They are not routed here,
  except one Drobny case chapter.
- It is an index. If a book skill changes, check that the paths here still exist.
- Each book skill also has `glossary.md`, `patterns.md` and `cheatsheet.md`. Use them for
  a term or a quick rule. Use the chapter files for an answer.
- Full extracted text sits at `/home/ak/.local/share/book-to-skill/fulltext/<book-skill>/full_text.txt`.
  Search it when a chapter file is too thin.
- Related topic skill: `fed-rate-hike`.
