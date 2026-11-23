# Chapter 11: Optimal forecasting horizon for skilled investors
**Authors**: Stephen Satchell and Oliver Williams | **Book pages**: 227-250 | **Type**: METHOD (a theoretical model of forecast horizon choice. It has no data and no case.)

## Core Idea
Forecasting skill, measured by the Information Coefficient (IC), can differ by horizon. The chapter rebuilds Fishwick's (2007, this book's Chapter 10) horizon model in continuous time. It swaps exponential IC decay for power decay. That swap gives a closed-form optimal horizon t* and explicit comparative statics. It then questions how Fishwick and Grinold combine several models (s. 11.1, s. 11.6).

## Frameworks Introduced
- **Single-model horizon problem** (s. 11.2). A score S(0) known at time 0 conditions a stream of instantaneous forecast returns R(r). Choose the horizon t that maximizes W(t), the net conditional expected return per unit time.
- **Theorem 1, optimality conditions** (s. 11.2.3). First-order and second-order conditions for t*, valid when H(t) > 0.
- **Theorem 2, aggression comparative statics** (s. 11.2.3). The sign of dt*/dS(0) depends on average versus marginal beta at t*.
- **Initial value dependent IC function** (Definition 1, eq. 11.2). IC(r) = IC(0) g(r), with g positive and decreasing.
- **Power-decay closed form** (s. 11.3, eq. 11.7). With g(r) = r^(-alpha), t* has an explicit formula and constant elasticities.
- **CEV-style horizon volatility** (s. 11.3.1, eq. 11.8). Forecast volatility sigma(r) = sigma r^theta. The closed form survives with alpha replaced by (alpha - theta).
- **Theorem 3, shape theorem** (s. 11.3). Relates the sign of dt*/d(shape parameter) to the shape of g.
- **Partial Information Coefficient (PIC)** (s. 11.4.1, eq. 11.9). Fishwick's weight for model i among k correlated models.
- **Joint weight-and-horizon optimization** (s. 11.4.2, eqs 11.11-11.13). A mean-variance frontier exists for each t. Then minimize variance over t.
- **Alternative multi-model formulation** (s. 11.5, eqs 11.15-11.16). One scalar score, k models. Condition R(r) on S(0), not S(0) on R(r).
- **Lambert W solution for exponential decay** (Appendix B, eq. 11.19). The continuous-time Fishwick case has a solution, but not in elementary functions.

## Formulas
All formulas below were recovered from PDF, book pp. 228-243 and 247-248. The text extraction lost every Greek letter.

Assumptions 1-4 (s. 11.2.1):

    S(0) ~ N(0, 1)
    R(r) ~ N(0, sigma^2(r))
    S(0), R(r) bivariate normal
    IC(r) = Corr(R(r), S(0)) = Cov(R(r), S(0)) / sigma(r)

- S(0): conditioning information (the score) known at time 0. The authors also call it "aggression".
- R(r): instantaneous forecast rate of return (alpha) at time r. sigma(r): its standard deviation.

Cumulative return, beta and objective (s. 11.2.2, unnumbered):

    R[0,t]  = integral_0^t R(r) dr
    beta(t) = Cov(R[0,t], S(0)) / Var(S(0)) = integral_0^t sigma(r) IC(r) dr
    W(t)    = beta(t) S(0)/t - C(t)/t = H(t)/t,   H(t) = beta(t) S(0) - C(t)

- beta(t): "the volatility-weighted cumulative IC". C(t): total cost function. W(t): net conditional expected rate of return.

Theorem 1 (s. 11.2.3), assuming H(t) > 0:

    H'(t*) t* - H(t*) = 0
    S(0) beta''(t*) < C''(t*)

Theorem 2 (s. 11.2.3):

    dt*/dS(0) > 0  if  beta(t*)/t* < beta'(t*)
    dt*/dS(0) < 0  if  beta(t*)/t* > beta'(t*)

Constant volatility case (eq. 11.1): cumulative IC = beta(t)/sigma.

IC decay (eqs 11.2-11.4):

    IC(r) = IC(0) g(r),  g > 0,  dg/dr < 0          (11.2)
    IC(r) = IC(1) exp(-b(r-1)),  r a positive integer (11.3, Fishwick, discrete)
    IC(r) = IC(0) exp(-b r)                           (11.4, continuous)

Theorem 1 with constant sigma and constant cost C (eq. 11.5):

    sigma IC(0) S(0) g(t*) t* = sigma IC(0) S(0) integral_0^t* g(r) dr - C

