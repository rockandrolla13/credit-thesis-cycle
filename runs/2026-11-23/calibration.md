# Post-case calibration (phase B)

Written 2026-11-23, update run, after `fresh.md` was finished. `fresh.md` was not edited after this file was started.
This file adds to the fresh view. It does not change it.
Chapter files are under `/home/ak/.agents/skills/<skill>/chapters/`.
Part 1 is carried from the previous `calibration.md`. I did not re-read those chapters today. Part 2 was read or measured today.

## Part 1. Analogues carried from the previous run

1. **US 2000 to 2002. Closest, but only fragments.** IG widened 117bp and HY 431bp (willer ch03, Table 3.5). In 2002 two large failures pulled credit lower while lending conditions improved (willer ch11).
2. **US 1927 to 1929.** A technology boom, Fed tightening and leverage outside banks (dalio ch08).
3. **Subprime 2007 to 2008.** The weakest borrowers lost access first. Risk came back to banks through credit lines (cassidy ch19 and ch22, claessens ch03).
4. **1998.** A spread shock with no recession (axilrod ch06, gurevich ch05). The Fed was on hold.
5. **Baring 1890.** A railway boom, a higher centre rate and a failed bond issue (eichengreen ch07).
6. **Past US investment booms, by size.** Railroads averaged 2.24% of GDP a year from 1870 to 1890. Telecom and fibre averaged 1.10% from 1996 to 2003. The AI scenario is 3.22% from 2025 to 2032 (van-nieuwerburgh sec09, author's scenario).
7. **Seven investment booms, by aftermath.** Their end came with a growth slowdown "of more than 1 pp on average" (bis sec04, January 2026 note).
8. **The price of going off balance sheet, October 2025.** A base of about 100 to 130bp for the vehicle premium (bis sec02, van-nieuwerburgh sec04).
9. **Investment-grade credit in 2007.** One manager recalls the IG index spread at 35bp in summer 2007 and "almost 300 bp" in 2008 (drobny-invisible-hands ch03, from memory). Today's IG spread is 98bp, so the starting point is far less tight.
10. **Crowded credit in 2005.** A correct view on tight credit was early by two years (drobny-inside-the-house-of-money ch13).

## Part 2. New today

11. **March 2020, the week of 15 to 20 March.** An emergency cut did not stop the funding squeeze. Stocks and Treasuries fell together and margin calls forced sales of collateral. The author dates the end of the funding stress to one day, after which "funding pressure does not return, though stocks may fall much further" (gurevich ch06). Use: an equity fall and a funding event are separate things. Last week had the first without the second. Funding markets showed no stress in the previous pack (I24). No source today reports any.
12. **A newsletter author's own history.** Bonds worked well from 2001 to 2003. In 2008 the corrections were "wild", and he made more from other dislocations than from market direction (Applied Macro, 23 Nov 2026). One person's account. It supports analogue 1 only loosely.
13. **October 1987.** One account says Friday 20 Nov is not like the Friday before the 1987 crash, because positioning differs and futures rose on Monday (@dampedspring, 23 Nov 2026). His opinion, not checked.
14. **The 1999 hiking cycle.** One account uses it for 2-year yield ranges (@BraxResearch, 29 Sep 2026). Not used.

## Evidence items that cite history (from the packs)

- The Fed has not hiked on a day when the VIX closed above 30 since 1990 (a risk adviser's table, relayed by Not_Mr Risk, 22 Nov 2026). The VIX closed at 35.89 on 20 Nov (FRED). The December meeting is on 9 Dec. This is an observation about past days, not a rule the Fed follows. If equities rebounded on 23 Nov as two accounts say, the VIX may be lower by 9 Dec.
- After seven midterms that gave a Republican president a Democratic Congress, IG spreads were 10bp wider on average three months later (@ZeGoodTrader, 3 Nov 2026). Carried.

## Move sizes

Carried:
- IG widening in recessions: 67 to 486bp, median 124bp. HY: 431, 785 and 1,602bp (willer ch03, Table 3.5).
- In acute stress, single-A and Baa bonds "can do as badly as Ba and B" (willer ch11).
- A demand shock of 1% of a rating group moved its price 3.94% on impact (chaudhary sec04). A flow shock, not issuance.
- AI financing news moved the 10-year term premium by about 1.5bp, gone in two days (bis sec03).

Measured today from `readings.json` (FRED, prints of 20 Nov against two days before):
- One equity shock: the S&P 500 fell from 7,323.63 to 6,910.39 in two days, and the VIX rose from 24.56 to 35.89.
- In the same two days IG widened 5bp, AA 5bp, A 4bp, BBB 6bp, HY 29bp, BB 24bp, B 35bp and CCC 49bp.
- Over one month IG widened 10bp (88 to 98), HY 49bp (327 to 376) and CCC 95bp (1,307 to 1,402).
- Use: this is the size of a sharp equity fall with no funding event. The grid's "AI digestion" has IG +18bp and HY +108bp over six months. The month already delivered about half of each. The grid moves are changes from today, so they stand. The PM may judge them small.
- The AA to BBB ratio rose from 0.578 to 0.590 in those two days. In the grid, a capex-cut scenario lowers the ratio to about 0.46. The market did not trade last week as a capex cut.

## Base rates

- "Only a minority of credit booms end in a financial crisis" (claessens ch01, carried).
- The first debt problems appear about six months before the economy peaks (dalio ch02, carried).
- A full drawdown of bank lines to lending funds cost about 2bp of capital ratio in the Fed staff arithmetic for 2024 (fed-bank-lending-to-private-credit sec04, carried).

## Adjustments (additive, none applied to the grid)

1. **"Repricing, not a break" keeps its slight edge.** Spreads widened in order of rating, the primary market stayed open (Alphabet sold a bond in Canada), and no funding stress is reported. Against: two banks met weak demand for data-centre loans and one ABS leg was delayed.
2. **Proposal to the PM, carried: the funding-accident test may have the wrong shape.** The BIS loss map points to slow marks at insurers and funds. I did not change the test.
3. **The hard-landing moves may still be too small.** Carried. The books give a median IG move of 124bp, over about a year. The grid has +56bp in six months.
4. **The December hike is less certain than its last known price.** The VIX precedent points that way. The last price in hand is about 96%, from before the fall. I did not change the probability of "Higher rates, supply grind", because its test is the policy rate in May 2027, not in December.
5. **No probability change is proposed.** The 20 Nov prints confirm the size of a move that the previous run already knew about. The two items that could move a probability by 5 points are each one unconfirmed source: a chief executive's return and a cut chip order. They also point in opposite directions.
6. **The timing lesson cuts against acting on "not priced".** Carried from item 10.
