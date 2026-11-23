# Chapter 13: The hidden binomial economy and the role of forecasts in determining prices
**Authors**: Stephen Satchell and Oliver Williams | **Book pages**: 265-279 | **Type**: METHOD (a theoretical one-period equilibrium model. It has illustrative numbers and no data.)

## Core Idea
The binomial option model takes the stock price as given. This chapter asks what economy could sit beneath it. Agents hold different forecasts f_i of the up state and different utility functions. In such a one-period world, "price is driven entirely by forecasts and has no connection with true probability" (abstract). The authors derive closed-form equity prices for power utility agents and for a power utility agent trading with a prospect theorist.

## Frameworks Introduced
- **General set-up** (s. 13.2). One riskless bond, one risky asset, two time-1 states with returns u and d, and u > r_f > d. Agent i holds subjective probability f_i of "up".
- **Optimism h_i** (eq. 13.2). The agent's odds of "up" divided by the risk-neutral odds. It summarizes his forecast.
- **Conditional equilibrium** (s. 13.2). The chapter solves for the equity price given the interest rate. The full problem is left to a separate paper.
- **State prices** (s. 13.2.1, eq. 13.5). The state 1 price is the risk-neutral probability discounted at the riskless rate.
- **Proposition 1** (s. 13.2.2). With increasing concave utility, the sign of the equity holding follows optimism.
- **Power utility demand and equilibrium** (s. 13.3, eqs 13.10-13.12). Equity share x_i has a closed form in h_i, risk aversion alpha_i and the three rates.
- **Proposition 2, aggregation condition** (s. 13.3). A representative agent exists if ln(h_i) = alpha_i ln(k) for all i, with k > 1.
- **Two-agent positive-price condition** (s. 13.3, Figures 13.1-13.2). A hyperbola in (k_A, k_B) bounds the belief pairs that give a positive price.
- **Mixed equilibrium** (s. 13.4, eqs 13.13-13.15). A power utility investor trades with a "prospector" who follows prospect theory.

## Formulas
All formulas were recovered from PDF, book pp. 267-277. The extraction lost pi, lambda, alpha, beta and all overbars.

Risk-neutral probability and optimism (eqs 13.1, 13.2):

    pi  = (r_f - d) / (u - d),   (u - r_f)/(r_f - d) = (1 - pi)/pi        (13.1)
    h_i = [f_i/(1 - f_i)] / [pi/(1 - pi)] >= 0                            (13.2)

- u, d: risky asset rates of return in the up and down states. r_f: risk-free rate. f_i: agent i's probability of "up".

Market clearing (eqs 13.3, 13.4). w_0i: agent i's investible wealth. x_i: his share in the risky asset. n-bar units of the risky asset and m-bar units of the bond are outstanding. S_0, B_0: equilibrium stock and bond prices. H: number of agents.

    if m-bar = 0:  S_0 = (1/n-bar) sum_i w_0i     (the bond is not identified)
    B_0 = 1/(1 + r_f)                                                      (13.3)
    1/(1 + r_f) = (1/m-bar) sum_i w_0i - (n-bar/m-bar) S_0                 (13.4)

State prices (eq. 13.5):

    state 1 price = (r_f - d) / [(u - d)(1 + r_f)] = pi/(1 + r_f)          (13.5)
    state 2 price = (1 - pi)/(1 + r_f)

Budget and first-order condition (eqs 13.6-13.9). Endowment n-bar_i shares and m-bar_i bonds. Chosen holdings n_i and m_i. c_0i: time-0 consumption. I_i = w_0i - c_0i.

    w_0i = n-bar_i S_0 + m-bar_i/(1 + r_f)                                 (13.6)
    w_1i = n_i S_1 + m_i                                                   (13.7)
    E_0i[ u_i'(w_1i) (S_1 - S_0(1 + r_f)) ] = 0                            (13.8)
    u_i'(n_i S_0(1+d) + m_i) / u_i'(n_i S_0(1+u) + m_i) = h_i              (13.9)

- E_0i takes expectations with respect to f_i and 1 - f_i.
- State-by-state form: u_i'(up wealth) f_i = lambda pi and u_i'(down wealth)(1 - f_i) = lambda(1 - pi), with lambda = u_i'(c_0i)/(1 + r_f) = E_0i(u_i'(w_1i)).