Power decay and its closed form (eqs 11.6, 11.7), for S(0) > 0, C > 0:

    g(r) = r^(-alpha),  0 < alpha < 1                          (11.6)
    t*   = [ C(1-alpha) / (sigma alpha S(0) IC(0)) ]^(1/(1-alpha))   (11.7)

Elasticities (a)-(e), s. 11.3:

    dln t*/dln C     =  1/(1-alpha) > 1       (a)
    dln t*/dln S(0)  = -1/(1-alpha) < -1      (b)
    dln t*/dln IC(0) = -1/(1-alpha) < -1      (c)
    dln t*/dln sigma = -1/(1-alpha) < -1      (d)
    dln t*/dalpha    = (1/(1-alpha)) (ln t* - 1/(alpha(1-alpha)))   sign ambiguous   (e)

Theorem 3 (s. 11.3), g(r) = g(r, theta), theta a shape parameter, as printed:

    sign[dt*/dtheta] = sign[ (dg(t*,theta)/dtheta) t* - integral_0^t (dg(r,theta)/dtheta) dr ]

Horizon-dependent volatility (eq. 11.8 and the unnumbered result on p. 236):

    sigma(r) = sigma r^theta                                         (11.8)
    beta(t)  = IC(0) sigma t^(theta-alpha+1) / (theta-alpha+1)
    t* = [ C(1-(alpha-theta)) / ((alpha-theta) sigma S(0) IC(0)) ]^(1/(1-(alpha-theta))),  0 < alpha-theta < 1

- Elasticities keep the form above with (alpha - theta) in place of alpha. The signs of dln t*/dalpha and dln t*/dtheta are ambiguous.

PIC and Fishwick's multi-model return (eqs 11.9, 11.10):

    PIC = COR^(-1) IC                                              (11.9)
    IC(0,t) = sqrt(1/t) * sum_{j=1..t} IC(j)       (constant sigma)
    V_ii = sqrt(1/t) * (1 - exp(-b_i t)) / (1 - exp(-b_i)),  V_ij = 0 for i != j
    E(AR[0,t]) = S' COR^(-1) V IC(1) sigma_1m/t - C/t              (11.10)

- COR: k x k correlation matrix of model scores. IC: k x 1 vector of model ICs. V: diagonal matrix that turns initial ICs into cumulative ICs. S: k x 1 score vector. sigma_1m: common alpha standard deviation.

The authors' amended version, with weights w (w'e = 1), diagonal score matrix S and cost vector C (eqs 11.11-11.14):

    w'Pi = E(w'AR[0,t]) = w'S'V IC(1) sigma_1m/t - w'C/t           (11.11)
    Var(w'AR[0,t]) = w' Sigma(t) w
    min u = (1/2) w'Sigma w - lambda'(Phi w - G),  Phi = (Pi, e)',  G = (mu, 1)'   (11.12)
    w_hat = Sigma^(-1) Phi' (Phi Sigma^(-1) Phi')^(-1) G           (11.13)
    delta(t) = G' (Phi Sigma^(-1) Phi')^(-1) G      (minimized variance. Then minimize over t)
    w'Pi = S(0) w'V IC(1) sigma_1m/t - w'C/t                       (11.14, single scalar score)

Alternative formulation (eqs 11.15, 11.16):

    Alpha(r) = E(R(r)|S(0)) = S(0) sigma(r) IC(r)                  (11.15)
    Alpha(r) = Cov(R(r), S(0)) S(0) = D(r) IC(r) S(0)              (11.16, R(r) a k x 1 vector)
    Alpha[0,t] = D ( integral_0^t G(r) dr ) IC(0) S(0)   (constant D, IC(r) = G(r) IC(0))

- D(r): diagonal matrix of the k forecast standard deviations. G(r): diagonal decay matrix.

