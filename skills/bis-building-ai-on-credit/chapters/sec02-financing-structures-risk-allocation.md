# Section 2: Emerging Credit Relationships and Risks in the AI Credit Boom
Source: BIS Bulletin No 140, pp 2-4 (Graph 2, footnotes 3 to 6). Dated 27 October 2026.

## Core Idea
A small number of investment-grade firms support a web of on- and off-balance sheet commitments. Vehicles turn data-centre risk into long-dated investment-grade debt. The structures "obscure the final allocation of risks", and the real exposures concentrate in a few large firms, "more than what their balance sheets suggest".

## Frameworks Introduced

### The stylised structure (Graph 2, recovered from PDF p 3)
Graph 2 has five boxes. Solid arrows are "cash and contracts". Dashed arrows are "guarantees and backstops: contingent claims, where risk routes back".

| Party | Credit standing | What it gives the vehicle or the chain | Arrow type |
|---|---|---|---|
| **Data centre vehicle** | Issues private debt | "owns the site, building and chips" | Centre |
| **Hyperscalers** | Investment grade | "equity, leases, offtake" | Solid |
| **Hyperscalers** | Investment grade | "guarantees" | Dashed |
| **Neoclouds, AI labs** | Mostly unrated or below investment grade | "offtake" | Solid |
| **Chip vendor** | Not stated in the graph | "chips" to the vehicle | Solid |
| **Chip vendor** | | "residual-value support" to the vehicle | Dashed |
| **Chip vendor** | | "equity, capacity backstop" to neoclouds and AI labs | Dashed |
| **NBFIs** (insurers, private credit funds) | | Hold the vehicle's "debt" | Solid |
| **Banks** | | "funding lines" to the vehicle | Solid |
| **Banks** | | "fund leverage" to the NBFIs | Solid |

### Who owns, who lends, who bears loss (pp 2-4)

| Question | Answer in the source |
|---|---|
| Who owns the asset? | The special purpose vehicle. It owns the data centre and "earns its income from the contracts it has signed". The hyperscaler sometimes holds a minority stake and does not consolidate. |
| Who lends? | Institutional investors, often through private placement, buy the vehicle's bond or asset-backed security. Banks give construction financing to some vehicles. Banks may also lend to the private credit funds that buy the debt. Neoclouds also borrow against their chips, "often at floating rates". |
| Who pays the income? | Hyperscalers lease capacity, "sometimes on short initial terms with options to renew". Neoclouds and AI labs sign similar contracts. |
| Who supports the residual? | Hyperscalers, in some cases, through a guarantee of the residual value of the assets. The chip vendor, in some cases, through contingent support for facility lease obligations and limited protection against a fall in asset values. |
| Who bears loss first if the lease is not renewed? | The vehicle must find a new tenant or sell the assets. It can then call the residual value guarantees, "but they are typically capped". |
| Who bears the loss beyond the cap? | "the insurers, funds and other investors that hold the debt as well as ... their bank lenders". |
| Where does risk route back? | To the hyperscalers and the chip vendor, through the dashed arrows. Hyperscalers' aggregate off-balance sheet commitments "already exceed their reported debt" (Moody's Ratings (2026)). |

### How the structure transforms credit (p 3)
1. **Ring-fence the building.** Lenders get a secured claim on a durable building. The building, its power connection and its cooling plant "can be rented to other tenants".
2. **Add the chips as collateral.** The authors call chips "arguably less robust as collateral". They have fewer other uses and may lose value with each new generation. So capacity contracts and initial lease terms "typically run for a few years".
3. **Add guarantees.** Guarantees from hyperscalers and chip vendors provide the residual support needed "to issue long-term investment-grade debt".

### Who gains what (p 4)
- **Neoclouds and AI labs**: access to long-dated investment-grade funding from a deep investor pool.
- **Hyperscalers**: capacity without direct balance sheet debt. Payments can be recorded as operating expenses, not debt-financed capex. They keep rating headroom. They avoid owning chips that the next generation may make obsolete. Short initial terms with renewal options give flexibility.
- **The price of that flexibility**: the lease rate. The vehicle's debt yields more than the hyperscaler's own bonds.
- **Chip vendor**: support for customer financing "sustains demand for its hardware".

### The four financial stability risks (p 4)
1. **Concentration.** Lease commitments and guarantees rest on a small number of large firms. Mitigant stated in the text: hyperscalers generate large cash flows from non-AI segments.
2. **Interconnection.** A chip supplier may sell hardware to a customer, hold its equity, buy its capacity and guarantee some of its payments. Trouble at the customer hits the supplier through each channel. Banks are exposed directly (construction loans) and indirectly (loans to funds).
3. **Partial protection.** Contractual support covers investors only in part. Non-renewal or early termination can force a re-let or sale "at a time when similar capacity is also being offered to the market".
4. **Opacity.** Leases not yet started are disclosed but not recorded as debt. Guarantees are "often recorded at little or no value until payments become likely". Such claims are harder to size than bonds.

