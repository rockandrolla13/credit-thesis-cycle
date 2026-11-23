# Chapter 4: Optimal portfolios from ordering information

**Authors**: Robert Almgren and Neil Chriss | **Book pages**: 55-99 | **Type**: METHOD (a portfolio-construction procedure with proofs, tested on one reversal backtest and one simulation)

## Core Idea
An investor often knows only the order of expected returns, not their values. The chapter replaces the expected-return vector of Markowitz with a set of inequality beliefs. It defines which portfolios are preferable under those beliefs, and it shows that one vector, the centroid of the cone of consistent returns, captures the preference. The optimal portfolio is then the mean-variance portfolio that uses the centroid in place of expected returns (s. 4.1, 4.3).

## Frameworks Introduced
- **Portfolio sort** (s. 4.2): "information about an investor's belief as to the order of expected returns". It may be complete, partial, or several sorts at once.
- **Belief vectors and belief matrix** (s. 4.2.2): each belief is a homogeneous linear inequality `D_j^T r >= 0`. The m beliefs stack into the m x n matrix D. Beliefs need not be independent, and m may be below, equal to or above n. One restriction: the consistent set must have a non-empty interior. That rules out opposing inequalities used to force an equality.
- **Consistent cone Q** (eq. 4.3): the set of all expected-return vectors that satisfy the beliefs. Any r in Q "may be the actual expected return vector".
- **Relevant / irrelevant decomposition** (s. 4.2.3): R is the span of the belief vectors. R-perp is its orthogonal complement. Every portfolio splits as `w = w0 + w_perp`. Preference uses only w0.
- **Preference relation from a sort** (s. 4.2.3): v is preferred to w if the relevant part of v has expected return at least that of w for every r in Q. The relation is weak. Many pairs cannot be compared.
- **Efficient portfolio and efficient set** (s. 4.2.4): w is efficient in the budget constraint set M if no allowable v is strictly preferred to it. The efficient set is not one portfolio. Under a risk constraint its size is 1/n! of the possible set (s. 4.2.5).
- **Theorems 1 and 2** (s. 4.2.4): w is efficient if and only if M has a supporting hyperplane at w whose normal b lies in Q-bar = Q ∩ R. Theorem 1 needs b strict or b in the relative interior. Theorem 2 needs Q with non-empty interior and M convex. The normal b is "in effect a vector of imputed returns" (s. 4.2.5).
- **Extended preference relation** (s. 4.3.2): put a probability measure mu on Q. Prefer v to w if v beats w on a set of consistent returns with larger measure.
- **Centroid** (s. 4.3.2, Theorems 3 and 4): c is the centre of mass of Q under mu. If mu has mirror symmetry about Q-bar, two portfolios are equally preferable exactly when `(w - v)^T c = 0`.
- **Centroid optimal portfolio** (Definition 1, Theorem 5, s. 4.3.3): w in M is centroid optimal if no v in M has `v^T c > w^T c`. Only the direction of c matters, not its length.
- **Neutral measure** (s. 4.3.4): the authors require a radially symmetric density, constant over directions inside Q. The radial part may have any form with finite total measure. The result does not depend on it.
- **Three ingredients of the formulation** (s. 4.6): (1) ordering information that gives a cone of consistent returns, (2) a probability density inside that cone, (3) a convex constraint set for the portfolio.
- **Four construction methods compared** (s. 4.5.1): linear, centroid, optimized linear, optimized centroid.
- **Permutation distance** (s. 4.5.3): a number that measures how far a proposed ordering is from the true ordering.