Proposition 1 (s. 13.2.2), for u_i' > 0 and u_i'' < 0:

    h_i > 1 iff n_i > 0;   h_i = 1 iff n_i = 0;   0 < h_i < 1 iff n_i < 0

Power utility (eqs 13.10-13.12):

    V_i = f_i [w_0i(1+r_f) + x_i w_0i(u - r_f)]^(1-alpha_i)/(1-alpha_i)
          + (1-f_i) [w_0i(1+r_f) + x_i w_0i(d - r_f)]^(1-alpha_i)/(1-alpha_i)          (13.10)
    x_i = (1 + r_f)(h_i^(1/alpha_i) - 1) / [u - r_f + h_i^(1/alpha_i)(r_f - d)]        (13.11)
    n-bar S_0 = sum_i I_i x_i                                                           (13.12)

- alpha_i: agent i's coefficient of risk aversion. The solution for x_i does not depend on w_0i.

Position limits (s. 13.3), independent of alpha_i:

    lim x_i as h_i -> 0        = -(1 + r_f)/(u - r_f)
    lim x_i as h_i -> infinity =  (1 + r_f)/(r_f - d)

Proposition 2 condition (s. 13.3):

    ln(h_i) = alpha_i ln(k) for all i,  k a constant > 1

Two agents A and B, with k_i = h_i^(1/alpha_i) (s. 13.3). Net demand and the positive-price condition:

    x = (1+r_f)(k_A - 1)/[u - r_f + k_A(r_f - d)] + (1+r_f)(k_B - 1)/[u - r_f + k_B(r_f - d)]
    x > 0  <=>  (k_A + [1/(2 pi) - 1]) (k_B + [1/(2 pi) - 1]) > 1/(4 pi^2)

Prospect theorist (s. 13.4, eqs 13.13, 13.14):

    V_i = f_i [x_i w_0i(u - r_f)]^(1-alpha_i)/(1-alpha_i)
          - lambda_i (1-f_i) [-x_i w_0i(d - r_f)]^(1-beta_i)/(1-beta_i)
    0 = [x_i w_0i(u-r_f)]^(-alpha_i) f_i (u-r_f) - lambda_i [x_i w_0i(r_f-d)]^(-beta_i) (1-f_i)(r_f-d)    (13.13)
    x_i = (h_i/lambda_i)^(1/(alpha_i-beta_i)) * (1/w_0i) * (r_f-d)^(beta_i/(alpha_i-beta_i)) / (u-r_f)^(alpha_i/(alpha_i-beta_i))   (13.14)

- alpha_i, beta_i: risk aversion coefficients for gains and for losses. lambda_i: general loss aversion parameter.

Mixed equilibrium price, investor 1 power utility, investor 2 prospector (eq. 13.15):

    n-bar S_0 = w_01 (1+r_f)(h_1^(1/alpha_1) - 1) / [u - r_f + h_1^(1/alpha_1)(r_f - d)]
                + (h_2/lambda_2)^(1/(alpha_2-beta_2)) (r_f-d)^(beta_2/(alpha_2-beta_2)) / (u-r_f)^(alpha_2/(alpha_2-beta_2))   (13.15)

## Key Concepts
- **HARA utility**: Hyperbolic Absolute Risk Aversion class, defined in footnote 1 by -U''(w)/U'(w) = 1/(A + Bw) (recovered from PDF, book p. 265).
- **Optimism**: h_i. An optimist has h_i > 1, a pessimist 0 < h_i < 1.
- **"Martingale" / risk-neutral in beliefs**: h_i = 1. This agent holds no equity (Remark 1, s. 13.3).
- **Investible wealth**: w_0i, strictly I_i after time-0 consumption.
- **Representative agent**: one investor with aggregate investible wealth whose demand has the form of eq. 13.12.
- **One-fund separation**: under Proposition 2, all investors hold the same proportion of equity.
- **Prospector**: the authors' term for an investor who follows prospect theory. He values gains and losses against a benchmark of all-cash investment.
- **Mixed equilibrium**: agents' utility functions come from different families.

## Mental Models
- A Bernoulli asset lets one number describe an agent's whole belief. That makes heterogeneity easy to read (s. 13.1).
- Price depends on the cross-section of investible wealth, optimism and risk aversion (eq. 13.12). True probabilities do not enter.
- Moving wealth from optimists to pessimists lowers the price, and conversely (s. 13.3).
- Higher risk aversion raises the price if the agent is a pessimist and lowers it if he is an optimist (s. 13.3).
- Wealth scales the power utility investor's demand. It has no impact on the prospector's demand (s. 13.4).

