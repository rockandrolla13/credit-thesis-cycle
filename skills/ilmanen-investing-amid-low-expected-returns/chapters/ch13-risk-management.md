# Chapter 13: Risk Management

## Core Idea
"Survival comes first." Manage the big portfolio risk, which for most investors is equity direction. Diversify first, then pay for hedges or insurance only where a risk threatens survival. Option-based tail insurance has been costly. Trend following has protected in slow bear markets and earned a positive return.

## Frameworks Introduced
- **Broad lens** (13.1): judge an investment by its effect on the whole portfolio, on total wealth, over time, and by whether liabilities are limited. Unlimited liabilities (short stock, naked calls) are the most dangerous.
- **Four horsemen** (Bernstein): inflation, deflation, confiscation, devastation.
- **Failing fast versus failing slow**: regulators see fast failure and may raise the risk of slow failure by limiting risk in a low-return world.
- **Four techniques** (13.2):
  1. Diversification: correlation below one. Keeps rewarded exposures.
  2. Hedging: negative correlation to holdings. May remove a premium.
  3. Insurance: upfront cost, asymmetric payoff.
  4. Dynamic risk control: stop-loss, drawdown control, portfolio insurance. Reactive. "A plan beats no plan."
- **Order of use** (13.3): diversify across rewarded factors, diversify away unrewarded risk, then hedge or insure a dominant or existential risk.
- **Leverage safety rules**: safer to lever low-risk assets or to offset diversification gains than concentrated risky positions. Safer with futures than short-term borrowing. Safer on liquid assets: "the combination of leverage and illiquidity can be especially toxic". Add option protection or drawdown rules.
- **Put versus Trend**: Trend suits slow, long bear markets. Put suits fast, short ones.
- **Volatility as a starting point** (13.4): most downside measures are roughly proportional to volatility when returns are near symmetric. Add maximum drawdown, tail-event performance, liquidity, leverage, operational and ESG checks.
- **Volatility targeting** (Box 13.1): hold larger positions when estimated volatility is low. Main benefit is steadier risk, so investors use their full risk budget. It may raise the Sharpe ratio for equities, momentum and trend. It works when volatility persists (monthly autocorrelation 0.6-0.7) and expected return does not rise with volatility.
- **Kelly criterion**: growth-optimal bet size. Drawdown risk is "uncomfortably high". Most prefer half Kelly.

## Worked Example: Put versus Trend, January 1985 to March 2020 (Figure 13.1)
| | Multi-asset Trend (10% volatility target) | Long 5% out-of-the-money one-month S&P 500 puts (scaled to 10% volatility) |
|---|---|---|
| Geometric mean excess return | 8.7% | -6.4% |
| Sharpe ratio | 0.84 | -0.61 |
| CVaR 5% | -5.7% | -5.5% |
| Maximum drawdown | -35% | -92% |
| Skew | 0.1 | 3.5 |
| Equity correlation | -0.08 | -0.64 |

Put is gross of costs. Trend is net of estimated costs. The author's argument: index puts are expensive because they pay in bad times. Implied volatility usually exceeds realized, and the skew is steep. Over 35 years options "discounted even more extreme outcomes than what occurred". Taleb's counter, as the author reports it: there is not enough data to judge a strategy with rare payoffs. The author says the 2010s cost tail-insurance strategies perhaps over 90% of allocated capital. He also grants that Trend's record is "too good to be true" and expects less.

