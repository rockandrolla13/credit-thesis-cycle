# Chapter 7: Bayesian forecasting of options prices: a natural framework for pooling historical and implied volatility information

**Authors**: Theo Darsinos and Stephen Satchell | **Book pages**: 151-175 | **Type**: METHOD (a Bayesian forecasting framework, followed by an empirical test on FTSE 100 index options)

## Core Idea
Historical volatility looks backward. Implied volatility looks forward. The literature usually feeds them into rival models. The authors pool them in one Bayesian model: implied volatility is the prior, historical returns are the sample (s. 7.3). They then derive a predictive density for tomorrow's option price that treats both the underlying price and its volatility as random (s. 7.3.4). On FTSE 100 calls the pooled forecast is about as good in sample, slightly better one day ahead, and much better in a trading test (s. 7.4).

## Frameworks Introduced
- **Classical framework** (s. 7.2). The price follows geometric Brownian motion. The Black-Scholes call price has one unobservable input, sigma^2. The analyst estimates it with the sample variance s^2, whose scaled value is chi-square with t - 1 degrees of freedom.
- **Two routes to volatility** (s. 7.1, after Engle and Mustafa, 1992):
  1. Direct and backward-looking: a statistic of historical returns, or an estimated volatility process.
  2. Indirect and forward-looking: invert an option pricing model on market prices to get implied volatility.
