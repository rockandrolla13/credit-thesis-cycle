# Chapter 5: Some choices in forecast construction
**Authors**: Stephen Wright and Stephen Satchell | **Book pages**: 101-116 | **Type**: METHOD (it sets out a framework for merging forecasts and a risk measure for optimizing on them. It has no data set and no empirical results)

## Core Idea
A forecast of return is a probability distribution, not a number. The authors say there is "no single 'correct' way" to build it. They offer a standard form, the mixture of normals, that can hold the output of many model types at once. The form can be highly non-normal, so they pair it with mean-CVaR optimization on a Monte Carlo set. The authors call it "a framework for comparing, contrasting and communicating the results of other models, rather than a model in its own right" (s. 5.2).

## Frameworks Introduced
- **Linear factor model (LFM) as a local linearization** (s. 5.2, eq. 5.1-5.5). Returns are a non-linear function of factors and noise. A Taylor expansion gives the linear form. The linear coefficients are partial derivatives at one point, so they are local.
  - Two caveats the authors list (s. 5.2): (1) the point of linearization changes with time, (2) the partial derivatives change as that point changes.
  - Their response: recalculate factor exposures every period and stay "agnostic as to how the recalculation is done".
- **Three parameter-behaviour assumptions** (s. 5.2). The user picks one:
  1. Stationary parameters.
  2. Smoothly varying parameters over time.
  3. Discontinuous parameter behaviour.
  The authors say modelling techniques lie "on a spectrum of increasing complexity" as assumptions relax from (1) to (3).
- **Local normality** (s. 5.1, s. 5.3). Returns are normal over short periods or conditional on a state of the world. Unconditional returns can then be non-normal.
- **Mixture of normals risk model** (s. 5.3, eq. 5.6-5.7). There are m regimes. Each regime has its own multivariate normal and a probability. The unconditional density is the probability-weighted sum.
  - Three routes to the same form (s. 5.3): identified or hidden regimes (regime-switching, Hamilton 1989), smoothly moving states (GARCH, Kalman filter), and several candidate models each given a degree of belief.
- **The four-state example** (s. 5.3), S = 4:
  1. High alpha, high risk.
  2. High alpha, low risk.
  3. Low alpha, high risk.
  4. Low alpha, low risk.
  The authors place the time of writing in regime 4 and "circa 2000-2002" in regime 3.
- **Mixed estimation for relative value views** (s. 5.4.3, eq. 5.9-5.13). A normal prior is multiplied by a normal likelihood for views on linear combinations of assets. The authors credit Black and Litterman for popularizing it.
- **Stochastic scenarios** (s. 5.4.3). Each state of the world has its own multivariate normal. Individual scenarios are drawn from it. The result is a Monte Carlo distribution. Arbitrary payoff functions can then be applied for options, convertible bonds or structured products.
- **Threshold risk measures and mean-CVaR optimization** (s. 5.5). VaR, CVaR and the loss gain ratio. CVaR is optimized by linear programming on the Monte Carlo set.
- **Six model types the form supports** (s. 5.6): scorecards, equilibrium models, factor models, scenario and stochastic scenario models, Bayesian updating models, relative value models.

## Formulas
All Greek symbols below were lost in the text extraction. All are recovered from the PDF pages cited.

**Linear factor model** (eq. 5.1, recovered from PDF, book p. 104):

    Y_it = Σ β_ijt f_jt + V_it,     i = 1,...,n,  j = 1,...,k

- y_it: return, or rate of return, to asset i at time t. The equation prints capital Y.
- β_ijt: exposure of asset i's return to factor j at time t.
- f_jt: value of factor j at time t.
- V_it: idiosyncratic error, with mean α_it and variance σ_i^2.
- The printed sum carries no index. The text implies a sum over j.
- Key assumption: the factors pick up the common covariation, so the V_it are uncorrelated.

**Matrix form** (eq. 5.2, recovered from PDF, book p. 104):

    y = β f + V

- y and V are n x 1 vectors. f is a k x 1 vector. β is an n x k matrix.

