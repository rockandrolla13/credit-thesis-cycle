# Chapter 6: Portfolio Construction

## Core Idea
A geopolitical or causal view is not finished until it sets asset weights. Use optimization, not ad hoc sizing: linear programs for directional and causal views, Black-Litterman and its ordinal form for views against a benchmark, robust and GAN-based methods for model uncertainty, and an "epistemic" Shapley value to merge a team's probability judgments coherently.

## Frameworks Introduced

- **Why optimize** (6.1): ad hoc weighting causes inconsistent adjustments, higher transaction costs, bias and emotion, uncalibrated risk exposures, and weights that are hard to explain to stakeholders. **Portfolio construction** is defined as "the determination of asset weights in a portfolio."

- **Linear program for a directional geopolitical view** (6.2; eq. 6.1 recovered from PDF p. 151): maximize return subject to caps on the portfolio's weighted correlation with each disliked country index, a cap on weighted beta, full investment and position bounds.
  - Bearish view: cap the weighted correlation (an upper bound). Bullish view: turn the cap into a floor (a lower bound).
  - The disliked assets may stay in the problem with a zero-weight constraint.

- **Linear program for causal views** (6.2.1; eq. 6.2 recovered from PDF p. 152): assign each candidate causal scheme a buy and a sell, and minimize the portfolio's total causal distance, using each scheme's total distance score from Chapter 5 as the cost coefficient.
  - The scores are "metrics which indicate the epistemic utility of each scheme."
  - Constraints: trades sum to zero, bounds on total trade size, bounds on each buy and each sell.

- **Mean-variance optimization (MVO)** (6.3.1; Markowitz 1952; recovered from PDF p. 153):
  - Objective: max over w of w'μ - (γ/2) w'Σw.
  - Solution: w = (1/γ) Σ^-1 μ.
  - μ = asset returns, Σ = covariance matrix, γ = risk aversion.

