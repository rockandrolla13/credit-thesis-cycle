---
name: van-nieuwerburgh-financing-ai-buildout
description: "Knowledge base from the paper \"Financing the AI Buildout\" by Stijn Van Nieuwerburgh (NBER Working Paper 35865, October 2026). Use when sizing AI data-centre investment and debt supply, costing a data-centre campus per MW, reading off-balance-sheet structures (leases, joint ventures, SPVs, residual value guarantees, vendor financing), adjusting hyperscaler leverage for leases, testing asset life against debt term, computing the revenue or GPU-hour price a buildout needs, or citing the Hyperion (Meta and Blue Owl) transaction."
---

<!-- argument-hint: [topic, framework name, or section number] -->

# Financing the AI Buildout
**Author**: Stijn Van Nieuwerburgh (Columbia Business School and NBER) | **Pages**: 32 | **Sections**: 6 plus 4 appendices | **Generated**: 2026-11-23

## Source Record
- **Exact title**: Financing the AI Buildout
- **Author**: Stijn Van Nieuwerburgh
- **Series and date**: NBER Working Paper No. 35865, October 2026
- **Version used**: the draft dated October 2, 2026, inside the NBER PDF. The paper says it is forthcoming in the Fall 2026 Brookings Papers on Economic Activity. It is not peer-reviewed.
- **URL**: https://www.nber.org/papers/w35865 (PDF: https://www.nber.org/system/files/working_papers/w35865/w35865.pdf)
- **Local copy**: `/home/ak/Documents/PapersForThemes/van-nieuwerburgh-financing-ai-buildout/w35865.pdf` (sha256 `f18a7506...5891ed`)
- **Scope**: United States only. Project data as of September 12, 2026.

## How to Use This Skill

- **Without arguments**: load the core frameworks below
- **With a topic**: ask about `Hyperion`, `residual value guarantee`, `cost per MW`, `required revenue`. I find and read the relevant section file
- **With a section**: ask for `sec04` or `appendix D`
- **Browse**: ask "what sections do you have?"

When a question needs detail that is not in Core Frameworks, I read the section file before I answer.

---

## Core Frameworks & Mental Models

### 1. AI is a physical capital boom (Sec I, Sec II)
The near-term footprint of AI is chips, power, cooling and buildings. Treat it as an infrastructure investment cycle. A general-purpose technology induces complementary investment in a physical network. Returns depend on uncertain future demand. Financing needs are large.

### 2. The campus cost model: $41m per MW (Sec II, App A)
| Block | $m per MW of total facility power | Share |
|---|---|---|
| Facility (real estate, cooling, backup power) | 11 | about 27% |
| Power infrastructure | 2 | about 5% |
| IT (GB300 racks at $4m, plus 20% for network, storage, integration) | 28 | about 68% |

A 200 MW campus costs about $8.2bn in 2025. A 1 GW campus costs about $41bn. Cost grows 4% a year by completion cohort. These are the author's estimates.

### 3. Pipeline is not supply: the realisation scenario (Sec II, App B)
- Announced: about 494 GW of planned and under-construction US capacity (Cleanview, September 12, 2026).
- Central scenario: 188.3 GW completes in 2025-32. 114.9 GW completes later. 213.5 GW never completes.
- Haircut rule: the by-2032 share falls from 90% (2026 projects) by 10 points per year of horizon. Undated projects get 20%. Projects with imputed capacity get less.
- Capacity-weighted non-realisation is 43.2%. Project-count cancellation is 32.6%.

### 4. The investment bill (Sec II, App B, App C)
$8.973tn in 2025-32. Average 3.22% of GDP a year. Peak 4.96% in 2028. Past US booms were smaller: railroads 2.24%, highways 1.13%, telecom and fiber 1.10%, canals 0.66%, electrification 0.50%. The estimate excludes IT replacement and later pipeline growth.

