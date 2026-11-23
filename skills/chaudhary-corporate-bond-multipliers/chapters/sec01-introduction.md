# Section 1: Introduction and Literature Review (1, 1.1)

## Core Idea
The paper asks how well the corporate bond market absorbs demand-driven price pressure. Its answer depends on what you call "an asset". A single bond has many close substitutes, so its own price barely moves. A whole rating bucket has few substitutes, so its price moves a lot. Estimates that ignore this difference overstate the bond-level effect by about an order of magnitude (Section 1).

## Frameworks Introduced
- **Multiplier (M)**: "the direct price effect of the demand shock holding the prices of all other assets fixed" (footnote 1). It is "approximately the inverse of the own price elasticity of demand". Unit: percent change in price per 1 percent demand shock. The demand shock is measured as a share of the bond's amount outstanding (Section 3.2, Figure A.1).
  - When to use: any question of the form "a buyer or seller moves X percent of this asset, how far does the price go on impact".
- **Substitute passthrough (M̃)**: "the percentage increase in an asset's price due to its close substitutes' prices rising by 1%" (Section 1).
  - When to use: to judge how far a shock in one bond spreads to its neighbours.
- **Aggregation rule**: "the more aggregated the demand shock, the higher the multiplier and the lower the substitute passthrough" (Section 1, Figure 1).
- **Two bias channels** when close substitutes are not controlled (Section 1):
  1. General equilibrium. A shock to one bond lifts the prices of its close substitutes.
  2. Correlated shocks. Flow and mandate shocks hit similar bonds together.
  Both make the measured own effect too large.

## Key Concepts
- **Detailed rating category**: AAA, AA+, AA, AA- and so on (footnote 4).
- **Coarse rating category**: AAA, AA, A, BBB and so on (footnote 4).
- **Close substitutes**: in the baseline, all other bonds in the same detailed rating category (Section 1).
- **Reduced-form estimate**: a regression of returns on demand shocks without a substitution structure. The authors say such estimates are "not readily generalizable because they depend on the types of shocks used in the study" (Section 1).
- **Micro versus macro multiplier**: introduced here, defined in Section 4.2.

## Mental Models
- Substitutability is "double-edged". High substitutability lowers the direct price effect of a shock. It raises the spillover to substitutes (Section 1).
- A regression with detailed characteristic-by-time fixed effects estimates the security-level multiplier. A regression without them estimates an average between portfolio-level and security-level multipliers (Section 1). The two are different parameters.

## Anti-patterns
- **Reading a no-fixed-effects estimate as a bond-level multiplier.** It mixes direct and spillover effects (Section 1).
- **Assuming homogeneous substitution in a structural model of bonds.** The authors call this contrary to "real-world patterns" and a source of bias (Section 1).

## Reference Tables

Headline numbers as the introduction states them (Section 1). See the Trust Notes in SKILL.md: the introduction and Section 4 do not agree on every figure.

| Level | Multiplier | Substitute passthrough | Source in paper |
|---|---|---|---|
| Single bond, homogeneous substitution | "around 0.34" in Section 1. Table 1 reports 0.41 | not estimated | Section 1, Table 1 |
| Single bond, heterogeneous substitution | 0.06, insignificant | about 1 | Section 1 |
| Single bond, upper bound for imperfect passthrough | at most 0.08 | n/a | footnote 3, Appendix D.1 |
| Detailed rating x quarter to maturity | 0.3 | slightly below the bond level | Section 1 |
| Coarse rating group | 3.94 | "effectively" 0 | Section 1 |

Implied market demand elasticity at the bond level, "assuming inelastic supply": 16.6 (footnote 2).

Prior estimates the authors cite (Section 1.1). These are other papers' numbers, reported by the authors.

| Paper | Setting | Multiplier |
|---|---|---|
| Bretscher et al. (2022) | corporate bonds, demand system | about 0.26 |
| Darmouni et al. (2023) | two-layer framework with fund flows | 0.5 to 1.25 by period |
| Siani (2022) | primary market | 0.29 to 0.53 |
| Fang (2022) | nested logit, IG and HY nests | about 0.1 |
| Jansen (2021) | European government bonds, maturity buckets | about 0.24 (footnote 5) |
| Gabaix and Koijen (2021) | whole equity market | about 5 |
| Li (2021) | stock portfolios, reversion | four quarters |

The authors place their own bond-level number at "around 0.05" in this subsection.

## Worked Example
**Scenario** (Section 1): Apple's 10-year bond and Google's 10-year bond are both AA+. Bed Bath & Beyond bonds are in default.
**Application**: the Apple bond is a good substitute for the Google bond and a poor substitute for the defaulted bond. A shock to the Apple bond is absorbed by investors moving to other AA+ bonds.
**Outcome**: little own price effect on the Apple bond. Strong spillover inside AA+. Weak spillover to distant ratings.

## Key Takeaways
1. A multiplier holds substitute prices fixed. A raw regression coefficient does not.
2. The bond-level multiplier falls from roughly 0.3 to 0.4 to about 0.06 once close substitutes are controlled.
3. Portfolio multipliers are larger and rise with aggregation, up to 3.94 for coarse rating groups.
4. The price effect reverts. The introduction gives "after a quarter" and "around two quarters" in different sentences.
5. Multipliers are larger for high-yield bonds, longer maturities and higher arbitrage risk.

## Connects To
- **sec02**: the demand system behind M and M̃.
- **sec03**: how the demand shock is built from fund flows.
- **sec04**: the tables behind every number above.
