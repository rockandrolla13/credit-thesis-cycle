# Chapter 4: When Does Capital Account Liberalization Help More Than It Hurts?

Authors: Barry Eichengreen with Carlos Arteta and Charles Wyplosz. Prepared for a conference at Tel Aviv University, March 25-26, 2001. Part II, Capital Account Liberalization. This is an empirical method chapter: cross-country growth regressions.

## Core Idea
The positive link between capital account openness and growth is "decidedly fragile". It varies with the period, the openness measure and the estimator. The one contingency with consistent support is sequencing: openness helps growth only where the black market premium is small, that is, where macroeconomic imbalances were removed first.

## Frameworks Introduced
- **Edwards regression (baseline)**: growth of GDP per capita on the period investment ratio, human capital (years of schooling), log initial GDP per capita, and the Quinn capital account index (0 to 4).
  - When to use: as the starting specification for any test of a liberalization effect.
  - Four critiques the authors raise before using it:
    1. Timing. Edwards has the Quinn index only for 1973 and 1988. One is too early and one too late for growth in the 1980s.
    2. Weights. Weighting by 1985 GDP per capita loads the result on rich countries where an effect is most plausible, and raises the reverse-causality risk (note 7).
    3. Instruments. Geographic variables may not be correlated with liberalization, and economic and financial instruments may not be exogenous.
    4. Omitted openness. Countries that open the capital account also open trade and stabilize, so the index may pick up those policies.
- **Contingency test by interaction**: add Quinn times a conditioning variable and read the pair of coefficients.
  - How: (1) Quinn times per capita GDP for the income hypothesis; (2) Quinn times liquid liabilities/GDP for financial depth; (3) Quinn times the International Country Risk Guide law and order index (0 to 6) for institutions; (4) Quinn times the Sachs-Warner open dummy for sequencing.
  - Reading: a negative level coefficient with a positive interaction means openness hurts when the conditioning variable is low and helps when it is high.
- **Sachs-Warner openness index** (Sachs and Warner 1995): a country is open if none of five criteria holds: average tariffs above 40 percent; nontariff barriers on more than 40 percent of imports; a socialist economic system; a state monopoly of major exports; a black market premium above 20 percent. The first four test trade distortion. The fifth indicates macroeconomic policy inconsistent with the administered exchange rate.
- **Decomposition test: trade distortion versus macro imbalance**.
  - How: split Sachs-Warner into (a) the Barro-Lee trade openness dummy (tariffs and nontariff barriers both under the 40 percent lines) and (b) the black market premium, each interacted with Quinn.
  - If the premium interaction matters, macro stabilization is the prerequisite (McKinnon 1991). If the trade interaction matters, removing trade distortions is the prerequisite (Brecher and Díaz-Alejandro 1977).
  - Three premium measures: BMP1 is a dummy equal to one if the premium is under 20 percent; BMP2 is 100 percent minus the premium, divided by 100; BMP3 is BMP2 truncated at zero.
  - Result: the premium interaction is positive and significant at the 90 percent level under all three measures. The trade interaction approaches significance in only one of three.
- **Three sub-periods tied to Quinn observation dates**: 1973-1981 (syndicated bank lending), 1982-1987 (debt crisis), 1988-1992 (post-Brady), plus a pooled sample with period dummies.

## Key Concepts
- **Quinn index (as used here)**: 0 to 4 in half-point steps, higher is more open. Available for 1973, 1982 and 1988.
- **IMF openness dummy**: share of years with no restriction on line E2. It gives "uniformly insignificant effects" here.
- **Black market premium**: percent premium over the official exchange rate, the chapter's indicator of macroeconomic imbalance.
- **Hall-Jones instruments**: distance from the equator, landlocked dummy, island dummy, share speaking English, share speaking a major European language.
- **Edwards-style instruments**: Quinn index in 1973, liquid liabilities/GDP in 1970 and 1975, distance to the equator, OECD dummy.
- **Immiserizing capital inflow**: foreign capital drawn into a protected sector where servicing cost exceeds the return.
- **Multicollinearity among openness measures**: Sachs-Warner, Quinn and their interaction are highly correlated, which limits what the sub-period samples can separate.

