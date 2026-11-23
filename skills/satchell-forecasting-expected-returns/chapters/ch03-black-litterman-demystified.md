# Chapter 3: A demystification of the Black-Litterman model: managing quantitative and traditional portfolio construction
**Authors**: Stephen Satchell and Alan Scowcroft | **Book pages**: 39-53 | **Type**: METHOD (a Bayesian derivation with two extensions. The two numeric examples illustrate the method and test nothing)

## Core Idea
The Black-Litterman (BL) model is Bayes' theorem applied to expected returns. The fund manager's views form the prior. Equilibrium returns from the quantitative model form the data. The posterior is a blend that both camps can use. The authors give the mathematics, which they say had "no readable description", plus two extensions.

## Frameworks Introduced
- **BL as a bridge between judgemental and quantitative managers** (s. 3.1). Managers give views. The views enter the quantitative model. The final forecast reflects both.
- **Equilibrium excess returns** (s. 3.2). pi comes from the CAPM, or from the prevailing supply of value-weighted assets: pi = delta Sigma w_m.
- **Bayes' theorem in BL notation** (s. 3.2). pdf(E(r)|pi) = pdf(pi|E(r)) pdf(E(r)) / pdf(pi). Three parts:
  1. pdf(E(r)): the prior. It holds the manager's views.
  2. pdf(pi): the marginal pdf of equilibrium returns. Not modelled. It "disappears in the constant of integration".
  3. pdf(pi|E(r)): the conditional pdf of the equilibrium return data, given the investor's forecasts.
- **Assumption A1 (views as linear restrictions)** (s. 3.2). k beliefs. Known (k x n) matrix P and (k x 1) vector q. y = P E(r) ~ N(q, Omega). Omega is diagonal. Larger omega_ii means more disbelief. omega_ii = 0 is absolute certainty. In practice, bound omega_ii above zero.
- **Assumption A2 (data model)** (s. 3.2). pdf(pi|E(r)) is N(E(r), tau Sigma). tau is a known scaling factor "often set to 1".
- **Theorem 1 (posterior mean and variance)** (s. 3.2, proof in Appendix). The posterior is normal. The authors add the variance formula, which BL "did not report".
- **Extension 1: stochastic tau, multivariate t posterior** (s. 3.4, A3, A4, Theorem 2, Corollary 1). Put a scale gamma prior on omega = 1/tau. The posterior of E(r) becomes multivariate t.
- **Extension 2: scenario probabilities** (s. 3.4, A5, eqs 3.1-3.3). The manager gives m scenarios q_i with prior probabilities p_i. The data update them to posterior probabilities p_i*.
- **Consistency check for confidence inputs** (s. 3.4). If a scenario looks unlikely under eq. 3.3, revise its omega_ii upwards.

### Procedure used in the examples (s. 3.3)
1. Fix the asset universe, benchmark weights and Sigma.
2. Set delta and compute pi.
3. State one view: P (1 x n) and q.
4. Set tau and the confidence omega (Tables 3.1, 3.5).
5. Compute the conditional forecast E(r|pi) by Theorem 1 (Tables 3.2, 3.6).
6. Feed E(r|pi) to a mean-variance optimizer with constraints (Tables 3.3, 3.7).
7. Read the tilts against the benchmark (Tables 3.4, 3.8).

