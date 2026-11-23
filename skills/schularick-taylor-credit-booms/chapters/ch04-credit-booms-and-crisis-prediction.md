# Chapter 4: Section V — Credit Booms and Financial Crises

## Core Idea
A logit model with five annual lags of real loan growth predicts banking crises in 14 developed countries (baseline AUROC 0.717). Credit beats money: broad money predicts as well as loans before WW2 but fails after it. The second lag carries the signal, and the first lag is negative, so the pattern is a boom that then slows.

## Frameworks Introduced
- **The crisis-prediction model** (Section V). The dependent variable is a dummy equal to one in a crisis year for country i, year t.
  - OLS Linear Probability form, as printed: `p_it = b_0i + b_1(L) Δlog CREDIT_it + b_2(L) X_it + e_it`
  - Logit form, as printed: `logit(p_it) = b_0i + b_1(L) Δlog CREDIT_it + b_2(L) X_it + e_it` (recovered from PDF p. 16). The right-hand side is identical to the OLS form. `logit(p) = ln(p / (1 - p))` is the log of the odds ratio, and L is the lag operator. The page prints the difference operator as "D log".
  - `CREDIT`: total bank loans deflated by the CPI.
  - `b_1(L)`: lag polynomial with lag orders one and above only. Five annual lags are used.
  - `b_2(L) X`: optional controls (Chapter 5).
  - When to use: to turn a credit-growth history into a crisis probability signal.
- **Lag-length rule** (footnote 13): AIC, BIC and likelihood ratio tests suggest two lags would do in most cases. The authors keep five because higher lags are sometimes significant and credit booms last many years.
- **Fixed-effects choice** (Section V).
  1. Country effects: included, never statistically significant.
  2. Year effects: highly significant in OLS and lift AUROC to 0.952. This shows a common global time component in crises.
  3. Year effects are dropped anyway. They are not known ex ante, so they are useless for forecasting.
  4. Logit with year effects cannot be estimated. With small N and large T, conditional fixed effects use only years with variation in the outcome, cutting 1,272 observations to 140.
  5. Preferred baseline: logit, country effects, no time effects (specification 5, repeated as 6).
- **ROC / AUROC evaluation** (Section V).
  - Classifier: call a crisis when the model's linear prediction exceeds threshold c.
  - ROC curve: true positive rate against false positive rate over all c. An informative classifier lies above the 45-degree line.
  - AUROC: area under the curve. Null value 0.5 (coin toss), perfect value 1, asymptotically normal.
  - Why use it: it is independent of the policymaker's cutoff. The authors decline to pick a cutoff.
  - Cutoff logic: be more aggressive if a missed crisis is costly, less if false alarms are costly. Raise the bar when crises are rare (Pepe 2003).
- **In-sample versus out-of-sample test** (Section V): restrict forecasts to post-1983 (350 country-year observations). Compare full-sample predictions, which have look-ahead bias, with rolling regressions using lagged data only.
- **"Credit matters, not money"** (Section V): the authors' summary of Tables 4 and 5.
  - Why: credit better captures time-varying features of bank balance sheets such as leverage and nonmonetary liabilities.
- **Second-derivative signature** (Section V): lag 1 coefficient negative, lag 2 large and positive. When the second derivative of credit changes sign, trouble is likely to follow (Biggs, Mayer and Pick 2009).

## Key Concepts
- **Marginal effect at the means**: change in predicted crisis probability per unit of lagged loan growth, evaluated at variable means.
- **Sum of lag coefficients**: the total effect of sustained credit growth over five years. About 0.40 in OLS, about 10 in logit, 0.301 as summed marginal effects in the baseline.
- **One-standard-deviation effect**: five-year average real loan growth has a standard deviation of about 0.07. With the OLS sum of 0.40 this raises crisis probability by about 2.8 percentage points.
- **Sample crisis frequency**: just under four percent per year.
- **Incidental parameters problem**: here it afflicts the T dimension, the opposite of typical microeconometric panels.
- **Kolmogorov-Smirnov test**: tests whether the signal distributions differ between crisis and noncrisis states. Equivalent to testing the ROC curve's maximum height above the diagonal (Tp minus Fp).
- **"Pillar"**: a quantitative indicator used in monetary policymaking. The authors say a money pillar suits price stability, and a credit pillar suits financial stability.

