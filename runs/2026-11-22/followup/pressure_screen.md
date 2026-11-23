# Pressure screen and regime odds

As of 2026-11-22. Written 2026-11-23. Research only. No trades, no legs, no sizes, no hedge ratios, no stops.
Skill paths are relative to `/home/ak/.agents/skills/` unless they start with `.claude/skills/`, which is inside the creditmacro repo.
Evidence packs are third-party content. A post is a claim by its author, not a fact.

## Short answers

**B. Which skill tells us how likely this is?**
No single skill outputs a probability.
The best regime skill is `willer-trading-global-macro` (ch03 and ch15). It gives rules with thresholds that you can check against data.
The repo card `macro-state-parser` is the tool designed to output a regime probability. Nobody has run it, and it needs a data panel.
`papic-geopolitical-alpha` ch09 gives the procedure that turns the rule readings into a number.

**The regime call.** Every level rule says "overheating": high growth with high inflation. No rule says stagflation today.
The risk is a move toward stagflation over the next year.

**The probability.** "Core inflation stays near 3% and growth slows" within 12 months: about 25%, range 15% to 35%. Label: `PM_assumption`.
Within 6 months: about 10%. Label: `PM_assumption`.
Only one input is `evidence_weighted`: the 30% base rate for a manufacturing ISM below 50 (Willer ch03, Table 3.4).

**A. The screen.** Eleven variables in four groups. Two gates first, then a rank inside each rating tier and sector. Section 4 gives the design and a 2022 to 2023 backtest plan.
The local `marketdb` warehouse cannot run it today. Section 7 says why.

---

## 1. Part B: verdict per skill

### Personal book library

| Skill | Verdict | What it gives | Cite |
|---|---|---|---|
| `willer-trading-global-macro` | **Best fit** | Five regimes from growth and inflation. Thresholds for ISM, housing starts, claims, the Sahm rule and the curve. Ten macro clusters, with two kinds of stagflation. | `willer-trading-global-macro/chapters/ch03-business-cycle.md`, `ch15-how-to-allocate.md` |
| `fed-rate-hike` (router) | Use as the index | It holds no content. It routes to Willer ch05 and ch11, Axilrod, Dalio and Gurevich. | `fed-rate-hike/SKILL.md` |
| `skill-to-use` (router) | Use as the index | It routes "allocation by regime" questions to Willer. It warns that several Willer rules failed in 2022 to 2023. | `skill-to-use/SKILL.md` |
| `papic-geopolitical-alpha` | Useful for the number | Prior, data streams, posterior. A decision tree with conditional probabilities. "Draw the tree before trusting a gut number." It gives no macro thresholds. | `papic-geopolitical-alpha/chapters/ch09-net-assessment.md` |
| `simonian-computational-global-macro` | Useful as a cross-check | The Noisy-OR model joins several independent causes into one probability. It needs a probability per cause, and no book supplies those. | `simonian-computational-global-macro/chapters/ch05-causal-inference.md` |
| `dalio-how-countries-go-broke` | Partly useful | A two-indicator matrix: real yield and curve shape. Neutral real yield about 2%. It says tight or easy money, not growth odds. | `dalio-how-countries-go-broke/chapters/ch10-big-debt-cycle-1945-to-now.md` |
| `dalio-big-debt-crises` | Useful for the screen, not for the odds | ch02: the riskiest debtors miss payments about six months before the economy peaks. ch05 covers inflationary depressions in countries with foreign-currency debt. That is not the US case in a 12-month window. | `dalio-big-debt-crises/chapters/ch02-deflationary-cycle-early-bubble-top.md`, `ch05-inflationary-depressions-and-currency-crises.md` |
| `axilrod-inside-the-fed` | Useful for one branch | How the Fed decides when it cannot hold both growth and inflation in bounds. It compares chairmen by the real funds rate. It gives no probability. | `axilrod-inside-the-fed/chapters/ch01-overview-policy-management-and-managers.md`, `ch09-concluding-remarks.md` |
| `gurevich-trades-of-march-2020` | Minor | A six-step script for how Fed policy ends a cycle. Step 1 is "We are overheating: hike!". His own positions are case memory and I did not use them. | `gurevich-trades-of-march-2020/chapters/ch02-the-pivot.md` |
| `koo-balance-sheet-recession` | Not relevant | The router describes it as private-sector debt paydown with zero rates not working. Today the Fed is hiking. | `skill-to-use/SKILL.md` |
| `bresciani-turroni-economics-of-inflation` | Not relevant | The router describes it as German hyperinflation, 1914 to 1931. It is a scan with a trust warning. | `skill-to-use/SKILL.md` |
| `credit-cycle` (router) | Useful for Part A | It routes warning-sign questions to Willer ch11, Dalio ch02 and Cassidy ch16. | `credit-cycle/SKILL.md` |