## Formulas
The chapter numbers only eqs 3.1-3.3 and A.1-A.12. Others are cited by section. All were recovered from the PDF (book pp. 40-42, 47-52). The text extraction lost every Greek letter.

    (s. 3.2)  pi = beta (mu_m - r_f)
    (s. 3.2)  beta = Cov(r, r'w_m) / sigma_m^2
    (s. 3.2)  pi = delta Sigma w_m ,   delta = (mu_m - r_f) / sigma_m^2

- r: (n x 1) vector of asset excess returns. pi: (n x 1) equilibrium excess returns. mu_m: return on the global market in domestic currency. r_f: riskless domestic rate. beta: (n x 1) asset betas. w_m: global market weights by market value. sigma_m^2: variance of the world market return. Sigma = Cov(r, r'). delta: a positive constant.
- E(r) is shorthand for E(r_t+1 | I_t), with I_t all information up to period t.

    (s. 3.2)  pdf(E(r)|pi) = pdf(pi|E(r)) pdf(E(r)) / pdf(pi)

    (A1)      y = P E(r) ,  y ~ N(q, Omega)
    (A2)      pdf(pi|E(r)) is N(E(r), tau Sigma)

    (Theorem 1)  pdf(E(r)|pi) ~ N( [ (tau Sigma)^-1 + P' Omega^-1 P ]^-1 [ (tau Sigma)^-1 pi + P' Omega^-1 q ] ,
                                   [ (tau Sigma)^-1 + P' Omega^-1 P ]^-1 )

Appendix shorthand, used in both theorems:

    C = (tau Sigma)^-1 pi + P' Omega^-1 q
    H = (tau Sigma)^-1 + P' Omega^-1 P          (symmetric, H = H')
    A = q' Omega^-1 q + pi' (tau Sigma)^-1 pi

    (A.1)  pdf(E(r)|pi) ∝ exp( -1/2 (E(r) - H^-1 C)' H (E(r) - H^-1 C) )
    (A.2)  mean of E(r)|pi = H^-1 C
    (A.3)                  = [ (tau Sigma)^-1 + P' Omega^-1 P ]^-1 [ (tau Sigma)^-1 pi + P' Omega^-1 q ]
    (A.4)  Var(r|pi) = [ (tau Sigma)^-1 + P' Omega^-1 P ]^-1

Proof step (Appendix): the exponent is rewritten as

    (E(r) - H^-1 C)' H (E(r) - H^-1 C) + A - C' H^-1 C

and the terms without E(r) go into the constant of integration.

Extension 1 (s. 3.4):

    (A3)  pdf(pi | E(r), tau) ~ N(E(r), tau Sigma)
          pdf(E(r) | tau)     ~ N(q, tau Omega)
    (A4)  pdf(omega) = (lambda/2)^(m/2) omega^((m/2)-1) exp(-lambda omega / 2) / Gamma(m/2) ,   0 < omega < infinity

- omega = 1/tau, "often called the precision". m and lambda are hyperparameters. Gamma(.) is the gamma function. Assumed independent of pdf(pi).
- Remark 2 as printed: E(omega) = m lambda and Var(omega) = 2 m lambda^2.

    (Theorem 2)  pdf(E(r)|pi) ∝ [ m + (E(r) - theta)' lambda* V (E(r) - theta) ]^(-(m+n)/2)
                 lambda* = m / (lambda + A - C' H^-1 C)

- theta: the mean E(r|pi) from Theorem 1. V: stated as Var(r|pi) from Theorem 1. A multivariate t distribution.

    (Corollary 1)  pdf(omega | E(r), pi) is scale gamma, "degrees of freedom" m + n, scale factor G + lambda
                   G = (pi - E(r))' Sigma^-1 (pi - E(r)) + (P E(r) - q)' Omega^-1 (P E(r) - q)
                   E(omega | E(r), pi)   = (m + n)(G + lambda)
                   Var(omega | E(r), pi) = 2 (m + n)(G + lambda)^2
                   increase in precision = (m + n)(G + lambda) - m lambda = m G + n (G + lambda)

Extension 2 (s. 3.4):

    (A5)   prior: P E(r) = q_i , i = 1..m , each with prior probability p_i , SUM p_i = 1
    (3.1)  phi_i = pdf(pi | P E(r) = q_i)
                 = (1/(2 pi_const))^(k/2) * 1/det(P Sigma P') * exp( -(P pi - q_i)' (P Sigma P')^-1 (P pi - q_i) / (2 tau) )
    (3.2)  p_i* = p_i phi_i / SUM_i p_i phi_i
    (3.3)  p_i* = p_i exp( -(P pi - q_i)' (P Sigma P')^-1 (P pi - q_i) / (2 tau) )
                  / SUM_i p_i exp( -(P pi - q_i)' (P Sigma P')^-1 (P pi - q_i) / (2 tau) )

- pi_const is the number 3.14159..., written here to separate it from the return vector pi. p_i*: posterior probability of scenario i. phi_i reaches its maximum when P pi = q_i.

## Key Concepts
- **Equilibrium excess returns (pi)**: implied returns from the equilibrium model. "The input of the quantitative manager" (s. 3.2).
- **Prior pdf**: here, the manager's views on E(r) (s. 3.2).
- **Hyperparameters**: q and Omega. They parameterize the prior and are known to the investor (A1).
- **Degree of disbelief (omega_ii)**: diagonal element of Omega. Larger means less belief in view i (A1).
- **Natural conjugate prior**: the Bayesian name for the prior BL chose (s. 3.2).
- **Conditional forecast E(r|pi)**: the posterior mean. Forecasts "after updating for the information from the quantitative model" (s. 3.2).
- **Precision (omega = 1/tau)**: in the first extension only. Note the symbol clash with omega_ii (s. 3.4).
- **Scale gamma**: the prior and posterior family for precision (A4, Corollary 1).
- **Tracking error (active risk)**: "the annualized standard deviation of portfolio active return" (footnote 3).
- **ICAPM**: used here to mean international CAPM, not intertemporal CAPM (footnote 1).
- **Universal hedging factor**: Black's (1990) result that all investors hedge the same share of overseas investment. Adler and Prasad (1992) show how restrictive it is (s. 3.2).

## Mental Models
- **Views are the prior, the market is the data.** The authors note their reading "may differ from BL" (s. 3.2).
- **A view is a new equilibrium, not a short-term call.** The 0.5% Swiss-German view is a "modest target" chosen to stress this (s. 3.3.1).
- **The forecast is the product of the view and the data model.** A forecast can move against the view's wording, as Ireland does. Read it as how far the neutral forecast must change to reflect the view (s. 3.3.2).
- **The optimizer filters forecast changes.** A large forecast change can give a small weight change once benchmark weight, beta and covariances count (s. 3.3.1, Italy).
- **Fat tails as a diagnostic.** Small m in the t posterior puts more weight in the tails. This captures uncertainty about the forecasts (s. 3.4).
- **Managers think in scenarios.** They can supply scenarios with probabilities more easily than a gamma prior (s. 3.4).
- "The rational investor is a Bayesian" (Markowitz 1987, quoted in s. 3.4).

## Anti-patterns
- **Feeding raw forecast alphas to an optimizer.** They are volatile and give "completely unacceptable revisions to portfolio weights" (s. 3.3.2).
- **Assuming A2 holds for every manager.** Many practitioners show "the most alarming biases relative to the market view" (s. 3.2).
- **Using priors that carry no behavioural meaning.** Diffuse and other priors "cannot be easily understood in behavioural terms" (s. 3.2).
- **Setting omega_ii to exactly zero.** Bound it above zero as a practical matter (A1).
- **Adding FX as an asset class without care.** It needs hedge-ratio assumptions (s. 3.2).
- **Asking a non-mathematical manager for gamma-prior parameters.** The prior is "too complex to capture the beliefs" of such a manager (s. 3.4).
- **Reading a posterior scenario probability as a per-view probability.** It relates to the entire scenario (s. 3.4).

## Reference Tables

**Tables 3.1 and 3.5 Bayesian parameters**

| Parameter | Symbol | Example 1 (Table 3.1) | Example 2 (Table 3.5) |
|---|---|---|---|
| Delta | delta | 5.00 | 3.000 |
| Tau | tau | 1.00 | 1.000 |
| View | q | 0.05 | 0.015 |
| Confidence | omega | 0.05 | 0.025 |

**Tables 3.3 and 3.7 Optimization parameters**

| Parameter | Example 1 (Table 3.3) | Example 2 (Table 3.7) |
|---|---|---|
| Risk aversion lambda | 2.5 | 1.5 |
| Tracking error limit | 2.5 | 2.5 |
| Portfolio beta | 1.0 | 1.0 |

**Tables 3.2 and 3.4 Example 1: forecasts and optimization results** (sterling-based, 11 European equity markets)

| Market | Bench weight | Swiss Cov x100 | pi | E(r\|pi) | Diff | Beta | Solution weight (%) | Weight diff |
|---|---|---|---|---|---|---|---|---|
| Switzerland | 0.0982 | 0.1884 | 5.34 | 5.53 | +0.19 | 0.80 | 12.19 | +2.37 |
| Germany | 0.1511 | 0.0724 | 6.46 | 6.31 | -0.15 | 0.97 | 12.81 | -2.30 |
| Denmark | 0.0136 | 0.0766 | 5.31 | 5.29 | -0.02 | 0.80 | 1.22 | -0.14 |
| Spain | 0.0409 | 0.0666 | 8.07 | 7.99 | -0.08 | 1.20 | 4.27 | +0.18 |
| Finland | 0.0125 | 0.0666 | 10.69 | 10.55 | -0.14 | 1.57 | 1.37 | +0.11 |
| France | 0.1234 | 0.1016 | 7.93 | 7.89 | -0.03 | 1.18 | 12.61 | +0.27 |
| Italy | 0.0568 | 0.0061 | 8.06 | 7.88 | -0.18 | 1.20 | 5.63 | -0.05 |
| Netherlands | 0.0870 | 0.0826 | 5.64 | 5.62 | -0.03 | 0.85 | 8.04 | -0.66 |
| Norway | 0.0103 | 0.0979 | 8.43 | 8.40 | -0.03 | 1.25 | 1.10 | +0.07 |
| Sweden | 0.0474 | 0.0776 | 7.71 | 7.67 | -0.04 | 1.15 | 4.77 | +0.02 |
| UK | 0.3588 | 0.0784 | 6.33 | 6.33 | -0.00 | 0.95 | 36.00 | +0.12 |

**Tables 3.6 and 3.8 Example 2: forecasts and optimization results** (US dollar-based, 15 European markets)

| Market | Group | Bench weight | pi | E(r\|pi) | Diff | Beta | Solution weight (%) | Weight diff |
|---|---|---|---|---|---|---|---|---|
| Austria | Hard | 0.0060 | 14.84 | 15.05 | +0.21 | 1.09 | 3.27 | +2.67 |
| Belgium | Hard | 0.0244 | 13.75 | 13.83 | +0.08 | 1.02 | 4.82 | +2.38 |
| France | Hard | 0.1181 | 14.86 | 14.98 | +0.12 | 1.10 | 15.90 | +4.09 |
| Germany | Hard | 0.1446 | 13.57 | 13.60 | +0.04 | 1.00 | 18.63 | +4.17 |
| Netherlands | Hard | 0.0832 | 12.33 | 12.38 | +0.06 | 0.92 | 9.28 | +0.96 |
| Ireland | Hard | 0.0076 | 11.18 | 11.03 | -0.15 | 0.84 | 3.39 | +2.63 |
| Denmark | Soft | 0.0130 | 12.24 | 11.92 | -0.32 | 0.91 | 0.00 | -1.30 |
| Finland | Soft | 0.0120 | 18.83 | 17.58 | -1.24 | 1.37 | 0.00 | -1.20 |
| Italy | Soft | 0.0543 | 16.62 | 15.42 | -1.20 | 1.22 | 2.66 | -2.77 |
| Norway | Soft | 0.0098 | 15.55 | 15.04 | -0.51 | 1.14 | 0.00 | -0.98 |
| Portugal | Soft | 0.0049 | 11.84 | 11.67 | -0.17 | 0.88 | 0.00 | -0.49 |
| Spain | Soft | 0.0392 | 13.63 | 13.03 | -0.60 | 1.01 | 0.98 | -2.94 |
| Sweden | Soft | 0.0454 | 13.04 | 12.28 | -0.76 | 0.97 | 1.82 | -2.72 |
| Switzerland | Soft | 0.0940 | 13.27 | 13.29 | +0.02 | 0.98 | 6.79 | -2.61 |
| UK | Soft | 0.3433 | 12.74 | 12.68 | -0.06 | 0.95 | 32.46 | -1.88 |

**Table 3.9 Posterior probabilities** (ten equally likely scenarios for the EMU example, prior 10.00% each)

| Scenario outperformance (%) | 0.5 | 1.0 | 1.5 | 2.0 | 2.5 | 3.0 | 3.5 | 4.0 | 4.5 | 5.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| Posterior probability (%) | 10.07 | 10.06 | 10.05 | 10.04 | 10.02 | 10.00 | 9.98 | 9.96 | 9.93 | 9.90 |

## Worked Example

**Example 1: Swiss versus German equities** (s. 3.3.1)
- View: a sterling-based investor believes Swiss equities will outperform German equities by 0.5% per annum. Returns are in sterling and unhedged.
- One belief, k = 1. P = [1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0] over 11 markets. The text gives q = 0.5%.
- Parameters (Table 3.1): delta 5.00, tau 1.00, view 0.05, confidence 0.05.
- Forecast (Table 3.2): Switzerland rises from 5.34 to 5.53. Germany falls from 6.46 to 6.31. Other markets move too. Larger moves go with low covariance with Switzerland. Italy has covariance 0.0061 and moves -0.18.
- Optimization (Table 3.3): mean-variance utility, risk aversion 2.5 "set with reference to delta", tracking error limit 2.5. Portfolio beta and the sum of weights are constrained to unity.
- Result (Table 3.4): Switzerland +2.37 points and Germany -2.30 points against the benchmark. Italy's weight moves only -0.05.
- Currency holdings could vary from zero to minus the market weight. All solution currency weights were negligible.
- Sharpe ratio 0.16. Tracking error 0.39.

**Example 2: hard-currency markets, "a possible EMU scenario"** (s. 3.3.2)
- View: a US dollar-based investor believes six hard currency markets will outperform nine other European markets, on average, by 1.5% per annum.
- Still one view. P is (1 x 15) = [1/6 ... 1/6  -1/9 ... -1/9].
- Parameters (Table 3.5): delta 3.000, tau 1.000, view 0.015, confidence 0.025. Delta is 3 "to ensure that the level of the conditional forecast accords with historical experience".
- Forecast (Table 3.6): hard markets rise and soft markets fall, broadly. Two exceptions: Ireland (hard) falls 0.15 and Switzerland (soft) rises 0.02.
- Optimization (Table 3.7): weights positive and summing to unity, beta at unity, tracking error bounded at 2.5, risk aversion 1.5.
- Result (Table 3.8): all six hard markets gain weight, including Ireland (+2.63). All nine soft markets lose weight. Four go to 0.00.
- All solution currency weights are zero. Sharpe ratio 0.18. Tracking error 1.8.

**Scenario update on the EMU example** (s. 3.4, Table 3.9)
- Ten scenarios of hard-market outperformance, 0.5% to 5.0%, each with prior p_i = 0.1.
- Eq. 3.3 gives posteriors from 10.07% (0.5%) down to 9.90% (5.0%).
- The authors read this as: "substantial outperformance is much less likely given the historic covariances".

## Key Takeaways
- BL is a standard Bayesian result with a natural conjugate prior. Neither A1 nor A2 is essential (s. 3.2).
- The posterior mean blends pi and the views. The posterior variance is [ (tau Sigma)^-1 + P' Omega^-1 P ]^-1 (Theorem 1).
- One view moves forecasts for all assets (Tables 3.2, 3.6).
- Combining neutral forecasts with views "produces robust inputs for the optimizer" (s. 3.3.2).
- With stochastic tau, the posterior is multivariate t. The mean and covariance stay the same up to a scale factor. It remains consistent with mean-variance analysis and the CAPM, per Klein and Bawa (1976) (s. 3.4).
- The authors give no numbers for the t model. They judge its prior too complex for a typical manager (s. 3.4).
- Scenario posteriors give the manager a consistency check on prior beliefs and on the confidence numbers omega_ii (s. 3.4).
- A volatility extension through implied volatility has "no simple way forward" (s. 3.2).

## Source Defects
- **Damaged in text**: every Greek letter (pi, Sigma, Omega, omega, tau, delta, beta, mu, lambda, theta, phi, Gamma), all decimal points, and the layout of Theorem 1, A4, Theorem 2, eqs 3.1-3.3 and the Appendix.
- **Recovered from PDF**: all formulas above and Tables 3.1-3.9 (book pp. 40-52). PDF page = book page + 8.
- **Not transcribed**: Appendix eqs A.5-A.12 (the integration steps for Theorem 2 and the corollary). They are legible in the PDF on book pp. 51-53.
- **Inconsistencies in the source, recorded as printed**:
  - Example 1 text gives q = 0.5%. Table 3.1 gives View = 0.05.
  - The result is stated as "Corollary 1" and then cited and proved as "Corollary 2.1".
  - Theorem 2 says V is Var(r|pi) from Theorem 1. The proof gives V = m H / (lambda + A - C' H^-1 C).
  - The Appendix prose writes "A - C'HC". The equations write A - C' H^-1 C.
  - The expanded quadratic in the proof of Theorem 1 prints one factor as P' Omega P, without the inverse.
  - "E(omega|E(r),pi) - E(w)" mixes omega and w. The Appendix uses w for the precision.
  - The Zellner (1971) multivariate t definition calls theta and V "matrices" of size (l x 1).
  - The symbol omega means a view's disbelief (A1) and the precision 1/tau (A4). The symbol lambda means risk aversion (Tables 3.3, 3.7) and a gamma hyperparameter (A4).
  - Example 1 says beta and the weight sum are constrained. Example 2 says that, "as in Example 1", weights are also constrained to be positive.
  - The chapter cites "Lee (1999)". Chapter 2 cites a Lee work of the same title as Lee (2000).
- Units in Tables 3.2 and 3.6 are not labelled. The tracking error figures carry no unit.

## Connects To
- **ch02-black-litterman-step-by-step**: Idzorek's implementation guide for the same formula. It uses Pi, lambda and Q where this chapter uses pi, delta and q. It calls the equilibrium the prior. It criticizes this chapter's equal-weighting P and cites its tau "often set to 1".
- **ch06-bayesian-black-scholes** and **ch07-bayesian-option-forecasting**: Bayesian treatment of volatility and options. This chapter raises a volatility prior and leaves it open (s. 3.2).
- **ch08-robust-optimization**: another answer to optimizer sensitivity to forecast changes.
- **ch04-portfolios-from-ordering-information**: another way to turn manager views into portfolios.
