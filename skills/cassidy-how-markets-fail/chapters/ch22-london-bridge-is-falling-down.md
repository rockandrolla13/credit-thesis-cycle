# Chapter 22: London Bridge Is Falling Down

## Core Idea
A small loss in one market became the worst financial breakdown since the 1930s through amplification. Leverage, mark-to-market accounting and short-term funding made every bank react to falling prices in the same way at the same time. This case study covers August 2007 to March 2008. It carries a general mechanism: Hyun Song Shin's **loss spiral**.

## Frameworks Introduced
- **The Millennium Bridge analogy / "synchronous lateral excitation"** (Hyun Song Shin, 2005 paper). When the footbridge opened on June 10, 2000, it swayed. Pedestrians adjusted their steps to the sway, which increased it. "The wobble can feed on itself."
  - Mapping (Figure 22.2, recovered from EPUB image 00009.jpg, two loops side by side): **bridge moves → signal → pedestrians adjust steps → feedback → bridge moves**, and **prices fall → signal → banks sell → feedback → prices fall**.
  - Shin: "The pedestrians on the bridge are like banks adjusting their stance and the movements of the bridge are like price changes. You want diversity, but the market price is a lightning rod that imposes uniformity."
  - **Threshold effect**: below one hundred and sixty people the bridge was safe. Above that the wobble was likely. Markets work while liquidity is above some level. Below it, "all the elements that formed a virtuous circle to promote stability now will conspire to undermine it". Shin: "What we don't know is where the threshold is."
  - Engineering fix: shock absorbers. The bridge reopened in February 2002 without trouble.
