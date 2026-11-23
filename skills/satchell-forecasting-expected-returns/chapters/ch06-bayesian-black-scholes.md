# Chapter 6: Bayesian analysis of the Black-Scholes option price

**Authors**: Theo Darsinos and Stephen Satchell | **Book pages**: 117-149 | **Type**: METHOD (a derivation of option-price densities plus a numerical illustration on chosen FTSE 100 values, with no out-of-sample test)

## Core Idea
The Black-Scholes (BS) call price is a random variable. Before the sample, it depends on two unknowns: the asset price P_t and the volatility sigma. After the sample, P_t is data and only sigma stays unknown. The authors put priors on drift and variance, add the likelihood of the sample variance, and derive the prior and posterior densities of the call price itself (s. 6.2). They extend Karolyi (1993), who treated only volatility as random. The numerical result: conditioning on the asset price removes most of the dispersion (s. 6.4).

## Frameworks Introduced
- **Four distributional assumptions** (s. 6.2.1):
  1. The price is log-normal given drift mu and volatility sigma (Assumption 1).
  2. The drift mu has a normal prior with mean m and variance sigma^2/t (Assumption 2). m is a hyperparameter.
  3. The likelihood of sigma^2 comes from the chi-square law of (t-1)s^2/sigma^2 (Assumption 3).
  4. The variance sigma^2 has an inverted-gamma-1 prior with hyperparameters lambda and theta (Assumption 4).
- **Prior density of the option price** (s. 6.2.2, eq. 6.6-6.8). Steps:
  1. Build the joint prior pdf(P_t, sigma) by integrating mu out (Proposition 1).
  2. Change variables from (P_t, sigma) to (c, sigma), using the implied price Psi(c, sigma).
  3. Integrate sigma out numerically. No closed form exists.
  - Remark 4 gives a second route: change to (c, P_t) with the implied volatility Theta(c, P_t), then integrate P_t out. Both routes give the same numbers.
- **Posterior density of the option price** (s. 6.2.3, eq. 6.9-6.14). Steps:
  1. Bayes rule: pdf(P_t, sigma | s) = pdf(P_t, sigma, s) / pdf(s) (eq. 6.9, Propositions 2 and 3).
  2. Change variables from sigma to c through the implied volatility Theta(c, P_t). The Jacobian is 1/vega (eq. 6.10-6.12).
  3. Divide by pdf(P_t | s) (eq. 6.13, Proposition 4). The result is analytic and contains a modified Bessel function (eq. 6.14).
- **Loss-function reading of the posterior** (s. 6.2.3). Quadratic loss selects the posterior mean. Absolute-error loss selects the median. Zero-one loss selects the mode.
- **Risk-neutral posterior** (Corollary 2). Set m = r and drop Assumption 2. The authors stop there: the prior and predictive densities are "not invariant in m".
- **Grid evaluation** (s. 6.3, eq. 6.15-6.21). Calibrate lambda and theta from prior beliefs on the mean and variance of volatility. Then evaluate the densities on a grid.

## Formulas
All items below are recovered from the PDF pages. The text extraction lost every Greek letter.

Price process and BS price (recovered from PDF, book pp. 119-122):

    dP_t = mu P_t dt + sigma P_t dW_t                                   (6.1)
    P_t  = P_0 exp[(mu - sigma^2/2) t + sigma (W_t - W_0)]              (6.2)
    x_t  = log(P_t / P_0)                                               (6.3)
    s^2  = sum_{i=1..t} (x_i - xbar)^2 / (t - 1)                        (6.4)
    c = C(P_t, K, sigma, tau, r)                                        (6.5)
      = P_t PHI( [log(P_t/K) + (r + sigma^2/2) tau] / (sigma sqrt(tau)) )
        - K exp(-r tau) PHI( [log(P_t/K) + (r - sigma^2/2) tau] / (sigma sqrt(tau)) )

    mu = expected rate of return, sigma = volatility, W = Brownian motion,
    t = sample size (time from 0 to t), K = strike, tau = T - t = time to expiry,
    r = risk-free rate, PHI = standard normal cdf, phi = standard normal pdf.

Assumptions 2 to 4 (recovered from PDF, book pp. 120-121):

    pdf(mu | sigma, m, t) = sqrt(t) / (sqrt(2 pi) sigma) * exp( - t (mu - m)^2 / (2 sigma^2) )
    pdf(s | sigma, v)     = 2 (v/2)^(v/2) / GAMMA(v/2) * s^(v-1) / sigma^v * exp( - v s^2 / (2 sigma^2) ),  v = t - 1
    pdf(sigma^2 | lambda, theta) = lambda^theta / GAMMA(theta) * (sigma^2)^-(theta+1) * exp( - lambda / sigma^2 )
    pdf(sigma | lambda, theta)   = 2 sigma * [the line above]

