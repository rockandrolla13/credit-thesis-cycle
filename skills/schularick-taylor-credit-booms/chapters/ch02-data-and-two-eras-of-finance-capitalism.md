# Chapter 2: Sections II and III — The Data, and Money and Credit in Two Eras of Finance Capitalism

## Core Idea
Before WW2, bank credit and broad money moved together and held a stable ratio to GDP. After WW2, credit grew faster than money in every one of the 14 countries, funded by higher leverage and nonmonetary liabilities. That decoupling is why money stops proxying for credit.

## Frameworks Introduced
- **Two eras of finance capitalism** (Section III).
  - First era, 1870 to WW2: money and credit were volatile but kept a roughly stable relationship to each other and to GDP. They grew a little faster than GDP from 1870 to about 1890, then stayed roughly stable until the 1920s credit boom. Both collapsed in the 1930s.
  - Second era, post-1945: loans and bank assets rose rapidly in the Bretton Woods era and passed their pre-1940 ratios to GDP by about 1970. Credit also rose relative to broad money. The pre-WW2 ratios of credit and assets to money were also passed circa 1970.
  - When to use: decide whether a money aggregate is a valid stand-in for credit. It was before WW2. It is not after.
- **Year-effects trend extraction** (Section III): the method behind Figures 1 and 2.
  - How: for any variable x, estimate `x_it = a_i + b_t + e_it` with country and year fixed effects. Plot the estimated year effects `b_t` as the average global level of x in year t.
  - Why it works: country fixed effects absorb level differences caused by inconsistent national definitions.
- **Two-step postwar leverage mechanism** (Section III).
  1. Banks first grew loan books relative to available deposits (higher leverage).
  2. After the 1970s they sustained credit growth with new funding sources, mainly debt securities, creating nonmonetary bank liabilities.
- **Wholesale-funding fragility chain** (Section III).
  1. Banks depend on nonmonetary funding from financial markets.
  2. Market borrowing conditions, liquidity and confidence then matter more for credit creation, and may amplify the cyclicality of financing (Adrian and Shin 2008).
  3. Deposit insurance alone no longer secures banking stability.
  4. The Lender of Last Resort must confront wholesale (nondeposit) bank runs and may have to underwrite the whole funding market, as in 2008-09. The authors call this "mission creep".

## Key Concepts
- **Total lending / bank loans**: end-of-year outstanding domestic-currency lending by domestic banks to domestic households and nonfinancial corporations, excluding lending within the financial system (Section II).
- **Banks**: monetary financial institutions, including savings banks, postal banks, credit unions, mortgage associations and building societies where data exist. Brokerage houses, finance companies and insurers are excluded (Section II).
- **Total bank assets**: year-end sum of all balance sheet assets of banks with national residency, excluding foreign currency assets (Section II).
- **Narrow money**: M0 or M1. **Broad money**: typically M2 or M3 (Section II).
- **Loan-money ratio**: bank loans over broad money, the paper's "key leverage measure" (Section II).
- **Nonmonetary liabilities**: bank funding that is not money, mainly debt securities (Section III).
- **Sample**: United States, Canada, Australia, Denmark, France, Germany, Italy, Japan, Netherlands, Norway, Spain, Sweden, Switzerland, United Kingdom. Annual, 1870-2008.
- **Excluded periods**: 1914-1919 and 1939-1947 (war and aftermath), and the post-WW1 German crisis 1920-1925 (Table 1 notes).

## Mental Models
- Think of loans/money as a regime indicator. A flat ratio means the liability side tells you what the asset side is doing. A rising ratio means it does not.
- Use within-country time variation, not cross-country levels. The authors avoid level comparisons because definitions of credit, money and banks differ profoundly across countries.
- Read the leverage build-up as global. After WW2 the rise in both ratios is "strikingly similar" in all 14 countries, not only in the Anglo-Saxon ones.

## Anti-patterns
- **Comparing credit levels across countries**: definitions differ, and for the Netherlands and Spain historical data cover commercial banks only.
- **Treating bank-balance-sheet credit as total credit**: footnote 7 says the numbers likely underestimate recent credit creation because securitized lending left bank balance sheets. In the United States, nonbank intermediaries such as broker-dealers expanded even faster than commercial banks.
- **Steering credit through money once funding is nonmonetary**: the link loosens. The authors note central banks found this out in the 1980s (Friedman and Kuttner 1992).

## Reference Tables

**Table 1 — Annual Summary Statistics by Period** (checked against PDF p. 6)