### Project skills (read-only)

| Skill | Verdict | What it would contribute | Cite |
|---|---|---|---|
| `macro-state-parser` | **The right tool, not yet run** | A regime probability vector that sums to one, from a filtered panel of many series. It refuses a hand-asserted label. Its seam is "pending". It needs a panel of about 150 monthly series. | `.claude/skills/macro-state-parser/SKILL.md` |
| `macro-regime-classifier` | Useful as discipline | A regime label from observable data. It lists stagflation as one joint state. It requires a flag for regime-transition risk. It forbids forecasts. | `.claude/skills/macro-regime-classifier/SKILL.md` |
| `evidence-weighting` | Useful | Anchor on a base rate, then move in proportion to the evidence. It forbids an invented base rate. | `.claude/skills/evidence-weighting/SKILL.md` |
| `scenario-pricing-engine` | Useful for labels | It never invents a probability. A probability with no evidence reference is `PM_assumption`. | `.claude/skills/scenario-pricing-engine/SKILL.md` |
| `priced-in-estimator` | Useful for the gap | It asks what the market already discounts. Section 3 applies it. | `.claude/skills/priced-in-estimator/SKILL.md` |
| `term-premium-estimator` | Minor | It separates a term-premium move from a rate-expectations move. This matters for the 10-year yield at 5.04% with falling breakevens. It gives no growth signal. | `.claude/skills/term-premium-estimator/SKILL.md` |
| `outcome-calibration-engine` | Useful later | It scores a probability after the outcome arrives. It generates nothing. Use it to grade the 25% in a year. | `.claude/skills/outcome-calibration-engine/SKILL.md` |

---

## 2. The readings

All FRED values pulled on 2026-11-23 with a keyless request. Lead-supplied values are marked "lead".

| Series | Value | Date | Source |
|---|---|---|---|
| Fed funds upper bound | 4.00% | 2026-11-22 | FRED DFEDTARU |
| 2-year Treasury | 4.76% | 2026-11-19 | FRED DGS2 |
| 10-year Treasury | 5.04% | 2026-11-19 | FRED DGS10 |
| 10-year real yield (TIPS) | 2.88% | 2026-11-19 | FRED DFII10 |
| 10-year breakeven | 2.15% | 2026-11-20 | FRED T10YIE |
| 10-year minus 3-month | +0.60 | 2026-11-20 | FRED T10Y3M |
| 10-year minus 2-year | +0.29 | 2026-11-20 | FRED T10Y2Y |
| Core PCE, year on year | 3.1% | Sep 2026 | FRED PCEPILFE, my arithmetic (130.902 / 126.940) |
| Core PCE, 3-month annualised | 2.9% | Sep 2026 | FRED PCEPILFE, my arithmetic |
| Core CPI, year on year | 2.6% | Sep 2026 | FRED CPILFESL, my arithmetic. October 2025 is missing, so no October figure. |
| Core CPI, 3-month annualised | 3.7% | Oct 2026 | FRED CPILFESL, my arithmetic |
| Headline CPI, year on year | 3.7% | Sep 2026 | FRED CPIAUCSL, my arithmetic |
| ISM manufacturing | 55.5 | Oct 2026 | lead |
| Housing starts | 1,309k | Oct 2026 | FRED HOUST |
| Unemployment rate | 4.1% | Oct 2026 | FRED UNRATE |
| Sahm rule | 0.00 | Oct 2026 | FRED SAHMREALTIME |
| Initial claims | 203k | 2026-11-14 | FRED ICSA |
| Payrolls, monthly change | +165k, 3-month average +137k | Oct 2026 | FRED PAYEMS, my arithmetic |
| SLOOS net tightening, large firms | 1.7, up from 0.0 | Q4 2026 | FRED DRTSCILM |
| Chicago financial conditions | -0.48 (loose) | 2026-11-13 | FRED NFCI |
| 30-year mortgage rate | 7.28% | 2026-11-19 | FRED MORTGAGE30US |
| Gasoline, regular | $3.81, down from $4.15 | 2026-11-16 | FRED GASREGW |
| WTI oil | $89.53, from $107.56 on 30 Oct | 2026-11-17 | FRED DCOILWTICO |
| VIX | 28.4 on 19 Nov. About 36 after 20 Nov. | 2026-11-19 | FRED VIXCLS, then lead |
| IG / HY / CCC spread | 94bp / 352bp / 1,361bp | 2026-11-19 | FRED BAMLC0A0CM, BAMLH0A0HYM2, BAMLH0A3HYC |
| BBB / BB / B spread | 117bp / 210bp / 380bp | 2026-11-19 | FRED BAMLC0A4CBBB, BAMLH0A1HYBB, BAMLH0A2HYB |
| Fund managers who expect a recession | 3% | 20 Nov 2026 | BofA survey via WSJ, in `evidence/email.md` item 7 |

