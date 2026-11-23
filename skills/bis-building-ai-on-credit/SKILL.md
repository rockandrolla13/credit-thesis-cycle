---
name: bis-building-ai-on-credit
description: "Knowledge base from the BIS Bulletin \"Building AI on credit: structures and spillovers\" by Mathias Drehmann and Egemen Eren (October 2026), with BIS Bulletin No 120 and the BIS Quarterly Review March 2026 box as companions. Use when mapping who owns, lends to and bears loss on AI data-centre debt, reading off-balance sheet vehicles and guarantees, sizing hyperscaler debt supply against Treasury and corporate issuance, or citing the BIS event study of AI financing news on the term premium and investment-grade spreads."
---

<!-- argument-hint: [topic, framework name, or section number] -->

# Building AI on credit: structures and spillovers
**Authors**: Mathias Drehmann and Egemen Eren (BIS) | **Pages**: ~6 plus a 2-page online annex, with 2 companion documents | **Sections**: 5 | **Generated**: 2026-11-23

## How to Use This Skill

- **Without arguments** — load core frameworks for reference
- **With a topic** — ask about `residual value guarantee`, `term premium event study`, or another indexed topic. I find and read the relevant section
- **With section** — ask for `sec03`. I load that specific section
- **Browse** — ask "what sections do you have?" to see the full index

When you ask about a topic not covered in Core Frameworks below, I will read
the relevant section file before answering.

## Source Documents

| # | Title | Authors | Date | Publisher | URL |
|---|---|---|---|---|---|
| Main | "Building AI on credit: structures and spillovers", BIS Bulletin No 140 | Mathias Drehmann and Egemen Eren | 27 October 2026 | Bank for International Settlements | https://www.bis.org/publications/bulletin-140-building-ai-credit-structures-and-spillovers.pdf |
| Annex | Online annex for BIS Bulletin no 140 (Tables A1 and A2) | Same | Same | BIS | https://www.bis.org/publications/bis-bulletin/bisbulletin-140-building-ai-credit-structures-and-spillovers-online-annex.pdf |
| Companion 1 | "Financing the AI boom: from cash flows to debt", BIS Bulletin No 120 | Iñaki Aldasoro, Sebastian Doerr and Daniel Rees | 7 January 2026 | BIS | https://www.bis.org/publications/bulletin-120-financing-ai-boom-cash-flows-debt.pdf |
| Companion 2 | "Financing the AI infrastructure boom: on- and off-balance sheet borrowing", box in BIS Quarterly Review, March 2026 | Cited in Bulletin 140 as E Eren, I Krohn and K Todorov | 16 March 2026 | BIS | https://www.bis.org/publ/qtrpdf/r_qt2603u.htm |

The views are the authors' and "do not necessarily reflect the views of the BIS or its member central banks".

---

## Core Frameworks & Mental Models

### 1. The two questions (B140, Sec 1)
1. Who bears the loss if AI returns fall short?
2. Does the borrowing raise long-term rates for borrowers with no link to AI?

### 2. Good boom, bad boom (B140, Sec 1)
Risk depends on whether productivity gains arrive and whether the profits "accrue to those making the initial investments". The two boom types "are difficult to distinguish in real time" (Gorton and Ordoñez (2020)). Credit growth sizes the boom. It does not classify it. So map where the risk sits.

### 3. The structure: who owns, who lends, who loses (B140, Sec 2)
- **Owner**: a special purpose vehicle owns the site, building and chips. It issues a privately placed bond or ABS.
- **Tenants**: investment-grade hyperscalers lease capacity, "sometimes on short initial terms with options to renew". Neoclouds and AI labs, mostly unrated or sub-investment grade, sign similar contracts.
- **Lenders**: NBFIs (insurers, private credit funds) hold the debt. Banks give construction funding to vehicles and leverage to the funds.
- **Backstops**: hyperscalers and the chip vendor give residual value support and lease guarantees. These are contingent and "typically capped".
- **Loss order**: non-renewal, then re-let or sale into a glut, then the capped guarantee, then insurers and funds, then their bank lenders.
- **Where risk routes back**: a few hyperscalers and the chip vendor. Hyperscalers' off-balance sheet commitments "already exceed their reported debt" (Moody's).

### 4. Three-layer credit transformation (B140, Sec 2)
1. A secured claim on a durable, re-lettable building.
2. Chips, which are "arguably less robust as collateral".
3. Guarantees that supply the residual support for long-term investment-grade debt.

### 5. Four financial stability risks (B140, Sec 2)
Concentration. Interconnection. Partial protection. Opacity. A 2008-style funding run "appears less likely" because the debt is long term. The stated dangers are a valuation freeze, losses at holders and their banks, and delayed recognition.

### 6. The Hyperion benchmark (B140, Sec 2)
$27.3 billion of A+ bonds from a Meta and Blue Owl joint venture. Meta's lease starts in 2029, runs four years, renewable to 20 years. Priced at 225 bp over Treasuries in October 2025. Meta's own 20- and 30-year bonds priced at 88 and 98 bp two weeks later. The hyperscaler pays for flexibility "through the lease rate".

