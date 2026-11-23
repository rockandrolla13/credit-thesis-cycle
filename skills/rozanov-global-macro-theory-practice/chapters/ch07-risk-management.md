# Chapter 7: Risk Management in Global Macro Funds

**Author**: Barry Schachter (pp. 119-138)

## Core Idea
Risk management in macro is a partnership with the risk taker, not only a control function. The chapter gives ten principles, the mechanics of risk controls, and a defence of VaR as a tool whose limits tell you when to use it. It is the most method-dense chapter in the book.

## Frameworks Introduced
- **Independence versus partnership** (p. 120): full independence buys control and costs an "adversarial relationship" that cuts the two-way flow of information. The author wants "significant enforcement authority" plus a commitment to improve risk-adjusted performance.
- **Ten principles of global macro risk management** (pp. 120-125):
  1. **Only take those risks that are central to the view being expressed.** "Even a star alpha generator may be correct only 55% of the time", so unintended risks hurt.
  2. **Do not expose a position to "unknown unknowns" that are affecting price.** Price behaviour "inconsistent with the flow of market news is a signal to hedge, reduce or eliminate".
  3. **Whatever can go wrong probably will go wrong.** Structure a known, limited downside, for example with long options. Set "an explicit exit strategy before putting on the trade". Inputs to the exit: position size, risk tolerance, conviction, volatility, and possibly chart levels.
  4. **Trading liquidity is a fickle friend.** Avoid "roach motels". If you must use one, think hold-to-maturity. Watch crowding.
  5. **The best hedge is to exit the position.** A late hedge in a related market adds basis risk. Lift it as soon as a direct exit or direct hedge is possible.
  6. **Beware of changes in risk regimes.** Shifts come from "positive feedback effects" among participants. They change correlations and volatilities. Monitor precursors.
  7. **Diversification is about the number of risk factors, not individual positions.**
  8. **Good fences make good risk takers.** Agreed guidelines alert a trader who leaves their usual parameters.
  9. **Do not be dogmatic.** Do not put "too much faith in any model or any set of historical observations". Build to survive inevitable errors.
  10. **Everyone is a risk manager.** The risk taker is the front line.
- **Risk control menu** (pp. 125-127):
  - Portfolio VaR. The author's typical figure: maximum 95th percentile one-day VaR "around 3% of allocated capital".
  - Notional limits, "especially in the case of credit instruments, where the principal is at risk".
  - Credit limits by rating category or by range of market credit spread.
  - Price sensitivities: maximum price impact per basis point for rates.
  - Equity: net or gross market value, beta, factor exposure.
  - Volatility: aggregate vega by asset class.
  - Relative value trades: recognise that different tenors carry different risk factors (2-year versus 10-year Treasuries, 3-month versus 15-month Brent).
  - Controls are tailored to each manager's markets, holding period, number of positions and style. "No positive relationship exists between the level of detail and the degree of effectiveness."
  - Waiver rule: the risk taker asks for a temporary waiver. If they do not ask and the level is exceeded, the risk manager can force adjustments.
- **Absolute loss control versus drawdown control** (pp. 127-128):

  | | Absolute loss | Drawdown |
  |---|---|---|
  | Measure | Maximum loss on capital over a set interval | Peak cumulative return minus current cumulative return |
  | Action at limit | Halt. Close all positions | Halt |
  | Implied view | Losses of capital are capped | "Profits earned by the risk taker are owned by the fund" |
  | Cost to return | Lower | Higher. It deters adding risk after gains, and it squeezes high-volatility strategies |
  - A manager who breaches maximum loss "typically is not allowed to resume trading". Exceptions return with much less capital and tighter controls.
  - Manage the halt dynamically. Large books take time to unwind.
- **Realist versus instrumentalist view of models** (pp. 129-131):
  - Realist: a model should describe the world as it works. On that test VaR is "flawed".
  - Instrumentalist: a model is a tool of convenience. The question is whether it is useful within an agreed scope. The onus is on the risk manager, not the model.
  - VaR's scope: a loss "likely to be exceeded with some small chance". It "does not explain" tail events. It gives "very reasonable risk forecasts in ordinary market environments".
  - Common sense is "itself model-based". It over-fits history too and carries cognitive bias. Use both.
- **Scenario stress test: five construction steps** (pp. 132-133):
  1. Choose the economic scenario. Subjective. For macro it must be global.
  2. If hypothetical, pick the core markets where the impact is most immediate. If historical, fix the start and end dates.
  3. Set the factor shocks for the core markets, with input from economists and strategists.
  4. Propagate to non-core factors, for example through betas. Decide first whether no-arbitrage relations hold and whether spreads may change sign.
  5. Re-price every instrument and scale by position size.
