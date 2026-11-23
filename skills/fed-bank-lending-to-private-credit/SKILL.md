---
name: fed-bank-lending-to-private-credit
description: "Knowledge base from the Federal Reserve FEDS Note \"Bank Lending to Private Credit: Size, Characteristics, and Financial Stability Implications\" (Berrospide, Cai, Lewis-Hayre, Zikes, May 2025), with the companion FEDS Note \"Introducing Private Credit into the Financial Accounts of the United States\" (Brinkman et al., October 2026). Use when sizing bank credit lines to BDCs and private debt funds (committed versus drawn), matching private credit vehicles in FR Y-14Q or BDC 10-Q filings, reading utilization, pricing, default probability and leverage of those loans, running a credit-line drawdown stress on CET1 and LCR, or pulling private credit sectors and instruments from the Z.1 Financial Accounts."
---

<!-- argument-hint: [topic, framework name, or section number] -->

# Bank Lending to Private Credit: Size, Characteristics, and Financial Stability Implications
**Authors**: Jose Berrospide, Fang Cai, Siddhartha Lewis-Hayre, Filip Zikes | **Type**: FEDS Note (Federal Reserve Board staff) | **Sections**: 6, plus 1 companion note | **Generated**: 2026-11-23

## Source Documents

| | Main note | Companion note |
|---|---|---|
| Exact title | Bank Lending to Private Credit: Size, Characteristics, and Financial Stability Implications | Introducing Private Credit into the Financial Accounts of the United States |
| Authors | Jose Berrospide, Fang Cai, Siddhartha Lewis-Hayre, Filip Zikes | Katie Brinkman, Christine Dobridge, Tim Dore, Simon Glossner, Elizabeth Holmquist, Nam Nguyen, Maria Perozek, Irina Stefanescu |
| Date | May 23, 2025 | October 16, 2026 |
| Series | FEDS Notes, Board of Governors of the Federal Reserve System | FEDS Notes, Board of Governors of the Federal Reserve System |
| URL | https://www.federalreserve.gov/econres/notes/feds-notes/bank-lending-to-private-credit-size-characteristics-and-financial-stability-implications-20250523.html | https://www.federalreserve.gov/econres/notes/feds-notes/introducing-private-credit-into-the-financial-accounts-of-the-united-states-20261016.html |
| DOI | https://doi.org/10.17016/2380-7172.3802 | https://doi.org/10.17016/2380-7172.4204 |
| Data end | 2024-Q4 (FR Y-14Q), 2024-Q1 (10-Q analysis) | 2025:Q4 |

