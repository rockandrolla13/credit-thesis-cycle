# Chapter 4: Liquid Asset Class Premia

## Core Idea
Any long-only return is cash plus premia. The chapter updates the evidence and gives forward-looking estimates for cash and four market premia: equity, term, credit and commodity. In 2021 all look low in total-return terms, mostly because cash is low.

## Frameworks Introduced
- **Pyramid of long-run return sources** (Figure 4.1): cash at the base, then market risk premia (ERP, BRP, CRP, CMP), then alternative risk premia (value, momentum, carry, defensive), then alpha. Illiquids sit at the side because they blend all of these.
- **Cash decomposition** (4.1): cash rate = expected inflation + expected real rate. The old US "normal" was near 4% (2-3% inflation, 1-2% real). The long-run real cash rate is near zero globally and near +1% in the US since 1900. Drivers of the neutral real rate R*: productivity and demographics, plus the saving glut.
- **Dividend discount model** (4.2): `E(R) ≈ DY + g + E(ΔV)`. With no mean reversion, `E(R) ≈ DY + g` (Gordon). The result is a real return. The author sets g at 1.5% real, from over a century of US EPS data, and E(ΔV) at zero.
  - CAEY (1/CAPE) is an alternative real-return proxy. Half of CAEY can proxy the income yield (payout ratio 0.5). Scale CAEY by 1.075 to compare with current earnings yield (note 14).
