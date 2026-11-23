# Chapter 2: Merger Arbitrage

## Core Idea
After a definitive merger agreement is signed, the target trades below the deal price. The gap is the spread. It pays the arbitrageur for the risk that a regulator, a shareholder vote, or the financing stops the deal, and for the time the money is tied up. About 95% of deals close, so the work is to avoid the 5% and to think in annualized returns.

## Frameworks Introduced
- **Sources of deal risk ("killjoys")**: three parties can object.
  1. A government regulator worried about competition.
  2. A dissenting shareholder who thinks the price is too low.
  3. An acquirer who finds the financing is not there.
- **Annualized return** (simple, no compounding): spread divided by the fraction of a year to closing.
  - 4% in one quarter is 16% a year. 4% in four months is 12%. The same 4% in six months is 8%.
  - 4.5% in four months, repeated three times, is 13.5% a year.
  - A dividend adds to the spread. A 4% annual yield over a six-month deal adds 2%, if the merger agreement does not stop the dividend.
  - The arbitrageur must find a new deal with a similar spread each time one closes.
- **Conservative closing date**: use the last day of the window the company gives. If a deal announced in 2023 is guided to "the second half of next year", use 31 December 2024. Then adjust for average closing times, sector, and regulatory or financing risk.
- **Closing-time base rates** (2,320 completed deals, 2010 to 2022, InsideArbitrage database): mean 131 days, median 107 days. Outliers: Change Healthcare / UnitedHealth 635 days, Xilinx / AMD 475 days. Pharmaceutical deals can close in three months. Semiconductor, banking, insurance and utility deals take longer.
- **Outside date**: the deadline in the merger agreement. At that date the parties can terminate or extend, more than once.
- **Deal types and how to capture the spread**:
  | Type | Capture | Stated risk |
  |---|---|---|
  | All cash | Buy the target and wait | Deal failure |
  | All stock | Buy the target and short the acquirer at the exchange ratio to "lock in the spread" | Borrow fees. Dividends owed on the short. On failure the target falls and the acquirer rises, a "double whammy" |
  | Cash plus stock | Buy the target and short the stock portion | Same as all stock on the stock leg |
  | Cash or stock | Elect one. Proration applies | You may not know what you will be paid |
  | Collar | Exchange ratio moves with the acquirer's price inside a range | The spread "has to be constantly recalculated" |
  | Special conditions and CVRs | Special dividends, a pre-close spinoff, or contingent value rights | Not all CVRs pay out |
- **CVR as a lottery ticket**: if the spread is positive and closing risk is low, the CVR is "a free or nearly free lottery ticket". Common in pharma and biotech deals.
- **The HSR sequence**: a filing under the Hart-Scott-Rodino Act starts a 30-day clock. The 2023 threshold is $111.4m. Companies file with both the FTC and the DOJ and one of them reviews. Five paths follow:
  1. Early termination of the waiting period.
  2. The clock runs out with no action.
  3. The companies pull and refile to reset the clock.
  4. A "second request" for more information. The deal cannot close until the companies comply.
  5. The agency sues to block.
- **Other regulators**: state agencies for insurance and utilities. CFIUS for cross-border deals with national security issues. Foreign competition authorities wherever the company operates (the UK's CMA, the European Commission, China's SAMR).
- **Walk-away law**: a signed definitive agreement cannot be put "on hold". The acquirer must prove a Material Adverse Change. A "specific performance" clause lets the target sue to force the close. Most such cases go to the Delaware Court of Chancery and settle at the agreed terms "or at a small discount".
- **Four option overlays**:
  1. Sell covered calls expiring after the expected close. You give up the upside of a bidding war.
  2. Buy puts when the spread is large and risk is high (the author did this on Microsoft / LinkedIn in 2016).
  3. Buy calls expiring shortly after the expected close (Apollo Education). The premium is lost if the deal fails or slips.
  4. Sell puts struck just below the deal price. You must buy the shares if the deal fails.
