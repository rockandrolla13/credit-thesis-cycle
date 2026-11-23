# Patterns and Techniques

Each technique belongs to the named contributor. The volume's authors disagree. Disagreements are listed at the end.

## Sovereign spread model with residual as stress gauge (d'Arvisenet, Ch 1)
**When to use**: separating fundamental from non-fundamental spread moves in a currency union.
**How**: panel GLS of the ten-year spread over the Bund on debt service ratio, fiscal effort, growth, liquidity (share of area treasury debt), a global risk factor (US corporate spread) and risk x debt-service squared. Published fit: `S = -0.78 + 0.02 R x DS^2 - 0.09 FE - 0.09 Y - 0.102 L + 0.25 R + 0.15 DS`, R2 0.67.
**Trade-offs**: valid to 2010 Q4 only. Later residuals reached 750 bp for Greece. Debt/GDP and debt service cannot enter together.

## OCA screening by supply-shock correlation (d'Arvisenet, Ch 1)
**When to use**: judging fit for a single monetary policy.
**How**: identify supply and demand shocks (Blanchard-Quah, Bayoumi-Eichengreen), correlate supply shocks with the core, and measure the share of adjustment completed in two years.
**Trade-offs**: output-gap correlations in Ch 9 give a different grouping.

## Competitiveness-adjusted debt ratio (Gros and Alcidi, Ch 2)
**When to use**: debt sustainability where an internal devaluation is pending.
**How**: adjusted ratio = headline ratio x (country GDP deflator index / benchmark index), base year 1999.
**Trade-offs**: sensitive to base year (1995 gives Greece 205 instead of 190) and benchmark (Germany gives 228).

## Growth-interest differential for sovereign and corporates (Gros and Alcidi, Ch 2)
**When to use**: flow test of debt-service capacity.
**How**: nominal GDP growth minus ten-year yield for the state, minus the new 1-5 year loan rate for firms. Compare boom and bust periods.
**Trade-offs**: economy-wide growth hides the squeeze on domestic-services SMEs.

## Growth decomposition under a programme (Anderson and Stallings, Ch 3)
**When to use**: explaining an output path during fiscal adjustment.
**How**: export effect = export volume growth x domestic value-added in exports over GDP. Fiscal headwind = change in cyclically adjusted primary balance x multiplier (0.4 Ireland, 1.0 Greece). Remainder = other. Then split the debt-ratio effect into denominator and numerator parts.
**Trade-offs**: the multiplier is assumed from other studies, not estimated.

## Three-channel implied default probability comparison (Christodoulakis, Ch 4)
**When to use**: reading disagreement between bonds, CDS and ratings.
**How**: invert a bond pricing formula (Poisson default), the Hull-White CDS model, and map average ratings to S&P five-year default frequencies. Test for forecast breakdowns (Giacomini-Rossi). Rank relative pessimism (Komunjer-Owyang) into regimes RR1, RR2, RR3.
**Trade-offs**: the chapter gives regimes only, no estimates.

## Net debt relief accounting (Xafa, Ch 5)
**When to use**: valuing a restructuring.
**How**: gross relief = tendered face value x haircut. Subtract recapitalization of domestic banks. Add buyback relief = face retired minus cash cost. Greece: 106 - 38 = 68, plus 21, equals 46% of GDP.
**Trade-offs**: says nothing about the ratio if GDP keeps falling.

## Local-law restructuring with retrofitted CACs (Xafa, Ch 5)
**When to use**: debt mostly under domestic law.
**How**: single-option offer, high acceptance threshold, statute inserting CACs into local-law bonds, sweetener in highly rated notes, GDP warrant.
**Trade-offs**: foreign-law series produce holdouts. A CDS credit event is triggered.

## Central bank loss flow analysis (De Grauwe, Ch 6)
**When to use**: assessing the fiscal cost of central bank bond purchases.
**How**: trace interest from the issuer to the central bank and back to treasuries by capital share, with and without default and recapitalization.
**Trade-offs**: transfers arise if bond rates differ. Inflation and moral hazard remain real risks.

## Privatization plan reality check (Christodoulakis, Ch 7)
**When to use**: assessing programme privatization revenue.
**How**: classify assets (company stakes, infrastructure, real estate, state rights), match each to a mode (sale, IPO, strategic investor, concession), allow for studies, competition clearance and legislation, and compare the target with historical proceeds.
**Trade-offs**: realism lowers headline financing.

## Stability gap and alternative potential output (Mathieu and Sterdyniak, Ch 8)
**When to use**: testing whether a deficit is structural.
**How**: stability gap = primary balance minus net debt x (interest rate less trend growth). Recompute structural balances assuming the crisis did not cut potential growth.
**Trade-offs**: rests on the authors' assumption that half the lost output is recoverable.

## Cyclical transfer scheme, balanced each period (Bernoth and Engler, Ch 9)
**When to use**: designing risk sharing without a large central budget.
**How**: fixed per-capita or per-worker contribution. Receipts proportional to the deviation of the national output gap, or of short-term unemployment, from the area average. Add fiscal rules and conditional entry.
**Trade-offs**: stabilizes small members more. Can raise volatility in stable members. Output gaps are revised.

## Fiscal solvency regression (Mody, Ch 10)
**When to use**: measuring how hard fiscal policy reacts to debt.
**How**: primary balance/GDP on lagged debt/GDP and output gap, by period and group. Euro area 2008-13: debt coefficient 0.14 against -0.01 outside.
**Trade-offs**: a high coefficient in recession signals pro-cyclicality.

## Announcement event study on spreads (Mody, Ch 10)
**When to use**: testing claims that restructuring news causes contagion.
**How**: abnormal change = actual spread change minus the prior 20-day average change, cumulated over five days and scaled by recent volatility.
**Trade-offs**: not proof of causality.

## Sovereign cocos (Mody, Ch 10)
**When to use**: pre-committing to restructuring.
**How**: contract trigger on lagged debt/GDP (or official assistance). First step maturity extension, further thresholds tie payments to outcomes.
**Trade-offs**: moral hazard, higher borrowing cost, legacy debt still needs exchanges.

## Default vs insolvency gap (Ganguin, Ch 11)
**When to use**: locating corporate stress.
**How**: compare rated-firm default rates with national insolvency indices.
**Trade-offs**: few rated firms in Greece and Portugal.

## Bank strength by leverage and distance-to-default (Blundell-Wignall and Roulet, Ch 12)
**When to use**: judging whether banks can support recovery.
**How**: core Tier 1 over total IFRS assets, target at least 5%. DTD above 3 standard deviations.
**Trade-offs**: ignores risk weights by design.

## Financial trilemma and loop mapping (Tsibanoulis and Kounadis, Ch 13)
**When to use**: assessing institutional reform.
**How**: check which of stability, integration and national control is given up, and which loop (sovereign-bank, deposit-bank, austerity-debt) a measure breaks.
**Trade-offs**: legal analysis, no quantification.

## Recorded disagreements
- Fiscal federalism: for (Ch 1, Ch 9, Ch 12). Against (Ch 8). Politically unavailable and insufficient without default rules (Ch 10).
- Sovereign debt: make it safe by ECB guarantee (Ch 8) or cap yields (Ch 12). Price it as risky with automatic restructuring (Ch 10).
- Timing of Greek restructuring: earlier would not have worked (Ch 5). Delay was the main error (Ch 4, Ch 10).
- Deauville: widened spreads (Ch 5). Effect small and transient (Ch 10).
- Internal devaluation: unavoidable (Ch 2). Failed (Ch 13).
- Market pricing: used as a working assumption (Ch 4). Rejected (Ch 6).
