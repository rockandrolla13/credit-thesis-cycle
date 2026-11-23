# Appendix D: Revenue Required to Support the Investment

**Type**: METHOD (break-even revenue model) | **Source pages**: 26-30

## Core Idea
Ask what mature annual revenue recovers the investment, replaces depreciating capital and pays the cost of capital. The author says the exercise "is not a forecast of AI revenues".

## Step method (App D, equations 2 to 7)
1. **Cohort cost.** Q_t = c_t x K_t. Use capacity completed in 2025-32 only (188.3 GW).
2. **Construction carry.** phi = 0.05122(1+r)^3 + 0.05122(1+r)^2 + 0.17561(1+r) + 0.72195. At r = 10%, phi = 1.04527.
3. **Capital base at commissioning.** B_t = phi x Q_t.
4. **Asset lives.** IT is 68% of cost with a six-year economic life. Non-IT is 32% with a 20-year life. The six-year life rests on "current industry assessment and accounting practices".
5. **Capital-recovery factor.** a(r, N) = r(1+r)^N / ((1+r)^N - 1).
6. **Required operating cash flow.** CF_t = B_t x [0.68 a(r,6) + 0.32 a(r,20)].
7. **Required revenue.** Rev_t = CF_t / mu, where mu is the operating cash-flow margin.

## Central numbers (r = 10%, mu = 50%). Author's estimates
- a(10%, 6) = 22.96%. a(10%, 20) = 11.75%. Weighted capital charge = 19.37% of the capital base.
- Required revenue = 38.74% of the capital base.
- Initial cost $8.762tn. Capital base $9.159tn. Required operating cash flow $1.774tn. Required mature revenue $3.549tn. That is 8.8% of 2032 GDP of $40.481tn.
- The $8.762tn differs from the $8.973tn of Table 5 (footnote 11): take out $565bn spent in 2025-2032 on projects that open after 2032, and add $354bn spent before 2025 on projects that open in 2025-2032.

## Table 6: by completion cohort ($bn)
| Year | GW | Cost | Capital | Required CF | Required revenue |
|---|---|---|---|---|---|
| 2025 | 13.8 | 563.9 | 589.4 | 114.2 | 228.4 |
| 2026 | 26.6 | 1,133.6 | 1,184.9 | 229.5 | 459.1 |
| 2027 | 35.8 | 1,588.8 | 1,660.7 | 321.7 | 643.4 |
| 2028 | 43.5 | 2,005.5 | 2,096.3 | 406.1 | 812.2 |
| 2029 | 21.5 | 1,029.6 | 1,076.2 | 208.5 | 417.0 |
| 2030 | 17.7 | 881.9 | 921.9 | 178.6 | 357.2 |
| 2031 | 16.1 | 835.5 | 873.3 | 169.2 | 338.3 |
| 2032 | 13.4 | 723.4 | 756.2 | 146.5 | 293.0 |
| Total | 188.3 | 8,762.2 | 9,158.8 | 1,774.3 | 3,548.5 |

## Table 7: required mature annual revenue, $bn
| Required return | Margin 33% | Margin 50% | Margin 67% |
|---|---|---|---|
| 5% | 4,333 | 2,860 | 2,134 |
| 10% | 5,377 | 3,549 | 2,648 |
| 15% | 6,554 | 4,326 | 3,228 |

## Market units (App D)
- $18.8m per MW-year of total facility power.
- $22.6m per MW-year of critical IT load at PUE 1.2.
- $2.58 per kWh of critical IT energy at full utilisation.
- About 1.10 million racks, or 79.3 million GPUs.
- Required price per GPU-hour:

| Utilisation | $ per GPU-hour |
|---|---|
| 100% (installed hour) | 5.1 |
| 80% (billed hour) | 6.4 |
| 70% (billed hour) | 7.3 |

- Market comparison: $6.07 per GPU-hour B200 rental price, Ornn Compute Price Index, August 31, 2026 (accessed September 1, 2026).
- Author's reading: the requirement "does not appear implausible relative to current pricing". The open question is whether demand absorbs 188 GW at high utilisation and whether prices hold as capacity and competition grow.

## Demand yardstick (App D)
Take $100bn as a 2026 benchmark for the combined annual revenue of OpenAI and Anthropic. Revenue must grow about 81.3% a year through 2032 to reach $3.549tn.

## Asset-life sensitivity (App D)
| IT economic life | Weighted capital charge | Required revenue | % of 2032 GDP | $ per installed GPU-hour |
|---|---|---|---|---|
| Six years (central) | 19.37% | about $3.5tn | 8.8 | 5.1 |
| Three years | 31.10% | about $5.7tn | 14.1 | 8.2 |

All other assumptions are unchanged at r = 10% and mu = 50%.

## Limits (App D)
- The return is unlevered. The appendix models no debt service. It does not mention taxes or a ramp-up path.
- "Mature" revenue means all cohorts are operational.
- It inherits every assumption of Appendix A and Appendix B.
