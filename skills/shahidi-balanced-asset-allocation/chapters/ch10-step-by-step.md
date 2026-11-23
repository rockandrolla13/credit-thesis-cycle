# Chapter 10: How to Build a Balanced Portfolio: The Step-by-Step Process

## Core Idea
Build one ideal portfolio for each of the four economic climates. Balance weighted volatility *within* each one. Then balance weighted volatility *across* the four. With the four core asset classes the result is 20% equities, 20% commodities, 30% long-term Treasuries and 30% long-term TIPS.

## Frameworks Introduced
- **The four economic portfolios** (Table 10.1):

  | Environment | Ideal portfolio |
  |---|---|
  | Rising growth | Stocks and commodities |
  | Falling growth | Treasuries and TIPS |
  | Rising inflation | Commodities and TIPS |
  | Falling inflation | Stocks and Treasuries |

  Each holds two assets so that it stays agnostic on the other variable.
- **Weighted volatility**: allocation times volatility. The author's measure of exposure.
- **Step 1: balance within each economic portfolio.** Choose the split so the two assets have about the same weighted volatility.
- **Step 2: balance across the four economic portfolios.** Choose the share of each so all four have equal weighted volatility. The text sums the two weighted volatilities to get the portfolio's total. The author notes the true total is lower because of correlation benefits.
- **Final step**: for each asset, multiply its Step 1 share by its portfolio's Step 2 share. Add the two products.
- **Three factors set an asset's impact on total return**:
  1. Its economic bias.
  2. Its volatility.
  3. Its weighting in the portfolio.
  - Failure modes: ten assets with one bias. One asset far more volatile than the rest. Good assets with wrong weights.
- **Not exactly risk parity**: risk parity equalizes the *risk* of asset classes. The author says the aim should be to balance the *economic exposure*. A risk parity fund heavy in equities and credit-sensitive assets can be risk balanced and still not balanced, because those assets behave alike.
- **Diagnosing any portfolio**: assign bias, volatility and weight to each holding. Then you can predict "fairly reliably" in which environments it will beat or miss. You do not predict *when*.

## Key Concepts
- **Economic portfolio**: the ideal two-asset portfolio for one economic climate.
- **Total portfolio**: the combination of the four economic portfolios.
- **Core bonds**: the intermediate bonds in 60/40. About half as volatile as long-term Treasuries.
- **Risk parity**: weighting to equalize asset class risk, often with leverage on low-volatility assets.

## Mental Models
- The odds of each environment are about fifty-fifty against expectations. So give each similar exposure.
- "The main benefit comes in moving in the direction of improved balance." Exact weights matter less.
- Relative volatility drives the answer. The author says precise data would lead to a similar conclusion.

## Anti-patterns
- **Stopping at risk balance**: equal risk across assets with the same bias is not balance.
- **Using low-volatility core bonds as the falling-growth asset**: the 40% moves too little.
- **Leaving the rising-inflation portfolio empty**: 60/40 does this.

## Reference Tables

### Table 10.2: approximate volatility used in the exercise
| Asset class | Approximate volatility |
|---|---|
| Equities | 15% |
| Long-term Treasuries | 10% |
| Long-term TIPS | 10% |
| Commodities | 15% |

These are rounded. Tables 4.1 and 8.2 give 19% and 17% for equities and commodities.

### Table 10.5: putting it together
| Asset class | Economic portfolio | Step 1 share | Step 2 share | Product | Total |
|---|---|---|---|---|---|
| Equities | Rising growth | 50% | 20% | 10% | 20% |
| | Falling inflation | 40% | 25% | 10% | |
| Commodities | Rising growth | 50% | 20% | 10% | 20% |
| | Rising inflation | 40% | 25% | 10% | |
| Treasuries | Falling growth | 50% | 30% | 15% | 30% |
| | Falling inflation | 60% | 25% | 15% | |
| TIPS | Falling growth | 50% | 30% | 15% | 30% |
| | Rising inflation | 60% | 25% | 15% | |

Tables 10.3, 10.4 and 10.6 are images and are lost. The worked example below rebuilds 10.3 and 10.4 from the text and Table 10.5.

## Worked Example
*Step 1, within each economic portfolio.* The text gives the 50/50 rising-growth split and its 7.5% weighted volatility. The other rows follow from the shares in Table 10.5 and the volatilities in Table 10.2. They are this skill's arithmetic, not printed figures.

| Economic portfolio | Asset | Volatility | Share | Weighted volatility |
|---|---|---|---|---|
| Rising growth | Equities | 15% | 50% | 7.5% |
| | Commodities | 15% | 50% | 7.5% |
| Falling growth | Treasuries | 10% | 50% | 5.0% |
| | TIPS | 10% | 50% | 5.0% |
| Rising inflation | Commodities | 15% | 40% | 6.0% |
| | TIPS | 10% | 60% | 6.0% |
| Falling inflation | Equities | 15% | 40% | 6.0% |
| | Treasuries | 10% | 60% | 6.0% |

The text states the rule for the inflation rows: commodities are about 50% more volatile than TIPS, so TIPS get about a 50% greater weight.

*Step 2, across the four.* Totals by simple sum: 15%, 10%, 12%, 12%. The text gives the shares.

| Economic portfolio | Total volatility | Share | Weighted volatility |
|---|---|---|---|
| Rising growth | 15% | 20% | 3.0% |
| Falling growth | 10% | 30% | 3.0% |
| Rising inflation | 12% | 25% | 3.0% |
| Falling inflation | 12% | 25% | 3.0% |

*60/40 through the same lens* (from the text describing Table 10.6):
- Rising growth: equities only. High volatility and a 60% weight. High weighted volatility.
- Falling growth: core bonds only. Low volatility. The 40% "does not move the needle much".
- Rising inflation: nothing.
- Falling inflation: both assets. The whole portfolio benefits.
- Verdict: expect it to do well in rising growth and falling inflation and "very poorly" in the opposite.

## Key Takeaways
1. Four economic portfolios, two assets each, balanced by weighted volatility.
2. Shares across the four: 20% rising growth, 30% falling growth, 25% rising inflation, 25% falling inflation.
3. Result: 20/20/30/30.
4. Balance economic exposure, not asset risk.
5. Use the three-factor check on any portfolio to find its hidden bet.

## Connects To
- **Ch 9**: the arrows picture of the same logic.
- **Ch 11**: the historical record of the 20/20/30/30 mix.
- **Ch 12**: 60/40 named as a bet on growth above and inflation below expectations.
