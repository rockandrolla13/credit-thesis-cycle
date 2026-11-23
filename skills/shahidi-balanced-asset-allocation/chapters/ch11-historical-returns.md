# Chapter 11: The Balanced Portfolio: Historical Returns

## Core Idea
From 1927 to 2013 the 20/20/30/30 portfolio earned about the same excess return as 60/40 with about 30% less volatility, steadier results across long cycles and smaller drawdowns. Its bad periods line up with the two undiversifiable risks: surprise jumps in cash rates and deleveragings. The author tells the reader not to rely on this data too much.

## Frameworks Introduced
- **Three performance questions**:
  1. Has it earned steady, attractive returns over the long run?
  2. Have there been long periods of underperformance?
  3. Over shorter periods, are large downturns rare and small, or frequent and large?
- **Why 20% equities can match 60% equities**:
  - *Fewer big losses.* A 50% loss needs a 100% gain to recover. "The volatility matters."
  - *Rebalancing advantage.* Annual rebalancing across assets that react differently forces selling winners and buying losers. The actual return is "about 1 percent better per year" than the weighted average of the components.
- **Free lunch claim**: a well-balanced portfolio earns the same return with less risk. "It is not that the balanced portfolio is so special, but that 60/40 is so inefficient."
- **When the balanced portfolio loses to cash** (the two undiversifiable risks):
  1. *Cash rates rise far more than discounted.* The rise must be large and unexpected. Cases: 1980, 1994. A variant is a jump in *expected* future cash rates with no Fed move: 2013, which "lasted about a month".
  2. *Risk appetite collapses.* Risk premiums spike. Cases: 1929-1932 and 2008-2009, both deleveragings.
- **Why these episodes are rare and short**:
  - Deleveragings come once or twice in a century.
  - A rate shock needs a big Fed move that is also unforeseen.
  - Falling asset values weaken the economy through the wealth effect. The Fed then eases. "The Fed won't let them last too long."
  - After the fall, higher risk premiums raise forward returns.
  - A deleveraging may last longer than a rate shock.
- **Rising-rate question**: results depend on *why* rates rise. Inflation: TIPS and commodities help. Growth: stocks and commodities help.
- **Caveat on history**: actual history is one of many paths that could have occurred. "Focus on the process rather than the historical data."

## Key Concepts
- **Rolling returns**: returns for every start month over a fixed window. The chapter uses 3-month and 1, 3, 5, 7 and 10-year windows, 5,955 data points in total.
- **Peak-to-trough drawdown**: the loss from buying at the worst time and selling at the low.
- **Recovery time**: months to regain the prior peak.
- **Rebalancing advantage**: the return above the weighted average of component returns.
- **Wealth effect**: lower asset values cut spending.

## Mental Models
- Tortoise and hare. The balanced portfolio wins by avoiding major slowdowns, not by sprinting.
- A tuned engine. Parts move up and down inside. The outside runs smoothly. 60/40 is the engine with two parts removed.
- Zoom out. Over 86 years the growth of $1 looks like a straight upward line.
- You are most likely to change strategy after underperformance and just before recovery.

## Anti-patterns
- **Fearing the 60% bond weight because rates are low**: excess returns should not differ much between rising and falling rate periods.
- **Selling at the trough**: the consistency numbers assume you hold.
- **Over-reading the backtest**: what did not happen matters as much as what did.

## Reference Tables

### Table 11.1: annualized excess returns to 12/31/2013
| | 10 yr | 25 yr | 50 yr | 75 yr | Since 1927 |
|---|---|---|---|---|---|
| Balanced | 5.8% | 6.2% | 4.2% | 4.8% | 4.3% |
| 60/40 | 5.1% | 5.6% | 3.3% | 4.6% | 4.4% |
| Cash | 1.7% | 3.6% | 5.5% | 4.1% | 3.8% |

### Table 11.3: volatility, 1927-2013
| | Volatility |
|---|---|
| Equities | 19.2% |
| Core bonds | 4.8% |
| 60/40 | 11.7% |
| Commodities | 17.1% |
| Long-term Treasuries | 10.0% |
| Long-term TIPS | 10.6% |
| Balanced portfolio | 8.2% |

The balanced portfolio's volatility is below that of every component.

### Table 11.5: worst calendar years for the balanced portfolio
| Year | Excess | Cash | Total |
|---|---|---|---|
| 1930 | -13.0% | 2.3% | -10.7% |
| 1931 | -26.9% | 1.2% | -25.8% |
| 1932 | -5.5% | 0.9% | -4.6% |
| 1937 | -8.7% | 0.3% | -8.4% |
| 1969 | -7.8% | 7.1% | -0.7% |
| 1981 | -16.7% | 15.4% | -1.3% |
| 1994 | -9.9% | 4.3% | -5.6% |
| 2001 | -6.7% | 3.8% | -2.9% |
| 2006 | -6.2% | 5.0% | -1.2% |
| 2008 | -8.8% | 1.9% | -6.9% |