- **The rebound trade**: most arbitrage funds exit after a deal fails. This "often artificially depresses the stock of the target company for several days". The author calls this forced selling "the real opportunity in failed deals", above a new suitor or the termination fee.
- **Acquirer dislocation**: an acquirer can drop after a large deal is announced. In stock deals the arbitrageurs' shorting adds "temporary downward pressure".
- **Merger arbitrage as a bond alternative**: in high-rate periods "spreads widen to take time value of money into account". A portfolio of deals can "mimic some of the same characteristics of a bond portfolio without the interest rate risk". Choosing large spreads is like buying high-yield or junk bonds. Note a tension in the source: the body says the strategy does better when rates are high, and the chapter summary says some investors use it "especially during times when interest rates are low and bond yields are unattractive".

## Key Concepts
- **Definitive merger agreement**: the signed contract. It sets price, expected close, required approvals, and termination fees. It can run to 100 pages or more.
- **Go shop**: a period of usually 25 to 45 days in which the target may solicit a competing bid. New bids are rare.
- **Negative spread**: the target trades above the deal price because buyers expect a higher bid.
- **Tender offer / second-step merger**: holders tender shares. A buyer with a majority squeezes out the rest for cash.
- **Termination fee**: paid when a deal ends under stated conditions. It is not a free exit for the acquirer.
- **Poison pill**: a defence that lets the company issue many shares to dilute a hostile acquirer.
- **Other arbitrage forms the chapter lists**: cross-listing, dual share class, closed-end fund discount, statistical arbitrage.

## Mental Models
- Think of the spread's trend as a signal. The author cites Mitchell and Pulvino: spreads on failed mergers "tend to be large right after a deal is announced and increase in the days before the deal fails".
- Think of the average as a trap. "A six-foot-tall person can drown in a river that is on average about five feet deep."
- Use bear markets as a warning. He cites Cretin, Bouacha and Dieudonné (1,911 US and Canadian deals, January 1998 to September 2010): spreads widen and termination rates rise in bear markets such as 2001-2003 and 2008-2009.
- Asymmetry: "When a deal with 5% upside blows up, it can wipe out anywhere from 30% to 50% of your capital."

## Anti-patterns
- **Arbitrage tourism**: buying deals stuck at SAMR because the spread is large. "The large spread does not compensate" for months of delay with no visibility.
- **Ignoring annualized returns**: new investors skip a 3% spread over three months and "gravitate towards deals with large spreads and take on significant risk".
- **"I would not mind owning it if the deal fails"**: sector fundamentals can change while you wait.
- **Waiting for the last 1%**: see First Horizon below.
- **Paying a negative spread**: Vidler Water traded as high as $17.24 against a $15.75 cash deal (a negative spread of 9.5%). The deal closed at $15.75.
- **Assuming the termination fee lets the acquirer walk**: Twitter's fee was $1bn and it was not an exit.
- **Concentration**: the 95% close rate helps only if you hold many deals. Investors "rarely invest in dozens of deals simultaneously".
- Sectors experienced arbitrageurs avoid, per the author: deals with significant cross-border risk, and banking, insurance and utility deals.

## Reference Tables

### Renegotiated and litigated deals
| Deal | Original | Final | Note |
|---|---|---|---|
| Twitter / Musk (2022) | $54.20 | $54.20 | Closed 27 October 2022 after a Delaware suit |
| Forescout / Advent (2020) | $33 cash | $29 | 12.12% discount. Closed August 2020 |
| Tiffany / LVMH (2020) | $135 cash | $131.50 | Under 3% discount |
| Change Healthcare / UnitedHealth | $25.75 cash | Plus a $2 special dividend | DOJ sued 23 February 2022. Companies won 19 September 2022 |

### Spreads quoted in the chapter
| Deal | Spread | Why |
|---|---|---|
| Activision / Microsoft ($95 cash, stock at $78 in May 2023) | nearly 22% | FTC and foreign regulator risk |
| Cerner / Oracle | 1.3% | Close seen as very likely |
| Albertsons / Kroger ($24.6bn) | 39% | Regulatory concerns |
| Metromile / Lemonade (1 Lemonade share per 19 Metromile shares, 6 May 2022) | 14.06%, annualized 93.31% if closed by end June | All stock. Closed 28 July 2022 |
| Cooper Tire / Goodyear ($41.75 cash plus 0.907 Goodyear share) | a little over 3% at two points | Closed in 105 days, June 2021 |

