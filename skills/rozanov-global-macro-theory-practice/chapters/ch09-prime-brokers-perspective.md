# Chapter 9: Global Macro: A Prime Broker's Perspective

**Author**: Barry Bausano, Deutsche Bank Securities (pp. 163-179)

## Core Idea
Macro funds trade every product, so their financing was split across many single-product clearers. The chapter traces how prime brokerage moved from collateral-based equity lending to risk-based portfolio margining across products. It also covers what 2008 and the regulation that followed did to counterparty choice and to the cost of leverage. It describes market plumbing. It gives no trading method.

## Frameworks Introduced
- **Classic prime brokerage** (p. 165): one account to settle, clear, margin and report equity trades done with several brokers. The broker gives locates, lends stock for shorts and finances longs.
- **Four changes since the early 2000s** (pp. 165-169):
  1. *Globalisation*: emerging and frontier markets with their own settlement and currency rules. The broker's footprint became a selection factor.
  2. *Product expansion*: funds crossed asset classes with more complex instruments. Funds prefer to settle and finance with the executing broker, so execution share and financing share became concentrated in a few global firms.
  3. *Leverage availability*: synthetic equity finance, derivatives, cross-product margining. Prime finance changed "from a collateral-based agency lending business into a risk-based portfolio margin business".
  4. *After 2007-09*: focus on the size and stability of the broker's balance sheet.
- **Three sources of added leverage** (pp. 167-169):
  - *Synthetic equity finance*: the financier owns the asset and swaps the return to the client. This passes the 50% margin of "Regulation T". It made statistical arbitrage and similar "micro" strategies viable.
  - *ISDA derivatives*: margin is set from expected volatility of the position and from estimated liquidity, that is "the potential market moves that could transpire in the time required to exit the risk". Initial margin plus daily, sometimes intra-day, variation margin.
  - *Cross-product margining*: measure offsetting risks across legs and "assign margin to the net exposure".
- **The clearing and financing channels a macro fund used** (pp. 170-174):

  | Channel | How it works | Note |
  |---|---|---|
  | FX prime brokerage | Client trades on the broker's credit lines with many dealers. Positions and collateral consolidate | Born by the early 1990s |
  | Futures clearing merchant | Clears and settles listed futures, takes margin, posts to the exchange | Main clients: systematic macro, CTAs |
  | Repo | Client buys a bond and lends it back for cash less a haircut. Leverage "is determined by the size of the required haircut" | Trade-by-trade, not portfolio-based |
  | Derivatives intermediation | Client trades OTC swaps in the broker's name | "A credit enhancement transaction masquerading as an operational function". Curtailed after 2008 |
- **Post-crisis selection criteria for a financing counterparty** (p. 170): multi-currency deposit base, statutory access to central bank liquidity, size and strength at home, low credit default spreads, and having come through the crisis with little damage.
- **Regulatory aims** (p. 175), across Dodd-Frank, EMIR, MiFID and Basel III:
  1. More reporting.
  2. Central clearing for most derivatives.
  3. Higher capital cost for uncleared derivatives.
  4. Regulated execution.
- **The author's expected effects** (pp. 176-177), written in 2012:
  - Cleared trades are independently collateralised. Clearing houses take only "high-quality sovereign debt or cash". He expects a "significant drain on aggregate market liquidity" and money market distortions.
  - "Products that are less liquid, or that require longer duration and term financing, will all become more expensive to leverage."
  - Lower leverage in the system, changed valuations for those assets, and lower return expectations for strategies using term finance and illiquid assets.
  - Leveraged relative value between structured and basic instruments becomes harder. Successor strategies will be "low leverage and low turnover".
  - Liquid flow products gain. Systematic macro, managed futures and tactical trading "will become more prominent".
- **Six criteria for a dominant prime broker** (pp. 178-179): broad geography, broad product suite, large diversified balance sheet with central bank access, top-tier equity prime business, top-tier listed and OTC clearing, strong transaction banking.

## Key Concepts
- **Locate**: confirmation that stock can be borrowed for a short sale.
- **Haircut**: the margin withheld in a repo.
- **Reverse repo**: lending cash to borrow a security for delivery on a short.
- **Variation margin**: collateral moved as the trade's market value changes.
- **Swap execution facility (SEF)**: the automated venue required for clearing-eligible contracts. The European equivalent is the organised trading facility.
- **Latency**: transaction speed. Co-location reduces it.
- **Quant quake**: August 2007, when small moves in gross exposures hit leveraged equity market-neutral books (p. 168).

## Mental Models
- Think of leverage as something the financing structure grants, not something the strategy owns. When margin methods change, strategies appear or disappear.
- Being market "flat" is not being risk flat. Buying from dealer A and selling to dealer B leaves two credit exposures (p. 169).
- "A hedge was only valuable if the counterpart performed on their obligation."
- Concentration is the manager's trade-off: fewer counterparties give efficiency and netting. More give safety. The largest macro managers put "more than 80%" of business with their top two or three (p. 179).

## Anti-patterns
- **Ignoring counterparty credit in calm years**: the pre-2008 decade had no broker-dealer failures and produced "an emphasis on market risk to the exclusion of credit risk".
- **Reading notional as risk, or the reverse**: a hedged package can carry far less risk than its legs suggest. A highly leveraged "narrow slice" can carry far more than its net suggests.
- **Relying on a product that is "too-good-to-be-true"**: derivatives intermediation.
- **Margining offsetting legs separately**: the author's 1993 and 1999 fund launches needed one clearer per product. It was "operationally cumbersome and capital inefficient".

## Worked Example
*1. Russian GKOs, 1998* (pp. 169-170).
- Position: long high-yielding Russian Treasury bills (GKOs). Currency hedge: put options on the rouble.
- Event: at the height of the crisis "many option writers declared force majeure" and did not pay.
- Result: losses on the defaulted GKOs with no offset from the puts. "Counterparty credit risk exposure overwhelmed the market risk of the trade."

*2. Cross-product margining on a convertible bond* (p. 169).
1. Buy a convertible whose implied volatility is cheap against expected realised volatility.
2. Sell a delta-weighted amount of the issuer's equity.
3. Hedge rate risk with an interest rate swap.
4. Hedge residual credit risk with a credit default swap.
5. The net risk "may be far less than a cursory examination of all the notional trade legs might suggest". Margin is set on the net.
The chapter gives no numbers for this example.

*3. Expressing one view through many products* (p. 166). A view on the European sovereign crisis could go through currencies, sovereign debt, CDS on financial sector debt, or options on exporters' shares. In 2007-09 many macro managers expressed a negative US housing view through synthetic CDO tranches.

## Key Takeaways
1. Check who the counterparty to the hedge is and whether it can pay in the scenario the hedge is for.
2. Financing terms decide which relative-value strategies exist.
3. Collateral rules create demand for government bonds as collateral.
4. The author expected regulation to cut leverage most where assets are illiquid or need term funding.
5. Post-2008, a broker's access to central bank liquidity became a selection criterion.

## Connects To
- **Ch 2**: counterparty diligence from the manager's side.
- **Ch 7**: basis risk and liquidity principles.
- **Ch 10**: how to measure the leverage these facilities create.
