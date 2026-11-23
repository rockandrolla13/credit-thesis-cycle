# Cheatsheet: Bank Lending to Private Credit (FEDS Notes)

"Sec" = main note (May 2025). "C" = companion note (October 2026).

## Before quoting any number, fix four things
1. Committed or drawn.
2. Which lenders: Y-14 banks, all banks, all lenders.
3. Which vehicles: BDCs, PD funds, private equity, other NBFIs.
4. Which quarter.

## The numbers
| What | Value | Date | Scope | Cite |
|---|---|---|---|---|
| Bank commitments to BDCs + PD funds | ~$95 bn | 2024-Q4 | Y-14 banks, committed | Sec 3.1 |
| Same, 2013 | ~$8 bn | 2013-Q1 | Y-14 banks, committed | Sec 1 |
| Drawn | $56 bn | 2024-Q4 | Y-14 banks, utilized | Sec 3.1 |
| Revolvers / term loans | $79 bn / $16 bn | 2024-Q4 | Y-14 banks, committed | Sec 3.1 |
| BDC commitments | $56 bn | 2024-Q4 | Y-14 banks | Table 1 |
| PD fund commitments | $40 bn | 2024-Q4 | Y-14 banks | Table 1 |
| All-lender BDC commitments | ~$87 bn (estimate) | 2024-Q1 | All lenders, BDCs only | Sec 3.2 |
| Y-14 share of BDC commitments | ~60% | 2024-Q1 | | Sec 3.2 |
| Private credit + private equity lines | ~$322 bn | 2024-Q4 | Y-14 banks, committed | fn 2 |
| Other NBFI commitments | $2.2 tn | 2024-Q4 | Y-14 banks | Sec 3.1 |
| Share of regulatory capital | ~7% | 2024-Q4 | Average | Sec 3.1 |
| Share at five GSIBs | ~60% | 2024-Q4 | | Sec 3.1 |
| Full-drawdown shock | $36 bn | 2024-Q4 | BDCs + PD funds | Sec 4.2 |
| With private equity | $134 bn | 2024-Q4 | | fn 10 |
| US private credit asset class | $1.34 tn | 2024-Q2 | Preqin, LSEG | Sec 1 |
| Private credit vehicle AUM | >$2.6 tn | 2025:Q4 | US footprint | C Sec 2 |
| Private credit loans | ~$1.5 tn | 2025:Q4 | To US businesses | C Sec 2 |
| Bank loans to US vehicles | $349 bn | 2025:Q4 | Z.1, depository loans | C Sec 4.1 |
| Private credit share of business debt | 6% ($1.31 tn) | 2025:Q4 | Nonfinancial business | C Table 8 |

## Growth, five years to 2024-Q4 (Sec 3.1)
- Commitments to private credit vehicles: ~145%. Drawn: ~117%.
- BDCs: ~186%, the fastest of all NBFIs. Securitization vehicles: 141%. PD funds: 103%.
- Other NBFIs: ~53%. Nonfinancial corporates: 14%.

## Loan profile, 2024-Q4 (Table 1)
| | Util | Rate | Maturity | Delinq | Mean PD | Median PD |
|---|---|---|---|---|---|---|
| BDCs | 56.8% | 6.4% | 4.1y | 0.5% | 0.71% | 0.30% |
| PD funds | 55.0% | 6.6% | 2.6y | 0.7% | 2.07% | 0.22% |
| Other NBFIs | 48.7% | 6.2% | 3.0y | 0.7% | 1.65% | 0.37% |
All rated BBB on average, on banks' internal scales.

## Stress arithmetic (Sec 4.2, fn 9)
- Shock = undrawn lines = $36 bn.
- CET1: RWA + 0.5 × 36 = +$18 bn. 13.02% → 13.0%.
- LCR: HQLA − 36. Outflow base − 0.4 × 36 = −$14.4 bn. 122% → 121%.
- Risk weight on undrawn non-cancelable lines: 50% over one year, 20% under one year.

## Decision rules the sources support
- When a figure has no "committed" or "drawn" label, do not use it. (Sec 3.1)
- When the source is Y-14, add: largest US banks only, ~71% of bank corporate loans. (Sec 2.1)
- When the question is about BDCs, use the public 10-Q route. (Sec 2.2)
- When the question is about PD funds' bank borrowing, there is no public loan-level route. Use Z.1 sector totals. (Sec 2, C Table 2)
- When PD fund default risk is quoted, give mean and median. They point in opposite directions against other NBFIs. (Table 2)
- When someone cites "2 basis points", add the authors' caveat: upper bound for private credit vehicles alone, not for correlated NBFI drawdowns. (Sec 4.2)
- When risk is said to have left the banks through a risk transfer, check whether banks fund the buyer. (Sec 5)
- When comparing business debt across Z.1 vintages, check for the September 2026 break. (C Sec 3)
- When Y-14 and Z.1 bank-loan figures disagree, report both with scope. Do not splice them. (library note, sec07)

## Watch list
Named in the conclusion (Sec 6):
1. Public BDC leverage: ~40% (2017) → 53% (2024) debt to assets.
2. Bank and private credit partnerships.

Raised elsewhere in the note:
3. Utilization: rising again since the second half of 2024. (Sec 3.3)
4. NBFI reliance on credit lines for liquidity, above past levels. (Sec 4.2)

## Public versus confidential
| Public | Confidential or vendor |
|---|---|
| SEC BDC list | FR Y-14Q H.1 (supervisory) |
| BDC 10-Q and 10-K | SEC Form PF |
| Z.1 tables, DDP, FRED | Preqin, PitchBook, Moody's CLO, BDC Collateral, Compustat, Morningstar |
| SEC Form N-PORT | |

## Z.1 codes for bank funding of vehicles (C Tables 2 to 4)
- PD funds, depository loans: FL443168000
- BDCs, depository loans: FL453168003
- Interval and tender offer funds, depository loans: FL463168005
- Private credit loans, total: FL893167205