### 5. The financing gap (Sec III, Fig 1)
Capex of Oracle, Microsoft, Amazon, Meta and Alphabet went from about $97bn (2020) to more than $400bn (2025). The 2026 projection exceeds $800bn. That is above combined operating cash flow for the first time. External capital fills the gap.

### 6. Three-way separation (Sec III)
The structures separate users of compute, owners of assets, and investors who bear financial risk. They substitute project-level debt and third-party equity for hyperscaler equity and corporate debt. The hyperscaler stays central through leases, capacity commitments and guarantees. The shift relocates "ownership and leverage, rather than fully transferring the underlying economic risk".

### 7. Aggregate split hides asset-level leverage (Sec III)
Morgan Stanley projects about 60-40 equity to debt across the buildout. But hyperscaler cash goes mostly to IT. Shells and power go into levered vehicles. Asset-level leverage is therefore higher than the aggregate, and less visible.

### 8. The Hyperion template (Sec IV)
Five ingredients: investment-grade tenant credit, high project leverage, bankruptcy-remote entities, lease optionality, a residual value guarantee. Numbers: $27bn debt on $30bn assets (about 90%), DSCR 1.12x, A+ rating, 6.58% yield, at least 100bp above Meta's likely unsecured cost, more than $5bn extra interest. The rationale "is therefore not cheaper financing, but preservation of an asset-light corporate profile".

### 9. Lease-adjusted leverage (Sec IV, footnote 6)
Add commenced leases plus 0.75 times uncommenced leases to debt. For four hyperscalers excluding Amazon (June 2026): debt to capital goes from 20% to 48%. Debt to EBITDA goes from 0.7x to 2.6x.

### 10. Three vulnerabilities and one amplifier (Sec V)
Vulnerabilities: tenant and demand concentration, technological obsolescence, execution. Amplifier: high asset-level leverage and layered claims on fixed debt service. A modest shortfall in demand, timing or asset value produces much larger equity losses and can impair creditors.

### 11. Asset life versus debt term (Sec IV, Sec V, App C, App D)
- IT is 68% of cost. Its assumed economic life is six years. GPUs "may become economically obsolete within three to six years".
- Non-IT assets are 32% of cost with a 20-year life.
- Hyperion's bonds mature in 2049. Its leases are five four-year terms from 2029 with termination options.
- A three-year IT life raises the capital charge from 19.37% to 31.10%.

### 12. The required-revenue test (Sec V, App D)
The 2025-32 cohorts need about $3.55tn of mature annual revenue for a 10% unlevered return at a 50% cash margin. That is 8.8% of 2032 GDP and $5.1 per installed GPU-hour. At 80% utilisation it is $6.4 per billed hour. The Ornn index showed $6.07 on August 31, 2026.

### 13. Circularity (Sec V, footnote 9)
Suppliers finance their own customers. Example: a $500bn facility for NVIDIA chips (August 2026) with a 25% NVIDIA residual value guarantee, worth up to $125bn of backstops.

### 14. Measure and disclose first (Sec VI)
The author does not claim distress is imminent or that risk is already systemic. The priority is to map who bears demand, refinancing and residual-value risk.

---

## Key Techniques

**Bottom-up campus costing** (App A)
MW of facility power, then PUE, then racks, then rack price plus 20% add-ons, then facility and power per MW.

**Pipeline haircut** (App B)
Split announced capacity into by-horizon, later and never. Use lower rates for distant, undated and undisclosed projects.

**Spend phasing** (App B)
5.122% in t-3, 5.122% in t-2, 17.561% in t-1, 72.195% in the completion year t.

**Capital-recovery revenue test** (App D)
Capital base times a life-weighted annuity factor, divided by cash margin. Convert to dollars per GPU-hour.

**Lease-adjusted leverage** (Sec IV, footnote 6)
L2 and L4 from the formula above.

**Opacity read from CDS** (Sec IV, footnote 8)
Compare five-year CDS moves across hyperscalers over the build period.

---

## Section Index

