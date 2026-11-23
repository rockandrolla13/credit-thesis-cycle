# Chapter 12: Investments as bets in the binomial asset pricing model
**Authors**: David Johnstone | **Book pages**: 251-263 | **Type**: METHOD (a formal equivalence between investing and betting in a one-step binomial tree. It has one numeric illustration and no data.)

## Core Idea
In the Cox-Ross-Rubinstein binomial model, any long or short position in the asset equals a conventional bet at risk-neutral odds plus risk-free bonds. A Kelly (log optimal) bettor ends with prior wealth times (q/p)(1+r). Here q is his own probability of the outcome that occurred and p is the market's risk-neutral probability. That payoff can be packaged as a "$1 Kelly bet" and replicated with calls, puts and bonds.

## Frameworks Introduced
- **Decision-theoretic derivation of the call price** (s. 12.2, eqs 12.1-12.5). Start from actual probabilities and risk-adjusted discount rates. Add the hedge ratio and no-arbitrage. The actual probability drops out.
- **Replicating investments with bets** (s. 12.3, eqs 12.6-12.7). Long one unit equals bonds plus a bet on Up. Short one unit equals short bonds plus a bet on Down. The odds are risk-neutral odds.
- **Kelly betting in a binomial tree** (s. 12.4.1, eq. 12.8). The log utility gambler splits wealth between Up and Down in proportion to his own probabilities, whatever the payoffs.
- **$1 Kelly bet / Kelly derivative** (s. 12.4.2). A derivative that costs $1 and pays (q/p)(1+r). The gambler states his probability q_u and the amount to invest.
- **Kelly profit as a proper scoring rule** (s. 12.4.2). A log utility gambler maximizes subjective expected score by nominating his true belief.
- **Replication with puts and calls** (s. 12.5, eqs 12.9-12.12). One linear condition on the call and put weights replicates the Kelly bet.
- **Options on Kelly bets** (s. 12.6, eq. 12.13). A Kelly bet is a binary asset, so an option on it prices by eq. 12.5.

## Formulas
All formulas were recovered from PDF, book pp. 253-260. The extraction lost pi, Delta, alpha, gamma, theta, omega and Omega.

Asset and call prices under actual probabilities (eqs 12.1, 12.2):

    S = [pi_u S_u + (1 - pi_u) S_d] / (1 + r_s)        (12.1)
    C = [pi_u C_u + (1 - pi_u) C_d] / (1 + r_c)        (12.2)

- S: asset price at t = 0. S_u, S_d: its t = 1 values given Up or Down.
- pi_u: the market's aggregated assessment of the actual probability of Up.
- r_s, r_c: market risk-adjusted returns on the asset and on the call.
- C_u = Max(S_u - k, 0), C_d = Max(S_d - k, 0). k: strike price.

Hedge ratio, no-arbitrage condition and call price (eqs 12.3-12.5):

    Delta = (C_u - C_d) / (S_u - S_d)                               (12.3)
    [Delta S/(Delta S - C)] r_s + [-C/(Delta S - C)] r_c = r        (12.4)
    C = [p_u C_u + (1 - p_u) C_d] / (1 + r)                         (12.5)
    p_u = [S(1 + r) - S_d] / (S_u - S_d)

- Delta shares long and one call short form a risk-free portfolio. r: the risk-free rate. p_u: the risk-neutral probability of Up.

Conventional bet (s. 12.3, unnumbered). A bet of B on event omega in Omega returns B times alpha_Omega > 1 if the event occurs and 0 otherwise.

    alpha_Omega = 1 + 1/o_Omega = 1/p_Omega,   o_Omega = p_Omega / (1 - p_Omega)

- o_Omega: odds in favour ("odds on"). p_Omega: the odds-implied probability.

Long one unit (eq. 12.6): hold S_d/(1+r) in bonds and bet S - S_d/(1+r) = [S(1+r) - S_d]/(1+r) on Up at payoff

    alpha_u = [1 + 1/o_u](1 + r) = (1 + r)/p_u = (1 + r)(S_u - S_d) / [S(1+r) - S_d]    (12.6)
    o_u = p_u / (1 - p_u)

