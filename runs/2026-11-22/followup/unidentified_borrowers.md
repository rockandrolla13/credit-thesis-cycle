# Finding the borrowers the market has not yet identified

Written 2026-11-23. Follow-up to the 2026-11-22 run. Research only. No trades.
This file names borrower types and screening criteria. It gives no legs, sizes, hedge ratios or stops.

## The answer in four lines

1. No single skill covers the question. The best single book skill is `dalio-big-debt-crises`.
2. The best two supports are `cassidy-how-markets-fail` and `willer-trading-global-macro`.
3. In the repo, `global-io-network` gives the mapping method and `trap-detector` gives the key question: who is missing from the sample?
4. The screen points to six borrower types. Two are evidence_weighted. Four are PM_assumption.

One limit applies to everything below. The books reason about sectors, banking systems and countries. None gives a borrower-level default screen. The `credit-cycle` router says it does not cover "corporate default models" (`/home/ak/.agents/skills/credit-cycle/SKILL.md`, Scope and Limits). So every test below is a book method applied one level down. That step is mine, not the books'.

## How to read the attributions

- Book paths are relative to `/home/ak/.agents/skills/`.
- Project skill paths are relative to `/media/ak/10E1026C4FA6006E/GitRepos/creditmacro/.claude/skills/`.
- "email item N" means `evidence/email.md`. "substack item N" means `evidence/substack.md`. Both sit in `/home/ak/.local/share/credit-scenario-grid/runs/2026-11-22/`.
- X posts come from `/home/ak/.local/share/credit-scenario-grid/corpus/x/`. Many are cut where X shows "Show more".
- A post is a claim by its author. It is not a fact.
- The nine X accounts come from one person's follow list. They are not independent (`thesis.md`, Limits).

---

## Part 1. Which skill covers this?

### Personal book library

| Skill | Verdict | Reason | File |
|---|---|---|---|
| `skill-to-use` | Does not cover | It is an index. It holds no book content. It routes this question to `credit-cycle`. | `skill-to-use/SKILL.md` |
| `credit-cycle` | Covers part | It is the right entry point. Phase 2 "Warning signs" lists the chapters used below. It holds no content of its own. | `credit-cycle/SKILL.md` |
| `dalio-big-debt-crises` | Covers it, at sector level | Three tools fit. The productive-credit test asks whether borrowed money earns enough to service the debt (ch01). The bubble checklist says to find the bubble and "then map what is connected" (ch02). The pro forma stress test asks, for each sector and institution, whether it can get the new lending it needs (ch09). | `dalio-big-debt-crises/chapters/ch01-credit-debt-and-the-big-debt-cycle-template.md`, `ch02-deflationary-cycle-early-bubble-top.md`, `ch09-case-us-debt-crisis-and-adjustment-2007-2011.md` |
| `cassidy-how-markets-fail` | Covers part | Ch16 sorts every borrower into hedge, speculative or Ponzi finance by what its cash flow covers. Ch12 explains why a label such as "contract-backed" can hide quality. It gives no thresholds and no data. | `cassidy-how-markets-fail/chapters/ch16-hyman-minsky-and-ponzi-finance.md`, `ch12-hidden-information-and-the-market-for-lemons.md` |
| `willer-trading-global-macro` | Covers part | Ch03 says where to look: the assets that boomed most, then the leverage behind them and "where it sits". Ch11 gives tested market signals. The signals work on indices, not single borrowers. | `willer-trading-global-macro/chapters/ch03-business-cycle.md`, `ch11-credit.md` |
| `schulte-credit-driven-economy` | Covers part | Ch02 says to count lenders that do not fund with deposits. Without them a rise in leverage stays hidden. Its thresholds apply to a country's banks, not to a borrower. | `schulte-credit-driven-economy/chapters/ch02-loan-deposit-ratio.md`, `ch04-tangible-leverage-and-deleveraging-arithmetic.md` |
| `claessens-financial-globalization` | Covers part | Ch03 separates catalyst, trigger and amplifier. Its escalation chain ends with banks absorbing legally separate vehicles. Ch02 says opacity is invisible in spreads until prices fall. It explains spread, not selection. | `claessens-financial-globalization/chapters/ch03-channels-and-mechanisms-of-the-crisis.md`, `ch02-new-dimensions-of-the-crisis.md` |
| `hayford-malliaris-asset-prices-crisis` | Covers part | Ch02 says damage scales with how much the financial sector financed the boom. It says shocks amplify when borrowers lose financing. It gives no screen. | `hayford-malliaris-asset-prices-crisis/chapters/ch02-general-characteristics-of-financial-crises.md` |
| `simonian-computational-global-macro` | Covers part | Ch05 gives the Noisy-OR rule for combining several independent warning flags into one probability. It does not say which flags to use. | `simonian-computational-global-macro/chapters/ch05-causal-inference.md` |
| `schularick-taylor-credit-booms` | Does not cover | Its model predicts banking crises for a country from five years of bank loan growth. It cannot rank borrowers. | `schularick-taylor-credit-booms/chapters/ch04-credit-booms-and-crisis-prediction.md` |
| `papic-geopolitical-alpha` | Does not cover | The constraint method is about policymakers. Its rule "constraints, not preferences" fits contract terms only by analogy. | `papic-geopolitical-alpha/chapters/ch02-constraint-framework-three-pillars.md` |
| `borrower-monitoring` | Does not cover | It guides quarterly monitoring of borrowers a lender already holds. It does not find new ones. I read its header only. | `borrower-monitoring/SKILL.md` |

