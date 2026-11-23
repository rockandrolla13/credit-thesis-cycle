# Section 2: Data and Sample Construction (main note)

Source: main note, Section 2 (2.1, 2.2), footnotes 5 to 7.

## Core Idea
Private credit vehicles file almost nothing in public. The note builds its estimates from two sources: a confidential bank supervisory form (FR Y-14Q) and public BDC filings (SEC Form 10-Q). Each source needs its own matching algorithm.

## Source 1: FR Y-14Q, Schedule H.1 ("Y-14")

**What it is (Sec 2.1)**
- Quarterly reporting form filed with the Federal Reserve by "the largest U.S. banks".
- Schedule H.1 holds "all corporate loans over $1 million" extended by large bank holding companies subject to the annual Federal Reserve stress test.
- Coverage as of 2024-Q4: "about 75 percent of total bank assets in the U.S." and "around 71 percent of all bank-issued corporate loans".
- The note calls it "supervisory data". It is not public.

**Fields the note uses (Sec 2.1)**
For each reported credit facility:
- committed amount and utilized amount
- facility type: credit line or term loan
- maturity
- interest rate
- the bank's internal probability of default (PD)
- the bank's internal loss given default (LGD)
- the bank's internal credit rating
- borrower taxpayer identification number (TIN) and bank-provided borrower name (used for matching)

The risk measures are "banks' own quarterly internal risk measures". They are not agency ratings.

**How BDCs are identified (Sec 2.1)**
1. Take the list of BDCs from the SEC website (fn 6 gives the SEC open-data BDC page). The sample is 190 BDCs. 48 are publicly traded.
2. Search Y-14 for the BDC taxpayer identification numbers (TINs).
3. String-match bank-provided borrower names against BDC names and tickers.
4. Result: 99 of the 190 BDCs appear in Y-14. They account for "more than 90 percent of the total BDC assets".

**How PD funds are identified (Sec 2.1)**
1. String-match borrower names against a list of private credit managers from Preqin.
2. Run regular expression searches on borrower names for keywords such as "private credit" and "direct lending".
3. Manually verify all matches.
4. Result: 201 PD funds matched.

The note gives no coverage ratio for PD funds. It gives one only for BDCs.

## Source 2: SEC Form 10-Q filings by BDCs

**Why BDCs file (Sec 2.2)**
BDCs are not registered as investment companies. They are subject to certain provisions of the Investment Company Act and must file periodic reports, including Forms 10-Q and 10-K. Only three 10-Qs are filed per year. The fourth quarter is in the 10-K (fn 7).

**The extraction algorithm (Sec 2.2)**
1. Search the 10-Q filings for "SEC-provided tags that indicate debt commitments".
2. Use each tag's unique identifier to find other fields tied to the commitment.
3. Cross-check commitment totals against the reported aggregate debt amounts.
4. Where reported, manually collect lender names for each credit facility.

**The sample funnel (Sec 2.2)**
| Step | Count |
|---|---|
| BDCs in the SEC list | 190 |
| File 10-Qs | 140 |
| Report total assets in the 10-Q | 127 (total assets $333 billion) |
| Algorithm extracts lending data | 74 (87 percent of the $333 billion) |
| Of those, borrow from banks | 62 BDCs, 119 bank lending facilities |
| Of those, report borrowing from nonbanks | 12 BDCs |

## Other data used
- **Preqin** and **BDC Collateral via LSEG**: assets under management, Figure 1.
- **Compustat**: leverage for 40 publicly traded BDCs and about 650 other NBFIs (Sec 3.3, Figure 4).
- **FR Y-9C, S&P Capital IQ, LCR data**: capital and liquidity ratios for the stress exercise (Table 3 source line).

## Figure 1 data (recovered from the Fed's accessible version)
Assets under management, $ billion. 2024 is as of Q2.

| Year | BDCs | PD funds, invested capital | PD funds, dry powder |
|---|---|---|---|
| 2009 | 24.5 | 174.5 | 64.5 |
| 2012 | 45.2 | 197.2 | 77.7 |
| 2015 | 83.3 | 202.5 | 113.0 |
| 2019 | 123.1 | 337.1 | 214.9 |
| 2020 | 134.3 | 412.3 | 270.9 |
| 2021 | 207.7 | 559.2 | 272.4 |
| 2022 | 273.4 | 634.9 | 262.6 |
| 2023 | 318.8 | 742.3 | 279.8 |
| 2024 (Q2) | 374.9 | 753.1 | 277.9 |

Library arithmetic: the three 2024 columns sum to about $1.41 trillion. The text says $1.34 trillion "(Exhibit 1)". The note does not explain the gap, and it has no item labelled "Exhibit 1".

## What an outside investor can and cannot copy
This table is a library reading of the access status the note itself states. The note does not discuss replication by outsiders.

| Step | Source | Access status | Copyable? |
|---|---|---|---|
| List of BDCs | SEC website | Public, per the note (fn 6) | Yes |
| BDC debt commitments, drawn amounts, lender names | BDC 10-Q and 10-K filings | Public filings, per the note (Sec 2.2) | Yes, with the tag-search algorithm. Expect the note's own yield: 74 of 127 BDCs |
| BDC leverage | Compustat | Vendor database. The note does not state access terms | Yes, if you have the database |
| List of private credit managers | Preqin | Vendor database. The note does not state access terms | Yes for the list. Not for the match to bank loans |
| BDC and PD fund commitments by bank, utilization, interest rate, maturity | FR Y-14Q H.1 | Supervisory data, per the note | No |
| Bank internal PD, LGD, rating, delinquency on these loans | FR Y-14Q H.1 | Supervisory data, per the note | No |
| PD fund borrowing from banks | FR Y-14Q H.1 only | "public disclosures or regulatory filings by private credit vehicles are generally not available" | No. The note names no public substitute |
| Bank-level HHI and cosine similarity | FR Y-14Q H.1 | Supervisory data, per the note | No |
| Drawdown stress on CET1 and LCR | Y-14 undrawn amounts plus FR Y-9C, S&P Capital IQ, LCR | Inputs are mixed | The arithmetic is copyable. The undrawn amount is not, except from the note's published totals |

Practical consequence, stated in Sec 3.2: the public 10-Q route sees ALL lenders to BDCs (US banks, foreign banks, nonbanks). The confidential Y-14 route sees only the largest US banks. So the public route is wider on lenders and narrower on vehicles.

## Anti-patterns the method implies
- Do not read Y-14 totals as system totals. Y-14 covers about 71 percent of bank-issued corporate loans and no foreign bank lending booked outside these holding companies (Sec 2.1, Sec 3.2).
- Do not assume every BDC can be parsed. 53 of the 127 asset-reporting BDCs yielded no lending data (Sec 2.2).
- Do not treat keyword matches as final. The authors "manually verify all matches" (Sec 2.1).

## Limits the authors state (Sec 6)
"We also recognize the limitations of current regulatory data, and the difficulties associated with identifying banks' exposures to private credit in these data." They expect reporting changes by the banking agencies to "shed more light".