The two regression directions (s. 11.5.2), with x = R(r), y = S(0), D = sigma_1m I_k:

    beta_yx = (1/sigma_1m) COR^(-1) IC     (Fishwick's eq. 10.17 uses this)
    beta_xy = sigma_1m IC                  (the authors' eq. 11.15 uses this)

Lambert W solution for g(r) = exp(-b r) (Appendix B, eq. 11.19):

    t* = -(1/b) { W( e^(-1) [ C b/(sigma IC(0) S(0)) - 1 ] ) + 1 }
    requires 0 < C b/(sigma IC(0) S(0)) < 1 for t* positive

## Key Concepts
- **Information Coefficient (IC)**: correlation between forecast and actual returns (Grinold and Kahn 1999, s. 11.1).
- **Multi-period IC**: correlation of time-zero forecasts with returns over contiguous future periods. Skill can differ by horizon.
- **Score**: Grinold (1994): "a standardised measure that shows how strongly you feel about a particular stock at a particular time".
- **Aggression**: the authors' word for the size of S(0) (s. 11.2.4).
- **Average versus marginal cumulative IC**: beta(t*)/t* versus beta'(t*). Their ordering sets the sign in Theorem 2.
- **Active risk**: Grinold's alpha-associated risk. The authors call its introduction "highly problematic" (s. 11.2.3).
- **Grinold's dictum**: alpha equals IC times score times volatility (s. 11.5.1).

## Mental Models
- A fixed cost C is spread over the horizon. A longer horizon dilutes cost but uses weaker, decayed IC. t* balances the two.
- Higher cost pushes t* out more than proportionally. Higher score, IC(0) or volatility pulls t* in more than proportionally (elasticities above one in absolute value).
- Value stocks may forecast better at long horizons. Growth stocks may forecast well only at short horizons (s. 11.1, stated as plausible, not tested).
- With several models, ask which variable conditions on which. The answer changes the formula.

## Anti-patterns
- Reading alpha as a clean decay parameter. For 0 < r < 1, r^(-alpha) rises with alpha, so the sign of dt*/dalpha can be "wrong" (s. 11.3).
- Trusting power decay for realism. The authors say the Fishwick function is "more realistic". The only advantage of eq. 11.6 is eq. 11.7.
- Weighting each model by its own score without question. "It is by no means clear that this is appropriate" (s. 11.4.2).
- Assuming one common cost across models. The Fishwick framework cannot hold differential costs (s. 11.4.2).
- Conditioning S(0) on R(r). The authors argue the correct direction conditions R(r) on S(0) (s. 11.5.2).
- Assuming the joint weight-and-time problem has a solution. Whether it has a well-defined maximum "is an unsolved question" (s. 11.4.2).

## Reference Tables
Table 11.1, elasticities and sensitivities of optimal time (recovered from PDF, book p. 233):

| Parameter | g(r) = r^(-alpha), elasticity | g(r) = exp(-b r), derivative |
|---|---|---|
| C | > 1 | > 0 |
| S(0) | < -1 | < 0 |
| IC(0) | < -1 | < 0 |
| sigma | < -1 | < 0 |
| alpha | sign ambiguous | |
| b | | < 0 |

## Worked Example
The chapter has no data example. Its only numeric illustrations are these.
- Figure 11.1 plots g(r) = r^(-0.5) against g(r) = exp(-0.5 r) for r from 0 to 5. The power curve exceeds 1 for r < 1. The exponential curve stays between 0 and 1.
- Result (e): t* rises with alpha only if t* > exp(1/(alpha(1-alpha))). That threshold has a minimum of exp(4) at alpha = 1/2. For alpha near 0 or 1 it "could be very large" (s. 11.3).

## Key Takeaways
- Continuous time plus power decay yields a closed-form t* (eq. 11.7).
- Both models agree: higher costs lengthen t*, and higher aggression shortens it.
- They disagree on decay. In Fishwick's case more decay b shortens t*. With power decay the sign is ambiguous.
- Rising or falling forecast volatility by horizon fits the same closed form, given theta < alpha.
- The authors are "not convinced" that Grinold's or Fishwick's multi-model methods are the only ways to proceed (s. 11.6).

## Source Defects
- The text extraction lost all Greek letters, integrals and matrix notation. Every formula above comes from the PDF pages.
- PDF page equals book page plus 4 in this chapter.
- Source inconsistencies, recorded and not corrected:
  - The interpretation list on p. 234 labels (c) as volatility and (d) as IC(0). The equations label (c) as IC(0) and (d) as sigma.
  - s. 11.2.4 says that for Fishwick's case "the average is less than the marginal", then expects aggression to decrease t*. Theorem 2 as printed gives an increase for that ordering.
  - The middle line of the eq. 11.7 derivation prints "(alpha/(1 - a))".
  - Theorem 3 prints the integral's upper limit as t, not t*, and a stray differential sign inside the integral.
  - s. 11.2.2 says "If R(r) is serially uncorrelated, in the general case, we define a covariance function".
- Appendix A proofs and the Appendix B derivative algebra are not reproduced here.

## Connects To
- ch10-information-horizon: Fishwick's discrete-time model, eq. 10.2, eq. 10.17 and Table 10.2, which this chapter rebuilds and critiques.
- ch13-hidden-binomial-economy: same authors, on how forecasts enter equilibrium prices.
- ch05-choices-in-forecast-construction: related choices when building forecasts (link by topic only. This chapter does not cite it).