| # | Title | Key frameworks |
|---|---|---|
| sec01 | Introduction | Three-part argument, headline numbers |
| sec02 | AI as a Physical Capital Boom | Cost per MW, pipeline, scenario, Table 1 |
| sec03 | Ownership and Financing of AI Infrastructure | Financing gap, structures list, asset-level leverage |
| sec04 | Financial Architecture and Risk | Hyperion deal, RVG, GAAP gap, lease-adjusted leverage, CDS |
| sec05 | Risks in the AI Infrastructure Buildout | Three vulnerabilities, amplifier, circularity, REIT betas |
| sec06 | Policy and Research Questions | Measurement, disclosure list, stability questions |
| sec07 | Appendix A: Representative AI Campus Cost | Table 2, cost cross-checks |
| sec08 | Appendix B: Data Centers Capacity Count | Tables 3, 4, 5, haircut rates, spend phasing |
| sec09 | Appendix C: Historical Investment Booms | Six episodes, sources, asset-life caveat |
| sec10 | Appendix D: Revenue Required | Equations 2-7, Tables 6, 7, GPU-hour prices |

---

## Topic Index

- Accounting (GAAP) gap -> sec04
- Asset life, economic life of GPUs -> sec05, sec09, sec10
- Beta of data-centre REITs -> sec05
- Cancellation and non-realisation rates -> sec02, sec08
- Capex versus operating cash flow -> sec03
- CDS spreads -> sec04
- Circularity, vendor financing -> sec05
- Cost per MW -> sec02, sec07
- Disclosure wish list -> sec06
- GPU collateral, GPU-backed finance -> sec03
- GPU-hour price required -> sec05, sec10
- Historical booms -> sec02, sec09
- Hyperion, Beignet, Blue Owl -> sec04
- Lease commitments off balance sheet -> sec04
- Lease-adjusted leverage -> sec04
- Morgan Stanley financing split -> sec03
- Pipeline in GW -> sec02, sec08
- Private credit -> sec03, sec04
- Required revenue -> sec05, sec10
- Residual value guarantee -> sec04, sec05
- Sopaipilla -> sec04
- Spend phasing -> sec08
- Systemic risk position -> sec05, sec06

---

## Whose Numbers Are Whose

**The author's own estimates, scenarios and calculations**
- $41m per MW, $8.2bn per 200 MW campus, the three cost blocks (App A)
- 188.3 GW, 114.9 GW and 213.5 GW outcomes, and every haircut rate in Table 4 (App B). These are assumptions, not estimated probabilities
- 32.6% and 43.2% implied non-realisation (App B)
- $8.973tn, 3.22%, 3.17%, the annual path in Table 5 (App B)
- The historical-boom ratios, computed by the author from the cited historical series (App C)
- $3.549tn required revenue, Tables 6 and 7, all GPU-hour prices, the 81.3% growth rate (App D)
- Lease-adjusted leverage: 20% to 48%, 0.7x to 2.6x (Sec IV, footnote 6)
- Data-centre REIT rolling betas (Sec V, Fig 3)
- Capex and operating cash flow series, built from filings. The 2026 values use guidance and Wall Street estimates (Fig 1)
- "At least 100 basis points" and "more than $5 billion" for Hyperion's extra cost (Sec IV)

**Third-party numbers the author quotes**
- Morgan Stanley Research (2025): $2.9tn for 2025-2028, more than half external, 60-40 equity to debt, private credit $800bn, corporate debt $200bn, structured finance $150bn
- Moody's Ratings (2026a): $970bn lease commitments, $660bn not yet on balance sheet
- Wall Street Journal: $2.4tn off-balance-sheet liabilities for four hyperscalers
- S&P: Hyperion A+ rating, deal facts from the pre-sale report
- Moody's Ratings (2026c): 45 GW of new generation by 2030 for $110bn
- JLL (2026): $11.3m per MW. Cleanview: $8.9m per MW and all project counts
- Brandsaas et al. (2025): 33% abandonment rate
- Ornn Compute Price Index: $6.07 per GPU-hour on August 31, 2026
- CDS levels: reported without a named source

---

