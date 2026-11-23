# Chapter 4: Week 1: A Victory Parade (March 1 to 6, 2020)

## Core Idea
The front-end book built in 2018 and 2019 paid off in days. The author spent the week taking profits, rotating out of long-bond duration into swap-spread and cross-country relative value, starting to buy panic-priced risk assets, and then pressing the March front end again after the emergency cut. He also records one missed trade, April Fed Funds, as "a terrible misstep".

## Frameworks Introduced
- **Underpriced central bank response**: "the historical pattern had taught me that the market invariably underpriced the scope of the central bank's response. This was all I needed to know."
- **Nascent dislocation scan**: in rapid market change, "discover which assets are trading as if everything were going great and which are priced for Armageddon. Sell the former, and buy the latter."
  - How he applied it: US Treasuries had run ahead while Canadian bonds were "pricing a lesser case of the pandemic crisis". He bought Canada.
- **Developed-market rate differential mean reversion**: extreme rate differences between developed countries are "unsustainable ... for too long", so traders can play mean reversion. US minus Canada ten-year: about 0.8% at the 2018 high, about 0.2% by end-2019, then inverted (UST lower) as COVID brewed.
- **Intermeeting-cut rule**: "every intermeeting cut is followed by easing at the next meeting" (table below). Logic: if the situation is dire enough to surprise with liquidity, "why would it risk surprising the market by not providing more liquidity only two weeks later?"
- **Forget the past (extreme price action)**: "The only things that matter are the price that is in front of you this very second and whether transacting at this price will allow you to make money in the future." Not yesterday's plan, not P/L on the day or year, not where the asset traded ten minutes ago.
- **Missed trade = losing trade**: "missing a trade that would make money is no better than entering a losing position."
- **Deliberate delay**: "I rarely respond immediately to a big market event." His edge is "carefully contemplated strategies and not ... hunches". "My first impulse is just as likely to be stupid as to be useful." He holds this alongside the previous two rules and admits the tension cannot be measured.
- **Swap spread is not apples to apples** (market note, November 2015): a bond is an asset, term lending to the government with principal risk. A swap is a derivative, "a bet on a string of three-month interbank lending rates which includes no principal risk". Read inversion as "a spike in the term premium", not a mathematical breakdown.
  - Carry test: compare three-month LIBOR with the rolling Treasury funding (repo) rate. Arbitrage is blocked because investors cannot lock the funding rate and banks are balance-sheet constrained.
  - Verdict: "betting on its normalization is a good, but not riskless trade."
- **One swap, two goals**: instead of selling bond futures, pay fixed on swaps. This moves the book from outright long bonds to long bonds on a spread basis. It reduces interest rate risk and increases spread risk in one trade.
- **Risk-on / risk-off portfolio balance**: balance positive-beta trades with crisis trades so that "I have something working for me in every scenario".
- **Having my cake and eating it too**: when one leg has paid and its natural offset has not yet lost, take profit on the offset "before the market caught on".
- **Bottom-fishing rule**: "buy what I think will end up higher five years later and not worry about the immediate price action." Enabled by a bond-driven book that is negatively correlated to risk assets.
- **Curve behavior in easing**: "Typically, at the beginning of the crisis when the Fed cuts rates, the curve steepens, irrationally pricing that rates will go back up again soon (they never do)."
- **Rates singularity (ZIRP)**: "Sooner or later, something would happen-a crisis or a run-of-the-mill recession." In either case rates have "no path to follow except toward the central singularity, which is the zero interest rate policy".
- **Fear, then necessity; involuntary flows**: "Every crisis starts with fear and ends with necessity." Cash hoarding, tight credit and margin calls force players to retrench "regardless of their market view". Efficient-market and behavioral theories assume voluntary transactions; they fail, like Newtonian mechanics at relativistic speed, when forced volume dominates.
- **Pressing when the tide rises**: "pressing risk when the tide rises in your favor is not only valid but often necessary." Where you sold or bought recently is irrelevant.

## Key Concepts
- **LIBOR-OIS spread**: term premium of three-month LIBOR over projected overnight funding, normally "about 20 bps". Measured against forward Fed Funds, not the current setting.
- **LIBOR**: "a highly subjective rate" from banks' submissions; the Fed controls Fed Funds, not LIBOR.
- **Invoice spread**: forward-starting swap yield versus the forward yield of the bond future; a futures expression "highly correlated to the swap spread".
- **Asset swap / spread basis**: long bond against paying fixed on a swap.
- **Payer swaption**: option that gains if long-dated swap rates rise.
- **RFH0**: future on the EURCHF cross. **PE**: Mexican peso future. **DEDZ**: dividend futures. **ERIS**: swap futures used in the futures-only accounts.
- **The One Trade**: long the long end of the US Treasury curve, held for years; by early March at "the upper end of the channel".

