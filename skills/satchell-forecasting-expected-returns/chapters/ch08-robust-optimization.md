# Chapter 8: Robust optimization for utilizing forecasted returns in institutional investment
**Authors**: Christos Koutsoyannis and Stephen Satchell | **Book pages**: 177-190 (text ends on p. 187, references run pp. 188-189) | **Type**: METHOD (a literature survey plus a problem formulation. The "case study" is a set-up with no data and no results)

## Core Idea
Robust optimization tries to produce "more stable, relevant portfolios that are less prone to data and other errors" (s. 8.1). The authors see two broad approaches. Practitioners change the mathematical problem, mainly with quadratic inequality constraints. Academics use maximin expected utility, which rests on ambiguity aversion. The chapter surveys both. It then shows one practitioner formulation that constrains the first two moments of historical forecast errors.

## Frameworks Introduced
- **Risk versus uncertainty** (s. 8.1). Risk is when "you can capture model variation by assigning priors and probabilities". Uncertainty "is when you cannot assign probabilities".
- **Parameter uncertainty versus model uncertainty** (s. 8.1). The first comes from imperfect data. The second is the possibility of incorrect structure in the model.
- **The two broad approaches** (s. 8.1):
  1. A mathematical formulation. It uses more complex objective functions or constraints. Interior point solutions to second-order cone programming made it feasible. "This is the approach used by some practitioners."
  2. A maximin approach to expected utility, "much favoured by academics", based on ambiguity aversion.
- **Multiple scenarios versus multiple priors** (s. 8.1). The authors call multiple scenarios without probabilities "neo-Bayesianism". They call multiple priors with prior probabilities "classical Bayesianism".
- **Taxonomy of robustness notions** (s. 8.2). The topics in the authors' order: robust statistics, ranked forecasts, Bayesian adjustments including shrinkage and Black-Litterman, risk aversion corrections, constraints, resampling, utility bounds, the mathematics of robust optimization, and financial applications. See the reference table below.
- **Forecast-error (FE) constrained optimization** (s. 8.3, eq. 8.4-8.7). Maximize expected active return subject to three quadratic constraints: tracking error, mean FE and FE variance.
- **"Smart turnover" constraints** (s. 8.3, eq. 8.8-8.9). The same FE constraints written relative to the initial portfolio.
- **Maximin expected utility** (s. 8.4, Figure 8.1). Compute expected utility under each scenario. Take the minimum across scenarios at each weight. Choose the weight that maximizes that minimum.
- **Multiple experts on implied factor returns** (s. 8.4, eq. 8.10-8.13). Experts agree on risk and differ on alpha. A Bayesian assigns each expert a probability. An ambiguity-averse investor takes the minimum utility across experts.

## Formulas
All Greek symbols below were lost in the text extraction. All are recovered from the PDF pages cited.

**Standard mean-variance problem** (eq. 8.1, recovered from PDF, book p. 182):

    max U(w, λ) = α^T (w - b) - (λ/2) (w - b)^T C (w - b)

- w: vector of asset weights in the portfolio.
- λ: degree of risk aversion.
- α: vector of expected returns.
- b: vector of asset weights in the benchmark.
- C: covariance matrix of asset returns.

**Risk as a constraint** (eq. 8.2-8.3, recovered from PDF, book p. 182):

    max U(w, λ) = a^T (w - b)                           (8.2)
    subject to
    σ_P^2 = (w - b)^T C (w - b) < TE                    (8.3)

- The page prints a Latin "a" in eq. 8.2 and 8.4, where eq. 8.1 prints α. Recorded as printed.
- TE: the tracking error limit. The page compares a variance with TE. Recorded as printed.

**Robust problem with forecast-error constraints** (eq. 8.4-8.7, recovered from PDF, book p. 183):

    max U(w, λ) = a^T (w - b)                           (8.4)
    subject to
    (w - b)^T C (w - b) < TE                            (8.5)
    (w - b)^T μ_FE (w - b) < M^2                        (8.6)
    (w - b)^T C_FE (w - b) < S^2                        (8.7)

- μ_FE: "a diagonal matrix of squared mean forecast errors".
- M: "the maximum tolerable mean forecast error".
- C_FE: "the covariance matrix of forecast errors".
- S: "the maximum tolerable forecast error variance". The constraint bounds by S^2. Recorded as printed.