A caution on Dalio ch09. It is a case chapter. The router lists it under warning signs only for the stress-test method "stated inside a case chapter" (`credit-cycle/SKILL.md`, Phase 2). Use that one paragraph for fresh reasoning. Leave the 2007 narrative for the analogue step.

### Project skills (read-only)

| Skill | Verdict | What it does for this question | File |
|---|---|---|---|
| `global-io-network` | Covers part | It is the mapping method. Nodes are structural, not listed names. Edges have a direction. A shock must travel past first-degree neighbours. It names "unlisted supplier exposure" as an output. It needs an input-output table. No such table exists for contracts. | `global-io-network/SKILL.md` |
| `trap-detector` | Covers part | Its survivorship rule asks "what's missing from the sample?". Bond indices show only borrowers that issued bonds. It also says delays in balancing loops cause overshoot. | `trap-detector/SKILL.md` |
| `priced-in-estimator` | Covers part | It tests the words "not yet repriced". It says a wide spread "is not, by itself, mispricing". Strip the common factor first. It needs valuation history, which the packs lack for sectors. | `priced-in-estimator/SKILL.md` |
| `iceberg-classifier` | Covers part | It separates a hot topic from a structure. Its own example names an axis for project debt against hyperscaler debt. It classifies themes. It does not find borrowers. | `iceberg-classifier/SKILL.md` |
| `system-mapper` | Covers part | It separates stocks from flows. The bank-loan store is a stock. The bond take-out is a flow. Construction lag is a delay. | `system-mapper/SKILL.md` |
| `evidence-weighting` | Covers part | It sets the labelling rule. Anchor on a base rate. Make no move on evidence that is vivid but not diagnostic. I use it for the evidence_weighted and PM_assumption labels. | `evidence-weighting/SKILL.md` |
| `multi-source-theme-aggregator` | Covers part | It warns against confusing source count with independence. That applies to the X corpus. It ranks themes, not borrowers. | `multi-source-theme-aggregator/SKILL.md` |
| `causal-compiler`, `backdoor-identifiability-gate`, `edge-validity`, `factor-r2-router`, `scenario-pricing-engine`, `macro-regime-classifier`, `macro-state-parser`, `outcome-calibration-engine` | Do not cover | They build or test a causal chain, a regime or a probability set. None selects borrowers. I read their headers only. | each `SKILL.md` |

### Part 1 answer in one line

Best single skill: `dalio-big-debt-crises` (ch01, ch02, and the stress-test paragraph of ch09). Best two supports: `cassidy-how-markets-fail` (ch16, ch12) and `willer-trading-global-macro` (ch03, ch11). Enter through `credit-cycle`. In the repo, pair `global-io-network` with `trap-detector`.