## Mental Models
- Think of a 30-year Treasury on asset swap as pure default risk: 0.9% over its funding rate means, at zero default risk, a rally "from the price of 100 to roughly 122". In 2016 the bond traded "about 82 cents on a dollar in a state of deep 'workout'". The cause was foreign central bank selling and balance-sheet limits, not default fear.
- Use "I am long USTs" to mean cheap versus swaps, not "rates will fall". "One can be a bond bull even after allowing for a moderate rise in interest rates."
- Treat strong backward-looking data as an alternate-universe gauge. February payrolls were strong and "nobody cared".
- Separate forecast from positioning: "Although my forecast was wrong, my positioning wasn't."

## Anti-patterns
- **Anchoring on a price seen seconds ago**: "It is psychologically difficult to buy a contract that was seconds ago a few ticks lower."
- **Waffling at a decisive juncture**: 2016 examples. Post-Brexit, a deeper bond cut was called for; he was distracted by the parabolic JGB rally. On US election night the equity sell-off and bond rally was a "get out of jail free card" for bond bulls, and he sold "only a tiny amount".
- **Calling negative swap spreads "mathematically impossible"**.
- **Short-dated bets on funding normalization**: the danger in March Eurodollars "lay in the extremely short-term nature of the trade". He knew the Fed would get a handle on funding, but not how long it would take.
- **Building a large share of open interest** in a thin contract (RFH0): exposure to loss of exchange liquidity. CK flagged it; he added anyway.

## Reference Tables

**Historical FOMC intermeeting cuts and follow-up** (recovered from PDF p. 103):

| Intermeeting date | Event | Action (bp) | Rate after | Next FOMC | Follow-up (bp) | Rate after |
|---|---|---|---|---|---|---|
| 10/8/2008 | Lehman Collapse | -50 | 1.50% | 10/29/2008 | -50 | 1% |
| 1/22/2008 | Weakening Economy | -75 | 3.50% | 1/30/2008 | -50 | 3% |
| 9/17/2001 | Terrorist Attack | -50 | 3% | 10/2/2001 | -50 | 2.50% |
| 4/18/2001 | Economic Slump | -50 | 4.5% | 5/15/2001 | -50 | 4% |
| 1/3/2001 | Tech Bubble | -50 | 6.0% | 1/31/2001 | -50 | 5.50% |
| 10/15/1998 | LTCM/Russian Crisis | -25 | 5.0% | 11/17/1998 | -25 | 4.75% |

**Gains in basis points of the front-end positions held by March 6, 2020** (recovered from PDF p. 179):

| Trade | 1/31/2020 | 3/6/2020 | Profit (bp) |
|---|---|---|---|
| FFH0 | 98.44 | 99.1225 | 68.25 |
| EDM0 | 98.495 | 99.38 | 88.5 |
| EDM0 98.375 call | 0.175 | 1.015 | 84 |
| EDH0 | 98.36 | 99.065 | 70.5 |
| EDH0 98.5 call | 0.0225 | 0.575 | 55.25 |
| 7Y Treasury | 1.4199 | 0.711 | 70.89 |

The EDH0 calls "had appreciated twenty-five times".

**Swap-spread data points he cites:**

| Date | 30-year measure | Level |
|---|---|---|
| July 8, 2016 | 30-year bond yield (generational low) | 2.099% |
| July 8, 2016 | 30-year swap spread | mid -40s to -50s bp; swap at 1.6761% |
| Early March 2020 (chat) | 30-year swap spread | -38 to -39 bp |

## Worked Example
**Week 1 trade sequence, as the text states it.**