## Anti-patterns
- Drawing strong conclusions about risk aversion from representative-agent models. With heterogeneous beliefs, "an infinity of representative risk-aversion levels can be observationally equivalent" (s. 13.3).
- Giving a power utility agent normally distributed beliefs. That implies a positive probability of negative wealth and undefined utility (s. 13.1).
- Assuming that more optimism for everyone raises prices. With a prospector present it "does not necessarily raise or lower prices" (s. 13.4).
- Combining risk-neutral utility with non-risk-neutral beliefs. Such an agent wants to go "infinitely long or short" (Remark 1).
- Accepting the aggregation condition as natural. It requires the most risk-averse agents to be the most optimistic, which "does not sit well with our intuition" (s. 13.3).

## Worked Example
- **Position bounds** (s. 13.3). With "typical annual values" u = 10%, d = 0%, r_f = 5%, the maximum long and short positions are "± 2100%" of investible wealth.
- **Loss is capped** (s. 13.3). A maximally bullish agent who meets a down move ends with w_1i = w_0i(1+r_f) + w_0i(d - r_f)(1+r_f)/(r_f - d) = 0. Losses stop at initial investible wealth.
- **Two-agent hyperbola** (s. 13.3). Two agents have equal wealth and differ only in k_i. The boundary passes through (1,1) for every pi.
  - Figure 13.1, pi = 0.9: pessimism is "relatively hard to accommodate". The plotted boundary stays above about k_B = 0.6 across the k_A range shown (read from the figure).
  - Figure 13.2, pi = 0.1: the boundary falls to about k_B = 0.2 at k_A = 2 (read from the figure). An optimist accommodates pessimism more easily.
- **Prospect theory parameters** (s. 13.4). Printed "typical values": alpha_i = beta_i = .12 and lambda_i = 2.25.
- **Aggregation choices** (Remark 3). If alpha equals the sum of the alpha_i, h must equal the product of the h_i. If alpha equals the average alpha_i, h equals the geometric mean of the h_i.

## Key Takeaways
- In this one-period economy the equilibrium equity price is a function of forecasts, wealth, risk aversion and rates. True probability plays no part.
- Proposition 1: optimists hold equity long, pessimists short, and agents with risk-neutral beliefs hold none.
- Power utility gives closed-form demand (eq. 13.11) with finite position limits.
- A representative agent exists only under a restrictive link between optimism and risk aversion (Proposition 2).
- The prospector never takes an outright short position if lambda_i is non-negative (s. 13.4).
- Hwang and Satchell (2003): alpha_2 > beta_2 is necessary and sufficient for an internal optimum. Then prospector optimism raises prices and loss aversion lowers them (s. 13.4).
- The authors want better data on cross-sectional beliefs. Today "consultants' surveys of client optimism" measure them only roughly (s. 13.5).

## Source Defects
- The text extraction lost all Greek letters, overbars and exponents. All formulas come from the PDF pages. PDF page equals book page plus 3 in this chapter.
- The HARA footnote on book p. 265 is damaged in the text. The definition above comes from the PDF page.
- Figure values are read from small plots and are approximate.
- Source inconsistencies, recorded and not corrected:
  - s. 13.4 says the power utility demand is "given by equation (13.9)". The repeated formula is eq. 13.11.
  - s. 13.4 places eq. 13.10 in "Section 13.2". It appears in s. 13.3.
  - s. 13.4 says separate constant relative risk aversion yields "constant absolute risk aversion overall". The chapter does not derive this.
  - Proposition 2 says all investors must be optimists. The two-agent example then allows one pessimist. These are different cases, but the chapter does not say so.
  - The chapter prints alpha_i = beta_i = .12 as typical prospect theory values. It is recorded as printed.
- The Appendix derivation of the state-by-state conditions is not reproduced.

## Connects To
- ch12-investments-as-bets: this chapter generalizes Johnstone's binomial setting and reuses the risk-neutral versus subjective probability split.
- ch11-optimal-forecasting-horizon: same authors, on how a single investor uses forecasts.
- ch01-market-efficiency-and-forecasting: the link between forecasts and prices (link by topic only. This chapter does not cite it).