One oddity. Core PCE runs at 3.1% and core CPI at 2.6%. @biancoresearch says the gap between the two is the largest since 1985 and comes from housing weights (17 Sep 2026).

---

## 3. Part B applied: what each rule says today

### 3.1 Rule by rule

| # | Rule | Threshold in the book | Reading | Rule says |
|---|---|---|---|---|
| 1 | Five-regime cycle (Willer ch03) | Stagflation is low growth with high inflation. Overheating is high with high. The book gives no numeric cut-off for "high". | ISM 55.5, core PCE 3.1% | **Overheating** |
| 2 | ISM level (Willer ch03) | Below 45 is recession. 45 to 50 is an inventory correction. | 55.5 | No slowdown now |
| 3 | Housing starts (Willer ch03) | Below 1.1 million coincided with recession | 1,309k. It dipped to 1,182k in May and 1,191k in September. | No recession signal |
| 4 | Claims (Willer ch03) | Up 50k from the low and above 350k | 203k | Not met. The book calls this a lagging signal. |
| 5 | Sahm rule (Willer ch03) | 0.5 points | 0.00 | Not met. Also lagging. |
| 6 | 3m/10y inversion (Willer ch03) | Inversion forecasts Fed cuts. Median 14 months to recession. | +0.60, not inverted | No signal. Every recession in Table 3.3 followed an inversion. |
| 7 | Consumption leading indicator (Willer ch03) | Gasoline prices, mortgage rates and S&P returns lead the ISM by about 10 months | Oil reached $110. Mortgage rate 7.28%. S&P down about 8%. I did not compute the z-scores. | **Direction: lower ISM in about 10 months.** Direction only. |
| 8 | Recession causes (Willer ch03) | Look for Fed overtightening, large oil moves and asset bubbles | The Fed is hiking. Oil spiked. An AI equity fall is in progress (`thesis.md`). | All three candidate causes are present. The book gives no odds. |
| 9 | Macro clusters (Willer ch15) | "Tightening financial conditions" is inflation above average with growth near trend. It "can lead to stagflation, as in 2022-2023". | Inflation above average. The Fed is hiking. Equity volatility is high. | **Tightening financial conditions, a known path to stagflation** |
| 10 | Stock-bond correlation (Willer ch15) | Core CPI above 2.5% gives a mostly positive correlation | Core CPI 2.6% | Bonds may not protect when stocks fall |
| 11 | Inflation chain (Willer ch03) | Oil leads PPI, then headline CPI, then core CPI | Oil fell from about $108 to about $90 | Headline inflation should ease first. Core comes last. |
| 12 | Breakevens around hikes (Willer ch05) | Breakevens "fall when the Fed hikes in earnest" | 2.15%, a three-year low (lead) | Falling breakevens fit a hiking Fed. They are not proof that realised inflation will fall. |
| 13 | Real yield and curve matrix (Dalio, How Countries Go Broke, ch10) | Neutral real yield about 2%, give or take 1%. Tight money is a high real yield with a flat or inverted curve. | Real yield 2.88%. Short rate 1.04 points below the 10-year, and 79% of it. | Real yield at the top of the band. The curve has a normal shape. **Money is not yet tight on this matrix.** |
| 14 | Real funds rate (Axilrod ch09) | Compare the real funds rate with inflation's direction | 4.00% minus 3.1% is about 0.9% | Positive but low. Axilrod calls the neutral rate "something of a guess". |
| 15 | Six-step script (Gurevich ch02) | Step 1: "We are overheating: hike!" Step 2: "Stocks aren't the economy, stay the course." | The minutes favour more hikes while stocks fall (`report.md`, CNBC, 18 Nov 2026) | Step 1 to 2 of 6 |
| 16 | Sentiment (Willer ch03) | Majority soft or hard landing sentiment is "not predictive". Every recession starts out looking like a soft landing. | 3% expect a recession | No information either way |

