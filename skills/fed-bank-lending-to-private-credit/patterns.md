# Patterns: Bank Lending to Private Credit (FEDS Notes)

Each pattern is the authors' method. "Sec" = main note. "C Sec" = companion note.

## Committed versus drawn check
**When to use**: any time a bank exposure number is quoted. (Sec 3.1)
**How**: (1) Ask whether the number is committed or utilized. (2) Ask whether it covers revolvers, term loans or both. (3) Ask which lenders: Y-14 banks, all US banks, all lenders. (4) Ask which vehicles: BDCs, PD funds, private equity, all NBFIs. (5) Attach the quarter.
**Trade-offs**: slow. But the note's own figures run from $56 billion to $322 billion depending on these four choices.

## Vehicle matching in loan-level data
**When to use**: finding private credit vehicles in a loan register with free-text borrower names. (Sec 2.1)
**How**: (1) Start from an authoritative list (SEC BDC list, Preqin manager list). (2) Match on a hard identifier first (TIN). (3) String-match names and tickers. (4) Add keyword regex ("private credit", "direct lending"). (5) Verify every match by hand. (6) Report coverage against sector assets.
**Trade-offs**: needs the confidential register. Coverage for PD funds is unknown: the note gives a ratio only for BDCs.

## 10-Q debt commitment extraction (public route)
**When to use**: measuring a BDC's bank funding without supervisory data. (Sec 2.2, Sec 3.2)
**How**: (1) Search the 10-Q for SEC-provided tags that indicate debt commitments. (2) Follow each tag's identifier to related fields. (3) Cross-check the commitment total against reported aggregate debt. (4) Collect lender names by hand. (5) Classify the lead arranger: US bank, foreign bank, foreign non-bank, unknown.
**Trade-offs**: worked for 74 of 127 asset-reporting BDCs. Some BDCs report only outstanding debt. No fourth-quarter 10-Q exists: use the 10-K.

## Sample-to-sector scale-up
**When to use**: turning a partial sample into a sector total. (Sec 3.2)
**How**: (1) Sum outstanding debt in the sample. (2) Compute utilization where commitments are reported. (3) Assume that utilization holds for all. (4) Assume commitments per dollar of assets hold for all. (5) Scale to sector assets. (6) Compare with the supervisory total to get the large-bank share.
**Trade-offs**: two representativeness assumptions. The authors state both. The result is an estimate ("around $87 billion").

## Relative loan-quality comparison
**When to use**: judging whether a lender segment is riskier than its peers. (Sec 3.3)
**How**: compare the segment with a named comparison group on six measures: commitment, utilization, interest rate, time to maturity, rating, delinquency. Then compare default probability by rating bucket, mean and median, with the share of observations in each bucket.
**Trade-offs**: all risk measures are the lending banks' own. Mean and median can disagree, as they do for PD funds.

## Borrower leverage tracking
**When to use**: watching whether vehicles fund deals with more debt. (Sec 3.3)
**How**: total debt over total assets for listed BDCs, set against other NBFIs over time.
**Trade-offs**: public BDCs only (40 names). Nothing for PD funds.

## Concentration and similarity pair
**When to use**: deciding whether a shock to some borrowers is a one-bank problem or a system problem. (Sec 4.1)
**How**: (1) HHI of each bank's commitments across borrowers, averaged across banks. (2) Cosine similarity of commitments for each pair of banks, averaged across pairs. (3) Read together: concentrated but dissimilar means idiosyncratic shocks hit banks unevenly.
**Trade-offs**: says nothing about correlated drawdowns. The authors move to a stress test for that.

## Full-drawdown stress on capital and liquidity
**When to use**: bounding the direct hit to banks from a run on credit lines. (Sec 4.2, fn 9)
**How**: (1) Undrawn amount = committed minus drawn. (2) CET1: add undrawn amount × 0.5 to risk-weighted assets. Hold the numerator. (3) LCR: subtract the drawn amount from high-quality liquid assets. Subtract 40 percent of it from the outflow base. (4) Recompute both ratios. (5) Widen the borrower set (the note adds private equity funds) and repeat.
**Trade-offs**: aggregate ratios only. No credit losses. No drawdowns by other NBFIs. The authors label it an upper bound for private credit vehicles alone.

## Indirect-channel inventory
**When to use**: after the direct numbers look small. (Sec 5)
**How**: list the bank's other links: affiliated vehicles and minority stakes, partnerships, warehouse lines, originate-to-distribute flows, first-lien and second-lien splits, synthetic risk transfers. For each risk transfer, ask whether the bank also lends to the protection seller.
**Trade-offs**: the note offers no data for any of these.

## Financial Accounts lookup
**When to use**: system-wide levels and flows from public data. (C Sec 4)
**How**: (1) Vehicle balance sheets: S.124.8 (PD funds), S.124.5 (BDCs), S124.6 (interval and tender offer funds), S125s1.3 (ABS issuers, for MM CLOs). (2) Loans by lender and borrower: F4.4.s. (3) Fund share holders: F522.3.s. (4) From-whom-to-whom detail: Data Download Program or FRED. (5) Bank funding: the "Depository institution loans n.e.c." liability line of each vehicle sector.
**Trade-offs**: sector totals only. Form PF funds are classified by staff judgement. Annual filers are imputed and interpolated. Borrower sectors for PD funds are assumed from BDC and CLO data. Loans may include some syndicated loans.

## Vintage check on business debt
**When to use**: comparing nonfinancial business debt or leverage across time. (C Sec 3, C Sec 5)
**How**: confirm the Z.1 vintage. Before September 2026, private credit loans to corporates sat in miscellaneous liabilities, outside debt. After, they are debt. Compare like with like.
**Trade-offs**: none. Skipping it creates a false jump of about 5 percentage points of GDP.