### Types of sort (s. 4.4)
| Sort | Beliefs | Count m | Notes |
|---|---|---|---|
| Complete sort (s. 4.2.2, 4.4.1) | r1 >= r2 >= ... >= rn | n - 1 | One irrelevant direction, (1,...,1). Cone is a wedge with spine along the diagonal. |
| Sector sorts (s. 4.4.2) | Complete sort inside each of k sectors, none across sectors | n - k | R-perp has dimension k (the sector means). Q is a product of sector cones. |
| Complete sort with long-short beliefs (s. 4.4.3) | r1 >= ... >= r_l >= 0 >= r_(l+1) >= ... >= rn | n | No irrelevant direction. R is all of R^n. |
| Performance relative to index (s. 4.4.4) | First l stocks beat index I = sum mu_j S_j, the rest lag it | n | Belief vectors are orthogonal to (1,...,1), so not independent. Cone still has non-empty interior. |
| Partial sorts (s. 4.4.5) | Sorts that do not cover the whole universe | varies | Natural case: criteria valid inside a sector but not across sectors. |
| Multiple sorts (s. 4.4.5) | Two or more conflicting criteria, for example book-to-market and size | varies | Give probability p to cone Q1 and 1 - p to Q2. Combined centroid is the weighted average of the two centroids. |
| Missing information (s. 4.4.5) | Rankings in part of the list carry no meaning | varies | Average the centroid components inside the uncertain index range. |

### Constraint sets treated (s. 4.2.5)
1. **Total investment** `|w1| + ... + |wn| <= W`. Efficient portfolios hold only the top and bottom asset, long the first and short the last. "The covariance matrix plays no role."
2. **Risk constraint** `w^T V w <= sigma^2`. Efficient points are `w = V^-1 E x` with x >= 0.
3. **Risk constraint with market neutrality** `mu^T w = 0`.
4. **Transaction cost limit** `F(w) <= C`, intersected with any of the above.

## Formulas
All formulas below were recovered from the PDF. The text extraction lost every Greek letter and set symbol.

    Q-bar = { lambda * rho | lambda >= 0 }                          (4.1)
(recovered from PDF, book p. 59). rho = the given expected-return vector. Q-bar = the smallest cone containing rho.

    R_perp = { r in R^n | rho^T r = 0 }                             (4.2)
(recovered from PDF, book p. 60). The return vectors orthogonal to rho.

    Q = { r in R^n | D r >= 0 }
      = { r in R^n | D_j^T r >= 0 for each j = 1,...,m }            (4.3)
(recovered from PDF, book p. 61). D = m x n belief matrix. D_j = belief vector j. r = candidate expected-return vector.

    Complete sort: D has rows (0,...,0, 1, -1, 0,...,0)            (4.4)
(recovered from PDF, book p. 62). m = n - 1 rows. Row j has +1 in column j and -1 in column j+1.

    R_perp = { r | D r = 0 } = Q ∩ (-Q)
    R      = Span(D_1,...,D_m) = { D^T x | x in R^m }
    Q-bar  = Q ∩ R
    v >= w  iff  v0^T r >= w0^T r for all r in Q
            iff  v^T r  >= w^T r  for all r in Q-bar
(unnumbered, recovered from PDF, book pp. 62-63). ">=" between portfolios means "is preferred to". w0, v0 = components in R. The PDF prints the first line as "{r in R^n + Dr = 0}".

    E = (1/n) * [ n-1  n-2  n-3 ...    2       1
                  -1   n-2  n-3 ...    2       1
                  -1   -2   n-3 ...    2       1
                  ...
                  -1   -2   -3  ... -(n-2)     1
                  -1   -2   -3  ... -(n-2)  -(n-1) ]                (4.5)
(recovered from PDF, book p. 65). E = n x (n-1) dual matrix of D for a single sort, with `E_i^T D_j = delta_ij`. Q-bar = { E x | x >= 0 }. If the D_j are linearly independent, E is the Moore-Penrose pseudo-inverse of D.

    Risk constraint efficient set:   w = V^-1 * sum_{j=1..m} x_j E_j,   x_j >= 0
    "Centre" point x = (1,...,1):    b_i = sum_{j=1..n-1} E_ij = (n+1)/2 - i
(unnumbered, recovered from PDF, book p. 67). V = covariance matrix. b = normal, the imputed return vector. The second line is the linear return vector. Scale so that `w^T V w = sigma^2`.

    Market neutral:  w = V^-1 * sum_j x_j E~_j
                     E~_j = E_j - ( mu^T V^-1 E_j / mu^T V^-1 mu ) * mu