### 3.2 Where the rules disagree

1. **Levels against direction.** Rules 1 to 6 say growth is strong now. Rules 7 to 9 say the pressure on growth is building. The book puts the lag at about 10 months.
2. **Is money tight?** The Chicago index says financial conditions are still loose (-0.48). The equity fall and the VIX say they are tightening. Dalio's matrix says not yet tight. Willer notes that in the tightest quintile of the Chicago index forward returns are poor, and we are not there.
3. **Is inflation persistent?** Core PCE at 3.1% and core CPI at 3.7% over three months say yes. Oil and breakevens say no. Willer ch05 offers a way to hold both: breakevens fall once the Fed hikes in earnest.
4. **What should credit do?** The ISM rule favours HY over IG while the ISM is above 50 (Willer ch11). The lending-survey rule and the volatility rule both say hold no spread risk (Willer ch11, checked in `report.md` finding 6).
5. **The curve.** It is not inverted, so the classic recession signal is silent. The book's own 2022 example shows the signal failing with high inflation (Willer ch03, case).

### 3.3 The probability, built as a tree

Method: Papic ch09 (prior, data, tree) and the repo's `evidence-weighting` card (base rate first).

**Definitions, so the claim can be scored later.**
- "Inflation persists": core PCE year on year averages 2.75% or more over the six prints to October 2027.
- "Growth slows": the manufacturing ISM prints below 50 for two months in a row, or the Sahm rule reaches 0.50, by November 2027. This matches the hard-landing test in `report.md`, over a longer window.

**Step 1. Base rate for slower growth.** The ISM was below 50 in 29.6% of months (Willer ch03, Table 3.4, sample period not stated). Label: `evidence_weighted`.

**Step 2. Adjust for today.**
- Up: the Fed is hiking, oil spiked and equities fell. These are Willer's three recession causes and his consumption indicator (rules 7 and 8).
- Down: the ISM starts at 55.5, the curve is not inverted, housing starts are above 1.1 million and claims are low (rules 2 to 6).
- Net: I leave it near 35%. Label: `PM_assumption`.

**Step 3. Probability that inflation persists.** About 65%. Label: `PM_assumption`. No book rule gives this number.
- For: core PCE at 3.1%. @biancoresearch says core PCE has run above 2% for 67 months and has risen for a year and a half (18 Nov 2026). Unemployment is 4.1%. Core falls last in Willer's chain.
- Against: oil is down about 17% in three weeks. Breakevens are at a three-year low. Core PCE over three months runs at 2.9%. The Fed is hiking.

**Step 4. The tree.**

| Branch | Probability | Growth slows, given the branch | Joint |
|---|---|---|---|
| Inflation persists, so the Fed keeps hiking | 65% | 40% | **26%** |
| Inflation fades | 35% | 25% | 9% |

- Persistent inflation with slowing growth: **about 25%** over 12 months. Range 15% to 35%. Label: `PM_assumption`.
- Slowing growth with fading inflation: about 9%. Label: `PM_assumption`.
- The 40% is higher than the 25% because Willer lists Fed overtightening as a recession cause (ch03).

