# Chapter 4: Rating Agencies vs. Sovereign Debt Markets: A Tale of Interacting Risk Preferences

**Contributor**: George Christodoulakis (Manchester Business School; the volume's editor). Part I. The chapter summarizes his working paper Christodoulakis (2013). Sample: September 2008 to September 2011.

## Core Idea
Bond spreads, CDS spreads and credit ratings each imply a sovereign default probability, and the three do not agree. Their relative pessimism rotates in regimes after major events. The rotation groups the five periphery countries into three "clubs". CDS-bond interaction drove the escalation everywhere. Only for Greece did the rating agencies end up as the most pessimistic of the three. This chapter is thin: it reports results and gives no estimates or equations.

## Frameworks Introduced

- **Three competing implied default probabilities** (five-year horizon; note 1):
  - Bond PD: invert numerically the pricing formula of discounted expected pay-offs, assuming a Poisson default process.
  - CDS PD: invert the Hull and White (2000) CDS pricing model.
  - CRA PD: map the average Moody's, S&P and Fitch rating in each period to the observed five-year-ahead sovereign default frequency in S&P's Sovereign Foreign Currency Cumulative Average Default Rate table (1975-2011).
  - When to use: to compare what three information channels say about the same sovereign on one scale.

- **Forecast breakdown detection**: Christodoulakis (2013) applies the Giacomini and Rossi (2009) tests to the distance between two competing PD series. A significant rise in distance in a later period is a "sovereign risk forecast breakdown" (note 2).

- **Relative loss profile and relative pessimism**: a forecaster is pessimistic if the loss from under-forecasting risk exceeds the loss from an equal over-forecast. With competing forecasts, judge each against another instead of against outcomes. Estimated with the Komunjer and Owyang (2012) procedure, separately for eight periods.

- **Three preference regimes**, ranked from most to least pessimistic:
  - RR1: bond markets, CDS markets, CRA ratings.
  - RR2: CRA ratings, bond markets, CDS markets.
  - RR3: CDS markets, bond markets, CRA ratings.

- **Three country clubs** (propagation patterns):
  - Hellenic (Greece): RR3 -> RR1 -> RR2. CDS sparked pessimism in Periods 1-4 with CRAs least pessimistic. Bond markets were most pessimistic for the next three periods. CRAs became most pessimistic in Period 8.
  - Latin (Portugal, Spain, Italy): RR3 for about the first half, then one switch to RR1 for the second half. CRAs stayed least pessimistic throughout.
  - Celtic (Ireland): frequent switching between RR1 and RR3, never RR2. CRAs "rather passive".

## Key Concepts
- **CRA**: credit rating agency (S&P, Moody's, Fitch).
- **Implied probability to default**: the PD backed out of a price or rating, assuming the pricing model is right and the market efficient.
- **Pessimism / conservatism / prudence**: used interchangeably (note 3).
- **Forecast breakdown**: a statistically significant widening between two risk views.
- **Policy hubris**: declaring unsustainable debt sustainable because the official regime (fast fiscal adjustment plus conditional support) works only for sustainable debt.
- **Self-fulfilling crisis**: more likely in the euro area because of the structural features below.

## Mental Models
- Before 2008, euro-area spreads moved on common factors and global risk aversion. After 2008 they began to respond to country-specific factors. Periphery debt was underpriced for a decade, partly on an "unjustified perception of joint-and-several liability".
- Two design features make euro sovereign markets fragile: (1) a crisis in one member becomes common through bank exposures, shared ECB policy, trade and the common threat of euro collapse; (2) members lack devaluation and offsetting monetary policy. With timely restructuring unavailable, "debt sustainability problems arose at low levels of debt".
- Markets react faster than agencies. A rating action on one country can open a gap between markets and agencies for all peers.
- Use the ordering of the three PDs as a state variable. Agencies moving to the top of the pessimism ranking (RR2) was the Greek end-state.

## Anti-patterns
- **Treating one channel as the truth**: each PD rests on a model or a historical frequency table.
- **Delay through stigma**: before the Greek Private Sector Involvement, senior EU officials treated any talk of restructuring as a stigma (Bini Smaghi 2011 is cited). The author says this delayed restructuring and raised the fiscal and social cost.
- **Relying on CRAs without regard to their incentives**: oligopoly, opaque methods, weak accountability, misaligned interests, lack of independence, slow response to news.

## Reference Tables

Events and the breakdowns they caused (sect. 3):

| Event | Breakdown observed |
|---|---|
| Lehman collapse, September 2008 | Bond vs CDS views diverge in all five countries. No market-vs-CRA divergence |
| Fitch puts Greece on negative watch, May 2009 | Both markets diverge from CRAs in all five countries. Further bond-CDS divergence for Greece |
| Greece announces in October 2009 a 2008 deficit above 10% | Further market-vs-CRA divergence for Greece. A first signal for Ireland |
| EU-IMF bailout of Greece announced | Most countries unaffected. Further bond-CDS divergence for Italy |
| Irish bailout announced | Italy: CDS vs CRA divergence. Spain: bond vs CDS, and both markets vs CRAs |

Estimation periods (day.month.year as printed):

| Period | Dates |
|---|---|
| 1 | 05.09.08 - 09.01.09 |
| 2 | 16.01.09 - 29.05.09 |
| 3 | 05.06.09 - 16.10.09 |
| 4 | 23.10.09 - 05.03.10 |
| 5 | 12.03.10 - 23.07.10 |
| 6 | 30.07.10 - 10.12.10 |
| 7 | 17.12.10 - 29.04.11 |
| 8 | 06.05.11 - 16.09.11 |

Figure 4.3, my reading of the chart (PDF p. 110). These are chart readings, not printed values. The chart has no numeric scale. It stacks, for each of the eight periods, three rows of markers ordered by pessimism (top is most pessimistic). Marker shape gives the channel (oval bonds, diamond CDS, rectangle CRAs) and a flag fill gives the club.

| What the chart shows | Confidence |
|---|---|
| Rectangles (CRAs) fill the bottom row in Periods 1 to 7 for every club | clear |
| In Period 8 one diamond (CDS) with the Hellenic fill sits in the bottom row and a Hellenic rectangle (CRA) sits in the top row, which is regime RR2 for Greece | clear |
| In Period 8 the other two clubs have ovals (bonds) on top and rectangles at the bottom, which is RR1 | fairly clear |
| The top and middle rows in Periods 1 to 7 mix ovals and diamonds, so each club is in RR1 or RR3 | clear |
| Which club is RR1 and which is RR3 in each of Periods 1 to 7 | not legible: the flag fills cannot be told apart at the scan resolution |

So the chart confirms the prose (CRAs least pessimistic everywhere until Greece's switch in Period 8). It does not let me date the Latin switch or the Irish switches period by period.

## Worked Example
Greece, as the chapter narrates it:
1. Periods 1-4 (September 2008 to March 2010): regime RR3. CDS is the most pessimistic channel, bonds follow, ratings lag.
2. Periods 5-7 (March 2010 to April 2011): regime RR1. The bond market becomes the most pessimistic.
3. Period 8 (May to September 2011): regime RR2. Agencies overtake both markets.
4. Reading: pessimism started in CDS, passed to bonds and finally to ratings. The author says the Greek overshoot by the agencies "raises a number of interesting agency questions" and does not answer them.

## Key Takeaways
1. Put bond, CDS and rating signals on one scale (implied five-year PD) before comparing them.
2. Watch for regime rotation after discrete events, not only for spread levels.
3. The first two events (Lehman, the Greek crisis) broke forecasts across all five countries. Later events hit Ireland, Italy and Spain selectively and in sequence.
4. CDS led bonds in the early phase in every club.
5. Ratings were the least pessimistic channel for the Latin and Celtic clubs throughout the sample.
6. An official regime with no restructuring option creates an incentive to mislabel solvency.

## Connects To
- **Ch 1 (d'Arvisenet)**: spread model on fundamentals and the post-2010 residual.
- **Ch 5 (Xafa)**: the Greek restructuring whose delay this chapter criticizes. Xafa weighs the delay differently.
- **Ch 6 (De Grauwe)**: disputes that markets price sovereign risk efficiently, an assumption the PD inversion here takes as given "as standard".
- **Ch 10 (Mody)**: the cost of delayed restructuring.
- **Ch 11 (Ganguin)**: the rating-agency view from inside S&P.

## Extraction Notes
- Figures 4.1 and 4.2 are image placeholders. Figure 4.3 was read from PDF p. 110. Its marker shapes are legible but the club fills are not, so the exact period of each bond-CDS switch is still known only from the prose.
- The chapter gives no coefficient estimates, loss-function parameters or PD levels. They sit in the unpublished working paper.
- The chapter number in the heading is garbled ("Ly|"). The Contents confirm it is chapter 4.
