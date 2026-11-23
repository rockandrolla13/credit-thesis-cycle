# Causal chain against the skill library, 2026-11-23

Question: how much forward AI capex debt supply is priced into US IG and HY spreads, six months from 2026-11-23.
This file tests each of the eight links of the causal chain against all 35 skills in `skill-to-use/SKILL.md`.
Chapter files are under `/home/ak/.agents/skills/<skill>/chapters/`. Every row below rests on a chapter file that was opened or searched today.
A source says only what its chapter file says. Nothing here comes from general knowledge of a book.

Stances: supports, qualifies, contradicts, silent. "Analogue" marks a past episode or a dated case. An analogue is not evidence for the link.
Research only. No trades.

## The eight links

- L1. A few AA and A issuers supply 14% to 20% of 2026 IG issuance.
- L2. That supply lifts top-rated spreads against lower-rated spreads, and the pressure stays in the tier.
- L3. Part of the effect lands in Treasury yields, so the IG index spread is a weak gauge of supply.
- L4. The curve already holds about three Fed hikes, so only a surprise in the path is new.
- L5. The market sorts AI borrowers by the support of a big-tech customer.
- L6. Debt moves into vehicles, bank loans and private credit, where it costs more and leaves the bond indices. Bank-held AI loans start to show marks.
- L7. Wider spreads slow projects, and slower projects need less debt.
- L8. A capex cut does not remove signed leases, so less bond supply can arrive with more stress at vehicles and lenders.

## L1. A few AA and A issuers supply 14% to 20% of 2026 IG issuance

| Skill | Chapter file | Stance | What it says | Number |
|---|---|---|---|---|
| bis-building-ai-on-credit | sec01-ai-credit-boom-scale.md | supports (dated case data) | The five largest hyperscalers sold a large and rising amount of long bonds in 2026. | $222 billion gross to September 2026. More than 10% of long-term Treasury issuance |
| bis-building-ai-on-credit | sec03-spillovers-event-study.md | supports (dated case data) | Hyperscaler bonds of 10 years or more took a fast-rising share of long corporate issuance. | About 24% in 2026, from about 3% in 2024 |
| van-nieuwerburgh-financing-ai-buildout | sec03-ownership-and-financing.md | supports | Capex of five firms passes their operating cash flow in 2026, so the marginal dollar is borrowed. | 2026 capex $800.5bn against cash flow $707.1bn (guidance and estimates, chart labels) |
| willer-trading-global-macro | ch11-credit.md | qualifies | Issuance is endogenous. It rises when demand is strong and is pulled when demand is weak. | None for this link |
| dalio-big-debt-crises | ch02-deflationary-cycle-early-bubble-top.md | qualifies | A high average matters less than debt concentrated in key entities. The checklist gives questions, not thresholds. | None |

Neither paper gives a share of all IG issuance. The 14% and the one fifth come from one letter writer (`evidence/inbox.md`, I2 and the flag on I2). The two do not reconcile.

## L2. The supply lifts top-rated spreads against lower-rated spreads, and the pressure stays in the tier

