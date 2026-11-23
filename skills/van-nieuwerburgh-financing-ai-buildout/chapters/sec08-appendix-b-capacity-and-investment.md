# Appendix B: Data Centers Capacity Count

**Type**: METHOD (pipeline-to-investment model) | **Source pages**: 20-25

## Core Idea
Announced pipeline is not supply. Apply realisation haircuts by completion horizon and by data quality. Then phase the dollars over four years.

## Data (App B)
- Cleanview project records, accessed September 12, 2026. US only.
- 3,423 projects. Drop 46 cancelled. 3,377 active: 1,287 operational, 462 under construction, 1,628 planned.
- Projects under construction get the same realisation treatment as planned projects.

## Step 1: impute missing capacity (App B)
- Capacity is reported for 3,010 projects and missing for 367.
- Model: log capacity on log land area, log building area and log capex, with missing-value flags. Completion-year fixed effects. Regularised county-by-state and developer effects (ridge, penalty 1, five-fold cross-validation). 18 named developer groups.
- Fit: 3,010 observations, R-squared 0.830 in logs.
- Duan smearing factor 1.1313. Imputed values are capped at 2,000 MW. The cap binds for 13 predictions.
- Imputation adds 118.2 GW in total, across 43 operational, 10 under-construction and 314 planned projects.

## Table 3: capacity by completion year, before any haircut (GW)
| Completion year | Projects | Observed | Imputed | Total |
|---|---|---|---|---|
| Before 2025 | 1,009 | 39.1 | 1.3 | 40.5 |
| 2025 | 187 | 13.6 | 0.1 | 13.8 |
| 2026 | 293 | 26.9 | 1.7 | 28.7 |
| 2027 | 405 | 41.0 | 4.7 | 45.7 |
| 2028 | 369 | 42.4 | 5.4 | 47.9 |
| 2029 | 153 | 16.7 | 1.5 | 18.2 |
| 2030 | 109 | 12.5 | 1.8 | 14.3 |
| 2031 | 60 | 11.7 | 2.5 | 14.2 |
| 2032 | 46 | 7.1 | 2.5 | 9.5 |
| After 2032 | 29 | 2.2 | 8.3 | 10.5 |
| Planned, no date | 717 | 225.6 | 88.4 | 313.9 |
| **Total** | 3,377 | 438.9 | 118.2 | 557.1 |

The 2026 row holds 98 operational projects (9.4 GW), 145 under construction (12.9 GW) and 50 planned (6.3 GW). Installed base at end-2024 is 40.5 GW.

## Step 2: realisation haircuts (Table 4). The author's assumptions
Rates apply to planned and under-construction capacity only. Operational capacity and all 2025 capacity count in full.

| Completion year | Observed: by 2032 / after | Imputed: by 2032 / after | Outcome GW: by 2032 / after / never |
|---|---|---|---|
| 2025 | in full | in full | 13.8 / 0.0 / 0.0 |
| 2026 | 90% / 0% | 80% / 0% | 26.6 / 0.0 / 2.1 |
| 2027 | 80% / 5% | 65% / 10% | 35.8 / 2.5 / 7.3 |
| 2028 | 70% / 10% | 55% / 15% | 32.7 / 5.1 / 10.1 |
| 2029 | 60% / 15% | 45% / 20% | 10.7 / 2.8 / 4.7 |
| 2030 | 50% / 20% | 35% / 25% | 6.9 / 3.0 / 4.5 |
| 2031 | 40% / 25% | 25% / 30% | 5.3 / 3.7 / 5.2 |
| 2032 | 30% / 30% | 20% / 30% | 2.6 / 2.9 / 4.1 |
| After 2032 | 0% / 50% | 0% / 50% | 0.0 / 5.2 / 5.2 |
| Planned, no date | 20% / 30% | 10% / 25% | 54.0 / 89.8 / 170.2 |
| **Total** | | | **188.3 / 114.9 / 213.5** |

Rules behind the table (App B):
- The by-2032 share falls 10 points for each year of horizon.
- Imputed capacity gets a lower share than observed capacity.
- "Never" is the residual. It covers cancellation and downsizing. Read the shares as capacity-weighted outcomes, not project cancellation probabilities.

Reasons the author gives for haircuts: transmission, interconnection, transformers and firm generation take longer than land. Equipment and skilled labour limit the pace. Some projects need long-term commitments from hyperscalers or frontier labs. Financing costs may rise outside hyperscaler balance sheets. Local moratoria and utility-commission scrutiny delay or shrink projects.

## Results of step 2 (App B)
- Gross post-2024 pipeline: 516.7 GW.
- By 2032: 188.3 GW. That is 22.5 GW already operational in 2025 or 2026, plus 147.2 GW observed, plus 18.6 GW imputed.
- **Largest uncertainty**: the 313.9 GW with no date. It is most of the gross pipeline. 54.0 GW of it counts by 2032.
- Implied cancellation: 32.6% of 2,090 planned and under-construction projects, about 680 projects. Capacity-weighted: 43.2%, or 213.5 GW of 494.1 GW.
- Benchmark: Brandsaas et al. (2025) find 33% abandonment in Dodge data, and 30% for projects above $250m.

## Step 3: phase the spending (App B, equation 1)
| Year relative to completion (t) | Share of cost | What is spent |
|---|---|---|
| t-3 | 5.122% | Half of power infrastructure. Half of land and soft costs |
| t-2 | 5.122% | Same |
| t-1 | 17.561% | Half of building hard costs and fit-out. 10% of IT |
| t | 72.195% | Other half of hard costs and fit-out. 90% of IT |

- Real estate split: land 10%, soft costs 10%, building hard costs 40%, cooling and backup generators 40%.
- IT: the author is "not aware of requirements to pay for them in advance", despite advance purchase commitments.
- Formula: I_s = 0.72195 c_s K_s + 0.17561 c_(s+1) K_(s+1) + 0.05122 c_(s+2) K_(s+2) + 0.05122 c_(s+3) K_(s+3), with K in GW and c_t = $41m x 1.04^(t-2025) per MW.
- Undated capacity completed by 2032 (54.0 GW) is spread evenly over 2028-2032. Capacity pushed past 2032 (89.8 GW undated plus 19.9 GW dated) is spread evenly over 2033-2037.

## Table 5: scenario-implied US investment (author's estimates)
| Year | Investment $bn | Nominal GDP $bn | Investment / GDP % |
|---|---|---|---|
| 2025 | 790 | 30,762 | 2.6 |
| 2026 | 1,253 | 31,992 | 3.9 |
| 2027 | 1,597 | 33,272 | 4.8 |
| 2028 | 1,717 | 34,603 | 5.0 |
| 2029 | 978 | 35,987 | 2.7 |
| 2030 | 886 | 37,427 | 2.4 |
| 2031 | 863 | 38,924 | 2.2 |
| 2032 | 889 | 40,481 | 2.2 |
| 2025-32 | 8,973 | 283,448 | 3.17 |

- Average of the eight annual ratios: 3.22%. Peak: 4.96% in 2028 (App C).
- GDP sensitivity: 2.95% of cumulative GDP at 6% nominal growth. 2.74% at 8%.

## What the estimate leaves out (App B)
- Pipeline growth after September 12, 2026.
- **IT replacement.** Capacity commissioned in 2025-26 "may require substantial GPU and related equipment replacement by around 2030".
- Component-specific depreciation.
- The author says these exclusions make the estimate conservative.