Local copies: `/home/ak/Documents/PapersForThemes/fed-bank-lending-to-private-credit/` (`main.html`, `companion.html`, and the Fed's accessible figure-data pages `main-accessible.htm`, `companion-accessible.htm`).

## How to Use This Skill

- **Without arguments**: load the core frameworks below.
- **With a topic**: ask about `Y-14 matching`, `drawdown stress`, `BDC leverage`, `Z.1 private credit tables`. I read the relevant section file.
- **With a section**: ask for `sec03`. I load that file.
- **Browse**: ask "what sections do you have?".

When a question needs a number, I read the section file first. Every number carries a date and a scope. State both when you quote it.

---

## Core Frameworks & Mental Models

### 1. The headline sizes (Sec 1, Sec 3.1)
Largest US banks (FR Y-14Q filers), BDCs plus private debt (PD) funds, 2024-Q4:
- **Committed: about $95 billion.** Up from about $8 billion in 2013-Q1. Up about 145 percent in five years (about 19.5 percent a year).
- **Drawn: $56 billion.** Up about 117 percent in five years. About 5 percent of the US private credit industry (fn 4).
- Revolvers $79 billion ($49 billion BDCs, $30 billion PD funds). Term loans $16 billion ($7 billion BDCs, $9 billion PD funds).
- About 7 percent of banks' regulatory capital. About 60 percent sits at five US GSIBs.
- Context: other NBFIs $2.2 trillion committed. Nonfinancial corporates $4.2 trillion. Private credit plus private equity combined: about $322 billion (fn 2).

### 2. The two-source measurement method (Sec 2)
- **FR Y-14Q Schedule H.1**: confidential supervisory data. All corporate loans over $1 million at stress-tested bank holding companies. About 75 percent of US bank assets and 71 percent of bank-issued corporate loans. Fields: committed and utilized amounts, line or term loan, maturity, interest rate, bank-internal PD, LGD and rating.
- **BDC match**: SEC list of 190 BDCs. Search by taxpayer identification number, then string-match names and tickers. 99 found, over 90 percent of BDC assets.
- **PD fund match**: string-match borrower names against Preqin's manager list, plus keyword regex ("private credit", "direct lending"). 201 funds. All verified by hand.
- **BDC 10-Q route**: search SEC-provided tags for debt commitments, cross-check to total debt, collect lender names by hand. Funnel: 190 → 140 → 127 → 74 BDCs.

### 3. The all-lender scale-up for BDCs (Sec 3.2)
Outstanding bank credit to 74 BDCs was $43.6 billion (2024-Q1). Utilization on the 86 percent with reported commitments was 57.6 percent. Assume both ratios hold sector-wide. Result: about **$87 billion** committed to all BDCs from all lenders. Y-14 banks hold about 60 percent. Lead arrangers: 50 percent US banks, about 30 percent foreign banks, 2 percent foreign non-banks, 18 percent unknown.

### 4. The loan profile: "higher utilization, higher rates, lower PD, lower delinquency" (Sec 3.3)
| 2024-Q4 | Commit ($bn) | Util (%) | Rate (%) | Maturity (yrs) | Rating | Delinq (%) |
|---|---|---|---|---|---|---|
| BDCs | 56 | 56.8 | 6.4 | 4.1 | BBB | 0.5 |
| PD funds | 40 | 55.0 | 6.6 | 2.6 | BBB | 0.7 |
| Other NBFIs | 2193 | 48.7 | 6.2 | 3.0 | BBB | 0.7 |

Bank-estimated default probability, mean and median: BDCs 0.71 and 0.30. PD funds 2.07 and 0.22. Other NBFIs 1.65 and 0.37. Ratings and PDs are the banks' own.

### 5. The leverage watch item (Sec 3.3, Sec 6)
Public BDC debt to assets rose from about 40 percent in 2017 to 53 percent in 2024. Other NBFIs stayed near 42 percent. Sample: 40 public BDCs in Compustat.

### 6. Concentration and similarity (Sec 4.1)
Per-bank HHI of commitments across private credit borrowers: "moderate concentration", falling. Pairwise cosine similarity across banks: "low", falling. Reading: idiosyncratic drawdowns hit banks unevenly. Correlated drawdowns are the case to stress.

### 7. The full-drawdown stress test (Sec 4.2)
All undrawn lines drawn: +44 percentage points of utilization, **$36 billion**, about 2 percent of Y-14 banks' CET1 capital.
- CET1 ratio: risk weight 0.5, RWA +$18 billion, 13.02 percent to 13.0 percent (about 2 basis points).
- LCR: HQLA -$36 billion, outflow base -$14.4 billion (40 percent factor), 122 percent to 121 percent.
- With private equity funds added: $134 billion, CET1 to 12.94 percent, LCR to 120 percent (fn 10).
- The authors call it an "upper bound" for private credit vehicles "alone". Correlated drawdowns by other NBFIs are the stated open risk.

### 8. The indirect channels (Sec 5)
Affiliated BDCs and minority stakes. Partnerships. Warehouse financing and originate-to-distribute. First-lien by the bank with second-lien to a private credit manager, sometimes as a synthetic risk transfer. Caveat: banks lend to the same NBFIs that sell them the credit protection, so "some of the risk is actually not leaving the banking system as it appears". No sizes given.

### 9. Companion: private credit in the Financial Accounts (sec07)
From the September 2026 Z.1 release. 2025:Q4:
- Vehicle AUM over $2.6 trillion. US-domiciled $1.9 trillion. Private credit loans about $1.5 trillion.
- US vehicles' funding: equity $1.1 trillion, **bank loans $349 billion** (PD funds $150 billion, BDCs $181 billion, interval and tender offer funds $18 billion), debt securities $135 billion.
- Private credit is $1.31 trillion, 6 percent, of nonfinancial business debt of $23.29 trillion. Business debt to GDP is about 5 percentage points higher with it included.
- New public tables: S.124.8 (PD funds), S.124.5 (BDCs), S124.6 (interval and tender offer funds), F4.4.s (private credit loans), F522.3.s (PD fund shares).

### 10. The verdict, as the authors state it (Sec 1, Sec 6)
"growing fast but still small relative to other NBFIs". Financial stability implications "seem limited". The increasing interconnectedness "warrant[s] close monitoring".

---

## Section Index

| File | Section | Key topics |
|---|---|---|
| `chapters/sec01-introduction.md` | Main 1. Introduction | definitions, headline sizes, literature map, summary findings |
| `chapters/sec02-data-and-sample-construction.md` | Main 2. Data and sample construction | FR Y-14Q H.1 fields, BDC and PD fund matching, 10-Q algorithm, sample funnel, what outsiders can copy |
| `chapters/sec03-bank-lending-to-private-credit.md` | Main 3. Bank lending to private credit | committed versus drawn, revolvers versus term loans, 10-Q scale-up, Tables 1 and 2, utilization, BDC leverage |
| `chapters/sec04-direct-exposure-and-drawdown-stress.md` | Main 4. Direct exposure and implications | HHI, cosine similarity, $36 billion drawdown stress, CET1 and LCR arithmetic |
| `chapters/sec05-other-bank-interactions.md` | Main 5. Other interactions | affiliated BDCs, partnerships, warehouse lines, synthetic risk transfer |
| `chapters/sec06-conclusion.md` | Main 6. Conclusion | verdict, watch items, data limits |
| `chapters/sec07-companion-financial-accounts.md` | Companion note | Z.1 sectors and instruments, series codes, balance sheets, investor base, business debt effect, cross-note gap |

Reference files: `glossary.md`, `patterns.md`, `cheatsheet.md`.

## Method or Case

- **METHOD** (how to measure and test): `sec02` (data sources and matching), `sec04` (HHI, cosine similarity, drawdown stress arithmetic), the scale-up steps in `sec03` (Sec 3.2), and the measurement and classification parts of `sec07` (C Sec 3, C Sec 4 method notes).
- **CASE** (dated measurements and a dated verdict): `sec01`, the size and characteristic tables in `sec03`, `sec05`, `sec06`, and the 2025:Q4 balance sheet numbers in `sec07`.
- `sec03` and `sec07` are mixed. Each file marks its method steps separately from its numbers. When you reason fresh, take the method and leave the 2024 and 2025 levels and the "limited" verdict behind.

## Trust Notes

- **Extraction**: both notes are HTML pages, extracted in text mode. Prose and footnotes are complete. Tables came out one cell per line and were rebuilt by hand. Companion Table 1 has blank cells and its column placement was inferred from row totals. Check single cells against the Z.1 release.
- **Charts**: all figures were lost in extraction. Figure data for the main note (Figures 1 to 5) were recovered from the Fed's accessible-version page and are tabulated at selected dates only. Companion Figures 4 and 5 are not tabulated. Only the text claims about them are recorded.
- **Internal inconsistencies** are recorded in `sec03` and `sec07`. Examples: BDC loan rate 6.6 percent in text against 6.4 percent in Table 1. The $56 billion Y-14 BDC commitment is quoted for 2024-Q1 but matches 2024-Q4. "$56 billion" is used both for total drawn and for BDC committed. Foreign lending is $335 billion or $376 billion in the companion.
- **Cross-note gap**: the companion's depository loans to BDCs and PD funds ($137.0 billion and $132.5 billion at end 2024) are several times the main note's Y-14 figures. Neither note reconciles them. Do not splice the series.
- **Scope limits**: the main note covers BDCs and PD funds only, largest US banks only. It has no PD fund coverage ratio and no bank-level stress result. Ratings, PDs and LGDs are bank-internal. The risk-transfer caveat in Sec 5 rests on a press opinion piece, not data.
- **Status**: FEDS Notes are staff views, not Board positions. The main note's levels are as of 2024. The "limited" verdict is dated May 2025.
- **Not covered**: the related FEDS Note "U.S. Private Credit Vehicles: Institutional Structure and Aggregate Balance Sheets" was not fetched or read.

## Use for Credit and Macro Questions

- **Credit spreads**: nothing direct. The notes contain no spread series and no pricing model. They give the interest rate banks charge these vehicles (6.4 to 6.6 percent, 2024-Q4) and bank-internal default probabilities.
- **Debt-financed investment booms**: a measured bank-to-nonbank leverage link. Use the committed and drawn series, the BDC leverage series, and the Z.1 business debt table (private credit 6 percent of nonfinancial business debt, 2025:Q4) to size how much credit growth runs through private vehicles and how much of that rests on bank lines.
- **Inflation and Fed regimes**: almost nothing. One cited result: bank lending to BDCs helped sustain credit supply to middle-market firms through the recent tightening (Haque, Jang, Wang 2025, in Sec 1).
- **Issuer screening**: a public method for BDCs. Parse 10-Q debt commitment tags for committed, drawn and lender names, and track debt to assets. No public method for PD funds. The note names the largest BDC borrowers and lead arrangers as of 2024-Q1.
- **Central-bank view**: the staff verdict that direct-channel risk is "limited", with the stated conditions under which that could fail (correlated NBFI drawdowns, risk transfers that return to banks).
