# Chapter 5: Sections VI and VII — Robustness Tests, and Conclusions

## Core Idea
Adding GDP growth, inflation, interest rates, investment, stock prices and the credit-to-GDP level to the baseline never weakens the credit-growth signal. Two extra results emerge: crisis risk rises with the level of credit to GDP, and stock booms matter only in highly financialized economies. The authors conclude we moved from an "Age of Money" to an "Age of Credit".

## Frameworks Introduced
- **Omitted-variable robustness protocol** (Section VI): keep the baseline logit with country effects and five lags of real loan growth. Add five lags of one control at a time. Check three things.
  1. Do the credit lag coefficients keep their size and significance?
  2. Are the added lags jointly significant?
  3. Do pseudo R² and AUROC rise materially?
- **Investment-boom test** (Section VI, specification 19): does credit that funds investment carry less crisis risk than credit that funds consumption or speculation?
  - Result: most investment lags are insignificant. The one significant lag has the "wrong" positive sign. The sum of investment lags is positive (footnote 16).
  - Extra check: the five-year moving average of credit growth interacted with real investment growth is insignificant and does not change fit (results not reported, footnote 17).
  - Authors' inference: banks may be almost equally incapable of assessing repayment capacity in all cases.
  - Related doctrine named in footnote 15: the "Lawson doctrine", "Pitchford critique" or "consenting adults view", applied to current account deficits.
- **Leveraged versus unleveraged bubble distinction** (Section VI, citing Mishkin 2008).
  - Asset bubbles without increased leverage against higher asset values may pose no particular stability risk.
  - If booming prices relax collateral constraints, lending and prices feed each other. When the loop reverses, intermediary and household balance sheets come under severe strain.
- **Financial-depth effect** (Section VI, specifications 22, 23, 27): with country fixed effects, the level of log loans/GDP measures credit to GDP relative to the country's own average. A higher level raises crisis probability.
  - Offered explanations: complex, highly leveraged systems are more prone to disruption, or risk taking and moral hazard grow with the financial sector. Rajan (2005) is cited. Causality is left to further research.
- **Interaction design** (Section VI, Table 8): replace the five lags with five-year moving averages that exclude the current observation, then add interaction terms.
  - Credit growth × stock prices: insignificant, negative.
  - Credit growth × credit level: clearly insignificant. The effect of a credit boom does not depend on the size of the financial sector.
  - Stock prices × credit level: positive. Fit and AUROC improve considerably.
- **Age of Money versus Age of Credit** (Section VII): formerly credit was tied to money and money could proxy for credit. Financial innovation and regulatory ease broke the link.

## Key Concepts
- **Change in I/Y**: change in the investment-to-GDP ratio, the control in specification 19.
- **Nominal and real short-term interest rate**: controls in specifications 17 and 18, motivated by rates raised to defend a peg (Kaminsky and Reinhart 1999).
- **Stock prices as the only asset-price series**: house prices could not be used because of availability and comparability problems.
- **Loans / GDP (log)**: the financial-depth level variable.
- **Five-year moving average**: mean of the five preceding years, current year excluded.
- **Added-variable test**: χ² test that all five lags of the added control are zero.
- **Unwinding**: the phase when stock prices fall or credit growth reverses. The authors read the negative interaction as risk concentrating there.

## Mental Models
- Think of credit growth as the first-order signal and everything else as a small correction. Across Table 6 the pseudo R² moves from 0.0659 to at most 0.123.
- Use the level of credit to GDP as an independent second factor. It adds to the growth signal and does not multiply it.
- Treat an equity boom as conditional evidence. Weight it by financial depth. Conditional on low credit to GDP, stock booms are "inconsequential".
- Do not grade a credit boom by what it finances. The paper finds no conclusive evidence that the nature of the boom matters.

## Anti-patterns
- **"Productive credit is safe credit"**: the investment lags do not lower crisis risk.
- **Treating every asset bubble as a stability threat**: the authors cite the pre-2001 technology stock run-up as a boom that did not trigger large-scale instability.
- **Ignoring credit in a rule based on inflation and the output gap**: Section VII calls it a mishap of history that doctrine gave credit no role just when it mattered most.
- **Reading prediction as identification**: the authors say different identification strategies are clearly needed.
- **Treating credit as a perfect predictor**: Section VII notes credit can expand to support real gains in eras of financial development and innovation.

## Reference Tables

