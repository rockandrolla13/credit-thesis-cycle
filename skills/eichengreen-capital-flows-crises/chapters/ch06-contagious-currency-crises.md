# Chapter 6: Contagious Currency Crises

Authors: Barry Eichengreen with Andrew K. Rose and Charles Wyplosz. Portions first appeared in The Scandinavian Journal of Economics 98 (4), 1996, and in Ito and Krueger (eds), 1999. Part III, Crises. This is a method chapter: a probit on quarterly data for 20 industrial countries, 1959 to 1993.

## Core Idea
Contagion is a higher probability of a speculative attack at home that stems from an attack elsewhere, "above and beyond" domestic fundamentals. A crisis elsewhere raises the probability of a domestic crisis by about eight percentage points. Trade links, not macroeconomic similarity, are the dominant channel in this sample.

## Frameworks Introduced
- **Exchange market pressure index (EMP)** (recovered from PDF p. 175):

  `EMP(i,t) = [ a * %Δe(i,t) ] + [ b * Δ( i(i,t) - iG(t) ) ] - [ g * ( %Δr(i,t) - %Δr(G,t) ) ]`

  - `e` is the price of a Deutschmark in country i's currency, `i` the short-term interest rate, `iG` the German short rate, `r` the ratio of international reserves to narrow money M1 (note 9), and a, b, g are weights.
  - Weights are set to equalize the volatilities of the three components so that none dominates.
- **Crisis definition** (recovered from PDF p. 175):

  `Crisis(i,t) = 1 if EMP(i,t) > 1.5 * sd(EMP) + mean(EMP), and 0 otherwise`

  - Exclusion window: one quarter, applied to crises and to tranquil periods alike, so each country gives at most two observations a year.
  - Result: 77 crises and 1,179 tranquil periods.
- **Baseline contagion probit** (recovered from PDF p. 178):

  `Crisis(i,t) = w * D(Crisis(j,t)) + l * I(L)(i,t) + e(i,t)`, where `D = 1` if `Crisis(j,t) = 1` for any `j` other than `i`.

  - `I(L)` holds the controls, all as deviations from German values: capital controls, government electoral victory, government electoral loss, domestic credit growth, inflation, output growth, employment growth, the unemployment rate, the budget position/GDP, and the current account/GDP.
  - Five horizons: contemporaneous only; moving average of contemporaneous plus two lags; two lags only; contemporaneous plus four lags; contemporaneous plus eight lags.
  - Test: the null is w = 0. Rejecting it is "consistent with, but not definitive proof of, contagion".
- **Weighted contagion variable**: replace the dummy with `W(ij,t) = w(ij,t)` if `Crisis(j,t) = 1`, and 0 otherwise.
  - Trade weights: `w(ij,t) = EER(ij)`, the weight of country j in country i's IMF effective exchange rate index. These are the Multilateral Exchange Rate Model (MERM) weights, built from bilateral import and export weights in manufacturing. They do not vary over time.
  - Macro-similarity weights (recovered from PDF p. 184), for each of seven focus variables x:

    `w(ij,t) = Σj ( 1 - { Φ[ (x(jt) - m) / s ] - Φ[ (x(it) - m) / s ] } )`

    with `m` and `s` the mean and standard deviation, taken either over country i's own history (country-specific) or over all 20 countries at time t (time-specific). `Φ` is the standard normal distribution function. Identical standardized values give a weight of one. Opposite extremes give zero.
  - Seven focus variables: domestic credit growth, money growth, CPI inflation, output growth, unemployment, the current account, the budget deficit. Growth, current account and budget are multiplied by minus one so that higher always means riskier. Two standardizations times seven variables gives 14 weight sets.
- **Horse race with factor analysis**: the seven macro-weighted variables are highly collinear, so extract a single factor by the method of principal factors and enter it beside the unweighted and trade-weighted variables.
- **Two channels, two predictions**: the trade channel says crises spread among countries that trade disproportionately with each other or compete in third markets. The macro-similarity channel says crises spread among countries in similar economic and political positions, because an attack reveals information about how such governments respond.