| When | Instrument and action | Reasoning | Outcome / his verdict |
|---|---|---|---|
| Sun Mar 1 | Sell FFH0 at and above 98.665 (1.335%, implying 0.25% of easing for March) to take profit; also took profit on EDH0 | Gap up in all rate futures; option gamma grew positions; keep within risk limits | "A bit impatient"; the market "swallowed" his orders. FFH0 kept rallying Monday, "making me regret my earlier selling" |
| Sun Mar 1 | Buy Canadian bond futures | Canada priced "a lesser case" than the US | Could not trade in Asian hours; picked up later |
| Tue Mar 3, 7:00 a.m. PST | Fed cuts 0.50% intermeeting to 1%-1.25% | n/a | "One of my best trading days ever". June Eurodollar options "a fountain of cash"; March options "exploded"; FFH0 "a jackpot with immediate payout" |
| Tue Mar 3 | **Missed: buy April Fed Funds** | April was 98.89 (1.11%, 47 bp of easing versus February) before the cut; jumped to 99.05, dipped to 98.95 within two minutes. No April meeting, so this priced out further easing on March 18, against every precedent | Noticed at 7:07:48, zoomed in four minutes later, placed a moderate order about fifteen minutes after the event. "Too slow. The price slipped away, and I didn't want to chase it." "There would never be a second chance with that contract." |
| Tue Mar 3 | Reduce USD longs: cut shorts in CAD, JPY, CHF | The rate differential behind long USD was being removed by the Fed; rates had paid while the dollar had not given ground | Profit taken |
| Tue Mar 3 on | Reduce The One Trade; pay fixed on 30-year swaps against bonds | Bond future at top of channel; expected steepening; spreads moving more negative | Becomes central later. "Spoiler alert: the energy was well spent." |
| Wed Mar 4 | Add to long EURCHF via RFH0 | A risk-on trade that lost "almost no money" in the crisis; "reaching for even more cake" | Open |
| Wed Mar 4 | Exercise deep in-the-money Eurodollar options already offset by futures | Free cash for new opportunities | Done |
| Wed Mar 4 | Receive Canadian swaps (after BOC cut 0.50%) | Add duration in Canada, cut it in the US; Canadian spreads "too wide", US "too narrow"; offsets US swap-spread exposure | Open |
| Thu Mar 5 | Buy payer swaptions on long-dated swap rates | Long rates "had moved decidedly too far"; expected "a vicious snapback" when the disease blew over | Bought after long pricing and margin discussion, about 7:53 p.m. |
| Thu Mar 5 evening | Start buying Mexican peso (PE) | Panic pricing; five-year view | Open |
| Fri Mar 6 | Reverse hedges: buy back EDH0 above where he sold it days earlier, and add | "License to kill"; "Surely, LIBOR had no path but to go down" | March "continued to drift down as I bought it" while LIBOR was projected up. He "increased my bet further". Resolution in Ch 5 and 6 |

**Curve note for March 6**: the rally was a dramatic flattening, long rates falling most. This was "unusual relative to the historical pattern". His book had a steepening bias and "was no longer capitalizing on The One Trade".

**Forecast audit**: his October 2019 call of a 50% chance of further easing "was wrong"; the objective probability "was likely much less than 50 percent". Strong first-quarter data showed the economy had stabilized in late 2019.

## Key Takeaways
1. After an emergency cut, buy the next contract that prices no follow-up. Precedent in the table is six for six.
2. In extreme moves, act on the price in front of you. A fifteen-minute delay cost him the April trade.
3. When a hedge leg has not yet moved against you after the main leg paid, close it first.
4. Rotate from outright duration to spread duration when bonds are extended but cheap to swaps.
5. A negatively correlated core book is what funds buying panic-priced assets.
6. Size funding-normalization trades by time to expiry. Direction can be right and the contract can still expire first.
7. End of week 1: "If I were to stop the year right there, it would have been one of my best years of trading." He intended "to pyramid my gains".

## Connects To
- **Ch 2**: FFH0 and the surprise-ease asymmetry pay here.
- **Ch 5**: March Eurodollars and the LIBOR-OIS widening; swap spreads move further.
- **Ch 6**: funding stress peaks.
- **Ch 8**: verdicts on April Fed Funds, swaptions, FX and spreads.

## Extraction Notes
- The Slack transcript for this week is entirely screenshots (image placeholders). The extraction contains none of the chat text. Order sizes, exact fill prices and timestamps beyond those the prose quotes are therefore absent from this file. The screenshots are legible in the PDF (pp. 73-204) for anyone who needs a specific exchange.
- Two tables were read from the PDF (pp. 103, 179). All charts were left as captions.
- In the November 2015 note, two sentences are interleaved in the extraction around the heading "Inverted Swap Spreads - 'Not an Apples-to-Apples Comparison'". The meaning is clear and is paraphrased.
- The text says the swap yield was lower than the Treasury yield "by more than 4055 bps". This is an extraction artifact for a range (the same passage says "mid -40s to -50s"). Recorded as found.
- The curve chart caption refers to "the 2000 easing cycle" while the prose says "in 2001". Recorded as found.
- "EDHO" appears once in the text for EDH0.