### 7. The duration-supply channel (B140, Sec 3)
Long-dated AI debt goes to NBFIs that also hold long Treasuries and IG bonds. More long supply raises the compensation for duration risk (Greenwood and Vayanos (2014)). The effect should appear in the term premium, not in policy-rate expectations.

### 8. The event study and its results (B140, Sec 3 and annex)
- Design: 18 AI-financing news sessions, 5 January to 18 September 2026, 179 daily observations. Regress the daily change in the Adrian-Crump-Moench 10-year term premium on a news-day indicator. Control for the two-year yield change and FOMC statement days. Newey-West errors.
- Term premium: **+1.53 bp** (s.e. 0.46). A normal day moves about 3.5 bp.
- Later sample (17 June to 18 September, 8 days): +2.88 bp. Financing news only (9 days): +2.15 bp. Added controls: +1.80 bp.
- **IG spread: +0.13 bp** (s.e. 0.24). Not significant.
- The rise "was reversed within two trading days".
- Yields rose more at longer maturities. The 90% band excludes zero from 8 to 30 years.
- Status: "event-day associations, not causal effects".

### 9. The pressure gauge (B140, Sec 3)
Hyperscaler bonds of 10 years or more were about 24% of corporate issuance at those maturities and 13% of gross Treasury issuance in 2026, from about 3% and 1.5% in 2024. Vehicles add more. The authors warn that sustained issuance "could make them larger and more persistent". They give no threshold.

### 10. Scale (B140, Sec 1)
Capex above $800 billion by end-2026 (five hyperscalers, about 2.5% of US GDP). Gross bond issuance $222 billion to September 2026. Vehicle-linked bonds and ABS $75 to $100 billion. Lease commitments $1.2 trillion, of which $820 billion not yet started.

### 11. The debt-equity pricing gap (B120, Sec 4)
Private credit loans to AI firms carry the same spread as other loans (6.2 against 6.1 pp). AI equity implies outsized returns. Either lenders underestimate risk or equity overestimates cash flows.

### 12. Shadow borrowing (QR box, Sec 5)
Off-balance sheet obligations are "economically akin to debt". Three shock channels: vehicle refinancing pressure, procyclical private credit appetite, activation of guarantees.

---

## Which Claims Are the Authors' Estimates