- **Four refinements to equity expected returns** (4.2):
  1. Net total payout yield: `E(R) ≈ NTY + g_TPagg` (Straehl-Ibbotson 2017). Add net buybacks to the yield, then use aggregate payout growth, not per-share.
  2. Dilution: per-share growth lagged aggregate growth by up to 2% a year for much of the 20th century.
  3. Eight-part decomposition (L'Her et al. 2018): inflation/currency, dividend yield, GDP per capita growth, valuation change, payout ratio, margin, net buybacks, relative dynamism.
  4. Mean reversion versus structural change: the author assumes neither. "Model averaging is a good idea."
- **Three-way decomposition of the 10-year yield** (4.3, Figure 4.12): expected average inflation + expected average real short rate + bond risk premium (BRP). Survey-based BRP = yield minus the consensus forecast of average future short rates.
- **Three reasons the BRP turned negative** (4.3): low inflation risk premium, negative safe-haven premium (stock-bond correlation turned negative around 2000), and demand effects (QE, liability matching, safe-asset demand).
- **Stock-bond correlation rule** (note 32): growth news moves stocks and bonds in opposite directions. Inflation news moves them the same way. The sign depends on which uncertainty is larger.
- **Credit spread decomposition** (4.4): OAS = expected default loss + required premium for credit risk, illiquidity, tax and regulation. Also allow for IG **downgrading bias**.
- **Spread capture**: realized excess return divided by average OAS.
- **Turning water into wine** (4.5): single commodities compound at about zero. A rebalanced diversified basket compounds at over 3%.
- **Inflation hedge versus inflation protection** (4.5): hedging is about short-term correlation with inflation surprises. Protection is a long-run real premium. Equities and real estate may protect. They do not hedge.

## Credit premium: the numbers (4.4)
| Item | Value | Period / source cited |
|---|---|---|
| IG excess return over Treasuries, author's earlier estimate | 0.3-0.4% | *Expected Returns* (2011) |
| IG credit premium, duration-adjusted | near 1.5% | 1936-2014, Asvanunt-Richardson (2017) |
| Same, later starts | 1.0% from 1973, 0.7% from 1989, both to 2020 | text |
| IG arithmetic excess return | 75bp against average OAS of 132bp. Capture 56% | Table 4.3, 1989-2020 |
| IG capture when the sample ended in 2009 | 25% | text |
| HY excess return | about 2.8% against average spread of 5.2%. Capture 54% | Table 4.3 |
| Break-even spread for default losses | 15-25bp IG, 200-250bp HY | text |
| IG default plus downgrade leakage | "at most 30bp". The remaining leakage is index selling of fallen angels | text |
| Credit versus matched equity/Treasury mix | +1.5% IG, +3% HY | 1993-2019, Ben Dor et al. (2021) |
| Ex-post optimal weights across three assets | credits 48%, Treasuries 35%, S&P 500 17% | 1936-2014 |
| Credit correlation with equities | 0.25 | same |
| Fallen angels versus all HY, compound excess | 4.6% versus 2.3% (1997-2020). 6.5% versus 4.2% (2010-2020) | note 38 |
| Fallen angel volatility versus HY | 11% versus 10% | note 38 |
| Information ratio by maturity | 0.45 for 1-3 year, 0.05 for over 25 year (1989-2020). 0.74 and 0.12 since 2010 | text |

Market sizes cited: US corporates $10.0trn (mid-2021, SIFMA). Global leveraged loans $5trn, global HY $2.5trn, private credit almost $1trn, CLOs $0.8trn (IMF, October 2020).

The author's reading of why credit beats a stock/Treasury mix (from Ben Dor et al.): credits are "effectively short volatility" and benefit from leverage aversion. Illiquidity does not explain the edge. A caution in note 35: early-decade corporate data may overstate the premium.

Behaviour of spreads: narrow in calm times, sharply wider in recessions and crises. The HY spread "anticipates rather than reacts to" defaults (Figure 4.14). IG index quality fell and duration lengthened, which would justify wider spreads. Reach-for-yield offset that.

Active credit managers: most IG-benchmarked funds and credit hedge funds run a persistent long credit beta. That explains much of their outperformance and makes them worse equity diversifiers. They show no significant value, momentum or defensive exposure, only carry.

## Other premia: the numbers
| Premium | Historical | Forward view, 2021 |
|---|---|---|
| Global equities 1900-2020 (Dimson-Marsh-Staunton) | 8.3% compound nominal, 5.3% real, 4.4% over bills, 3.1% over bonds, SR 0.35 | US DDM: 1.7% income + 1.5% growth = about 3.2% real. Plus 2.3% inflation = 5.5% nominal. Arithmetic 6.8%, SR 0.43 at 16% volatility and zero cash |
| US versus rest, real | 6.6% versus 4.5% (1900-2020). 11.3% versus 4.4% (2010-20) | US-rest valuation gap "about as wide in 2021 as it has ever been" |
| Bond risk premium 1920-2020 | 1.8% a year against average term spread of 1.4%. SR 0.3 for the 10-year, 0.4 global | BRP below zero. Curve still upward-sloping |
| Commodity basket 1900-2020 | 4.9% compound, SR 0.37. Other start dates give 3-4% | "A constant premium of some 3% over cash" for a diversified basket, not single commodities |
| Gold | Near zero real over centuries. No net real rise in the 40 years after the 1970s spike | Inverse to real rates, but "not very strong" |

BRP decomposition numbers: yields fell over 10% in four decades. Expected inflation fell from 5% to 2%, BRP from 3-4% to below zero, expected real short rates from 3% to below zero. Falling BRP explains "almost 4%". Fed assets: $0.8trn before 2008, $4.5trn by 2015, $8trn by mid-2021.

Table 4.4 (1877-2020): equal-weighted composite GM 3.4%, AM 4.9%, volatility 18%, SR 0.27. Average single commodity GM 0.0%, AM 4.0%, volatility 28%, SR 0.12.

## Mental Models
- Use arithmetic mean for a one-period or rebalanced small holding. Use geometric mean for long horizons. The gap is about half the variance (1.3% at 16% volatility).
- t-statistic of a mean = Sharpe ratio × √years. US equities: 0.40 × 11 = 4.4.
- GDP growth does not predict equity returns across countries (Box 4.2). Correlation of real return with real GDP growth is 0.0 across 43 countries, 1997-2017. With net buybacks it is 0.60. China is the dilution case.
- A steep yield curve is "as good as it gets" as a bond timing signal, and still not reliable. Forwards and consensus predicted rising yields "for almost 30 years".
- For a bond portfolio, starting yield predicts return best at a horizon near twice the duration (note 33).
- Yield curve steepness matters more than yield level for near-term excess or currency-hedged bond returns.
- Front-end credit is most exposed when "bonds trade on price, not yield", as in autumn 2008 and spring 2020.

## Anti-patterns
- **Assuming yields must rise**: "one of the costliest mistakes of recent decades for pension funds".
- **Calling equities or real estate inflation hedges**.
- **Measuring credit by total return**: for IG that mostly measures rate exposure.
- **Compounding bearishness**: adding valuation mean reversion on top of an already low yield-based estimate, as some providers do.
- **Judging commodities by single-commodity charts**.

## Key Takeaways
1. Equities in 2021: expensive in absolute terms, cheap against cash. Below-average returns with above-average premia.
2. The credit premium is real in the newer evidence and not redundant to stocks plus Treasuries.
3. Fallen angels and short-dated credit kept their edge through the 2010s.
4. "At the time of writing, credit spreads are well below historical averages." The larger problem for total return is the low riskless curve.
5. Commodities and break-even inflation are the only listed assets that like rising inflation in Figure 4.17. Most portfolios "are not well-positioned if it arrives".

## Extraction Notes
- Table 4.3 (credit statistics by rating), Table 4.2 (L'Her decomposition) and Table 4.5 (commodity indices) did not survive. Only values quoted in prose are recorded. The per-rating spread and return figures are lost. The prose says spreads rise monotonically as rating falls and excess return shows "a bump for BB".
- Table 4.1 survived: real growth 1900-2020 of GDP per capita 1.9%, DPS 1.8%, EPS 1.5%. Sub-periods for EPS: 0.5%, 2.1%, 1.9%.
- Figure 4.8 text values survive: net total yield averaged 3.7% (1901-1971), 2.1% (1972-1999), 1.5% (2000-2020).
- All figures are images.

## Connects To
- **Ch 5**: illiquid credit and the smoothing issue.
- **Ch 6**: carry and defensive styles in credit. Variance risk premium.
- **Ch 8**: why these premia exist.
- **Ch 16**: timing with valuations.
