# Chapter 3: Section IV — Money, Credit, and Output after Financial Crises: An Event Analysis

## Core Idea
The authors track money, credit, output and prices for five years after 79 banking crises, split at WW2. Postwar policy stopped the collapse of money and replaced deflation with mild inflation, yet output and investment losses relative to trend were at least as large as before.

## Frameworks Introduced
- **Crisis definition** (Section IV): a financial crisis is an event in which a country's banking sector experiences bank runs, sharp increases in default rates and large capital losses that result in public intervention, bankruptcy or forced merger of financial institutions.
  - Coding rule (footnote 9): code a crisis if a significant part of the banking system was affected, measured by the number or size of affected institutions.
- **Crisis-dating procedure** (Section IV).
  1. Start from documentary descriptions in Bordo et al. (2001) and Reinhart and Rogoff (2009).
  2. Compare and merge the two for consistent event windows.
  3. Corroborate against Laeven and Valencia (2008) and Cecchetti, Kohler and Upper (2009).
  4. Send the dates to country specialists and ask them to confirm or add events.
  5. Result: 79 major banking crises in 14 countries. The country-year table is in the online Appendix, not in the extracted text.
- **Post-crisis event window** (Section IV): compare each variable in years 0-5 of a crisis with its noncrisis ("normal") trend, separately for 1870-1939 and 1945-2008. Rerun excluding the 1930s to check that the Great Depression does not drive the result.
- **Second-derivative rule** (footnote 10): "it is the second derivative of loan growth that changes sign during a crisis, not the first" (citing Biggs, Mayer and Pick 2009). Negative loan growth is not the crisis signal. Prewar average loan growth turned slightly negative in the year after a crisis began, but the Great Depression drives that.
- **Policy-insurance feedback hypothesis** (Section IV): the authors' two-way reading of why real losses stayed large.
  - Direction 1: finance grew and levered up, so shocks to it are potentially larger, absent the policy response.
  - Direction 2 (reverse causality, stated as an open question): implicit government insurance and expected rescues may have contributed to the growth of finance and leverage, "creating more of the very hazards they were intended to solve".

## Key Concepts
- **Cumulative log level effect**: the gap between a variable's level after years 0-5 of a crisis and its noncrisis trend (Table 2).
- **Normal**: the noncrisis-year growth rate used as the benchmark in Figures 4-6.
- **Fisherian debt-deflation**: falling prices raising real debt burdens. Operated prewar. Avoided postwar.
- **Deposit insurance effect**: the authors link it to the greater stability of narrow and broad money in postwar crises.
- **Uninsured funding**: total bank assets rely more on it, and became more volatile postwar.
- **Procyclical nonloan items**: bank assets fell more than loans postwar, which the authors say confirms Adrian and Shin (2008).
- **Irregular deleveraging**: what the postwar response avoided on the loan side.

## Mental Models
- Think of postwar crisis policy as changing the nominal path, not the real path. Money and prices hold up. GDP and investment do not.
- Read the split by balance-sheet side. Insured liabilities (money) stabilized. Assets funded by uninsured sources became more volatile.
- Treat the 1930s as a special case in any prewar average. Excluding them removes the significance of the prewar output and investment declines.

## Anti-patterns
- **Using negative credit growth as the crisis signal**: footnote 10 says the sign change is in the second derivative.
- **Inferring that stronger defenses mean smaller real costs**: Table 2 shows the postwar GDP and investment effects are larger, not smaller.
- **Reading pre-1930s crises as costly on the 1930s template**: excluding the 1930s, prewar real output and investment effects are not statistically significant.

## Reference Tables

**Table 2 — Cumulative Effects after Financial Crises**
Cumulative log level effect after years 0-5 of a crisis, versus noncrisis trend. Standard errors in parentheses.

