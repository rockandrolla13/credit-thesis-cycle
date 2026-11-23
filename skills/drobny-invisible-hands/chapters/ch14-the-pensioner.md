# Chapter 14: The Pensioner (anonymous, runs a major portfolio at one of the largest pension funds), with the author's Conclusion

Type: METHOD. This is the most systematic chapter in the book: a portfolio construction method stated from first principles by a real money manager who did not lose money in 2008. The Conclusion is the author's closing argument.

## Core Idea
Treat risk as an input, not an output. Build the portfolio with the highest return per unit of risk by spreading risk equally across as many risk premia as possible. Then set the risk level with leverage. A return target does the reverse and forces the fund into concentrated equity risk.

## Frameworks Introduced
- **Four elements that 2008 tested**: (1) passive asset mix, (2) active risk allocation, (3) risk measurement techniques, (4) risk control decisions. "Extremely few real money plans were doing any of the four very well."
- **Dollar notional thinking versus risk budgeting**: allocating by dollars makes portfolios look diversified when they are not.
  - A 60-40 stock-bond portfolio is about 90-10 in risk terms, because stocks are "approximately five times more volatile than bonds".
  - An equal risk allocation to stocks and bonds suggests about 20-80 in dollars.
  - 60-40 with private equity "is really more like 80-40 (with a hidden 20)".
  - 60-40 does well with rising growth and falling inflation. It does "very poorly" with falling growth (2008), rising inflation (the 1970s) and deflation (Japan).
- **Building the Maximum Sharpe Ratio (MSR) portfolio** (his sequence):
  1. Seek as many different sources of return as possible. Do not overexpose to any one risk.
  2. Equal-weight "most things by risk", within capacity limits. Diversify internationally.
  3. Add inflation protection. Use real return bonds and/or commodities. Real estate and equities are *not* short-run inflation hedges: they are businesses, and the central bank answers inflation by raising rates to slow demand.
  4. Apply the same rule to the active book. 60 percent of money in equities does not mean 60 percent of active risk in equity programs.
  5. Manage illiquidity "as a limited resource".
  6. Run a risk system that gives long-term risk, short-term risk and a reasonable tail estimate, and treats liquid and illiquid assets separately.
  7. "Embrace leverage." Choose the risk level you accept and lever the MSR portfolio to it.
- **Leverage and the efficient frontier ("Finance 101", Figure 14.1)**: do not accept a portfolio at its native volatility. Moving along the frontier into riskier assets is right only if you cannot use leverage and need more than the MSR portfolio returns. He puts the cost of the leverage constraint at "potentially 2 percent per annum under realistic assumptions".
- **Four types of leverage**:
  1. To hedge liabilities. Safest. Reduces risk, may not raise return. *Good.*
  2. To improve diversification: lever up low-volatility assets and lever down risky ones. Can cut risk and raise return. *Good.*
  3. To lever risky positions for more return. "Often ends in tears, and should be avoided."
  4. Off-balance-sheet hidden leverage that makes risky assets riskier, such as private equity. "Probably the most common" in real money. Its one advantage is that it is non-recourse.
- **Accounting leverage versus economic leverage**: accounting leverage shows on the fund's balance sheet (repo, derivatives). Economic leverage sits inside another entity (a company's own debt, a levered fund). A ban on the first drives risk into the second. "Leverage is not a true measure of risk."
- **Illiquidity as a short option**: entering an illiquid investment gives up the option to sell when you choose. "Illiquidity is essentially a short put option on opportunity cost." Like all short gamma strategies it earns steadily and gives it back when volatility spikes.
- **Illiquidity as a negative externality**: the department that locks money away gets the premium. The whole plan bears the cost. Without central control the result is overinvestment, a "tragedy of the commons". Rule: give managers a liquidity limit as well as a risk budget.
- **Why "alpha" failed together**: most managers earned it through persistent exposure to four things: the equity risk premium, the illiquidity premium, short volatility, and credit. All four are highly correlated "for purely theoretical reasons". Credit "is really just a slice of the equity risk premium".
- **Non-constant volatility, not fat tails**: liquid markets such as the S&P 500 "were not exceedingly 'fat' or nonnormal in 2008". They showed non-constant volatility. More look-back data is not always better. A risk system that tracks short-term changes in risk "would have gone a long way to reducing losses". He points to stochastic volatility models.
- **Marginal contribution to risk**: judge an opportunity by what it adds to total portfolio risk, not alone. (See worked example.)
- **Risk budgeting incentives**: a central risk system assigns each manager a maximum risk. Pay is based on profit earned per unit of assigned risk.
- **Constraints have costs**: the three common ones are limits on leverage, limits on permitted assets and strategies, and limits on pay for internal staff. "No matter how well-meaning, constraints generally lead to workarounds."
- **Agency risk and horizon**: a manager who can be fired on short-term results will rationally protect the job at the fund's cost. Three ways: buy options to floor interim returns, avoid negatively skewed investments, or run the optimal portfolio at lower risk. Half the risk halves the drawdowns and halves the expected excess return.