All models: logit with country effects. Credit rows are lags of Δlog(loans / P). Robust standard errors in parentheses. `***` 1 percent, `**` 5 percent, `*` 10 percent. Baseline for comparison: sum of lags 9.697, pseudo R² 0.0659, AUROC 0.717.

**Table 6 — Robustness Checks** (baseline plus five lags of one control)

| | (15) Real GDP growth | (16) Inflation | (17) Nominal short rate | (18) Real short rate | (19) Change in I/Y |
|---|---|---|---|---|---|
| L1 | 1.544 (2.081) | -0.771 (2.362) | 0.113 (2.072) | -1.458 (2.442) | -0.152 (2.250) |
| L2 | 8.571*** (2.403) | 10.22*** (2.690) | 8.491*** (2.982) | 10.99*** (2.689) | 7.131** (2.845) |
| L3 | 3.114 (2.347) | -1.590 (2.856) | 1.054 (3.443) | -1.258 (3.239) | 0.546 (3.213) |
| L4 | 2.555* (1.441) | 1.503 (1.461) | 0.241 (1.697) | 2.686 (1.673) | 1.124 (1.366) |
| L5 | 3.539** (1.555) | 1.128 (1.842) | 1.996 (2.058) | 0.821 (1.820) | 3.004 (1.943) |
| Observations / groups | 1,272 / 14 | 1,272 / 14 | 969 / 14 | 961 / 14 | 1,218 / 14 |
| Sum of credit lag coefficients | 19.32*** (4.329) | 10.49*** (3.121) | 11.89*** (3.275) | 11.78*** (3.385) | 11.65*** (3.404) |
| Test credit lags = 0, χ² | 28.99***, p 0.00002 | 24.45***, p 0.000178 | 19.45***, p 0.00159 | 26.54, p 0.00007 | 16.59, p 0.00536 |
| Test added lags = 0, χ² | 34.43, p 0.000002 | 19.55, p 0.00152 | 3.888, p 0.566 | 14.98, p 0.0105 | 4.895, p 0.429 |
| Test country effects = 0, χ² | 10.41, p 0.660 | 8.031, p 0.842 | 7.727, p 0.806 | 5.888, p 0.922 | 8.538, p 0.807 |
| Pseudo R² | 0.123 | 0.104 | 0.0765 | 0.110 | 0.0870 |
| Pseudolikelihood | -193.3 | -197.4 | -181.8 | -174.9 | -196.2 |
| Overall test, χ² | 61.47***, p 0.00023 | 52.23***, p 0.000466 | 36.40**, p 0.0275 | 47.46***, p 0.00128 | 52.38***, p 0.000445 |
| AUROC | 0.751*** (0.0432) | 0.770*** (0.0422) | 0.725*** (0.0448) | 0.750*** (0.0454) | 0.737*** (0.0419) |

The credit-lag test p-values and the rows from pseudo R² down are recovered from PDF p. 24. The page prints no significance stars on the credit-lag tests in columns 18 and 19, although their p-values are 0.00007 and 0.00536.

What each specification tests:

| Spec | Hypothesis | Verdict in the text |
|---|---|---|
| 15 | The business cycle, not credit, drives crises | Credit coefficients barely change |
| 16 | Inflation contributes to crises (Demirgüç-Kunt and Detragiache 1998) | Same |
| 17, 18 | High rates trigger crises | Some lags significant at 5 percent. Baseline story unaltered. |
| 19 | The composition of the boom matters | No conclusive evidence |

**Table 7 — Credit, Asset Prices, and Financial Development**