---

## Part 2. A way to find the not-yet-identified borrowers

### Step 1. The dependency map

**Method.** Three files give the method.

- Willer ch03: start with the assets that boomed most. Then ask how much leverage financed them and where it sits.
- Dalio ch02: find the bubble, then map what is connected to it. A high average is less dangerous when evenly spread than when concentrated in key entities.
- `global-io-network/SKILL.md`: label each edge by direction. Push the shock past first-degree neighbours. Do not collapse a node to one listed issuer.

**The map.** Each ring is a borrower type. The evidence shows that each ring exists. It does not size any ring.

| Ring | Who | How it depends on a big-tech contract | Evidence that the ring exists |
|---|---|---|---|
| 0 | Big-tech tenants | They are the source. Four firms make more than 75% of AI capex. | email item 22 (POLITICO, 28 Oct 2026) |
| 1a | Debt with a signed, live, parent-backed contract | Directly. The contract pays the debt. | A loan backed by one tenant is rated A3 (@nodiligence, 6 and 21 Nov 2026). Shells sold with a parent guarantee (@junkbondinvest, 16 Nov 2026). |
| 1b | Debt with a conditional contract | Directly, but only later or only for a while. | A backstop that starts when the last hall is live (@nodiligence, 5 Nov 2026). A lease either side can end on 90 days' notice (@nodiligence, 13 Nov 2026). $186.2bn of one lab's commitments is terminable or conditional (substack item 15, 16 Nov 2026). |
| 2a | Landlords and GPU clouds whose tenant is an AI lab or a smaller customer | At one remove. The tenant depends on big tech for its own funding. | Loans backed by smaller customers are rated BB+ (@nodiligence, 21 Nov 2026). A lease signed with "no tenant name" (@nodiligence, 18 Nov 2026). |
| 2b | Equipment lessors and chip-backed vehicles | At one remove. The lessee pays rent out of contract income. | A GPU deal placed in a vehicle off the sponsor's balance sheet (@junkbondinvest, 20 Nov 2026). Lenders want legal control of chip collateral (email item 16, FT headline, 20 Nov 2026). |
| 2c | Vendor guarantors | At one remove, in reverse. The chip seller stands behind its customer's debt. | $530bn of gross guarantees at one chip seller (substack item 8, SemiAnalysis preview, 12 Nov 2026). Up to $72bn behind two vehicles at another (@nodiligence, 29 Oct 2026). |
| 2d | Power producers and power developers | At one remove. Demand for power follows the build. | Twenty-year power contracts with a hyperscaler (@nodiligence, 10 Nov 2026). A developer that ordered generators and "couldn't fund" them (@nodiligence, 9 Nov 2026). |
| 2e | Construction and engineering firms | At one remove. Their order book is the build. | 25 private-equity deals for these firms in the first half of 2026 (@junkbondinvest, 12 Nov 2026). |
| 3a | Banks with bridge and construction loans | At two removes. They wait for a bond to repay them. | Seven banks hold a $14.2bn one-year bridge (@nodiligence, 29 Oct 2026). Banks hold $15bn of bridges on a stopped project (substack item 14, Citrini preview, 4 Nov 2026). Banks hold $5bn to $7bn of BB data-centre debt (substack item 20, 31 Oct 2026). |
| 3b | Life insurers | At two removes. They hold privately rated loans and lease-backed paper. | Regulators scaled back scrutiny of private ratings (email item 23, 28 Oct 2026). A bank seeks insurers to take risk on $10bn of AI debt (substack item 20, 31 Oct 2026). |
| 3c | Private credit funds and BDCs | At two removes. They lend to rings 2a, 2d and 2e. | Withdrawals passed inflows in early 2026 (email item 20, 15 Oct 2026). Loans marked below 80 cents are 5% of BDC portfolios (substack item 12, 14 Nov 2026). |
| 3d | Holders of AI-linked ABS, CMBS and risk-transfer notes | At two removes. | AI-related ABS reached $28.6bn (substack item 11, 21 Nov 2026). S&P warned on banks' risk transfers (email item 11, The Banker, headline only, 16 Nov 2026). |

