# Section 7 (Companion): Introducing Private Credit into the Financial Accounts of the United States

Source: Brinkman, Dobridge, Dore, Glossner, Holmquist, Nguyen, Perozek, Stefanescu, FEDS Note, 16 October 2026. Cites below are to that note's own sections ("C Sec"), tables ("C Table") and footnotes ("C fn").

## Core Idea
From the September 2026 Z.1 release, the Financial Accounts carry private credit as its own sectors and instruments. The series are public and quarterly. They give system-wide balance sheets for the vehicles, including how much they borrow from depository institutions.

## Definition (C Sec 1, C Sec 4.3)
Private credit = "privately negotiated loans to businesses that are originated by nonbank investment funds rather than by traditional financial intermediaries such as banks".
- It covers corporate direct lending, asset-based and specialty finance, real estate debt, infrastructure debt and other privately negotiated loans.
- It "does not depend on the identity of the borrower, the purpose of the loan, or the assets supporting repayment".
- It spans senior secured, junior, unsecured and hybrid debt-equity instruments.

This is wider than the main note's definition (direct loans to mid-market businesses by PD funds and BDCs).

## What was added (C Sec 4)
**Three new sectors**
| Sector | Z.1 tables | Primary data source | Series start |
|---|---|---|---|
| Private debt funds (US-domiciled) | S.124.8.s (stocks), S.124.8.t (transactions) | Confidential SEC Form PF, merged with Preqin, PitchBook, Moody's | 2012:Q4 |
| Business development companies | S.124.5.s, S.124.5.t | BDC Collateral (LSEG LPC), built from BDC 10-Qs and 10-Ks | 2012 (Figure 1) |
| Interval and tender offer funds | S124.6.s, S124.6.t | Morningstar and SEC Form N-PORT | 2021 |

**One addition to an existing sector**
- Middle-market CLOs go into Issuers of asset-backed securities, tables S125s1.3.s and S125s1.3.t. Source: Moody's Analytics Global CLO database. Private credit loans are added on the asset side (line 7) and the same amount of corporate bonds on the liability side (line 18).

**Two new instruments**
- Private credit loans: table F4.4.s. Shows holders (lenders) and issuers (borrowers).
- Private debt fund shares: table F522.3.s. Shows issuers and investor sectors.

**Not added as sectors**: foreign-domiciled PD funds and MM CLOs. They were already in the Rest of the World (ROW) sector. Their loans to US businesses and their fund shares are now separately identified (C Sec 3).

## Method notes that matter for use (C Sec 4.2, C fn 7 to 12)
- **PD funds are not flagged in Form PF.** The staff classify funds using fund strategies, fund names and vendor classifications.
- **Annual filers are imputed.** For funds that file Form PF only annually, the staff impute balance sheets from quarterly filers with similar strategies, then interpolate quarters.
- **Form PF misses some lenders.** It captures funds whose adviser is SEC-registered. Some non-US advisers are exempt, "causing some U.S. loans to fall outside Form PF" (C fn 7).
- **AUM excludes dry powder.** Uncalled commitments are a memo item on S124.8.s (C fn 9).
- **Loan figures may include syndicated loans.** The staff are "currently unable to fully distinguish between the two types" (C fn 10).
- **MM CLOs may be undercounted** in the Moody's data (C fn 12).
- **Borrower sectors are estimated.** Borrower identity is known for BDC loans and MM CLO loans. The staff apply that same sector split to PD fund and interval and tender offer fund loans (C Sec 4.3).
- **BDC cost and fair value** are both in the data, so the staff split changes into transactions and revaluations.
- **Foreign PD fund balance sheets are assumed** to look like US-domiciled ones (C Sec 4.1).

## Size numbers, 2025:Q4 unless stated