## Mental Models
- Think of a significant coefficient as one draw from a grid of period by measure by estimator. The authors move across the grid before believing anything.
- Use the black market premium as a sequencing gauge. A large premium says the administered exchange rate is inconsistent with other policies, and opening the capital account then mainly opens a route for capital flight.
- Think of bad sequencing as latent damage. It "does not actually damage growth so long as international capital markets are flush with funds", but does serious damage "if lending suddenly dries up". The negative level effect shows up only in 1982-1987.

## Anti-patterns
- **Unconditional policy advice from this evidence**: the authors say the evidence is "insufficiently robust".
- **GDP-per-capita weights in a test of an income contingency**: the weights bias toward the hypothesis.
- **Slow-moving lagged financial variables as instruments**: lagged liberalization and financial depth are correlated with current values and may not isolate the exogenous part (note 17).
- **System estimation with a derived second dependent variable**: TFP growth is derived partly from GDP growth, so errors are positively correlated and significance can be spurious (note 8).
- **Concluding from the income interaction that institutions matter**: per capita GDP is not a measure of institutions. Test the institutional variable directly.

## Reference Tables
Signs were checked against the PDF because the extract drops minus signs. Coefficients with t-statistics in parentheses. Significance: * 10 percent, ** 5 percent, *** 1 percent. All OLS with robust standard errors.

### Table 4.3, columns 1-4: Quinn index entered alone (recovered from PDF p. 89)

| | 1973-1981 | 1982-1987 | 1988-1992 | Pooled |
|---|---|---|---|---|
| Quinn index, beginning of period | 0.264 (0.94) | 0.095 (0.29) | 1.131* (1.98) | 0.487** (2.17) |
| Observations | 62 | 62 | 60 | 184 |
| R2 | 0.34 | 0.29 | 0.27 | 0.26 |

### Table 4.4, columns 5-8: interaction with law and order (recovered from PDF p. 94)

| | 1973-1981 | 1982-1987 | 1988-1992 | Pooled |
|---|---|---|---|---|
| Quinn index | -0.273 (-0.75) | -0.817** (-2.04) | 1.194* (1.70) | 0.005 (0.02) |
| Quinn x law and order | 0.171** (2.12) | 0.250** (2.44) | -0.016 (-0.11) | 0.137** (2.18) |
| Observations | 62 | 62 | 60 | 184 |
| R2 | 0.39 | 0.35 | 0.27 | 0.28 |

The financial depth interaction (columns 1-4) is 0.003, 0.002, -0.002 and 0.002 with t-statistics of 0.6 or less. None is significant.

### Table 4.5: sequencing (recovered from PDF pp. 95-96)

| | 1973-1981 | 1982-1987 | 1988-1992 | Pooled |
|---|---|---|---|---|
| Columns 1-4: Quinn index | 0.194 (0.55) | -0.361 (-1.17) | 0.455 (0.61) | 0.224 (0.85) |
| Columns 1-4: Quinn x SW open | 0.458 (1.67) | 0.919*** (3.54) | 0.917* (1.81) | 0.720*** (3.45) |
| Columns 5-8: Quinn index | 0.366 (0.93) | -0.128 (-0.36) | 1.049 (1.38) | 0.509* (1.82) |
| Columns 5-8: Quinn x SW open | -0.134 (-0.22) | 0.469 (0.90) | -0.386 (-0.37) | -0.001 (-0.01) |
| Columns 5-8: SW open in levels | 1.754 (1.37) | 1.197 (0.78) | 3.441 (1.20) | 2.020* (1.83) |
| Observations | 60 | 60 | 59 | 179 |

### Table 4.6: trade distortions versus black market premium, pooled, 141 observations (recovered from PDF pp. 99-100)

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 |
|---|---|---|---|---|---|---|
| Quinn index | -0.214 (-0.49) | 0.138 (0.42) | -0.963 (-1.40) | -0.158 (-0.37) | 0.182 (0.56) | -0.777 (-1.12) |
| Quinn x Barro-Lee trade openness | 0.324 (1.14) | 0.522** (2.01) | 0.288 (1.10) | 0.055 (0.19) | 0.251 (0.94) | 0.068 (0.26) |
| Quinn x BMP1 | 0.546* (1.69) | | | 0.520 (1.64) | | |
| Quinn x BMP2 | | 0.064** (2.52) | | | 0.056** (2.50) | |
| Quinn x BMP3 | | | 1.257** (1.99) | | | 1.091* (1.71) |
| SW open in levels | | | | 1.644** (2.22) | 1.597** (2.14) | 1.468** (2.02) |
| R2 | 0.34 | 0.34 | 0.36 | 0.37 | 0.37 | 0.38 |