| Skill | Chapter file | Stance | What it says | Number |
|---|---|---|---|---|
| chaudhary-corporate-bond-multipliers | sec04-estimation-results.md | supports | A coarse rating bucket has few substitutes. A demand shock moves its price and does not pass through to the rest of IG. | 1% of the bucket moves its price 3.94%. Passthrough from the rest of IG -0.04 (469 observations, first-stage F 21.32) |
| chaudhary-corporate-bond-multipliers | sec04-estimation-results.md, sec06-conclusion.md | qualifies | The shocks are fund flows, and "No estimate uses issuance". Persistence was tested only at a finer level, where the effect faded in a quarter. | 0.27 in the shock quarter, 0.04 one quarter later |
| chaudhary-corporate-bond-multipliers | sec05-arbitrage-risk.md | qualifies | At the fine portfolio level the pooled IG multiplier is near zero and the HY one is larger. The paper gives no AA or BBB number. | Pooled IG "close to 0". Pooled HY "around 0.6" |
| willer-trading-global-macro | ch11-credit.md | contradicts | Supply does not forecast credit returns. The authors ignore supply forecasts. | Correlation of returns with same-month supply -0.12. With returns one month later +0.22 (backtest) |
| willer-trading-global-macro | ch11-credit.md | qualifies | In acute stress the lowest IG ratings underperform most. The ratio would then fall for a reason that is not supply. | None |
| bis-building-ai-on-credit | sec03-spillovers-event-study.md | silent on tiers | The test uses the IG index spread only. It has no rating split. | None |
| bis-building-ai-on-credit | sec05-companion-qr-box-on-off-balance-sheet.md | qualifies (dated case data) | Hyperscaler CDS rose with "both the volume of supply and uncertainties around the projects' payoffs". Supply is one of two causes. | Chart reading, March 2026: about 40bp for higher-rated and about 150bp for lower-rated hyperscalers |
| dalio-how-countries-go-broke | ch02-mechanics-in-words-and-concepts.md | supports (method only, sovereign context) | Price is total spending over total quantity. List the buyers and ask if their buying can keep pace with supply. | None |
| credit-cycle | SKILL.md, Points to Compare 10 | qualifies (router) | It lists "Does supply move spreads?" as an open question and tells the reader to say what each source measures. | None |

## L3. Part of the effect lands in Treasury yields, so the IG index spread is a weak gauge

| Skill | Chapter file | Stance | What it says | Number |
|---|---|---|---|---|
| bis-building-ai-on-credit | sec03-spillovers-event-study.md | supports | Long AI debt goes to the investors that hold long Treasuries, so supply should show in the term premium. The IG index spread did not move on the same days. | Term premium +1.53bp on 18 news days. IG spread +0.13bp (standard error 0.24), not significant |
| bis-building-ai-on-credit | sec03-spillovers-event-study.md | qualifies | The effect is small, reverses within two trading days, and is "not causal". A normal day moves the premium more. | Normal daily move about 3.5bp. Hyperscaler long bonds about 13% of gross Treasury issuance in 2026 |
| willer-trading-global-macro | ch05-rates-framework.md | qualifies | Supply shows in swap spreads much more than in curve shape. Supply fears matter mostly with an inverted curve and no cuts near. | None |
| willer-trading-global-macro | ch11-credit.md | supports | Total return on a corporate bond is two bets, duration and spread. Judge them apart. | None |
| ilmanen-investing-amid-low-expected-returns | ch04-liquid-asset-class-premia.md | supports | The 10-year yield splits into expected inflation, expected real short rates and a bond risk premium. IG total return mostly measures rate exposure. | None used |
| chaudhary-corporate-bond-multipliers | sec06-conclusion.md | qualifies | The paper assumes that corporate bonds and Treasuries are weak substitutes. That assumption is the opposite of this link. | None |
| dalio-how-countries-go-broke | ch02-mechanics-in-words-and-concepts.md | supports (method only, sovereign context) | When buyers are near their limits, buying must slow as supply rises. | None |
| shahidi-balanced-asset-allocation | ch03-drivers-of-returns.md | silent on supply | It treats rates through expectations of cash rates only. | None |

## L4. The curve already holds about three Fed hikes, so only a surprise in the path is new