**Headline (C Sec 2, C Sec 4.1)**
| Measure | Value |
|---|---|
| AUM of private credit vehicles, all with a US footprint | about $350 billion in 2012, "over $2.6 trillion" at 2025:Q4 ($2,661 billion, C Table 1) |
| AUM of US-domiciled vehicles | $1.9 trillion ($1,857 billion) |
| Private credit loans to US businesses | about $1.5 trillion ($1,458 billion, C Table 1) |
| of which from foreign-domiciled PD funds | $335 billion |
| Funding of US vehicles: equity | $1.1 trillion ($1,065 billion) |
| Funding of US vehicles: bank loans | **$349 billion** |
| Funding of US vehicles: debt securities | $135 billion |

**C Table 1: balance sheets of vehicles with a US footprint, $ billion, 2025:Q4**
| | US PD funds | BDCs | Interval and tender | US CLOs | Domestic subtotal | Foreign PD funds | Foreign CLOs | Total |
|---|---|---|---|---|---|---|---|---|
| Total financial assets | 939 | 572 | 292 | 54 | 1,857 | 763 | 41 | 2,661 |
| Private credit loans to the US | 498 | 456 | 76 | 53 | 1,083 | 335 | 40 | 1,458 |
| Private credit loans to rest of world | 34 | | 1 | | 35 | 83 | 1 | 119 |
| Syndicated loans | | 43 | 8 | | 51 | | | 51 |
| Corporate equities | 173 | 42 | 129 | | 344 | 168 | | 512 |
| Total liabilities | 397 | 286 | 56 | 54 | 792 | 227 | 41 | 1,060 |
| **Depository institution loans n.e.c.** | **150** | **181** | **18** | | **349** | 73 | | 422 |
| Other loans and advances | 84 | | | | 84 | 83 | | 167 |
| Debt securities (corporate bonds) | | 82 | | 54 | 135 | | 41 | 176 |
| Total equity and shares | 541 | 287 | 237 | | 1,065 | 537 | | 1,602 |

Blank cells are blank in the source. The extraction flattened this table. Column placement was rebuilt from row totals and from C Tables 2 to 5. Verify against the Z.1 release before relying on a single cell.

**Depository loans to the vehicles over time, $ billion (C Tables 2, 3, 4)**
| Borrower sector | 2023 | 2024 | 2025:Q2 | 2025:Q3 | 2025:Q4 | Series code |
|---|---|---|---|---|---|---|
| PD funds | 132.0 | 132.5 | 135.4 | 143.3 | 150.3 | FL443168000 |
| BDCs | 101.5 | 137.0 | 147.3 | 158.2 | 180.8 | FL453168003 |
| Interval and tender offer funds | 9.9 | 13.3 | 15.7 | 15.8 | 18.4 | FL463168005 |

**Vehicle balance sheets, selected lines, $ billion**
| Line | 2023 | 2024 | 2025:Q4 | Code |
|---|---|---|---|---|
| PD funds: financial assets | 754.6 | 842.5 | 938.7 | FL444090000 |
| PD funds: private credit loans | 432.5 | 480.6 | 532.2 | FL443067205 |
| PD funds: total liabilities | 302.4 | 337.2 | 397.5 | FL444190005 |
| PD funds: shares outstanding | 452.2 | 505.2 | 541.3 | LM443164500 |
| PD funds: dry powder (memo, not in assets) | 245.7 | 260.0 | 307.4 | FL442000093 |
| BDCs: total financial assets | 318.8 | 440.9 | 572.2 | FL454090003 |
| BDCs: private credit loans | 238.1 | 340.8 | 455.9 | FL453067203 |
| BDCs: total liabilities | 156.3 | 215.5 | 285.5 | FL454190005 |
| BDCs: debt securities | 45.3 | 64.4 | 81.5 | FL453163003 |
| BDCs: total equity | 162.5 | 225.4 | 286.7 | LM453164105 |
| BDC assets: traded perpetual | 151.9 | 163.8 | 181.0 | LM454090013 |
| BDC assets: private perpetual | 115.1 | 204.7 | 306.8 | LM454090023 |
| BDC assets: private finite | 51.8 | 72.4 | 84.5 | LM454090033 |
| Interval and tender: total assets | 160.1 | 210.6 | 292.4 | FL464090005 |
| MM CLOs (domestic): private credit loans | 31.7 | 42.9 | 53.7 | FL673067205 |

