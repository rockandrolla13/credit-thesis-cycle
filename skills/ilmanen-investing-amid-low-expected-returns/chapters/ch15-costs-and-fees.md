# Chapter 15: Costs and Fees

## Core Idea
The goal is to maximize risk-adjusted net return, not to minimize costs or fees. Market beta is nearly free and belongs to the asset owner. Uncorrelated return is scarce and commands a fee in proportion to its active risk.

## Frameworks Introduced
- **Annual trading cost** (15.1): cost per amount traded × annual turnover. Example: 200% turnover at 20bp impact costs 40bp a year.
- **Implementation shortfall** (Perold 1988): market impact (pre-trade price to traded price) plus the opportunity cost of pre-trade drift between model time and trade time.
- **Three reasons naive cost subtraction understates a strategy**:
  1. Multi-factor portfolios net trades across factors.
  2. Managers can trade only part of the way toward the cost-free optimum.
  3. A fast signal with negative net alpha can still be used to delay trades that slow signals call for.
- **Alpha decay versus cost trade-off** (Figure 15.1): maximizing gross return trades too fast. Minimizing cost trades too slow. Maximize expected net return.
- **Concave price impact**: impact rises with trade size, as a share of daily volume, "at a decreasing rate" for patient, liquidity-providing traders. Linear models overstate costs.
- **Fair fee principle** (15.2): "investors should not pay alpha fees for beta performance". Fees should be proportional to active risk, with near zero for beta.
- **Fee differences reflect two things**: the perceived beta/alpha split, then the perceived quality of the beta-adjusted alpha.
- **Asness Law**: "no investment product is so good that high enough fees cannot make it a bad investment."
- **Split of gross alpha**: Berk-Green (2004) gives 100% to skilled managers. With managers also competing for capital and skill uncertain, the split is more even (Garleanu-Pedersen 2018).

## Worked Example: comparing a long-only style fund with a market-neutral ARP fund
1. Long-only equity fund: market risk at about 15% volatility plus 2% active risk from style tilts.
2. It charges nothing for beta and 30bp for the 2% active risk.
3. A market-neutral ARP fund targets 10% volatility with the same styles. That is five times the active risk.
4. Fair fee for the ARP fund: 5 × 30bp = 150bp.
5. If the ARP fund is on offer at 120bp, it is the better deal despite the higher headline fee.
6. Corollary: a zero-beta manager with 10% active risk should be indifferent to halving its fee if it halves all positions.
The same logic applies to traditional active funds, hedge funds and private equity, which all bundle beta with other exposures.

## Numbers
| Item | Value | Source in text |
|---|---|---|
| Mean implementation shortfall, all equity trades, 1998-2016 | 11bp, of which 10bp market impact | Frazzini-Israel-Moskowitz (2018), $1.7trn of live trades, 21 markets |
| Value-weighted shortfall | 16bp (15bp impact) | same |
| Market impact, large cap / small cap | 9bp / 19bp | same |
| Impact measured against VWAP | 4.5bp, an understatement for a large trader | same |
| Excess fees spent trying to beat passive US indices, 1980-2006 | 67bp a year | French (2008) |
| Passive equity fund fees, 2010s | 0-30bp | 15.2 |
| Active equity fund fees | 30-80bp | 15.2 |
| Institutional price of equity beta | at most 10bp | 15.2 |
| Hedge funds, all-in | 2-3% | 15.2 |
| Private equity funds, all-in | near 5% | 15.2 |
| Negotiated hedge fund terms | 1-1.5% fixed plus 10-15% performance | 15.2 |

## Key Concepts
- **Market impact**: the dominant cost for large investors in listed assets.
- **Alpha decay**: how fast a signal's expected edge fades. Momentum decays faster than value.
- **VWAP**: volume-weighted average price.
- **2+20**: the classic hedge fund fee, traced to A.W. Jones in the 1940s.
- **Closet indexing**: bulk beta sold with a thin layer of active risk at an active fee.
- **Tax-loss harvesting** (Box 15.1): high-turnover strategies realize gains and also create losses to harvest. The general tax goal is deferral.

## Mental Models
- A private equity fund that turns over twice a decade may still have higher annual trading costs than a large-cap momentum strategy.
- Low turnover is not a virtue by itself. Ask whether the manager simply cannot run fast-decay strategies well.
- Blending diversifying returns with market risk lowers the headline fee. It does not make the fee fairer.
- Hedge fund fees track recent performance, not volatility or diversifying power. That shows more belief in persistence than the evidence supports.
- Private equity investors pay for a "cocktail": perceived alpha, illiquidity premium, high beta, embedded leverage and the smoothing service.
- Trade toward a moving target: "skating where the puck is going" (Garleanu-Pedersen 2013).

## Anti-patterns
- **Fee minimization**: pushes investors to cash and index funds, and invites managers to sell structured products with hidden costs.
- **Subtracting standalone cost estimates from each factor**.
- **Comparing turnover or costs across managers without the alpha earned**.
- **Using VWAP benchmarks for large orders**.
- **Assuming co-investments or direct deals improve net returns**: "lemons risk" and weaker in-house teams offset fee savings.

## Key Takeaways
1. Institutional equity trading costs are lower than older academic estimates when execution is patient.
2. Value and momentum survive real costs and scale better than size. Short-term reversal is the most cost-constrained.
3. Fee pressure has hit mutual funds and hedge funds. It "has not yet had much bite" in private equity.
4. "Bulk beta is abundant and cheap, while perceived alpha is scarce and costly."
5. The author's verdict on investor choices: they "appear more faith-based than evidence-based".

## Extraction Notes
- Figures 15.1 to 15.3 are images. Figure 15.3 (CEM fee medians by asset class) is not recoverable.
- The trading cost study uses the data of "a large institutional money manager (who could it be?)", meaning the author's employer.

## Connects To
- **Ch 5**: private equity fees and the smoothing service.
- **Ch 7**: alpha, beta and demystifying.
- **Ch 9**: trading costs in backtest discounts.
