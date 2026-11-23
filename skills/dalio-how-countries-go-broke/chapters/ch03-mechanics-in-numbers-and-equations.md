# Chapter 3: The Mechanics in Numbers and Equations

## Core Idea
Debt sustainability reduces to four ratios and one compounding identity. Measure government debt against government revenue, not GDP, then solve the identity for whichever lever (interest rate, growth, inflation, spending, taxes) must move to hold the ratio flat.

## Frameworks Introduced
- **Unsustainable debt burden (definition)**: money coming in is less than money going out, so savings fall and/or borrowing rises until savings run out or no more can be borrowed. Then "a debt failure occurs."
- **The four most important indicators** (out of "about 35 indicators"):
  1. Debts relative to income.
  2. Debt service (interest plus principal) relative to income.
  3. Nominal interest rates relative to (a) inflation and (b) nominal income growth.
  4. Debt and debt service relative to savings (e.g., reserves).
  - When to use: to size the risk and severity of a debt squeeze. They cannot time it.
  - How: track level and rate of change of each. Very high debt, very large deficits, low savings and very high, fast-rising rates mean "a very high risk of a debt default or debt devaluation crisis."
- **Debt-to-revenue, not debt-to-GDP**: "GDP doesn't matter for the government's ... finances unless it is tapped into because what matters are its actual cash flows."
- **Debt "death spiral" toy model** (Example 3) and **central bank steps in** (Example 4): see Worked Example.
- **Rate-to-FX mechanics**: lowering a rate does not much change the expected 10-year forward value of the currency. Less interest in the meantime makes the deal worse, so spot must fall to restore the return through appreciation. Printed money can also flow straight out into other currencies.

## Equations
Equations 1 to 4 below come from the EPUB's long-description text (Descriptions 3 to 7). The images themselves are absent from the extract.

1. Future debt / future revenue
   = [ (future expenses excl. interest − future revenue) + current debt × (1 + interest rate) ] / [ current revenue × (1 + growth rate) ]
2. Future debt service / future revenue
   = (future interest costs + future principal payments) / [ current revenue × (1 + growth rate) ]
   - future interest costs = future debt level × average effective interest rate on debt
   - future principal payments = future debt level × share of debts coming due
3. Interest rate required to keep debt flat
   = revenue growth rate − (future expenses excl. interest − future revenue) / starting debt level
4. Future debt / future savings
   = [ (current expenses excl. interest − current revenue) + current debt × (1 + interest rate) ] / (current savings + expected savings)
   Future debt service / future savings = (future interest costs + future principal payments) / (current savings + expected savings)
   - The author's footnote calls equation 4 "inexact" because a surplus can either build savings or pay down debt.

Footnote forms (recovered from EPUB images f0070-01.jpg and f0070-02.jpg), with g = income growth rate, i = interest rate, t = year:
- (Debt/Income)_t − (Debt/Income)_{t−1} = (i_t − g_t) × (Debt/Income)_{t−1} + (Primary Deficit/Income)_t
- To hold the ratio constant: Primary Deficit/Income = (g − i) × Debt/Income

Note: in the second footnote form "primary deficit" must be read as the sustainable primary balance. The text states it as "primary deficits as a share of income must equal the difference between growth rates and interest rates multiplied by the current ratio of debt to income."

## Key Concepts
- **Primary deficit / surplus**: revenue minus spending excluding interest.
- **Debt service**: interest plus principal due each year to avoid default.
- **Roll**: debt coming due and reissued at the new rate. Rate rises reach interest cost gradually.
- **Maturity shortening**: stressed creditors lend shorter, so principal due rises for the same debt.
- **M0**: money supply created when the central bank buys bonds with new reserves/cash.