Composition facts the note states:
- PD funds: private credit loans are about 60 percent of assets and corporate equities about 18 percent. Loans are about 60 percent of borrowing.
- BDCs: private credit loans are 80 percent of assets. Bank loans are "about 2/3" of liabilities. Statutory leverage limit: up to 2:1 debt to equity. At least 70 percent of assets must be in eligible portfolio companies.
- Interval and tender offer funds: private credit plus syndicated loans are nearly 30 percent of assets. Corporate equities are 44 percent. Borrowing is limited.

**C Table 6: private credit loans (F4.4.s), $ billion**
| | 2023 | 2024 | 2025:Q4 |
|---|---|---|---|
| Total | 1,042.6 | 1,253.6 | 1,493.5 |
| Borrower: nonfinancial corporate | 764.5 | 916.9 | 1,087.9 |
| Borrower: nonfinancial noncorporate | 148.1 | 181.7 | 222.7 |
| Borrower: other financial business | 100.2 | 121.8 | 147.8 |
| Borrower: rest of the world | 29.8 | 33.2 | 35.1 |
| Lender: BDCs | 238.1 | 340.8 | 455.9 |
| Lender: interval and tender offer funds | 34.0 | 53.1 | 76.3 |
| Lender: PD funds | 432.5 | 480.6 | 532.2 |
| Lender: ABS issuers (CLOs) | 31.7 | 42.9 | 53.7 |
| Lender: rest of the world | 306.4 | 336.2 | 375.5 |

From-whom-to-whom example (C Sec 4.3): US nonfinancial corporates owe roughly $1.1 trillion. $622 billion from private debt funds, $341 billion through BDCs, $57 billion through interval and tender offer funds, $69 billion through middle-market CLOs. This detail is not on the published Z.1 tables. It is available through the Fed's Data Download Program and FRED (C fn 14).

**C Table 7: who holds PD fund shares (F522.3.s), $ billion, 2025:Q4**
Total $689.4 billion: $541.3 billion issued by US PD funds, $148.2 billion by ROW.
| Holder | $ bn | Share (C Figure 3) |
|---|---|---|
| State and local government employee pension funds | 195.2 | 28.3% |
| Households (includes nonprofits) | 155.9 | 22.6% |
| Life insurance companies | 99.1 | 14.4% |
| Private pension funds | 94.4 | 13.7% |
| Rest of the world | 91.5 | 13.3% |
| State and local governments | 29.4 | 4.3% |
| Other financial business | 24.0 | 3.5% |

Shares "reflect deployed capital and do not include dry powder". The mix has been stable for a decade. The life insurer share rose somewhat. Household and private pension shares fell modestly.

## Effect on aggregate measures (C Sec 5)
**C Table 8: nonfinancial business debt, 2025:Q4**
| Debt type | $ trillion | Share |
|---|---|---|
| Corporate bonds | 8.08 | 35% |
| Mortgages | 7.20 | 31% |
| Depository loans | 2.87 | 12% |
| Other debt | 2.21 | 9% |
| **Private credit** | **1.31** | **6%** |
| Syndicated loans | 0.77 | 3% |
| Industrial revenue bonds | 0.65 | 3% |
| Commercial paper | 0.21 | 1% |
| Total | 23.29 | 100% |

- Private credit was "around one percent" of business debt in 2012.
- Business debt to GDP is "around 5 percentage points higher in recent years" with private credit included.
- Even so, the ratio "remains below the median as measured since 2012 and has been on a declining trend since 2020".
- Annual debt growth since 2018 is "somewhat higher" with private credit. "the trend is not substantially different".
- Before the change, "aggregate debt positions of nonfinancial businesses were understated".