## Key Concepts
- **Risk premium**: the return paid for bearing a named risk. His method is to be "paid to play" across many of them.
- **Native volatility**: the volatility of a portfolio before leverage.
- **Lay board**: a pension board with plan members who are not investment professionals. He says it leads to "grossly suboptimal decision making".
- **Path dependency**: contribution and benefit decisions follow short-term results, so the true horizon "may be shorter than you think".
- **Passive versus active approach to the mix**: hold the best diversified portfolio and only rebalance, or tilt toward assets that look cheap. He respects both and does not claim to know which is right.
- **The 90/10 mismatch**: about 90 percent of plan risk and return comes from the asset mix, and he suggests only about 10 percent of resources go to it.

## Mental Models
- "If the return requirement were 20 percent, then you would have to put all your money in microcap stocks and just pray like hell."
- Private capital, real estate and infrastructure are "businesses packaged in an illiquid form", so they behave like equity.
- "Labeling something a hedge does not necessarily make it one."
- The growth of private equity may reflect demand for an off-balance-sheet levered asset more than a plan to earn the illiquidity premium.
- "There is no magic, only more diversified and less diversified."
- "Finance is a boring discipline." Building a sound portfolio is "a thankless, but absolutely essential task".
- If everyone adopts his model, early adopters gain as its assets reprice, and 60-40 holders are left with even lower return on risk.

## Anti-patterns
- **Starting from a return target.** Risk becomes secondary.
- **Calling 2008 a non-normal event**: this "simply seeks to abrogate responsibility".
- **A token allocation to alternatives**: "small enough to have a negligible impact on performance but just big enough to claim that progress has been made".
- **Smoothing by not marking**: illiquid assets hide losses, then leave a "mark-to-market hangover".
- **Risk systems built "more for board reporting than for portfolio management".**
- **Paying outside managers large hidden fees while capping internal pay.**
- **Selling liquid managers in a crisis because illiquids cannot be sold.**
- **Choosing trade A every time** (see below).

## Worked Example: three opportunities
| Trade | Expected return | Correlation to existing portfolio | Who picks it |
|---|---|---|---|
| A | high | high | "Everybody wants the great trade A" |
| B | medium | moderate | some |
| C | relatively low | truly uncorrelated | few, because it is boring and earns no personal credit |

His point: C is often the right choice on marginal risk. The incentive that pays for the 25 percent trade "completely neglects risk".

## Worked Example: levering the MSR portfolio (his numbers)
1. The MSR portfolio has volatility of 4 percent and excess return of 3 percent.
2. The plan is willing to run 10 percent volatility.
3. He says a three times levered MSR portfolio "is very likely to make more money for less risk than a similarly risky 60-40 portfolio". Simple scaling of his own figures gives about 12 percent volatility and 9 percent excess return at three times. The source does not reconcile this with the 10 percent target.
4. Precondition: a risk system and risk culture able to measure risk with leverage. He says most pension funds do not yet have one, so for them 60-40 is "an act of unfortunate but necessary prudence".

## Reference Tables

### Table 14.2: three largest US and Canadian public pensions (survived as text)
| | US pensions | Canadian pensions |
|---|---|---|
| AUM/wages ratio (as printed) | 0.07% | 0.15% |
| 5-year annualized return | 2.34% | 5.04% |
| 10-year annualized return | 3.05% | 5.50% |
| 10-year annualized volatility | 14.53% | 11.06% |

The row label reads "AUM/Wages" in the source. The values only make sense as wages over assets.

### "The 1% Effect" (boxed text)
- CalPERS grew from $28 billion in 1984 to a peak of $260 billion in 2007 and stood near $200 billion at end 2009.
- One percentage point more a year for 25 years would have added $55 billion.
- Spending an extra $100 million a year on talent for 25 years would still leave $46.5 billion. Current compensation cost is about $180 million a year.

## The author's Conclusion (Drobny)
- A year after the crash he asked a large public pension CIO what he would have done had he known how fall 2008 would unfold. The answer was "Good question."
- "Rationalizations and references to relative performance neither fund budgets nor honor cash liabilities."
- All real money investors should take "more of a risk-adjusted, absolute return approach".
- The 30-year tailwind of falling rates and inflation is "arguably" over, with both near zero.
- "Pension funds, not banks, are the real 'too big to fail' institutions."

## Key Takeaways
1. Convert every allocation from dollars to risk before judging diversification.
2. Count credit, illiquidity and short volatility as forms of equity risk.
3. Set a liquidity limit centrally, alongside the risk budget.
4. Look for hidden economic leverage wherever accounting leverage is banned.
5. Use a risk measure that responds to short-term changes in volatility.
6. Rank trades by marginal contribution to portfolio risk.
7. Price every constraint, including pay and governance.

## Extraction Notes
- Figure 14.1 (leverage and the efficient frontier) and Table 14.1 (football coach versus pension manager salaries) are lost. Table 14.2 survived.
- He gives no formula for the MSR portfolio and no asset-by-asset weights.

## Connects To
- **Ch 1**: the three macro principles. This chapter is the detailed version of the first.
- **Ch 3, Ch 4**: Leitner and the House also lever low-risk assets instead of concentrating in equity.
- **Ch 11**: the Equity Trader's "bucket by risk" is the same idea from the hedge fund side.
- **Ch 5**: the Philosopher's beta-plus is this chapter's illiquidity premium.