- **Reverse stress test** (pp. 134-135): search for the set of shocks that gives the largest portfolio loss, under plausibility constraints. Origin: maximum loss optimisation, 1995. Follow with a perturbation analysis. The author rates it poorly suited to macro because the book turns over fast.
- **Tail-risk strategy design** (pp. 135-136): pick instruments that react predictably across many crises. The author's flight-to-safety list: short equity indexes, long credit protection, long volatility, long safe-haven currencies (US$, ¥, Sfr), long risk-free sovereign debt. Single stocks and single bonds are unsuitable.

## Key Concepts
- **Risk appetite**: the fund's tolerance for risk, which the loss and drawdown controls enforce.
- **Liquidity black hole**: large speculators exit the same crowded trade at once (p. 122).
- **VaR-limit spill-over**: a volatility spike in one market raises portfolio VaR and forces sales elsewhere. Many desks do it together (p. 123).
- **Factor shock**: the assumed change in a core market price in a stress scenario.
- **Availability bias**: overestimating a rare event's probability just after it happens (p. 135).
- **Margin-to-equity**: how systematic funds state leverage. Discretionary funds state it as a percentage of assets (p. 137).

## Mental Models
- Use the crowding rule: in macro "the number of unique big picture views is relatively small, while the number of risk takers is large". The author's usual indicator is the CFTC weekly report of large speculative positions.
- Think of maximum loss as "a buoy marking the safe channel". It is known in advance and must never be crossed.
- Think of a macro fund as its own tail hedge. It is nimble, liquid, and can trade the trends that follow a crisis. The author says the logic for a dedicated tail programme inside a macro fund "is not strong". Trend followers can stand in for tail hedges in an investor's portfolio, with less convexity.
- Weigh each model's output by its relevance to present conditions.

## Anti-patterns
- **Instrument drags in an unrelated risk**: see the worked example.
- **Counting positions as diversification**: Mexican peso/US dollar correlates "extremely" highly with the S&P 500, which correlates highly with emerging equity indexes. In the author's experience, even very large macro portfolios have "more than half of their volatility explained by significantly fewer than 10 risk factors" under principal component analysis (p. 124).
- **Old historical scenarios**: replaying 1987 "may be more misleading than meaningful".
- **Reading one stress number as robust**: a scenario says nothing about nearby shock values.
- **Buying tail insurance after the event**: "prohibitively expensive".
- **Replacing models with common sense**, or relying on either mechanically.
- **Prescriptive regulation** of which model to use and how (p. 131).

## Worked Example
*1. Principle 1, the Euribor leg* (p. 121).
- View: short-term risk-free rates in the US and Europe will diverge.
- First expression: three-month US dollar OIS swap versus three-month Euribor future.
- Problem: Euribor moves with the ECB policy rate and also with "liquidity and credit conditions in Europe's interbank market". The view can be right and the trade can still lose on interbank stress.
- Fix: replace the Euribor leg with an EONIA swap.
- General rule: check each leg for factors that are not the thesis.

*2. A tail-like trade inside the alpha book* (pp. 136-137). In 2011 many macro funds bearish on the eurozone were long Danish krone against the euro. The krone was pegged to the euro. A break-up was expected to end the peg with krone appreciation. Low volatility, low carry cost and asymmetric payoff made it "an attractive component of a longer-horizon bearish euro trade".

*3. The limit of imagination* (p. 134). The March 2011 Japan earthquake, tsunami and nuclear accident. To the author's knowledge no risk manager had simulated that combination.

## Key Takeaways
1. Write the exit before the entry.
2. Unexplained price action is a reason to cut, even on an existing position.
3. Measure diversification in factors.
4. Choose between a loss limit and a drawdown limit knowingly. The drawdown limit costs more return.
5. Use VaR for ordinary conditions and aggregation. Use scenarios for imagined breaks. Trust neither alone.
6. A stress test is subjective at every step. Two managers will get two answers for "euro break-up".

## Connects To
- **Ch 1**: the Commodities Corporation 50% rule is an absolute loss control.
- **Ch 2**: a manager's view of the same controls. Both authors prefer cutting to hedging.
- **Ch 4**: the statistical case for and against stop-losses.
- **Ch 6**: KIKOs as a liquidity illusion.
- **Ch 10**: leverage measures.