(unnumbered, recovered from PDF, book p. 69). mu = vector of market weightings, with `mu^T w = 0`.

    Rebalancing cost = F(w) = sum_{i=1..n} eta_i * |w_i - w_i^0|^(k+1)
    M = M_0 ∩ { w | F(w) <= C }
(unnumbered, recovered from PDF, book p. 70). w^0 = current portfolio. eta_i = stock-specific liquidity coefficient. k = impact exponent, "k = 1/2 is a typical value". C = total cost limit. M_0 = a pre-existing constraint set.

    Q_w = { r in Q | w0^T r >= 0 }
    v >= w (with respect to mu)  iff  mu(Q_{v0-w0}) >= mu(Q_{w0-v0})
    c = integral over r in Q of r d(mu)
    Theorem 4:  w ~ v  iff  (w - v) c^T = 0
(unnumbered, recovered from PDF, book pp. 72-74). mu here = probability measure on return space with mu(Q) = 1. c = centroid. "~" = equally preferable.

    Radial symmetry:  mu(r) = f(|r|) * g(r/|r|),  g constant on the part of the unit sphere inside Q
    Example:          f(rho) = rho^(n-1) * exp(-rho^2 / 2R^2)
(unnumbered, recovered from PDF, book p. 76). R = a typical scale of return, "for example 5% per year". Its value does not matter.

    Long-short, n = 5, l = 2:  rows of D are
      ( 1 -1  0  0  0)
      ( 0  1  0  0  0)
      ( 0  0 -1  0  0)
      ( 0  0  1 -1  0)
      ( 0  0  0  1 -1)                                              (4.6)
(recovered from PDF, book p. 80).

    Index beliefs:  r_j - (mu_1 r_1 + ... + mu_n r_n) >= 0,  j = 1,...,l
                    (mu_1 r_1 + ... + mu_n r_n) - r_j >= 0,  j = l+1,...,n
                    mu_j > 0,  mu_1 + ... + mu_n = 1
(unnumbered, recovered from PDF, book p. 81). mu_j here = index weights.

    r_it = F_t + eps_it + mu_i                                      (4.7)
    Var(eps_it) = sigma_i^2 / 2
    sigma^2(F)  = (1/N) * sum_i sigma_i^2 / 2
    sigma_max   = delta * sigma_min,   sigma_min = 0.005 / sqrt(2)
(recovered from PDF, book pp. 90-91). F_t = factor return. eps_it = idiosyncratic return. mu_i = expected-return constant of stock i. delta = volatility dispersion. The log sigma_i are equally spaced.

    sigma(pi) = sqrt( sum (pi(i) - i)^2 / sum (pi_max(i) - i)^2 ) = sqrt( (1 - b) / 2 )
(unnumbered, recovered from PDF, book p. 92). pi = permutation of the true order. pi_max = full reversal. b = slope of the regression of pi(i) on i. Complete randomness is at sigma = 1/sqrt(2).

    c_{j,n} = n!/((j-1)!(n-j)!) * integral_{-inf..inf} w F(w)^(n-j) (1 - F(w))^(j-1) f(w) dw
            = n!/((j-1)!(n-j)!) * integral_{0..1} F^-1(z) z^(n-j) (1 - z)^(j-1) dz          (4.8)
    z_mean = (n - j + 1)/(n + 1),   z_max = (n - j)/(n - 1)
    Blom:   c_{j,n} ≈ N^-1( (n + 1 - j - alpha) / (n - 2*alpha + 1) )
    Authors' fit:  alpha = A - B * j^(-beta),  A = 0.4424, B = 0.1185, beta = 0.21
(recovered from PDF, book pp. 98-99). c_{j,n} = centroid component for rank j of n. f, F = standard Gaussian density and distribution. N^-1 = inverse cumulative normal.

