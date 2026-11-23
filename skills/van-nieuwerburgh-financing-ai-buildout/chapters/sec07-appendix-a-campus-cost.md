# Appendix A: Representative AI Campus Cost

**Type**: METHOD (cost model) | **Source pages**: 18-20

## Core Idea
Build the cost of a 200 MW AI training campus from three blocks: facility, power, IT. Convert to dollars per MW. Use that benchmark for the aggregate.

## Step method (App A). All values are the author's assumptions, 2025
1. **Power budget.** 200 MW total facility power. PUE 1.2. Critical IT capacity is about 166.7 MW. The other 33.3 MW runs cooling, electrical conversion, lighting and other non-IT loads. The PUE matches Cleanview facilities that report both measures.
2. **Facility.** $11m per MW of total power. Cost $2.2bn.
3. **Power infrastructure.** $2m per MW of total power. Cost $0.4bn. Covers new generation (grid or behind-the-meter), substations, transmission upgrades and interconnection.
4. **Rack count.** NVIDIA GB300 NVL72 at about 142 kW per rack gives about 1,170 racks. This is a "cluster-equivalent" count (footnote 10): each rack carries its pro rata share of network and storage power.
5. **Rack cost.** $4.0m per integrated system. Total $4.68bn. The price includes GPUs, high-bandwidth memory, Grace CPUs, NVLink switching, power systems and the rack.
6. **IT add-ons.** Plus 10% of rack cost for external network fabric and fiber. Plus 5% for shared storage. Plus 5% for installation, integration and commissioning. Installed IT is about $4.8m per rack, $5.62bn in total, about $34m per MW of critical IT capacity.
7. **Total.** About $8.2bn, or $41m per MW of total facility power.

## Table 2: 200 MW AI training campus
| Component | Assumption | Cost $bn | Share % |
|---|---|---|---|
| Data center facility | 200 MW x $11m | 2.200 | 26.8 |
| Incremental power infrastructure | Campus-level allowance | 0.400 | 4.9 |
| IT equipment | 1,170 racks x $4.8m | 5.616 | 68.4 |
| - Integrated GB300 NVL72 systems | 1,170 racks x $4.0m | 4.680 | 57.0 |
| - External network fabric and fiber | 10% of rack cost | 0.468 | 5.7 |
| - Shared data storage | 5% of rack cost | 0.234 | 2.8 |
| - Integration and commissioning | 5% of rack cost | 0.234 | 2.8 |
| **Total** | | **8.216** | **100.0** |

Facility plus power is about 32%. Installed IT is about 68%.

## Cross-checks the author gives (App A)
| Benchmark | Source | Author's comment |
|---|---|---|
| $11.3m per MW global construction cost forecast | JLL (2026) | Close to the $11m assumption |
| $8.9m per MW average real estate investment, data centres operational in 2025 and 2026 | Cleanview | The author's number is higher |
| Liquid-cooled US data centres cost 7-10% more than air-cooled | Turner & Townsend (2025) | Supports the higher number |
| 45 GW of new generation needed by 2030 at $110bn, or $2.44m per MW | Moody's Ratings (2026c) | Excludes grid connection and transmission. So $2m per MW "is likely conservative" |
| About $15m per MW for Hyperion, excluding IT | Sec IV footnote 3 | "broadly consistent" with $11m facility plus power |

## Bias the author flags (App A)
- The IT price is for a state-of-the-art architecture. It may exceed the average installed architecture.
- Against that, "the cost of quality-adjusted datacenter IT appears to be rising".

## Aggregation rule (App A)
- Capacity completed in year t costs $41m x 1.04^(t-2025) per MW.
- The same formula deflates capacity completed before 2025.
- Each cohort is valued at its completion-year cost, including spending before completion.