| Variable | Pre-WW2 N | Pre-WW2 Mean | Pre-WW2 SD | Post-WW2 N | Post-WW2 Mean | Post-WW2 SD |
|---|---|---|---|---|---|---|
| Loans / money (first row so labelled) | 665 | 0.4217 | 0.3582 | 831 | 0.5470 | 0.4239 |
| Assets / money (first row so labelled) | 617 | 0.7132 | 0.4453 | 828 | 1.0135 | 0.6688 |
| Broad money / GDP | 742 | 0.5343 | 0.2070 | 834 | 0.6458 | 0.2405 |
| Loans / money (second row so labelled) | 642 | 0.7581 | 0.4382 | 833 | 0.8380 | 0.4942 |
| Assets / money (second row so labelled) | 586 | 1.2790 | 0.5642 | 831 | 1.5758 | 0.7525 |
| Δ log Real GDP | 868 | 0.0148 | 0.0448 | 854 | 0.0270 | 0.0253 |
| Δ log CPI | 826 | -0.0002 | 0.0568 | 852 | 0.0452 | 0.0396 |
| Δ log Narrow money | 787 | 0.0278 | 0.0789 | 825 | 0.0780 | 0.0717 |
| Δ log Money | 741 | 0.0365 | 0.0569 | 833 | 0.0857 | 0.0552 |
| Δ log Loans | 652 | 0.0416 | 0.0898 | 833 | 0.1094 | 0.0749 |
| Δ log Assets | 607 | 0.0433 | 0.0691 | 825 | 0.1048 | 0.0678 |
| Δ log Loans / money | 626 | 0.0017 | 0.0729 | 825 | 0.0222 | 0.0643 |
| Δ log Assets / money | 573 | 0.0043 | 0.0452 | 820 | 0.0182 | 0.0595 |

Notes from the source: Money is broad money. Loans are total bank loans. Assets are total bank assets. The printed page itself repeats the labels "Loans/money" and "Assets/money". See Extraction Notes.

**What the table tests**: whether growth rates of money, loans and assets differ between eras. The authors' reading (Section II):

| Measure | Pre-WW2 | Post-WW2 | Authors' comment |
|---|---|---|---|
| Broad money growth | 3.65% | 8.57% | |
| Loan growth | 4.16% | 10.94% | Similar to money prewar, much faster postwar |
| Asset growth | 4.33% | 10.48% | Same pattern |
| Loan-money ratio growth | 0.17% per year | 2.22% per year | "a 20-fold increase" |
| Asset-money ratio growth | 0.43% per year | 1.82% per year | "a quadrupling" |

**Thresholds and dates from Section III**

| Fact | Value |
|---|---|
| Loans and assets pass pre-1940 ratios to GDP | about 1970 |
| Credit and assets pass pre-WW2 ratios to money | circa 1970 |
| Log loan-money and asset-money ratios versus prewar average, around 2000 | +0.750 log points, "about ×2 in levels" |
| Crisis frequency 1945-71 | "virtually zero" |
| Crisis frequency since 1971 | four percent annual probability (footnote 8: Bordo et al. 2001) |

## Worked Example
How the authors build the "average global trend" plotted in Figures 1 and 2:

1. Take a variable for all 14 countries and all years, for example log(loans / broad money).
2. Regress it on a full set of country dummies and year dummies: `x_it = a_i + b_t + e_it`.
3. Discard the country effects `a_i`. They hold definitional and level differences.
4. Plot the year effects `b_t` against time.
5. Read the result: flat from 1870 to 1930, a fall in the Great Depression (banking-system deleveraging), then a secular rise from the 1950s.

Cross-check with Figure 3, which shows the same ratios by country at decadal dates. The authors report one prewar exception: Italy and Spain show rapid prewar leverage growth, which they attribute to financial catch-up of the periphery relative to the core. After WW2 all countries trend up.

## Key Takeaways
1. Use bank loans to the nonfinancial private sector, deflated or scaled, as the credit variable. That is the paper's definition.
2. Loan-money growth rose from 0.17% to 2.22% per year across the WW2 break. This is the paper's headline leverage fact.
3. Use fixed effects and time-series variation. Do not compare credit levels across countries.
4. Bank-balance-sheet data understate credit where securitization and nonbanks are large.
5. Rising reliance on wholesale funding moves the run risk from depositors to funding markets.
6. Crisis frequency moved with leverage: near zero in 1945-71, about four percent a year after 1971.

## Connects To
- **Ch 1**: the money view versus credit view question these facts speak to.
- **Ch 3**: how the two eras differ after a crisis.
- **Ch 4**: Table 5 shows broad money fails as a crisis predictor postwar, the regression counterpart of the decoupling shown here.
- **Adrian and Shin (2008)**: procyclical balance sheets and market-based funding.
- **Kashyap et al. (2008), Farhi and Tirole (2009)**: cited for the case for capital and liquidity requirements.

## Extraction Notes
- Table 1 duplicate labels: not resolvable. The printed table (PDF p. 6, journal p. 1034) itself labels rows 1-2 and rows 4-5 "Loans/money" and "Assets/money", with different numbers. This is a defect in the source, not in the extraction. The text describes the upper panel as "ratios of assets and loans to money and GDP", so one pair is probably relative to GDP. The page does not say which. All numbers in the table match the page.
- Figures 1, 2 and 3 are image placeholders only. Their content above comes from the authors' prose description.
- The Table 1 notes are spliced into the middle of a body sentence in the extraction.
