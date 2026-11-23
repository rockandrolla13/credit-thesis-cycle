---
name: rozanov-global-macro-theory-practice
description: "Knowledge base from \"Global Macro: Theory and Practice\" edited by Andrew Rozanov (Risk Books, 2012), an edited volume of 14 practitioner chapters. Use when applying its contributors' frameworks for discretionary versus systematic macro, GTAA versus CTA, the macro strategist's scenario grid and reaction-function analysis, macro risk management (VaR, stress tests, stop-losses, loss limits), derivatives leverage and margin-to-equity, short-volatility return signatures, and macro's crisis behaviour in institutional portfolios, studying the book, or referencing its concepts."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# Global Macro: Theory and Practice
**Editor**: Andrew Rozanov (Permal Group) | **Publisher**: Risk Books, 2012 | **Pages**: ~323 | **Chapters**: 14 (plus Introduction), each by different authors | **Generated**: 2026-11-23

## How to Use This Skill

- **Without arguments** — load core frameworks for reference
- **With a topic** — ask about `stop-loss`, `scenario grid`, `leverage`, or another indexed topic; I find and read the relevant chapter
- **With chapter** — ask for `ch07`; I load that specific chapter
- **Browse** — ask "what chapters do you have?" to see the full index

When you ask about a topic not covered in Core Frameworks below, I will read
the relevant chapter file before answering.

This is an edited volume. The chapters do not share one method. Every framework below names its author. Attribute it to that author, not to "Rozanov" or "the book".

---

## Core Frameworks & Mental Models

### 1. What global macro is (Rozanov, Ch 1)
Five shared traits: global scope, multi-asset coverage, top-down approach, focus on liquidity, asymmetric trade construction. Three axes of style: discretionary/systematic, fundamental/technical, trend/relative value. Two temperaments: Soros ("invest first, investigate later", a move against you is information) and Robertson (research first, a move against you is a chance to add). Keynes was right on the thesis and wiped out by leverage three times.

### 2. Themes as a compass (Tropin, Ch 2)
A discretionary manager builds themes from growth, inflation and policy. The trade is the gap between the compass and the price. Two entries: position for the market to "catch up", or "fade" a misread data point. Demand "a 1:1 mapping of views and positions". Beta should be "episodic and not a consistent presence".