Proposition 1, joint prior of price and volatility (recovered from PDF, book p. 123):

    pdf(P_t, sigma) = 1 / (sqrt(pi t) P_t) * lambda^theta / GAMMA(theta) * sigma^-(2(theta+1)) * exp( - lambda / sigma^2 )
                      * exp( - [ ln(P_t/P_0) - (m - sigma^2/2) t ]^2 / (4 sigma^2 t) )

Prior density of the option price (recovered from PDF, book pp. 124-125):

    1/J = PHI(d1),  d1 = [ ln(P_t / (K e^(-r tau))) + sigma^2 tau / 2 ] / (sigma sqrt(tau))        (6.6)
    pdf(c, sigma) = pdf( Psi(c, sigma), sigma ) |J|                                                (6.7)
    pdf(c) = integral_0^inf pdf(c, sigma) d sigma                                                  (6.8)

    Psi(c, sigma) = the BS formula inverted in P_t ("implied price"). d1* is d1 with P_t = Psi(c, sigma).
    vega = phi(d1) P_t sqrt(tau).

Posterior density (recovered from PDF, book pp. 126-129):

    pdf(P_t, sigma | s) = pdf(P_t, sigma) pdf(s | sigma) / pdf(s)                                  (6.9)
    1/J = vega                                                                                     (6.10)
    pdf(P_t, c, s) = pdf(P_t, Theta(c, P_t), s) |J|                                                (6.11)
    pdf(P_t, c | s) = pdf(P_t, c, s) / pdf(s)                                                      (6.12)
    pdf(c | P_t, s) = pdf(P_t, c | s) / pdf(P_t | s)                                               (6.13)

    Proposition 3:  pdf(s) = 2 / B(v/2, theta) * lambda^theta * (v/2)^(v/2) * s^(v-1) / (lambda + v s^2/2)^(v/2 + theta)

    Full posterior (6.14), with A = 2 (2 lambda + v s^2) t + ( ln(P_t/P_0) - m t )^2 and Th = Theta(c, P_t):

    pdf(c | P_t, s) = |J*| (A/64)^((2 theta + t)/4)
                      / [ K_{theta + t/2}( sqrt(A)/4 ) * Th^(2 theta + v + 2) * (t/16)^(theta + t/2) ]
                      * exp( - (2 lambda + v s^2) / (2 Th^2) + ( ln(P_t/P_0) - m t ) / 4 )
                      * exp( - [ ln(P_t/P_0) - (m - Th^2/2) t ]^2 / (4 Th^2 t) )

    J* = 1 / ( phi( [ ln(P_t / (K e^(-r tau))) + Th^2 tau / 2 ] / (Th sqrt(tau)) ) P_t sqrt(tau) )
    Theta(c, P_t) = the BS formula inverted in sigma (implied volatility).
    K_a(.) = modified Bessel function of the second kind of order a. B(.,.) = beta function.

At-the-money simplification, P_t = K exp(-r tau) (Corollary 1, recovered from PDF, book p. 129):

    Theta(c, P_t) = (2 / sqrt(tau)) PHI^-1( (1/2)(c/P_t + 1) )

Calibration of the prior and the grid (recovered from PDF, book pp. 132-133):

    E(sigma)   = lambda^(1/2) GAMMA(theta - 1/2) / GAMMA(theta)                                    (6.15)
    E(sigma^2) = lambda / (theta - 1)                                                              (6.16)
    Var(sigma) = E(sigma^2) - [E(sigma)]^2                                                         (6.17)
    Psi(c, sigma) = n x u matrix of implied prices Psi(c_i, sigma_j)                               (6.18)
    SIGMA = n x u matrix whose every row is (sigma_1, ..., sigma_u)                                (6.19)
    pdf(c, sigma) = n x u matrix of pdf(c_i, sigma_j), built with elementwise products             (6.20)
    pdf(c) ~ sum_{j=1..u} pdf(c_i, sigma_j) DELTA_j                                                (6.21)

Not recovered: the risk-neutral posterior of Corollary 2 (book p. 130) and the densities pdf(c | s) and pdf(c | P_t) in Appendix A.4. The exponents (t/16)^(theta + t/2) in eq. 6.14 are small print on the page. Verify them before use.

