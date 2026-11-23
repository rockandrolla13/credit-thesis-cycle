---
name: chaudhary-corporate-bond-multipliers
description: "Knowledge base from the paper \"Corporate Bond Multipliers: Substitutes Matter\" by Manav Chaudhary, Zhiyu Fu and Jian Li (LSE FMG Discussion Paper 955, June 2026). Use when sizing the price effect of a demand shift in corporate bonds, choosing between bond-level and rating-bucket multipliers, checking how long demand-driven price pressure lasts, judging spillover between close substitutes, building a flow-induced demand shock, or testing a claim that bond supply or flows are priced into spreads."
---

<!-- argument-hint: [topic, framework name, or section number] -->

# Corporate Bond Multipliers: Substitutes Matter
**Authors**: Manav Chaudhary (University of Chicago), Zhiyu Fu (Washington University in St. Louis, Olin Business School. The paper prints "Zhiyu Fu". Other listings give "Julie Zhiyu Fu"), Jian Li (Columbia Business School)
**Version**: Financial Markets Group Discussion Paper No. 955, June 2026, ISSN 0956-8549 | **Pages**: 108 | **Section files**: 9 | **Generated**: 2026-11-23
**URL**: https://www.fmg.ac.uk/sites/default/files/2026-06/DP955.pdf (landing page: https://www.fmg.ac.uk/publications/discussion-papers/corporate-bond-multipliers-substitutes-matter)

## How to Use This Skill

- **Without arguments** — load core frameworks for reference
- **With a topic** — ask about `aggregation`, `passthrough`, or another indexed topic; I find and read the relevant section file
- **With section** — ask for `sec04`; I load that specific file
- **Browse** — ask "what sections do you have?" to see the full index

When you ask about a topic not covered in Core Frameworks below, I will read
the relevant section file before answering.

---

## Core Frameworks & Mental Models

### 1. What a multiplier is (Section 1 footnote 1, Section 2.1)
The multiplier M is "the direct price effect of the demand shock holding the prices of all other assets fixed". It is about one over the own-price demand elasticity. Unit: percent of price per 1 percent demand shock. The shock is a share of the asset's amount outstanding. The response is a return. The paper never converts it to a spread.

### 2. The pricing equation (Section 2.1, eq. 4)
`Δp_j = M u_j + M̃ Δp_sub + ν̃`. M is the own multiplier. M̃ is the **substitute passthrough**: the percent rise in an asset's price when its close substitutes rise 1 percent. "The total price impact of demand shocks ultimately depends on the structure of the shocks." Ask whether a shock is specific to one bond or shared by similar bonds.

### 3. Two-layer substitution and the aggregation rule (Section 2.2, eq. 8 to 12)
Bonds in the same detailed rating are close substitutes (elasticity γ^c). All others are distant (γ^d). At the bond level `M = 1/γ^o` and `M̃ = γ^c/γ^o`. For a whole close-substitute group `M^G = 1/(γ^o - γ^c)`. Widening the asset removes the escape route to close substitutes. So "the more aggregated the demand shock, the higher the multiplier and the lower the substitute passthrough".

### 4. The estimates, by level (Section 4, Tables 1, 2, 5)
| Asset | Substitutes held fixed | M | M̃ |
|---|---|---|---|
| Single bond, time fixed effects only | market | 0.41*** | n/a |
| Single bond | same detailed rating | 0.04 to 0.06, not significant | 1.11*** |
| Detailed rating x quarter to maturity | same detailed rating | 0.29** | 0.99*** |
| Coarse rating x 3 maturity groups | same coarse rating | 1.33* | 0.77*** |
| Coarse rating x 2 maturity groups | same coarse rating | 1.71* | 0.56** |
| Coarse rating (AAA, AA, A, BBB ...) | same investment-grade category | 3.94*** | -0.04, not significant |

Read the last row as: a demand shock of 1% of a rating bucket's outstanding moves that bucket's price about 3.94% on impact, with no measurable spillover to other buckets. It rests on 469 observations and a first-stage F of 21. It pools all coarse ratings. The paper gives no separate AA or BBB number at this level.

### 5. How long it lasts (Section 4.3, Table 6)
Baseline portfolio only. Cumulative effect: 0.27** in the shock quarter, 0.04 one quarter later, -0.01 and -0.16 after that. The effect "almost fully reverts in the following quarter". The paper does not test persistence at the rating-bucket level.