## Key Concepts
- **Cone**: a set that contains every positive multiple of each of its points (s. 4.2.1).
- **Homogeneous belief**: an inequality with no constant term. A belief such as "the average of r1 and r2 is at least 3% annual" is not allowed (s. 4.2.2).
- **Budget constraint set**: "any bounded, convex subset of the space of all portfolios". Portfolio variance is the key example (s. 4.2).
- **Dual (polar) set**: `A* = { x | x^T y >= 0 for all y in A }` (s. 4.2.4).
- **Difference asset**: an asset that expresses one belief, for example D = S1 - S2 (s. 4.5.3).
- **Linear portfolio**: dollar-neutral, with linearly decreasing weights by rank (s. 4.5.1).
- **Reversal hypothesis**: stock prices reverse after moves caused by liquidity. The authors take it as given (s. 4.5.2).
- **Information ratio**: the annualized ratio of sample mean to sample standard deviation of daily returns (s. 4.5).
- **Volatility dispersion**: the ratio of the largest to the smallest idiosyncratic volatility in the simulation (s. 4.5.3).

## Mental Models
- **Direction, not magnitude.** Under a fixed risk budget the classic portfolio depends only on the direction of the expected-return vector. So a vector is interchangeable with its cone (s. 4.2.1).
- **Ignore what you have no view on.** Preference compares only the relevant component w0. Directions with no sign belief are left out (s. 4.2.3).
- **Normal equals imputed returns.** Each efficient point on the risk ellipsoid corresponds to exactly one normal b, and b acts as a return vector (s. 4.2.5).
- **"More often" in place of "always".** The centroid comes from relaxing certainty to "a greater percentage of the time" (s. 4.3).
- **The centroid looks like the inverse cumulative normal.** It overweights the top and bottom ranks and underweights the middle. Tails make neighbouring extreme ranks differ more than neighbouring middle ranks (s. 4.4.1).
- **Constraints and beliefs are separate inputs.** Portfolio constraints are "orthogonal" to the inequality structure on returns (s. 4.3.3).
- **Markowitz is the special case.** One belief vector D1 = rho gives the classic result (s. 4.2.4, 4.6).

## Anti-patterns
- Building portfolios from a sort with ad hoc rules, such as "buying the top decile of stocks and selling the bottom decile". The authors call existing methods "very ad hoc" with no use of volatility or correlation (s. 4.1, 4.6).
- Ignoring the covariance matrix. Unoptimized portfolios had information ratios "consistently around three or less" (s. 4.5.2).
- Using the linear profile as the "centre" of the efficient set. The authors say the centroid is "a more logical definition" and that "the difference is important" (s. 4.2.5).
- Using opposing inequalities to impose an equality. The cone then has empty interior, every point is efficient, and the theorems say nothing (Appendix A, "Need for interior").
- Discarding one of two conflicting sorts. Both hold information "that it would be suboptimal to discard" (s. 4.4.5).
- Reading the backtest as a tradable result. The authors measure no transaction costs. They note that strategies with pre-cost information ratios "as high as 5" can still lose money in actual trading (s. 4.5.2).
- Treating lag 0 or lag 1 as realistic. Lag 0 is "technically impossible" and lag 1 is "unrealistically long" (s. 4.5.2).

## Reference Tables

### Table 4.1: Information ratios, reversal strategy (recovered from PDF, book p. 88)
CRSP daily US stocks, 19 January 1990 to 31 December 2002. Each cell: unoptimized linear, unoptimized centroid / optimized linear, optimized centroid.

Lag 0:

| N | K=5 | K=10 | K=15 | K=20 | K=25 |
|---|---|---|---|---|---|
| 25 | 2.50, 2.47 / 3.21, 3.20 | 2.36, 2.40 / 2.37, 2.50 | 1.72, 1.75 / 1.84, 1.95 | 1.42, 1.45 / 1.69, 1.93 | 1.59, 1.61 / 1.63, 1.79 |
| 50 | 2.88, 2.95 / 3.53, 3.99 | 2.92, 3.10 / 3.26, 3.63 | 2.39, 2.52 / 3.03, 3.35 | 2.07, 2.16 / 2.93, 3.30 | 2.06, 2.14 / 2.79, 3.07 |
| 100 | 3.18, 3.20 / 4.26, 4.76 | 2.98, 3.12 / 3.65, 4.09 | 2.46, 2.61 / 3.54, 3.95 | 2.09, 2.17 / 3.19, 3.73 | 2.17, 2.19 / 3.10, 3.43 |
| 150 | 3.04, 3.14 / 4.79, 5.65 | 2.83, 2.99 / 4.15, 4.82 | 2.57, 2.69 / 4.13, 4.80 | 2.21, 2.33 / 3.69, 4.44 | 2.29, 2.34 / 3.53, 3.97 |
| 250 | 2.80, 2.93 / 4.88, 5.73 | 2.43, 2.64 / 3.67, 4.47 | 2.16, 2.33 / 3.61, 4.27 | 1.94, 2.10 / 3.39, 4.12 | 2.06, 2.20 / 3.13, 3.68 |
| 500 | 2.97, 3.22 / 5.82, 6.88 | 2.40, 2.72 / 4.33, 5.38 | 2.11, 2.37 / 4.31, 5.25 | 1.91, 2.19 / 4.44, 5.40 | 1.93, 2.16 / 4.31, 5.10 |