### 3. Systematic macro: value and trend fail in opposite regimes (Sternberg Ch 3, Yelnik Ch 4)
- GTAA: valuation-based, relative value, contrarian. Fails in strong trends ("value traps").
- CTA: trend following. Fails in volatile, range-bound markets.
- Their returns are lowly correlated (0.2 in Yelnik's A$/¥ example), so combine them.
- **Stop-loss test** (Yelnik, citing Kaminski and Lo): a stop helps only if the strategy's returns are positively auto-correlated. In many GTAA models they are not, and the stop "would thus tend to subtract value". Any cut needs a re-entry rule.
- Robustness (Yelnik): shift the back-test start date. Do not model the last crisis: "one-off events by definition do not recur out of sample".
- Sternberg's tactical rules: three states (long, short, none), volatility sizing, a stop on each trade, partial profit-taking, trailing stops. A system can profit with a hit rate below 50%.

### 4. The macro strategist: two schools (Wilson Ch 5, Frieda Ch 6)
- A strategist forecasts markets, not the economy, and forecasts **direction and volatility**. Too low a volatility forecast is the dangerous error.
- *Fundamental school*: economic logic wins in the long run. Tools: impossible trinity, Triffin dilemma, canonical currency crisis model.
- *Behavioural school* (Wilson): study the reaction function of the actor with power over the price. When the actor's framework breaks down, valuation stops working as a guide. Find the actor's balance-sheet pressure point. Case: SNB 2008-11.
- *Scenario grid* (Frieda): Good/Neutral/Bad per region, region weights, "joint probability = sum of country weights × scenario probabilities", then themes, then bottom-up country trades.
- *Regime credibility* (Frieda): macro funds "bet on the credibility of macro regimes". Focus on "vulnerability and consequences", not triggers. Rules of thumb are state-dependent: the 3% current account rule "failed miserably" after 2000.
- Positioning data are "partial and static". Hidden derivative exposure (KIKOs, 2008) can remove liquidity from a market that looked liquid.

### 5. Ten principles of macro risk management (Schachter, Ch 7)
1. Only take those risks that are central to the view being expressed.
2. Do not expose a position to "unknown unknowns" that are affecting price.
3. Whatever can go wrong probably will go wrong. Set the exit before entry.
4. Trading liquidity is a fickle friend. Watch crowding.
5. The best hedge is to exit the position.
6. Beware of changes in risk regimes.
7. Diversification is about the number of risk factors, not individual positions.
8. Good fences make good risk takers.
9. Do not be dogmatic.
10. Everyone is a risk manager.

VaR is a tool for ordinary conditions and aggregation (the *instrumentalist* view). It "does not explain" tail events. Scenario stress tests are subjective at each of their five steps. Absolute loss limits cost less return than drawdown limits.

### 6. Leverage is not risk (Casano Ch 10, de Vrij et al. Ch 14, Bausano Ch 9)
- Three kinds: balance sheet, margin, derivatives-based. Macro uses the third and borrows nothing.
- Gross notional is "a flawed risk indicator". It ignores volatility, strategy type, liquidity and correlation. Read **margin-to-equity** and the **capital utilisation ratio**, and watch them through time.
- Financing structure decides which strategies exist (Bausano). A hedge is only worth what its counterparty can pay (Russian GKOs, 1998).
- "Leverage is a tool to mitigate risks and not a control variable" (Ch 14). Set it from stress-tested cash needs.

### 7. Risk is highest when it looks lowest (de Vrij, Hoevenaars, van der Sluis, Ch 14)
"Forward-looking downside risks are highest when risky assets are rich and volatility levels are low." Volatility is "an improper measure of downside risk". Pro-cyclical leverage "to squeeze more yield out of tiny spreads is very dangerous". A 60/40 capital mix is a 92% equity risk mix on the authors' inputs. Size by risk contribution.

### 8. Reading return statistics (Kodmani and Rozanov Ch 12, Berkelaar Ch 13)
- Read skewness, kurtosis, equity correlation and serial correlation beside the Sharpe ratio. Strongly negative skew with high kurtosis marks a "short volatility" strategy. Serial correlation near 0.5 marks smoothed, illiquid marks.
- Dow Jones Credit Suisse indexes, January 1994 to June 2012: global macro 11.7% a year, Sharpe 0.88, skew 0.02, equity correlation 0.22. Managed futures 6.3%, Sharpe 0.27, equity correlation −0.04. August 2007 to February 2009: macro +5.3%, managed futures +21.8%.
- After eight dislocations, both beat other strategies in year one. In years two and three discretionary macro led and managed futures lagged.
- Standard risk factors explain about 79% of equity long/short returns and 8% to 26% of macro and managed futures returns.
- No "typical" macro experience exists. From January 2009 to June 2012 one macro index lost 16% and another gained 35%.

### 9. Macro in an institutional portfolio (Fox Ch 11, Ch 12-14)
Macro is not an asset class. Mercer places it in the growth portfolio as a risk reducer, at 5-10% of total assets across several managers. A fund of macro funds starts at 2-to-1 discretionary to systematic (Ch 12). The structural edge named by two chapters: price-insensitive counterparties such as central banks, hedgers and index investors.

### 10. Geopolitics (Murrin, Ch 8)
A "Five Stages of Empire" cycle. The author says it is "not a model in the traditional quantitative sense". It is untested narrative. See Trust Notes.

---

## Method or Case

The library keeps method and case apart. Several chapters hold both. Use the section pointers.

| Chapter | Type | What is method, what is case |
|---|---|---|
| ch00 Introduction | Neither | A map of the book |
| ch01 Origins | **CASE** | History: Keynes, Commodities Corporation, Soros, Tiger. The 50% loss rule is the one method item |
| ch02 Discretionary manager | **METHOD** | Operating method for a firm: manager questions, allocation, risk layers. One firm's practice |
| ch03 Systematic strategies | **METHOD** (descriptive) | Process steps with no parameters. The Figure 3.1/3.2 walk-through is illustration |
| ch04 Shades of macro | **METHOD** | Style taxonomy, stop-loss test, back-test hygiene |
| ch05 Macro strategist | **METHOD + CASE** | Method: two functions, two schools. Case: "From theory to practice: the SNB, 2008-11" |
| ch06 Emerging markets | **METHOD + CASE** | Method: credibility questions, scenario grid, positioning toolkit. Case: Mexico 1990-94, Turkey 2000-11, the 2H 2011 trade list, KIKOs 2008 |
| ch07 Risk management | **METHOD** | Ten principles, controls, stress tests, model philosophy |
| ch08 Geopolitical risk | **CASE-like narrative** | An untested cycle story with historical analogies and dated forecasts. Do not file as method |
| ch09 Prime broker | **CASE** (industry history) | How financing evolved. GKO 1998 episode. 2012 regulatory outlook |
| ch10 Leverage | **METHOD** | Arithmetic, ratios, four flaws of notional |
| ch11 Consultant | **CASE** (allocator practice) | What Mercer clients did and why. Style map is a small method item |
| ch12 Fund of funds | **METHOD + CASE** | Method: four-statistic test, event study, three drifts, benchmark rules. Case: index history 1994-2012, the 2007-09 allocator sequence |
| ch13 Institutional case | **METHOD** | Unsmoothing, ETL optimisation, tail tests, factor regressions, with their 1994-2012 results |
| ch14 GTAA for long-term investors | **METHOD + CASE** | Method: mandate blueprint, risk allocation, valuation-based risk. Case: the authors' 2007-08 positioning and their own fund's 2007-10 correlations |

---

## Use for Credit and Macro Questions

- **Credit spreads**: no spread valuation model. It gives three things. A warning rule: tight spreads with low volatility is the high-risk state, and the authors were short credit in 2007 on valuation (Ch 14). One data point: the EMBI Global spread reached 151 basis points in mid-2007 with an average rating of BB+, read as volatility suppression (Ch 6). Risk control forms for credit books: notional, rating-bucket and spread-range limits (Ch 7). Ch 9 argues that margin and capital rules decide how much leverage illiquid or term-financed assets can carry.
- **Debt-financed investment booms**: little. Ch 6 treats credit-led growth against a peg, the cost of bank clean-ups, and booms "mistaken for structural breaks", all for emerging markets. Hong Kong bank credit-to-GDP (178% to 264%, 2007 to 2011) is its one boom metric. Nothing on corporate capital spending cycles.
- **Inflation and Fed regimes**: thin. A method for reading a central bank's reaction function (Ch 5). Remarks on QE and Operation Twist distorting the curve in 2010-11 (Ch 3) and on emerging market responses to QE1 and QE2 (Ch 6). The February 1994 surprise hike appears only as a dislocation date (Ch 12). Nothing on measuring inflation.
- **Issuer screening**: nothing. The screening it covers is of fund managers.
- **Best use**: process discipline around a macro or credit thesis. Scenario grids, clean expression of a view, exit rules, leverage and liquidity reads, and tests for hidden short-volatility risk.

---

## Trust Notes

- **Charts are lost.** Extraction was text-only. Every figure is gone, including the Figure 3.1/3.2 system charts, the SNB charts, the empire curves and debt charts in Ch 8, the Figure 12 and 13 performance charts and the Figure 14.2 panels. Chapter files reconstruct them from the surrounding text and say so.
- **Damaged tables.** Table 3.1's header was garbled. Its last three columns are read as annualised return, standard deviation and drawdown, which is probable, not certain. Table 6.1's text columns ran together, so only the probabilities are reproduced. Tables 13.3 and 13.4 lost their column positions, so most factor coefficients cannot be assigned to a strategy. Figure 13.7's pie weights were recovered from loose labels and one column sums to 97%.
- **Not converted**: "About the Authors" and the index. Chapter boundaries were set from page headers because the extractor found only five ranges.
- **Sponsored and dated.** Permal Group commissioned the book and runs funds of macro funds. Most contributors sell or advise on the product they describe. All data end in mid-2012. Forward calls (Ch 1, 6, 8, 9) are recorded as made. Their outcomes are not in the text.
- **Ch 8 is not evidence.** It states sweeping historical claims as certain and gives no test. One figure in it (China's population as "56% male") is the author's and is unverified.
- **Windows differ.** Ch 11 has the macro index down 5% in calendar 2008. Ch 12 has it up 5.3% from August 2007 to February 2009. Both are stated correctly for their windows. Index returns carry backfill and survivorship bias, which Ch 12 and Ch 13 admit.

---

## Chapter Index

| # | Title | Author(s) | Key Frameworks |
|---|-------|-----------|----------------|
| [ch00](chapters/ch00-introduction.md) | Introduction | Isaac Souede | Chapter map, sponsor disclosure |
| [ch01](chapters/ch01-origins-history-prospects.md) | Global Macro: Origins, History, Prospects | Andrew Rozanov | Five traits, three axes, four stages, 50% loss rule, Soros versus Tiger |
| [ch02](chapters/ch02-discretionary-macro-managers-perspective.md) | Discretionary Global Macro: A Manager's Perspective | Kenneth G. Tropin | Themes as compass, eight manager questions, allocation models, cut-don't-hedge |
| [ch03](chapters/ch03-systematic-strategies.md) | Systematic Strategies: A Quantitative Approach to Global Macro | Menachem Sternberg | Five-step process, tactical system versus classic CTA, Table 3.1 |
| [ch04](chapters/ch04-different-shades-of-macro.md) | The Different Shades of Macro | Igor Yelnik | Fader, GTAA modules, GTAA versus CTA, stop-loss test, back-test hygiene |
| [ch05](chapters/ch05-role-of-macro-strategist.md) | The Role of a Global Macro Strategist | Grant Wilson | Analysis and prediction, fundamental versus behavioural, SNB case |
| [ch06](chapters/ch06-emerging-markets.md) | Emerging Markets in Global Macro Investing | Gene Frieda | Regime credibility, five reserve trends, scenario grid, KIKOs |
| [ch07](chapters/ch07-risk-management.md) | Risk Management in Global Macro Funds | Barry Schachter | Ten principles, controls, loss versus drawdown, VaR defence, stress tests |
| [ch08](chapters/ch08-geopolitical-risk.md) | Geopolitical Risk in Global Macro Investing | David Murrin | Five Stages of Empire, creditor leverage |
| [ch09](chapters/ch09-prime-brokers-perspective.md) | Global Macro: A Prime Broker's Perspective | Barry Bausano | Financing channels, cross-product margining, counterparty risk, regulation |
| [ch10](chapters/ch10-understanding-leverage.md) | Understanding Global Macro Leverage | John Casano | Three leverage types, margin-to-equity, four flaws of notional |
| [ch11](chapters/ch11-investment-consultants-perspective.md) | Global Macro: An Investment Consultant's Perspective | Simon Fox | Style map, sources of return, base and growth portfolio |
| [ch12](chapters/ch12-fund-of-hedge-funds-perspective.md) | Global Macro: A Fund of Hedge Fund's Perspective | Omar Kodmani, Andrew Rozanov | Four-statistic test, event study, 2-to-1 rule, three drifts, index divergence |
| [ch13](chapters/ch13-case-for-macro-in-institutional-portfolios.md) | The Case for Global Macro in Institutional Portfolios | Arjan Berkelaar | Unsmoothing, ETL optimisation, tail tests, factor regressions |
| [ch14](chapters/ch14-gtaa-and-macro-for-long-term-investors.md) | GTAA and Global Macro for Long-Term Institutional Investors | Gerlof de Vrij, Roy Hoevenaars, Pieter Jelle van der Sluis | Pyramid, five return sources, mandate blueprint, valuation-based risk |

## Topic Index

- **Back-test robustness / over-fitting** → ch03, ch04
- **Behavioural versus fundamental strategy** → ch05
- **Benchmarks and index divergence (HFRX, Dow Jones Credit Suisse)** → ch12, ch13
- **Capital allocation to traders** → ch01, ch02
- **Commodities Corporation** → ch01
- **Counterparty risk** → ch02, ch09, ch14
- **Credit (limits, spreads, short-credit 2007)** → ch06, ch07, ch13, ch14
- **Crisis performance (2007-09, eight dislocations)** → ch03, ch11, ch12, ch13
- **Crowding and positioning** → ch06, ch07
- **CTA / managed futures / trend following** → ch03, ch04, ch11, ch12, ch13
- **Currency crises and pegs (ERM, Mexico, Asia, Turkey)** → ch05, ch06
- **Drawdown and loss limits** → ch01, ch02, ch07
- **Emerging markets** → ch01, ch06
- **Expected tail loss / CVaR** → ch13
- **Factor regressions (Fama-French, Fung-Hsieh)** → ch12, ch13
- **Geopolitics** → ch08
- **GTAA / tactical asset allocation** → ch04, ch11, ch14
- **Keynes as investor** → ch01
- **KIKO options (2008)** → ch06
- **Leverage (types, margin-to-equity, notional)** → ch07, ch09, ch10, ch14
- **Liquidity** → ch02, ch06, ch07, ch10, ch12
- **Manager selection and due diligence** → ch02, ch11, ch12, ch13, ch14
- **Prime brokerage, repo, margining** → ch09
- **Quantitative easing, Operation Twist** → ch03, ch06
- **Reaction function** → ch05
- **Regulation (Dodd-Frank, EMIR, Basel III)** → ch09
- **Risk parity / risk allocation** → ch14
- **Scenario analysis** → ch06, ch07
- **Short-volatility profile, skew and kurtosis** → ch10, ch12, ch13
- **SNB and the Swiss franc (2008-11)** → ch03, ch05
- **Soros and Robertson** → ch01, ch10
- **Stop-losses** → ch03, ch04, ch07, ch14
- **Stress testing (scenario, reverse)** → ch07
- **Style drift** → ch01, ch04, ch12
- **Tail-risk hedging** → ch07, ch12, ch13, ch14
- **Themes** → ch02, ch14
- **VaR** → ch02, ch07, ch13
- **Volatility forecasting and sizing** → ch03, ch05

## Supporting Files

- [glossary.md](glossary.md) — all key terms with definitions
- [patterns.md](patterns.md) — all techniques, each with its author
- [cheatsheet.md](cheatsheet.md) — decision rules, thresholds and tells
- Full text: `/home/ak/.local/share/book-to-skill/fulltext/rozanov-global-macro-theory-practice/full_text.txt` — grep it for depth the chapter files omit (local extraction, not shipped)

---

## Scope & Limits

This skill covers the book content only. For hands-on implementation in your codebase,
combine with project-specific tools. For topics beyond this book, check related skills
or ask the agent directly.

The book is a 2012 practitioner survey written for institutional allocators. It describes how macro funds work and why to own them. It contains no pricing model and few testable trading rules. Trade ideas in Ch 6 and positions in Ch 14 are historical records of what the authors did or proposed. They are not recommendations.