## Reference Table: 18 largest S&P 500 drawdowns (Table 13.1, excess of cash)
| Peak | Trough | Months | Depth | Put | Trend | Treasury | Gold | QMJ |
|---|---|---|---|---|---|---|---|---|
| Mar 1920 | Aug 1921 | 17 | -26% | | 10% | -4% | | |
| Aug 1929 | Jun 1932 | 34 | -84% | | 54% | -1% | | |
| Jan 1937 | Mar 1938 | 13 | -50% | | -8% | 6% | | |
| May 1946 | Nov 1946 | 6 | -22% | | 4% | -1% | | |
| Jul 1956 | Dec 1957 | 17 | -18% | | -1% | -1% | | 1% |
| Nov 1961 | Jun 1962 | 7 | -23% | | 0% | 0% | | 0% |
| Jan 1966 | Sep 1966 | 8 | -18% | | 6% | -2% | | 2% |
| Nov 1968 | Jun 1970 | 19 | -37% | | 37% | -13% | | 34% |
| Dec 1972 | Sep 1974 | 21 | -50% | | 123% | -11% | 129% | 5% |
| Nov 1980 | Jul 1982 | 20 | -35% | | 18% | -6% | -59% | 13% |
| Jun 1983 | Jul 1984 | 12 | -15% | | 2% | -6% | -28% | 17% |
| Aug 1987 | Nov 1987 | 3 | -31% | 23% | -6% | 0% | 7% | 4% |
| Aug 1989 | Oct 1990 | 14 | -18% | -6% | 11% | -1% | -4% | 29% |
| Apr 1998 | Aug 1998 | 4 | -15% | 11% | 13% | 4% | -12% | 12% |
| Mar 2000 | Sep 2002 | 30 | -49% | 11% | 52% | 23% | 5% | 96% |
| Oct 2007 | Feb 2009 | 16 | -52% | 31% | 15% | 14% | 14% | 53% |
| Apr 2011 | Sep 2011 | 5 | -16% | 9% | -8% | 10% | 4% | 20% |
| Dec 2019 | Mar 2020 | 3 | -20% | 27% | -2% | 10% | 4% | 4% |

**Caution**: the extraction dropped empty cells. Rows before 1987 have fewer values than columns. The column placement for those rows is inferred from when each series starts (puts 1985, gold and QMJ later) and from Figure 6.8's "123% in 1974" for Trend. The six rows from 1987 on have five values each and need no inference.

## Key Concepts
- **Tail hedging**: unless qualified, it means equity market tail events.
- **Antifragile**: Taleb's aim of portfolios that flourish in bad times. The author calls it "an unnecessary luxury. Surviving such times is enough."
- **Margin of safety**: count it "as a source of expected return, not as risk mitigation" (note 13).
- **Square-root-of-time rule**: 1% monthly volatility is about 3.46% annual if returns are not serially correlated.
- **Knightian uncertainty**: risk that cannot be measured.
- **Maverick risk, surplus risk, active risk**: the three risks beyond absolute portfolio risk.

## Mental Models
- The three worst episodes of the century for Western markets: the 1930s Depression, the 1970s inflation, 2008-9. Bear markets of 10-20% are "dodged bullets".
- Events with huge human cost can leave equity markets unharmed. US equities did well in both world wars and in mid-2020.
- Scenario analysis without probabilities helps little. There is always a scenario where you lose everything.
- You can insure the wrong tail: short-dated deep puts did little in the slow 2000-3 fall. Inflation hedges bought after 2008 looked wasted.
- A put overlay can pay for itself if it lets the investor hold more risk (70/30 instead of 60/40). Few will keep it while it bleeds.
- Use annual returns to estimate risk for smoothed illiquid assets.
- Risk is more forecastable than return. Daily data and short windows forecast volatility better, even for long horizons (Page 2021).

## Anti-patterns
- **Minimizing risk instead of managing it**.
- **Levering illiquid or concentrated positions**.
- **Running regular volatility buying or selling as a large allocation**: buyers leave after years of bleeding, sellers after a blow-out.
- **"Only permanent loss of capital matters"**: overconfident. "Everyone has a breaking point."
- **Chasing antifragility at any cost**.

## Key Takeaways
1. In Table 13.1, Put, Trend and quality-minus-junk were the most consistent hedges, ahead of Treasuries and gold. Put is "by far the costliest".
2. Leverage is needed for the diversification the book favours. It can and must be managed.
3. Institutions should debate which mix of absolute, active, surplus and peer risk drives decisions.
4. Named deleveraging episodes: August 1998, August 2007, September 2008.

## Extraction Notes
- Figure 13.1's statistics box survived and is reproduced. The chart is an image.
- Table 13.1: see the caution above.

## Connects To
- **Ch 6**: trend and QMJ construction.
- **Ch 8**: bad times.
- **Ch 11 and Ch 12**: diversification and constraints.
- **Ch 16**: tactical timing as another response to risk.