Lag 1 day:

| N | K=5 | K=10 | K=15 | K=20 | K=25 |
|---|---|---|---|---|---|
| 25 | 2.32, 2.32 / 2.39, 2.41 | 2.10, 2.15 / 1.84, 1.86 | 1.61, 1.61 / 1.35, 1.40 | 1.20, 1.24 / 1.25, 1.43 | 1.46, 1.46 / 1.35, 1.48 |
| 50 | 2.91, 2.97 / 2.58, 2.89 | 2.80, 2.96 / 2.52, 2.85 | 2.29, 2.37 / 2.46, 2.65 | 1.85, 1.90 / 2.32, 2.54 | 1.93, 1.97 / 2.30, 2.48 |
| 100 | 3.25, 3.15 / 3.07, 3.30 | 2.77, 2.84 / 2.47, 2.83 | 2.29, 2.38 / 2.62, 3.02 | 1.81, 1.85 / 2.34, 2.87 | 1.95, 1.94 / 2.38, 2.68 |
| 150 | 3.31, 3.23 / 3.55, 3.89 | 2.68, 2.73 / 3.07, 3.48 | 2.38, 2.44 / 3.24, 3.69 | 1.89, 1.98 / 2.72, 3.28 | 2.00, 2.04 / 2.75, 3.05 |
| 250 | 2.94, 2.90 / 3.41, 3.86 | 2.22, 2.32 / 2.41, 2.90 | 1.87, 1.97 / 2.35, 2.88 | 1.59, 1.69 / 2.26, 2.86 | 1.68, 1.80 / 2.10, 2.54 |
| 500 | 2.72, 2.84 / 3.55, 4.20 | 1.95, 2.15 / 2.27, 2.95 | 1.60, 1.81 / 2.47, 3.19 | 1.36, 1.59 / 2.74, 3.46 | 1.37, 1.60 / 2.71, 3.30 |

### Table 4.2: Information ratios, simulated one-factor markets (recovered from PDF, book p. 94)
500 stocks, 2000 days, mean over 50 iterations, annualized with 256 days per year. Same cell layout as Table 4.1.

| Vol disp | dist 0 | dist 0.1 | dist 0.2 | dist 0.5 | dist 0.7 |
|---|---|---|---|---|---|
| 1 | 18.1, 18.6 / 21.0, 21.4 | 18.0, 18.3 / 20.7, 21.1 | 16.9, 17.2 / 19.5, 19.9 | 9.5, 9.6 / 11.1, 11.2 | 0.0, 0.0 / 0.0, 0.0 |
| 2 | 17.3, 17.5 / 21.4, 22.0 | 17.1, 17.3 / 21.0, 21.6 | 16.2, 16.3 / 19.9, 20.3 | 9.1, 9.2 / 10.8, 11.0 | -0.1, -0.1 / 0.1, 0.2 |
| 4 | 15.4, 15.2 / 23.4, 24.3 | 15.3, 15.1 / 22.9, 23.6 | 14.5, 14.4 / 21.5, 22.1 | 8.5, 8.6 / 11.3, 11.5 | 0.0, 0.0 / -0.2, -0.3 |
| 8 | 13.3, 12.8 / 27.2, 28.8 | 13.1, 12.6 / 26.4, 27.8 | 12.7, 12.2 / 24.7, 25.8 | 7.8, 7.7 / 12.3, 12.5 | 0.0, 0.0 / 0.5, 0.5 |
| 16 | 11.6, 11.0 / 34.3, 36.8 | 11.5, 10.9 / 33.0, 35.1 | 11.2, 10.6 / 30.3, 31.9 | 6.9, 6.8 / 14.1, 14.4 | 0.0, -0.1 / -0.1, 0.0 |
| 20 | 11.1, 10.4 / 37.4, 40.4 | 10.9, 10.3 / 36.4, 39.2 | 10.6, 9.9 / 32.6, 34.5 | 6.8, 6.7 / 15.3, 15.7 | 0.0, 0.0 / -0.8, -0.8 |