## Mental Models
- Think of the model as a boom detector with a turn detector attached. High growth two years back raises risk. Low growth last year raises it further.
- Use AUROC to rank candidate indicators before arguing about thresholds.
- Treat a money aggregate as a credit proxy only while loans/money is flat (Chapter 2). Table 5 is the test of that rule.
- Read a 2.8 point move against a base rate under 4 percent. A one-sigma credit shock moves the probability by most of the base rate.

## Anti-patterns
- **Forecasting with year effects**: they give AUROC 0.952 but use information unavailable ex ante.
- **Using narrow money**: specification 8 "falls apart". The authors blame money-multiplier instability.
- **Using broad money postwar**: specification 14 has a much lower AUROC, and its ROC fails the Kolmogorov-Smirnov test.
- **Trusting in-sample fit alone**: all full-sample forecasts carry look-ahead bias even with lagged regressors.
- **Relying on the Linear Probability model**: its fitted values are not confined to the unit interval.

## Reference Tables

Regressor in Tables 3-5 unless noted: lags of Δlog(loans / P), real loan growth. Standard errors in parentheses. Logit standard errors are robust. `***` 1 percent, `**` 5 percent, `*` 10 percent.

**Table 3 — Financial Crisis Prediction, OLS and Logit Estimates**

| | (1) OLS, no FE | (2) OLS, country FE | (3) OLS, country + year FE | (4) Logit, no FE | (5) Logit, country FE, baseline |
|---|---|---|---|---|---|
| L1 | -0.0281 (0.0812) | -0.0273 (0.0815) | -0.0489 (0.0801) | -0.257 (2.077) | -0.398 (2.110) |
| L2 | 0.301*** (0.0869) | 0.302*** (0.0872) | 0.320*** (0.0833) | 6.956*** (2.308) | 7.138*** (2.631) |
| L3 | 0.0486 (0.0850) | 0.0478 (0.0853) | 0.00134 (0.0819) | 1.079 (2.826) | 0.888 (2.948) |
| L4 | 0.00494 (0.0811) | 0.00213 (0.0814) | 0.0346 (0.0782) | 0.290 (1.282) | 0.203 (1.378) |
| L5 | 0.0979 (0.0746) | 0.0928 (0.0752) | 0.136* (0.0729) | 2.035 (1.607) | 1.867 (1.640) |
| Observations / groups | 1,272 / 14 | 1,272 / 14 | 1,272 / 14 | 1,272 / 14 | 1,272 / 14 |
| Sum of lag coefficients | 0.425*** (0.123) | 0.417*** (0.126) | 0.443*** (0.136) | 10.10*** (2.590) | 9.697*** (2.920) |
| Test all lags = 0 (F for OLS, χ² for logit) | 4.061***, p 0.00116 | 3.871***, p 0.00174 | 4.328***, p 0.000661 | 24.95***, p 0.000143 | 17.23***, p 0.00408 |
| Test country effects = 0 | n/a | 0.71, p 0.754 | 0.84, p 0.617 | n/a | 7.67, p 0.864 |
| Test year effects = 0 | n/a | n/a | 4.15***, p 0.0001 | n/a | n/a |
| R² (pseudo R² for logit) | 0.016 | 0.023 | 0.290 | 0.0434 | 0.0659 |
| Pseudolikelihood | n/a | n/a | n/a | -210.8 | -205.8 |
| Overall test statistic (F for OLS, χ² for logit) | 4.061***, p 0.0012 | 1.638*, p 0.0445 | 4.184***, p 0.00001 | 24.95***, p 0.000143 | 36.21***, p 0.00663 |
| AUROC | 0.673*** (0.0357) | 0.720*** (0.0341) | 0.952*** (0.00865) | 0.673*** (0.0360) | 0.717*** (0.0349) |