## Key Concepts
- **Unconditional (prior)**: conditional only on time-0 information, the prior parameters lambda, theta, m, and the known sample size t (s. 6.2.2).
- **c = C(P_t, sigma) versus c = C(sigma)**: the first treats price and volatility as random. The second, used by Karolyi (1993), fixes the price (Remarks 2, 3, 7).
- **Implied price Psi(c, sigma)**: the underlying price that reproduces c at volatility sigma. It needs Newton-Raphson, except at the money (footnote 12).
- **Implied volatility Theta(c, P_t)**: the volatility that reproduces c at price P_t. It also needs Newton-Raphson, except at the money (footnote 13).
- **Inverted-gamma-1 prior**: the prior family for sigma^2, chosen because (t-1)s^2/sigma^2 is chi-square (s. 6.2.1).
- **Empirical Bayes prior**: a prior built from the data, or from prior sample data, or from the long-run average of volatility (s. 6.3).
- **Estimation risk**: the dispersion that the volatility estimate leaves in the option price. A larger sample reduces it (s. 6.4).
- **Support of the posterior**: the no-arbitrage bounds of the call. For K = 2025 the printed support is 187.066 < c < 2206 (s. 6.4).

## Mental Models
- The BS price is unusual as a Bayesian object. It depends on data (price) and on a parameter (volatility) (s. 6.1).
- Read the option price through four information states: pdf(c), pdf(c | s), pdf(c | P_t), pdf(c | P_t, s). Dispersion falls along that chain (s. 6.2.3).
- The sample size t works in opposite directions. A longer horizon t widens the prior. A larger sample t tightens the posterior (s. 6.4).
- A posterior density is a platform, not a point. Combine it with a loss function, or read quantiles and value-at-risk from it (abstract, s. 6.2.3).
- The posterior still depends on m. The true mu is integrated out, but m stays because prices are random before sampling (Remark 6).

## Anti-patterns
- **Treating volatility as known**: using log-normal price quantiles with sigma = s understates the range. The authors compare (7.38, 630.54) with (0.1, 786.9) (s. 6.4, Table 6.1).
- **Fixing the underlying price when forecasting**: the authors say existing forecasting theories vary only volatility (s. 6.5).
- **Assuming a normal option-price distribution for VaR**: a long call has a thinner left tail than the normal, so the computed VaR is too high. For a short call it is too low (s. 6.5).
- **Using a very large sample to estimate s**: the authors warn about non-stationarity (s. 6.4).
- **Deriving a risk-neutral prior or predictive density**: the authors say it "does not make sense" in this problem (Corollary 2).

## Reference Tables

### Table 6.1: 2.5% and 97.5% quantiles of the prior pdf(c) and of pdf(c | s), K = 2025
| t | pdf(c) 2.5% | pdf(c) 97.5% | pdf(c) mean | pdf(c\|s) 2.5% | pdf(c\|s) 97.5% | pdf(c\|s) mean |
|---|---|---|---|---|---|---|
| 30 | 0.1 | 828.9 | 262.9 | 0.1 | 786.9 | 234.1 |
| 25 | 0.4 | 751.7 | 252.2 | 0.1 | 712.0 | 227.6 |
| 20 | 1.7 | 679.1 | 240.4 | 0.8 | 646.2 | 220.3 |
| 15 | 5.2 | 606.5 | 227.6 | 3.6 | 583.0 | 212.4 |
| 10 | 14.9 | 523.4 | 214.1 | 11.5 | 509.1 | 204.1 |
| 5 | 39.8 | 416.2 | 200.2 | 37.2 | 410.4 | 195.6 |

Bottom panel of Table 6.1. Log-normal price with P_0 = 2200, t = 30, mu = 0.0006, sigma = 0.016: quantiles 1879.2 and 2649.5, mean 2240, SD 196.7, skewness 0.264, excess kurtosis 0.124. BS prices at those two quantiles: 7.38 and 630.54.

### Table 6.2: quantiles of the posterior pdf(c | P_t, s), K = 2025, P_t = 2206
| t | 2.5% | 97.5% | Mean |
|---|---|---|---|
| 30 | 188.9 | 195.2 | 189.8 |
| 20 | 188.7 | 196.4 | 189.8 |
| 10 | 188.5 | 196.9 | 190.1 |
| 5 | 188.3 | 197.2 | 190.4 |