## Worked Example
The chapter's own chain of tests, in order.
1. Replicate Edwards for the 1980s with 61 countries (Table 4.1). Unweighted: the 1988 Quinn level is 0.599 (t 1.48) and the 1973-1988 change is 0.600 (t 2.28). Weighted by GDP per capita: the level is 1.005 (t 2.35) and the change is 0.280 (t 0.91). So which one is significant flips with the weights.
2. Swap in the IMF dummy. Nothing approaches significance.
3. Add the income interaction. It is significant only for the level, unweighted. With the change in Quinn the signs point to smaller effects in rich countries.
4. Instrument. Hall-Jones instruments make every openness term insignificant. Edwards-style instruments (52 observations) reproduce his negative level and positive interaction, but only in levels and unweighted, and the interaction "goes to zero" if financial depth or lagged openness is dropped from the instrument list.
5. Fix timing with three sub-periods (Table 4.3). The level effect is positive in all three, significant only in 1988-1992, and significant at 95 percent when pooled, "heavily driven by one of our cross sections".
6. Test financial depth and law and order (Table 4.4). Depth fails. Law and order works in 1973-1981 and 1982-1987 and fails in 1988-1992.
7. Test sequencing (Table 4.5). The Quinn x Sachs-Warner interaction is significant at 99 percent when pooled. Adding Sachs-Warner in levels kills the interaction, and F-tests cannot choose between "separate effects" and "sequencing".
8. Decompose (Table 4.6). The premium interaction survives with Sachs-Warner in levels under BMP2 and BMP3. The two external policy measures with the most consistent effects are Sachs-Warner openness and the premium interaction.
9. Sub-periods (Table 4.7, 47 observations each). The premium result is driven by 1982-1987, where the Quinn level is -1.867 (t -3.00) and the Quinn x BMP1 interaction is 1.016 (t 2.46).

## Key Takeaways
1. Use the Quinn index, not the IMF dummy. The IMF dummy shows nothing in any specification.
2. A positive growth effect of openness is robust only for 1988-1992, the post-Brady years.
3. There is "scant support" for a financial depth contingency and "more support" for a rule-of-law contingency, which is "not overwhelming".
4. Trade openness raises growth on its own. The effect of capital account openness is not contingent on trade openness. It is contingent on a small black market premium.
5. With macro imbalances present, "capital account liberalization is as likely to hurt as to help".
6. The sequencing evidence is strongest in the 1980s and may be period-specific. The authors warn against overselling it.
7. Openness to FDI is a separate matter. The authors take the positive growth effect of FDI as established (note 2).

## Extraction Notes
- The extract drops minus signs in all regression tables, leaving extra spaces. Signs above were recovered from PDF pages 89, 94 to 96, 99 and 100. Pages 94 and 95 were checked as page images. On the other pages, signs were read from the PDF text layer, where a negative shows as a space inside the t-statistic's parenthesis.
- Table 4.7 is badly scrambled in the extract (rows and columns interleaved) and was not rebuilt. The two 1982-1987 figures quoted in the worked example come from column 2 and match the prose ("strongly negative in 1982-1987").
- Tables 4.1 and 4.2 are not reproduced in full. The figures quoted from Table 4.1 were checked against PDF pp. 85-86.
- The Table 4.1 note says "Columns 5-8 are weighted". Table 4.2 carries the same note in the extract. Recorded as printed.
- The data appendix says the law and order index starts in 1984 and "we use the 1984 value for 1973 and 1981". The cross-sections start in 1973 and 1982, so "1981" may be a slip in the source. Recorded as printed.

## Connects To
- **Ch 3**: the survey that frames Rodrik versus Edwards and the measurement problem.
- **Ch 11**: turns the sequencing result into policy order.
- **Ch 2**: the debt crisis of 1982 as the event that makes bad sequencing costly.
- **Sachs and Warner 1995; Rodriguez and Rodrik 2000**: note 32 says the latter also find most of the explanatory power of the Sachs-Warner index in the black market premium.