| | (20) + nominal stock price change | (21) + real stock price change | (22) + loans/GDP level | (23) + real stock prices + loans/GDP |
|---|---|---|---|---|
| Credit L1 | -2.491 (2.324) | -2.540 (2.312) | -0.755 (2.293) | -3.392 (2.470) |
| Credit L2 | 7.316** (2.910) | 7.165** (2.915) | 7.599*** (2.871) | 7.848** (3.215) |
| Credit L3 | 3.405 (2.899) | 3.185 (2.864) | 0.720 (3.307) | 3.297 (3.171) |
| Credit L4 | -1.352 (1.521) | -1.684 (1.539) | 0.0933 (1.497) | -1.747 (1.669) |
| Credit L5 | 1.678 (1.835) | 1.771 (1.784) | 2.326 (1.784) | 2.460 (1.994) |
| Stock L1 | -1.046** (0.464) (recovered from PDF p. 27) | -0.865** (0.434) | | -0.768* (0.455) |
| Stock L2 | 0.535 (0.644) | 0.563 (0.673) | | 0.550 (0.666) |
| Stock L3 | 0.272 (0.651) | 0.715 (0.692) | | 0.691 (0.690) |
| Stock L4 | 0.954 (0.822) | 1.098 (0.811) | | 1.024 (0.814) |
| Stock L5 | 0.0844 (0.631) | 0.467 (0.703) | | 0.438 (0.627) |
| Loans / GDP (log) | | | 1.100* (0.624) | 1.601** (0.703) |
| Observations / groups | 1,061 / 14 | 1,062 / 14 | 1,271 / 14 | 1,061 / 14 |
| Sum of credit lag coefficients | 8.557** (3.468) | 7.898** (3.443) | 9.984*** (2.918) | 8.466** (3.460) |
| Test credit lags = 0, χ² | 22.04***, p 0.000515 | 20.65***, p 0.000944 | 17.45***, p 0.00371 | 21.19***, p 0.000747 |
| Test added lags = 0, χ² | 8.664, p 0.123 | 13.28**, p 0.0209 | | 11.89**, p 0.0363 |
| Test country effects = 0, χ² | 5.499, p 0.939 | 5.433, p 0.942 | 11.43, p 0.575 | 10.33, p 0.587 |
| Pseudo R² | 0.0882 | 0.0901 | 0.0749 | 0.108 |
| Pseudolikelihood | -169.8 | -169.5 | -203.8 | -166.2 |
| Overall test, χ² | 39.65**, p 0.0119 | 46.84***, p 0.00154 | 41.48***, p 0.00208 | 47.20***, p 0.00212 |
| AUROC | 0.727*** (0.0399) | 0.731*** (0.0383) | 0.731*** (0.0379) | 0.764*** (0.0358) |

The first stock-price lag is negative in all three columns that include stock prices. The rows from pseudo R² down are recovered from PDF p. 27.

What each specification tests:

| Spec | Hypothesis | Verdict in the text |
|---|---|---|
| 20 | Nominal stock booms predict crises | Lags insignificant |
| 21 | Real stock booms predict crises | Significant at 5 percent. AUROC rises from 0.717 to 0.731. Contribution "relatively small". |
| 22 | Larger financial systems are more crisis-prone | Level significant. AUROC up "about two points". |
| 23 | Depth matters with stock prices included | Level still significant |

**Table 8 — Interactions** (regressors are five-year moving averages)

| | (24) Baseline | (25) | (26) | (27) | (28) | (29) |
|---|---|---|---|---|---|---|
| Δlog(loans/P) | 5.340*** (2.069) | 5.012** (2.288) | 7.526*** (2.464) | 6.752*** (2.012) | 6.632*** (2.243) | 7.370*** (2.368) |
| Δlog(stocks/P) | | 0.524 (1.391) | 2.704 (2.103) | | | 0.236 (1.464) |
| Δlog(loans/P) × Δlog(stocks/P) | | | -22.77 (14.19) | | | |
| Loans/GDP (log) | | | | 1.432*** (0.530) | 1.515** (0.751) | 1.704*** (0.615) |
| Δlog(loans/P) × loans/GDP (log) | | | | | -1.243 (8.516) | |
| Δlog(stocks/P) × loans/GDP (log) | | | | | | 4.661 (3.401) |
| Observations / groups | 1,278 / 14 | 1,278 / 14 | 1,278 / 14 | 1,437 / 14 | 1,437 / 14 | 1,278 / 14 |
| Test country effects = 0, χ² | 7.447, p 0.878 | 7.528, p 0.873 | 7.980, p 0.845 | 15.58, p 0.272 | 14.58, p 0.334 | 16.21, p 0.238 |
| Pseudo R² | 0.0348 | 0.0351 | 0.0407 | 0.0456 | 0.0457 | 0.0652 |
| Pseudolikelihood | -203.7 | -203.7 | -202.5 | -246.8 | -246.8 | -197.3 |
| Overall test, χ² | 17.58, p 0.227 | 18.47, p 0.239 | 22.95, p 0.115 | 35.78***, p 0.00190 | 35.71***, p 0.00317 | 30.92**, p 0.0205 |
| AUROC | 0.663*** (0.0392) | 0.662*** (0.0385) | 0.669*** (0.0369) | 0.689*** (0.0368) | 0.689*** (0.0367) | 0.714*** (0.0371) |