## Key Concepts
- **Contagion**: a systematic effect on the probability of an attack that stems from attacks on other currencies, beyond domestic fundamentals.
- **Common unobserved shock**: the rival explanation. The authors compare it with an epidemiologist's problem of telling a contagious germ from a disease-conducive environment.
- **Tequila Effect**: pressure on Latin American and East Asian currencies after the Mexican peso crash of 1994, hard to explain by trade links with Mexico.
- **Competitiveness channel** (Gerlach and Smets 1995): a successful attack depreciates one currency, the partner runs a trade deficit and loses reserves, and is then attacked.
- **Selective contagion** (Buiter et al. 1998): in a system of N periphery countries pegged to a center, some leave after a center shock, and their exit relieves pressure on the rest.
- **Illiquidity channel** (Goldfajn and Valdés 1995): intermediaries offering liquid claims to foreigners face runs, which become currency runs and spread as investors liquidate elsewhere.
- **Information cascade** (Shiller 1995) and **wisdom after the fact** (Caplin and Leahy 1995): one market's reaction signals to others. Traders hold back until a crisis elsewhere confirms private suspicions.
- **Probit slope derivative**: the effect of a one-unit change in a regressor on crisis probability, in percentage points, at the mean of the data.

## Mental Models
- Think of contagion as a residual. It is what the incidence of crises elsewhere explains after fundamentals are controlled for. That is why it can never be fully separated from an omitted common shock.
- Use weighting to add structure. If a weighted measure of crises elsewhere beats the naive dummy, the result is less likely to be a common shock.
- Use the examples the chapter gives as templates: the United Kingdom to Ireland (direct export market), Finland to Sweden (third-market competition), Spain to Portugal (export market, "despite the virtual absence of imbalances in domestic fundamentals").

## Anti-patterns
- **Inferring contagion from hand-picked episodes**: collapsed pegs are unrepresentative of attacks, because some pegs are abandoned without attack and some attacks are repelled.
- **Testing contagion without controlling for fundamentals**: note 14 says Sachs, Tornell and Velasco (1996) do this.
- **Using capital flows to neighbors as a contagion proxy**: the authors' objection to Calvo and Reinhart (1995).
- **Reading the size of a weighted coefficient like the dummy's**: the weighted variable is a dummy times a weight, so its coefficient has no simple probability interpretation.
- **Entering seven collinear similarity measures and reading individual significance**: individually insignificant, jointly significant.

## Reference Tables
Probit slope derivatives times 100, with z-statistics in parentheses. Signs for negative entries were read from the PDF text layer.

### Table 6.1: benchmark (selected rows)

| | Contemporaneous | MA contemp. + 2 lags | MA of 2 lags | MA contemp. + 4 lags | MA contemp. + 8 lags |
|---|---|---|---|---|---|
| Crisis elsewhere | 7.45 (3.8) | 8.33 (4.0) | 8.14 (4.3) | 8.72 (4.0) | 8.83 (3.8) |
| Inflation rate | .75 (3.5) | .57 (2.4) | .40 (1.9) | .59 (2.1) | .64 (1.8) |
| Unemployment rate | .86 (3.0) | .96 (3.2) | .92 (3.5) | 1.04 (3.3) | 1.19 (3.4) |
| Budget position/GDP | .47 (1.9) | .41 (1.6) | .35 (1.5) | .46 (1.6) | .57 (1.8) |
| Observations | 645 | 626 | 703 | 608 | 572 |
| McFadden R2 | .15 | .12 | .13 | .12 | .10 |

### Table 6.2: sensitivity of the "crisis elsewhere" coefficient

| Perturbation | Crisis elsewhere | Observations |
|---|---|---|
| Two-quarter window, 2 sd threshold | 9.38 (3.5) | 326 |
| Doubled weight on exchange rate changes | 7.42 (3.3) | 623 |
| Pre-1979 | 12.31 (2.8) | 233 |
| EMS observations only | 19.90 (3.4) | 224 |
| Only observations with capital controls | 7.88 (2.9) | 425 |
| Events elsewhere in place of crises | 6.99 (3.4) | 626 |

### Table 6.3: trade-weighted contagion variable

| | Contemporaneous | MA contemp. + 2 lags | MA of 2 lags | MA contemp. + 4 lags | MA contemp. + 8 lags |
|---|---|---|---|---|---|
| Crisis elsewhere (trade-weighted) | .44 (5.0) | .66 (5.1) | .61 (5.3) | .72 (5.2) | .74 (5.2) |
| McFadden R2 | .18 | .19 | .19 | .19 | .18 |

### Table 6.5: macro-weighted variables entered one at a time (country-specific standardization)

| | Contemporaneous | MA of 2 lags | MA contemp. + 8 lags |
|---|---|---|---|
| Credit similarity | 6.67 (3.7) | 7.46 (4.4) | 8.82 (4.1) |
| Money similarity | 6.23 (3.8) | 7.05 (4.4) | 7.81 (3.8) |
| Inflation similarity | 7.17 (4.1) | 7.79 (4.7) | 9.21 (4.4) |
| GDP similarity | 6.03 (3.7) | 5.74 (3.8) | 6.84 (3.6) |
| Unemployment similarity | 5.10 (3.4) | 5.25 (3.6) | 5.82 (3.2) |
| Current account similarity | 7.35 (4.3) | 7.53 (4.7) | 8.91 (4.4) |
| Budget similarity | 6.15 (3.7) | 5.78 (3.8) | 6.13 (3.1) |

