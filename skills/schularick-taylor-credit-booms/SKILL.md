---
name: schularick-taylor-credit-booms
description: "Knowledge base from \"Credit Booms Gone Bust: Monetary Policy, Leverage Cycles, and Financial Crises, 1870-2008\" by Moritz Schularick and Alan M. Taylor. Use when applying Schularick and Taylor's frameworks for credit booms, financial crisis prediction, leverage cycles, money view versus credit view, post-crisis dynamics and AUROC early-warning models, studying the paper, or referencing its regression tables."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# Credit Booms Gone Bust: Monetary Policy, Leverage Cycles, and Financial Crises, 1870-2008
**Author**: Moritz Schularick and Alan M. Taylor | **Pages**: ~33 | **Chapters**: 5 | **Generated**: 2026-11-21

The source is a journal paper with seven sections. This skill merges them into five chapter files.

## How to Use This Skill

- **Without arguments** — load core frameworks for reference
- **With a topic** — ask about `crisis prediction`, `money vs credit`, or another indexed topic; I find and read the relevant chapter
- **With chapter** — ask for `ch04`; I load that specific chapter
- **Browse** — ask "what chapters do you have?" to see the full index

When you ask about a topic not covered in Core Frameworks below, I will read
the relevant chapter file before answering.

---

## Core Frameworks & Mental Models

### 1. The three views of money and credit (ch01)
- **Money view** (Friedman and Schwartz): control aggregate bank liabilities. What banks lend is secondary.
- **Irrelevance view** (Modigliani and Miller): financial structure does not affect real decisions.
- **Credit view** (Mishkin, Bernanke, Gertler): the quantity and mechanisms of bank credit matter beyond bank money.
- Inside the credit view, ask: is credit a **propagator** of shocks (financial accelerator) or a **source** of shocks (Minsky, Kindleberger)? The paper tests "source".

### 2. Two eras of finance capitalism (ch02)
- **1870-1939**: money and credit kept a stable ratio to each other and to GDP, except the 1930s collapse. The money view is an adequate simplification.
- **1945-2008**: credit decoupled from broad money. Loan-money ratio growth went from 0.17% to 2.22% a year. Loans and assets passed prewar ratios about 1970. Log loan-money ratios stood +0.750 log points above the prewar average around 2000.
- Mechanism: higher leverage first, then funding by nonmonetary liabilities (mainly debt securities) after the 1970s.
- Consequence: runs move to wholesale funding, and deposit insurance alone no longer secures stability.
- Use within-country time variation. Do not compare credit levels across countries.

### 3. Post-crisis dynamics, then versus now (ch03)
Cumulative log level versus noncrisis trend after years 0-5 (Table 2):

| | Pre-WW2 | Post-WW2 |
|---|---|---|
| Broad money | -0.139*** | -0.077* |
| Bank loans | -0.248*** | -0.144*** |
| Bank assets | -0.156*** | -0.258*** |
| Real GDP | -0.041** | -0.079*** |
| Real investment | -0.190** | -0.257*** |
| Price level | -0.089*** | 0.007 |

- Postwar policy stopped monetary collapse and deflation. It did not reduce real losses.
- Excluding the 1930s, prewar GDP and investment effects are insignificant.
- Open question the authors raise: did implicit government insurance feed the leverage it was meant to contain?

### 4. "Credit booms gone wrong": the crisis-prediction model (ch04)
- Model: crisis dummy on five annual lags of real loan growth. OLS: `p_it = b_0i + b_1(L) Δlog CREDIT_it + b_2(L) X_it + e_it`. Logit: `logit(p_it)` on the same right-hand side.
- Preferred baseline: logit, country fixed effects, no year effects. 1,272 observations, 14 countries.
- Baseline lags: L1 -0.398, **L2 7.138***, L3 0.888, L4 0.203, L5 1.867. Sum 9.697***. Summed marginal effects 0.301. Pseudo R² 0.0659. **AUROC 0.717** (s.e. 0.0349).
- Size: one standard deviation of five-year real loan growth (0.07) adds about 2.8 percentage points to a crisis probability with a base rate under 4%.
- Out-of-sample, post-1983: AUROC 0.646 (s.e. 0.0695). In-sample on the same window: 0.763.
- Year effects lift AUROC to 0.952 but are not known ex ante. Drop them for forecasting.

### 5. The second-derivative rule (ch03, ch04)
- "It is the second derivative of loan growth that changes sign during a crisis, not the first."
- In the regressions L1 is negative and L2 is large and positive. Read the signal as a boom that has started to slow.
- Do not use negative credit growth as the crisis marker.

### 6. Credit matters, not money (ch04)

| Five lags of | Full sample AUROC | Pre-WW2 | Post-WW2 |
|---|---|---|---|
| Real loans | 0.717 | 0.763 | 0.718 |
| Real broad money | 0.681 | 0.728 | 0.659 |
| Narrow money | 0.631 | | |
| Loans / GDP | 0.743 | | |
| Loans / broad money | 0.680 | | |

- Prewar, money and credit predict equally well (AUROC equality p = 0.37).
- Postwar, the broad money model has an insignificant overall χ² (p 0.280) and fails the Kolmogorov-Smirnov test.
- Policy reading: a money "pillar" suits price stability. A credit pillar suits financial stability.