## Worked Example

### A. Three assets, complete sort (s. 4.2.4, recovered from PDF, book p. 66)
Beliefs r1 >= r2 >= r3 give two belief vectors and two duals:

    D1 = (1, -1, 0)^T      D2 = (0, 1, -1)^T
    E1 = (1/3)(2, -1, -1)^T    E2 = (1/3)(1, 1, -2)^T

`D_i^T E_j = delta_ij`. The angle between D1 and D2 is 120 degrees. The angle between E1 and E2 is 60 degrees. All four lie in the plane whose normal is (1, 1, 1)^T.

### B. Computing the centroid (s. 4.3.5, Appendix B)
1. Draw x from an n-dimensional uncorrelated Gaussian.
2. Complete sort: sort the components of x into decreasing order to get y. Sorting is a series of reflections, so y is a draw from the Gaussian restricted to Q.
3. Sector sorts: sort only inside each sector. This fixes the relative weights between sectors.
4. Long-short beliefs: first correct signs so the first l components are non-negative and the last n - l are non-positive. Then sort inside each section.
5. Average many draws of y. The average estimates c.
6. For a single sort, skip the simulation and use the Blom formula with the authors' alpha. They report maximum fractional error below 0.5% for very small n.
7. For other belief structures reflections may not preserve measure. "Each new situation must be evaluated on its own."

Result for a complete sort: the centroid optimal portfolio equals the Markowitz portfolio for expected returns that are normally distributed in rank order (s. 4.3.5).

### C. The reversal backtest (s. 4.5.2)
1. Data: CRSP daily total returns, NYSE, Amex and Nasdaq, 19 January 1990 to 31 December 2002.
2. Universe: the 1000 largest stocks with at least 1000 valid days of prior data. A stock that drops out is replaced by the largest eligible stock not already held.
3. Each day, choose N stocks at random from the list. N is 25, 50, 100, 150, 200, 250, 300 or 500.
4. Sort by the negative of cumulative total return from day t-L-K to t-L-1. K is 5, 10, 15, 20 or 25 days. L is 0 or 1.
5. Estimate the covariance matrix from 2N rows of daily returns for the N stocks, up to but not including day t.
6. Form the four portfolios. Normalize each to unit ex ante risk. Do not constrain them to market neutrality.
7. Hold for one day, then rebalance at the close.

Results the authors report. Both optimized methods beat the unoptimized ones, and the gain grows "logarithmically with portfolio size". The two unoptimized portfolios are "essentially equivalent". For N = 500, K = 5, lag 0, Table 4.1 gives 2.97 (linear), 3.22 (centroid), 5.82 (optimized linear) and 6.88 (optimized centroid). The gain is weaker at lag 1 and for longer reversal periods. In monthly returns the optimized centroid wins "over 80% of the time for large portfolios, with zero lag" (Figure 4.8). The authors add that this is not a direct test of the centroid reasoning, because realized returns also depend on covariance and non-Gaussian effects.

### D. The simulated test (s. 4.5.3)
1. Generate returns from eq. 4.7. Expected returns mu_i are the ascending sort of N normal draws with "mean and variance both equal to 0.6/16 · sigma^2(F)". The authors say this gives each stock an annualized Sharpe ratio of about 0.6.
2. Vary portfolio size from 25 to 500 and volatility dispersion from 1 to 20. In a sample of 500 large US stocks the authors measured dispersion from 4.31 to 16.7.
3. Degrade the sort with permutations at distances 0, 0.01, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2, 0.25, 0.5 and 0.7071.
4. Run 2000 time steps and 50 iterations per parameter set. Covariance and true order are known exactly.