### Tables 6.3 to 6.5: posterior versus price-only conditioning, t = 30, P_t = 2206
| Case | Density | 2.5% | 97.5% | Mean | SD | Skewness | Excess kurtosis |
|---|---|---|---|---|---|---|---|
| In the money, K = 2025 (Table 6.3) | pdf(c\|P_t, s) | 188.9 | 195.2 | 189.8 | 2.3 | 1.81 | 1.12 |
| | pdf(c\|P_t) | 188.3 | 197.2 | 191.2 | 2.3 | 1.52 | 3.00 |
| Near the money, K = 2225 (Table 6.4) | pdf(c\|P_t, s) | 39.0 | 59.1 | 47.6 | 4.85 | 0.70 | 0.57 |
| | pdf(c\|P_t) | 35.8 | 61.6 | 47.3 | 6.60 | 0.62 | 0.64 |
| At the money, K = 2212.63 (Table 6.4) | pdf(c\|P_t, s) | 44.7 | 64.9 | 53.3 | 4.86 | 0.74 | 0.61 |
| | pdf(c\|P_t) | 41.4 | 73.9 | 53.1 | 6.62 | 0.64 | 0.78 |
| Out of the money, K = 2425 (Table 6.5) | pdf(c\|P_t, s) | 1.7 | 8.9 | 4.27 | 1.73 | 1.15 | 2.14 |
| | pdf(c\|P_t) | 1.1 | 10.1 | 4.22 | 2.30 | 1.45 | 3.24 |

## Worked Example
The chapter's own illustration (s. 6.4). Time is in trading days, with 252 days per year.
1. **Prior beliefs from 30 prior days of FTSE 100 data.** Expected return 15% per annum. Volatility 25% per annum. Standard error of the volatility estimate about 0.25/sqrt(2 x 30) = 3.2% per annum.
2. **Daily format.** E(mu) = m = 0.0006. E(sigma) = 0.0158. Std. Dev.(sigma) = 0.002. Var(sigma) is printed as 4^-06. E(sigma^2) is printed as 2.5364^-04.
3. **Solve for the prior parameters.** lambda = 0.004 and theta = 16.72. Initial index value P_0 = 2200.
4. **Sample.** At t = 30 the index is P_t = 2206. Daily sample standard deviation s = 0.016. v = t - 1 = 29. The values follow Ncube and Satchell (1997).
5. **Options.** European calls with K = 2025, 2225 and 2425. tau = 15 trading days. r = 0.0002 daily.
6. **Result before the price is known.** The 95% range of the K = 2025 call is (0.1, 828.9) under the prior and (0.1, 786.9) given s (Table 6.1).
7. **Result after the price is known.** The posterior 95% range is (188.9, 195.2), with mean 189.8 (Table 6.2).
8. **Adding s to the price.** Conditioning on both price and s gives less variability than price alone. Near the money the SD falls from 6.60 to 4.85 (Table 6.4).

## Key Takeaways
- The asset price is "very informative" for the posterior density of the call price (abstract).
- Conditioning on s alone, with the price unknown, "does not offer much improvement" (s. 6.4).
- The posterior of a long call shows positive skewness and excess kurtosis in all three moneyness cases (Tables 6.3-6.5).
- Near and at the money the posterior is close to normal. The departure grows as the option moves in or out of the money (s. 6.4, s. 6.5).
- The authors present the analytic posterior as an alternative to delta-normal and delta-gamma VaR approximations (s. 6.5).
- The authors defend the BS setting: the model is still widely used, and Dumas et al. (1998) favour building on its deficiencies (s. 6.1).
- Stated extensions: an Ornstein-Uhlenbeck price process, stochastic volatility, stochastic interest rates, warrants and corporate bonds (Remark 1, s. 6.5).
- The chapter is "not about forecasting". The authors call it a prelude to a Bayesian theory of option price forecasting (s. 6.5).

## Source Defects
- The text extraction dropped all Greek letters and most operators. Every formula above comes from the PDF pages. PDF page = book page + 7.
- Not recovered: Corollary 2's formula (book p. 130), Appendix A.1 to A.4 algebra (book pp. 142 onward), and the figures' exact curves.
- Source inconsistency, section numbers: the outline in s. 6.1 cites Sections 6.1 to 6.4. The printed sections are 6.2 to 6.5.
- Source inconsistency, equation cites: s. 6.4 cites eq. (6.21) for E(sigma^2) and eqs. (6.20), (6.19) for lambda and theta. Section 6.3 assigns those jobs to eqs. (6.15)-(6.17).
- Source inconsistency, Proposition 4: the formula has 2(2 lambda + v s^2)t inside the Bessel argument. The "where" line below it prints 2(2 lambda t + v s^2)t.
- Proposition 2 prints "2 sigma 2" in one denominator, which looks like a typesetting slip for 2 sigma^2. It is recorded, not corrected.
- Table 6.3 prints the same SD (2.3) for both densities. The powers 4^-06 and 2.5364^-04 appear exactly so on the page.

## Connects To
- **ch07-bayesian-option-forecasting**: same authors. It adds a predictive density and replaces the (lambda, theta) prior with an implied-volatility prior. It tests the result on FTSE 100 options.
  Section 6.5 points to this extension as Darsinos and Satchell (2001a), a paper that pools implied and historical volatility to forecast FTSE 100 options.
- The chapter cites no other chapter of this book.
