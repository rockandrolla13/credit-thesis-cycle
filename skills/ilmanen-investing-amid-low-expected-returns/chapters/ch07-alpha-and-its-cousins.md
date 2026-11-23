# Chapter 7: Alpha and Its Cousins

## Core Idea
Alpha is the return left after all systematic exposures are removed. It is scarce, hard to define, and often sold bundled with beta. Use factor regressions to see what a manager's return is made of before paying for it.

## Frameworks Introduced
- **Three meanings of "alpha"** (7.1):
  1. Practitioner: active return, the plain difference from a benchmark.
  2. Academic one-factor: the CAPM regression intercept. It penalizes above-market beta.
  3. Multi-factor: the intercept after market and style factors.
  "There is no unique measure of alpha for any fund/strategy."
- **Alpha morphs into alternative risk premia**: proprietary signals become widely known. It happened to value, momentum and carry. Alternative risk premia are still "alpha to you" if you hold little of them.
- **Two dimensions of the pyramid** (7.2): market directionality and uniqueness. ARP is alpha-like in being market-neutral and beta-like in being widely known.
- **The quant trade-off**: "overfitting risk in proprietary alpha" against "overcrowding and obsolescence risks in ARP".
- **Sharpe's arithmetic** (1991): active managers hold the market collectively, so they must underperform passive after costs. Two challenges: passive also trades, and direct investors (over half of global equities) are an unmeasured, plausible source of negative alpha.
- **Efficiently inefficient markets** (Pedersen): enough inefficiency to pay for active effort, and no more.
- **Samuelson's dictum**: markets may be micro efficient and macro inefficient.
- **Demystifying regression** (7.3): regress a manager's or industry's returns on market and style factors. Each factor's contribution is its beta times the factor's full-sample premium. The intercept is alpha.

## Worked Example: the hedge fund industry, 1994-2020 (Table 7.1, 12-factor regression)
1. Excess return over cash: 4.3% a year.
2. Market risk premia: 2.0%. Mostly equity beta. Simple equity correlation 0.77, plus correlation with last month's equities from stale pricing.
3. Alternative risk premia: 1.6%. Mainly momentum stock selection and trend in futures. Also put selling, tech sector and small caps.
4. Unexplained alpha: 0.7%.
5. One negative loading: quality stock selection, costing about 0.3% a year.
Industry equity beta is near 0.3 and correlation near 0.8 (7.1).

Superstars (Figure 7.3, Brooks-Tsuji-Villalon 2018):
- Buffett (Berkshire, 1977-2016): more return from market, quality and low-risk tilts than from value. Some alpha remains.
- Soros (Quantum, 1985-2004): "more than fully explained" by a handful of factors, mainly trend. Regression alpha is negative.

## Key Concepts
- **Paying alpha fees for beta performance**: a single fee on a blend of alpha and market exposure.
- **Alpha decay**: measured alpha fell over time for mutual funds, institutional funds, hedge funds and private equity.
- **Dusty corners**: small and micro caps, emerging and frontier markets, less liquid fixed income, private assets. More alpha dispersion, higher fees.
- **Differentiated declines**: weak markets with wide stock dispersion. Stock pickers tend to do better then.
- **Systematic versus discretionary** (Box 7.1): neither wins on raw returns. Active-return correlation is about 0.15 within each group and about 0.05 across.

## Numbers
| Item | Value | Where |
|---|---|---|
| Passive share of all global equities | 18% ($12trn of $68trn) | note 3 |
| Passive share of delegated equities | 38% | note 3 |
| Passive share of US mutual fund assets, 2007 to 2021 | equities 19% to 50%. Fixed income 7% to 31% | 7.1 |
| Active systematic equity share | under 10% after doubling in the 2010s | Box 7.1 |
| Correlation among active fixed income managers, and with equities | 0.6-0.7 | Figure 7.2 |
| Interquartile range of manager returns | VC and buyout ±10%. Long/short equity ±3%. US equity funds ±2%. US bond funds ±1% | note 12 |
| Hedge fund industry size | perhaps $5trn, not $3trn | note 9 |

## Mental Models
- Active fixed income managers beat benchmarks in the 2010s because they were long credit and so long equity risk. Active US equity managers lagged because their usual tilts (cash, small caps, non-US) all hurt. Neither result should be expected to persist (note 15).
- Use a poker test for a market: "You'd rather play with patsies than with sharks."
- Wide dispersion in private assets cuts both ways. Alpha "can also be deeply negative".
- Complexity, discretion or tactical trading does not make a strategy alpha.

## Anti-patterns
- **Assuming your managers have alpha**: persistence evidence is "modest at best".
- **Counting hedge fund return as alpha** when most is equity beta.
- **Trusting database alphas**: survivorship and selection biases. Barth et al. (2021) cut the other way: non-reporting funds did better.
- **Preferring new proprietary signals because their backtests look better**: shorter history and more degrees of freedom guarantee that.

## Key Takeaways
1. Net alpha for active mutual funds is negative in over half a century of studies. Other delegated groups show positive but decaying active returns.
2. The passive share is far from a level that would hurt price discovery.
3. Private equity alpha persistence disappeared after the late 1990s. It still held for venture capital in the 2000s.
4. The author states his bias: his beliefs may make him "give too short shrift to discretionary active managers". He cannot write about AQR's proprietary research.

## Extraction Notes
- Table 7.1 (factor-by-factor betas and contributions) did not survive. The three group totals come from the prose.
- Figures 7.1 to 7.3 are images. Buffett and Soros bar values survive only as loose numbers and are not reproduced.

## Connects To
- **Ch 4**: active credit managers' beta tilt.
- **Ch 5**: private equity demystified.
- **Ch 10**: equation 2 and the factor model behind alpha.
- **Ch 15**: fair fees.