**Non-linear origin** (eq. 5.3, recovered from PDF, book p. 104):

    y = H(f, U)

- H: an n x 1 vector non-linear function. U: an m x 1 source of noise.

**Taylor expansion around zero vectors** (eq. 5.4, recovered from PDF, book p. 104):

    y = H(0,0) + H1(0,0) f + H2(0,0) U + Rem_t

- H1(0,0): the n x k matrix of partial derivatives with respect to f.
- H2(0,0): the n x m matrix of partial derivatives with respect to U.
- Rem_t: higher-order terms.
- The authors equate β_t to H1(0,0).

**Idiosyncratic term** (eq. 5.5, as printed, book p. 104):

    V = H(0,0) = H2(0,0) U + Rem_t

- The page prints "=" between H(0,0) and H2(0,0)U. Comparison with eq. 5.4 suggests a "+" was meant. Recorded, not corrected.

**Regime density** (eq. 5.6, recovered from PDF, book p. 107):

    Pdf_i(x) ~ N(μ_l, Ω_l)

- μ_l, Ω_l: mean vector and covariance matrix of returns in regime l, with l = 1...m.
- N(.): multivariate normal.
- The left side carries subscript i on the page. The right side uses l.

**Regime probabilities and mixture** (eq. 5.7, recovered from PDF, book p. 107):

    Σ π_l = 1,   l = 1,...,m
    pdf(x) = Σ π_l pdf_l(x)

- π_l: probability of regime l.

**Forecast scores with full covariance** (eq. 5.8, recovered from PDF, book p. 109. The authors attribute it to Grinold and Kahn 1999, p. 263):

    E(y|g) = E(y) + Cov(y, g) . Var^-1(g) (g - E(g))

- g: vector of raw forecast scores. y: return vector.
- In the authors' words: expected return given the scores equals consensus expected return plus a scaled deviation of the score from its consensus value.

**Bayes' equation** (unnumbered, book p. 109):

    P(A|B) = P(A)(P(B|A)/P(B))

