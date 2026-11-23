# Chapter 10: Four Equations and Predictive Techniques

## Core Idea
Four equations organize the book: how returns are generated, what returns investors require, how to build a portfolio, and how active value is added. A short tour of forecasting methods follows.

## Frameworks Introduced
- **Equation 1: return identity** (10.1). Return = income + capital gain = dividend yield + dividend growth + valuation change.
  - It is an accounting identity on realized returns. Take expectations to get the dividend discount model: `E(R) = DY + g` when growth and valuations are constant.
  - Earnings form: with a fixed payout k = D/E, dividend yield = k × earnings yield and g = (1 − k) × return on equity. In steady state, expected real return equals the earnings yield. This justifies CAEY as a proxy.
  - Bonds: coupon plays the dividend. Capital gain ≈ duration × yield decline.
  - **"There is no reason for the expected capital gain to be structurally positive."** It is positive for equities. It is negative for volatility selling, credit (defaults and downgrades), emerging currency carry (depreciation) and possibly real estate (rents lag inflation).
- **Equation 2: CAPM**. `Expected return = riskless rate + beta × market risk premium`.
  - Only systematic risk is paid. Beta sets an asset's contribution to portfolio volatility.
  - Multi-factor versions add premia and sensitivities. Each factor's premium should still fit "bad returns in bad times". The regression intercept is alpha.
- **Equation 3: mean-variance optimization**. `Maximize expected portfolio return − risk aversion × portfolio variance`.
  - Unconstrained, the answer is the maximum Sharpe ratio portfolio.
  - Optimality condition: the ratio of marginal return contribution to marginal risk contribution is equal across assets.
  - Optimal weight rises with an asset's Sharpe ratio and falls with its equity market correlation.
  - The market risk premium should fall when aggregate risk aversion or expected market risk falls.
- **Equation 4: fundamental law of active management (FLAM)**, extended. `IR = IC × √N × TC`.
  - IC is forecasting skill: the correlation of signal with return. N is breadth: independent forecasts a year. TC is the transfer coefficient: correlation between the unconstrained ideal portfolio and the actual one.
  - Four times the independent bets doubles the information ratio.
  - The square root only works for uncorrelated bets. The gain arrives through lower volatility, so leverage is needed to turn it into return.
  - Applied to timing: a slow market-timing strategy has almost no breadth, so it needs far more skill.

## Predictive techniques (10.2)
| Choice | Option A | Option B | The author's guidance |
|---|---|---|---|
| Expected returns | Constant: historical average | Time-varying: starting yields, DDM | Asset class premia have moved to B. Style premia still anchor on A, discounted |
| Horizon | Long (5-10 years) | Short (1 month to 1 year) | Long: yields and valuations. Short: momentum, macro, news. Multi-decade: even value effects dilute |
| Dimension | Time series (absolute, directional) | Cross section (relative, market-neutral) | Contrarian timing is "most vulnerable to structural changes" because it needs a neutral valuation |
| Method | Regression | Portfolio sort | Near-equivalent (Pedersen 2015). Time-series regression maps to timing. Cross-sectional regression maps to selection |

- **Debiasing a historical average**: regress returns on contemporaneous valuation changes. The slope absorbs the windfall. The annualized intercept is the valuation-neutral return. It still ignores that today's yield may be below the sample average.
- **Typical component weights for 5-10 year forecasts**: 1 on current yield, 1 on historical growth, 0 on valuation change.
- **Time-series strategy return** (note 13): predictive correlation × signal strength × volatility ("IC × Z × Vol").
- **Fama-MacBeth regressions**: each period regress asset returns on characteristics. The coefficients are returns on unit-exposure long/short portfolios. Average them over time.
- **Characteristics versus covariances** (note 14): characteristics predict better. Covariances are needed for hedging and for demystifying.

## Key Concepts
- **Information ratio**: beta-adjusted active return over tracking error (Grinold-Kahn).
- **Value at risk**: the same information as volatility, stated as a loss (note 7).
- **Variance drain**: geometric mean is below arithmetic mean.
- **Rolldown, pull-to-par**: predictable bond price changes as a bond ages.
- **Machine learning** (Box 10.1): "evolutionary, not revolutionary". Limited by small data and low signal-to-noise for multi-month returns. More promise in risk management and trading costs.

## Mental Models
- Use the identity on any asset: where does the income come from, and is the expected capital gain positive or negative?
- Risk parity math: equal risk in three or four uncorrelated asset classes with similar Sharpe ratios gives 1.5 to 2 times the single-asset Sharpe ratio.
- Style math: four uncorrelated styles double the Sharpe ratio. Applying them in four or five asset classes could double it again. The author flags "perhaps a big if".
- Factor allocation equals asset allocation with the same universe and constraints. The gain comes from relaxing shorting and leverage limits.
- A risk-neutral investor who maximizes arithmetic return "would almost surely go broke".

## Anti-patterns
- **Over-constraining an optimizer** until it returns what you wanted.
- **Chasing the purest factor positions**: complex, with so much estimation error they "might not be worth the trouble".
- **Estimating long-horizon predictor weights by regression** with few independent observations.
- **Expecting machine learning to solve low expected returns**: nowcasting helps short-term trading and "would do nothing to help us collectively".

## Key Takeaways
1. A fall in required return raises realized return at the same time. This is the discount rate effect in Equation 1's last term.
2. Carry overstates expected return wherever expected capital gains are negative. Credit is one of the named cases.
3. Breadth is easier to add than skill.
4. Use strong priors, not fitted weights, for decade-ahead forecasts.

## Extraction Notes
- All four equations were typeset as images or special layout and extracted as scrambled fragments. They are restated above from the surrounding prose. The exact printed notation is lost.

## Connects To
- **Ch 2 and Ch 4**: Equation 1 in use.
- **Ch 7 and Ch 8**: Equation 2 in use.
- **Ch 11 and Ch 12**: Equations 3 and 4 in use.
- **Ch 16**: timing as a low-breadth strategy.