**Smart turnover form** (eq. 8.8-8.9, recovered from PDF, book pp. 183-184):

    (w - w_i)^T μ_FE (w - w_i) < M^2                    (8.8)
    (w - w_i)^T C_FE (w - w_i) < S^2                    (8.9)

- w_i: initial portfolio weights.

**k-factor model for returns** (eq. 8.10-8.11, recovered from PDF, book p. 186):

    y_t = α_t i + β_t V_t + u_t                         (8.10)
    E(u_t u_t') = D
    y_t = β_t V_t + u_t                                 (8.11)

- y_t, u_t: N x 1 vectors. i: an N x 1 vector of ones.
- β_t: an N x k matrix of known exposures.
- V_t: the k x 1 vector of unknown implied factor returns.
- D: a diagonal N x N covariance matrix.
- α_t: an unknown scalar. It is the same for all stocks, so the authors drop it for stock selection.

**Weighted least squares estimator** (unnumbered, recovered from PDF, book p. 186):

    V̂_t = (β_t' D̂^-1 β_t)^-1 (β_t' D̂^-1 y_t)
    V̂_t ~ (V_t^p, (β_t' D̂^-1 β_t)^-1)

- D̂^-1: estimated from residuals of previous periods. The authors recommend rolling windows.
- V_t^p: the "true" value of V_t.

**Experts' priors and the mixture** (unnumbered, recovered from PDF, book p. 186):

    V_t^j ~ N(V_0^j, Ω^j)
    pdf(V_t^p) = Σ π_j N(V_0^j, Ω^j)
    pdf(V̂_t, V_t^p) = pdf(V̂_t | V_t^p) pdf(V_t^p) = Σ π_j N(μ_j, θ_j)

- j: the expert. V_0^j, Ω^j: that expert's prior mean and covariance.
- π_j: probability assigned to expert j, "based on past performance or pedigree or introspection".
- θ_j: the posterior covariance for expert j. The chapter gives no expression for it.

**Posterior mean for expert j** (eq. 8.12, recovered from PDF, book p. 186, as printed):

    μ_j = ((β_t' D̂^-1 β_t) + Ω_j^-1)^-1 [ (β_t' D̂^-1 β_t)^-1 V_t + Ω_j^-1 V_0^j ]

- The page prints the inverse (β_t' D̂^-1 β_t)^-1 inside the square bracket, and V_t without a hat. Recorded as printed.

**Mixture moments** (unnumbered, recovered from PDF, book p. 187, as printed):

    mean       = Σ π_j θ_j
    covariance = Σ π_j θ_j + Σ π_j μ_j μ_j' - (Σ π_j μ_j)(Σ π_j μ_j)'

- The page prints θ_j in the mean. The covariance line uses μ_j for the means. Recorded as printed.

**Ambiguity-averse utility and optimum** (eq. 8.13 and text, recovered from PDF, book p. 187, as printed):

    expected stock return under expert j:  β_t μ_j
    covariance (shared by all experts):    β_t Ψ β_t' + D
    μ_j(w) = w' β_t μ_j - λ w' (β_t Ψ β_t' + D) w
    U(w)   = min_j ( U_j(w) )
    w*     = (β_t Ψ β_t' + D)^-1 ( Σ λ_j β_r μ_j )      (8.13)

- Ψ: an estimate of the factor covariance matrix.
- λ in the utility line: not redefined here. It is the risk aversion symbol of eq. 8.1.
- λ_j in eq. 8.13: Lagrange multipliers. They determine "which of the experts' opinions is the most pessimistic" for the given weights.
- The utility is printed as μ_j(w) and then referred to as U_j(w). Eq. 8.13 prints β_r, not β_t. Both recorded as printed.
- The authors say the form is "like Theorem 1 in Lutgens and Schotman (2004)".

## Key Concepts
- **Ambiguity aversion** (s. 8.1, s. 8.4). Aversion to situations where probabilities cannot be assigned. The authors tie it to Knight (1921) and Ellsberg (1961).
- **Error-maximization** (footnote 1). Mean-variance optimizers can place "excessive weights" on "unrealistically high estimates". The authors credit Jobson and Korkie (1980).
- **Forecast error (FE)** (s. 8.3). "The difference between the ex ante expectation of return and the subsequent realized return". It is "easily measured and is independent of the forecasting methodology".
- **Shrinkage** (s. 8.2). Sample information is shrunk towards model-based ex ante information to deal with estimation uncertainty.
- **Second-order cone programming (SOCP)** (s. 8.2). It "deals with linear objective functions and linear and SOC constraints".
- **Interior point method** (s. 8.2). Nesterov and Nemirovsky (1994). It lets an investor solve problems "with any number of quadratic constraints" efficiently.
- **Centroid** (s. 8.2). The "n-dimensional geometric centre-of-mass of the consistent set" in the Almgren and Chriss approach.
- **Maximin expected utility** (s. 8.4). Gilboa and Schmeidler (1989). Uncertainty is handled by multiple priors and a maximin rule.
- **Pseudo risk aversion corrections** (s. 8.2). Cavadini et al. (2001). They penalize allocations exposed to both estimation risk and model risk.

## Mental Models
- Split forecast inputs into "informative" and "noisy" data. Limit the noisy and let the informative add value (s. 8.3).
- The main cause of portfolio instability is instability in return expectations. Constrain that directly (s. 8.3).
- Maximin gives "a theoretical structure to the well-known practice of scenario-analysis" (s. 8.4).
- The more ambiguity-averse the investor, the more priors the investor entertains, and "generically" the lower the resulting expected utility (s. 8.4).
- The difference from conventional Bayesian analysis: "we do not assign probabilities to the scenarios" (s. 8.4).
- Institutional examples of ambiguity (s. 8.4): a pension trustee deciding on a hedge fund, and operational risk. Regulated, exchange-traded assets carry "much less".
- It is non-convexity, not non-linearity, that slows a solution down (s. 8.2, attributed to Rockafellar 1993).
- A wrong constraint can still help. A non-negativity constraint is equivalent to shrinking extreme elements of the covariance matrix (s. 8.2, attributed to Jagannathan and Ma 2003).
- FE constraints are "independent of the source of the bias". The authors name accounting-standard differences across regions and sector or style biases in factors (s. 8.3).

## Anti-patterns
- **Guessing λ and iterating to a tracking error** (s. 8.3). λ is "difficult to evaluate with confidence". Feasibility may be unknown, "leading to the failure of this iterative procedure".
- **Treating either mean-variance form as robust** (s. 8.3). "Both equations (8.1) and (8.2) suffer from robustness issues." Output weights can be "disproportionately unstable".
- **Resampling as the answer** (s. 8.2). The authors doubt that Michaud's simple average "captures the distributional properties of the underlying uncertainty" or fits maximum expected utility. They cite Harvey et al. (2004) on a Jensen's inequality problem and note the "computational overload".
- **General non-linear optimization on large problems** (s. 8.2). Time rises exponentially with the number of assets. It can return local optima.
- **Plain quadratic programming for real-life constraints** (s. 8.2). It "can only handle linear constraints".
- **Formulations with no economic meaning** (s. 8.2). On Costa and Paiva's linear matrix inequalities: "at least none is provided by the authors".
- **Equating maximin with the worst-case scenario** (s. 8.4). The maximin portfolio "is not the same as the worst-case scenario".
- **Ambiguity-aversion methods on large portfolios** (s. 8.5). The approach "seems hard to implement for large portfolios with high levels of ambiguity". The multipliers in eq. 8.13 "may be very difficult to compute numerically".

## Reference Tables
The chapter prints no numbered tables. The table below is compiled from the text of s. 8.2.

### Taxonomy of robustness notions (s. 8.2)

| Notion | What it does, per the text | Sources the authors cite | Authors' comment |
|---|---|---|---|
| Robust statistics | Estimators that resist data errors and contamination, for example a one-off extreme such as October 1987 | Huber (1964), Hampel (1974), Least Trimmed Squares (Rousseeuw 1985), Iteratively Reweighted Least-Squares (Holland and Welsch 1977), GMM (Ronchetti and Trojani 2001), M-estimators (Hampel et al. 1986), S-estimators (Rousseeuw and Yohai 1984), τ-estimators (Yohai and Zamar 1988), Victoria-Feser (2000), Perret-Gentil and Victoria-Feser (2003) | Robust estimates give more stable portfolios. They mitigate estimation error and "more importantly model uncertainty". |
| Ranked forecasts | Use rankings instead of point estimates. Combine with conventional risk by adjusting risk aversion or mapping ranks back to returns | Satchell et al. (2003), Satchell and Wright (2005) | "Robustness through incomplete information". "This is indeed what many funds do." |
| Cones and the centroid | Returns consistent with an ordering lie in a cone. Portfolio A beats B if A wins over more of the cone under measure P. The optimum reduces to the centroid | Almgren and Chriss (2004, 2006) | It criticizes the ranked approach above. It resembles performance systems that compare a manager with random constrained portfolios. |
| Bayesian shrinkage of means | Biased-shrinkage estimators applied to the mean | James and Stein (1961), Jobson et al. (1979), Jorion (1986) | The same idea applies to other optimizer inputs. |
| Covariance shrinkage | Shrink the sample covariance towards a single-index matrix (2003) or a constant correlation matrix (2004). Intensity minimizes a loss based on the Frobenius norm | Ledoit and Wolf (2003, 2004) | Controls estimation error. |
| Black-Litterman | Start from equilibrium returns. Tilt towards investor views by degree of confidence | Black and Litterman (1990, 1992), Lee (2000), Kandel and Stambaugh (1996), Pastor and Stambaugh (2000), Barberis (2000), Pastor (2000) | Lee says it "largely mitigates" error-maximization. It extends to an equities factor model. |
| Risk aversion corrections | Pseudo risk aversion corrections for estimation risk and model risk together | Cavadini et al. (2001) | "Substantial reductions in their loss function". Better than treating either risk alone. |
| Constraints | Portfolio constraints control estimation error | Jagannathan and Ma (2003) | The fall in sampling error is "often higher" than the rise in specification error. |
| Resampling | Simulate parameters, optimize repeatedly, average the portfolios | Michaud (1989, 1998), Harvey et al. (2004) | See Anti-patterns. |
| Utility bounds | Lower bounds on expected utility through an exponential (Markov) inequality on the tail of final wealth | Anderson et al. (2000), Chu (2004) | A bound valid for all scenarios encompasses the later maximin analysis. |
| Mathematics of robust optimization | Interior point methods for convex problems. SOCP. Maximin built into the method | Rockafellar (1993), Nesterov and Nemirovsky (1994), Ben-Tal and Nemirovski (1998), Lobo et al. (1997), Lobo (2000), Cornuejols and Tütüncü (2006), Gilboa and Schmeidler (1989) | Allows extra quadratic constraints on the first and second moments of historic forecast error. |
| Financial applications | "Uncertainty structures" shown to be a conic problem. Parameter uncertainty reduced to linear matrix inequalities | Goldfarb and Iyengar (2003), Costa and Paiva (2002) | The second lacks economic meaning, per the authors. |

## Worked Example
The chapter has three examples. Only the urn example carries stated numbers.

**1. Case study: forecast errors and quadratic constraints (s. 8.3).** The case study is a formulation. It reports no data, no parameter values and no results.
1. Start from the mean-variance problem with a risk-aversion term (eq. 8.1).
2. Move risk into a constraint (eq. 8.2-8.3). The user then knows "prior to execution whether or not the problem is feasible".
3. Measure FE for each asset: ex ante expected return minus subsequent realized return.
4. Add a mean FE constraint (eq. 8.6) and a FE variance constraint (eq. 8.7).
5. Both are quadratic. The mean FE constraint is quadratic by choice, so "as the forecast error increases in magnitude, we penalize stocks increasingly aggressively".
6. Solve with interior point methods. The authors point to Lobo et al. (1997) for an implementation.
7. Optionally write the FE constraints relative to initial weights (eq. 8.8-8.9). The optimizer then deviates from the initial position only "where there is stable, historically accurate alpha".
8. Claimed effects, stated as expectations and not tested in the chapter: less turnover due to noise, more stable portfolios, less exposure to data errors or misspecification. The authors "feel that it may offer a better approach" than re-sampling and bootstrapping.

**2. Ellsberg's urns (s. 8.4, quoted from Anderson et al. 2000, p. 7).**
1. Urn A holds fifty red and fifty black balls. Urn B's mix is unknown.
2. The player guesses the colour drawn from one urn only and wins a payoff if right.
3. The Bayesian-Savage model predicts indifference or a preference for Urn B. Ellsberg argued a preference for Urn A is reasonable.
4. The maximin reading (Gilboa and Schmeidler 1989): the worst case for Urn B is betting on a colour with zero balls. That pays zero.
5. Zero is worse than "the $50 you would expect to get from Urn A if the prize is $100".

**3. Two scenarios, one risky asset (s. 8.4, Figure 8.1, recovered from PDF, book p. 185).**
1. The figure plots expected utility E(U(w)) against the weight w of the risky asset. The x-axis runs 0 to 1. The y-axis runs -0.01 to 0.01.
2. There are two utility curves, one per scenario. Each has its own optimum, labelled AA and BB.
3. CC is the maximum of the lower envelope of the two curves. The authors prefer CC.
4. The text says the worst-case scenario "would be BB, since BB has lower expected utility than AA".
5. The text says CC holds more of the risky asset "than AA but less than BB".
6. Approximate readings from the chart image only, not stated in the text: AA near w = 0.35 to 0.4, CC near w = 0.5, BB near w = 0.75. One curve crosses zero utility near w = 0.75. Treat these as rough.

## Key Takeaways
1. Robustness covers both parameter uncertainty and model uncertainty.
2. Practitioner interest centres on mean-variance with quadratic inequality constraints. Academic interest centres on ambiguity aversion (s. 8.5).
3. Use a tracking error constraint in place of a risk-aversion term to know feasibility in advance.
4. Constrain the mean and variance of historical forecast errors. This discounts "historically unstable or erroneous alphas".
5. Written against initial weights, the same constraints act as smart turnover limits.
6. With several experts, the Bayesian route weights them and gives a mixture of normals. A single prior "recapture[s] the Black-Litterman model". The ambiguity-averse route takes the minimum utility across experts.
7. The authors call their own update "extreme". It keeps all priors and does not use sample information to learn their probabilities. There is "no agreed way of updating non-unique priors" (s. 8.4).

## Source Defects
- **Lost in extraction, recovered from PDF**: all Greek symbols and summation signs in eq. 8.1-8.13 and the unnumbered formulas, the conditional bar in the joint density, the τ in "τ-estimators", and Figure 8.1. Recovered from book pp. 178 and 182-187.
- **PDF page offset**: PDF page = book page + 7 in this file, checked on the running headers of book pp. 178-189.
- **Page range**: the brief gives pp. 177-190. The chapter's last printed page is 189.
- **The "numbers" of the case study**: s. 8.3 contains none. Nothing was omitted.
- **Figure 8.1**: the curve positions listed above are read by eye from the chart. The text gives no coordinates.
- **Inconsistencies in the source itself, recorded and not corrected**:
  - Eq. 8.2 and 8.4 print "a" where eq. 8.1 prints α.
  - Eq. 8.3 and 8.5 bound a variance by TE.
  - S is defined as a maximum variance, and eq. 8.7 bounds by S^2.
  - Eq. 8.12 prints (β_t' D̂^-1 β_t)^-1 V_t in the bracket, with no hat on V_t.
  - The mixture mean is printed as Σ π_j θ_j. The covariance formula treats μ_j as the means.
  - θ_j is never defined.
  - The utility is printed μ_j(w) and then called U_j(w). Eq. 8.13 prints β_r.
  - λ is both the risk aversion and, with a subscript, a Lagrange multiplier.
  - The prior covariance is written Ω^j in the densities and Ω_j in eq. 8.12.
  - Spellings vary: "Victora-Feser" and "Victoria-Feser", "Shmeidler" and "Schmeidler".
  - The text says Urn B "can never be worse" than Urn A's 50 per cent. Two paragraphs later it gives Urn B a worst-case payout of zero. Recorded as stated.

## Connects To
- **ch04-portfolios-from-ordering-information**: s. 8.2 summarizes Almgren and Chriss's cone and centroid method and says it is "republished in this book (see Chapter 4)".
- **ch03-black-litterman-demystified**: cited for the mean and covariance of a mixture of normals. A single prior recovers Black-Litterman.
- **ch02-black-litterman-step-by-step**: the authors note "a number of chapters in this book" discuss Black and Litterman's model.
- **ch05-choices-in-forecast-construction**: the same mixture-of-normals form over regimes or priors. Satchell and Wright (2005) is cited here for ranked forecasts.