| Skill | Chapter file | Stance | What it says | Number |
|---|---|---|---|---|
| shahidi-balanced-asset-allocation | ch03-drivers-of-returns.md | supports | If cash rates follow the path in the curve, the change does not move returns. Only the unexpected change does. | None from the book. Today: 2-year 4.76% against a 4.00% ceiling (`readings.json`) |
| papic-geopolitical-alpha | ch11-geopolitical-alpha.md | supports | A view must be out of consensus, "or the market may have already priced it in". | None |
| drobny-inside-the-house-of-money | ch16-anonymous-currency-specialist.md | supports (one manager's opinion) | The price of money that firms use to judge investment is the 18-month to two-year rate, not the overnight rate. | None |
| satchell-forecasting-expected-returns | ch12-investments-as-bets.md | qualifies | A market-implied probability is a pricing weight. It is not the market's belief. This applies to the 96% for December. | None |
| ilmanen-investing-amid-low-expected-returns | ch04-liquid-asset-class-premia.md | qualifies | The curve is a poor forecaster. Forwards and consensus predicted rising yields "for almost 30 years". | None |
| dalio-big-debt-crises | ch02-deflationary-cycle-early-bubble-top.md | qualifies | Tightening is the usual trigger at a top. The more leverage and the higher the prices, the less tightening it takes. | None |
| axilrod-inside-the-fed | ch09-concluding-remarks.md | qualifies (thin) | The Fed has generally avoided raising rates further than the economy needs to stop an asset boom. | None |
| fed-rate-hike | SKILL.md, Points to Compare 3 | qualifies (router) | It lists hikes that the market prices and the Fed never delivers as an open comparison. | None |
| gurevich-trades-of-march-2020 | ch02-the-pivot.md | analogue | A trader's 2019 view: the Fed surprises with eases and never with hikes. Past episode, one opinion. | None |

## L5. The market sorts AI borrowers by the support of a big-tech customer

| Skill | Chapter file | Stance | What it says | Number |
|---|---|---|---|---|
| van-nieuwerburgh-financing-ai-buildout | sec03-ownership-and-financing.md | supports | Long agreements with investment-grade hyperscalers make project debt financeable. Frontier AI firms lack a credit profile of their own. | None |
| bis-building-ai-on-credit | sec02-financing-structures-risk-allocation.md | supports | Guarantees from hyperscalers and chip vendors supply the support needed to issue long investment-grade debt. | None |
| bis-building-ai-on-credit | sec02-financing-structures-risk-allocation.md | qualifies | The support is partial and "typically capped". Do not read the vehicle rating as the tenant rating. | None |
| bis-building-ai-on-credit | sec05-companion-qr-box-on-off-balance-sheet.md | supports (dated case data) | The lower-rated hyperscalers repriced first. Do not treat the sector as one credit. | Chart reading, March 2026: about 150bp against about 40bp |
| campbell-in-search-of-distress-risk | sec03-logit-model-of-bankruptcy-and-failure.md | supports (narrow) | For listed firms, leverage and past share returns signal failure at short horizons and fade fast. It has no bond or sponsor data. | Sample 1963 to 2003 |
| hayford-malliaris-asset-prices-crisis | ch02-general-characteristics-of-financial-crises.md | supports | Borrowers that depend on outside finance do worse when credit tightens. | None |
| dalio-big-debt-crises | ch02-deflationary-cycle-early-bubble-top.md | supports | The riskiest debtors miss payments first, and credit spreads tick up. | About six months before the economy peaks |
| christodoulakis-european-periphery-debt-crisis | ch04-rating-agencies-vs-sovereign-debt-markets.md | analogue | In euro-area sovereigns from 2008 to 2010, pessimism showed in CDS first, then bonds, then ratings. | None |

The evidence that lenders price from the customer's credit is two posts by one account (`evidence/x.md`, O2, and `fresh.md` link 5). No skill tests it.

## L6. Debt moves into vehicles, bank loans and private credit, costs more and leaves the bond indices. Bank-held loans start to show marks

| Skill | Chapter file | Stance | What it says | Number |
|---|---|---|---|---|
| van-nieuwerburgh-financing-ai-buildout | sec03-ownership-and-financing.md | supports | The structures move ownership and leverage away from the operating company. Reported leverage can stay low while asset-level leverage rises. | Morgan Stanley split for 2025 to 2028: private credit about $800bn, corporate debt about $200bn, structured finance about $150bn |
| bis-building-ai-on-credit | sec02-financing-structures-risk-allocation.md | supports | The hyperscaler pays for flexibility through the lease rate. The vehicle's debt yields more than the hyperscaler's own bonds. | Analogue, October 2025: 225bp for one vehicle against 88bp and 98bp for its tenant |
| bis-building-ai-on-credit | sec01-ai-credit-boom-scale.md | supports (dated case data) | Vehicle-linked bonds and ABS, and leases not recorded as debt, are large. | $75 to $100 billion placed in 2026. Leases $1.2 trillion at mid-2026 |
| bis-building-ai-on-credit | sec04-companion-bulletin-120-cash-flows-to-debt.md | contradicts (on cost, for private credit loans) | Private credit lenders priced AI loans like any other loan. | 6.2 points over the base rate for AI loans against 6.1 for others (January 2026) |
| fed-bank-lending-to-private-credit | sec07-companion-financial-accounts.md | supports (dated level) | Banks fund the lending funds, so part of the risk returns to banks. | Bank loans of $349 billion to US private credit vehicles (2025:Q4) |
| fed-bank-lending-to-private-credit | sec04-direct-exposure-and-drawdown-stress.md | qualifies | A full draw of bank lines to lending funds costs little capital. The authors call it an upper bound for these vehicles "alone". | $36 billion drawn. About 2bp of capital ratio (2024 data) |
| schulte-credit-driven-economy | ch02-loan-deposit-ratio.md | supports | Count lenders that do not fund with deposits. A count of deposit banks alone hides a "stealth" rise in leverage. | None used |
| claessens-financial-globalization | ch01-commonalities-with-previous-crises.md | supports | A boom in one segment can hide in a flat aggregate. Fast-growing lending outside the regulated perimeter is a risk flag. | None |
| claessens-financial-globalization | ch02-new-dimensions-of-the-crisis.md | supports (analogue for the mechanism) | In 2007 to 2009, opaque structures did not show in spreads until prices fell. | None |
| schularick-taylor-credit-booms | ch02-data-and-two-eras-of-finance-capitalism.md | qualifies | Its credit measure is bank loans. It understates credit where non-banks and securitisation are large. | None |
| dalio-big-debt-crises | ch02-deflationary-cycle-early-bubble-top.md | supports | New lenders outside regulation grow in a bubble. | None |
| drobny-invisible-hands | ch14-the-pensioner.md | supports (one manager's opinion) | A limit on visible leverage drives risk into leverage that sits inside another entity. | None |
| ilmanen-investing-amid-low-expected-returns | ch05-illiquidity-premia.md | supports and qualifies | Private assets report smoothed returns and understate risk. The extra yield for illiquidity is modest and "may vanish" in complacent times. | No private credit number survives in the skill |
| willer-trading-global-macro | ch16-private-assets-and-crypto.md | supports | Private credit is equity beta with lagged marks. Its data hold no proper down cycle. | Backtest: advantage falls from 0.7 to 0.26 after unsmoothing |
| cassidy-how-markets-fail | ch20-in-the-alphabet-soup.md, ch22-london-bridge-is-falling-down.md | analogue | In 2007 the off-balance-sheet vehicles drew on their sponsors and came back to bank balance sheets. | None used |
| suria-event-driven-edge | ch06-spinoffs.md | supports (narrow, issuer level) | Where a parent places the debt shows which entity it wants to keep strong. | None |
| credit-cycle | SKILL.md, Points to Compare 11 | qualifies (router) | It lists "How risky is private credit?" as an open question across four sources. | None |

The sub-claim on marks rests on one loan sale (`evidence/inbox.md`, I13). No skill has data on AI loan marks.

## L7. Wider spreads slow projects, and slower projects need less debt

| Skill | Chapter file | Stance | What it says | Number |
|---|---|---|---|---|
| cowen-risk-and-business-cycles | ch02-risk-based-theory-real-terms.md | supports | Tighter finance or higher volatility cuts long, risky investment at once, with no boom needed first. | None |
| cowen-risk-and-business-cycles | ch02-risk-based-theory-real-terms.md | qualifies | The author reports two objections. Investment responds little to rates, and firms set hurdle rates far above the cost of capital. Rates matter little for when to commit. | Hurdle rates of "three or four times the cost of capital" |
| cowen-risk-and-business-cycles | ch05-empirical-evidence.md | qualifies | The tests of volatility on investment are mixed, and the samples end before 1997. | None |
| willer-trading-global-macro | ch11-credit.md | supports | Issuance is pulled when demand for credit is weak. | None |
| van-nieuwerburgh-financing-ai-buildout | sec02-physical-capital-boom.md | supports | Announced capacity is not supply. A large part never completes in the author's scenario. | 43.2% of capacity not realised. A scenario, not a forecast |
| van-nieuwerburgh-financing-ai-buildout | sec05-risks.md | supports | Booms turn when demand falls short, financing tightens, or adoption is slower than the debt matures. | None |
| dalio-big-debt-crises | ch02-deflationary-cycle-early-bubble-top.md | supports | When the riskiest debtors miss payments, risky lending slows. | None |
| hayford-malliaris-asset-prices-crisis | ch02-general-characteristics-of-financial-crises.md | supports | A boom lasts while new buyers have "credit and belief". It ends when that supply runs out. | None |
| drobny-inside-the-house-of-money | ch16-anonymous-currency-specialist.md | supports (one manager's opinion) | Firms judge investment against the 18-month to two-year rate. | None |
| cassidy-how-markets-fail | ch11-the-prisoners-dilemma-and-rational-irrationality.md, ch14-the-rational-herd.md | qualifies | Each firm can find it rational to keep going while its rivals do. The brake then works late. | None |
| bis-building-ai-on-credit | sec02-financing-structures-risk-allocation.md | qualifies | Vehicles let neoclouds and AI labs reach a deep pool of long investment-grade funding. That weakens the brake from public spreads. | None |

No run file shows a project slowed by spreads. No large spender has cut 2027 capex (`thesis_full.md`, section 5).

## L8. A capex cut does not remove signed leases, so less bond supply can come with more stress at vehicles and lenders

| Skill | Chapter file | Stance | What it says | Number |
|---|---|---|---|---|
| van-nieuwerburgh-financing-ai-buildout | sec05-risks.md | supports | Debt service is fixed while revenue depends on use and renewals. A modest shortfall becomes a large loss for junior claims. If demand disappoints, hyperscalers may protect owned sites and shift work away from leased ones. | None |
| bis-building-ai-on-credit | sec02-financing-structures-risk-allocation.md | supports | The stress path is non-renewal, re-letting into a glut, a capped guarantee, then loss at insurers, funds and their banks. | None |
| bis-building-ai-on-credit | sec02-financing-structures-risk-allocation.md | qualifies | Some leases run "on short initial terms with options to renew". A tenant can then leave at renewal, and the claim on it is not fixed. A run on short-term funding "appears less likely". | Analogue: one lease starts in 2029 and first runs four years |
| bis-building-ai-on-credit | sec01-ai-credit-boom-scale.md | supports (dated case data) | Leases not yet started are large. | About $820 billion of $1.2 trillion at mid-2026 (Moody's) |
| schularick-taylor-credit-booms | ch04-credit-booms-and-crisis-prediction.md | supports | The danger sign is a credit boom that then slows. Limit: the measure is bank loans in 14 countries. | Baseline AUROC 0.717 |
| cassidy-how-markets-fail | ch16-hyman-minsky-and-ponzi-finance.md | supports | A borrower whose cash flow covers interest only must roll its debt. The mix of such borrowers measures fragility. | None |
| hayford-malliaris-asset-prices-crisis | ch02-general-characteristics-of-financial-crises.md | supports | Shocks grow when borrowers lose financing. The damage depends on how much the financial sector funded the boom. | None |
| dalio-big-debt-crises | ch01-credit-debt-and-the-big-debt-cycle-template.md | supports (thin) | The test is whether the borrowed money earns enough to service the debt. Borrowing to pay debt service is a warning sign. | None |
| rozanov-global-macro-theory-practice | ch06-emerging-markets.md | supports (process) | Study "vulnerability and consequences" before triggers. | None |
| drobny-invisible-hands | ch01-rethinking-real-money.md | supports (one author's view) | Commitments to pay in later are a form of leverage with an option-like loss profile. | None |
| suria-event-driven-edge | ch05-spacs.md | supports (narrow, issuer level) | Count capitalised leases with net debt. Stopping at market value misses lease commitments. | None |
| koo-balance-sheet-recession | ch01-america-subprime-fiasco.md | qualifies | First classify the stress as local or systemic. The link does not say which. | None |
| fed-bank-lending-to-private-credit | sec04-direct-exposure-and-drawdown-stress.md | qualifies | The direct bank loss from lending funds is small on 2024 data. Correlated draws by other non-banks stay open. | About 2bp of capital ratio. Wider case with private equity funds: $134 billion, ratio from 13.02% to 12.94% |
| claessens-financial-globalization | ch01-commonalities-with-previous-crises.md | qualifies | Only a minority of credit booms end in a crisis. | None |
| claessens-financial-globalization | ch03-channels-and-mechanisms-of-the-crisis.md | analogue | In 2007 to 2009 banks took their off-balance-sheet vehicles back under stress. | None |
| eichengreen-capital-flows-crises | ch07-baring-crisis-in-a-mexican-mirror.md | analogue | In 1890 a railway boom met higher centre rates and a failed bond issue before the investments paid. | None |

The $1.3tn of signed leases not yet started is one letter's count (`evidence/inbox.md`, I4). The BIS has about $820 billion at mid-2026 on a Moody's count.

## Skills that are silent on all eight links

| Skill | Reason |
|---|---|
| skill-to-use | Index. It holds no book content. |
| thesis-builder | Tool. It sets the steps and gates of the memo. |
| credit-scenario-grid | Tool. Its grid encodes L2, L7 and L8 (ratio 0.64 under supply grind, 0.46 under a capex cut), but those are our own assumptions and not evidence. |
| simonian-computational-global-macro | ch05 gives a way to draw a causal graph. It says nothing on the content of any link. Its graphs have no loops, so L7 must be drawn across time. That last point is our inference. |
| bresciani-turroni-economics-of-inflation | Hyperinflation in Germany. No link touches it. |
| dalio-changing-world-order | Reserve currencies and internal order. ch02 says debt is paid ahead of equity, which is too general to test a link. |

## Count

35 skills. 29 say something on at least one link: 24 as method or dated data, 2 as routers (credit-cycle, fed-rate-hike) and 3 as analogue only (gurevich, christodoulakis, eichengreen). 6 are silent on all eight.

| Skill | Links |
|---|---|
| bis-building-ai-on-credit | L1, L2, L3, L5, L6, L7, L8 |
| van-nieuwerburgh-financing-ai-buildout | L1, L5, L6, L7, L8 |
| chaudhary-corporate-bond-multipliers | L2, L3 |
| fed-bank-lending-to-private-credit | L6, L8 |
| willer-trading-global-macro | L1, L2, L3, L6, L7 |
| dalio-big-debt-crises | L1, L4, L5, L6, L7, L8 |
| dalio-how-countries-go-broke | L2, L3 |
| cowen-risk-and-business-cycles | L7 |
| shahidi-balanced-asset-allocation | L4 |
| satchell-forecasting-expected-returns | L4 |
| ilmanen-investing-amid-low-expected-returns | L3, L4, L6 |
| papic-geopolitical-alpha | L4 |
| axilrod-inside-the-fed | L4 |
| campbell-in-search-of-distress-risk | L5 |
| hayford-malliaris-asset-prices-crisis | L5, L7, L8 |
| cassidy-how-markets-fail | L6 (analogue), L7, L8 |
| claessens-financial-globalization | L6, L8 |
| schularick-taylor-credit-booms | L6, L8 |
| schulte-credit-driven-economy | L6 |
| koo-balance-sheet-recession | L8 |
| rozanov-global-macro-theory-practice | L8 |
| drobny-inside-the-house-of-money | L4, L7 |
| drobny-invisible-hands | L6, L8 |
| suria-event-driven-edge | L6, L8 |
| credit-cycle | L2, L6 (router) |
| fed-rate-hike | L4 (router) |
| gurevich-trades-of-march-2020 | L4 (analogue) |
| christodoulakis-european-periphery-debt-crisis | L5 (analogue) |
| eichengreen-capital-flows-crises | L8 (analogue) |

Six verdicts differ from `sweep.md`, which judged each skill against the whole question and not link by link. Suria, Dalio (How Countries Go Broke), Eichengreen and Christodoulakis were "not relevant" there and give a narrow or analogue line here. Simonian was "relevant, method (tool)" there and is silent on every link here. Satchell moves from the pricing section to L4.

## Verdict by link

| Link | Strongest support | Strongest objection | Verdict |
|---|---|---|---|
| L1 | BIS sec03: hyperscaler long bonds were about 24% of long corporate issuance in 2026, from about 3% in 2024. | The 14% and the one fifth come from one author and do not reconcile. No skill gives a share of all IG issuance. | Well supported |
| L2 | Chaudhary sec04: a rating bucket is a weak substitute for the rest of IG (3.94% price move, passthrough -0.04). FRED: ratio 0.581 against a mean of 0.476. | Willer ch11: supply is endogenous and does not forecast returns. Chaudhary measures flows, not issuance, and its effect fades in a quarter at the finer level. | Supported with a caveat |
| L3 | BIS sec03: term premium +1.53bp and IG spread +0.13bp on the same 18 days. | The same test: 18 days, not causal, gone in two days. Willer ch05: supply shows in swap spreads more than in the curve. | Supported with a caveat |
| L4 | Shahidi ch03: only the unexpected change in cash rates moves returns. | Satchell ch12: a priced probability is not a belief. Ilmanen ch04: forwards were wrong on yields for almost 30 years. | Supported with a caveat |
| L5 | Van Nieuwerburgh sec03 and BIS sec02: the tenant's credit and guarantees are what make the debt financeable. | BIS sec02: the support is partial and capped. The direct evidence is two posts by one account. | Supported with a caveat |
| L6 | Van Nieuwerburgh sec03 and BIS sec02: the structures move leverage out of sight, and vehicle debt yields more than the tenant's bonds. | BIS sec04: private credit priced AI loans like other loans (6.2 against 6.1 points). The marks rest on one loan sale. | Supported with a caveat. The sub-claim on marks is thin |
| L7 | Cowen ch02: tighter or more volatile finance cuts long investment at once. Willer ch11: issuance follows demand. | Cowen's own reported objections on hurdle rates. Cassidy ch11 and ch14: firms keep going while rivals do. No run file shows a project slowed by spreads. | Thin |
| L8 | Van Nieuwerburgh sec05: fixed debt service turns a modest shortfall into a large loss. BIS sec02: the loss path to funds and banks. | BIS sec02: short first lease terms let a tenant leave, and a run "appears less likely". Fed sec04: small direct bank loss on 2024 data. | Supported with a caveat |

The strongest single contradiction is Willer ch11 against L2. It says supply is endogenous and that the authors ignore supply forecasts.