**Prior and view densities** (eq. 5.9-5.10, recovered from PDF, book p. 110):

    pdf_1(r) = c exp(-0.5 (x - μ)' S^-1 (x - μ))        (5.9)
    pdf_2(x) = c exp(-0.5 (x - g)' V^-1 (x - g))        (5.10)

- μ, S: mean and covariance of the prior. In the Black-Litterman form the prior comes from CAPM equilibrium assumptions.
- x: relative return. g, V: its mean and covariance.
- Eq. 5.9 prints r on the left and x on the right. Recorded as printed.

**View portfolios** (eq. 5.11-5.12, recovered from PDF, book p. 111):

    x = P.r                                              (5.11)
    pdf_2(r) ∝ exp(-0.5 (P.r - g)' V^-1 (P.r - g))       (5.12)

- P: the matrix of linear combinations. The text calls x the return on "a set of hypothetical portfolios".

**Product of prior and likelihood** (eq. 5.13, recovered from PDF, book p. 111):

    pdf_1(r) x pdf_2(r) ∝ exp(-0.5 (r - μ)' S^-1 (r - μ) - 0.5 (P.r - g)' V^-1 (P.r - g))

**Updated mean and covariance** (unnumbered, recovered from PDF, book p. 111):

    β = [S^-1 + P' V^-1 P]^-1 [S^-1 μ + P' V^-1 g]
    Σ = [S^-1 + P' V^-1 P]^-1

- β here is the updated mean. The same letter is the exposure matrix in eq. 5.2.
- Σ here is the updated covariance.
- The authors refer to Satchell and Scowcroft (2000) for the expansion.

**Simplex standard form** (unnumbered, book p. 114):

    Maximize   Z = a_1 x_1 + a_2 x_2 + ... + a_n x_n
    subject to x_i >= 0,  i = 1,...,n
    and constraints of the form
               a_i1 x_1 + a_i2 x_2 + ... + a_in x_n <= b_i
            or a_i1 x_1 + a_i2 x_2 + ... + a_in x_n >= b_i
            or a_i1 x_1 + a_i2 x_2 + ... + a_in x_n  = b_i

- The chapter gives no formula for VaR, CVaR or the loss gain ratio. It defines them in words only.

## Key Concepts
- **Ergodic** (footnote 1): a stochastic process whose "sample properties mirror its population properties".
- **Frequentist view versus likelihood view** (s. 5.1). Long-horizon investors can lean on large-sample theory. Investors judged quarterly or annually need the likelihood view, which augments noisy data with theory, judgement and experience.
- **Temporal aggregation** (s. 5.2). Correlation of hourly data is not correlation of monthly data. Hourly data carry end-of-day effects. The density of daily prices cannot always be recovered from the density of hourly prices.
- **Conjugate prior form** (s. 5.4.2). A normal prior times a normal likelihood gives a normal posterior. The posterior can serve as the next prior.
- **Mixed estimation** (s. 5.4.3). The authors' name for the Bayesian update with relative value views.
- **Scorecard** (s. 5.3, s. 5.6). A rank-based forecast format from the authors' earlier papers. The simplified four-state model uses four scorecards, one per scenario, each with a probability, and one shared covariance structure.
- **VaR** (s. 5.5). It "relates the probability of falling below a return threshold to the level of that return threshold".
- **CVaR, or mean excess loss** (s. 5.5). The "average expected loss conditional on a return threshold being exceeded". The authors call it sub-additive and convex, citing Artzner et al. (1999).
- **Loss gain ratio** (s. 5.5). CVaR divided by upside potential. Upside potential is "the weighted probability of exceeding the threshold return".

## Mental Models
- Treat the investment committee's question as fixed: "what do we do next, given our understanding of current local linearities?" (s. 5.2).
- The only certainty in forecasting is change. The only decision needed at each rebalance is what to do next (s. 5.2).
- Different forecast styles matter at different times. Top-down macro views are critical at business-cycle turning points. Stock-specific issues dominate mid-cycle (s. 5.1).
- Forecast a dimension or hedge it. Every dimension should be accommodated, "or the risks implicit in not forecasting a dimension should be hedged away" (s. 5.1).
- Read the Bayesian view update as a set of "fuzzy" simultaneous linear equations. Each equation has its own confidence. The prior biases the fit toward the most likely solution (s. 5.4.3).
- Add sophistication "when (and only when)" the problem needs it (s. 5.3).
- Model-building is deciding when an approximation is close enough and when to elaborate (s. 5.4.2).
- Each Monte Carlo draw defines a hyperplane in asset-weight space. Portfolios above it beat the threshold return for that draw (s. 5.5).
- Return drivers get arbitraged away once understood. The modelling process is "chasing a moving target" (s. 5.6).

## Anti-patterns
- **Fixed coefficients in a linear factor model** (s. 5.2). They "suffer from severe inaccuracies through time, unless the underlying structure is actually linear".
- **Trusting a rolling window to catch a new factor** (s. 5.2). "Virtually all linear factor models failed in the late 1990s" on the Internet factor.
- **Fixing that with higher-frequency data alone** (s. 5.2). It adds noise sensitivity, misses parameter jumps, and measures something different.
- **Double-counting correlated inputs** (s. 5.4.1). High scores on two correlated factors count the same score twice.
- **Sequential Bayesian updates with dependent information** (s. 5.4.2). The method assumes each new input is independent of all earlier inputs.
- **Assuming every input is correlated with every other** (s. 5.4.2). It adds noise and removes physical insight into the estimation.
- **Reading the Black-Litterman posterior covariance as the real covariance of asset returns** (s. 5.4.3). The authors say it "should not be interpreted" that way.
- **Too few scenarios** (s. 5.4.3). An optimizer needs "many more scenarios than there are assets".
- **Classical mean-variance on a non-normal forecast** (s. 5.5). It "will implicitly fit the nearest normal distribution" and lose the non-normal information.
- **Optimizing on VaR** (s. 5.5). See the three problems below.

## Reference Tables
The chapter prints no numbered tables. The two tables below are compiled from the text of s. 5.4 and s. 5.5.

### Practical problems in model building and the authors' stated remedies (s. 5.4)

| Section | Problem | Authors' stated remedy | Caveat the authors add |
|---|---|---|---|
| 5.4.1 | Factors are not independent. Stepwise regression coefficients depend on the order of entry. Separately calibrated top-down and bottom-up sub-models can share drivers, so scores are double-counted. | Three "palliative actions": (a) select factors to be as independent as possible, (b) jointly estimate all driver sensitivities, (c) use the Grinold and Kahn form with full covariance between forecasts and returns (eq. 5.8). | Remedy (c) assumes you know the full covariance. |
| 5.4.2 | Sequential Bayesian updating assumes each new input is independent of all previous inputs. | Enter related items simultaneously as a joint probability distribution, with their correlation. | Estimating all correlations adds noise. If independence is a good enough approximation, keep the simpler model. |
| 5.4.3 | Views are relative, not absolute. There may be many of them, some inconsistent, some missing. | Mixed estimation (eq. 5.9-5.13). It finds a solution and a confidence, reconciles inconsistent inputs, and fills missing forecasts from the prior. | The posterior covariance is not the real asset covariance. The mean can be unstable to small input changes. Perfect confidence gives simultaneous linear equations, so expect ill-conditioning in some cases. |
| 5.4.3 | Factor views must be merged with asset and relative views. | Reuse eq. 5.12 with x as the asset return and r as the factor return. | None stated. |
| 5.4.3 | Scenario views. Individual scenarios are tedious to generate and may not be independent. | Stochastic scenarios: states with their own multivariate normals, sampled into a Monte Carlo set. | Check independence of scenarios. Generate many more scenarios than assets. |

Reconciliation rule for inconsistent views (s. 5.4.3): with equal confidence the effect is "the average of the two independently". If one has high confidence it dominates the low-confidence input.

### Threshold risk measures compared (s. 5.5)

| Measure | Definition in the text | Authors' stated weakness | Optimizable in their LP set-up |
|---|---|---|---|
| VaR | Confidence that portfolio return over a period is above a threshold | Ignores the distribution beyond the threshold. Sub-portfolio VaRs do not sum to portfolio VaR. Optimization is mixed integer and computationally expensive. | No. It is an integer function, a count of hyperplanes. |
| CVaR (mean excess loss) | Average expected loss conditional on the threshold being exceeded | Ignores upside potential. Two portfolios with equal CVaR can differ in upside. | Yes. The authors call it "the only linear measure" they can optimize this way. |
| Loss gain ratio | CVaR divided by the weighted probability of exceeding the threshold | Reflects risk per unit return. It is not a pure downside measure. | No. It is a ratio of upside and downside risk. |

Authors' reporting rule (s. 5.5): most investors would want both CVaR and the loss gain ratio. VaR "may well be the statistic to report" because it is widely quoted, even though the other two drive portfolio selection.

For small non-normality the authors mention mean absolute deviation or rank correlation. Both are symmetric, so they do not suit highly asymmetric distributions (s. 5.5).

## Worked Example
The chapter has no numerical example. It has two illustrations.

**1. The new managing director (s. 5.4.2).**
1. You hold a forecast return distribution for a company. It rests partly on the sector going into recession with poor sales prospects.
2. New information arrives. The company appoints a well-respected MD.
3. Question: is this independent of the prior?
4. If the MD is respected as "an excellent salesman rather than good at controlling costs", the information "is NOT independent". His value depends on whether sales growth or cost-cutting is the key skill in that environment.
5. Authors' rule: you can still add it. Enter the related items together as a joint distribution. That carries the correlation between the management change and the macro environment.

**2. CVaR as a linear programme (s. 5.5).**
1. Start from a set of Monte Carlo simulated return series from the mixture of normals.
2. Each draw gives a hyperplane in weight space. Portfolios that exceed the threshold return lie above it.
3. The problem is not in simplex standard form, because viable solutions lie on both sides of each hyperplane.
4. For each hyperplane add two dummy variables, d+ and d-. Constrain them to be the positive and negative distances above and below the hyperplane.
5. Replace the original constraints with these. Set the objective to the sum of distances below each hyperplane.
6. "Hence minimizing this minimizes CVaR."
7. Count hyperplanes above and below a point to get VaR. Evaluate upside as well as downside to get the loss gain ratio.

The only number in the chapter's examples: a rolling window of "say, 7 years of monthly data" takes "several years" to show the Internet factor (s. 5.2).

## Key Takeaways
1. Use the linear factor model as a local approximation. Recalculate exposures every period.
2. Put every forecast source into one form: regimes, each multivariate normal, each with a probability.
3. Check independence before you combine inputs. This applies to regression factors, Bayesian updates and scenarios alike.
4. Use Bayesian mixed estimation for relative and factor views, but do not trust its posterior covariance as a risk estimate.
5. Turn the mixture into a Monte Carlo set. Apply payoff functions for assets with asymmetric payoffs.
6. Optimize on CVaR by linear programming. The authors state that mean-CVaR "agrees with the classical model" when the forecast is normal (abstract, s. 5.1).
7. The authors seek a process design, not one model. Their criteria are flexibility, robustness to noise, simplicity, parsimony, intuitive reporting and theoretical rigour (s. 5.6).

## Source Defects
- **Lost in extraction, recovered from PDF**: every Greek symbol and the summation signs in eq. 5.1, 5.2, 5.5, 5.6, 5.7, 5.9, 5.13 and the updated mean and covariance. The conditional bar in eq. 5.8 and in Bayes' equation. The proportionality sign in eq. 5.12 and 5.13. Recovered from book pp. 104, 107, 109, 110, 111.
- **PDF page offset**: PDF page = book page + 7 in this file, checked on the running headers of book pp. 104-114.
- **Inconsistencies in the source itself, recorded and not corrected**:
  - Eq. 5.1 prints Y_it. The text uses y_it. The sum has no index.
  - Eq. 5.5 prints "V = H(0,0) = H2(0,0)U + Rem_t".
  - Eq. 5.6 prints subscript i on the left and l on the right.
  - Eq. 5.9 prints pdf_1(r) with x inside the exponent.
  - The sentence before eq. 5.13 cites "equations (5.1) and (5.4)" as the two normals. The two normals shown are eq. 5.9 and eq. 5.12.
  - The updated mean is named β, which also names the exposure matrix.
  - The third simplex constraint prints "a_i1 x_1 + ... a_i2 x_2 + a_in x_n = b_i", with the ellipsis misplaced. The text says "i constraints" and also uses i as the index.
  - The numbered list in s. 5.5 says CVaR "multiplies that downside probability by the average amount by which the threshold is exceeded". The later paragraph defines it as a conditional average loss. The two wordings differ.
  - The text states CVaR "is always greater than VaR". Recorded as stated.
  - The reference list gives "Satchell, S., Wright, S. and Hwang, S. (2003)". The text cites it as "Satchell and Wright, 2003".
- **Not present in the chapter**: no proof or numerical test of the claim that mean-CVaR agrees with mean-variance under normality. No formulas for VaR, CVaR or the loss gain ratio. No figures and no numbered tables.

## Connects To
- **ch02-black-litterman-step-by-step** and **ch03-black-litterman-demystified**: s. 5.4.3 uses the same prior-times-likelihood update. The authors point to Satchell and Scowcroft (2000), "reproduced in this book", for the algebra.
- **ch04-portfolios-from-ordering-information**: the chapter builds on the authors' rank and scorecard work, which uses ordering information in place of forecast alphas.
- **ch08-robust-optimization**: ch08 also uses a mixture of normals over priors and a multiple-scenario view of utility. It cites Satchell and Wright (2005) for ranked forecasts.
