# Cheatsheet — Credit Booms Gone Bust (Schularick and Taylor)

Chapter numbers refer to this skill's chapter files.

## Decision rules
- When choosing a crisis-risk axis, use bank credit, not money. Postwar broad money fails as a predictor (Ch 4).
- When the loan-money ratio is flat, money may proxy for credit. When it trends, it may not (Ch 2, Ch 4).
- When credit growth was high two years ago and slowed last year, raise crisis risk. The signal is the second derivative (Ch 3, Ch 4).
- When credit growth turns negative, do not treat that as the signal. It is a Great Depression artifact (Ch 3).
- When a boom funds "productive investment", do not lower the risk estimate (Ch 5).
- When an equity boom occurs at low credit to GDP, treat it as inconsequential for financial stability. Risk grows with financial depth (Ch 5).
- When credit to GDP is high relative to the country's own history, add risk independently of credit growth (Ch 5).
- When a model uses year effects, reject it for forecasting (Ch 4).
- When sizing post-crisis damage, expect no deflation postwar but full real losses (Ch 3).
- When working on emerging markets, do not assume these results carry over. The sample is 14 developed countries (Ch 4, Ch 5).

## Which aggregate predicts crises?

| Regressor (five lags) | Full sample AUROC | Pre-WW2 | Post-WW2 | Verdict |
|---|---|---|---|---|
| Real loans | 0.717 | 0.763 | 0.718 | Baseline. Works in both eras. |
| Loans / GDP | 0.743 | | | Slightly better on the full sample |
| Loans / broad money | 0.680 | | | Some success |
| Real broad money | 0.681 | 0.728 | 0.659 | Fine prewar. Fails postwar. |
| Narrow money | 0.631 | | | Lags jointly insignificant |

## Does adding X help? (baseline AUROC 0.717, pseudo R² 0.0659)

| Added | AUROC | Added lags jointly significant? |
|---|---|---|
| Real GDP growth | 0.751 | Yes, p 0.000002 |
| Inflation | 0.770 | Yes, p 0.00152 |
| Nominal short rate | 0.725 | No, p 0.566 |
| Real short rate | 0.750 | Yes, p 0.0105 |
| Change in I/Y | 0.737 | No, p 0.429 |
| Nominal stock prices | 0.727 | No, p 0.123 |
| Real stock prices | 0.731 | Yes, p 0.0209 |
| Loans/GDP level | 0.731 | Coefficient 1.100* |
| Real stocks + loans/GDP level | 0.764 | Level 1.601** |

The summed credit lag coefficients stay significant in every row.

## Thresholds and defaults

| Item | Value | Source |
|---|---|---|
| Lags of credit growth | 5 annual (2 would pass formal selection) | Ch 4 |
| Base rate of crises | just under 4% per year | Ch 4 |
| One-sigma credit shock | 0.07 in five-year average real loan growth | Ch 4 |
| Effect of one sigma | about +2.8 percentage points crisis probability | Ch 4 |
| Summed marginal effect, baseline logit | 0.301 | Ch 4 |
| Out-of-sample AUROC, post-1983 | 0.646 (s.e. 0.0695) | Ch 4 |
| Loan-money ratio growth | 0.17% a year prewar, 2.22% postwar | Ch 2 |
| Credit passes prewar ratios | about 1970 | Ch 2 |
| Crisis frequency | near zero 1945-71, 4% a year after 1971 | Ch 2 |
| Crises in sample | 79, in 14 countries, 1870-2008 | Ch 3 |

## Five years after a crisis, versus trend (Ch 3)

| Variable | Pre-WW2 | Post-WW2 |
|---|---|---|
| Broad money | -14% | -8% |
| Bank loans | -25% | -14% |
| Bank assets | -16% | -26% |
| Real GDP | -4.1% | -7.9% |
| Real investment | -19% | -26% |
| Price level | -8.9% | +0.7% |

## Tells
- Loans growing faster than deposits: leverage phase.
- Loans funded by debt securities: wholesale-run exposure.
- Bank assets falling more than loans after a shock: procyclical securities book.
- A model that predicts well only with time dummies: it has learned the global wave, not the country signal.