## Key Concepts
- **Off-balance sheet vehicle / special purpose vehicle**: an entity that owns the data centre and issues the debt. The sponsor does not consolidate it.
- **Offtake**: a contract to take capacity from the vehicle (Graph 2 label).
- **Residual value guarantee**: support for the value of the assets at the end of the lease. Typically capped.
- **Capacity backstop**: the chip vendor's commitment to buy computing capacity from some neoclouds.
- **Rating headroom**: room under the current rating that the hyperscaler keeps by not adding the debt.
- **Circular financing**: the multiple links between AI firms. The source points to BIS Bulletin No 137 (Frost et al (2026)) and does not develop it.
- **Hidden single-name exposure**: a lender's total exposure to one ultimate guarantor across its bonds and several vehicles.

## Mental Models
- Use the dashed arrows as the map of loss. Solid arrows show who pays in normal times. Dashed arrows show where the claim lands in stress.
- Think of the lease rate as the price of an option. The hyperscaler pays extra spread to keep the right not to renew.
- Treat a short initial lease term against long bonds as the weak joint. The bond is investment grade because of a renewal the tenant has not promised.
- Think of the same vendor's chips in many hands as correlated collateral. Resale values "could fall sharply if many seek to sell used chips at the same time".

## Anti-patterns
- **Reading hyperscaler leverage from the balance sheet**: commitments already exceed reported debt.
- **Treating the vehicle rating as the tenant's rating**: the guarantee is partial and capped.
- **Counting exposure bond by bond**: "Without a clear view of the ultimate guarantor, lenders may hold larger exposures to a single firm than they realise."
- **Expecting a 2008-style run**: most of the debt is long term, so a run on short-term funding "appears less likely". The stated failure modes are different: a market freeze because investors cannot value the debt, losses at holders and their bank lenders, and delayed recognition.

## Worked Example: the Hyperion data centre (footnotes 3 and 5)
1. **Owner**: a joint venture between Meta and Blue Owl managed funds. Meta does not consolidate the venture.
2. **Debt**: $27.3 billion of privately placed senior secured bonds, rated A+ by S&P. That is one notch below Meta.
3. **Support**: Meta's lease commitments. They begin in 2029 and initially run for four years. Options to renew give a total lease term of up to 20 years.
4. **Residual protection**: "limited residual-value protection for the first 16 years of operation".
5. **Price**: 225 basis points over Treasuries in October 2025.
6. **Comparison**: two weeks later Meta's own 20-year and 30-year bonds priced at 88 and 98 basis points over Treasuries.
7. **Reading**: the vehicle paid roughly 127 to 137 basis points more than its tenant at long maturities. The gap is arithmetic on the two quoted prices. The source presents it as the cost of flexibility that hyperscalers pay "through the lease rate".

## Worked Example: the chip vendor's support (footnote 4, annex Table A2)
- August 2026: NVIDIA signed memoranda of understanding with six investment firms. The platforms aim to raise more than $500 billion of third-party capital for AI infrastructure over time.
- NVIDIA said it may provide residual value support for up to 25% of a project. It did not specify the form.
- Annex Table A2 also lists, for 17 August 2026, NVIDIA guarantees of up to $105 billion for data centre leases of an OpenAI affiliate.

## The worked case of hidden exposure (p 4)
An insurer holds a hyperscaler's bonds and the debt of several vehicles leased to that hyperscaler. Its exposure to the hyperscaler is larger than its bond holdings alone suggest.

## Policy conclusion (p 4)
"Closer monitoring and fuller disclosure of these commitments would help investors, rating agencies and supervisors assess the risks."

## Key Takeaways
1. The vehicle owns the asset. NBFIs hold the debt. Banks lend to both the vehicle and the NBFIs.
2. The investment-grade rating comes from three layers: the building, the chips, and capped guarantees.
3. Loss beyond the cap falls on insurers, funds and their bank lenders.
4. Risk routes back to a few hyperscalers and one kind of chip vendor.
5. The stress path is non-renewal, re-letting into a glut, a capped guarantee, then slow loss recognition.
6. The risks grow "especially if their adoption becomes more widespread".

## Extraction Notes
- Graph 2 was an image. The table above reproduces every label after reading PDF page 3.
- The source names individual firms "for illustrative purposes" and says this is no statement on their soundness.

## Connects To
- **Section 1**: the size of the commitments ($1.2 trillion of leases).
- **Section 3**: the same NBFIs hold long-dated Treasuries and investment-grade bonds.
- **Section 5 (Quarterly Review box)**: the earlier description of the same structure as "shadow borrowing".