- **Black-Litterman (BL)** (6.3.2; Black and Litterman 1990, 1991, 1992; equations recovered from PDF pp. 154-155): a Bayesian extension of MVO that frees the manager from "total reliance on historical data."
  1. Reverse-engineer prior mean excess returns from benchmark weights: (6.3) μ0 = γ Σ w0.
  2. Prior is normal with mean μ0 and variance τΣ. With no views, the result replicates the benchmark.
  3. State views with matrices C and M: (6.4) C'μ1 = M.
  4. View variance (He and Litterman 1999): Ω = τ × diag(C'ΣC).
  5. Posterior mean: (6.5) μ~ = μ0 + τ Σ C [ τ (C'ΣC) + Ω ]^-1 [ M - C'μ0 ].
  - **τ**: the manager's confidence in the benchmark, or desired degree of active management. Higher confidence in benchmark returns means a lower τ. τ is typically small (footnote 5).

- **Ordinal Black-Litterman (OBL)** (6.3.3; equations recovered from PDF p. 156): BL for teams that rank assets instead of forecasting. Views enter as rank-based Q vectors on returns, variances and covariances.
  - (6.6) V_post = C_prior + τ ( C_prior - τ C_prior P_var^T ( P_var C_prior P_var^T + (1/τ) I )^-1 P_var C_prior ) Q_var
  - (6.7) E_post = E_prior + τ C_prior P_ret^T ( Q_ret - P_ret E_prior )
  - (6.8) C_post = C_prior + τ C_prior P_cov^T ( Q_cov - P_cov C_prior P_cov^T )
  - Q conventions: higher Q_returns = preference for higher expected return. Higher Q_variances = preference for lower variance. Higher Q_covariances = preference for more diversifying assets.
  - Solved with sequential quadratic programming.

- **Robust MVO** (6.4; Fabozzi et al. 2007; eq. 6.9 recovered from PDF p. 158): replace the single expected-return vector with a set of possible vectors and optimize to worst cases.
  - Argmax over w of E^(r)'w - δ'ψ - λ w'Σw, with w'l = 1.
  - δ = estimation error of expected returns. ψ = weights that react to estimation error. The term -δ'ψ shrinks the weights of assets with large estimation error.
  - Basis: the maxmin expected utility theory of Gilboa and Schmeidler (1989), ambiguity aversion in Ellsberg's (1961) sense.

- **Robust Black-Litterman (rBL)** (6.4; Simonian and Davis 2011; equations recovered from PDF pp. 159-161): BL with uncertainty about the covariance matrix Σ, handled with multiple priors.
  1. Describe uncertainty about Σ by the sampling distribution of its estimator (bootstrap or asymptotic).
  2. Measure how far an alternative prior N_a(μ_a, Σ_a) is from the reference prior N(μ0, Σ) with the **Kullback-Leibler divergence**. (6.10) D(P|Q) = ∫ log( p(x)/q(x) ) p(x) dx.
  3. Closed form as printed: (6.11) D(N_a|N) = ½ ( ln(|Σ_a|/|Σ|) + tr(Σ_a^-1 Σ) + (μ_a - μ0) - n ).
  4. Keep each alternative prior consistent with the benchmark: (6.12) μ_a = γ Σ_a w0.
  5. Set the confidence hyperparameter p in the covariance estimate. It defines η through (6.13) P( D(N_a|N) ≤ η ) = 1 - p. Lower confidence widens the set of "ex ante plausible" priors.
  6. Solve the maxmin problem: (6.14) max over w { min over Σ~_a of w'μ_a - (γ/2) w'Σ~_a w }, subject to (6.15) D(N_a|N) ≤ η.
  7. BL relationships under the alternative prior (6.16): μ~ = μ_a + τ Σ_a C [ τ [C'Σ_a C] + Ω_a ]^-1 [ M - C'μ_a ]. Σ~_a = Σ_a + ( Σ_a^-1/τ + C'Σ_a C )^-1. Ω = τ × diag(C'Σ_a C). μ_a = γ Σ_a w0.
  - Interpretation: the manager picks the distribution that maximizes utility while "nature" picks the one that minimizes it.

- **GAN-based robust optimization** (6.4.1; Goodfellow et al. 2014): a non-parametric complement to the methods above, for testing "exotic" scenarios.
  - **Generative Adversarial Network**: a **Generator** turns random noise into data. A **Discriminator** classifies data as real or fake. They play a minimax game over **epochs**. The text's analogy is a counterfeiter against a detective.
  - Early-epoch output barely resembles the real series and late-epoch output closely resembles it. The whole set gives "alternative market histories."
  - Use: generate many synthetic return and covariance scenarios, then choose the weights that perform well across them on measures such as Sharpe ratio and maximum drawdown.

- **Judgment aggregation** (6.5): combining a team's views so the result is logically or probabilistically coherent.
  - **The discursive problem** (Kornhauser and Sager 1986; Pettit 2001): majority votes on premises can imply a conclusion that the majority vote on the conclusion rejects (Table 6.6).
  - **The probabilistic problem**: averaging managers' probabilities for q, p ∧ q and p | q usually breaks the rule p | q = (p ∧ q) / q.
  - Coherence means consistency with Kolmogorov's (1956) axioms.
  - Alternative noted: Osherson and Vardi (2006) minimize absolute deviation by simulated annealing.

- **Epistemic Shapley value** (6.5, 6.5.1; based on Simonian 2012, 2014): treat the *propositions* as the players, not the managers.
  - **Ideal value** of a proposition = the average of the managers' estimates. It plays the role of a claim.
  - Replace the efficiency axiom with (6.17) **Consistency: ∀R, CON_R**. On every ordering, consistency with the Kolmogorov axioms must be preserved.
  - Procedure: for each ordering of the propositions, earlier propositions take their ideal values. A later proposition takes its ideal value unless that breaks coherence, in which case it is forced to the coherent value. Average each proposition across orderings.
  - Earlier propositions act like players with veto power in permission games.
  - **Coherence adjustment**: feed the resulting values back in as ideal values and repeat. Each pass tightens coherence.
  - **Weighted variant**: drop the symmetry axiom by weighting each manager's estimates before computing ideal values, for example by expertise or seniority.
  - Other variants noted: **quasivalue** (orders not drawn uniformly) and **coalitional structure** (a fixed partition of N as the unit of allocation).
  - Goal: "a coherent and fair allocation of 'epistemic influence.'"

## Key Concepts
- **Prior**: the distribution representing beliefs about a parameter before evidence (footnote 3).
- **Hyperparameter τ**: scales prior variance to the covariance matrix.
- **Maxmin utility**: maximize utility under the worst-case distribution.
- **Model misspecification**: the risk that parameters assumed certain are wrong.
- **Latent variable z**: the random noise input to the Generator.
- **Bi-conditional**: a rule of the form (x ∧ y) ↔ z.
- **Deductive vs inductive reasoning**: propositional logic versus probabilistic reasoning. Finance usually uses the second.

## Mental Models
- **Use an LP when the view is "less of this exposure" or "more of that"** and return forecasts are simple.
- **Use BL when a benchmark anchors the portfolio and views are numeric.** Use OBL when views are rankings.
- **Use rBL when you doubt the covariance matrix**, and set p to how much you doubt it.
- **Think of GAN scenarios as alternative market histories** for validation, alongside Monte Carlo and bootstrapping.
- **Think of causal distance as a cost.** The LP funds the most central causal scheme most.

## Anti-patterns
- **Ad hoc weighting**: reactive to noise, biased, costly and hard to explain.
- **Assuming returns, variances and covariances are known with certainty**: the critical MVO assumption. "Parameter uncertainty is real."
- **Averaging probability estimates across managers**: the fairest-looking method "usually results in incoherent outcomes."
- **Relying only on parametric robust methods**: they generate a limited range of scenarios.
- **Excluding a disliked asset and stopping there**: the remaining portfolio can still be correlated with it.

## Reference Tables

**Eq. 6.1. Directional LP** (recovered from PDF p. 151)

```
Maximize  0.04 x1 + 0.03 x2 + 0.07 x3
s.t.      0.2 x1 + 0.1 x2 + 0.4 x3  <= 0.2     (correlation to excluded country 1)
          0.1 x1 + 0.3 x2 + 0.3 x3  <= 0.3     (correlation to excluded country 2)
          0.60 x1 + 1.0 x2 + 0.85 x3 <= 0.8    (beta to benchmark)
          x1 + x2 + x3 = 1
          0.05 <= x1, x2, x3 <= 0.50
```
Result: x1 = 43%, x2 = 38%, x3 = 19%, expected return 4.19%.

**Eq. 6.2. Causal-view LP** (recovered from PDF p. 152)

```
Minimize  0.66 x1 + 0.83 x2 + 0.50 x3 - 0.66 x4 - 0.83 x5 - 0.50 x6
s.t.      x1 + x2 + x3 + x4 + x5 + x6 = 0.0
          0.04 <= x1 + x2 + x3 <= 0.05
          0.005 <= x1, x2, x3 <= 0.05          (buys)
          -0.02 <= x4, x5, x6 <= -0.005        (sells)
```
Result: x1 = 0.5%, x2 = 0.5%, x3 = 3.0%, x4 = -1.5%, x5 = -0.5%, x6 = -2.0%.

**Table 6.2. OBL example inputs** (recovered from PDF p. 157)

| Item | Value |
|---|---|
| Assets | A, B, C |
| w (benchmark weights) | [0.05, 0.03, 0.03] |
| h (historical returns) | [0.06, 0.07, 0.05] |
| C_prior | rows [0.060, 0.030, 0.020], [0.030, 0.050, 0.025], [0.02, 0.025, 0.040] |
| E_prior | [w1 h1, w2 h2, w3 h3] |
| P_variances | [0, 1, 0] |
| P_returns | [0, 0, 1] |
| P_covariances | [0, 0, 1] |
| Q_variances | [0.500, 0.333, 0.167] |
| Q_returns | [0.167, 0.500, 0.333] |
| Q_covariances | [0.500, 0.167, 0.333] |

Constraints: total allocation budget 1%, buys and sells sum to zero. Result: sell A (-1%), neutral B (0%), buy C (+1%).

**Table 6.3. GAN algorithm** (losses recovered from the PDF text layer, p. 164)

```
Step 1: randomly initialize θg, θd.
Step 2 (Discriminator, k steps): sample real x and latent z.
        Ld = (1/k) Σ_i [ log D(x_i; θd) + log(1 - D(G(z_i; θg); θd)) ]
        θd <- θd + αd * grad_θd Ld
Step 3 (Generator, n steps): sample latent z.
        Lg = -(1/n) Σ_i log D(G(z_i; θg); θd)
        θg <- θg + αg * grad_θg Lg
Repeat until convergence.
```

**Table 6.4. GAN for robust portfolio optimization** (formulas recovered from the PDF text layer, pp. 165-166)

```
N assets; μ initial returns; Σ initial covariance.
Input size K = N + N(N+1)/2          (N(N+1)/2 = lower-triangular covariance elements)
Hyperparameters: α = 0.001 (learning rate), T = 1000 epochs, M = 200 scenarios.
Generator: z1 = ReLU(W1 · x + b1);  z2 = W2 · z1 + b2.
Each epoch t = 1..T:
  1. generate M synthetic scenarios from noise
  2. check shape equals K
  3. split into R_gen (M x N returns) and L_gen (M x N(N+1)/2 covariance elements)
  4. Loss1 = (1/M) Σ_i || R_gen_i - μ ||^2
     Loss2 = (1/M) Σ_i || Σ_gen_i - Σ ||
     total = Loss1 + Loss2; update G by backpropagation
Weights: choose the weight set that maximizes the Sharpe ratio; normalize to sum to 1.
```
Trained with the Adam optimizer (footnote 11).

**Table 6.5. Inputs to the GAN example**

| Item | Value |
|---|---|
| Epochs | 1000 |
| Learning rate | 0.001 |
| Adversarial scenarios | 200 |
| Reference returns | [8%, 12%, 10%, 9%, 11%] |
| Covariance row 1 | 0.010, 0.005, 0.004, 0.002, 0.003 |
| Covariance row 2 | 0.005, 0.020, 0.015, 0.008, 0.010 |
| Covariance row 3 | 0.004, 0.015, 0.030, 0.010, 0.012 |
| Covariance row 4 | 0.002, 0.008, 0.010, 0.015, 0.007 |
| Covariance row 5 | 0.003, 0.010, 0.012, 0.007, 0.025 |

Constraints: weights sum to one, no shorting. Result: [0.1593, 0.2392, 0.2008, 0.1792, 0.2215]. The text notes the portfolio is well diversified with minimal constraints.

**Table 6.6. Judgment aggregation problem**

| Worker | Serious danger? | Effective measure? | Pay sacrifice? |
|---|---|---|---|
| 1 | Yes | No | No |
| 2 | No | Yes | No |
| 3 | Yes | Yes | Yes |
| Majority | Yes | Yes | No |

The majority row is derived from the three votes. The source table has no such row but states the conflict in the text.

**Table 6.7. Manager probability assignments**

| Manager | q | p ∧ q | p given q |
|---|---|---|---|
| 1 | 0.50 | 0.10 | 0.20 |
| 2 | 0.25 | 0.20 | 0.80 |
| Average (ideal value) | 0.375 | 0.15 | 0.50 |

**Table 6.8. Epistemic Shapley orderings** (x = q, y = p ∧ q, z = p given q)

| Ordering | x | y | z |
|---|---|---|---|
| xyz | 0.375 | 0.15 | 0.40 |
| xzy | 0.375 | 0.1875 | 0.50 |
| yxz | 0.375 | 0.15 | 0.40 |
| yzx | 0.30 | 0.15 | 0.50 |
| zxy | 0.375 | 0.1875 | 0.50 |
| zyx | 0.30 | 0.15 | 0.50 |
| **SV** | 0.35 | 0.1625 | 0.46 |

**Table 6.9. Second iteration** SV: x = 0.349, y = 0.1627, z = 0.465.

**Table 6.10. Weighted orderings** (Manager 1 weight 0.666, Manager 2 weight 0.334. Ideal values q = 0.4165, p ∧ q = 0.1334, p given q = 0.4004)

| Ordering | x | y | z |
|---|---|---|---|
| xyz | 0.4165 | 0.1334 | 0.32 |
| xzy | 0.4165 | 0.1668 | 0.4004 |
| yxz | 0.4165 | 0.1334 | 0.32 |
| yzx | 0.3331 | 0.1334 | 0.4004 |
| zxy | 0.4165 | 0.1668 | 0.4004 |
| zyx | 0.3331 | 0.1334 | 0.4004 |
| **SV** | 0.3887 | 0.1445 | 0.372 |

## Worked Example

**1. From causal graphs to trades** (6.2.1). Three causal schemes for a fall in interest rates, with total distance scores G1 0.66, G2 0.83, G3 0.50 (Chapter 5).
- Mapping assumed in the text: G1 supports buying consumer staple stocks and selling private REITs. G2 supports buying private REITs and selling consumer staples. G3 supports buying public REITs and selling consumer staples.
- Solve eq. 6.2. The most central scheme, G3, receives the largest buy (3.0%). G1 and G2 receive the minimum buy (0.5% each).
- Pair trades: buy 0.5% staples and sell 1.5% private REITs. Buy 0.5% private REITs and sell 0.5% staples. Buy 3.0% public REITs and sell 2.0% staples.
- Net: buy 3.0% public REITs, sell 1.0% private REITs, sell 2.0% consumer staples.
- The author notes this is one of several ways to assign buys and sells.

**2. Coherent team probability** (6.5.1). Two managers judge q (a regime occurs) and p ∧ q, which imply p given q.
- Averages: q = 0.375, p ∧ q = 0.15, p given q = 0.50. Incoherent, because 0.15 / 0.375 = 0.40, not 0.50.
- Ordering xyz: x takes 0.375, y takes 0.15, so z is forced to 0.40.
- Ordering xzy: x takes 0.375, z takes 0.50, so y is forced to 0.1875.
- Ordering yzx: y takes 0.15, z takes 0.50, so x is forced to 0.30.
- Average across the six orderings: q = 0.35, p ∧ q = 0.1625, p given q = 0.46. Coherent to two decimals (0.464 against 0.466 at the third).
- Iterate once more: 0.349, 0.1627, 0.465. The ratio is 0.465872 against an SV estimate of 0.465873.
- Weighted case: if Manager 1 counts twice as much, the SV is q = 0.3887, p ∧ q = 0.1445, p given q = 0.372. Further iteration refines it.

## Key Takeaways
1. Turn each view into a constraint or a cost in an optimizer. Do not size by feel.
2. For a bearish geopolitical view, cap the portfolio's correlation to the affected market as well as its weight.
3. Fund competing causal stories in proportion to their centrality, using total distance scores as LP costs.
4. Use rankings directly through OBL when the team does not produce point forecasts.
5. Model doubt about the covariance matrix explicitly (rBL), and stress-test on GAN-generated histories.
6. Never average a team's linked probabilities. Use the epistemic Shapley procedure and iterate to the precision needed.
7. Every example is deliberately minimal. The author says added variables and constraints are "likely necessary" in practice.

## Connects To
- **Ch 3**: the Shapley value and its axioms.
- **Ch 5**: causal graphs G1 to G3, Table 5.6 distance scores and do-operator probabilities feed the LP.
- **Ch 2 to 4**: simulations supply the directional views expressed here.
- **External**: Markowitz (1952), Black and Litterman (1990 to 1992), He and Litterman (1999), Fabozzi et al. (2007), Simonian and Davis (2011), Gilboa and Schmeidler (1989), Goodfellow et al. (2014), List and Pettit (2002).

## Extraction Notes
- All numbered equations (6.1 to 6.17) and the MVO, GAN and Table 6.4 formulas were undecoded in the extraction. They were recovered from PDF page images (pp. 151-153, 155-161) or the PDF text layer (pp. 164-166, 169) as marked.
- Tables 6.2 and 6.5 were flattened into one line in the extraction. They were rebuilt from the PDF (Table 6.2) and from the flattened line (Table 6.5), whose 25 numbers form a symmetric 5 × 5 matrix.
- Source inconsistency, eq. 6.2: the text says the second and third constraints set "upper and lower bounds" and the fourth and fifth likewise. The printed order is lower then upper.
- Source inconsistency, OBL: Table 6.1 says P_returns and P_variances are identity matrices. Table 6.2 gives them as the vectors [0, 0, 1] and [0, 1, 0]. Eq. 6.6 names the posterior "V_posterior" and the text does not show the intermediate posterior values for the example.
- Source as printed, eq. 6.11 and 6.15: the mean term is printed as (μ_a - μ0), not as a quadratic form. Eq. 6.10 is headed D(P|Q) while the text describes Q conditional on P. Reproduced as printed.
- Source as printed, Table 6.3: both updates are labelled "gradient ascent," including the Generator's update on a loss with a leading minus sign.
- Source as printed, Table 6.4: the loss items are numbered (i), (iii), (ii), (iv) in the extraction. Loss1 carries a squared norm and Loss2 does not. Table 6.4 describes only a Generator, with no Discriminator, although it is called a GAN.
- Source as printed, 6.5.1: the coherence ratio is written "q/p ∧ q". The numbers match (p ∧ q)/q. Table 6.8 prints the SV for z as 0.46 (the average of the column is 0.4667).
- The text spells the value both "Shapley" and "Shapely".