## Mental Models
- Think of debt service as plaque in the arteries and default as the heart attack.
- Think of the economy as a Rubik's Cube: changing one driver changes the others.
- Rule of thumb: with zero primary deficit, debt/income is flat if i = g. With i 2% above g, debt/income rises around 50% over 20 years (50% becomes 75%, 400% becomes 600%). The author calls i versus g "probably the single most important variable."
- Rule of thumb: a primary deficit equal to 5% of the debt stock needs i to be 5% below revenue growth to hold the ratio flat.
- A central bank can slow debt growth by pushing i below g through bond purchases. That lowers nominal and real returns to lender-creditors. If debt growth stays as projected, "central banks will have to push real interest rates lower."

## Anti-patterns
- **Quoting debt/GDP for a sovereign's cash-flow squeeze**: GDP is "only partially related."
- **Assuming rollover**: the equations size the squeeze if debt is rolled. They do not capture holders selling.
- **Single-lever fixes**: each lever alone would be "intolerably too large."

## Reference Tables
**Example 1. Debt-to-income after 10 years, i = g** (rows: starting debt/income, columns: primary deficit as % of government revenue). The table is linear: ending ratio = starting ratio + 10 × deficit.

| Start | 0% | 5% | 10% | 15% | 20% | 30% |
|---|---|---|---|---|---|---|
| 100% | 100% | 150% | 200% | 250% | 300% | 400% |
| 300% | 300% | 350% | 400% | 450% | 500% | 600% |
| 600% | 600% | 650% | 700% | 750% | 800% | 900% |

**Central government snapshot "at the time of this writing"**

| | Debt % GDP | Debt % revenue | Deficit % GDP | Deficit % revenue | Revenue % GDP |
|---|---|---|---|---|---|
| USA | 100% | 583% | 6% | 37% | 17% |
| JPN | 215% | 1376% | 4% | 26% | 16% |
| CHN | 90% | 321% | 5% | 16% | 28% |
| FRA | 86% | 478% | 6% | 31% | 18% |
| DEU | 44% | 340% | 2% | 17% | 13% |
| GBR | 92% | 256% | 6% | 16% | 36% |

China's figures include local governments and related entities.

**Example 2. Debt-to-income after 10 years, constant 12% primary deficit** (columns: nominal interest rate minus nominal growth)

| Start | -3% | -2% | -1% | 0% | 1% | 2% | 3% |
|---|---|---|---|---|---|---|---|
| 0% | 106% | 110% | 115% | 120% | 125% | 131% | 137% |
| 300% | 329% | 357% | 387% | 420% | 455% | 494% | 536% |
| 500% | 479% | 522% | 569% | 620% | 676% | 736% | 801% |
| 600% | 553% | 604% | 660% | 720% | 786% | 857% | 934% |
| 700% | 628% | 686% | 750% | 820% | 896% | 978% | 1067% |

**Example 4. 10-year expected change in FX** (rows: FX move per 1% of GDP increase in M0, columns: maximum private bond holdings as % of government income). Assumes 12% primary deficit, starting M0 = 110% of government income, starting debt 5.8x income.

| Sensitivity | 700% | 600% | 500% | 400% | 300% | 200% | 100% |
|---|---|---|---|---|---|---|---|
| 0.5% | 0% | -5% | -13% | -21% | -28% | -34% | -40% |
| 1.0% | 0% | -10% | -25% | -38% | -49% | -58% | -65% |
| 2.0% | 0% | -19% | -44% | -62% | -75% | -84% | -89% |

**How the US can stabilize debt-to-income in the next 10 years** (one lever at a time)

| Input or lever | Value |
|---|---|
| Debt today | 100% of GDP, 583% of revenue |
| CBO projected debt 2035 | 118% of GDP, 648% of revenue |
| CBO nominal growth / real / inflation | 3.9% / 1.9% / 2.0% |
| CBO effective nominal interest rate | 3.5% (text also says 3.45%) |
| Current interest rate (average of 3M and 10Yr) | 4.5% |
| Interest rate required | 1.0% (−3.5% vs current, −2.5% vs CBO) |
| Inflation required | 4.5% (+2.5%) |
| Spending cut required | 12% (47% of discretionary spending) |
| Revenue increase required | 11% |

