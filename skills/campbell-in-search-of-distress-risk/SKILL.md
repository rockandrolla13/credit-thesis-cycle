---
name: campbell-in-search-of-distress-risk
description: "Knowledge base from the paper \"In Search of Distress Risk\" by John Y. Campbell, Jens Hilscher and Jan Szilagyi (NBER Working Paper 12362, July 2006; later Journal of Finance 2008). Use when applying the Campbell-Hilscher-Szilagyi failure model: predicting corporate bankruptcy or failure with a dynamic logit, building NIMTAAVG, TLMTA, EXRETAVG, SIGMA, RSIZE, CASHMTA, MB and PRICE, choosing predictors by forecast horizon, comparing with distance to default, screening issuers for distress, or citing the low returns of distressed stocks."
---

<!-- argument-hint: [topic, variable name, table number, or section number] -->

# In Search of Distress Risk
**Authors**: John Y. Campbell, Jens Hilscher, Jan Szilagyi | **Pages**: 54 | **Sections**: 5 plus Appendix | **Generated**: 2026-11-23

**Version used**: NBER Working Paper No. 12362, dated July 2006 (PDF created 16 June 2006). URL: https://www.nber.org/papers/w12362. File fetched from https://www.nber.org/system/files/working_papers/w12362/w12362.pdf. The paper was later published in the Journal of Finance 63(6), 2008. **The published version was not read.** Its tables, sample and numbers may differ from those here.

## How to Use This Skill

- **Without arguments** — load the core frameworks below
- **With a topic** — ask about `NIMTAAVG`, `distance to default`, or another indexed topic; I find and read the relevant section file
- **With a section** — ask for `sec03`; I load that file
- **Browse** — ask "what sections do you have?" to see the index

When you ask about a topic not covered in Core Frameworks below, I will read the relevant section file before answering.

---

## Core Frameworks & Mental Models

### 1. The question and the two-step design (Sec 1)
The literature says size and value premia pay for "distress risk". The authors test it. Step one: build a fitted probability of failure. Step two: sort stocks on it and measure returns.

### 2. Two event definitions (Sec 2)
- **Bankruptcy**: Chapter 7 or Chapter 11 filing. January 1963 to December 1998. 797 events.
- **Failure**: bankruptcy, delisting, or a D rating. January 1963 to December 2003. 1,614 events.
- Sample: 1,695,036 firm-months. COMPUSTAT quarterly data and CRSP monthly and daily data. Indicators from Kamakura (KRIS).

### 3. The model form (Sec 3, eq 1 and 4)
```
P_{t-1}(Y_it = 1) = 1 / (1 + exp(-α - β·x_{i,t-1}))
P_{t-1}(Y_{i,t-1+j} = 1 | Y_{i,t-2+j} = 0) = 1 / (1 + exp(-α_j - β_j·x_{i,t-1}))
```
A monthly dynamic logit. The second line is the probability of failure in month j given survival to then. It is a marginal probability, not a cumulative one.

### 4. The eight predictors of the "best model" (Sec 2, Sec 3, Appendix)
| Variable | Construction | Sign at 1 month |
|---|---|---|
| NIMTAAVG | Net income / (market equity + total liabilities), last four quarters, weights halving each quarter | - |
| TLMTA | Total liabilities / (market equity + total liabilities) | + |
| EXRETAVG | Log return minus S&P 500 log return, last 12 months, weights halving each quarter (φ = 2^(-1/3)) | - |
| SIGMA | Annualized SD of daily returns over three months, centred on zero | + |
| RSIZE | log(firm market equity / total S&P 500 market value) | + (weak) |
| CASHMTA | Cash and short-term investments / (market equity + total liabilities) | - |
| MB | Market-to-book ratio | + |
| PRICE | log(price per share), truncated above at $15 | - |

Rules: lag accounting data two months. Winsorise at the 5th and 95th percentiles. Adjust book assets by 10% of the market-book equity gap. Replace missing SIGMA and missing lags with cross-sectional means.

