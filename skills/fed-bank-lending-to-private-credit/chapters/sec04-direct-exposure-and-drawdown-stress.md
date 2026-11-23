# Section 4: Banks' Direct Credit Exposure and Its Implications (main note)

Source: main note, Section 4 (4.1, 4.2), Table 3, Figure 5, footnotes 8 to 10.

## Core Idea
Two tests of the direct credit channel. First, how concentrated and how alike are banks' exposures. Second, what happens to bank capital and liquidity if every private credit vehicle draws its whole line at once. Answer to the second: about 2 basis points of CET1 ratio and about 1 percentage point of LCR.

## Framework 1: Concentration by HHI (Sec 4.1)
- Compute the Herfindahl-Hirschman Index for each bank's portfolio of commitments to its private credit clients.
- Range 0 to 1. Higher means less diversified across borrowers.
- Average the index across banks. Do it separately for BDCs and PD funds.
- Finding: the average HHI "declined significantly" over the past decade. It "remains at levels that indicate moderate concentration".

## Framework 2: Similarity by cosine similarity (Sec 4.1)
- Following Girardi et al. (2021), compute cosine similarity of commitments for each PAIR of banks.
- The note states the range as -1 to 1. Higher means more similar exposures.
- Average across all bank pairs.
- Finding: similarity also declined. "the most recent readings indicate low levels of similarity".

**Figure 5 series (recovered from the Fed's accessible version)**
| Quarter-end | HHI, BDCs | HHI, PD funds | Similarity, BDCs | Similarity, PD funds |
|---|---|---|---|---|
| 2013-Q1 | 0.43 | 0.77 | 0.13 | 0.29 |
| 2017-Q4 | 0.41 | 0.54 | 0.06 | 0.16 |
| 2019-Q4 | 0.46 | 0.39 | 0.08 | 0.09 |
| 2021-Q4 | 0.38 | 0.31 | 0.08 | 0.05 |
| 2023-Q4 | 0.32 | 0.28 | 0.06 | 0.04 |
| 2024-Q4 | 0.26 | 0.33 | 0.04 | 0.04 |

**How the authors combine the two (Sec 4.1)**
- Moderate concentration plus low similarity means banks "do not appear to be exposed to the same BDCs and PD funds".
- So IDIOSYNCRATIC drawdowns "might not affect all banks to the same degree".
- But CORRELATED drawdowns by the whole sector "could be sizable". That motivates the stress test.

## Framework 3: The full-drawdown stress test (Sec 4.2)

**Trigger the authors have in mind**: "market disruptions and restricted access to capital calls" force vehicles to draw on bank lines.

**Scenario**: private debt vehicles "withdraw all remaining undrawn funds from their credit lines".

**Steps and numbers (Table 3, footnote 9)**
1. Size the shock. Undrawn lines are drawn in full: utilization rises "about 44 percentage points", equal to **$36 billion** of new drawdowns. That is "about 2 percent of Y-14 banks' CET1 capital".
2. Capital effect. An undrawn non-cancelable line with maturity over one year carries a 50 percent risk weight (20 percent if under one year). Table 3 uses 0.5. The CET1 numerator does not change. The denominator, risk-weighted assets, rises by $18 billion.
3. Liquidity effect. Under the LCR, banks hold high-quality liquid assets equal to 40 percent of unused credit lines to NBFIs. Table 3 uses 0.4. The numerator falls by $36 billion. The denominator falls by $14.4 billion.
4. Read the result.

| Ratio | Current | Assumption | Change in numerator ($ bn) | Change in denominator ($ bn) | New ratio |
|---|---|---|---|---|---|
| CET1 ratio | 13.02% | 0.5 | 0 | +18 | 13.0% (about 2 bp lower) |
| LCR | 122% | 0.4 | -36 | -14.4 | 121% (about 1 pp lower) |

Table 3 sources: FR Y-9C, S&P Capital IQ, and LCR.

**Wider scenario (fn 10)**: add full drawdowns by private equity funds. Total new drawdowns: **$134 billion**. CET1 falls from 13.02 percent to 12.94 percent. LCR falls from 122 percent to 120 percent.

**Other rule the note records (fn 9)**: the LCR requirement is 100 percent for liquidity facilities that back commercial paper issuance and asset-backed commercial paper conduits.

## The authors' conclusion and caveat (Sec 4.2)
- Conclusion: the largest US banks are "well capitalized and highly liquid". Concerns "from the direct credit channel seem limited". These portfolios are also "subject to severe stress in supervisory stress tests".
- Caveat, in the note's words: the calculation "provides an upper bound of the potential impact from private credit vehicles alone".
- The open risk: liquidity demands from private debt vehicles "could be correlated with liquidity pressures elsewhere and lead to other NBFI drawdowns during stress". These "could exceed historical experience given that NBFIs are now more reliant on credit lines for liquidity than they have been in the past".
- Fn 8 points to Kiernan, Yankov, Zikes (2024) for a framework covering correlated drawdowns by ALL borrowers.

## What the stress test does not cover
These are limits visible in the method. The note states the first two.
- Drawdowns by other NBFIs at the same time (stated, Sec 4.2). Other NBFI commitments are $2.2 trillion against $95 billion here (Sec 3.1).
- Risk that returns to banks through synthetic risk transfers (stated, Sec 5).
- Credit losses on the drawn loans. The exercise moves risk weights and liquid assets. It applies no loss rate.
- Lending by foreign banks and non-Y-14 banks. The scenario uses Y-14 banks' CET1 and LCR only.

## Anti-pattern
Do not quote "2 basis points" as the system's exposure to private credit. It is the direct-line drawdown effect on aggregate ratios of Y-14 banks, for BDCs and PD funds alone. Sixty percent of commitments sit at five GSIBs (Sec 3.1), and the note gives no bank-level stress result.

## Connections
- Inputs: `sec03-bank-lending-to-private-credit.md`.
- Indirect channels the stress test leaves out: `sec05-other-bank-interactions.md`.