Short one unit (eq. 12.7): hold -S_u/(1+r) in bonds and bet S_u/(1+r) - S = [S_u - S(1+r)]/(1+r) on Down at payoff

    alpha_d = [1 + 1/o_d](1 + r) = (1 + r)/(1 - p_u) = (1 + r)(S_u - S_d) / [S_u - S(1+r)]   (12.7)
    o_d = 1/o_u = (1 - p_u)/p_u

Kelly problem (s. 12.4.1, unnumbered). Wealth W, belief q_u, proportion gamma bet on Up and (1 - gamma) on Down:

    E[U] = q_u Log[gamma W (1+r)/p_u] + (1 - q_u) Log[(1 - gamma) W (1+r)/(1 - p_u)]
    first-order condition:  q_u/gamma - (1 - q_u)/(1 - gamma) = 0   =>   gamma = q_u

Kelly wealth multiplier (eq. 12.8):

    wealth at t=1 = W * (q/p)(1 + r)                               (12.8)

- q: the gambler's ex ante probability of the event that occurred. p: the market's risk-neutral probability of that event.
- Up: W(1+r) q_u/p_u. Down: W(1+r)(1 - q_u)/(1 - p_u).

Mis-stated belief (s. 12.4.2, unnumbered). Betting proportion theta of $1 as if belief were g_u when it is q_u:

    q_u Log[{theta g_u/p_u + (1 - theta)}(1+r)] + (1 - q_u) Log[{theta (1-g_u)/(1-p_u) + (1 - theta)}(1+r)]

- Maximized at theta = 1 and g_u = q_u.

Replication with options (eqs 12.9-12.12). Weights theta_c in calls, theta_p in puts, theta_rf in bonds:

    theta_c + theta_p + theta_rf = 1                                               (12.9)
    theta_c C_u/C + theta_p P_u/P + theta_rf (1+r) = (q_u/p_u)(1+r)                (12.10)
    theta_c C_d/C + theta_p P_d/P + theta_rf (1+r) = [(1-q_u)/(1-p_u)](1+r)        (12.11)
    theta_c = [q_u - p_u(1 - theta_p)] / (1 - p_u)                                 (12.12)

- P_u = Max(k_p - S_u, 0), P_d = Max(k_p - S_d, 0). k_c, k_p: call and put strikes.
- Eq. 12.9 is redundant given 12.10 and 12.11. theta_rf = 1 - (theta_c + theta_p).
- With theta_c = 0: theta_p = (p_u - q_u)/p_u. With theta_p = 0: theta_c = (q_u - p_u)/(1 - p_u).

Call on a $1 Kelly bet (s. 12.6, payoffs as printed, then eq. 12.13 for q_u > p_u and k <= r):

    C_u = Max[(q_u/p_u)(q + r) - k, 1]   if Up        (printed "(q + r)". See Source Defects)
    C_d = Max[((1-q_u)/(1-p_u))(1 + r) - k, 1]   if Down
    C = [1 + q_u(1 + r) - p_u(1 + k)] / (1 + r)                                    (12.13)

Betting payoffs of a call on a Kelly bet (s. 12.6.1, unnumbered):

    beta_u = (C_u - C_d)(1+r) / [C(1+r) - C_d] = (1+r)/p_u
    beta_d = (C_u - C_d)(1+r) / [C_u - C(1+r)] = (1+r)/(1 - p_u)

## Key Concepts
- **Risk-neutral probabilities**: "pseudo-probabilities" used to find arbitrage-free prices. They are not the market's beliefs (s. 12.1, s. 12.2).
- **Actual probabilities**: natural, physical or subjective probabilities. The market aggregates them into S.
- **Conditional independence**: C is "independent of pi given S". A shift in pi moves S, and so moves C (s. 12.2).
- **No Dutch book / no arbitrage**: the same principle, dated to de Finetti (1937) in decision theory.
- **Kelly bet / log optimal / growth optimal**: a bet that maximizes expected log wealth. The rule is myopic (s. 12.4).
- **Mental account**: a bankroll set aside for gambling, of which the gambler invests 100% in Kelly bets (s. 12.4.2).
- **Proper scoring rule**: a rule under which the forecaster does best by stating his true belief (de Finetti 1974).
- **Back and lay**: buying and selling a security on a betting exchange (s. 12.7).

