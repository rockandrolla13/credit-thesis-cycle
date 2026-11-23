# Patterns and Techniques

Each pattern is the authors' method. Section numbers refer to `chapters/`.

## 1. Loss-allocation map for an off-balance sheet structure (Sec 2)
**When to use**: a deal claims an investment-grade rating on an asset whose tenant is not the borrower.
**How**:
1. Name the owner of the asset (the vehicle).
2. List the lenders: bondholders, construction banks, banks that lend to the bondholders.
3. List the income contracts: leases and offtake, with initial term and renewal options.
4. List the contingent supports: residual value guarantees, lease backstops, vendor support. Record each cap.
5. Follow the stress path: non-renewal, re-let or sale, capped guarantee, loss to holders, loss to their bank lenders.
6. Sum each party's exposure to the same ultimate guarantor across all its holdings.
**Trade-offs**: the source says the contingent claims "are harder to size than bonds". The map shows direction, not amounts.

## 2. Three-layer credit transformation check (Sec 2)
**When to use**: judging how a vehicle's debt reached investment grade.
**How**: separate the three layers. (1) The building, power connection and cooling plant, which can be re-let. (2) The chips, which are "arguably less robust as collateral". (3) Guarantees, which are residual and capped.
**Trade-offs**: chip values are correlated across holders because many firms hold the same vendor's hardware.

## 3. Sponsor spread versus vehicle spread (Sec 2)
**When to use**: pricing the flexibility a hyperscaler buys by not owning the asset.
**How**: compare the vehicle's bond spread with the tenant's own bond spread at similar maturity. Hyperion: 225 bp against 88 bp (20-year) and 98 bp (30-year), two weeks apart.
**Trade-offs**: one example, two weeks apart, different ratings by one notch. The source gives it as an illustration.

## 4. Good boom, bad boom benchmark (Sec 1)
**When to use**: placing the pace of a debt build-up against history.
**How**: index credit to 100 at the boom start. Compare with the mean paths of past good and bad booms from Gorton and Ordoñez (2020), 37 countries. For AI firms, index each firm's debt to 100 in Q3 2025 and take the median.
**Trade-offs**: the paths of good and bad booms look alike on average until the productivity outcome is known. The benchmark sizes pace. It does not classify.

## 5. Event study of supply news on the term premium (Sec 3)
**When to use**: testing whether a sector's debt supply moves benchmark yields.
**How**:
1. Build a dated list of news sessions. Move after-close releases to the next session.
2. Regress the daily change in the 10-year term premium on a news-day indicator.
3. Control for the change in the two-year yield and FOMC statement days.
4. Use Newey-West standard errors (four lags).
5. Robustness: a later sub-sample, a narrower event definition, added controls (post-FOMC session, long Treasury auctions, change in VIX).
6. Plot the cumulative relative change from session -1 to +5 to test persistence.
**Trade-offs**: "event-day associations, not causal effects". News can be anticipated or can coincide with other events. The sample here is 18 days.

## 6. Curve-shape test for a duration channel (Sec 3)
**When to use**: checking that a yield move is about duration risk and not policy expectations.
**How**: run the news-day regression at each maturity of the zero coupon curve with the same controls. A response that rises with maturity is consistent with a duration channel. Here the 90% band excludes zero from 8 to 30 years.
**Trade-offs**: consistent with the channel, "not causal evidence".

## 7. Credit-spread placebo (Sec 3)
**When to use**: checking whether supply news reaches the wider investment-grade market.
**How**: swap the dependent variable for the daily change in the ICE BofA US corporate IG option-adjusted spread. Result: 0.13 bp, standard error 0.24, not significant.
**Trade-offs**: an index-level daily test. It says nothing on single names or on the vehicles' private debt.

## 8. Issuance-share pressure gauge (Sec 3)
**When to use**: tracking whether the load on duration investors is growing.
**How**: divide the sector's gross issuance at maturities of 10 years or more by (a) corporate issuance at those maturities and (b) gross Treasury issuance. 2024: about 3% and 1.5%. 2026 to date: about 24% and 13%.
**Trade-offs**: excludes off-balance sheet vehicle debt, which adds "further long-dated claims". The source gives no threshold.

## 9. Debt-equity pricing gap (Sec 4)
**When to use**: testing whether lenders and shareholders agree on a sector's risk.
**How**: compare loan spreads, maturity, size and security for the sector against all other borrowers, with controls. Then set the result against the sector's equity valuations. AI loans: 6.2 pp against 6.1 pp spread.
**Trade-offs**: the test says one market is wrong. It does not say which.

## 10. Capex against free cash flow crossover (Sec 4)
**When to use**: dating the point where a cash-funded sector needs external finance.
**How**: track capex to revenue, free cash flow to assets, and the level of capex against free cash flow. The switch to debt follows when free cash flow lags capex.
**Trade-offs**: asset-weighted averages over five firms can hide a single weak firm.

## 11. Investment boom scale and aftermath comparison (Sec 4)
**When to use**: sizing the macro cost if the investment stops.
**How**: measure the rise in investment as a share of GDP. Compare with past booms. Then compare GDP growth one year and five years after each boom with growth during it.
**Trade-offs**: seven booms. The smallest boom relative to GDP (dot-com) had the largest contraction, so size alone does not rank the damage.

## 12. Shock transmission channels for shadow borrowing (Sec 5)
**When to use**: stress-testing a vehicle structure.
**How**: check three channels. Refinancing pressure at the vehicle. Procyclical shifts in private credit appetite. Activation of guarantees.
**Trade-offs**: the box lists the channels without sizing them.
