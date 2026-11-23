# Chapter 10: Understanding Global Macro Leverage

**Author**: John Casano, Financial Diligence Networks (pp. 181-193). Partly based on a 2011 paper he wrote at NEPC.

## Core Idea
Leverage in a macro fund is built into derivatives. It is not borrowed. Gross notional leverage therefore says little about risk. The chapter gives the arithmetic for both kinds of leverage, four reasons the gross notional number misleads, and the metrics to watch in its place.

## Frameworks Introduced
- **Three types of leverage** (pp. 182-183):
  1. *Balance sheet leverage*: financing longs with the cash proceeds of short sales.
  2. *Margin leverage*: borrowing from the prime broker.
  3. *Derivatives-based leverage*: leverage "inherent in the derivative instruments". Notional is not exchanged. Cash funds only margin, collateral and option premium.
- **Three ways to state a derivatives return** (p. 183): on notional, on NAV, on margin cash. For a fund investor, return on NAV is "the most relevant". The other two show how the manager uses cash.
- **Long/short equity arithmetic** (p. 184):
  - Gross = long + short. Net = long − short. Leverage = gross ÷ 100%.
  - Cash = capital + short proceeds − longs, if the broker passes on all short proceeds.
- **Macro arithmetic** (pp. 184-185):
  - Leverage = total notional ÷ NAV.
  - **Margin-to-equity ratio** = margin posted ÷ NAV.
  - "As the overall margin requirements for the fund near the size of the fund's NAV, the portfolio becomes increasingly risky."
  - Typical figure: "the average global macro fund uses around 20% of their NAV as margin". The rest sits in government-backed cash securities at the custodian.
- **Capital utilisation ratio** (pp. 188, 191): (margin requirements + net option premium cost) ÷ total equity. The author calls it "a much more relevant metric" than gross notional for a macro fund. He also reports the objection: some positions need little margin and are very volatile.
- **Four reasons gross notional leverage is a flawed risk indicator** (pp. 188-190):
  1. **Notional is not tied to volatility.** Soros: US$100 million in Treasury bills "has a much different risk factor" than US$100 million in 30-year bonds.
  2. **Managers use leverage differently.** Relative-value books carry large notional and are "not necessarily 'riskier'" than directional books.
  3. **Leverage does not account for liquidity.** Two times notional in illiquid emerging market credit is riskier than four times in liquid G7 rates, at equal volatility.
  4. **Leverage does not account for correlations.** Long equities and long government bonds, when negatively correlated, is less risky than the notional shows. That holds only while the correlation holds.
- **Holistic risk read** (p. 191). Look at all of: VaR, DV01, capital utilisation ratio, instrument types, stress test results, liquidity profile, and the quality of the risk function.
- **Time-series rule** (p. 192): track each measure through time with one consistent method. A jump is a prompt to meet the manager.

## Key Concepts
- **Notional**: the value of the underlying that a derivative references.
- **Unencumbered cash**: fund cash not posted as margin.
- **Safety margin**: Soros's term for buying power kept above regulatory margin. He calls uncommitted buying power "not a reliable measure" because margin rates differ across investments (p. 187).
- **Option-writing return profile**: "a short truncated right tail, a concentration of positive returns just above 0% and the occasional dramatic left-tail event". The author assigns it to event-driven and statistical arbitrage, and "to some extent" to relative-value macro (p. 189).
- **Homogeneous portfolio**: the only setting where notional leverage works as a risk metric (p. 192).

## Mental Models
- Think of leverage as Soros described it: it "adds a third dimension: credit". The equity base "has to support the credit used". Quantum put equity into illiquid stocks and used leverage only in liquid "commodities" (index futures, bonds, currencies), to avoid "a catastrophic collapse in case of a margin call" (p. 187).
- Soros's cap, as quoted: "I try not to exceed 100% of the Fund's equity capital in any one market."
- Low volatility is not low risk. High volatility is not a defect if it comes from large gains and low correlation.
- A derivative can cut risk. A call option giving US$5 million of equity exposure caps the downside that US$5 million of stock does not (p. 191).
- Macro funds on exchanges "may have more control over their cash" than equity funds whose prime broker can raise margin terms (p. 186).

## Anti-patterns
- **Applying equity gross/net analysis to a derivatives book.**
- **Adding notional across funds with different strategies**: "misleading because each strategy acquires leverage differently".
- **Relying on one or two indicators.**
- **Treating risk measures as static.**
- **Neglecting cash management**: a macro fund holds most of its assets as cash, so custodian credit quality and interest rates matter more (p. 186).
- **The LTCM pole**: gross notional of 100 times equity across liquid and illiquid securities (p. 189). The author notes LTCM was a fixed income relative-value fund, not a macro fund.

## Worked Example
*1. Long/short equity* (p. 184, Table 10.1).

| | Long-only | Market-neutral | 130/30 | Case I | Case II |
|---|---|---|---|---|---|
| Long | 100% | 100% | 130% | 145% | 215% |
| Short | 0% | 100% | 30% | 65% | 100% |
| Net | 100% | 0% | 100% | 80% | 115% |
| Gross | 100% | 200% | 160% | 210% | 315% |
| Cash | 0% | 0% | 0% | 20% | 0% |
| Leverage | 1x | 2x | 1.6x | 2.1x | 3.15x |

Case I cash: 100% + 65% − 145% = 20%. Case II: 100% + 100% − 215% = −15%, so the fund borrows 15% on margin. Case II uses both balance sheet and margin leverage.

*2. Global macro* (pp. 184-185, Table 10.2). NAV US$50,000. One generic metal contract is 10,000 ounces at US$10, so US$100,000 notional. Margin is US$3,000 per contract.

| Contracts | Notional | Margin | Unencumbered cash | Leverage | Margin-to-equity |
|---|---|---|---|---|---|
| 1 | US$100,000 | US$3,000 | US$47,000 | 2x | 6% |
| 2 | US$200,000 | US$6,000 | US$44,000 | 4x | 12% |

With two contracts, a 1% price rise credits US$2,000. That is 33% on the cash outlay and 4% on NAV. The manager borrowed nothing. The second contract doubled portfolio volatility.

*3. A warning pattern* (p. 192). Margin-to-equity over four months: 10%, 12%, 9%, 25%. The author reads this as "a dramatic change in the way the portfolio was managed" and a reason to ask for a meeting.

*4. Two relative-value poles* (p. 189). LTCM at 100 times. Against it, a fund at three to five times AUM, almost only in liquid sovereign bonds, with unencumbered cash near 90%.

## Key Takeaways
1. Ask how the leverage is sourced before asking how much there is.
2. For a derivatives book, read margin-to-equity or capital utilisation, then volatility, liquidity and correlation.
3. Smooth returns with high notional can be a short-option profile.
4. Liquidity ranks above notional. "What was once liquid can dry up quickly."
5. Use one definition of leverage consistently and watch the change.

## Connects To
- **Ch 7**: risk controls in VaR, DV01 and notional terms. The note that systematic funds quote margin-to-equity.
- **Ch 9**: where each kind of leverage comes from.
- **Ch 1**: Keynes, wiped out three times by leverage.
- **Ch 12**: allocator risk statistics by strategy.