## Worked Example
**Toy model: a government with US-like numbers.** Income growth 3.9%, spending excluding interest 112% of income, starting debt $30.1tn (583% of income), starting rate 3.5%, 35% of debt matures each year.

Year 1: revenue $5.4tn, spending $6.0tn, principal due $10.5tn. The text gives interest of $1tn and gross issuance of $12.2tn.

Path A, **interest rates rise 50bp a year** (4.0% in year 1 to 8.5% in year 10) because buyers demand more:

| Year | 1 | 5 | 10 |
|---|---|---|---|
| Nominal income ($tn) | 5.4 | 6.3 | 7.6 |
| Interest ($tn) | 1.2 | 2.3 | 5.1 |
| Borrowing ($tn) | 12.4 | 16.8 | 26.8 |
| Ending debt ($tn) | 31.9 | 42.2 | 65.5 |
| Debt/income | 595% | 676% | 865% |
| Debt service/income | 217% | 257% | 342% |
| Interest/income | 22% | 37% | 67% |

With flat rates the same government ends year 10 at debt 650% and interest 22% of income.

Path B, **the central bank buys all issuance above a private holding cap of 600% of government income**, holding the rate at 3.5%:

| Year | 1 | 5 | 10 |
|---|---|---|---|
| Ending debt ($tn) | 31.8 | 39.4 | 51.3 |
| Money stock M0 ($tn) | 5.9 | 7.8 | 11.8 |
| Bonds held by private sector ($tn) | 31.8 | 37.5 | 45.4 |
| Debt/income | 593% | 631% | 677% |
| Interest/income | 19.5% | 20.8% | 22.4% |

The central bank buys about $6tn of bonds and M0 rises from $5.7tn to $11.8tn. At a sensitivity of 1% FX per 1% of GDP printed, the author expects about 10% currency depreciation. The debt ratio is contained and the cost moves to the currency and to bondholders.

## Key Takeaways
1. US baseline: primary deficit about 12% of revenue, plus about 20% of revenue borrowed for interest. Total deficit about 32% of revenue.
2. With i = g, US debt/revenue rises from about 580% to about 700% in 10 years. With CBO rates slightly below growth, to about 650%.
3. Higher starting debt makes the i − g term dominate. At 700% start, moving i − g from −3% to +3% moves the 10-year ratio from 628% to 1067%.
4. Observable signs of weak private demand: (a) rates rising while the economy and currency are weak, or (b) the central bank spending reserves or printing to buy government debt.
5. Governments "unfailingly" monetize when debt is in their own currency.
6. If tax cuts assumed to expire are extended, the CBO estimate is 1.5% of GDP or 8% of revenue a year worse than baseline.

## Connects To
- **Ch 4 to 6**: these ratios through 35 historical crises.
- **Ch 16**: Japan as the case of i pushed below g for 20 years.
- **Ch 17**: the same ratios in the author's US risk indicators.
- **Ch 18**: the combination of levers the author proposes.
- **Domar-style debt dynamics**: the footnote identity is the standard (i − g) form.

## Extraction Notes
- Tables arrive flattened to one cell per line. Row and column alignment was rebuilt from the cell counts. In the Example 4 table, the central bank purchase rows have fewer cells than years, so their year alignment is uncertain and is not reproduced.
- Source inconsistency, recorded not corrected: the Example 3 text says year-1 interest is $1tn and issuance $12.2tn, while the rising-rate table shows $1.2tn and $12.4tn (the table applies 4.0% in year 1).
- The colored boxes marking "US Trajectory Today" in the grids are not in the text. The prose places the US near 600% start, 10 to 15% deficit, and i − g of about −0.4%.
- Charts f0069-01, f0071-01 to f0073-01 are equation images. Their content was taken from the long-description text, not from the images.