### 5. The horizon result (Sec 3.1, Table 4)
| Lag (months) | 0 | 6 | 12 | 24 | 36 |
|---|---|---|---|---|---|
| NIMTAAVG | -29.672 | -23.915 | -20.264 | -13.232 | -14.061 |
| TLMTA | 3.36 | 2.057 | 1.416 | 0.917 | 0.643 |
| EXRETAVG | -7.35 | -7.792 | -7.129 | -5.607 | -2.564 |
| SIGMA | 1.482 | 1.268 | 1.411 | 1.515 | 1.334 |
| RSIZE | 0.082 | 0.047 | -0.045 | -0.132 | -0.18 |
| CASHMTA | -2.401 | -2.397 | -2.132 | -1.37 | -1.414 |
| MB | 0.054 | 0.047 | 0.075 | 0.108 | 0.125 |
| PRICE | -0.937 | -0.468 | -0.058 | 0.212 | 0.279 |
| Constant | -9.079 | -8.069 | -9.164 | -10.233 | -10.534 |
| Pseudo R2 | 0.312 | 0.188 | 0.114 | 0.061 | 0.044 |

- **Short-term signals**: leverage and past excess returns. They decay fastest.
- **Intermediate**: profitability and cash.
- **Persistent**: volatility, market-book and size. They hold or gain.
- "Market-based variables become more important relative to accounting variables as we increase the forecast horizon."
- z statistics and Table 3 are in [sec03](chapters/sec03-logit-model-of-bankruptcy-and-failure.md).

### 6. Relative weight of each predictor (Sec 3)
One-standard-deviation move from sample means: leverage +156%, volatility +64%, price -56%, profitability -44%, past return -28%, cash -21%, market capitalization +17%, market-book +9%.

### 7. Against the benchmarks (Sec 3, Sec 3.2, Table 5)
- Against the Shumway five-variable model: pseudo R2 rises from 0.27 to 0.31 (failure, 1963-2003).
- Against distance to default: DD alone has an R2 of 0.159 at lag 0. The best model has 0.312. Adding DD leaves it at 0.312.
- Out of sample (1981-2003, coefficients re-estimated each year on prior data): 0.310 at lag 0, 0.108 at 12 months, 0.039 at 36 months.
- This version has no classification-accuracy table. Fit is judged by pseudo R2 and by Figure 1.

### 8. What the firm model misses (Sec 3.3)
The model tracks the aggregate failure rate but underpredicts in much of the 1980s and overpredicts in 1974-5 and the early 1990s. Year dummies stay significant. The AAA-BAA spread and the Treasury term spread interact with size and leverage (fn 11, no coefficients given).

### 9. The return finding (Sec 4, Table 6)
Sort each January, 1981 to 2003, on the 12-month failure probability. Value-weight. Hold one year.
- Mean return in excess of the market falls from 3.39% a year (safest 5%) to -16.30% (top 1%).
- Long safest decile, short most distressed decile: 10.20% a year (t 1.90). CAPM alpha 12.60 (2.36). Three-factor alpha 22.89 (6.15). Four-factor alpha 12.18 (3.45).
- Distressed portfolios have higher market beta, HML and SMB loadings, volatility and positive skewness.
- The effect holds in every size and book-to-market quintile. It is strongest in small stocks.
- "Stocks with a high risk of failure have low average returns, despite their high loadings on small-cap and value risk factors."

### 10. Why, according to the authors (Sec 4.1, Sec 5)
- Not an earnings-expectation error: no underperformance around announcements (Table 9).
- Not one variable: five of seven significant predictors add to it. Leverage and price work the other way (Table 10).
- Investors do see the risk: the long-short return has a 0.23 correlation with VIX changes.
- Candidates left open: valuation error, taste for skewness, private benefits of control, limits to arbitrage, and unexpected in-sample shifts (institutional ownership, correlation 0.31).
- The authors allow that it "could disappear or even reverse".

---