## Method or Case

**METHOD** (how to measure, reason, test)
- sec01 Introduction (framing)
- sec02 AI as a Physical Capital Boom (sizing method)
- sec03 Ownership and Financing (capital-stack map)
- sec05 Risks (risk framework). It contains two short case items: the NVIDIA facility and the REIT beta evidence
- sec06 Policy and Research Questions
- sec07 Appendix A (cost model)
- sec08 Appendix B (pipeline-to-investment model). Its inputs are a dated snapshot, September 12, 2026
- sec10 Appendix D (required-revenue model)

**CASE** (a past episode or transaction)
- sec04 Financial Architecture and Risk: the Hyperion transaction of October 2025, the Sopaipilla deal of July 2026, and the CDS moves to July 2026. The lease-adjusted leverage formula in footnote 6 is method
- sec09 Appendix C: US investment booms from 1836 to 2003

Note: sec02, sec03, sec08 and sec10 mix method with current-episode numbers. The formulas are method. The dated numbers are case data about the 2025-2026 buildout.

---

## Trust Notes

- **Text source**: `pdftotext`, text mode, 32 pages, about 12,600 words. The body, footnotes, all seven tables and all equations came through and were checked against each other.
- **Figure 1** is a chart. Its data labels came through, but the mapping of labels to years in sec03 is this skill's reading. Check the PDF before you cite a single year. The Capex/OCF ratio line has no readable values.
- **Figure 2** (the Hyperion entity diagram) is lost. Only the caption survives. Entity names in sec04 come from that caption.
- **Figure 3** (REIT betas) is lost. Only the text claim "from roughly 0.5 to around 1" and the specification notes survive. There is no beta series and no standard error.
- **Working paper**. Not peer-reviewed. Other drafts exist (the paper mentions a March 2026 webinar and a Brookings workshop). Their numbers may differ. This skill uses only the October 2, 2026 draft.
- **Small internal inconsistencies in the source**: the abstract says a 1 GW campus costs about $41bn and "nearly $9 trillion", with 3.2% of GDP. The body gives $8.973tn, 3.22% as the average of annual ratios and 3.17% of cumulative GDP. Table 6 uses $8.762tn, a different cohort basis (footnote 11). Say which one you use.
- **The haircut rates are assumptions.** The author calls the result "a scenario rather than a forecast". The undated 313.9 GW is "the largest source of uncertainty".
- **The paper has no credit-loss model**, no spread model, no default or recovery estimate, and no aggregate debt-issuance forecast of its own. The debt split is Morgan Stanley's.
- **The CDS reading is an interpretation.** The paper does not test it against other causes.
- **Hyperion's $30bn excludes IT equipment.** Do not divide it by 2 GW and compare with $41m per MW.

---

## Use for Credit and Macro Questions

- **Credit spreads**: gives one priced data point for the off-balance-sheet premium. Hyperion's A+ debt came at 6.58%, at least 100bp over Meta's likely unsecured cost. It also gives five-year CDS moves for five hyperscalers (November 2025 to July 2026). It gives no spread model and no index-level analysis.
- **Debt-financed investment booms**: this is its main use. It sizes the boom ($8.973tn, 3.22% of GDP a year), ranks it against five past US booms, maps the financing structures, and states three conditions under which such booms turn financially consequential.
- **Inflation and Fed regimes**: nothing. The paper assumes 4% nominal GDP growth and 4% cost growth. It does not discuss inflation, rates or policy.
- **Issuer screening**: gives a lease-adjusted leverage formula, a disclosure checklist (leases, residual value guarantees, joint-venture stakes, tenant concentration, renewal options) and a capex-to-operating-cash-flow test. It covers five hyperscalers only.
- **Supply sizing**: gives a method to turn announced GW into dollars per year, and the quoted Morgan Stanley split of the debt by channel.

---

## Supporting Files

- [Glossary](glossary.md)
- [Patterns](patterns.md)
- [Cheatsheet](cheatsheet.md)
- [Sections](chapters/)