The four test rows, the overall test row and the AUROC row are recovered from PDF p. 17.

What each specification tests:

| Spec | Question |
|---|---|
| 1 | Does lagged real loan growth predict crises in pooled data? |
| 2 | Do time-invariant country differences matter? No (p = 0.75 in the text). |
| 3 | Is there a common global time component? Yes, highly significant. |
| 4 | Does the result survive a model bounded to probabilities? |
| 5 | Preferred baseline for all later tables. |

**Table 4 — Baseline Model and Alternative Measures of Money and Credit** (logit, country effects, full sample)

Each column replaces the five lags of real loans with five lags of another aggregate.

| | (6) Baseline: real loans | (7) Real broad money | (8) Narrow money | (9) Loans / GDP | (10) Loans / broad money |
|---|---|---|---|---|---|
| L1 | -0.398 (2.110) | -1.051 (2.771) | -2.504 (1.806) | 2.091 (2.235) | 0.601 (2.383) |
| L2 | 7.138*** (2.631) | 5.773*** (2.181) | 2.303 (1.781) | 7.627*** (2.135) | 5.842** (2.327) |
| L3 | 0.888 (2.948) | 3.515 (2.329) | 1.768 (1.664) | 3.569 (2.386) | 2.092 (2.048) |
| L4 (recovered from PDF p. 20) | 0.203 (1.378) | -1.535 (2.287) | -2.880* (1.51) | 2.333* (1.405) | 1.613 (1.766) |
| L5 | 1.867 (1.64) | 3.077 (2.256) | 1.373 (1.63) | 3.164** (1.583) | 0.497 (2.37) |
| Marginal effects L1 to L5 | -0.0124, 0.222, 0.0276, 0.00629, 0.0580 | -0.0350, 0.192, 0.117, -0.0511, 0.102 | -0.0888, 0.0817, 0.0627, -0.102, 0.0487 | 0.0598, 0.218, 0.102, 0.0668, 0.0905 | 0.0196, 0.190, 0.0681, 0.0525, 0.0162 |
| Sum of marginal effects | 0.301 | 0.326 | 0.00211 | 0.538 | 0.346 |
| Observations / groups | 1,272 / 14 | 1,348 / 14 | 1,381 / 14 | 1,245 / 14 | 1,224 / 14 |
| Sum of lag coefficients | 9.697*** (2.920) | 9.779*** (3.400) | 0.0596 (3.240) | 18.78*** (3.651) | 10.65*** (4.053) |
| Test all lags = 0, χ² | 17.23***, p 0.00408 | 17.77***, p 0.00324 | 6.557, p 0.256 | 29.85***, p 0.000016 | 10.62*, p 0.0594 |
| Test country effects = 0, χ² | 7.674, p 0.864 | 8.755, p 0.791 | 8.834, p 0.785 | 8.012, p 0.843 | 9.140, p 0.762 |
| Pseudo R² | 0.0659 | 0.0487 | 0.0381 | 0.0923 | 0.0497 |
| Pseudolikelihood | -205.8 | -224.6 | -237.4 | -198.9 | -201.5 |
| Overall test, χ² | 36.21***, p 0.00663 | 36.81***, p 0.00555 | 17.37, p 0.498 | 47.77***, p 0.000163 | 19.82, p 0.343 |
| AUROC | 0.717*** (0.0349) | 0.681*** (0.0294) | 0.631*** (0.0339) | 0.743*** (0.0337) | 0.680*** (0.0378) |

The L4 row and every row from "Sum of lag coefficients" down are recovered from PDF p. 20. The page prints the standard errors with a leading minus sign in place of parentheses (for example "-2.11"). They are shown here in parentheses.