## Method or Case

| File | Type | Why |
|---|---|---|
| sec01 Introduction | METHOD | Sets the question and the research design |
| sec02 Data description | METHOD | Event definitions, variable construction, outlier and timing rules |
| sec03 Logit model | METHOD | Model form, coefficient tables by horizon, distance-to-default test, out-of-sample fit |
| sec06 Appendix | METHOD | Exact formulas |
| sec04 Returns on distressed stocks | METHOD with a dated CASE result | The sorting and attribution procedure is method. The return numbers are one historical sample: US stocks, 1981-2003 |
| sec05 Conclusion | CASE-leaning | Interprets the 1981-2003 result and its possible causes |

The coefficient values in Tables 3 and 4 are estimates from US listed firms, 1963-2003. The method carries over. The numbers are sample-specific.

## Use for Credit and Macro Questions

- **Issuer screening**: this is the paper's main use. It gives a tested list of failure predictors, their construction, and their relative weight by horizon. It needs listed equity. It says nothing on private issuers.
- **Mapping to the issuer pressure screen**:
  - *Equity drawdown*: tested, in three forms. EXRETAVG (12-month weighted excess return), PRICE (log price capped at $15) and SIGMA (volatility). All significant. The return signal fades after 12 months.
  - *Net leverage*: partly. TLMTA is **total liabilities** over market assets. It is gross and is not debt over earnings. Cash enters separately as CASHMTA. Leverage is the strongest one-month signal and decays fast.
  - *Margin change*: partly. NIMTAAVG is the **level** of net income over market assets with a one-year weighted history. The paper tests no change in margin.
  - *Interest coverage*: not tested. The closest items are NIMTAAVG and CASHMTA, which the authors motivate as liquid assets "available to make interest payments". No interest expense variable appears.
  - *Refinancing need*: not tested. Maturity enters only through the distance-to-default debt proxy (short-term plus half of long-term debt). Current and acid test ratios were tried and were slightly worse than CASHMTA (fn 8).
  - *Cyclicality*: not tested as a firm predictor. The paper shows distressed portfolios have high market beta and fall when VIX rises, and that year effects remain.
  - *Not tested at all*: floating-rate share, coupon step-up, cost intensity, customer concentration, spread per turn of leverage.
  - *In the paper and not in the screen*: SIGMA, RSIZE, MB, CASHMTA and PRICE.
- **Credit spreads**: no bond or CDS spread data. Two indirect points only. The aggregate AAA-BAA spread helps predict bankruptcy through interactions (fn 11). The authors link the VIX sensitivity of distressed stocks to the known credit spread and VIX correlation.
- **Debt-financed investment booms**: little. Table 1 shows failures jumping after 1998, which the authors tie to young firms listed in the late-1990s boom. High MB predicts failure more strongly at long horizons.
- **Inflation and Fed regimes**: nothing.
- **Pricing of risk**: a warning. In this sample equity investors recognised distress and were not paid for it. Do not assume a measured default risk is priced.

## Trust Notes

- **Extraction**: technical mode ran for 22 minutes on a loaded machine without output and was stopped. Text mode (pdftotext) was used. The ten tables came through as aligned text. Every decimal in this skill was checked by script against the extracted text. Table cells could still be misaligned in ways a number match does not catch.
- **Version**: July 2006 NBER working paper, not the 2008 Journal of Finance article. Do not cite these numbers as the published ones.
- **Text and table disagree** on the headline returns. The text says 10.0%, 12.4%, 22.7%, 12.0% and -17.0%. Table 6 prints 10.20, 12.60, 22.89, 12.18 and -16.30. Both are in sec04.
- **Table 7 Panel A, "Small" row**: its five cells duplicate Table 8 Panel A's "Low" row and do not reproduce the row's own printed difference. Treat those five cells as a source error.
- **Book asset adjustment sign**: the Appendix formula prints `BE - ME`. The Section 2 text implies `ME - BE`. Unresolved.
- **NIMTAAVG subscript**: the last term prints as `t-9,t-12`. The Appendix says "seven" variables are winsorised where Section 2 says "all".
- **Figures 1 to 6 were not read.** They are charts. Only the authors' descriptions of them are used.
- **Formulas**: eq 2, eq 3, the SIGMA estimator and the DD equations were rebuilt from multi-line layout. Check them against the PDF before coding.
- **Not in the paper**: MB has no formula. Cash has no Compustat item number. The "small positive values" for negative book equity are not stated. The one-standard-deviation impacts name no column. Phat has no stated time unit.
- **No accuracy table** in this version. Do not quote a hit rate or accuracy ratio from this skill.