### 6. Identification (Section 3)
The shock is flow-induced trading by 1,071 US bond mutual funds, 2002Q1 to 2021Q3, quarterly. Three steps: fund flow over lagged AUM, strip the predictable part with a three-lag autoregression, sum over funds using lagged holding shares. It is a Bartik design. It needs lagged shares to be exogenous (**Assumption 1**), not the flows. The passthrough needs the group version (**Assumption 1'**). Checks: one-year share lags, factor controls, factor-purged flows, large shocks only, PIMCO outflows in 2014, index rebalancing.

### 7. Why the bias arises (Section 2.2)
Leaving out close-substitute returns overstates M for two reasons. General equilibrium lifts close substitutes when a bond is shocked. Flow and mandate shocks hit similar bonds together. Bond level: 0.41 falls to about 0.06. Stocks: 0.38 falls only to 0.25 (Appendix IA.D).

### 8. Heterogeneity and arbitrage risk (Section 5)
At the baseline portfolio level the pooled investment-grade multiplier is "close to 0" and the pooled high-yield multiplier is "around 0.6". Short maturities are near 0. Medium and long are "around 0.3-0.5", not significantly different. One standard deviation more arbitrage risk adds 0.43 to M. Sharpe ratios of trading the gap are 0.02 to 0.11. The authors call this evidence "suggestive".

### 9. Stated limits
- Shocks are secondary-market fund flows. No estimate uses issuance.
- Net supply is held constant in the framework. With elastic supply the multiplier is "the inverse of a weighted average of supply and demand elasticities" (footnote 9).
- "Our identification strategy does not allow us to uncover the macro elasticity for the corporate bond market as an asset class" (footnote 30).
- Crisis quarters (2008Q3-Q4, 2020Q1-Q2) are dropped. "We cannot rule out the possibility that multipliers differ in crisis periods" (footnote 25).
- Flows are assumed to pass one for one into demand. The bond-level upper bound is 0.08 (Appendix D.1).
- Typical large shocks are about 1% of outstanding (Section 3.2).

---

## Use for Credit and Macro Questions

- **Credit spreads.** Gives a measured on-impact price response to demand shifts at five levels of aggregation, and a reversal within about a quarter at the baseline level. All in price terms.
- **AA to BBB spread ratio.** The paper supports one qualitative claim: rating buckets are weak substitutes for each other (M̃ about 0 at the coarse rating level), so demand pressure on one bucket can move it against another. It also shows investment-grade multipliers are near zero at the fine portfolio level. It does **not** give an AA or BBB multiplier, a spread conversion, or persistence at the bucket level.
- **How much new bond supply is priced.** The paper does **not** answer this. Its shocks come from mutual fund flows, PIMCO outflows and index rebalancing. It holds supply constant. Treating new issuance as a negative demand shock of the same size is the reader's assumption, not the authors'. The only primary-market number is a citation: Siani (2022), 0.29 to 0.53 (Section 1.1).
- **Debt-financed investment booms.** Nothing direct. Usable only as a bound on short-run absorption of a bucket-specific flow, under the caveat above.
- **Inflation and Fed regimes.** Nothing on inflation. On QE the authors say "which bonds the central bank buys matters less than what kind of bonds it buys" and leave the numbers to future work (Sections 2.2, 4.2).
- **Issuer screening.** Little. Issuer-level multipliers exceed bond-level ones (Table F.1). Excluding financial issuers raises the bond-level estimate to about 0.15 (Table E.1).

## Method or Case

- **METHOD**: sec01 (definitions, literature), sec02 (demand framework), sec03 (shock construction, identification), sec04 (estimates), sec05 (arbitrage risk), sec06 (conclusion, limits), sec07 (proofs, robustness), sec09 (online appendix).
- **CASE**: none in full. sec08 is METHOD, and it contains one past episode: Bill Gross's exit from PIMCO in September 2014 and the outflows that followed (Appendix H.1). File that subsection as CASE material.

## Trust Notes

- **Extraction.** Technical mode (Docling) ran and read all 108 pages. Its tables match the PDF, but it dropped some standard errors (the Shock rows of Tables 5 and 6) and left 84 display equations as "formula-not-decoded" placeholders. Every equation in this skill was rebuilt from a second, layout-preserving text pass of the same PDF (`pdftotext -layout`), in which subscripts and fractions are split across lines. **Formulas may be damaged.** The numbers in the tables were checked in both passes.
- **Figures.** Figures 1, 2, 5, A.1, C.1, H.1, IA.A.1, IA.B.1 and IA.B.2 are images and were not read. Figure 1 repeats Table 5 and Figure 2 repeats Table 6. Figures 3 and 4 were read by eye from the PDF and are marked approximate in sec05. Per-rating multipliers (Figure 4a) and maturity multipliers (Figure 5a) exist only as plots.
- **The paper disagrees with itself in places.** The homogeneous bond-level multiplier is "around 0.34" in Section 1 and 0.41 in Table 1 and Section 4.1. The corrected bond-level value appears as 0.06, "around 0.05" and 0.04. Reversion is "after a quarter", "around two quarters" and "after six months" in different sentences. Table 6 is the firm source: 0.27 at T, 0.04 at T+1.
- **Table oddities.** Tables IA.B.1 and IA.B.2 (bonds under one year excluded) print the same coefficients and sample sizes as Tables 1 and 2. Table D.5 prints five data columns under six headers. Table 8 reports t statistics, the other tables report standard errors.
- **Formulas.** Check eq. 8, 12, 13 and Appendix B against the PDF before relying on a subscript.
- **Status.** A discussion paper, not a refereed article. An earlier version is on SSRN (abstract 4292266). Only the June 2026 FMG version was read.

---

## Section Index

| # | Title | Key Frameworks |
|---|-------|----------------|
| [sec01](chapters/sec01-introduction.md) | Introduction and Literature Review | Multiplier, substitute passthrough, aggregation rule, two bias channels, prior estimates |
| [sec02](chapters/sec02-demand-framework.md) | Demand Framework | General demand system, homogeneous and two-layer substitution, eq. 12 aggregation, shock propagation |
| [sec03](chapters/sec03-empirical-strategy.md) | Empirical Strategy | Three-step flow shock, IV and FE specifications, Assumptions 1 and 1', pooled exposure design |
| [sec04](chapters/sec04-estimation-results.md) | Estimation Results | Tables 1 to 6, five aggregation levels, micro-to-macro spectrum, dynamics |
| [sec05](chapters/sec05-arbitrage-risk.md) | Arbitrage Risk | Convergence-trade Sharpe ratio, ArbRisk, IG and HY, maturity heterogeneity |
| [sec06](chapters/sec06-conclusion.md) | Conclusion | Collected list of stated limits |
| [sec07](chapters/sec07-appendices-identification-robustness.md) | Appendices A to G and I | Identification proofs, Appendix B derivation, passthrough bound, robustness tables, nested logit link |
| [sec08](chapters/sec08-appendix-h-alternative-identification.md) | Appendix H: Alternative Identifications | PIMCO event design, index rebalancing back-of-envelope |
| [sec09](chapters/sec09-online-appendix.md) | Online Appendix IA.A to IA.E | Flow factor model, large shocks, multiple substitutes, stocks, two-asset CARA model |

## Topic Index

- **Aggregation rule / portfolio multiplier** → sec01, sec02, sec04, sec07
- **Arbitrage risk / Sharpe ratio** → sec05, sec09
- **Assumption 1 and 1' (share exogeneity)** → sec03, sec07
- **Bartik / shift-share / pooled exposure design** → sec03, sec07
- **Central bank purchases (QE)** → sec02, sec04
- **Close substitutes, definition and alternatives** → sec02, sec04, sec09
- **Crisis periods** → sec03, sec04, sec06
- **Dynamics / persistence / reversal** → sec04
- **Elasticity, implied** → sec01, sec04
- **Equity market comparison** → sec09
- **Financial issuers excluded** → sec07
- **Flow-induced trading (FIT) / shock construction** → sec03, sec07, sec09
- **Homogeneous versus heterogeneous substitution** → sec02, sec04
- **Index rebalancing** → sec08
- **Investment grade versus high yield** → sec05
- **Issuer-level multiplier** → sec04, sec07
- **Limits stated by the authors** → sec06
- **Literature estimates (Bretscher, Darmouni, Siani, Fang)** → sec01
- **Maturity heterogeneity** → sec05
- **Micro versus macro multiplier** → sec04
- **Nested logit** → sec07
- **Omitted variable bias** → sec02
- **Passthrough from flows to demand (bound)** → sec03, sec07
- **PIMCO / Bill Gross (2014)** → sec08
- **Shock propagation (eq. 13)** → sec02
- **Substitute passthrough (M̃)** → sec01, sec02, sec04
- **Supply elasticity / constant supply** → sec02, sec06

## Supporting Files

- [glossary.md](glossary.md) — all key terms with definitions
- [patterns.md](patterns.md) — all techniques and design patterns
- [cheatsheet.md](cheatsheet.md) — quick reference tables and decision guides
- Source PDF: `/home/ak/Documents/PapersForThemes/chaudhary-corporate-bond-multipliers/DP955.pdf`
- Full text: `/home/ak/.local/share/book-to-skill/fulltext/chaudhary-corporate-bond-multipliers/full_text.txt` — grep it for depth the section files omit (local extraction, not shipped). Tables are clean. Equations are missing.
- Layout text: `/home/ak/.local/share/book-to-skill/fulltext/chaudhary-corporate-bond-multipliers/layout_text_pdftotext.txt` — use it for equations and for standard errors the first file dropped.

---

## Scope & Limits

This skill covers the paper content only. For topics beyond this paper, check related skills
or ask the agent directly.

It reports the authors' estimates and rules as theirs. It contains no trade recommendation.
