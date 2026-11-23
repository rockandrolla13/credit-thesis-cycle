# Chapter 7: The Coin-Tossing View of Finance

## Core Idea
Modern finance rests on Louis Bachelier's idea that price moves are like coin tosses: independent, random, and bell-curve distributed. That idea produced the efficient market hypothesis, value-at-risk and Black-Scholes. Mandelbrot's evidence of fat tails and volatility clustering shows the assumptions are wrong, so risk models built on past data can expose their users to danger. This chapter is the source of Cassidy's **illusion of predictability**.

## Frameworks Introduced
- **The coin-tossing view / random walk** (Louis Bachelier, "The Theory of Speculation", 1900). Price moves until optimists and pessimists cancel out. Then the next move is up or down with equal chance. "The mathematical expectation of the speculator is zero."
  - Best forecast of a price next week is the current price.
  - Revival: Jimmy Savage found Bachelier's work in 1954 or 1955 and alerted Paul Samuelson.
- **Efficient market hypothesis** (Eugene Fama; thesis published in *The Journal of Business*, January 1965; three forms in the *Journal of Finance*, 1970). Financial markets always generate the correct prices given all available information.
  - **Weak form**: prices cannot be predicted from past movements.
  - **Semistrong form**: prices reflect all publicly available information.
  - **Strong form**: prices reflect all information, including private information.
  - Fama's claim: the first two "clearly confirmed", only "limited evidence" against the third.
  - Correction mechanism: if prices rise above fundamentals, informed speculators sell. Friedman set out this logic in a 1951 essay on exchange rates.
- **Proof by contradiction for unpredictability**: assume a reliable prediction method exists. Someone finds it and profits. There are no patents on ideas, so others copy it. The returns are arbitraged away.
- **Bell-curve risk measurement**. Compute the mean daily change and the standard deviation (sigma) from a sample. Under the normal distribution the chance of a move beyond one sigma is roughly one in three, beyond two sigma about one in twenty, beyond three sigma about one in three hundred.
- **Value-at-risk (VAR)**: use those statistics to put a dollar value on the risk of adverse outcomes over a day, month or year, then hold capital against it.
- **Black-Scholes option pricing formula** (Fischer Black and Myron Scholes, published May 1973). Inputs listed in the text: strike price, current price, duration of the option, interest rate on government bonds, standard deviation of the stock, and a table of the normal distribution. The text does not reproduce the formula.
- **Grossman-Stiglitz paradox** (Sanford Grossman and Joseph Stiglitz, 1975, "On the Impossibility of Informationally Efficient Markets"). If prices already reflect all information, nobody has an incentive to gather it. If nobody gathers it, prices cannot reflect it. "For the market to work at all, there must be some level of inefficiency."
- **Fat tails and volatility clustering** (Benoit Mandelbrot, from cotton price records obtained through Hendrik Houthakker). Price changes show many small moves, some very large ones, and few intermediate ones.
  - Rule: "Large changes tend to be followed by more large changes, positive or negative. Small changes tend to be followed by more small changes."
  - Implication: the independence assumption fails. Markets alternate between long calm and short frantic periods, and the causal relationships may vary over time.

## Key Concepts
- **Financial "veil"**: the older view that finance merely covers the real economy. Monetarists and Keynesians shared it, and the standard model put the whole financial sector in one equation.
- **Central processor**: Cassidy's image of financial markets within Hayek's telecommunications system.
- **Fundamental analysis**: research on earnings and operations. Fama called it "a fairly useless procedure".
- **Index funds**: funds that replicate the overall market with minimal fees.
- **Put / call**: the right to sell or buy a stock at a specified price on a future date.
- **Derivatives**: options and option-like securities used to guard against extreme outcomes.
- **Quantitative finance**: also includes Harry Markowitz's mean-variance approach and the capital asset pricing model.

## Mental Models
- Think of normal-distribution risk as sand grains in a heap. Mandelbrot's data show "statistical boulders".
- If the market's underlying reality keeps changing, treat models fitted to past data as "of limited use, at best".
- Use the efficient market hypothesis for what it gets right. Prediction is very hard, and most funds do not beat the market (Burton Malkiel, *A Random Walk Down Wall Street*).

## Anti-patterns
- **Two-statistic risk**: making precise statements about extremes from one sample's mean and standard deviation.
- **Treating every price as correct**: Cassidy notes the hypothesis implies oil was correctly priced at roughly $50 a barrel in January 2007, $140 in June 2008, and $40 in February 2009.
- **Teaching the hypothesis as a description of reality**: the state of M.B.A. courses by the 1980s.

## Reference Table
Dow Jones Industrial Average daily moves, 1916 to 2003 (Mandelbrot and Hudson, *The (Mis)Behavior of Markets*, 2004, as quoted):

| Daily move larger than | Bell curve predicts | Observed |
|---|---|---|
| 3.4% | 58 days | 1,001 days |
| 4.5% | 6 days | 366 days |
| 7% | once every 300,000 years | 48 days in the 20th century |

## Worked Example
**Sizing risk on one stock the coin-tossing way.**
1. Pull one year of closing prices.
2. Compute the average daily change and its standard deviation, sigma.
3. Read the odds from the normal distribution: beyond one sigma roughly 1 in 3, beyond two sigma about 1 in 20, beyond three sigma about 1 in 300.
4. A bank applies the same steps to its portfolio to get the odds of a big fall, then sets capital reserves and hedges.
Now apply the Dow table above. The same method understates moves beyond 3.4 percent by a factor of about seventeen (58 predicted, 1,001 observed). The procedure is cheap and precise, and wrong in the tail.

## Key Takeaways
1. The efficient market hypothesis extends the invisible hand to Wall Street. Smith never did (Ch 2).
2. VAR, option pricing and most derivative pricing rely "to some extent" on Black-Scholes and the bell curve.
3. Fat tails and volatility clustering are documented across stocks, bonds and currencies.
4. Some inefficiency is logically required for markets to work.

## Connects To
- **Ch 8**: the same rationality assumption applied to the whole economy.
- **Ch 13-14**: beauty contests and herding as reasons prices leave fundamentals.
- **Ch 20, 22**: VAR and rating models in the crisis.
