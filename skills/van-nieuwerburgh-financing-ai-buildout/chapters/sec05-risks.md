# Section V: Risks in the AI Infrastructure Buildout

**Type**: METHOD (risk framework) with short CASE evidence | **Source pages**: 11-13

## Core Idea
The problem is not only that the assets carry technology and operating risk. The financing structure "can transmit and amplify those risks". The size of a loss depends on where the leverage sits and how contracts allocate the loss.

## Three underlying vulnerabilities (Sec V)
1. **Tenant and end-demand concentration.**
   - Many large campuses are effectively single-tenant.
   - Tenant commitments rest on AI service profits and on a small set of model developers and enterprise customers.
   - If demand disappoints, hyperscalers may protect their owned facilities and shift workloads away from leased capacity. The adjustment then lands on third-party assets.
2. **Technological obsolescence.**
   - Campuses built for today's chips may lose competitiveness "well before their physical structures wear out".
   - Higher rack densities, new interconnects and new cooling needs can force costly retrofits.
   - More efficient models, edge computing or decentralised inference could cut demand for large central campuses.
   - This creates "a mismatch between the long maturities of infrastructure financing and the potentially much shorter economic lives of the underlying assets".
3. **Execution.**
   - Power, transmission, permits and hardware are capacity-constrained and outside the developer's control.
   - Named bottlenecks: grid interconnection delays, rising power costs, local opposition, shortages of GPUs, high-bandwidth memory and networking equipment.
   - Semiconductor production concentration adds geopolitical risk.
   - The investor risk is cost overrun and also that "revenue begins later or never reaches the levels assumed at underwriting".

## The revenue hurdle (Sec V, detail in App D). Author's estimate
- The 2025-2032 buildout needs about $3.55tn of mature annual revenue to earn a 10% unlevered return at a 50% operating cash-flow margin.
- That equals about 8.8% of 2032 GDP.
- It equals $5.1 per installed GB300 GPU-hour at full utilisation, or $6.4 per billed GPU-hour at 80% utilisation.
- The author calls the $6.4 figure "comparable to frontier-GPU rental prices at the end of August 2026".
- The underwriting question: do demand and pricing power hold once 188 GW is operational?

## The amplifier: leverage and layered claims (Sec V)
- Debt service is fixed. Project revenue depends on utilisation, lease renewals and residual values.
- "A relatively modest deterioration in demand, delays, or asset values" can produce much larger losses for equity and can impair creditors.
- SPVs, guarantees, securitisation and originate-to-distribute lending can weaken monitoring and hide where exposures sit (DeMarzo 2005, Coval et al. 2009, Gete and Mercader 2026).

## Circularity along the value chain (Sec V, footnote 9)
- Chip designers, cloud providers, model developers, data-centre operators and infrastructure investors depend on each other through contracts, strategic investments and financing.
- A shock to one segment spreads to cloud revenue, lease payments, asset values and creditor recoveries.
- Exposures are "more correlated than they may appear when each transaction is viewed in isolation".
- **Vendor financing case (footnote 9)**: in August 2026, Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs and KKR stood up a $500bn credit facility to finance NVIDIA chips. NVIDIA provides a 25% residual value guarantee. That exposes it to as much as $125bn of backstops. Google and Broadcom entered a similar arrangement for TPU chips.

## Asset-pricing evidence (Sec V, Fig 3). Author's regression
- The market beta of listed data-centre REITs rose from roughly 0.5 to around 1.
- Their beta to the non-AI part of the S&P 500 also rose. It is now comparable to their exposure to AI stocks.
- Reading: data centres look "less like defensive infrastructure assets or a hedge against AI-related risk and more like part of the same systematic risk complex".
- Specification (Fig 3 notes): 36-month rolling betas. Dependent variable is the value-weighted data-centre REIT return (FTSE Nareit) minus the T-bill rate. Regressors are the S&P 500 excess return, the 10-year Treasury excess return, and the Fama-French size, value, profitability and investment factors. The second run splits the S&P 500 into AI stocks and the rest. AI stocks are the constituents of the Global X AIQ ETF on March 18, 2026. Monthly sample, January 2018 to March 2026.

## The author's balanced conclusion (Sec V)
- "These developments do not imply that financial distress is imminent." Strong application growth and high utilisation could support the buildout.
- History (railroads to telecom) shows that large capital-intensive expansions turn financially consequential under three conditions:
  1. demand falls short,
  2. financing conditions tighten,
  3. the adoption speed of the technology does not match the maturity of the debt that financed it.
- The right question is "under what conditions project-level losses could become correlated and propagate across firms and financial institutions".
