# Chapter 20: In the Alphabet Soup

## Core Idea
Three technologies were said to have made finance safe: securitization, statistical risk models, and credit derivatives. Each failed for a stated reason. Pools of similar loans concentrate systematic risk. Value-at-risk measures recent volatility, not disaster. Credit default swaps add unfunded leverage and hide who owes what. This chapter applies the **illusion of predictability** to the US banking system from 2004 to 2007.

## Frameworks Introduced
- **Correlation, not count, gives diversification** (Cassidy): the benefits of diversification "depend on the assets being truly diverse; in a statistical sense, they need to have a low degree of correlation". Subprime pools "simply joined like with like": bubble-area properties and low-rated borrowers.
  - **Systematic risk**: for corporate bonds it is the state of the economy. For mortgage bonds it is the state of the housing market. "Combining subprime mortgages magnified rather than diminished the exposure to this risk."
  - Causal chain: borrowers planned to refinance within two years. That needed rising prices. If prices stalled, they built no equity before reset, could not refinance, and defaulted together.
- **Thin subordination test**: in a typical RMBS the equity and mezzanine layers were less than 10 percent of principal. More than 90 percent was senior or super senior. The structure insulated senior paper "from minor shocks, not a major reversal in the housing market".
  - How to use: compare the subordinate share with a plausible correlated loss rate. If losses can exceed the cushion, the top rating is not safe.
- **Mezzanine CDO**: a CDO built from the junior and mezzanine claims of other mortgage securities. With slices of many RMBSs and enough excess spread, many were rated AAA.
- **Value-at-risk (VAR) and its four failures**. VAR gives a dollar loss that should be exceeded only with a stated probability over a stated period.
  - Simplest method: (1) take past data for the portfolio, (2) compute its standard deviation, (3) assume daily moves follow the normal distribution, (4) read off the loss at the chosen confidence level.
  - Failure 1, conceptual: it redefines risk as volatility and assumes "the future would resemble recent history". Risk as the chance of disaster "is impossible to quantify accurately".
  - Failure 2, calm data: in a tranquil period such as 2002-2006 "virtually any model would have understated the 'tail risk'". There was not enough variation in the data.
  - Failure 3, correlation: models reward diversification using normal-time correlations. Under stress "all correlations go to one".
  - Failure 4, procyclical leverage: falling measured VAR frees capital, so leverage rises just as calm lengthens (worked below).
  - Cassidy's summary: "when it is needed most is precisely when it performs most poorly." Proper role: "a useful adjunct to an overall strategy of controlling risk, not … a substitute for one."
  - David Viniar of Goldman Sachs on its valid use: it shows "what you should expect to happen on a daily basis in an environment that is roughly the same".
- **Credit default swaps as unfunded credit insurance**. A CDS pays the buyer if a borrower defaults, in return for premiums. Cassidy: they "aren't really swaps at all".
  - Leverage effect: sellers took the same default risk as a lending bank but "didn't set aside any capital". Most CDSs were **unfunded**, with no collateral posted. This "effectively added even more leverage to the system".
  - **Network risk**: protection was laid off in chains (Bank A to Bank B to Bank C to a hedge fund). Trades were private with no central repository. "From the outside, it was impossible to determine who owed what to whom." Firms were exposed "several links down the chain" to risk that "couldn't be quantified or hedged".
  - Crisis implication: firms become "justifiably suspicious of each other, and liquidity could quickly dry up".
- **Shadow banks as attached, not independent**: SIVs issued short-term debt and bought long-term assets from their parents. Sponsors gave them guaranteed credit lines, so the assets and liabilities "remained part of their families' overall finances".

## Key Concepts
- **RiskMetrics**: J.P. Morgan's VAR method, traced to Sir Dennis Weatherstone's request for a daily "4:15 report". Published as an industry standard in 1995.
- **Risk-based capital requirements**: from 1996 the BIS let banks use their own VAR models to set capital. Incorporated in the 2004 **Basel II** accord.
- **Fat-tail fixes**: other probability distributions, historical simulation, exponential smoothing, GARCH, Monte Carlo simulation. Cassidy says none solved the basic problem that past data poorly predict extreme moves.
- **Single-name CDS / basket CDS**: protection on one loan or bond, or on a basket.
- **ABX index**: a broad subprime credit index to which some CDSs were linked.
- **Notional value**: the face value of the debt insured.
- **Super senior**: the top tranche, with the lowest interest rate and so the hardest to sell as spreads narrowed.