---

## Section Index

| # | Title | Key content |
|---|-------|-------------|
| [sec01](chapters/sec01-introduction.md) | Introduction | Distress-premium conjecture, two failure definitions, four contributions, heart-attack rule |
| [sec02](chapters/sec02-data-description.md) | Data description | Event indicators, ten variables, winsorising, two-month lag, Tables 1 and 2 |
| [sec03](chapters/sec03-logit-model-of-bankruptcy-and-failure.md) | A logit model of bankruptcy and failure | Eq 1-4, Tables 3, 4, 5, impact ranking, horizons, distance to default, out-of-sample R2, time effects |
| [sec04](chapters/sec04-risks-and-returns-on-distressed-stocks.md) | Risks and average returns on distressed stocks | Portfolio method, Tables 6-10, VIX and institutional links, explanations |
| [sec05](chapters/sec05-conclusion.md) | Conclusion | Two contributions, three candidate explanations, prior studies |
| [sec06](chapters/sec06-appendix-variable-construction.md) | Appendix | Ratio formulas, asset adjustment, SIGMA, distance to default |

## Topic Index

- **Aggregate failure rate / time effects** → sec03
- **Bankruptcy indicator** → sec01, sec02
- **Book asset adjustment** → sec02, sec06
- **CASHMTA (cash)** → sec02, sec03, sec06
- **Delisting returns** → sec04
- **Distance to default (DD)** → sec03, sec06
- **Earnings announcement test** → sec04
- **EXRET / EXRETAVG** → sec02, sec03, sec06
- **Failure indicator** → sec01, sec02
- **Fama-MacBeth return attribution** → sec04
- **Horizon effects** → sec03
- **Industry effects (FIRE)** → sec03
- **Institutional ownership** → sec04, sec05
- **Long-short portfolios (LS1090, LS2080)** → sec04
- **MB (market-book)** → sec02, sec03, sec04
- **NIMTA / NIMTAAVG** → sec02, sec03, sec06
- **Out-of-sample R2** → sec03
- **PRICE** → sec02, sec03
- **Pseudo R2** → sec03
- **RSIZE** → sec02, sec03, sec06
- **Shumway model** → sec01, sec03
- **SIGMA** → sec02, sec03, sec06
- **Size and value double sorts** → sec04
- **Skewness** → sec04, sec05
- **TLMTA (leverage)** → sec02, sec03, sec06
- **VIX** → sec04
- **Winsorising** → sec02, sec06
- **Z-score and O-score** → sec01, sec05

## Supporting Files

- [glossary.md](glossary.md) — all key terms with definitions
- [patterns.md](patterns.md) — the paper's procedures as reusable patterns
- [cheatsheet.md](cheatsheet.md) — horizon table, decision rules, thresholds
- Source PDF: `/home/ak/Documents/PapersForThemes/campbell-in-search-of-distress-risk/w12362.pdf`
- Full text: `/home/ak/.local/share/book-to-skill/fulltext/campbell-in-search-of-distress-risk/full_text.txt` — grep it for depth the section files omit (local extraction, not shipped)

---

## Scope & Limits

This skill covers the working paper only. It reports the authors' rules and findings as theirs. It makes no trade recommendation. The return results are for US stocks, 1981-2003. The failure coefficients are for US listed firms, 1963-2003.