**Step 5. Cross-check with a Noisy-OR (Simonian ch05).** Three causes of a slowdown with my own inputs: Fed overtightening 15%, the oil shock 10%, the equity fall 15%, plus a 5% leak. All four inputs are `PM_assumption`.
1 - (0.85 x 0.90 x 0.85 x 0.95) = 38%. That sits close to the 35% in step 2.

**Six months.** The grid gives hard landing 10% over six months as a `PM_assumption` (`report.md`). The 10-month lead in rule 7 argues that most of the slowdown risk falls in months 7 to 12. So the six-month joint figure is about 10% at most. Label: `PM_assumption`.

**What is priced.** Breakevens at 2.15% price fading inflation. A 3% recession vote prices no slowdown. The 2-year yield at 4.76% against a 4.00% policy rate prices more hikes. So the market prices "hikes work and nothing breaks". The joint case of sticky inflation with weaker growth gets little attention.

**What would move the number.**
- Up: ISM new orders minus inventories turns down (Willer ch03 calls it a lead with false signals). Soft data falls below hard data (Willer ch03). A second SLOOS tightening print.
- Down: core PCE three-month rate under 2.5% for two prints. The Fed pauses. The ISM holds above 55.

---

## 4. Part A: the issuer screen

### 4.1 The mechanism

1. Persistent inflation keeps policy rates and yields high. Interest cost rises at each reset and each refinancing.
2. Inflation lifts input, energy and wage costs. Margins fall where the firm cannot pass costs on.
3. Slowing growth cuts volumes and pricing power. Earnings fall while interest cost rises.
4. Lenders tighten. "Tighter standards mean less lending, more rollover risk, then defaults" (Willer ch11).
5. The riskiest debtors show stress about six months before the economy peaks (Dalio, Big Debt Crises, ch02).

Dalio adds a warning. An economy-wide average is "useful but ultimately inadequate", because debt concentrated in key entities is more dangerous than the same debt spread evenly (Big Debt Crises, ch02). That is the case for an issuer-level screen.

### 4.2 The eleven variables

"Convention" means analyst convention, not from the library.

**Group 1: balance-sheet exposure**

| # | Variable | What it measures | Why it matters now | Data source | Threshold | Cite |
|---|---|---|---|---|---|---|
| 1 | Interest coverage, now and after refinancing. EBITDA divided by cash interest. Redo it with today's market coupon for the rating. | Can earnings pay the interest? | Minsky's test. Hedge borrowers pay interest and principal. Speculative borrowers pay interest only and must roll. Ponzi borrowers cannot pay the interest. | 10-K and 10-Q. Market coupon from TRACE yields or FRED rating-tier yields. | Below 1.0x is Ponzi finance by Minsky's definition. Below 2.0x is a convention. | `cassidy-how-markets-fail/chapters/ch16-hyman-minsky-and-ponzi-finance.md`. `dalio-big-debt-crises/chapters/ch01-credit-debt-and-the-big-debt-cycle-template.md` (borrowing to pay debt service is a warning sign). |
| 2 | Refinancing need. Debt due within 24 months, divided by cash plus undrawn credit lines plus 24 months of free cash flow. | Must the firm come to market? | Rollover risk rises when lenders tighten. The monitoring skill puts "upcoming maturity with no clear refinancing path" on the watchlist. | Debt maturity table in the 10-K. FINRA or Mergent FISD for bond maturities. | Above 1.0 is a convention. | Willer ch11 (SLOOS chain). `borrower-monitoring/SKILL.md`. Cassidy ch16. |
| 3 | Floating-rate share of debt, net of disclosed hedges. | How fast a hike reaches the income statement | Levered loans are floating rate. Private credit is mostly floating rate with three to seven year maturities. | Debt footnote and market-risk section of the 10-K. Loan data for private borrowers is not public. | Above 50% is a convention. | Willer ch11 (loans logic, private credit definition). |
| 4 | Coupon step-up. Today's market yield for the issuer minus its average coupon. | The jump in interest cost at refinancing | @junkbondinvest reports about 8 points for CCC issuers and about 1 to 2 points for BB and B (30 Oct and 18 Nov 2026, the second citing PIMCO). | TRACE yields against coupons from FISD or filings. | None in the library. Above 3 points is a convention. | Evidence only: corpus `x/junkbondinvest.md`. |
| 5 | Net leverage. Net debt divided by EBITDA, with add-backs haircut. Plus covenant headroom where a covenant exists. | Debt against earnings | Net leverage is the most common binding covenant in mid-market credit. A borrower should be on the watchlist before a breach. | 10-K. Credit agreement for the covenant. | Headroom within 5% to 10% is "watchlist" in the monitoring skill. Leverage levels are a convention and vary by sector. | `covenant-compliance/SKILL.md`, `borrower-monitoring/SKILL.md`, `ebitda-addback-treatment`. |