Results. Information ratios rise with volatility dispersion and with the number of stocks. They fall as permutation distance rises. The method is "highly robust to information loss". At dispersion 20 and distance 0, optimized linear gives 37.4 and optimized centroid 40.4, "an improvement of over 8%". At distance 0.5 the figures are 15.3 and 15.7, "a spread of only 2.6%". The authors' explanation: the optimized centroid maximizes exposure to difference assets, and permutations turn some of those negative. They pose a robust centroid algorithm as an open question.

## Key Takeaways
1. A sort defines a cone of consistent returns. That cone, not a point estimate, is the input.
2. Sure dominance alone leaves a large efficient set. A probability measure on the cone narrows it to one portfolio.
3. Under a radially symmetric measure the centroid fully describes the preference. Optimization then reduces to maximizing a known linear function over the constraint set.
4. For a complete sort the centroid is close to the inverse cumulative normal at equally spaced points.
5. In the authors' tests the gain comes from combining the centroid with the covariance matrix. Without covariance, centroid and linear weights perform about the same.
6. The framework accepts sector sorts, sign beliefs, index-relative beliefs, conflicting sorts and unreliable ranges.
7. The authors' own caveats: no transaction costs, unrealistic lags, and the reversal hypothesis is assumed, not tested.

## Source Defects
- The text extraction lost all Greek letters, set symbols, preference symbols, overbars and matrix layout. Every formula above came from the PDF pages. PDF page = book page + 7 for this chapter.
- Tables 4.1 and 4.2 were checked against the PDF. The decimal points were damaged in the text.
- Figures 4.1 to 4.10 are charts. Only their captions and the values the authors quote are used here.
- Inconsistencies in the source, recorded and not corrected:
  - s. 4.2.1 prints the half-space as Q-bar with "rho^T r <= 0", then calls it "the half-space Q" with inward normal rho.
  - The lemma before Theorem 4 prints "w_c^T = w_0^T c". The proof of Theorem 4 cites "Theorem 1" for a bisection step.
  - s. 4.1 says the efficient set is "less than 1/n!" of the constraint set. s. 4.2.5 says it "is 1/n!".
  - s. 4.4.1 says the Figure 4.4 vectors have "the same sum of squares". The caption says the same sum of absolute values. The text also cites "Risk restraint" for the section titled "Risk constraint".
  - s. 4.4.4: the printed belief matrix shows "mu_n" without a minus sign in the top right entry.
  - s. 4.4.5 first weights two centroids by p and 1 - p, then calls the general case "an equal-weighted combination".
  - s. 4.5.1 says the backtests "compare information coefficients". Everywhere else the measure is the information ratio.
  - s. 4.5.2 lists eight portfolio sizes. Table 4.1 shows six (no 200 or 300).
  - s. 4.5.2 says the optimized results are "always better" than the unoptimized ones. Several lag-1 cells of Table 4.1 show the reverse (for example N = 50, K = 5: 2.58 against 2.91). The N = 25, K = 5, lag 0 cell shows optimized centroid 3.20 below optimized linear 3.21.
  - s. 4.5.3 says expected returns are "in descending order" and then writes r1 <= ... <= rN.
  - s. 4.5.3 says "10 permutations" and lists 12 distances. It also says the distance lies "between zero and one" while complete randomness is at 1/sqrt(2). One paragraph writes the distance as epsilon.
  - s. 4.3 says the proofs for that section are in Appendix A. Appendix A proves only Theorems 1 and 2.

## Connects To
- `ch02-black-litterman-step-by-step` and `ch03-black-litterman-demystified`: other ways to turn views into inputs for a mean-variance optimizer.
- `ch08-robust-optimization`: s. 4.6 states that this framework includes robust optimization, with the density modelled directly.
- `ch05-choices-in-forecast-construction`: turning ranks or signals into return forecasts.
- `ch12-investments-as-bets`: difference assets as single-belief bets.
