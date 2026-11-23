# Chapter 4: The Different Shades of Macro

**Author**: Igor Yelnik (pp. 59-76)

## Core Idea
Macro styles sit on a fader from pure discretion to pure system. Inside systematic macro, two streams are converging: value-based, relative-value GTAA and trend-following CTAs. They complement each other because they fail in different markets. A model still needs a human with a "big picture" view, and a stop-loss rule needs the same scrutiny as any other model part.

## Frameworks Introduced
- **Art, science and sport** (pp. 59-60): macro is a mix of the three. More art gives the discretionary caller of big moves. More science gives the system that makes money "without having any views about its direction". Sport is the public score.
- **The fader: six changes as you move from discretionary to systematic** (pp. 61-62):
  1. The daily process depends less on key individuals.
  2. It becomes less emotional. The model takes losses "without hesitation".
  3. More independent trading ideas. Concentrated high-conviction bets give way to a broad portfolio.
  4. Risk management becomes more elaborate. Cost: loss of the human ability to handle "an entirely new environment".
  5. Products can be customised (risk target, universe, modules on or off).
  6. Instruments become simpler and more liquid, because non-linear relationships are hard to model without losing robustness.
- **The four standard GTAA modules** (p. 64):
  1. Asset class selection: long and short global equity versus global bonds.
  2. Stock country selection: long/short country equity markets.
  3. Bond country selection: long/short country bond markets.
  4. Currency selection: long/short currency pairs via forwards.
  - The modules are largely independent. Capacity rule of thumb: "Up to fifteen developed equity markets, eight bond markets and a dozen currency pairs can be traded without limiting the capacity too much."
- **GTAA versus CTA** (pp. 63-66):

  | | GTAA | CTA / managed futures |
  |---|---|---|
  | Root | Tactical switching between cash, bonds, equities (late 1970s, 1980s) | Trend following on technical rules. Older than GTAA |
  | Stance | Contrarian, mean reversion, relative value only | Mostly directional |
  | Starting model | Valuation | Moving averages |
  | Universe | Narrower, liquid developed markets | Up to 100 markets |
  | Format | Overlay in a managed account, low target volatility. Later unconstrained | Fund or account |
  | Fails when | Strong trends. "Value traps" | Volatile, range-bound markets |
- **Risk-factor view of a position** (pp. 67-68): a position expresses "which risks one wants to bear", not only which asset will outperform. Compare strategies by (a) which risk premia they exploit, (b) how explicitly, (c) how exposure is sized over time. Long S&P 500 and long FTSE 100 are nearly the same equity premium. Long A$/Sfr and long NZ$/¥ are both carry.
- **Stop-loss test** (pp. 72-74), citing Kaminski and Lo (2007):
  - A stop-loss assumes strategy returns are *positively auto-correlated*.
  - If they are, the stop adds value. If not, it "may lead to deteriorating returns in the long run".
  - In many systematic macro strategies, "particularly GTAA", returns are not positively auto-correlated. A stop there "would thus tend to subtract value".
  - A stop is "by definition backward looking". A systematic strategy also needs a systematic re-entry rule. Slow value signals make re-entry hard: an undervalued currency is still undervalued months later.

## Key Concepts
- **GTAA**: global tactical asset allocation, a systematic, mostly relative-value macro style built for institutions.
- **Overlay**: a derivatives programme run on top of a client's portfolio, constrained by that portfolio.
- **Value trap**: a valuation signal that keeps adding against a persistent trend.
- **Anthropomorphic stop-loss**: a stop built into a system for human comfort, not for statistical reasons (p. 73).
- **Selection bias in research**: of two similar ideas, the one with the better back-test gets chosen (p. 71).
- **Super-quant product**: the author's term for a product combining top-down macro with other quantitative strategies (p. 67).
- **Rebranding**: some CTAs relabelled as GTAA to move from the hedge fund bucket to the GTAA bucket. Directional positions were recast as relative value "vis à vis cash" (p. 66).

## Mental Models
- Think of discretionary vision as acting over the life of a trade. Think of systematic vision as acting over the life of the model (pp. 70-71).
- Use the autopilot analogy: a good autopilot still needs "a talented and experienced pilot" (p. 71).
- Use the risk-factor lens to check whether two strategies are a real fit. Short-term CTA models take different risks from long-term ones and can diversify GTAA.
- When a complex strategy exceeds its past maximum drawdown, expect that at least one component is past its own worst result. That is the moment to ask whether a factor or a risk method needs replacing (p. 74).

## Anti-patterns
- **Parameter over-optimisation**: "creative" parameter choice gives a meaningless back-test. Idea-level over-optimisation is harder to spot (p. 71).
- **Modelling the last crisis**: fitting unsustainable leverage, one-off central bank interventions or liquidity squeezes "produces superb results in sample". "One-off events by definition do not recur out of sample."
- **Complexity**: "Attempts to model everything lead to too much complexity and unreliable results." Simple models miss things and are "much more robust".
- **Principals overriding the system**: if it becomes common, the investor is buying a discretionary product with key-man risk. The author's image is the fake chess automaton (p. 63).
- **Misreading a normal loss**: an investor in a 20% volatility programme who panics at a 5% monthly loss. That loss is "not that far beyond one standard deviation" (p. 73).

## Worked Example
Figure 4.1: A$/¥, 2002 to 2009 (pp. 66-67). The chart is lost. The text describes it.
- Price path: long uptrend. Elevated volatility in 2007. Sharp reversal in 2008. New uptrend in 2009.
- *PPP model* (valuation): near neutral at first. It built a growing short against the trend and lost for most of the period. It reached the 2008 collapse "very well prepared". It went nearly flat as the currency fell, then began a new short in 2009.
- *Momentum model*: long when the 20-day moving average is above the 60-day, short otherwise. It changed sign often and followed the prevailing direction.
- Correlation of the two models' returns in this sample: 0.2.
- Conclusion: combine them.

Figure 4.2: back-test start date (p. 69). One risk factor in a relative developed-market bond futures model shows an information ratio of 0.31 from 1996. Starting the same test 15 months later gives about half that. The idea did not change. The evidence did.

## Key Takeaways
1. Value and momentum fail in opposite regimes. Their low correlation is the case for combining them.
2. Test return auto-correlation before adding a stop-loss.
3. Any cut needs a defined way back in.
4. History is usually too short for statistical proof. Judgement and a causal story for why the model should earn a premium fill the gap.
5. Check a back-test by moving its start date.

## Connects To
- **Ch 3**: a practitioner's defence of tactical systems with stops. This chapter qualifies it.
- **Ch 7**: stop-losses seen by a risk manager.
- **Ch 13, Ch 14**: GTAA and risk premia in institutional portfolios.