The market has sorted ring 1a from ring 2a. That is the user's observation (@nodiligence, 21 Nov 2026). The open question is ring 1b, rings 2b to 2e, and all of ring 3.

### Step 2. Nine screening tests

Each test gives a flag, not a verdict. No book gives a borrower-level threshold. Where a threshold appears, the file states what it was built for.

| # | Test | Observable data needed | Threshold in the book | Source | Do the packs hold the data? |
|---|---|---|---|---|---|
| 1 | **Minsky class.** Does cash flow cover interest and principal, interest only, or not even interest? Flag interest that is deferred or added to principal. | Interest cover from operations. Capitalised or payment-in-kind interest. Amortisation schedule. Date rent starts against date coupons start. | No threshold in the book. The rule is a three-way sort. | Cassidy ch16 | Partly. Coupons fall due before rent starts on a delayed project (substack item 13, 9 Nov 2026). Median BDC payment-in-kind income rose from 8.7% to 9.2% (@junkbondinvest, 5 Nov 2026). No borrower table. |
| 2 | **Roll test.** Can the borrower get new lending to a) roll maturing debt and b) keep raising debt to finish what it started? | Maturity schedule. Bridge expiry dates. Undrawn committed lines. Remaining capex commitments. | No threshold in the book. | Dalio ch09 (method paragraph only) | Partly. A one-year bridge (@nodiligence, 29 Oct 2026). One GPU cloud says public debt markets are closed to it (`evidence/x.md` X3, 11 Nov 2026). Of private debt due in 2027, the share marked below 90 doubled to 31% (@junkbondinvest, 31 Oct 2026). No bridge calendar. |
| 3 | **Contract quality.** Is the big-tech support signed, in force today, guaranteed by the parent, and as long as the debt? | Tenant name. Guarantor. Start condition. Termination and redesign rights. Contract term against debt tenor. | No threshold in the book. Ch12 says a signal works only if it is hard to obtain. Applying that to leases is my step. | Cassidy ch12 | Partly. Several single deals are described (ring 1b above). A tenant can slow payment by asking for a redesign (@nodiligence, 7 Nov 2026). No systematic contract file. |
| 4 | **Mismatch.** Does the borrower fund a long asset with short debt? Does its lender fund illiquid loans with money that can leave? | Debt tenor against asset life and contract term. Lender redemption terms and funding mix. | No threshold in the book. Ch02 lists four mismatch types. | Dalio ch02 | Partly. One GPU cloud borrowed for five years against contracts of about three (email item 20, 15 Oct 2026). Banks underwrite GPUs at three to four years while operators book six (@nodiligence, 5 Nov 2026). Fund withdrawals passed inflows (email item 20). |
| 5 | **Who absorbs the vehicle?** For each off-balance-sheet vehicle or guarantee, who pays if it fails? | Sponsor support terms. Guarantee size against the guarantor's cash flow. Recourse terms. | No threshold in the book. Ch03 lists banks absorbing separate vehicles as a step in the escalation chain. | Claessens ch03 | Partly. Guarantee totals for two chip sellers (ring 2c above). No recourse terms. |
| 6 | **Count the lenders outside banks.** Add private credit, insurers and securitisation to bank loans before judging leverage. | System loans including non-deposit lenders, against deposits. Lender tangible leverage. | Loan/deposit ratio above 1.2 is dangerous. About 1.3 with tangible leverage of 30 to 40 times means a banking break within months. Both are thresholds for a country's banking system. They are not borrower thresholds. | Schulte ch02, ch04 | No. No pack gives a loan/deposit ratio or lender leverage. One insurer is reported at $66.5bn of assets on $1.38bn of statutory capital, with no AI exposure named (substack item 16, 12 Nov 2026, from a short seller). Statutory capital is not Schulte's tangible measure. |
| 7 | **Already priced?** Compare the borrower's spread move with its rating bucket. Strip the market-wide move first. Flag borrowers that fail tests 1 to 4 but moved no more than their bucket. | Spread history by borrower and by rating bucket. Agency rating against where the debt trades. | No threshold for the gap. Willer ch11 reports that bonds entering a fallen-angel index priced about 150bp cheap to peers. That is a study result, not a screen level. | `priced-in-estimator/SKILL.md`. Willer ch11 for the forced-seller line between investment grade and junk. | Partly. AI lessees and guarantors trade four to seven notches below their ratings (email item 5, second-hand, 21 Nov 2026). 15 of 17 AI debt structures are wider since issue (@junkbondinvest, 2 Nov 2026). No spread history by borrower. |
| 8 | **Lender signals.** Read the bank lending survey, listed private-credit funds, and bank shares against the index. | Fed SLOOS. Listed BDC and private-credit manager share prices against their 200-day average. Bank index against the S&P 500 over three months. | Survey: hold spread risk only if the last survey loosened. Private credit: below the 200-day average, "risks could increase". The authors call this rule "very speculative". Accident trigger: banks lag the S&P 500 by three standard deviations over three months in a falling market. | Willer ch11, ch03 | No. No pack holds the survey, the 200-day readings or bank relative performance. All three are public. |
| 9 | **Missing from the sample.** List AI-linked borrowers with no traded bond and no CDS. | Loan-level data. Private placement records. Index membership. | No threshold in the skill. | `trap-detector/SKILL.md` (survivorship rule) | Partly. ETFs hold 3% of investment-grade data-centre bonds (email item 3, 19 Nov 2026). Most of the build sits in "short bank loans" (@nodiligence, 10 Nov 2026, one source). No list of borrowers. |