**Household net worth**: the old treatment overstated some household assets (deposits and equities held by the vehicles were attributed to households by residual). It understated others (directly held fund and BDC shares were missing). The note gives no net number.

## How the old accounts hid private credit (C Sec 3)
- Loans to nonfinancial corporates sat in "miscellaneous liabilities", not in debt instruments.
- Loans to noncorporate businesses were classified as depository institution loans.
- Bank loans to US private credit vehicles were "incorrectly attributed to foreign nondepository financial institutions".
- BDC and US MM CLO debt securities were not recorded at all.

A pre-September-2026 Z.1 vintage is therefore not comparable with a later one on business debt.

## Reading the two notes together
This comparison is a library note. Neither document makes it.

| | Main note (Y-14) | Companion (Z.1) |
|---|---|---|
| BDC borrowing from banks | $31.9 bn drawn, $55.6 bn committed, 2024-Q4, largest US banks. All-lender committed estimate $87 bn, 2024-Q1 | $137.0 bn depository loans, end 2024. $180.8 bn, 2025:Q4 |
| PD fund borrowing from banks | $24.1 bn drawn, $39.7 bn committed, 2024-Q4 | $132.5 bn depository loans, end 2024. $150.3 bn, 2025:Q4 |
| Vehicle universe | 99 matched BDCs, 201 matched PD funds | Sector totals from Form PF and BDC Collateral |

The Z.1 figures are several times the Y-14 figures for the same year-end. The companion does not cite the main note and does not reconcile the two. The documents differ in lender coverage, vehicle coverage and the definition of private credit. Do not splice the two series. Do not explain the gap without a source.

## Inconsistencies inside the companion (recorded, not corrected)
- C Sec 4.1 says $335 billion of US loans come "from foreign-domiciled funds". C Sec 4.3 says foreign-domiciled vehicles account for $376 billion. C Table 6 shows $375.5 billion for ROW. C Table 1 shows $335 billion for foreign PD funds plus $40 billion for foreign CLOs.
- C Sec 6 says "approximately $1.1 trillion in private credit loan activity by U.S.-domiciled vehicles". C Sec 4.3 says "about $1 trillion".
- C Figure 2 gives 2025:Q4 borrower shares of 74.6% nonfinancial corporate, 15.2% noncorporate, 7.8% other financial, 2.4% ROW. C Table 6 implies about 72.8%, 14.9%, 9.9% and 2.4% (library arithmetic).
- The from-whom-to-whom example gives $622 billion from private debt funds and $69 billion through MM CLOs. Both exceed the domestic holdings in C Table 6 ($532.2 billion and $53.7 billion). The note does not say whether the example includes foreign vehicles.

## What an outside investor can and cannot copy
| Item | Access, per the note |
|---|---|
| Sector balance sheets, instrument tables F4.4.s and F522.3.s | Public Z.1 tables |
| From-whom-to-whom detail | Public through the Data Download Program and FRED (C fn 14) |
| Depository loans to PD funds, BDCs, interval and tender offer funds | Public Z.1 lines (codes above) |
| Fund-level Form PF data | Confidential. Not copyable |
| BDC-level data | BDC Collateral is "proprietary". It is built from public 10-Qs and 10-Ks |
| MM CLO data | Moody's Analytics Global CLO database |
| Interval and tender offer funds | Morningstar and public SEC Form N-PORT |

What the public Z.1 data do not give: bank-level exposures, committed versus drawn amounts, loan pricing, maturities, default probabilities or ratings. Those exist only in the main note's Y-14 tables.

## Pointers the note gives
- A further FEDS Note, "U.S. Private Credit Vehicles: Institutional Structure and Aggregate Balance Sheets", holds the classification and imputation detail. This skill does not cover it.
- The Guide to the Financial Accounts holds series construction detail.
- The September 2026 release also added a hedge fund sector (C fn 2).