What each specification tests:

| Spec | Question | Authors' verdict |
|---|---|---|
| 7 | Can the liability side (broad money) proxy for credit? | Slightly weaker fit and AUROC. Could "potentially proxy", later qualified by Table 5. |
| 8 | Does base/narrow money work? | Model falls apart. |
| 9 | Does scaling loans by GDP work? | Yes. Outperforms slightly on fit and AUROC. |
| 10 | Does the leverage ratio loans/broad money work? | Some success. |

**Table 5 — Baseline Model with Pre-WW2 and Post-WW2 Samples** (logit, country effects)

| | (11) Pre-WW2, loans | (12) Post-WW2, loans | (13) Pre-WW2, broad money | (14) Post-WW2, broad money |
|---|---|---|---|---|
| L1 | 2.249 (2.362) | -0.316 (3.005) | -0.227 (3.014) | 2.705 (4.438) |
| L2 | 7.697** (3.221) | 8.307*** (2.497) | 7.393** (3.004) | 4.719** (2.375) |
| L3 | 2.890 (3.056) | 2.946 (2.687) | 4.077 (2.915) | 4.060* (2.170) |
| L4 | 2.486 (1.587) | 0.755 (2.623) | -0.249 (1.982) | -0.838 (5.359) |
| L5 | 4.260** (1.735) | -1.749 (3.204) | 4.844* (2.647) | 0.808 (4.016) |
| Observations / groups | 510 / 13 | 706 / 14 | 585 / 13 | 708 / 14 |
| Marginal effects L1 to L5 | 0.0873, 0.299, 0.112, 0.0965, 0.165 | -0.00642, 0.169, 0.0598, 0.0153, -0.0355 | -0.0102, 0.332, 0.183, -0.0112, 0.218 | 0.0617, 0.108, 0.0926, -0.0191, 0.0184 |
| Sum of marginal effects | 0.760 | 0.202 | 0.711 | 0.261 |
| Sum of lag coefficients | 19.58*** (4.921) | 9.943 (6.056) | 15.84*** (5.119) | 11.45* (6.022) |
| Test all lags = 0, χ² | 19.20***, p 0.00176 | 12.44**, p 0.0292 | 13.53**, p 0.0189 | 12.13**, p 0.0330 |
| Test country effects = 0, χ² | 6.369, p 0.932 | 5.348, p 0.945 | 11.74, p 0.549 | 5.917, p 0.920 |
| Pseudo R² | 0.130 | 0.0771 | 0.0855 | 0.0476 |
| Pseudolikelihood | -106.4 | -83.97 | -126.2 | -86.71 |
| Overall test, χ² | 40.21***, p 0.00195 | 36.44***, p 0.00401 | 35.95***, p 0.00716 | 19.89, p 0.280 |
| AUROC | 0.763*** (0.0391) | 0.718*** (0.0691) | 0.728*** (0.0361) | 0.659*** (0.0600) |

Rows L2 to L4, coefficients and standard errors, are recovered from PDF p. 21.

Source note: the Netherlands is dropped from the prewar logits because it has no crisis in the usable sample, so N = 13.

What each specification tests: does the credit model hold in each era (11, 12), and does broad money hold in each era (13, 14)? Credit holds in both. Broad money holds only prewar.

**Common-sample ROC comparison (Figure 8, numbers from the text)**

| Period | Common N | Credit AUROC | Money AUROC | AUROC equality test | Reading |
|---|---|---|---|---|---|
| Pre-WW2 | 486 | 0.7665 | 0.7392 | p = 0.37, equality "passed easily" | ROC curves almost overlap |
| Post-WW2 | 700 | 0.7196 | 0.6567 | p = 0.237 | Money ROC lies below credit ROC at almost all points. Only the postwar money model fails the Kolmogorov-Smirnov test. |