### 7. Robustness: nothing displaces credit (ch05)
- Adding five lags of real GDP growth, inflation, nominal or real short rates, or the change in investment/GDP leaves the credit lags significant. Summed credit coefficients run 10.49 to 19.32 against 9.697 in the baseline.
- Pseudo R² rises only to 0.0765-0.123. AUROC 0.725-0.770.
- **Investment booms are not safer.** Investment lags are mostly insignificant, and their sum is positive.

### 8. Asset prices and financial depth (ch05)
- Real stock price lags are jointly significant (p 0.0209) but lift AUROC only from 0.717 to 0.731.
- **Financial-depth effect**: log loans/GDP, relative to the country's own mean, raises crisis risk (1.100* alone, 1.601** with stock prices, AUROC 0.764).
- Interactions on five-year moving averages:
  - Credit growth × stock prices: -22.77, insignificant. Risk concentrates in the unwinding.
  - Credit growth × credit level: -1.243, insignificant. A credit boom is dangerous at any depth.
  - Stock prices × credit level: 4.661. AUROC rises from 0.663 to 0.714. Stock booms matter in deep financial systems and are inconsequential in shallow ones.
- Use the leveraged versus unleveraged bubble distinction (Mishkin 2008). A bubble without added leverage may carry little stability risk.

### 9. Age of Money to Age of Credit (ch05)
- The stable money-credit link broke after the Great Depression and WW2.
- The authors' conclusion: recurrent financial instability has "more often than not been the result of credit booms gone wrong".
- Credit is not a perfect predictor. It can expand to support real gains in periods of financial development.

### Limits to carry with every use
- Sample: 14 developed countries, annual data, bank-balance-sheet credit only. Securitized and nonbank credit is understated.
- The results are predictive. The authors say identification of causality needs other strategies.
- Several regression tables are damaged in the text extraction. The chapter files carry values repaired from the PDF page images, each marked "recovered from PDF p. N".

---

## Chapter Index

| # | Title | Key Frameworks |
|---|-------|----------------|
| [ch01](chapters/ch01-introduction-three-views-research-questions.md) | Introduction and Section I: Money, Credit, and Crises in the Long Run | Money / irrelevance / credit views, propagator versus source, three research questions |
| [ch02](chapters/ch02-data-and-two-eras-of-finance-capitalism.md) | Sections II-III: The Data, and Two Eras of Finance Capitalism | Data definitions, Table 1, two eras, year-effects trend, wholesale-funding fragility |
| [ch03](chapters/ch03-event-analysis-after-financial-crises.md) | Section IV: Money, Credit, and Output after Financial Crises | Crisis definition and dating, event window, Table 2, second-derivative rule |
| [ch04](chapters/ch04-credit-booms-and-crisis-prediction.md) | Section V: Credit Booms and Financial Crises | Crisis logit, Tables 3-5, ROC/AUROC, out-of-sample test, credit versus money |
| [ch05](chapters/ch05-robustness-asset-prices-financial-depth-conclusions.md) | Sections VI-VII: Robustness Tests, and Conclusions | Tables 6-8, investment-boom test, financial depth, interactions, Age of Credit |

## Topic Index

- **Age of Money / Age of Credit** → ch05
- **Asset prices, stock prices** → ch05
- **AUROC, ROC curve** → ch04, ch05
- **Bank assets, bank loans (definitions)** → ch02
- **Baseline specification** → ch04
- **Broad money as predictor** → ch04
- **Crisis dating, crisis definition** → ch03
- **Credit booms gone wrong** → ch01, ch04
- **Credit view, money view, irrelevance view** → ch01
- **Deposit insurance, Lender of Last Resort** → ch02, ch03
- **Event analysis, post-crisis losses** → ch03
- **Financial accelerator** → ch01
- **Financial depth, loans/GDP level** → ch05
- **Fisherian debt-deflation** → ch03
- **Fixed effects, year effects** → ch02, ch04
- **Interaction terms** → ch05
- **Investment booms, Lawson doctrine** → ch05
- **Leverage, loan-money ratio** → ch02
- **Marginal effects** → ch04
- **Moral hazard, implicit insurance** → ch03, ch05
- **Narrow money** → ch02, ch04
- **Nonmonetary liabilities, wholesale funding** → ch02
- **Out-of-sample forecast** → ch04
- **Policy pillar, monetary policy rule** → ch01, ch04, ch05
- **Robustness controls (GDP, inflation, interest rates)** → ch05
- **Second derivative of credit** → ch03, ch04
- **Summary statistics (Table 1)** → ch02
- **Two eras of finance capitalism** → ch01, ch02

## Supporting Files

- [glossary.md](glossary.md) — all key terms with definitions
- [patterns.md](patterns.md) — all techniques and design patterns
- [cheatsheet.md](cheatsheet.md) — quick reference tables and decision guides
- Full text: `/home/ak/.local/share/book-to-skill/fulltext/schularick-taylor-credit-booms/full_text.txt` — grep it for depth the chapter files omit (local extraction, not shipped)

---

## Scope & Limits

This skill covers the paper's content only. For hands-on implementation in your codebase,
combine with project-specific tools. For topics beyond this paper, check related skills
or ask the agent directly.

All eight figures are missing from the text extraction (seven image placeholders and one garbled chart). Only the Figure 8 legend values were read from the PDF. The crisis-date table is in an online Appendix that was not extracted. Table 1 repeats two row labels in the printed source, so those rows cannot be identified. The reference list is not summarized.
