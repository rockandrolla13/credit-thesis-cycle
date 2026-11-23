# Chapter 19: The Subprime Chain

## Core Idea
Securitization replaced the bank loan officer with a long chain of fee-earning intermediaries. No link screened or monitored the borrower. Cassidy's verdict: "Far from solving the hidden-information problems that Akerlof had identified, the industry had simply ignored them." The belief that the chain's self-interest would work out well was "the illusion of harmony". This is a historical case study of the US subprime industry, 1980 to 2007.

## Frameworks Introduced
- **The mortgage chain** (Figure 19.1, recovered from EPUB image 00004.jpg). Nodes and flows as drawn:
  1. **Mortgage brokers** give advice to the **home buyer** and receive fees from the **mortgage lender**.
  2. The **mortgage lender** gives loans to the home buyer and receives interest.
  3. The **Wall Street bank** gives (warehouse) loans to the mortgage lender and receives mortgages.
  4. The Wall Street bank pays fees to the **rating agencies**, which give AAA/AA ratings to the **RMBS/CDOs**.
  5. The Wall Street bank passes mortgages to **warehouses/conduits**, which link to the RMBS/CDOs.
  6. **Investors** pay cash for RMBS/CDOs and receive interest.
  7. **SIVs** hold RMBS/CDOs and fund themselves by selling ABCP to investors for cash.
  8. **Insurers/financial firms** write CDSs for investors and for SIVs.
  - How to use: for each link ask who is paid by volume, who bears the default, and who can see the borrower. In this chain payment was by volume at every link, and the loss sat at the far end.
- **Adverse selection in lending and the old remedy**: applying for a high-interest loan signals that the applicant badly needs money and could not get a regular loan. Banks dealt with this by **rationing**. Below a minimum standard, no loan.
  - The subprime alternative was **risk-based pricing**: many rates by FICO score and down payment. Greenspan (April 2005) said lenders could now "quite efficiently judge the risk posed by individual applicants and … price that risk appropriately".
- **Wall Street's three protections for RMBS investors**:
  1. **Diversification**, here by geography. Falling prices in one state are offset by rising prices elsewhere. This protects against **idiosyncratic risk** (Harry Markowitz), not against a common fall.
  2. **Subordination**: four classes, super senior, senior, mezzanine, and junior (equity). Losses hit junior first, then mezzanine, then senior.
  3. **Excess spread**: mortgage payments at first exceed interest paid to investors. The difference builds a reserve fund.
- **Issuer-pays conflict and rating shopping**. Rating agencies are "a private-sector solution to the problem of hidden information". Since the 1970s issuers have paid them.
  - Steps to failure: (1) structured products pay three or four times the fee, (2) agencies advise banks how to structure deals to reach investment grade, (3) bankers play agencies against each other, (4) per Jerome Fons, originators "typically chose the agency with the lowest standards, engendering a race to the bottom".
  - Regulatory lock-in: **risk-weighted capital requirements** in the 1980s and 1990s tied bank capital to credit ratings. The agencies "replaced government officials as the primary monitors of bank balance sheets".
- **Balkanized regulation**: several agencies supervised parts of the same industry, and sometimes of the same firm. They "engaged in turf wars", so firms could play one against another.

## Key Concepts
- **Subprime**: generally, loans to borrowers with a FICO rating below 640. The typical subprime borrower in 2006 scored 623 (New York Fed study).
- **Warehouse loans**: Wall Street credit lines that funded mortgage companies, at 6 or 7 percent against 10 percent or more charged to borrowers.
- **Private label** mortgage-backed securities: those without Fannie or Freddie backing.
- **2/28 hybrid ARM**: a fixed rate (6 or 7 percent, say) for two years, then a floating rate, typically 10 to 15 percent, for twenty-eight years. Payments typically rose 50 to 100 percent at reset. Cassidy: "really just leveraged bets on the direction of house prices".
- **RMBS as a mutual fund, CDO as a fund of funds**: Cassidy's analogy. A CDO combines pieces of many RMBSs.
- **Predatory lending**: exploiting the lender's information advantage over an unsophisticated borrower.
- **Enabling laws**: Depository Institutions Deregulation and Monetary Control Act of 1980 (ended rate caps), Alternative Mortgage Transaction Parity Act of 1982 (variable rates, balloon payments), Tax Reform Act of 1986 (kept only mortgage interest deductible).

## Mental Models
- Compare with the old model. Beneficial kept its loans and capped combined first and second mortgages at 80 percent of property value. Holding the loan "gave them an incentive to be careful".
- A higher yield for the same rating is a warning. An AAA bond from IBM might yield 5.5 percent while an AAA subprime security yielded 5.75 or 6 percent.
- Treat an earlier bust that was ignored as evidence of the incentive problem. In 1997-1998 six of the top ten subprime lenders failed or were sold. Big banks bought the survivors "on the cheap".
- Officials saw only a micro issue. Convinced the system was stable, they treated subprime problems as about access to credit, not about the whole economy.