### Collar example: Zynga / Take-Two (announced January 2022)
- $3.50 cash plus $6.361 in Take-Two stock per Zynga share.
- If Take-Two's 20-day VWAP is between $156.50 and $181.88, the ratio adjusts to deliver $9.86 in total.
- Above the range the ratio is 0.0350. Below the range it is 0.0406.
- Take-Two fell from above $210 at announcement to $123.62 at the close on 23 May 2022. Holders got $3.50 and 0.0406 shares.

### Bidding wars
- Spirit Airlines: JetBlue against Frontier, four months, seven rounds. JetBlue won at 32% above Frontier's offer, with a larger $400m termination fee payable to Spirit if regulators blocked the deal.
- Straight Path: AT&T against Verizon. The price nearly doubled from the original deal.

## Worked Example: Twitter (2022)
1. 4 April: Musk discloses a stake of over 9%.
2. 25 April: the board agrees to $54.20 per share. Financing of $46.5bn is lined up. The stock closes at $51.70, about 5% below the price.
3. 26 April: stock at $50, spread about 8%. A close by year-end would be about 12% annualized.
4. Growth stocks fall. Musk says the deal is "on hold" and raises the bot issue.
5. 11 July: stock at $32.65. Spread 66%.
6. Twitter sues in Delaware. The judge rejects the data requests as "absurdly broad" and notes "there wasn't any due diligence".
7. The court sets a deadline of 5pm on 28 October. The deal closes on 27 October at $54.20.

## Worked Example: two failed deals
- **Rite Aid / Walgreens.** October 2015: $9 cash, $17.2bn. Rite Aid had 4,600 stores. The FTC was not satisfied by a plan to divest 865 stores to Fred's. After more than 15 months the deal was recut to $6.50-$7. An offer to divest up to 1,200 stores also failed. The FTC pointed to earlier divestiture buyers that went bankrupt (Haggen, FSNA). Terminated 29 June 2017. Walgreens paid a $325m fee and later bought 2,186 stores for $5.175bn. Rite Aid stock later lost more than 90%.
- **Rogers / DuPont.** 2 October 2021: $277 cash, $5.2bn, a 46% premium. US antitrust cleared in under three months. Shareholders approved a month later. Eight months after that, every approval was in except SAMR. DuPont refiled at SAMR's request, then terminated nearly 13 months after announcement. Fee: $162.5m. Rogers fell more than $100 in a day. The author says the macro environment had changed and SAMR's delay gave DuPont a way out. SAMR approvals can take 12 to 15 months.

## Worked Example: First Horizon / TD (dark side)
$25 cash, $13.4bn. The spread went from small to over 20%, then narrowed to under 1%. The narrow spread was "a good exit". The author was invested and writes that "waiting for that last 1% proved to be very expensive". Bank failures in early 2023 followed. The deal was called off and the stock fell under $10.

## Key Takeaways
1. Compute the annualized return on a conservative closing date before comparing deals.
2. Read the merger agreement for required approvals, the outside date, and the termination terms.
3. Treat a widening spread as information, not as a bargain.
4. Prefer all-cash deals unless you can short the acquirer.
5. Study failed deals. They drive the result, and their aftermath can be a trade.
6. Wait for forced selling to finish before a rebound trade. The author says he entered and exited Rogers too early.
7. In a crisis, "almost all correlations go to one".

## Connects To
- **Ch 3**: Harold Hamm's insider buying at Continental Resources became a go-private arbitrage.
- **Ch 4**: tender offer mechanics.
- **Ch 5**: SPAC deals fail more often (a little over 9%) than merger deals (5%).
- **Ch 6**: Biohaven / Pfizer combined a merger spread with a spinoff.

## Extraction Notes
Five images are lost: Image 2.1 (Twitter deal timeline), 2.2 (Activision spread), 2.3 (Merger Arbitrage Tool), 2.4 (deal success, failure and new offers by year, 2010 to 2022), 2.5 (Willis Towers Watson price chart). The year-by-year counts in Image 2.4 are not in the text. Only the 95% and 5% totals are. The chart from the Cretin paper is described and not reproduced. The chapter also has a primer on options and on bonds, which is omitted here.
