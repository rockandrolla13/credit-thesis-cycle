# Patterns: Capital Flows and Crises (Eichengreen)

Concrete techniques from the book. Each is stated so it can be applied.

## Four-Context Lending Boom Template
**When to use**: judging whether a surge of cross-border lending is well founded (Ch 2).
**How**: assess the economic context (upswing or rebound), the commercial context (is trade growing faster than output), the political context (do lender governments stay at arm's length), and the financial context (instrument, intermediary, innovation). Then name the lender-country shock that could stop the flow.
**Trade-offs**: qualitative. It ranks episodes but gives no threshold.

## Countercyclical Flow Test
**When to use**: deciding whether capital flows stabilize or destabilize a borrower (Ch 2).
**How**: check whether the lender's capital exports rise or fall when its own economy and import demand weaken. Pre-1914 Britain: rise. 1920s United States: fall.
**Trade-offs**: depends on the lender's monetary regime, which can change.

## Exchange Market Pressure Crisis Dating
**When to use**: building a crisis sample that includes repelled attacks and excludes orderly realignments (Ch 5, Ch 6).
**How**: EMP = a x %change in exchange rate + b x change in interest differential - g x relative %change in reserves, all against a reference country. Set weights to equalize component volatilities. Flag quarters above the mean by 1.5 (Ch 6) or 2 (Ch 5) standard deviations. Apply an exclusion window of one or two quarters.
**Trade-offs**: ad hoc weights. Reserves data miss swaps, forwards and third-party intervention. Quarterly data miss short attacks.

## Event Study Against Tranquility
**When to use**: describing how variables behave before and after an episode type (Ch 5).
**How**: plot mean deviations from tranquil-period values for eight quarters either side, with a band of two standard deviations. Compare episode types by differencing.
**Trade-offs**: univariate. Follow with a multinomial logit across all episode types.

## Contagion Probit With Weighted Crises Elsewhere
**When to use**: testing for contagion and its channel (Ch 6).
**How**: regress the crisis indicator on a dummy for a crisis elsewhere plus domestic controls. Then replace the dummy with crises weighted by trade links and by macro similarity. Reduce collinear similarity measures to one factor. Enter all three together.
**Trade-offs**: cannot fully exclude common shocks. Year effects halve the estimate.

## Interaction Test for Contingent Effects
**When to use**: asking whether a policy helps only under some condition (Ch 4).
**How**: add policy x condition to the regression. A negative level term and positive interaction means harm when the condition is weak. Vary period, weights, instruments and the policy measure before believing it. Split composite conditions (Sachs-Warner) into parts.
**Trade-offs**: multicollinearity between the level terms and the interaction.

## Zone of Vulnerability Screen
**When to use**: judging whether a peg can be defended (Ch 8, Ch 9).
**How**: check unemployment, bank health, short-term and foreign-currency debt, and rate-sensitive household or public debt. Then ask what event could lower the reward for holding the peg.
**Trade-offs**: identifies who is exposed, not when the attack comes.

## Out-of-Sample Early Warning Check
**When to use**: testing whether a new crisis resembles old ones (Ch 8).
**How**: apply coefficients estimated on earlier crises to the new sample. Rank countries. Then drop variables that may be effects of an expected crisis (short-term debt, reserve loss) and re-rank. Countries hit but ranked low are contagion candidates.
**Trade-offs**: one cross-section. Debt definitions must match the financial structure.

## Boom-Bust Mirror Comparison
**When to use**: testing a claim that a crisis is unprecedented (Ch 7).
**How**: line up two episodes on context, center-country rates, guarantees, public finances, state banks, saving, exchange rate policy, outbreak and aftermath. Mark where they differ.
**Trade-offs**: two cases. The differences (here, the rescue) carry as much information as the parallels.

## Imputed Saving Proxy
**When to use**: estimating saving where national accounts are missing (Ch 7).
**How**: saving = investment + current account, with investment proxied by investment-good imports and the current account by the trade balance and debt service.
**Trade-offs**: rough. The source is inconsistent on the sign of the debt service term.

## Capital Account Sequencing
**When to use**: advising on, or grading, a liberalization path (Ch 11, with Ch 4).
**How**: domestic financial reform and macro stabilization first, then FDI and foreign bank entry, then stock and bond markets, then offshore bank borrowing. Use price-based inflow taxes. Pair with a hard peg or a float.
**Trade-offs**: barriers reduce pressure to reform. Securities markets are slow to build, so flows may wait for the banks.

## Chilean-Style Inflow Tax
**When to use**: lengthening the maturity of foreign borrowing during the transition (Ch 3, Ch 10, Ch 11).
**How**: require an unremunerated deposit on all capital imports for a fixed period (Chile: 30 percent for one year). Apply to every borrower so that banks cannot route around it.
**Trade-offs**: does not reduce total inflows. Some avoidance. Effectiveness is debated.

## Three Lines of Defense
**When to use**: deciding whether prudential capital controls are warranted (Ch 10).
**How**: check bank owners' capital and subordinated debt, then regulators' capacity and independence. Where both are weak, limit foreign borrowing.
**Trade-offs**: controls must not discriminate among banks, and must not become a reason to delay reform.