**Combining the flags.** Simonian ch05 gives the Noisy-OR rule: P = 1 − Π(1 − p_i). Several unlikely causes can add up to a likely outcome. The chapter says the inputs "usually come from expert opinion". It also says to add a leak term for causes left out. So a combined score is a PM judgement, not a measurement. I give no numbers.

**What "not yet identified" means in this screen.** A borrower type fails two or more of tests 1 to 5, and test 7 or test 9 says its price has not moved or cannot be seen.

### Step 3. Borrower types the tests point to

These are types. They are not trade ideas. The label rule follows `evidence-weighting/SKILL.md`: no move on a vivid but single-source claim.

- **evidence_weighted**: at least two packs support that the type exists, and at least one dated item shows its price has not moved or is not visible.
- **PM_assumption**: the type follows from the method, but the packs do not show its price either way.

| # | Borrower type | Tests it fails | Evidence it exists | Evidence it is not repriced | Label |
|---|---|---|---|---|---|
| 1 | **Developers on short bank bridges that wait for a bond take-out, where the big-tech backstop starts only at completion** | 2, 3, 4, 9 | $14.2bn one-year bridge (@nodiligence, 29 Oct 2026). $15bn of bridges on a stopped project (substack item 14, 4 Nov 2026). Banks take five months to offload risk (@junkbondinvest, 28 Oct 2026). | The debt has no traded bond, so bond spreads cannot show it (@nodiligence, 10 Nov 2026). Counter-evidence: one bank sold a data-centre loan piece at a mid-80s price (substack item 11, 21 Nov 2026). So some repricing has begun in the loan market. | evidence_weighted |
| 2 | **Vendor guarantors: equipment sellers that guarantee their customers' debt** | 5, 7 | $530bn of gross guarantees, up from $184bn a quarter earlier (substack item 8, 12 Nov 2026). Up to $72bn at a second seller (@nodiligence, 29 Oct 2026). | One guarantor's five-year CDS tightened about 12bp in the week its chief executive resigned (@nodiligence, 16 Nov 2026, one source). | evidence_weighted, thin |
| 3 | **Banks that hold the bridges, the hung data-centre loans and the risk-transfer links to private credit** | 4, 6, 9 | Ring 3a items above. An ECB probe of bank links to private credit (email item 8, 20 Nov 2026). | None. No pack quotes bank spreads or bank share prices. | PM_assumption |
| 4 | **Life insurers that hold privately rated AI and data-centre loans** | 4, 6, 9 | Email item 23 (28 Oct 2026). Substack item 20 (31 Oct 2026). Insurers hold single-A AI paper calibrated to a very low default chance (substack appendix, DEBT SERIOUS, 30 Sep 2026, second-hand). | None. No pack quotes insurer spreads. `calibration.md` says the key unknown has moved to the lenders. | PM_assumption |
| 5 | **Lease-backed single-A data-centre paper where the tenant's support is conditional** | 3, 7 | Ring 1b items above. Single-A lease-backed bonds paid 257bp against 195bp earlier in the year (@nodiligence, 10 Nov 2026). | The group tightened as a whole. One tenant's data-centre bonds moved from 180bp to 146bp over its own bonds (substack item 1, 21 Nov 2026). Spreads narrowed after 9 Nov (email item 2, 19 Nov 2026, before the 20 Nov fall). The market prices the tenant's name. No pack shows it prices the contract terms. | PM_assumption |
| 6 | **Second-order suppliers funded in private markets: sponsor-owned construction and engineering firms, and power developers without a long contract** | 1, 2, 9 | 25 sponsor deals in the first half of 2026 (@junkbondinvest, 12 Nov 2026). A power developer that could not fund its order (@nodiligence, 9 Nov 2026). | First sign of identification: two energy muni deals worth $3bn were delayed on weak demand (email item 8, 20 Nov 2026). Otherwise no prices. One post jokes that private credit managers still mark at par (@junkbondinvest, 18 Nov 2026). | PM_assumption |