### Table 6.6: the three measures together (country-specific standardization; recovered from PDF p. 191)

| | Contemporaneous | MA of 2 lags | MA contemp. + 8 lags |
|---|---|---|---|
| Crises elsewhere: unweighted | 4.66 (2.0) | 5.18 (2.3) | 4.80 (1.7) |
| Crises elsewhere: trade weights | .39 (3.6) | .58 (4.3) | .75 (4.3) |
| Crises elsewhere: macro factor weights | -.85 (.6) | -1.87 (1.3) | -2.18 (1.2) |
| Contagion test, chi-squared (3) | 31 | 38 | 34 |
| McFadden R2 | .20 | .20 | .19 |

The time-specific standardization gives nearly the same numbers: unweighted 4.74, 4.97, 4.44; trade .40, .58, .73; macro factor -.94, -1.64, -1.68.

## Worked Example
The chapter's identification sequence.
1. Build the EMP index for 20 countries against Germany and flag crises at 1.5 standard deviations. The 77 crises cluster in 1973 and 1992.
2. Run the baseline probit. The dummy for a crisis elsewhere gives 7.45 to 8.83 percentage points across five horizons, with z-statistics near 4.
3. Stress the definition. A stricter threshold, a heavier exchange rate weight, pre-1979 data, capital-control observations and events in place of crises all leave the effect in place. The EMS sub-sample gives 19.90, "almost three times" the benchmark.
4. Admit the limit. The dummy cannot separate contagion from a common shock. Adding year-specific controls cuts the estimate to about 4 percent with marginal significance (note 13).
5. Add structure. Trade weights raise the fit (R2 from about .12-.15 to .18-.19) and the z-statistic to about 5.
6. Try macro weights. All seven together: individually insignificant, jointly significant (chi-squared (7) of 20 to 28). One at a time: each significant at the .01 level.
7. Run the horse race. With all three measures in, the trade-weighted variable stays positive and significant, the macro factor turns negative and insignificant, and the unweighted dummy stays significant. The last point suggests "other channels than those that we have emphasized".

## Key Takeaways
1. Define contagion operationally as the coefficient on crises elsewhere after controls. Use the eight-point estimate as the chapter's central figure.
2. Weight crises elsewhere by trade exposure first. It is the channel with the strongest support in this sample.
3. Macro similarity matters when tested alone and vanishes beside trade links. The authors allow that similarity may simply be harder to measure.
4. Inflation and unemployment are the two domestic variables that consistently raise crisis probability in these probits.
5. Contagion is far stronger inside a collective peg (the EMS sub-sample).
6. The sample is industrial countries. The authors flag emerging markets as the priority for future work, and the introduction to the book (Ch 1, note 5) cites Glick and Rose 1999 as confirming the trade result.

## Extraction Notes
- The extract leaves six formulas undecoded, all in this chapter. The EMP index, the crisis definition, the baseline probit and the macro weights were recovered from PDF pp. 175, 178 and 184. The first line of the extended (weighted) model on PDF p. 182-183 was not recovered. Its form follows from the printed definition of `W`.
- The macro weight formula is recorded as printed, with braces around the difference of the two distribution values and a summation sign over j. The prose (weight of one for identical values, zero for opposite extremes) implies the braces mean absolute distance. That reading is an inference.
- Figure 6.1 (crises per quarter) is an image placeholder and was not opened.
- The extract drops minus signs in Tables 6.1 to 6.6. Negative entries in Table 6.6 were recovered from the PDF text layer and match the prose ("negative and insignificant"). Tables 6.2 and 6.4 are not reproduced in full because their sign pattern was not checked cell by cell.
- The introduction says "eight percentage points". The conclusion says "by 8 percent". Recorded as printed.
- The chapter says its earlier work covered "some two dozen OECD economies" while the panel here and in Ch 5 is 20 countries. Ch 5 flags crises at two standard deviations with a two-quarter window (78 crises). This chapter uses 1.5 standard deviations with a one-quarter window (77 crises). Both recorded as printed.

## Connects To
- **Ch 5**: the same index, data and controls, applied to antecedents and aftermath.
- **Ch 8**: the EMS as a collective peg, and the 1992 to 1993 examples of Ireland, Portugal and Sweden.
- **Ch 9**: contagion in Asia, where trade, common creditors and investor reassessment all appear.
- **Ch 1**: the monsoonal-effects caveat.
