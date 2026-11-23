# Patterns — Credit Booms Gone Bust (Schularick and Taylor)

Techniques the paper uses, stated so they can be reused. Chapter numbers refer to this skill's chapter files.

## Lagged-credit crisis logit (Ch 4)
**When to use**: you need a crisis-risk signal from a credit history for a developed economy.
**How**: regress a crisis dummy on five annual lags of Δlog(real bank loans), logit, country fixed effects, no time effects. Read the sum of lag coefficients and the summed marginal effects (baseline 9.697 and 0.301).
**Trade-offs**: AUROC is 0.717 in-sample and 0.646 out-of-sample. Informative but far from perfect. Pseudo R² is only 0.0659.

## Second-derivative signature (Ch 3, Ch 4)
**When to use**: timing within a credit boom.
**How**: look for strong growth two years back and slower growth last year. In the baseline, L2 = 7.138*** and L1 = -0.398. Postwar, L2 = 8.307*** and L1 = -0.316.
**Trade-offs**: L1 is never individually significant. The authors call the pattern "suggestive".

## AUROC model comparison (Ch 4)
**When to use**: ranking candidate indicators without committing to a cutoff.
**How**: compute AUROC and its standard error for each model. Test against 0.5. Compare models on a common sample with an AUROC equality test and a Kolmogorov-Smirnov test.
**Trade-offs**: says nothing about the best threshold. That depends on the costs of misses and false alarms and on how rare crises are.

## Era split at WW2 (Ch 2, Ch 3, Ch 4)
**When to use**: any long-run money or credit relationship.
**How**: estimate separately for 1870-1939 and 1945-2008. Exclude 1914-1919, 1939-1947 and Germany 1920-1925.
**Trade-offs**: halves the sample. Post-WW2 standard errors widen (AUROC s.e. 0.0691 against 0.0391 prewar).

## Money-versus-credit horse race (Ch 4)
**When to use**: testing whether a liability-side aggregate can stand in for credit.
**How**: swap the five loan lags for five lags of the alternative (broad money, narrow money, loans/GDP, loans/money). Repeat by era.
**Trade-offs**: on the full sample broad money looks adequate (AUROC 0.681). Only the era split exposes its postwar failure (0.659, overall χ² p 0.280).

## One-control-at-a-time robustness (Ch 5)
**When to use**: guarding a baseline against omitted-variable bias.
**How**: add five lags of one control. Check the credit coefficients, the joint test on the added lags, pseudo R² and AUROC.
**Trade-offs**: controls are never entered jointly in Table 6, so combined effects are untested there.

## Financial-depth level term (Ch 5)
**When to use**: asking whether a bigger financial system is riskier.
**How**: add log(loans/GDP) to the fixed-effects logit. The coefficient then measures depth relative to the country's own average.
**Trade-offs**: causality is unresolved. The authors list complexity, moral hazard and lax regulation as candidates.

## Moving-average interactions (Ch 5)
**When to use**: testing whether two risk factors compound.
**How**: replace lags with five-year moving averages that exclude the current year. Add the product term.
**Trade-offs**: predictive ability drops (AUROC 0.663 against 0.717). Timing is blurred, which the authors flag when reading the credit × stock result.

## Post-crisis event window (Ch 3)
**When to use**: measuring the cost of a crisis and the policy response.
**How**: compare the cumulative log level of each variable after years 0-5 with the noncrisis trend. Rerun without the 1930s.
**Trade-offs**: effects are relative to trend, not absolute. The 2008-2009 episode is outside the event sample.

## Multi-source crisis dating (Ch 3)
**When to use**: building a crisis chronology.
**How**: merge two documentary chronologies, corroborate against two more, then ask country specialists to confirm. Code a crisis when a significant part of the banking system is affected.
**Trade-offs**: "systemic" is a judgment call. The authors admit using discretion for comparability.

## Year-effects global trend (Ch 2)
**When to use**: showing an average cross-country trend when national definitions differ.
**How**: estimate `x_it = a_i + b_t + e_it` and plot `b_t`.
**Trade-offs**: hides country heterogeneity. Check a by-country plot.

## Rolling out-of-sample check (Ch 4)
**When to use**: testing a predictor for look-ahead bias.
**How**: restrict the forecast window (post-1983, 350 observations). Compare full-sample predictions with rolling regressions on lagged data only.
**Trade-offs**: small evaluation sample and wide standard errors (0.0695).