- **Authors' regression estimates** (B140 annex): every coefficient in Table A1, the two-day reversal, the curve response.
- **Authors' calculations from market data**: the $222 billion issuance, the "more than 10%" of long-term Treasury issuance, the 24% and 13% shares, the Graph 1.C boom comparison.
- **Third-party numbers the authors cite**: $1.2 trillion and $820 billion of leases (Moody's Ratings), $75 to $100 billion of vehicle debt ("market sources"), nearly $9 trillion of data centre investment over 2025-32 (Van Nieuwerburgh (2026)), capex above $800 billion (company guidance).
- **B120 authors' estimates**: AI investment at 1% of GDP (uses a rule that equipment is three times construction), the 0.4 pp growth contribution, the $300 to $600 billion private credit projection for 2030, all PitchBook-based loan statistics.
- **Chart readings made for this skill**: any value marked "approximate" or "chart reading" in the section files. These are not stated in the source text.

## Method or Case

The whole source describes one live episode, the AI credit boom of 2025-26. Inside it:

- **METHOD** (how to reason, measure, test):
  - sec02 — the loss-allocation map, three-layer transformation, four risks.
  - sec03 — the event-study design, curve test, credit placebo, issuance-share gauge.
  - sec04 — the debt-equity pricing gap test, the investment boom comparison, the 3x equipment rule.
  - sec05 — the three shock transmission channels.
- **CASE** (dated facts on the current episode, to be kept apart from fresh reasoning):
  - sec01 — scale numbers as of October 2026.
  - sec02 — the Hyperion and NVIDIA worked examples.
  - sec03 — the Table A1 results and the Table A2 event list.
  - sec04 — the January 2026 numbers on private credit and GDP.
  - sec05 — the March 2026 numbers on issuance and CDS.

sec02, sec03 and sec04 hold both. Take the method from them. Treat their numbers as case data with a date.

## Trust Notes

- All three documents are short central-bank notes. They are not peer-reviewed papers. The main Bulletin is six pages.
- The event study rests on 18 days in under nine months. The authors say the estimates are not causal. Sub-sample results rest on 8 or 9 days.
- The main text gives the sample start as 6 January 2026. The annex gives 5 January.
- Every graph was an image. Graph 2 (the structure diagram) was fully recovered from PDF page 3. Graph 1, Graph 3 and the Quarterly Review Graph A1 values are approximate chart readings where marked. Bulletin 120 Graphs 1 to 4 were not read beyond what the text states.
- The Quarterly Review box was taken from the HTML page. Its author names come from the reference list of Bulletin 140, not from the page text.
- The three documents have different dates and different firm samples. "AI firms" means five hyperscalers in some graphs, seven firms in Graph 1.C and three PitchBook verticals in Bulletin 120 Graph 3. Do not mix them.
- The Bulletin 120 projection of $300 to $600 billion cannot be rebuilt from the stated inputs. Cite it, do not recompute it.
- The source names firms "for illustrative purposes" and makes no statement on their soundness.
- The source gives no default probabilities, loss rates, recovery values or fair-value spreads.

## Use for Credit and Macro Questions

- **Credit spreads**: one direct test. On 18 AI news days the IG index spread moved 0.13 bp, not significant. One deal benchmark: Hyperion at 225 bp against 88 to 98 bp for its tenant. Private credit spreads on AI loans equal the market average (January 2026). CDS on lower-rated hyperscalers had risen by March 2026.
- **Debt-financed investment booms**: the main use. Scale, the good boom and bad boom benchmark, the loss map for off-balance sheet vehicles, and a comparison with seven past investment booms.
- **Inflation and Fed regimes**: nothing on inflation. On rates, only the term premium channel: a supply-driven rise "tightens financial conditions regardless of the stance of monetary policy".
- **Issuer screening**: a checklist, not a score. Off-balance sheet commitments against reported debt, lease term against bond term, guarantee caps, chip collateral, floating-rate chip borrowing at neoclouds, and multiple links to one chip vendor.

---

## Section Index

| # | Title | Key Frameworks |
|---|-------|----------------|
| [sec01](chapters/sec01-ai-credit-boom-scale.md) | Key Takeaways and the Scale of the AI Credit Boom (B140) | Two questions, good boom and bad boom test, three channels of AI debt, scale table |
| [sec02](chapters/sec02-financing-structures-risk-allocation.md) | Emerging Credit Relationships and Risks (B140) | Graph 2 structure, who owns / lends / loses, three-layer transformation, four risks, Hyperion |
| [sec03](chapters/sec03-spillovers-event-study.md) | Spillovers to Broader Bond Markets (B140 and annex) | Duration-supply channel, event-study method, Table A1, Table A2, issuance shares |
| [sec04](chapters/sec04-companion-bulletin-120-cash-flows-to-debt.md) | Companion: Financing the AI Boom, From Cash Flows to Debt (B120) | Cash flow to debt shift, private credit terms, debt-equity pricing gap, boom comparison |
| [sec05](chapters/sec05-companion-qr-box-on-off-balance-sheet.md) | Companion: On- and Off-Balance Sheet Borrowing (QR box) | Common vehicle structure, shadow borrowing, three shock channels, CDS by rating |

## Topic Index

- **AI news days (list of 18)** → sec03
- **Banks' exposure** → sec02, sec05
- **Capex (hyperscalers)** → sec01, sec04, sec05
- **CDS spreads of hyperscalers** → sec05
- **Chip collateral** → sec02
- **Chip vendor / NVIDIA support** → sec02, sec03
- **Circular financing** → sec02, sec04
- **Concentration risk** → sec02
- **Debt-equity pricing gap** → sec04
- **Dot-com comparison** → sec04
- **Duration risk / duration investors** → sec03
- **Event study (method and results)** → sec03
- **Free cash flow against capex** → sec04
- **GDP contribution of AI investment** → sec04
- **Good booms and bad booms (Gorton and Ordoñez)** → sec01
- **Guarantees / residual value** → sec02, sec05
- **Hidden leverage / shadow borrowing** → sec04, sec05
- **Hyperion (Meta and Blue Owl)** → sec02
- **Investment-grade spreads** → sec03
- **Issuance shares (24% and 13%)** → sec03
- **Lease commitments ($1.2 trillion)** → sec01, sec02
- **Loss allocation** → sec02
- **NBFIs (insurers, private credit funds)** → sec02, sec03
- **Neoclouds** → sec01, sec02
- **Off-balance sheet vehicle** → sec02, sec05
- **Opacity and disclosure** → sec02
- **Private credit** → sec04, sec05
- **Table A1 (regressions)** → sec03
- **Term premium** → sec03
- **Treasury market spillover** → sec03

## Supporting Files

- [glossary.md](glossary.md) — all key terms with definitions
- [patterns.md](patterns.md) — all techniques and test designs
- [cheatsheet.md](cheatsheet.md) — loss map, decision rules, number table, stress path
- Full text: `/home/ak/.local/share/book-to-skill/fulltext/bis-building-ai-on-credit/full_text.txt` — all three documents and the annex (local extraction, not shipped)
- Source files: `/home/ak/Documents/PapersForThemes/bis-building-ai-on-credit/`

---

## Scope & Limits

This skill covers the three BIS documents and the annex only. It reports the authors' rules and estimates as theirs. It gives no trade recommendation. The data end in September 2026 for the main Bulletin. Later issuance, spreads and events are not in the source and are not supplied here.