- **Bayesian pooling framework** (s. 7.3):
  1. Drift: a normal prior with hyperparameter m, estimated from the sample ("empirical" Bayes, a non-informative prior) (s. 7.3.1).
  2. Volatility: an inverted-gamma-1 prior with parameters (t's'^2/2, t'/2). s' is the implied volatility estimate. t' is the weight on it (s. 7.3.2).
  3. Sample: the historical standard deviation s from t daily returns, with weight t - 1.
- **Three-step posterior density of the option price** (s. 7.3.3):
  1. Get the posterior density of price and volatility (eq. 7.9-7.14).
  2. Apply the non-linear transformation from sigma to C_t through implied volatility (eq. 7.15).
  3. Divide by the density of the asset price given sample and prior information (eq. 7.16).
- **Predictive density of the option price** (s. 7.3.4, eq. 7.17-7.19). Rewrite the posterior as a density of the future price P_T and sigma. Transform to (P_T, C_T). Integrate P_T out with a single integration.
- **Choice of measure** (s. 7.3). Pricing uses the risk-neutral measure. Forecasting uses the objective measure, because "the predictive density is not invariant on the drift".
- **Five-agent forecasting contest with a filtered trading rule** (s. 7.4.2, eq. 7.22-7.27). See Worked Example.

## Formulas
All items are recovered from the PDF pages. The text extraction lost Greek letters and primes.

Classical framework (recovered from PDF, book pp. 155-156):

    P_t = P_0 exp[(mu - sigma^2/2) t + sigma W_t]                                         (7.1)
    C_t = C_BS(P_t, sigma) = P_t PHI(d1) - K exp(-r tau) PHI(d2)                          (7.2)
          d1 = [log(P_t/K) + (r + sigma^2/2) tau] / (sigma sqrt(tau)),  d2 = d1 - sigma sqrt(tau)
    Eq. 7.3 is the same density written for s^2. It is the likelihood of sigma^2.
    f(s | sigma, t) = 2 ((t-1)/2)^((t-1)/2) s^(t-2) / [GAMMA((t-1)/2) sigma^(t-1)]
                      * exp( - (t-1) s^2 / (2 sigma^2) )                                  (7.4)
    f(P_t | mu, sigma, t) = 1 / (P_t sqrt(2 pi t) sigma)
                            * exp( - [ln(P_t/P_0) - (mu - sigma^2/2) t]^2 / (2 sigma^2 t) )   (7.5)

    mu = instantaneous mean, sigma^2 = instantaneous variance, K = exercise price,
    r = risk-free rate, tau = T - t = time to maturity, PHI = standard normal cdf,
    s = sample standard deviation of t daily log-returns.

Priors (recovered from PDF, book pp. 157-158):

    f(mu | sigma, t, m) = sqrt(t) / (sqrt(2 pi) sigma) * exp( - t (mu - m)^2 / (2 sigma^2) )            (7.6)
    Eq. 7.7 is the same prior written for sigma^2: inverted-gamma-1 with parameters (t's'^2/2, t'/2).
    f(sigma | s', t') = 2 (t' s'^2 / 2)^(t'/2) exp( - t' s'^2 / (2 sigma^2) ) / [GAMMA(t'/2) sigma^(t'+1)]   (7.8)

    m = hyperparameter for the drift, s' = implied volatility estimate, t' = weight on s'.

Posterior steps (recovered from PDF, book pp. 159-160). Conditioning symbols are shortened:

    Eq. 7.9-7.11: multiply (7.6), (7.8) and (7.5), then integrate mu out to get f(P_t, sigma).
    f(P_t, sigma | s) = f(P_t, sigma) f(s | sigma, t) / f(s) = f(P_t, sigma, s) / f(s)    (7.12)
    Eq. 7.13-7.14: f(s) = 2 s f(s^2), where f(s^2) integrates (7.7) x (7.3) over sigma^2.
    f(P_t, C_t | s) = f(P_t, sigma = C_BS^-1(P_t, C_t) | s) |J|,  1/J = dC_t/d sigma = Vega   (7.15)
    f(C_t | P_t, s) = f(P_t, C_t | s) / f(P_t | s)                                        (7.16)

    Analytic posterior (unnumbered, book p. 160), with IV = C_BS^-1(P_t, C_t)
    and A = 2 (t' s'^2 + (t-1) s^2) t + ( ln(P_t/P_0) - m t )^2:

    f(C_t | P_t, s, t, s', t', m) = |J| (A/64)^((t'+t)/4)
                                    / [ K_{(t'+t)/2}( sqrt(A)/4 ) * IV^(t'+t+1) * (t/16)^((t'+t)/2) ]
                                    * exp( - (t' s'^2 + (t-1) s^2) / (2 IV^2) + ( ln(P_t/P_0) - m t ) / 4 )
                                    * exp( - [ ln(P_t/P_0) - (m - IV^2/2) t ]^2 / (4 IV^2 t) )

    Vega = phi( [ln(P_t / (K e^(-r tau))) + IV^2 tau / 2] / (IV sqrt(tau)) ) P_t sqrt(tau)
    K_a(.) = modified Bessel function of the second kind of order a. phi = standard normal pdf.

Predictive density (recovered from PDF, book pp. 161-162):

    Let S = t' s'^2 + (t-1) s^2,  n = t' + t,  h = T - t.

    f(P_T, sigma | P_t, s, ...) = (S/2)^((n-1)/2) / [ sqrt(pi h) P_T GAMMA((n-1)/2) ] * sigma^-(n+1)
                                  * exp( - S / (2 sigma^2) )
                                  * exp( - [ ln(P_T/P_t) - (m - sigma^2/2) h ]^2 / (4 sigma^2 h) )      (7.17)
    f(P_T, C_T | ...) = f(P_T, sigma = C_BS^-1(P_T, C_T) | ...) |J*|                                    (7.18)
    f(C_T | P_t, s, T, t, s', t', m) = integral_0^inf f(P_T, C_T | ...) dP_T                            (7.19)

    1/J* = phi( [ln(P_T / (K e^(-r (tau - h)))) + IV_T^2 (tau - h) / 2] / (IV_T sqrt(tau - h)) ) P_T sqrt(tau - h)
    IV_T = C_BS^-1(P_T, C_T). The remaining time to maturity at T is tau - (T - t).

Empirical tools (recovered from PDF, book pp. 163-170):

    C_t = e^(-r tau) [F_t PHI(d1) - K PHI(d2)],  d1 = [log(F_t/K) + sigma^2 tau/2] / (sigma sqrt(tau))   (7.20)
    MME = (1/N) sum_{i=1..N} (Chat_it - C_it) / C_it                                                    (7.21)
    MFE = (1/N) sum_{i=1..N} (Chat_i(t+1) - C_i(t+1)) / C_i(t+1)                                        (7.22)
    Trade only if (Chat_i(t+1) - C_it) / C_it > 2%                                                      (7.23)
    RT (buy)  = (100 / C_t) (C_(t+1) - C_t)                                                             (7.24)
    RT (sell) = (100 / C_t) ( - (C_(t+1) - C_t) )                                                       (7.25)
    NRT = RT - 100 * 2% = RT - 2                                                                        (7.26)
    NRT = RT - (100 / C_t) * 0.50                                                                       (7.27)

    F_t = FTSE 100 index future price (Black, 1976). Chat = estimated or forecast value. C = market price.
    Moneyness = (F_t / K) - 1. Negative means out of the money.

## Key Concepts
- **Informative prior**: the implied-volatility prior on sigma^2. It is strike- and maturity-specific, so the posterior volatility varies across strikes and maturities (s. 7.1).
- **Non-informative prior**: the drift prior, because m comes from the sample itself (s. 7.3.1).
- **Weight t'**: the analyst's chosen weight on implied volatility. The sample weight is t - 1. With t' = 1 and t = 30, the sample (weight 29) absorbs the prior (s. 7.3.2).
- **Posterior density**: used to explain today's observed option prices, the in-sample test (s. 7.4).
- **Predictive density**: the density of a not-yet-observed option value C_T given the sample (P_t, s). Used for the one-day-ahead test (s. 7.3.4).
- **MME / RME**: mean mispricing error, and the same error averaged within maturity or moneyness groups (eq. 7.21).
- **MFE / RFE**: mean forecasting error one day ahead, and the same error by time to maturity (eq. 7.22).
- **RT / NRT**: rate of return per trade on a £100 stake, before and after transaction costs (eq. 7.24-7.27).

## Mental Models
- "Bayesian statistical methods are naturally oriented towards pooling" information from separate sources (abstract).
- Treat the two volatility sources as prior and sample with explicit weights. Different weights give different point estimates. The authors call this "both a science and an art" (s. 7.3.2).
- Forecasting an option price is a joint bet on price and volatility. Only the predictive density gives the tool for that joint view (s. 7.4.2).
- Read trading profits as "a measure of economic worth and not necessarily as an attainable amount of money" (s. 7.4.2).

## Anti-patterns
- **Rival forecasts**: feeding implied and historical volatility separately into models instead of pooling them (abstract, s. 7.1).
- **Fixing tomorrow's underlying at today's close**: the practice of most out-of-sample option forecasts, per the authors (s. 7.1).
- **Plugging a marginal volatility measure into Black-Scholes**: quoted from Bauwens and Lubrano (2000) as "very dangerous", mainly near non-stationarity (footnote 6).
- **Over-complex volatility functions**: Dumas et al. (1998) find they do no better than smoothing implied volatilities, read as overfitting (s. 7.1).
- **Using the risk-neutral measure for forecasts**: objective probabilities need the objective measure (s. 7.3).
- **Reading the back-test as attainable profit**: traders told the authors the cost assumptions miss "huge spreads and extreme illiquidity" (s. 7.4.2).

## Reference Tables

### Table 7.1a: in-sample mean mispricing error (four contracts)
| Estimate | MME |
|---|---|
| Historical volatility, 15-day moving average | 0.114 |
| Historical volatility, 30-day moving average | 0.108 |
| Implied volatility, 15-day moving average | 0.060 |
| Implied volatility, 30-day moving average | 0.066 |
| Implied volatility, previous day | 0.042 |
| Bayesian, implied + historical, 15-day horizon | 0.050 |
| Bayesian, at-the-money implied + historical, 15-day horizon | 0.060 |
| Bayesian, implied + historical, 30-day horizon | 0.053 |
| Bayesian, at-the-money implied + historical, 30-day horizon | 0.072 |

Tables 7.1b and 7.1c split these errors by maturity and moneyness. They are not reproduced here.

### Table 7.2a and 7.2b: one-day-ahead forecast error (twelve contracts)
| Agent | MFE | 1 wk | 2 wk | 18 d | 3 wk | 25 d | 4 wk | 30 d | 7 wk |
|---|---|---|---|---|---|---|---|---|---|
| 1: historical volatility, 30-day | 0.231 | 0.311 | 0.370 | 0.228 | 0.209 | 0.197 | 0.094 | 0.208 | 0.234 |
| 2: implied volatility, 30-day | 0.225 | 0.406 | 0.351 | 0.257 | 0.167 | 0.140 | 0.133 | 0.193 | 0.155 |
| 3: today's implied volatility | 0.220 | 0.443 | 0.340 | 0.195 | 0.186 | 0.161 | 0.095 | 0.169 | 0.168 |
| 4: Bayesian, implied + historical | 0.196 | 0.197 | 0.323 | 0.256 | 0.173 | 0.154 | 0.124 | 0.167 | 0.173 |
| 5: Bayesian, at-the-money implied + historical | 0.198 | 0.194 | 0.321 | 0.258 | 0.174 | 0.156 | 0.138 | 0.162 | 0.180 |

### Table 7.3: mean return per trade (SD, t-ratio)
| Agent | Before costs | 2% costs | £0.50 per call |
|---|---|---|---|
| 1 | 1.4% (29.0, 0.46) | -0.6% (29.0, 0.20) | 0.4% (28.2, 0.14) |
| 2 | 2.3% (19.8, 1.11) | 0.3% (19.8, 0.15) | 1.7% (19.6, 0.83) |
| 3 | 0.4% (25.5, 0.15) | -1.6% (25.5, 0.60) | -0.4% (26.2, 0.15) |
| 4 | 6.6% (25.0, 2.52) | 4.6% (25.0, 1.76) | 5.8% (24.2, 2.29) |
| 5 | 6.2% (26.7, 2.22) | 4.2% (26.7, 1.51) | 5.4% (26.0, 1.98) |

### Tables 7.4 and 7.5: cumulative return and hit rates
| Agent | Cumulative, before costs | Cumulative, 2% costs | Cumulative, £0.50 | Profit | No trade | Loss |
|---|---|---|---|---|---|---|
| 1 | 128.4% | -138.6% | 39.9% | 52.7% | 4.4% | 42.9% |
| 2 | 212.2% | 38.2% | 156.2% | 34.0% | 37.4% | 28.6% |
| 3 | 38.8% | -123.2% | -33.7% | 30.8% | 41.7% | 27.5% |
| 4 | 603.1% | 417.1% | 531.7% | 46.2% | 34.1% | 19.7% |
| 5 | 567.5% | 354.5% | 490.7% | 49.5% | 24.2% | 26.3% |

The authors say Table 7.4 is for comparison between agents. It does not represent a cumulative return over the 8-year period.

## Worked Example
The chapter's empirical implementation (s. 7.4).

**Data.** Daily LIFFE data, September 1992 to December 2000. FTSE 100 index European call contracts. Each record has the underlying price, exercise price, expiry date, settlement price, volume, implied volatility and at-the-money implied volatility. The risk-free proxy is a UK Treasury bill of comparable maturity. The underlying is the index future, so the authors use Black's (1976) model (eq. 7.20). They keep maturities of one to seven weeks, and strikes that were close to the money at some stage.

**In-sample test (s. 7.4.1).**
1. Contracts: June 1998, March 1999, September 2000, December 2000. Moneyness ran from 5% out of the money to 8% in the money.
2. Five benchmarks put a volatility estimate into Black's model (see Table 7.1a).
3. Four Bayesian estimates use the posterior mean. They set t = t' = 15 or t = t' = 30. s' is the mean of implied or at-the-money implied volatilities over that window. m is the mean daily return over that window.
4. Result: historical volatility 10.8% to 11.4%. Implied volatility 4.2% to 6.6%. Bayesian 5.0% to 7.2%. The previous day's implied volatility wins with 4.2%.
5. The authors "cannot claim" in-sample superiority.

**Out-of-sample test (s. 7.4.2).**
1. Contracts: September 1992, June 1993, December 1994, December 1995, December 1996, June 1997, June 1998, December 1998, March 1999, June 1999, September 2000, December 2000.
2. Forecast dates per contract: 8, 15, 19, 22, 26, 29, 31 and 50 days before maturity. The dates were fixed in advance.
3. Agents 1 to 3 use Black's model with today's price for the underlying. Agent 1 uses the 30-day historical standard deviation. Agent 2 uses the 30-day mean implied volatility. Agent 3 uses today's implied volatility.
4. Agents 4 and 5 use the mean of the predictive density with 30-day windows. Agent 4 sets s' from implied volatilities. Agent 5 sets s' from at-the-money implied volatilities.
5. Forecast error: Agents 4 and 5 have the lowest MFE, 19.6% and 19.8%, against 22.0% to 23.1%. At 1 week to maturity their RFE is 0.197 and 0.194, against 0.311 to 0.443.
6. Trading rule: buy the call if the forecast exceeds today's market price, sell if it is lower. Trade only past the 2% filter (eq. 7.23). Stake £100 per trade. Close the position at tomorrow's settlement price. The risk-free rate is set to zero.
7. Trading result: Agents 4 and 5 earn 6.6% and 6.2% per trade before costs, with t-ratios 2.52 and 2.22. After costs they earn 4.2% to 5.8%. Standard deviations run from 19.6 to 29.
8. Hit rate when trading: Agent 4 about 70%, Agent 5 about 65%, Agent 1 about 55%, Agents 2 and 3 about 54% and 53% (text under Table 7.5).

## Key Takeaways
- Both densities can be evaluated "solely on the basis of observables": historical data on the underlying and reported option prices (s. 7.3.4).
- In sample, the previous day's implied volatility is hard to beat. The Bayesian estimates parallel the implied-volatility estimates (s. 7.4.1).
- One day ahead, the gap between implied and historical benchmarks narrows, and the Bayesian forecasts lead (s. 7.4.2).
- The largest forecast gain is for close-to-maturity options, 1 week (Table 7.2b).
- The authors report "a modest outperformance" on MFE and RFE and "quite substantial outperformance" in the trading test (s. 7.5).
- They "do not claim guaranteed excess risk adjusted returns" (s. 7.5).
- They did not tune the weights. Stated extensions: performance-based weights, EWMA or GARCH inputs, longer horizons (s. 7.5).

## Source Defects
- The text extraction dropped Greek letters, primes and exponents. All formulas above come from the PDF pages. PDF page = book page + 7.
- Source inconsistency: step 1 of s. 7.3.3 cites "equation (6.8)" for the volatility density. The density in question is printed as eq. (7.8).
- Source inconsistency: the Appendix labels its formulas "Equation (7.12)" to "(7.16)". Their content matches main-text densities with different numbers, for example the joint density of drift and volatility, which is eq. (7.9). The Appendix formulas were not recovered here.
- Eq. (7.21) and (7.22) print no absolute-value bars. Every reported error is positive. The file keeps the printed form.
- Eq. (7.23) prints a one-sided filter. The text says agents also sell when the forecast is below the market price.
- Table 7.3 prints positive t-ratios beside negative mean returns (for example -0.6% with 0.20).
- The chapter does not print N, the number of trades behind the t-ratios. Footnote 13 defines the t-ratio in words only.
- In eq. (7.19) the exponents are small print on the page. Verify them before use.

## Connects To
- **ch06-bayesian-black-scholes**: same authors. It derives the prior and posterior densities of the Black-Scholes price that this chapter cites as Darsinos and Satchell (2001). Chapter 6 uses generic prior parameters (lambda, theta). This chapter sets them from implied volatility.
- The chapter cites no other chapter of this book.
