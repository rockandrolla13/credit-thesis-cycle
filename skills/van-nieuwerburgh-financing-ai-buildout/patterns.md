# Patterns: Financing the AI Buildout (Van Nieuwerburgh)

## Bottom-up campus costing
**When to use**: you need the capital cost of a data-centre campus or of N GW. (App A)
**How**: (1) Take total facility MW. (2) Divide by PUE 1.2 for critical IT MW. (3) Divide by 142 kW for the rack count. (4) Price racks at $4.0m and add 20% for network, storage and integration. (5) Add $11m per MW facility and $2m per MW power. (6) Grow the $41m per MW total by 4% for each year after 2025.
**Trade-offs**: uses state-of-the-art rack pricing. The power block "is likely conservative". Cleanview's realised facility cost is lower ($8.9m per MW).

## Pipeline haircut
**When to use**: someone quotes announced GW as if it were supply. (Sec II, App B)
**How**: (1) Sort projects by completion year and by whether capacity is disclosed. (2) Apply Table 4 rates: 90% by 2032 for 2026 projects, falling 10 points a year, 20% for undated projects, lower for imputed capacity. (3) Report three buckets: by 2032, after 2032, never.
**Trade-offs**: the rates are the author's assumptions. The undated bucket drives the answer. Benchmark only at the project-count level (33% in Brandsaas et al.).

## Spend phasing
**When to use**: you need annual investment flow, not completed capacity. (App B)
**How**: put 5.122% of a cohort's cost in t-3, 5.122% in t-2, 17.561% in t-1 and 72.195% in t. Sum across cohorts with equation 1.
**Trade-offs**: assumes GPUs are paid on delivery. Excludes IT replacement.

## Separate the user, the owner and the risk bearer
**When to use**: reading any data-centre financing. (Sec III, Sec VI)
**How**: for each asset name (1) who uses the compute, (2) who legally owns it, (3) who bears demand risk, refinancing risk and residual-value risk. Then list the contracts that pull risk back to the tenant: leases, capacity commitments, guarantees.
**Trade-offs**: public data rarely answers step 3. Rated deals are a small share of the market.

## Hyperion template check
**When to use**: a new off-balance-sheet campus deal appears. (Sec IV)
**How**: look for the five ingredients. Investment-grade tenant. High project leverage. Bankruptcy-remote entities. Short renewable leases with termination rights. A residual value guarantee. Then record debt-to-asset, DSCR, rating gap to the tenant, yield gap to tenant unsecured debt, and bond maturity against lease term.
**Trade-offs**: one fully documented case plus one near copy (Sopaipilla).

## Lease-adjusted leverage
**When to use**: judging a hyperscaler's real leverage. (Sec IV, footnote 6)
**How**: lease obligations = commenced leases + 0.75 x uncommenced leases. Compute (debt + leases) / (debt + leases + book equity) and (debt + leases) / EBITDA. Compare with the unadjusted ratios.
**Trade-offs**: the 0.75 is a rough present-value factor. It leaves out residual value guarantees and purchase commitments. The author drops Amazon because of warehouse leases.

## Asset life against debt term
**When to use**: any long-dated financing of compute infrastructure. (Sec V, App C, App D)
**How**: (1) Split cost into IT (68%, six-year life, possibly three) and non-IT (32%, 20-year life). (2) Compare with bond maturity and lease term. (3) Check who pays for IT replacement. (4) Rerun the capital charge with a three-year IT life.
**Trade-offs**: the six-year life is an accounting convention. The paper gives no empirical GPU resale data.

## Required-revenue test
**When to use**: asking whether a buildout can earn its cost of capital. (App D)
**How**: (1) Cohort cost. (2) Multiply by phi. (3) Multiply by 0.68 a(r,6) + 0.32 a(r,20). (4) Divide by the cash margin. (5) Convert to dollars per GPU-hour and divide by utilisation. (6) Compare with a transaction-based rental index.
**Trade-offs**: unlevered and mature-state. The comparison price is today's, before 188 GW arrives.

## Three-conditions test for a boom
**When to use**: asking whether an investment boom turns into a financial problem. (Sec V)
**How**: check for (1) demand short of plan, (2) tighter financing conditions, (3) a gap between technology adoption speed and debt maturity. Then ask where leverage sits and whether losses are correlated across the same tenants.
**Trade-offs**: qualitative. The paper sets no thresholds.

## Joint-shock question
**When to use**: framing a stress scenario. (Sec VI)
**How**: assume utilisation, collateral values and refinancing capacity fall together. Trace losses through banks, insurers, private credit funds and securitisation vehicles. Check concentration in the same tenants.
**Trade-offs**: the paper poses the question and does not answer it.

## Anti-patterns the author warns against
- Reading reported hyperscaler capex as the whole buildout. It excludes leased data centres. (Sec III Fig 1 notes, Sec VI)
- Reading reported hyperscaler leverage as economic leverage. (Sec IV)
- Reading the 60-40 aggregate split as asset-level leverage. (Sec III)
- Treating GPU collateral like real estate or aircraft. (Sec III)
- Treating data-centre REITs as defensive or as a hedge against AI risk. (Sec V)
- Viewing each transaction in isolation. (Sec V)
- Comparing gross investment across booms without adjusting for asset life. (App C)
- Concluding that risk is already systemic, or that distress is imminent. (Sec V, Sec VI)