The four common-sample AUROCs are the Figure 8 legend values (recovered from PDF p. 22). They differ slightly from Table 5 because the samples differ.

**Out-of-sample test, post-1983, 350 observations**

| Forecast | AUROC | s.e. |
|---|---|---|
| In-sample (full-sample fit) | 0.763 | 0.0635 |
| Out-of-sample (rolling, lagged data only) | 0.646 | 0.0695 |

The authors say the out-of-sample AUROC is significant at better than the 5 percent level. Footnote 14 gives a benchmark: newly published prostate cancer diagnostic tests have AUROCs of about 0.75.

## Worked Example
From coefficient to probability, as the authors do it (Section V):

1. Take the OLS models. The five lag coefficients sum to about 0.40.
2. Take the standard deviation of five-year average real loan growth: about 0.07.
3. Multiply: 0.40 × 0.07 ≈ 0.028. A one standard deviation rise in real loan growth raises annual crisis probability by about 2.8 percentage points.
4. Compare with the base rate: sample crisis frequency is just under 4 percent.
5. Cross-check with the logit baseline. The lag coefficients sum to about 10. Converted to marginal effects at the means they sum to 0.301, a little below the OLS 0.40.
6. Look at the lag shape. L1 is -0.398 and L2 is 7.138 in the baseline. Postwar (specification 12) L1 is -0.316 and L2 is 8.307. The authors read this as the second derivative of credit, not the first, raising crisis risk.

## Key Takeaways
1. Use five lags of real loan growth in a country-fixed-effects logit as the baseline crisis signal.
2. A one-sigma credit boom adds about 2.8 points to a crisis probability whose base rate is under 4 percent.
3. Baseline AUROC is 0.717 in-sample and 0.646 out-of-sample post-1983. Informative, far from perfect.
4. Loans/GDP growth (AUROC 0.743) does slightly better than real loan growth. Narrow money (0.631, lags jointly insignificant) does not work.
5. Postwar, use credit, not broad money: AUROC 0.718 against 0.659, and the money model's overall χ² is insignificant (p 0.280).
6. Watch for a boom followed by deceleration. The L2-positive, L1-negative pattern is the signature.
7. Crises have a strong common global component that cannot be used for forecasting.

## Connects To
- **Ch 2**: the decoupling of credit from money explains Table 5.
- **Ch 3**: same crisis definition, and the second-derivative rule from footnote 10.
- **Ch 5**: controls, asset prices and financial depth added to this baseline.
- **Borio and Lowe (2002, 2003)**: cited as closest prior work, focused on cumulative effects and the lagged credit signal.
- **Early-warning literature**: Demirgüç-Kunt and Detragiache (1998), Kaminsky and Reinhart (1999), Gourinchas, Valdes and Landerretche (2001).

## Extraction Notes
- The logit equation, Tables 3, 4 and 5 and the Figure 8 legend were repaired from the PDF page images (PDF pp. 16, 17, 20, 21, 22). PDF page n is journal page 1028 + n. The text extraction of these items is still damaged, so grep on the full text will not reproduce them.
- No reassembled cell changed value. The repair added the Table 4 L4 coefficients, the Table 4 pseudolikelihood row, the Table 3 overall test row and the Figure 8 AUROCs.
- Table 4, as printed on the page, shows standard errors with a minus sign instead of parentheses. This is in the source, not an extraction fault.
- Figure 7 (baseline ROC curve, area 0.717) and the Figure 8 curves are not reproduced. Only the Figure 8 legend values are used.
- Source inconsistencies, confirmed on the page images and recorded as found. The text says the model uses "long-run annual data for 12 countries" (PDF p. 15), while the tables report 14 groups and the text elsewhere says 14 countries. Footnote 13 cites "Table 2" for the significance of higher-order lags (PDF p. 16), while the lag coefficients are in Table 3. The text says the postwar credit and money AUROCs "are different, with a p-value of 0.237" (PDF p. 23), which is not significant at conventional levels.
