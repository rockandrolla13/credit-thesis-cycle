# Section IV: Financial Architecture and Risk (the Hyperion transaction)

**Type**: CASE (one transaction, October 2025) with a reusable METHOD (leverage adjustment, footnote 6) | **Source pages**: 8-11

## Core Idea
Hyperion shows how an investment-grade tenant can carry about 90% project leverage off its balance sheet. The tenant pays more for the debt. It gets an asset-light reported profile in return.

## Deal facts (Sec IV, Fig 2). Sources named by the paper: S&P pre-sale report, Entergy 2025 Form 10-K
| Item | Value |
|---|---|
| Capacity | About 2.0 GW |
| Total investment | About $30bn. This is about $15m per MW. It **excludes IT equipment**, which Meta finances separately as tenant (footnote 3) |
| Equity sale | Meta sold an 80% equity stake to Blue Owl for about $2.5bn |
| Joint venture | Beignet. Meta holds 20% through Iris Crossing LLC. Blue Owl holds its stake through Beignet Investor LLC |
| Asset owner | Laidley LLC owns the campus. Its funding comes from Project Beignet Holdings LLC |
| Debt | $27bn raised in October 2025. Maturity 2049 |
| Rating | A+ from Standard & Poor's, one notch below Meta's corporate rating |
| Size claim | "the largest individual investment-grade corporate debt issuance in U.S. history" |
| Debt-to-asset | About 90% ($27bn of $30bn) |
| Debt service coverage ratio | 1.12x |
| Yield | 6.58%, "at least 100 basis points above" what Meta would likely have paid on comparable unsecured debt |
| Extra interest cost | More than $5bn over the life. It flows into Meta's lease payments |
| Power | Laidley has a Power Purchase Agreement with Entergy Louisiana, which develops three gas-fired units |

Comparison (footnote 4): Meta's own year-end 2025 leverage was about 25% on book equity and 4% on market equity. Meta's operating cash flow of $130bn is "at least 18x its 2026 debt service".

## Lease and guarantee mechanics (Sec IV)
- Five four-year leases. They begin in 2029 and run to the bond's 2049 maturity.
- At each renewal Meta may terminate for some or all of the campus.
- If Meta terminates, the assets go up for sale. Meta covers any shortfall between sale proceeds and a contractual minimum value. This is the **residual value guarantee** (RVG).
- Purpose: reconcile lenders' need for long, predictable cash flows with Meta's need for flexibility.

## Accounting gap (Sec IV)
- Under current GAAP, Meta recognises neither the future lease obligations nor the RVG before the relevant lease or guarantee becomes effective.
- Yet "one of the two commitments will ultimately materialize for sure".
- So reported leverage understates the economic obligation.

## Off-balance-sheet totals quoted (third-party numbers)
- **Moody's Ratings (2026a, February 2026)**: hyperscalers have roughly $970bn of lease commitments. About $660bn relates to future leases not yet on balance sheet. (Sec IV)
- **Wall Street Journal analysis (footnote 5)**: $2.4tn off-balance-sheet liabilities for Microsoft, Alphabet, Amazon and Meta. $904bn is future lease commitments. $1.52tn is future purchase commitments, mostly chips. On-balance-sheet obligations are $604bn: $356bn long-term debt and $248bn current lease obligations. Only one-fifth of the $3tn in data-centre-related obligations is recognised. The paper gives no date for the article.

## Method: lease-adjusted leverage (footnote 6). Author's calculation, June 2026 data
1. L1 = debt / (debt + book equity).
2. L2 = (debt + lease obligations) / (debt + lease obligations + book equity).
3. L3 = debt / EBITDA.
4. L4 = (debt + lease obligations) / EBITDA.
5. Lease obligations = commenced leases + 0.75 x future uncommenced leases. The 0.75 approximates a present value.
6. Exclude Amazon, because its leases include many warehouses. Aggregate the other four hyperscalers.

Result: L1 = 20% rises to L2 = 48%. L3 = 0.7x rises to L4 = 2.6x.

## Why Meta does it (Sec IV)
"The economic rationale for Meta is therefore not cheaper financing, but preservation of an asset-light corporate profile." A firm valued on high growth and low capital intensity may accept the higher borrowing cost.

## Why bondholders get paid more (Sec IV)
- No direct claim on Meta's balance sheet.
- Repayment depends on cash moving through the project structure and on Meta's lease and RVG.
- That adds structural, contractual, liquidity and enforcement risk.
- Longer duration and a specialised private-placement format add to the premium.

## The Hyperion template: five ingredients (Sec IV)
1. Investment-grade tenant credit.
2. High project-level leverage.
3. Bankruptcy-remote entities.
4. Lease optionality.
5. A residual value guarantee.

Repeat use (footnote 7): the 960 MW Sopaipilla project in El Paso, Texas, a Meta and BlackRock joint venture, "follows a nearly identical structure". It issued $12.3bn of A+ rated bonds in July 2026.

## Visibility limit (Sec IV)
Hyperion at least has a public rating and agency analysis. Publicly rated debt is "only a relatively small share" of data-centre financing. Much larger volumes go through syndicated bank loans and private credit, with little public information.

## Market pricing evidence: hyperscaler CDS (footnote 8)
Five-year CDS spreads, November 21, 2025 to July 22, 2026, in basis points:

| Firm | Nov 21, 2025 | Jul 22, 2026 |
|---|---|---|
| Alphabet | 44.7 | 57.7 |
| Meta | 56.1 | 80.2 |
| Microsoft | 35.1 | 47.7 |
| Amazon | 39.7 | 59.6 |
| Oracle | 118.8 | 205.5 |

The author's reading: the "broad-based repricing suggests" credit investors discount formal investment-grade status for off-balance-sheet commitments, future leases and financing opacity. The paper names no data source and runs no test of that cause.