## Anti-patterns
- **Relying on the seller's representations**: Wall Street banks mostly relied on lenders. Investors relied on ratings.
- **Approving whatever the software passes**: automated prequalification with compliant underwriting.
- **Volume targets for originators**: New Century had "a brazen obsession with increasing loan originations" and "no standard for loan quality" (bankruptcy examiner Michael Missal).
- **Praising access while ignoring standards**: even the critic Edward Gramlich called the subprime market "a promising development" in 2007.

## Reference Tables
Subprime volumes (Inside B&C Lending and text):

| Year | Subprime originations | Securitized |
|---|---|---|
| 1995 | $65 billion | about $18.5 billion |
| 1997 | $124.5 billion | about $66 billion |
| 2001 | $173.3 billion | not stated |
| 2002 | $213 billion | not stated |
| 2003 | $332 billion | not stated |
| 2005 (peak) | $625 billion | not stated |
| 2004 to 2006 total | more than $1.7 trillion | more than $1.3 trillion, roughly three quarters |

- Subprime plus Alt-A reached $1 trillion in 2006, about 40 percent of mortgages issued.
- Number of subprime mortgages: 624,000 in 2001 and 3.44 million in 2005.
- Average subprime loan: $151,000 in 2001 and $259,000 four years later.
- In 1999 almost half had a fixed rate. Six years later more than 80 percent were adjustable and more than a quarter interest-only. In 2005-2006 more than two-thirds were 2/28s.

Largest participants:

| Subprime loan issuers, 2005-2007 | | Subprime security issuers, 2005-2006 | |
|---|---|---|---|
| Countrywide | $97.2 billion | Lehman Brothers | $106 billion |
| Ameriquest | $80.7 billion | RBS Greenwich Capital | $99.3 billion |
| New Century | $76 billion | Countrywide Securities | $74.5 billion |
| First Franklin | $68 billion | Morgan Stanley | $74.3 billion |
| Long Beach Mortgage | $65.2 billion | Credit Suisse First Boston | $73.4 billion |

Typical ratings by tranche: super senior and senior AAA, AA or A. Mezzanine usually BB or above. Equity typically unrated.

Fees: Wall Street paid about $206,000 for a $200,000 loan in 2005. It earned $500,000 to $1 million per $100 million of ordinary subprime securities sold, and more on CDOs. Rating a $100 million RMBS cost about $30,000 to $40,000, against about $10,000 for a municipal bond. Structured finance was more than 40 percent of Moody's revenue in 2005.

## Worked Example
**GSAMP TRUST 2006-NC2** (Goldman Sachs, August 2006).
- 3,949 mortgages issued by New Century in the second quarter of 2006.
- Average loan about $223,000. Nearly 90 percent were 2/28 ARMs.
- Two fifths financed purchases. The rest were "cash out" refinancings.
- About half the homes were in California and Florida.
- Average FICO 626. Almost a third were below 600.
Apply the three protections. Diversification fails because half the pool sits in two states and nearly all loans share one reset structure. Subordination and excess spread then face a correlated loss, not scattered ones.

**A predatory loan** (Center for Responsible Lending). An elderly couple with a nearly repaid 1983 mortgage were promised 5 to 6 percent. The loan carried 9.9 percent, an annual percentage rate of 11.8 percent, and 10 "discount points" ($15,289) financed into the balance. Payments were $1,655 a month, about 57 percent of their income. The prepayment penalty was $7,500.

## Key Takeaways
1. Map the chain and find who holds the risk last.
2. Diversification covers idiosyncratic risk only.
3. Ratings paid for by issuers, and written into capital rules, cannot be an independent check.
4. More than $1 trillion of subprime RMBSs and CDOs issued in 2005 and 2006 were mostly rated AAA or AA. Almost all were later "savagely downgraded".
5. Supervision was thin. Thirty California examiners covered nearly five thousand consumer finance companies, with an exam about once every four years (Mark Zandi). More than fifty thousand mortgage broker firms had no federal supervisor.

## Extraction Notes
- Figure 19.1 is absent from the text extract and was read from the image. The image labels flows but not their size.
- The source names the Citigroup acquisition "Associated First Capital" here and "Associates First Capital" earlier in the chapter, and writes "Household Financial" and "Household Finance". Recorded as inconsistencies in the source.

## Connects To
- **Ch 12**: lemons, moral hazard, and why banks screen.
- **Ch 16**: originate-to-distribute and Ponzi finance.
- **Ch 18**: the exotic loans that fed the chain.
- **Ch 20**: CDOs, SIVs and credit default swaps.
- **Ch 21**: the pay incentives at each link.