### Table 11.6: annualized excess return by long cycle
| Period | Balanced | 60/40 | Cash |
|---|---|---|---|
| 1929-1948 (bear) | 5.7% | 2.2% | 0.5% |
| 1948-1965 (bull) | 2.8% | 8.4% | 2.3% |
| 1965-1982 (bear) | 1.1% | -2.3% | 7.5% |
| 1982-2000 (bull) | 6.1% | 9.2% | 6.5% |
| 2000-2013 (bear) | 6.1% | 2.7% | 2.1% |
| Average | 4.3% | 4.1% | 3.8% |

### Table 11.7: the rising-rate test, 1963-1981
| | Excess return | Risk | Return/risk |
|---|---|---|---|
| Balanced | 1.3% | 7.5% | 0.17 |
| 60/40 | -0.5% | 9.5% | -0.05 |
| Cash | 6.6% | | |

The 10-year Treasury yield rose from 3.8% to 15.3%. Per year: equities +0.3%, Treasuries -5.2%, commodities +5.3%, TIPS +3.4%.

### Table 11.8: share of rolling periods that underperformed cash
| Window | Balanced | 60/40 | All four asset classes at once |
|---|---|---|---|
| 3 months | 36% | 36% | 5% |
| 1 year | 28% | 33% | 4% |
| 3 years | 13% | 24% | 1% |
| 5 years | 13% | 23% | 1% |
| 7 years | 10% | 15% | 1% |
| 10 years | 2% | 15% | Never |

### Table 11.9: drawdowns of at least 10% (cumulative excess return)
| Balanced period | Loss | Months to recover | 60/40 period | Loss | Months to recover |
|---|---|---|---|---|---|
| 1929-1932 | -50% | 49 | 1929-1932 | -64% | 53 |
| 1937-1938 | -15% | 20 | 1937-1938 | -32% | 58 |
| 1968-1970 | -13% | 8 | 1968-1970 | -27% | 188 |
| 1980-1982 | -31% | 50 | 1972-1974 | -33% | 132 |
| 1983-1984 | -15% | 17 | 1980-1982 | -22% | 8 |
| 1993-1994 | -14% | 10 | 1987 | -21% | 20 |
| 2005-2007 | -11% | 6 | 2000-2002 | -29% | 50 |
| 2008-2009 | -26% | 19 | 2007-2009 | -32% | 22 |
| | | | 11 more periods | -10% to -15% | 18 average |

The balanced portfolio had 8 such periods. 60/40 had 19.

### Table 11.10: cumulative excess return in major bear markets
| Episode | Balanced | 60/40 | Cash |
|---|---|---|---|
| 2011 downturn | +5.5% | -8.3% | 0.0% |
| 2008 credit crisis | -17.6% | -32.3% | 2.6% |
| 2000-2002 | +21.2% | -26.6% | 10.9% |
| October 1987 crash | -5.7% | -20.5% | 1.6% |
| 1973-1974 | +13.7% | -33.3% | 16.5% |
| 1939-1941 | +30.5% | -13.7% | 0.3% |
| 1937 recession | -15.1% | -31.7% | 0.3% |
| 1929-1932 | -49.8% | -63.6% | 5.6% |

Windows run from the S&P 500 peak to its trough. Tables 11.2 and 11.4 are images and are lost.

## Worked Example
*Rebalancing through 2008 and 2009.*
- 2008: stocks had an excess return of -38.3%. Long-term Treasuries had +39.2%.
- Year-end rebalance to 20/20/30/30: buy stocks, sell Treasuries.
- 2009: stocks rose 26.9%. Long-term Treasuries fell 25.7%.
- The trade bought low and sold high. Repeated over time, this is the source of the roughly 1% a year above the weighted average.

*Two opposite eras, one result.* 1929-1948 was depression and prolonged weakness. 1982-2000 was the greatest boom. The balanced portfolio's excess return was 5.7% in the first and 6.1% in the second.

*Other facts stated.* Only three calendar years had excess losses above 10% (1930, 1931, 1981). Since the Great Depression, the worst calendar-year total return was -6.9% in 2008. All four assets lost to cash in the same calendar year three times: 1931, 1969, 1981. Only in 1931 were all four negative on a total return basis.

## Key Takeaways
1. Same long-run excess return as 60/40 (4.3% against 4.4%). Volatility 8.2% against 11.7%.
2. The weakest long cycle was 1965-1982 at 1.1%, because cash rates rose far more than expected.
3. Every 5, 7 and 10-year underperformance against cash traces to a cash-rate shock or a deleveraging.
4. Over 10-year windows the balanced portfolio lost to cash 2% of the time. 60/40 lost 15% of the time.
5. It still lost 50% against cash in 1929-1932. Balance does not protect against a collapse in risk appetite.

## Connects To
- **Ch 3**: the three-driver framework that predicts these results.
- **Ch 1**: deleveraging as the setting for the worst drawdowns.
- **Ch 12**: holding through underperformance as the main implementation risk.
