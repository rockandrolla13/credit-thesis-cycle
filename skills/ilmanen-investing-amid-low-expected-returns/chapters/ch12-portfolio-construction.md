# Chapter 12: Portfolio Construction

## Core Idea
Mean-variance optimization (MVO) is the workhorse. Its key insight: like high Sharpe ratios and good diversifiers, and trade them off. In practice the investor's constraints on leverage and illiquidity, and judgment calls made before any optimizer runs, drive the result.

## Frameworks Introduced
- **Three top-down questions before optimizing** (12.1):
  - Q1 How risk averse are you? Elicit with paired outcomes or drawdown pictures. Lived experience teaches more: if you could not hold through autumn 2008 or March 2020, the portfolio was too risky.
  - Q2 Does mean-variance miss something crucial? ESG, liquidity needs, leverage limits, liabilities.
  - Q3 What is the acceptable universe?
- **When a higher illiquid share is warranted** (the author's list for a Canadian pension fund):
  1. Younger workforce and more distant liabilities.
  2. Less need for near-term liquidity.
  3. Greater belief in illiquidity premia or in manager selection skill.
  4. Preference for smooth reported returns.
  5. Higher peer holdings.
- **The cube** (Figure 12.1): view a portfolio by asset class, by strategy style, and by macro factor (growth, inflation, illiquidity, tail risks). The first two are investable. Macro factors are not.
- **Four macro environments**: growth up or down crossed with inflation up or down, using US data over almost 50 years.
- **"Twice right"** (Asness 2015): a macro trader must get the macro forecast right and the asset's response right, like an exacta bet.
- **MVO recipe in words** (12.2): start from equal-volatility weights, then tilt to higher Sharpe ratios and better diversifiers.
- **Two-fund separation** (Box 12.1): first find the tangency (maximum Sharpe) portfolio of risky assets. Then choose how much cash or leverage to mix with it.
- **Two classes of MVO problems** (12.3): model errors (wrong question, missing preferences) and estimation errors (bad inputs, above all expected returns). They interact: a richer model needs more estimated parameters.
- **Three fixes**: add constraints (the "lazy" fix), shrink inputs toward priors, use robust optimization.
- **Two-stage optimization**: asset owner sets asset class weights, managers optimize within. Suboptimal but simple and accountable. The same applies to splitting a pension portfolio into liability-matching and return-seeking parts.

## Table 12.2: what each weighting scheme assumes (from Scherer 2015)
| Scheme | Inputs used | Optimal if |
|---|---|---|
| Equal weighting | none | means, volatilities and correlations are all equal |
| Equal volatility scaling | volatilities | Sharpe ratios are equal and correlations are equal |
| Minimum variance | volatilities and correlations | means are equal |
| Equal risk contribution (risk parity) | volatilities and correlations | Sharpe ratios are equal |
| Maximum Sharpe ratio | means, volatilities, correlations | always, given true inputs |
| Cap weighted | none | "Theory meets facts?" |

The conditions are restated from a garbled table and the surrounding prose. Check the source before quoting formulas.

## Worked Example: the AQR Portfolio Solutions inputs (Table 12.1, Figure 12.3, Box 12.1)
Inputs, as excess returns, called "plausible forward-looking estimates ... adjusted for the low expected return world":
| Asset | Expected excess return | Volatility | Net SR |
|---|---|---|---|
| Equities | 5.0% | 15% | 0.33 |
| Fixed income | 1.0% | 5% | 0.2 |
| Illiquid alternatives | 7.0% | 10% | 0.7 |
| Alternative risk premia | 7.0% | 10% | 0.7 |

Correlations: equity-fixed income 0.0. Illiquids with equity 0.7 and with fixed income 0.2. Alternative risk premia 0.1 with each of the others.

Results for equities and fixed income only:
| Portfolio | Equity / fixed income | Expected excess return | Volatility | SR |
|---|---|---|---|---|
| Constrained, 6% volatility | 34 / 62 | 2.3% | 6% | 0.39 |
| Constrained, 10% volatility | 66 / 34 | 3.6% | 10% | 0.36 |
| Unconstrained, 10% volatility | 57 / 103, cash -60 | 3.9% | 10% | 0.39 |

- Tangency portfolio: 36% equities, 64% fixed income.
- 60/40 expected excess return: 3.4%. 100% equities: 5% at 15% volatility with a lower SR.
- Adding illiquids or alternative risk premia with no leverage beyond 10% volatility: up to 7%, holding no traditional assets. A mix of both lifts SR above 0.7.
- Fully unconstrained at 10% volatility: 9.8%, SR 0.98. It needs 159% in illiquids and alternative risk premia, funded by 25% cash and 34% short stocks and bonds.
- The author's verdict: "Few investors would consider such an extreme portfolio." He reads the result as a model error. MVO does not know investors dislike illiquidity, leverage and shorting. He adds: "you may not agree with" the inputs.

## Macro sensitivities (Figure 12.2, 1972-2020)
- Global equities: best with growth up and inflation down. Worst in stagflation.
- Global government bonds: best with growth down and inflation down.
- Commodities: the opposite of bonds.
- Five discounted style premia: much milder variation across the four environments.
- 60/40 inherits the equity pattern. Simple risk parity had a higher Sharpe ratio overall and in three of four environments. The style composite was the most stable.
- Exceptions among styles: currency carry is equity-like. Defensive industry selection is bond-like (note 10).
- Bridgewater's All-Weather route and the volatility-and-correlation route arrive at nearly the same risk parity portfolio (note 9).

## Mental Models
- Contemporaneous macro sensitivities are not tradeable unless you can forecast the regime. Build for robustness instead.
- If you do time on macro views, time major asset classes, not styles. Asset class sensitivities are more reliable.
- Unconstrained optimizers "love" private assets because of smoothed risk. Cap them first.
- 60/40 in capital is about 90/10 in risk.
- Ask how you differ from the average investor, who holds the market (Cochrane, note 2).

## Anti-patterns
- **Naive use of historical average returns** as inputs: "a recipe for trouble".
- **Letting an optimizer exploit two highly correlated assets with different Sharpe ratios**: it builds a large levered long/short.
- **Solving the wrong problem**: assets only when liabilities matter, or financial assets only when housing and human capital matter.
- **No benchmark at all**: it "all too often results in misunderstandings".

## Key Takeaways
1. Expected returns are the least reliable input. Equal weight, minimum variance and risk parity avoid them on purpose.
2. Equal weighting is robust with small samples, but it makes the in-or-out choice decisive.
3. "I am not sure which is worse, naïve use or no use of optimizers."
4. The three institutional answers of Ch 3 can be sized with this example: more equities adds little, alternatives add more only if you accept their constraints.

## Extraction Notes
- Table 12.1 survived. Table 12.2's formulas extracted as fragments. Figure 12.2's Sharpe ratio labels survive as loose numbers without reliable column mapping and are not reproduced.
- Figure 12.3 capital and risk shares are loose numbers. Only the capital weights confirmed in prose are given.

## Connects To
- **Ch 3**: the three answers to low returns.
- **Ch 5**: why illiquid risk inputs are understated.
- **Ch 10**: Equations 3 and 4.
- **Ch 13**: constraints as risk management.