| Variable | Pre-WW2 | Pre-WW2, excluding 1930s | Post-WW2 |
|---|---|---|---|
| Log broad money | -0.139*** (0.027) | -0.103*** (0.029) | -0.077* (0.040) |
| Log narrow money | -0.083** (0.037) | -0.098*** (0.036) | 0.009 (0.053) |
| Log bank loans | -0.248*** (0.044) | -0.220*** (0.047) | -0.144*** (0.055) |
| Log bank assets | -0.156*** (0.035) | -0.144*** (0.038) | -0.258*** (0.050) |
| Log real GDP | -0.041** (0.020) | -0.018 (0.020) | -0.079*** (0.018) |
| Log real investment | -0.190** (0.091) | -0.115 (0.089) | -0.257*** (0.049) |
| Log price level | -0.089*** (0.025) | -0.055*** (0.026) | 0.007 (0.029) |

`***` 1 percent, `**` 5 percent, `*` 10 percent.

**What each column tests**

| Column | Test |
|---|---|
| Pre-WW2 | Size of post-crisis shortfall under gold-standard-era institutions |
| Pre-WW2 excluding 1930s | Whether the Great Depression alone produces the prewar result |
| Post-WW2 | Size of the shortfall under fiat money, deposit insurance and an active Lender of Last Resort |

**Dynamics described from Figures 4-6** (figures themselves not extracted)

| Variable | Pre-WW2 | Post-WW2 |
|---|---|---|
| Money and credit growth | Dipped significantly below normal. Did not recover to precrisis rates until five years after. | A dip is "hardly discernible". Only total bank assets behave differently. |
| Real output | Declines | More muted in absolute numbers, comparable relative to trend |
| Real investment | Maximum decline somewhat more pronounced, sharp bounce back after four to five years | Severe |
| Prices | Pronounced deflation for three years | Some upward pressure on inflation relative to normal |
| Narrow money | Stagnation | Expansion |

## Worked Example
Reading Table 2 the way the authors do (Section IV):

1. Compare columns 1 and 3 for nominal variables. Broad money: 14 percent below trend prewar, 8 percent postwar and "not statistically significant" in the authors' words (the table marks it at the 10 percent level). Narrow money: -8.3 percent prewar, +0.9 percent postwar. Price level: -8.9 percent prewar, +0.7 percent postwar.
2. Compare loans. 25 percent below trend prewar, 14 percent postwar. Loan-side deleveraging was smaller.
3. Compare bank assets. 16 percent below trend prewar, 26 percent postwar. The securities side became more procyclical.
4. Compare real variables. GDP: -4.1 percent prewar, -7.9 percent postwar. Investment: -19 percent prewar, more than -25 percent postwar.
5. Check column 2. Without the 1930s, prewar GDP (-1.8 percent) and investment (-11.5 percent) effects lose significance. The authors conclude the prewar output effect "is largely an artifact" of the 1930s.
6. Conclusion: more aggressive policy, same or larger real cost. The authors add that the Great Recession of 2008-2009 is not in the event sample and would strengthen this result.

Authors' two explanations for small pre-1930s losses: finance played a less central role in the economy, and economies had less nominal rigidity, especially before 1913 (Chernyshoff, Jacks and Taylor 2009).

## Key Takeaways
1. Expect loans about 14 percent and bank assets about 26 percent below trend five years after a postwar crisis.
2. Expect real GDP about 8 percent and real investment about 26 percent below trend over the same window.
3. Do not expect deflation after a postwar crisis. The price-level effect is +0.7 percent and insignificant.
4. Watch the change in credit growth, not its sign.
5. Postwar, the asset side of bank balance sheets is the volatile side.
6. The moral-hazard link from rescues to leverage is posed as an open question, not a finding.

## Connects To
- **Ch 2**: the leverage build-up that enlarges the potential shock.
- **Ch 4**: the same crisis dummy is the dependent variable in the prediction model, and the second-derivative pattern reappears in the lag coefficients.
- **Ch 5**: Section VII repeats the insurance-leverage conjecture.
- **Romer (1999)**: postwar recessions less frequent but not less severe, which the authors say their data mirror.
- **Fisher debt-deflation**.

## Extraction Notes
- Figures 4 and 5 are image placeholders. Figure 6 was extracted as scattered axis labels with no data. All figure content above comes from the authors' prose.
- The crisis-date table is in the online Appendix and is absent from the extracted text. No crisis dates can be listed.
- Source wording to note: the text calls the postwar broad money decline "not statistically significant", while Table 2 marks it with one star (10 percent level). Both are confirmed on the page image (PDF p. 13), and all Table 2 values match the page.