**Group 2: margin exposure**

| # | Variable | What it measures | Why it matters now | Data source | Threshold | Cite |
|---|---|---|---|---|---|---|
| 6 | Pass-through. Change in gross margin over four quarters while sector input prices rose. | Pricing power as revealed, not as claimed | "Revenue can be growing while margins deteriorate." The monitoring skill tells the analyst to trace compression to cost inflation, mix or pricing pressure. | 10-Q gross margin. BLS producer prices by industry. | The library gives none. A fall of 200bp or more is a convention. | `borrower-monitoring/SKILL.md`. Willer ch03 (oil leads PPI, then CPI). |
| 7 | Labour and energy intensity. Staff cost plus energy cost, divided by revenue. | Share of the cost base that reprices with wages and fuel | The sector cards name labour cost for HY healthcare and fuel cost for HY consumer cyclical. | 10-K where disclosed. Otherwise headcount times BLS sector wage. Energy from segment notes. | None. Rank within sector. Convention. | `credit-scenario-grid/sectors.md`. Thresholds: books are silent. |

**Group 3: demand exposure**

| # | Variable | What it measures | Why it matters now | Data source | Threshold | Cite |
|---|---|---|---|---|---|---|
| 8 | Cyclicality. Sensitivity of revenue growth to the manufacturing ISM over past cycles. | How much volume falls when growth slows | Below an ISM of 50, HY underperforms IG on a risk-adjusted basis. | Quarterly revenue history from filings. ISM. | ISM 50 is the regime line. The issuer cut-off is a convention. | Willer ch11 (ISM rule), ch03 (ISM levels). |
| 9 | Customer concentration and contract backing. Revenue share of the top customers, and whether an investment-grade party stands behind it. | Whether one customer's cut can break the borrower | The market already sorts AI borrowers by big-tech support (`thesis.md`). | 10-K major-customer disclosure. Convention. | None in the library. | Evidence only: `thesis.md` section 2, @nodiligence, 21 Nov 2026. |

**Group 4: market signals**