## Mental Models
- The trader's image of an AAA subprime pool: hundreds of drunks with locked arms, relying "on the fact that they are all falling in different directions".
- Follow Minsky: as a crisis recedes, officials and bankers "believe that a new era has arrived", and warnings "are naturally ignored".
- Use Nassim Taleb's 1997 prediction as a test of a risk report. VAR is "the alibi bankers will give shareholders (and the bailing-out taxpayer)".
- When issuers start keeping what they cannot sell, the market has turned. "They ate their own cooking, and got poisoned."
- Watch spreads against issuance. Subprime spreads narrowed as supply grew, buyers balked, and issuers kept the unsold paper.

## Anti-patterns
- **Tweaking models until the position looks safe**: "it was possible to present virtually any increase in lending as 'safe'".
- **Short data windows**: UBS's VAR models used five years of data, so they included no period of upheaval.
- **Ignoring fundamentals that contradict the model**: UBS relied on VAR "even though delinquency rates were increasing and origination standards were falling".
- **Lending without bearing default risk**: the J.P. Morgan 1997 deal let banks "make loans without carrying all, or perhaps even any, of the risk". Cassidy says this "should have set off alarm bells".
- **Cutting capital at the peak**: the Financial Services Regulatory Relief Act of 2006 passed the House 417 to 15 and the Senate by unanimous consent.

## Reference Tables
GSAMP TRUST 2006-NC2 capital structure, from its prospectus as the text reports it ($882 million issued):

| Rating band | Amount |
|---|---|
| AAA/Aaa | about $700 million |
| AA or A | $124 million |
| BBB+/Baa to BBB-/Baa | $30 million |
| Below BBB- | stated as "$27 billion" (see Extraction Notes) |

Mezzanine and equity together were less than 7 percent of the offering. Pool features: 90 percent adjustable-rate, more than 50 percent with balloon payments, about 38 percent with loan-to-value above 80 percent.

Other figures:

| Item | Figure |
|---|---|
| Subprime over prime RMBS yield, 2001-2003 | 200 to 300 basis points |
| Same, 2004-2006 | 100 to 200 basis points |
| SIV assets linked to big institutions, August 2007 | more than $300 billion. Citigroup's almost $100 billion |
| Retained mortgage assets | UBS $50 billion. Citigroup more than $50 billion in super senior. Merrill Lynch more than $40 billion |
| Credit derivatives outstanding, 2004 (BIS) | about $4.5 trillion |
| CDS notional outstanding, June 2007 (BIS) | $42.6 trillion |
| J.P. Morgan daily VAR, 1994 annual report | $15 million at 95 percent confidence |
| Philippines and Bulgaria bond correlation, 1998 | 0.04 before the crisis, 0.84 during it |

## Worked Example
**How falling VAR doubles leverage (Bank X).**
1. Bank X has $500 billion of assets and a VAR of $25 billion.
2. It holds capital of twice VAR, so $50 billion. Leverage (assets divided by capital) is ten.
3. Markets calm. The risk department reports VAR has halved to $12.5 billion.
4. Required capital falls to $25 billion. Cassidy's simplified end state is assets of $500 billion on capital of $25 billion. Leverage is twenty.
5. Return on equity and probably the stock price rise. The bank is far more exposed to "something unexpected".

**The first CDS deal (J.P. Morgan, 1997).** Morgan placed the credit risk of $9.7 billion of loans to about three hundred corporations in a special-purpose vehicle. Investors, mainly insurers and other banks, did not own the loans. They received about $700 million a year in premiums and would bear the losses on default. Morgan freed capital.

## Key Takeaways
1. Ask what the common risk factor is, and how thick the cushion is against it.
2. Do not accept a risk number without its data window and its correlation assumptions.
3. Count contingent liabilities as leverage.
4. Warnings were on record. Warren Buffett, February 2003: derivatives are "financial weapons of mass destruction", with risk "concentrated in the hands of relatively few derivatives dealers". A small-scale preview came in spring 2005 when General Motors' outlook was cut and CDS spreads jumped.
5. Greenspan (May 2005) still held that "private regulation generally has proved far better at constraining excessive risk-taking than has government regulation". Bernanke did not change the stance.

## Extraction Notes
- The source gives the GSAMP tranche rated below BBB- as "$27 billion". The other tranches and the $882 million total imply $27 million. Recorded as the source states it.
- The source's Bank X example says the bank ends with $500 billion of assets after investing its surplus capital. It does not show the intermediate balance sheet.
- The extract has "equity ranches" for "equity tranches".

## Connects To
- **Ch 7**: Bachelier, the bell curve and Mandelbrot's fat tails.
- **Ch 13**: Keynes on uncertainty, the basis of the conceptual objection to VAR.
- **Ch 17**: the 2000 law that barred CDS regulation, and Long-Term Capital.
- **Ch 19**: how the RMBSs were built and rated.
- **Ch 22**: what happened when the models and the insurance were tested.