## Mental Models
- Buying the asset is a bet on Up. Selling it is a bet on Down. The odds are observable because they are risk-neutral.
- At the margin, every investor is effectively risk-neutral. So all see risk-neutral prices as coherent (s. 12.2).
- The Kelly bettor's result depends only on q/p. He must give the realized outcome a higher probability than the market did.
- Markets "select for" log utility with true probabilities (Blume and Easley, as cited in s. 12.4).
- A sports bet presumably has zero covariance with other assets. Under CAPM its required return is the risk-free rate (s. 12.7).

## Anti-patterns
- Mistaking risk-neutral probabilities for the market's beliefs (s. 12.2).
- Saying pi "has no influence" on the option price. The market accounts for pi in S (s. 12.2).
- Believing risk-neutral valuation is right and neoclassical decision theory is wrong. The author calls this the most fundamental misconception (s. 12.2).
- Hedging Kelly bets across several nominal q_u values. A true Kelly bettor "would not do this". It lowers expected long-run growth (s. 12.4.2).
- Nominating q_u equal to 0 or 1. Only then can the payoff factor reach zero (s. 12.4.2).

## Worked Example
- **Bookmaker price** (s. 12.3). A price of alpha = 1.91 on Connors to beat Borg. A bet of x returns 1.91x if Connors wins and zero otherwise.
- **Out-predicting the market** (s. 12.4.1). The gambler puts 0.9 on the event that occurs. The market's risk-neutral probability is 0.6. His wealth at t = 1 is 50% higher than with riskless bonds alone.
- **Partial Kelly** (s. 12.1). Wealth of $100. Buy twenty $1 Kelly bets to invest 20% growth-optimally. Invest the rest more risk aversely.
- **Hedged portfolio** (s. 12.4.2). $20 of bets at q_u = 0.9 and $80 at q_u = 0.6. The 0.9 bets pay more given Up and lose more given Down.
- **Revealed belief** (s. 12.4.2). A log utility gambler who buys Kelly bets at q_u = 0.81 truly believes 0.81.
- **Call on a $1 Kelly bet** (s. 12.6). q_u = 0.9, p_u = 0.3, r = 0.1, k = 0.20.
  - C_u = (0.9/0.3)(1.10) - 0.2 = $3.10 given Up. C_d = $1 given Down.
  - By eq. 12.5 or eq. 12.13, the value at t = 0 is $1.48.

## Key Takeaways
- Long and short positions in a binary asset equal bets at risk-neutral odds plus bonds (eqs 12.6, 12.7).
- The Kelly bettor allocates in proportion to his own probabilities. His wealth multiplies by (q/p)(1+r) (eq. 12.8).
- The log optimal option weights are "fully determined by the rival probabilities, p_u and q_u" (eq. 12.12). Calls only or puts only can do the job.
- Log optimal investing in the asset and in any derivative of it gives the same terminal wealth (s. 12.6.1).
- The author expects the betting and finance research literatures to merge. He thinks betting market hedge funds are conceivable if betting markets offer systematic inefficiencies (s. 12.7).

## Source Defects
- The text extraction dropped every Greek symbol and most brackets. All equations above come from the PDF pages. PDF page equals book page plus 4.
- Source oddities, recorded and not corrected:
  - The Up payoff of the call on a Kelly bet prints "(q + r)". The numeric example uses 1.10, which matches (1 + r).
  - The same payoffs print a floor of 1 inside Max, and "out of the money" as C_d = 1. The text gives no reason for the floor.
  - s. 12.6 says "the price at t = 1 of the call option is C_u". Eq. 12.13 is stated for k <= r, yet the example uses k = 0.20 and r = 0.1.
  - The asset price is said to "rise exogenously" (s. 12.2).

## Connects To
- ch13-hidden-binomial-economy: generalizes this chapter's setting to an equilibrium with heterogeneous forecasts. It cites Johnstone (2006).
- ch06-bayesian-black-scholes and ch07-bayesian-option-forecasting: other option-pricing chapters in this book (link by topic only. This chapter does not cite them).
- ch01-market-efficiency-and-forecasting: betting-market efficiency literature is cited here (link by topic only).