**Types the market has already identified.** They are not in the table. GPU clouds with unsecured bonds near 15% (email item 10, 10 Nov 2026). CCC paper at 1,361bp (`thesis.md`). High-yield data-centre bonds, about 140bp wider since September (@junkbondinvest, 26 Oct 2026). The large issuer one notch above junk, with CDS at 341bp (@junkbondinvest, 21 Nov 2026).

**A check against the user's premise.** Contract-backed debt weakened least. It still weakened. The A-rated loan moved 7% in the week, against 10% to 12% for the unbacked debt (@nodiligence, 21 Nov 2026, one source). So the market has not ignored ring 1. It has ranked it.

### Step 4. What data is missing to run the screen for real

1. **A contract file.** Tenant, guarantor, start condition, termination rights and term for each lease-backed deal. This feeds test 3. The packs hold a handful of single deals.
2. **A bridge and construction-loan calendar.** Borrower, lender group, size, expiry date and planned take-out. This feeds tests 2 and 9. One X account asserts the store exists. No pack sizes it.
3. **Spread history by borrower and by sector.** `thesis.md` says sector spread levels "are not in free data". Without it test 7 cannot separate a borrower's move from the market's move.
4. **Lender exposure and funding.** AI and data-centre loans as a share of capital at banks, insurers and BDCs, plus how each lender funds itself. This feeds tests 4 and 6. The substack pack says nobody covers sized exposure at these lenders.
5. **Cash-flow cover by borrower.** Interest cover from operations and the share of interest that is capitalised. This feeds test 1. `fresh.md` records that the packs give "no measured answer".
6. **Three public series not yet pulled.** The Fed SLOOS, listed private-credit fund prices against their 200-day average, and bank shares against the S&P 500. These feed test 8.
7. **Guarantee terms.** Recourse and trigger terms behind the vendor guarantees. This feeds test 5. The one source is a paywalled preview.

### Limits of this note

- Every test is a sector-level method applied to borrower types. The books do not validate that step.
- Willer's rules are backtests. The index notes that several failed in the 2022 to 2023 cycle (`skill-to-use/SKILL.md`, Trust Notes).
- Schulte's skill is a single-chapter excerpt (`skill-to-use/SKILL.md`, Trust Notes).
- Much of the evidence is one X account. Several substack items are paywalled previews or digest summaries of other papers.
- I did not open the full text of any X post beyond what the corpus holds.
- The memory tools were not available in this session. I ran no prior-context lookup.