- **The loss spiral** (Table 22.1, adapted from Shin's Clarendon Lectures, June 2008). Three ingredients: a leverage target, mark-to-market accounting, and many firms acting together. See the worked example.
  - Why it is rational irrationality: "To each of these firms, slimming down and reducing leverage was a sensible and necessary strategy. From a system-wide perspective, it only added to the downward momentum."
- **Virtuous and vicious circles share an upward-sloping demand curve**: in good times rising asset values lift bank equity, so banks buy more assets and prices rise. In bad times the reverse. "Rising prices generate more demand; falling prices generate less demand." With a demand curve of "the wrong shape", prices may settle, "cycle around wildly", or "explode in one direction".
- **Mark-to-market as procyclical** (Gary Gorton, Yale, 2008): fair-value accounting assumes prices are the best estimate of value, "a commitment to Chicago School economics". Combined with "a laissez-faire attitude to banks' leverage, it can practically guarantee the emergence of booms and busts". Formalized in Financial Accounting Standards Board Rule 157, September 2006.
- **A freeze, not a crash**: in August 2007 the mortgage securities market did not spiral down. It "had simply frozen up". This was "an acute case of hidden information". Holders could not value their own paper, and lenders could not estimate a rival's exposure, so they hoarded capital. "Hayek's telecommunications system was no longer emitting any price signals."
- **Run on a non-bank as a prisoner's dilemma**: creditors of a firm with illiquid assets and short-term funding would all gain by staying. Each gains by leaving first. "Withdrawing money immediately is a dominant strategy." Runs "can be self-fulfilling", so "even an economically sound institution can be felled".
- **Securitization concentrated risk**: when asset-backed commercial paper died, SIVs drew on their parents' credit lines. "Far from distributing the risks associated with subprime, securitization and the construction of the shadow banking system had helped to concentrate it at the heart of the financial world."
- **Linked vicious circles**: the financial loss spiral, the housing cycle (foreclosures → forced sales → lower prices → negative equity → more defaults), and the real economy (construction and jobs).

## Key Concepts
- **Asset-backed commercial paper (ABCP)**: short-term bonds issued by SIVs and conduits to fund long-term assets.
- **Repo market**: overnight borrowing by selling assets with an agreement to repurchase. Fully secured and "widely regarded as ultrasafe".
- **Interbank lending market**: where banks fund daily operations. It "largely dried up" on August 9, 2007.
- **Leverage ratio**: total assets divided by equity capital.
- **Negative equity**: owing more on a mortgage than the home is worth.
- **Equilibrium relationships**: Paul Samuelson's point that most known regularities hold only in normal times. He suggested studying "the physics of avalanches".
- **Discount rate**: the rate at which the Fed lends to banks.

## Mental Models
- A market's size relative to total wealth is the wrong measure. The Fed reasoned that subprime was about $1 trillion of $12 trillion in mortgages, and that losing half of it would equal a 3 percent move in an $18 trillion stock market. It missed leverage, concentration and funding.
- Ask who funds long-term assets with overnight money. By 2006-2007 the big investment banks "had turned into hedge funds in disguise".
- Treat a denial of liquidity trouble as fuel. Bear's statement of March 10 "only drew attention" to the rumours.
- Treat balance sheet shrinkage across large firms as the visible trace of a loss spiral.

## Anti-patterns
- **"Contained"**: Ben Bernanke, March 2007, said the subprime problem "seems likely to be contained". He later told Cassidy, "I and others were mistaken early on."
- **Assuming a liquidity crisis is temporary**: most are. This one was not, because the information to reprice "simply didn't exist".
- **Treating off-balance-sheet as off-risk**: a senior policymaker said, "I don't think we recognized to what extent it could come back on the balance sheet when confidence eroded."
- **Refusing to recognize a bubble**: as late as October 2007 Bernanke said he had no way of knowing whether there had been one.

## Reference Tables
Table 22.1, the loss spiral ($ billion):

| | Panel A (start) | Panel B (after 1% fall) | Panel C (after selling) |
|---|---|---|---|
| Assets | 200 | 198 | 160 |
| Debt | 190 | 190 | 152 |
| Equity | 10 | 8 | 8 |
| Leverage ratio | 200/10 = 20 | 198/8 = 24.75 | 160/8 = 20 |

Balance sheet shrinkage:

| Firm | Before | A year later | Change |
|---|---|---|---|
| Merrill Lynch | more than $1 trillion (summer 2007) | about $875 billion | down an eighth |
| Morgan Stanley | about $1 trillion (November 2007) | about $660 billion | down a third |
| Citigroup | almost $2.2 trillion (December 2007) | slightly above $1.9 trillion | down more than a tenth |
| Goldman Sachs | $1.1 trillion (November 2007) | $885 billion | down about a fifth |

Timeline:

| Date | Event |
|---|---|
| July 2007 | S&P and Moody's review ratings on almost $18 billion of mortgage bonds |
| August 9, 2007 | BNP Paribas suspends three funds worth €1.6 billion. Interbank lending dries up. ECB offers €95 billion. Dow falls 387 points |
| August 10, 2007 | ECB adds €61 billion. Fed promises short-term credit |
| August 17, 2007 | Fed cuts the discount rate half a point to 5.75 percent |
| August-September 2007 | Outstanding ABCP falls by about $370 billion |
| Mid-September 2007 | Depositor run on Northern Rock. British government rescue |
| October 2007 | Write-downs: Merrill $7.9 billion, Citigroup $6.5 billion, UBS $3.4 billion. O'Neal and Prince leave |
| November-December 2007 | HSBC takes $45 billion of SIV assets on balance sheet. Citigroup takes $49 billion from seven SIVs |
| March 10-16, 2008 | Run on Bear Stearns. Sold to JPMorgan Chase at $2 a share, later raised to $10 |

Housing and economy: national home prices fell 17 percent from the third quarter of 2007 to the third quarter of 2008. Phoenix fell 32 percent, Miami 28 percent, San Diego 26 percent. By February 2008 roughly one in four subprime borrowers was at least a month behind. From August 2007 to October 2008, 936,439 homes were foreclosed on. About 8.5 million homeowners, one in seven mortgage holders, had negative equity by spring 2008. Housing starts virtually halved from a 1.5 million annual rate. Unemployment rose from 4.7 to 5 percent in December 2007.

## Worked Example
**The loss spiral, step by step.**
1. A firm targets leverage of 20. It has $200 billion of assets, $10 billion of equity and $190 billion of debt.
2. Asset values fall 1 percent, or $2 billion. Under mark-to-market it books the loss at once. Assets are $198 billion. Debt is unchanged, so equity is $8 billion, down 20 percent.
3. Leverage is now 24.75. To return to 20 the firm must sell $38 billion of assets and repay $38 billion of debt.
4. It ends with $160 billion of assets, $152 billion of debt and $8 billion of equity. A 1 percent price fall forced a 19 percent asset sale.
5. Every leveraged firm does this together. Sales push prices down, which creates new losses and restarts step 2.

**Bear Stearns, March 2008.** At the end of 2007 Bear had leverage above thirty to one, $395 billion of assets with more than $100 billion funded in repo, and more than $60 billion of hedge fund deposits. At thirty to one, "a mere 4 percent drop in the value of a firm's assets can wipe out its entire capital base". On Monday March 10 it had about $17 billion in cash. ING declined to renew about $500 million of loans. Goldman Sachs stopped taking over clients' Bear trades. Hedge funds withdrew, and repo lenders refused to roll "even high-quality collateral". By Thursday afternoon cash was $2 billion. Bear's stated mortgage holdings were $2 billion subprime, $15 billion prime and Alt-A, and $16 billion commercial.

## Key Takeaways
1. Amplification, not the size of the first loss, sets the size of a crisis.
2. Leverage targets plus fair-value accounting synchronize selling.
3. Short-term secured funding can run as fast as deposits.
4. A market can fail by freezing. Then no price exists to mark to.
5. Policymakers' priors mattered. Cassidy says Bernanke's view "reflected a failure of imagination" and the illusion of stability.

## Extraction Notes
- Table 22.1 is flattened in the extract. It is rebuilt above from the loose lines and the prose, which agree.
- The source says "roughly one in four subprime lenders was at least one month behind on his payment". The context shows borrowers are meant. The source also writes that equity is "$8" where $8 billion is meant.
- Figure 22.2 is absent from the text extract and was read from the image.

## Connects To
- **Ch 2**: positive feedback.
- **Ch 11**: the prisoner's dilemma behind the run.
- **Ch 12**: hidden information and frozen lending.
- **Ch 16**: the Minsky moment and debt deflation.
- **Ch 20**: SIVs, VAR and leverage.
- **Ch 23**: Lehman and the state rescue.
