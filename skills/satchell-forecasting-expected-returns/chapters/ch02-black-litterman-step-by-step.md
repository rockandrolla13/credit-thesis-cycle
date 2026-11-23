# Chapter 2: A step-by-step guide to the Black-Litterman model (Incorporating user-specified confidence levels)
**Authors**: Thomas Idzorek | **Book pages**: 17-38 | **Type**: METHOD (a step procedure for building expected returns, with one illustrative eight-asset example and no empirical test)

## Core Idea
The Black-Litterman model blends market equilibrium returns with investor views to give a new expected return vector. The author gives the input-building steps that earlier papers left out. He then adds his own method: set the uncertainty of each view from a 0% to 100% confidence level. The stated aim is "intuitive, diversified portfolios" (abstract).

## Frameworks Introduced
- **Reverse optimization** (s. 2.2.1, eq. 2.1). Extract implied equilibrium excess returns Pi from market capitalization weights, the covariance matrix and a risk-aversion coefficient. Pi is "the market-neutral starting point". With no views, the investor holds the market portfolio.
- **The Black-Litterman formula** (s. 2.3.1, eq. 2.3). The new combined return vector E[R] is a "complex, weighted average" of Pi and the view vector Q. The weights depend on the scalar tau and the view uncertainty Omega.
- **View specification: absolute and relative views** (s. 2.3.2). A view is Q + epsilon. P maps each view to assets. A relative view row sums to 0. An absolute view row has a single 1.
- **Tilt-direction rule for relative views** (s. 2.3.2). Compare the view with the difference in implied equilibrium returns. If the view is smaller, the model tilts toward the nominally underperforming asset. If larger, toward the outperforming asset. For multi-asset views, compare with the weighted average implied return differential of the two mini-portfolios.
- **Two schemes for P on multi-asset views** (s. 2.3.3). Equal weighting (Satchell and Scowcroft 2000, eq. 2.6) versus market capitalization weighting (the author's choice, eq. 2.7).
- **He-Litterman calibration of Omega** (s. 2.3.3, eq. 2.8). Set omega_k / tau equal to the variance of the view portfolio p_k Sigma p_k'. Then the value of tau drops out.
- **Fine tuning by information ratio** (s. 2.3.5). Bevan and Winkelmann (1998) recommend a maximum anticipated information ratio of 2.0. Above it, lower the weight on views.
- **Implied confidence level** (s. 2.4.1). Divide each actual weight change by the weight change under 100% confidence. The ratio is the confidence that the chosen Omega implies.
- **The new method (Idzorek's seven steps)** (s. 2.4.2, eqs 2.10-2.20). Solve for each omega_k so that the tilt from view k equals the 100%-confidence tilt times the user-specified confidence C_k.
- **Two-portfolio decomposition** (s. 2.3.4). The new portfolio is the market portfolio plus a set of long-short view mini-portfolios.

### The basic procedure (ss. 2.2-2.3, Figure 2.1)
1. Estimate lambda = (E(r) - r_f) / sigma^2 (footnote 5).
2. Compute Pi = lambda Sigma w_mkt (eq. 2.1).
3. State K views. Build Q (K x 1) and P (K x N).
4. Compute each view portfolio variance p_k Sigma p_k' (Table 2.4).
5. Build diagonal Omega (eq. 2.8, or the new method of s. 2.4).
6. Compute E[R] with eq. 2.3.
7. Compute weights w = (lambda Sigma)^-1 E[R] (eq. 2.2). With constraints, feed E[R] to a mean-variance optimizer instead (s. 2.3.4, citing He and Litterman 1999 and Litterman 2003).
8. Fine tune: check the risk-return statistics and unintended results (s. 2.3.5).

### The new confidence method, steps 1-7 (s. 2.4.2)
1. For each view k alone, compute E[R_k,100%] under 100% certainty (eq. 2.12).
2. Compute w_k,100% = (lambda Sigma)^-1 E[R_k,100%] (eq. 2.13).
3. Compute the maximum departure D_k,100% = w_k,100% - w_mkt (eq. 2.14). Assets outside view k get 0.
4. Multiply element by element by confidence: Tilt_k = D_k,100% * C_k (eq. 2.15). C_k is an N x 1 vector. Assets in the view carry the confidence level. Others carry 0.
5. Target weights: w_k,% = w_mkt + Tilt_k (eq. 2.16).
6. Find omega_k > 0 that minimizes the sum of squared differences between w_k,% and w_k (eqs 2.17, 2.18).
7. Repeat for all K views. Build the K x K diagonal Omega from the omega_k values. Solve eq. 2.3 (reprinted as eq. 2.20).

Note printed at steps 1 and 6: if an absolute view is stated as a total return, subtract the risk-free rate from Q_k. Throughout, tau "is held constant and does not affect" E[R].

## Formulas
All formulas below were recovered from the PDF (book pp. 19-21, 24-25, 27, 31-32, 35-36). The text extraction lost every Greek letter.

    (2.1)  Pi = lambda * Sigma * w_mkt

- Pi: implied excess equilibrium return vector (N x 1). lambda: risk-aversion coefficient. Sigma: covariance matrix of excess returns (N x N). w_mkt: market capitalization weights (N x 1).

    (fn 5) lambda = (E(r) - r_f) / sigma^2 ,   sigma^2 = w_mkt' Sigma w_mkt

- E(r): expected market (or benchmark) total return. r_f: risk-free rate. sigma^2: variance of market excess returns. Source: Grinold and Kahn (1999).

    (fn 7) beta = Sigma w_mkt / (w_mkt' Sigma w_mkt) = Sigma w_mkt / sigma^2

- beta: vector of implied betas relative to the market capitalization-weighted portfolio.

    (2.2)  w = (lambda * Sigma)^-1 * mu

- Solution of the unconstrained problem max_w  w'mu - lambda w' Sigma w / 2. mu: any excess return vector. If mu differs from Pi, w differs from w_mkt.

    (2.3)  E[R] = [ (tau Sigma)^-1 + P' Omega^-1 P ]^-1 [ (tau Sigma)^-1 Pi + P' Omega^-1 Q ]

- E[R]: new (posterior) combined return vector (N x 1). tau: a scalar. P: K x N matrix naming the assets in each view. Omega: K x K diagonal covariance matrix of view error terms. Q: view vector (K x 1). K: number of views. N: number of assets.

    (2.4)  view = Q + epsilon ,  epsilon ~ normal, mean 0, covariance Omega
    (2.5)  Omega = diag(omega_1, ..., omega_k)

- omega_k: variance of the error term of view k. Off-diagonals are 0 because the model assumes independent views. omega = 0 means 100% confidence.

    (2.8)  Omega = diag( (p_1 Sigma p_1') * tau , ... , (p_k Sigma p_k') * tau )

- p_k: row k of P (1 x N). This is the He and Litterman (1999) calibration.

    (Fig. 2.1) prior equilibrium distribution  N ~ (Pi, tau Sigma)
               view distribution               N ~ (Q, Omega)
               new combined distribution       N ~ (E[R], [ (tau Sigma)^-1 + P' Omega^-1 P ]^-1)

    (2.9)  E[R_100%] = Pi + tau Sigma P' (P tau Sigma P')^-1 (Q - P Pi)

- The formula when every diagonal element of Omega is zero.

    (2.10) Tilt_k ≈ (w_100% - w_mkt) * C_k
    (2.11) w_k,% ≈ w_mkt + Tilt_k
    (2.12) E[R_k,100%] = Pi + tau Sigma p_k' (p_k tau Sigma p_k')^-1 (Q_k - p_k Pi)
    (2.13) w_k,100% = (lambda Sigma)^-1 E[R_k,100%]
    (2.14) D_k,100% = w_k,100% - w_mkt
    (2.15) Tilt_k = D_k,100% * C_k          (element by element)
    (2.16) w_k,% = w_mkt + Tilt_k
    (2.17) min  SUM (w_k,% - w_k)^2     subject to omega_k > 0
    (2.18) w_k = [lambda Sigma]^-1 [ (tau Sigma)^-1 + p_k' omega_k^-1 p_k ]^-1 [ (tau Sigma)^-1 Pi + p_k' omega_k^-1 Q_k ]
    (2.19) Active risk from kth view = sqrt( w_A' Sigma w_A ) ,  w_A = w_k - w_mkt      (footnote 12)
    (2.20) same as (2.3)

- C_k: user-specified confidence in view k, 0% to 100%. w_k,%: target weight vector. D_k,100%: departure from market weights under 100% confidence in view k.

Footnote 11 statistics (from Grinold and Kahn 1999):

    Residual return     theta_P  = E[R_P] - beta_P * E[R_B]
    Residual risk       omega_P  = sqrt( sigma_P^2 - beta_P^2 * sigma_B^2 )
    Active return       E[R_PA]  = E[R_P] - E[R_B]
    Active risk         Psi_P    = sqrt( omega_P^2 + beta_PA^2 * sigma_B^2 )
    Active portfolio beta  beta_PA = (beta_P - 1)

- Subscript P is the portfolio. Subscript B is the market capitalization-weighted benchmark. Note that omega_P here is residual risk, not a view variance.

## Key Concepts
- **Implied equilibrium return vector (Pi)**: "the set of returns that clear the market", found by reverse optimization (s. 2.2.1).
- **Risk-aversion coefficient (lambda)**: "the rate at which an investor will forego expected return for less variance". It scales the reverse-optimized returns (s. 2.2.1).
- **Implied betas**: betas of the N assets against the market capitalization-weighted portfolio. CAPM returns from implied betas equal Pi. CAPM returns from regression betas can differ a lot (footnote 7).
- **Absolute view / relative view**: a return level for one asset, versus a return difference between assets (s. 2.3.2).
- **Nominally outperforming / underperforming**: labels from the wording of a view. The model may tilt the other way (s. 2.3.2).
- **View portfolio variance**: p_k Sigma p_k'. A source of information on how much confidence a view deserves (s. 2.3.3).
- **Scalar tau**: roughly inversely proportional to the weight on Pi. Guidance is scarce (s. 2.3.3). Lee sets 0.01 to 0.05. Satchell and Scowcroft say it is often 1. Blamont and Firoozy read it as about 1 divided by the number of observations.
- **Omega**: "the most abstract mathematical parameter" of the model (s. 2.4).
- **w_100%**: weights under complete certainty in the views. The largest departure from market weights (s. 2.4.1).
- **Implied confidence level**: (w-hat - w_mkt) / (w_100% - w_mkt). Valid "when an asset is only named in one view" (s. 2.4.1).
- **Information coefficient**: correlation of an analyst's forecasts with results. The author suggests it as one input to view confidence (s. 2.3.5).

## Mental Models
- **Start neutral.** Without views that differ from equilibrium, hold the market portfolio (s. 2.2.1).
- **A view is a mini-portfolio.** A relative view is a long leg and a short leg that net to 0. An absolute view has no offset, so weights stop summing to 1 (s. 2.3.4).
- **Views spread through covariance.** One view changes the expected return of every asset. Yet, unconstrained, only assets named in views change weight (s. 2.3.4).
- **Only the ratio omega/tau matters** under the eq. 2.8 calibration. Changing tau from 0.025 to 15 leaves E[R] unchanged (s. 2.3.3).
- **Confidence as a dial between two portfolios.** 0% gives w_mkt. 100% gives w_100%. The stated confidence picks the point between (s. 2.4.2).

## Anti-patterns
- **Feeding historical returns to a mean-variance optimizer.** The result is extreme: 1144.32% in US Bonds (Table 2.2).
- **Assuming similar return vectors give similar weights.** Two vectors with 99.8% correlation gave weights with 66% correlation (s. 2.2.1).
- **Calling Pi "the CAPM returns" without saying which betas.** Regression betas and implied betas give different vectors (footnote 7).
- **Equal weighting in P when assets differ in size.** It moves small asset classes too much and "may result in undesired and unnecessary tracking error" (s. 2.3.3).
- **Reading a view's wording as its direction.** View 3 says growth beats value by 2%. Equilibrium already implies 2.47%. The model cuts growth (s. 2.3.2).
- **Setting Omega from view portfolio variance alone.** It "ignores the stated confidence levels" of 25%, 50% and 65% (s. 2.4.1).
- **Leaving implied views unstated.** If a view implies views on highly correlated assets, the author says to "make these views explicit" (footnote 10).
- **Keeping absolute views under a unity constraint without checking.** Such investors "may want to remove absolute views" (s. 2.3.5).
- **Using a simple historical covariance matrix by default.** Use "the best possible estimate" (s. 2.3.5).

## Reference Tables

**Table 2.1 Expected excess return vectors** (60 months of excess returns, risk premium of 3, lambda about 3.07)

| Asset class | Historical | CAPM GSMI | CAPM portfolio | Pi |
|---|---|---|---|---|
| US Bonds | 3.15% | 0.02% | 0.08% | 0.08% |
| Int'l Bonds | 1.75% | 0.18% | 0.67% | 0.67% |
| US Large Growth | -6.39% | 5.57% | 6.41% | 6.41% |
| US Large Value | -2.86% | 3.39% | 4.08% | 4.08% |
| US Small Growth | -6.75% | 6.59% | 7.43% | 7.43% |
| US Small Value | -0.54% | 3.16% | 3.70% | 3.70% |
| Int'l Dev. Equity | -6.75% | 3.92% | 4.80% | 4.80% |
| Int'l Emerg. Equity | -5.26% | 5.60% | 6.60% | 6.60% |
| Weighted average | -1.97% | 2.41% | 3.00% | 3.00% |
| Standard deviation | 3.73% | 2.28% | 2.53% | 2.53% |

**Table 2.2 Recommended portfolio weights** (eq. 2.2 applied to each vector)

| Asset class | Historical | CAPM GSMI | From Pi | w_mkt |
|---|---|---|---|---|
| US Bonds | 1144.32% | 21.33% | 19.34% | 19.34% |
| Int'l Bonds | -104.59% | 5.19% | 26.13% | 26.13% |
| US Large Growth | 54.99% | 10.80% | 12.09% | 12.09% |
| US Large Value | -5.29% | 10.82% | 12.09% | 12.09% |
| US Small Growth | -60.52% | 3.73% | 1.34% | 1.34% |
| US Small Value | 81.47% | -0.49% | 1.34% | 1.34% |
| Int'l Dev. Equity | -104.36% | 17.10% | 24.18% | 24.18% |
| Int'l Emerg. Equity | 14.59% | 2.14% | 3.49% | 3.49% |

**Tables 2.3a / 2.3b View 3 mini-portfolios**

| Leg | Asset | Market cap ($bn) | Relative weight | Pi | Weighted |
|---|---|---|---|---|---|
| Outperforming | US Large Growth | 5174 | 90% | 6.41% | 5.77% |
| Outperforming | US Small Growth | 575 | 10% | 7.43% | 0.74% |
| | Total | 5749 | 100% | | 6.52% |
| Underperforming | US Large Value | 5174 | 90% | 4.08% | 3.67% |
| Underperforming | US Small Value | 575 | 10% | 3.70% | 0.37% |
| | Total | 5749 | 100% | | 4.04% |

**Table 2.4 Variance of the view portfolios**: View 1 = 2.836%. View 2 = 0.563%. View 3 = 3.462%.

**Table 2.5 Covariance matrix of excess returns (Sigma)**. Column order equals row order. (Verified against PDF, book p. 29.)

| | USB | IntB | USLG | USLV | USSG | USSV | IntDev | IntEm |
|---|---|---|---|---|---|---|---|---|
| US Bonds | 0.001005 | 0.001328 | -0.000579 | -0.000675 | 0.000121 | 0.000128 | -0.000445 | -0.000437 |
| Int'l Bonds | 0.001328 | 0.007277 | -0.001307 | -0.000610 | -0.002237 | -0.000989 | 0.001442 | -0.001535 |
| US Large Growth | -0.000579 | -0.001307 | 0.059852 | 0.027588 | 0.063497 | 0.023036 | 0.032967 | 0.048039 |
| US Large Value | -0.000675 | -0.000610 | 0.027588 | 0.029609 | 0.026572 | 0.021465 | 0.020697 | 0.029854 |
| US Small Growth | 0.000121 | -0.002237 | 0.063497 | 0.026572 | 0.102488 | 0.042744 | 0.039943 | 0.065994 |
| US Small Value | 0.000128 | -0.000989 | 0.023036 | 0.021465 | 0.042744 | 0.032056 | 0.019881 | 0.032235 |
| Int'l Dev. Equity | -0.000445 | 0.001442 | 0.032967 | 0.020697 | 0.039943 | 0.019881 | 0.028355 | 0.035064 |
| Int'l Emerg. Equity | -0.000437 | -0.001535 | 0.048039 | 0.029854 | 0.065994 | 0.032235 | 0.035064 | 0.079958 |

**Table 2.6 Return vectors and resulting portfolio weights**

| Asset class | E[R] | Pi | E[R]-Pi | w-hat | w_mkt | w-hat - w_mkt |
|---|---|---|---|---|---|---|
| US Bonds | 0.07% | 0.08% | -0.02% | 29.88% | 19.34% | 10.54% |
| Int'l Bonds | 0.50% | 0.67% | -0.17% | 15.59% | 26.13% | -10.54% |
| US Large Growth | 6.50% | 6.41% | 0.08% | 9.35% | 12.09% | -2.73% |
| US Large Value | 4.32% | 4.08% | 0.24% | 14.82% | 12.09% | 2.73% |
| US Small Growth | 7.59% | 7.43% | 0.16% | 1.04% | 1.34% | -0.30% |
| US Small Value | 3.94% | 3.70% | 0.23% | 1.65% | 1.34% | 0.30% |
| Int'l Dev. Equity | 4.93% | 4.80% | 0.13% | 27.81% | 24.18% | 3.63% |
| Int'l Emerg. Equity | 6.84% | 6.60% | 0.24% | 3.49% | 3.49% | 0.00% |
| Sum | | | | 103.63% | 100.00% | 3.63% |

**Table 2.7 Portfolio statistics**

| Statistic | Market portfolio | Black-Litterman portfolio |
|---|---|---|
| Excess return | 3.000% | 3.101% |
| Variance | 0.00979 | 0.01012 |
| Standard deviation | 9.893% | 10.058% |
| Beta | 1 | 1.01256 |
| Residual return | - | 0.063% |
| Residual risk | - | 0.904% |
| Active return | - | 0.101% |
| Active risk | - | 0.913% |
| Sharpe ratio | 0.3033 | 0.3083 |
| Information ratio | - | 0.0699 |

**Table 2.8 Implied confidence level of views**

| Asset class | w-hat - w_mkt | w_100% | w_100% - w_mkt | Implied confidence |
|---|---|---|---|---|
| US Bonds | 10.54% | 43.82% | 24.48% | 43.06% |
| Int'l Bonds | -10.54% | 1.65% | -24.48% | 43.06% |
| US Large Growth | -2.73% | 3.81% | -8.28% | 33.02% |
| US Large Value | 2.73% | 20.37% | 8.28% | 33.02% |
| US Small Growth | -0.30% | 0.42% | -0.92% | 33.02% |
| US Small Value | 0.30% | 2.26% | 0.92% | 33.02% |
| Int'l Dev. Equity | 3.63% | 35.21% | 11.03% | 32.94% |
| Int'l Emerg. Equity | - | 3.49% | - | - |

## Worked Example
The eight-asset example runs through the whole chapter.

1. **Equilibrium.** Risk premium 3, lambda about 3.07, 60 months of data. Eq. 2.1 gives Pi (Table 2.1). Eq. 2.2 on Pi returns w_mkt (Table 2.2).
2. **Views** (s. 2.3.2).
   - View 1: Int'l Developed Equity has an absolute excess return of 5.25% (confidence 25%). Pi gives 4.80%, so the view is 45 basis points higher.
   - View 2: Int'l Bonds outperform US Bonds by 25 basis points (confidence 50%). Pi implies 0.59%. The view is smaller, so expect a tilt toward US Bonds.
   - View 3: US Large Growth and US Small Growth outperform US Large Value and US Small Value by 2% (confidence 65%). Pi implies 2.47% (Tables 2.3a, 2.3b). The view is smaller, so expect a tilt toward value.
3. **Inputs** (eqs 2.4, 2.7). Asset order as in Table 2.1.

        Q = [5.25, 0.25, 2]'

        P = [  0   0   0    0    0    0   1   0 ]      (market capitalization method, eq. 2.7)
            [ -1   1   0    0    0    0   0   0 ]
            [  0   0  .9  -.9   .1  -.1   0   0 ]

   The equal-weighting alternative (eq. 2.6) has row 3 = [0 0 .5 -.5 .5 -.5 0 0].
4. **Omega** (eq. 2.8). With tau = 0.025 and Table 2.4 variances: Omega = diag(0.000709, 0.000141, 0.000866).
5. **Result** (Table 2.6). All eight expected returns change. Only the seven assets named in views change weight. US Bonds rise 10.54 points and Int'l Bonds fall 10.54. Value rises and growth falls, by 2.73 (large) and 0.30 (small). Int'l Developed Equity rises 3.63. Weights sum to 103.63% because View 1 has no offset.
6. **Check** (Table 2.7). Sharpe ratio moves from 0.3033 to 0.3083. The ex ante information ratio is 0.0699, far below the 2.0 ceiling.
7. **Implied confidence** (Table 2.8). The eq. 2.8 calibration implies 32.94% (View 1), 43.06% (View 2) and 33.02% (View 3). The stated levels were 25%, 50% and 65%. This gap motivates the new method.

The chapter does not print the omega_k values or final weights that the new method (steps 1-7) gives for this example.

## Key Takeaways
- Mean-variance optimization fails on three linked problems: concentrated portfolios, input sensitivity, and estimation error maximization (s. 2.1).
- Reverse-optimized equilibrium returns give a neutral start that maps back to market weights (s. 2.2.1).
- The model is a weighted average of Pi and Q. Tau and Omega set the weights. Both are hard to specify (s. 2.3.3).
- Higher confidence in a view moves E[R] toward the view. Lower confidence keeps it near Pi (s. 2.3.3).
- Under the He-Litterman calibration, tau becomes irrelevant (s. 2.3.3).
- The author prefers market capitalization weights in P over equal weights (s. 2.3.3).
- With constraints, the model is less intuitive. Pass E[R] to an optimizer (s. 2.3.4).
- The new method ties each omega_k to a stated 0% to 100% confidence and removes the need to choose tau (s. 2.4.2).

## Source Defects
- **Damaged in text**: every Greek letter (Pi, lambda, Sigma, tau, Omega, omega, epsilon, mu, beta), all decimal points, and the layout of eqs 2.3, 2.9, 2.12, 2.18 and the matrices.
- **Recovered from PDF**: eqs 2.1-2.20, footnotes 5, 7, 11 and 12, Figure 2.1 labels, and Tables 2.1-2.8 (book pp. 19-36). PDF page = book page + 8.
- **Not recoverable**: Figure 2.2 is a bar chart with no data labels. Use Table 2.8 for its numbers.
- **Inconsistencies in the source, recorded as printed**:
  - Tables 2.3a and 2.3b give 6.52% and 4.04%. The text states the differential as 2.47%.
  - Section 2.3.3 says the three-view example is "presented in Section 2.2". The views appear in s. 2.3.2.
  - The text calls omega "the variance of each error term" and also "the absolute difference from the error term's expected value of 0".
  - Footnote 11 calls sigma_B and sigma_P "the variance". Its formulas square them.
  - Table 2.6 shows US Bonds at 0.07% versus 0.08% with a difference of -0.02%.
  - Eq. 2.19 sits in a footnote. Eq. 2.20 repeats eq. 2.3.
  - The symbol omega means view variance in the body and residual risk in footnote 11.

## Connects To
- **ch03-black-litterman-demystified**: the Satchell and Scowcroft paper this chapter cites for the equal-weighting P, for tau "often set to 1", and for the posterior variance. Note the labelling differs. This chapter calls the equilibrium the prior. Chapter 3 treats the views as the prior.
- **ch08-robust-optimization**: another response to input sensitivity in mean-variance optimization.
- **ch04-portfolios-from-ordering-information**: another route from views to portfolios.
- **ch05-choices-in-forecast-construction**: forecast construction choices that feed any view vector.