The pseudolikelihood, overall test and AUROC rows are recovered from PDF p. 28.

What each specification tests:

| Spec | Question | Verdict in the text |
|---|---|---|
| 24 | Does a moving average reproduce the baseline? | Yes. AUROC 0.663, a little lower than with five lags. |
| 26 | Are stock booms more dangerous during credit booms? | Interaction insignificant and negative. No meaningful gain. |
| 27, 28 | Does a credit boom do more damage in a deeper system? | No. Interaction clearly insignificant. Level effect is independent. |
| 29 | Are stock booms more dangerous in deeper systems? | "Affirmative". Fit and AUROC improve considerably. Stock coefficient falls strongly. |

## Worked Example
The authors' reading of the negative credit × stock interaction in specification 26 (Section VI):

1. Both regressors are five-year moving averages, so timing is coarse.
2. Boom phase: credit growth strong and stock prices rising. The product is positive. With a coefficient of -22.77 this lowers predicted risk. The authors say crisis risk is low in this phase.
3. Turn: stock prices start falling or credit growth reverses. The interaction term turns negative and the odds increase.
4. Interpretation: it is the unwinding of leverage-driven bubbles that puts financial stability most at risk (Mishkin 2008).
5. Caveat from the source: the coefficient is statistically insignificant, and the lag structure may partly produce the result.

## Key Takeaways
1. No control in Table 6 displaces credit. The summed credit coefficients are higher than baseline in all five columns.
2. GDP growth, inflation and the real short rate are jointly significant as added controls. The nominal short rate and investment are not.
3. Add the level of credit to GDP, relative to the country's own mean, as a second risk factor. Coefficient 1.100 to 1.704 across specifications.
4. Weight equity booms by financial depth. Specification 29 lifts AUROC from 0.663 to 0.714.
5. Among the Section VI models, specification 16 has the highest AUROC (0.770), then 23 (0.764).
6. Do not relax on "productive" credit booms.
7. Section VII policy conclusion: credit aggregates carry information about future crises, and ignoring them is a choice against the historical record. How to use them in policy is left open.

## Section VII — Conclusions in Brief
- Postwar regime conjecture: fiat money plus Lenders of Last Resort, with a slow shift back toward financial laissez faire, encouraged credit expansion.
- The policy backstop partly insulated the real economy from a scaling-up of crisis damage.
- Implicit insurance and expected rescues might have contributed to the growth of finance and leverage.
- Crises "have more often than not been the result of credit booms gone wrong", most likely through failures in the operation or regulation of the financial system.
- Footnote 19 cites the dismissed Jackson Hole warnings by Borio and White (2003) and Rajan (2005) as examples of complacency.

## Connects To
- **Ch 4**: the baseline these tests perturb.
- **Ch 2**: rising credit to GDP, the variable that becomes a risk factor here.
- **Ch 3**: the insurance-leverage conjecture repeated in Section VII.
- **Ch 1**: credit as source, not only propagator. Section VI says the financial sector "is quite capable of creating its very own shocks".
- **Mishkin (2008), Rajan (2005), Bernanke and Gertler (2001)**: the asset-price policy debate.

## Extraction Notes
- Tables 6, 7 and 8 were repaired from the PDF page images (PDF pp. 24, 27, 28). PDF page n is journal page 1028 + n. The text extraction of the bottom rows is still shuffled, so grep on the full text will not reproduce them.
- No reassembled cell changed value. The repair fixed the sign of the Table 7 column 20 first stock-price lag (-1.046**), and added the pseudolikelihood rows and the Table 6 credit-lag test p-values.
- Table 8: the column headers read only "Baseline plus" on the page as well. The added terms are identified by which rows are filled.
- Source inconsistencies, confirmed on the page images and recorded as found. The text says GDP growth and inflation cannot raise fit "substantially" (PDF p. 23), while their added-variable tests are highly significant and AUROC rises to 0.751 and 0.770. The text says adding loans/GDP raises AUROC "by about two points" (PDF p. 26), while the table shows 0.717 to 0.731. The text says "some of the lags" of interest rates are significant, while the joint test for the nominal rate has p 0.566. Columns 27 and 28 report 1,437 observations against 1,278 elsewhere, with no explanation in the text.
- The interaction with investment growth (footnote 17) is not reported in the source.