| # | Variable | What it measures | Why it matters now | Data source | Threshold | Cite |
|---|---|---|---|---|---|---|
| 10 | Spread per turn of leverage, against the median for the same rating and sector. Also the change over three months. | Whether the bond market already charges for the risk | Credit investors react faster than equity investors (Willer ch11). In HY the spread level carries information. In IG it carries very little (Willer ch11). | TRACE prices. Leverage from variable 5. | None. Convention. | Willer ch11 (valuation, mental models). |
| 11 | Equity drawdown and distance from the 200-day average. Plus market-implied rating minus agency rating, in notches. | Whether equity and credit markets disagree with the agencies | Willer uses the 200-day average as his risk tool and watches listed private-credit funds against it. Applying it to single issuers is my extension. A gap at BBB- matters most, because a downgrade to HY forces IG funds to sell (Willer ch11). | CRSP daily. TRACE for the implied rating. Agency ratings. | Below the 200-day average (Willer's tool, my extension). Two notches or more is a convention. | Willer ch03, ch11. Evidence: Felder citing Groundbreaker, 5.3 notches on average for AI lessees (`evidence/email.md` item 5). |

### 4.3 Scoring sketch: gates first, rank second

**Gate 0. Data.** Score an issuer only with at least 8 of the 11 variables. Mark the rest "unscored". Never treat a missing value as safe.

**Gate 1. Rate channel.** Pass if any one holds: refinancing need above 1.0, floating share above 50%, or coverage after refinancing below 2.0x.

**Gate 2. Earnings channel.** Pass if the issuer is in the worst third of its sector on the margin group or on the demand group.

An issuer must pass both gates. The regime has two legs, and an issuer exposed to one leg only is a different problem.

**Side list. Already priced.** Put issuers with bonds below 80 cents or a CCC-implied rating on a separate list. `thesis.md` says weak credit is fully repriced. @junkbondinvest says price leads defaults: 8.01% of performing loans trade below 80 while the default rate is 0.55% (6 Nov 2026).

**Rank.**
1. Inside each rating tier and sector, turn each variable into a percentile. 100 is worst.
2. Average the percentiles inside each group. Then average the three fundamental groups with equal weights. Call this F.
3. Call the market group M.
4. Rank by F. Report F minus M beside it.
5. High F with low M means pressure that the market does not yet charge for. High F with high M means the market agrees.

Equal weights are deliberate. They leave nothing to fit.

### 4.4 Backtest on 2022 to 2023 (case, used only to test)

The first hike was March 2022 and the last was July 2023 (Willer ch15 Table 15.1 and ch05, case). Spreads peaked in October 2022 and retested in March 2023 (Willer ch11, case).

1. **Form the screen** from filings available on 31 December 2021. Use only data filed by that date.
2. **Universe:** US non-financial issuers with public bonds and public equity.
3. **Outcomes, January 2022 to December 2023:**
   - Downgrade of two notches or more, or any downgrade into CCC.
   - Default or distressed exchange.
   - Spread widening beyond the issuer's rating and sector peers, measured at the October 2022 peak.
   - Fall in interest coverage of 1.0x or more.
4. **Compare** the top fifth by F with the bottom fifth.
5. **Benchmarks to beat:** rating alone, starting spread alone, leverage alone.

**The screen fails if any of these holds.**
1. The top fifth does not have at least 1.5 times the downgrade and default rate of the bottom fifth.
2. F adds nothing to starting spread alone when both predict the outcomes. Then the market already knew.
3. The result disappears when any one sector is dropped.
4. The two gates pass more than 40% of the universe. Then they do not discriminate.
5. High F with low M does no worse afterwards than high F with high M. Then the gap carries no signal.

**Limits of this test.**
- 2022 to 2023 had hikes and inflation but no recession. Willer says housing starts and the manufacturing PMI "never reached recession levels" (ch03, case). So it tests the rate and margin legs well and the demand leg weakly.
- A second window is needed for the demand leg. That window must come from data, because the method chapters do not supply one.
- Survivorship matters. The universe must include issuers that later defaulted or were delisted.

### 4.5 Which sectors and tiers the screen would likely flag today

| # | Sector or tier | Why | Label |
|---|---|---|---|
| 1 | Healthcare providers in HY, loans and private credit | The sector card names labour cost and floating-rate debt. Fitch puts private-credit defaults for healthcare providers at 8.7% (@junkbondinvest, 2 Nov 2026). One large hospital operator's bonds fell 30 points in two months (@junkbondinvest, 22 Nov 2026). | `evidence_weighted` |
| 2 | Consumer-facing borrowers in HY and private credit: retail, leisure, autos | Fitch puts consumer private-credit defaults at 9.7% (same post). The mortgage rate is 7.28% (FRED). @biancoresearch says pay has trailed cumulative inflation since the COVID recession (3 Oct 2026). The grid gives this sector one of the largest hard-landing moves among HY sectors (+290bp). | `evidence_weighted` on the rate leg. `PM_assumption` on the demand leg. |
| 3 | Industrials and building materials in loans and private credit | Fitch puts industrial private-credit defaults at 9.7% (same post). JPMorgan expects loan defaults to double to 4.5% in 2027 and names software and building materials (DEBT SERIOUS, 21 Nov 2026, citing Bloomberg). Against: the ISM is 55.5. | `evidence_weighted` on the rate leg. `PM_assumption` on the demand leg. |
| 4 | Sponsor-owned software with floating-rate loans | "It is not defaults that software should fear, but rather refinancing" (DEBT SERIOUS, 12 Nov 2026). Lending-fund loans marked below 90 rose from 7.7% to 11.5% of portfolios in a year (same). Against: Fitch's software default rate is 0.6% (@junkbondinvest, 2 Nov 2026). | `evidence_weighted` for Gate 1. The sources disagree on the outcome. |
| 5 | Single-B and CCC issuers with 2027 to 2029 maturities | CCC issuers would pay about 8 points over their coupon (@junkbondinvest, 30 Oct 2026). $131bn of loans trade below 80. 62% are rated CCC+ or lower and 53% mature within three years (@junkbondinvest, 29 Oct 2026). A CCC maturity wall starts in 2027 (`evidence/email.md`, thread 1a111176bacab241). Most CCC names go to the "already priced" list. | `evidence_weighted` |
| 6 | Non-bank lenders and lending funds | Private-credit default rate 6.3%, a record (Fitch, via DEBT SERIOUS, 31 Oct 2026). Of private debt still due in 2027, the share marked below 90 doubled from 15% to 31% (@junkbondinvest, 1 Nov 2026). The grid says funding cost rises faster than loan yields. | `evidence_weighted` |
| 7 | HY real estate and homebuilders | Mortgage rate 7.28%. The grid gives this sector the largest "higher rates" move among HY sectors outside technology (+40bp). Grid moves are judgement. | `PM_assumption` |
| 8 | BBB- issuers with a wide market-implied gap | A downgrade forces IG funds to sell (Willer ch11). In acute stress the lowest IG ratings underperform the most (Willer ch11). One large AI borrower sits one notch above junk (`thesis.md`). | `PM_assumption` |

**Least likely to be flagged:** IG consumer non-cyclical, IG utilities, and energy while oil holds near $90. This follows the grid's sector rows, which are judgement. Label: `PM_assumption`.

**By tier.** Single-B carries the most new pressure. CCC is mostly already priced. BB is the least exposed, with a step-up near 1 point. BBB- is a cliff risk, not a coverage risk.

One caution on these sources. The eight X accounts came from one person's follow list and are not independent (`thesis.md`, Limits). Most of the facts in this table come from one account.

---

## 5. How Parts A and B connect

- The screen's two gates mirror the two branches of the tree. Gate 1 bites if inflation persists. Gate 2 bites if growth slows.
- At 25% for both together, the screen is a watchlist tool today. It is not a base case.
- Gate 1 alone matters in a larger share of outcomes. The grid gives "higher rates" 37% over six months as `evidence_weighted` (`report.md`).
- Dalio's six-month lead says run the screen before the ISM turns, not after (Big Debt Crises, ch02).

## 6. What I did not do

- I did not run `macro-state-parser`. No panel exists.
- I did not compute Willer's consumption indicator, the soft-against-hard data rule or the maximum-volatility z-score. I report direction only for the first. `report.md` covers the third.
- I did not run the screen on any issuer.
- I modified nothing in the repo.

## 7. Missing data

1. **The warehouse cannot run this screen or its backtest.** I queried `marketdb` on 2026-11-23. TRACE holds 15 issuers from 2023-05-30 to 2025-09-30. Thirteen of the fifteen are large investment-grade names. CRSP daily holds 30 stocks from 2019 to 2021. Neither covers 2022, and neither covers HY.
2. **Fundamentals.** No source here holds interest cost, maturities, floating share or margins by issuer. This needs Compustat or parsed 10-K and 10-Q filings, point in time.
3. **Bond terms.** Coupons, maturities and floating flags by bond. This needs Mergent FISD or similar.
4. **Rating history** with dates, to score downgrades in the backtest.
5. **Private borrowers.** Loan-only and private-credit borrowers file nothing public. Lending-fund holdings in SEC filings are the nearest proxy. @junkbondinvest warns that payment-in-kind share does not predict non-accruals cleanly: "you have to read the portfolio" (5 Nov 2026).
6. **Labour and energy cost by issuer.** Disclosure is patchy. The proxy in variable 7 is rough.
7. **ISM sub-indexes** (new orders, inventories) and the Citi data change indexes, for Willer's two leading rules.
8. **A macro panel** for `macro-state-parser`.
9. **Sector spread levels.** Free data has none (`report.md`, Limits).
10. **Independent evidence.** Several sector facts rest on one X account. The Fitch sector default rates need the original Fitch report.
