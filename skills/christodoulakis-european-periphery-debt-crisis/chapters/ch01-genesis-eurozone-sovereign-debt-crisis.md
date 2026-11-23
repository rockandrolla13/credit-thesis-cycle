# Chapter 1: The Genesis of the Eurozone Sovereign Debt Crisis

**Contributor**: Philippe d'Arvisenet (adviser to BNP Paribas). Part I. Written mid-2014 ("at the time of writing in mid-2014").

## Core Idea
Excess private and public debt alone did not cause the crisis. The eurozone lacked the mechanisms of a true monetary union (fiscal federalism, lender of last resort for sovereigns), so high debt plus a rise in risk aversion produced "sudden stops". Member states behaved as if they had issued debt in a foreign currency. The fix d'Arvisenet proposes is debt mutualization plus a small counter-cyclical central budget.

## Frameworks Introduced

- **Imbalance build-up chain (sect. 2.1)**: ECB inherits Bundesbank reputation -> low nominal and real rates everywhere -> real rates far below growth in the south, restrictive conditions in Germany -> borrowing binge, mostly private -> misallocation to residential construction (Spain, Ireland) or current government spending (Greece) -> growth above potential, inflation and unit labour cost divergence -> exports slow, imports soar -> external deficits widen -> financed for as long as investors lend -> sudden stop.
  - When to use: diagnosing whether a currency-union member is accumulating a sudden-stop exposure.
  - Tells: nominal growth far above interest rates; construction employment share at twice its long-run average (Spain, Ireland); a boom-inflated tax base that makes the fiscal position look sound (Ireland, Spain); very low sovereign spreads.
  - Empirical link stated: countries with low real rates showed large current account deficits; when the crisis erupted, countries with large current account deficits got high spreads.

- **Debt dynamics and "fiscal effort"** (recovered from PDF pp. 39-40; the extraction lost the equation):
  - `d_t = d_(t-1) (1 + r - g) + sp_t`, with d the debt ratio, r the real interest rate, g real growth, sp the primary balance (sign as printed).
  - Debt-stabilizing condition: `d_t - d_(t-1) = 0  =>  sp = d_(t-1) (r - g)`.
  - "Fiscal effort" (FE) = actual fiscal balance minus the balance required to hold the debt ratio at its previous-year level.

- **Sovereign spread model (sect. 2.2)**. Panel of ten EMU members, ten-year spread over the Bund, data to 2010 Q4 (stopped there to exclude "conversion risk", meaning euro-exit or break-up risk, and the bank-sovereign loop). Annual data interpolated to smoothed quarterly. GLS for cross-country heteroscedasticity and contemporaneous error covariance. US corporate bond spread used as the risk factor to avoid endogeneity.
  - Preferred equation (recovered from PDF p. 40; t-statistics in brackets):
    `S_it = -0.78 + 0.02 R_t x DS_it^2 - 0.09 FE - 0.09 Y_it - 0.102 L_it + 0.25 R_t + 0.15 DS_it`
    `        (5.9)   (1.74)             (-6.91)   (-3.55)    (-8.99)     (6.40)     (3.43)`   R2 = 0.67
  - S = spread; R = general risk factor (US corporate spread); DS = debt service ratio; FE = fiscal effort; Y = growth; L = liquidity (the country's central government debt as a share of eurozone treasury debt).
  - Author's reading: +1 point of debt service ratio widens the spread 15 bp; fiscal effort of 1% of GDP cuts it 10 bp; +1 point of growth cuts it 10 bp; +1% liquidity cuts it 2 bp; general risk aversion adds (by "20 basis points"); the R x DS^2 term means high-debt-service countries pay more in stress.
  - Debt/GDP and debt service are collinear and cannot both enter. A Greece dummy, or debt/GDP in place of debt service, did not improve the fit.
  - Result: the model tracks spreads from early 2008 to mid-2010. Residuals then explode: about 750 bp for Greece in 2010 Q4, 300 Portugal, 180 Spain, 140 Italy. The author attributes the gap to a confidence collapse and bank-sovereign interaction.

- **OCA criteria checklist (sect. 3.1)**: (1) strong trade integration (met); (2) little exposure to asymmetric shocks; (3) labour-market flexibility (real devaluation replaces nominal); (4) geographic labour mobility; (5) fiscal federalism as an automatic stabilizer. D'Arvisenet states criteria 2-5 were not respected.

- **Mundell test via supply-shock correlation (sect. 3.2)**: Bayoumi-Eichengreen (1994) on Blanchard-Quah (1989): supply shocks are persistent, demand shocks transitory. De Lucia (2011) finds only the six EU founders plus Austria pass (high positive supply-shock correlation). Greek and Irish supply shocks are largely independent of the rest.

- **"No crisis, no reform" (sect. 3.3)**: OECD evidence (Duval and Elmeskov 2006) that aggressive reform (a two-standard-deviation change in the OECD regulatory strictness indicator) happens only in crises (negative output gap of at least four points). Reform costs are concentrated and visible, benefits diffuse and late. Product-market and labour-market reforms are complements.

- **"Expansionary budget adjustments: a feeble concept"** (boxed insert, recovered from PDF p. 56; it continues on p. 57, which the extraction holds):
  - The earlier claim: Alesina and Perotti (1995) defined a successful consolidation as cutting the debt ratio by at least 5 points of GDP within three years, and found that "good" consolidations rested on containing current spending (public employment and wages, transfers, subsidies), not on raising taxes. Alesina and Ardagna (2009) confirmed this for OECD countries, 1970-2007.
  - The objection (IMF 2010; Perotti 2011): measuring consolidation by the change in the cyclically adjusted primary balance is biased. It picks up tightening done to cool overheating and balances moved by asset prices, so it understates the damage.
  - The corrected evidence (Guajardo et al. 2011, measures designed to repair public finances): a 1-point consolidation in GDP typically cuts activity by 0.5 points. The fall would be sharper without the usual policy-rate cut (about 0.2% at two years) and real exchange-rate fall (1.6%), which add 0.5 points through foreign trade.
  - By exchange-rate regime: the loss is 0.84 points under a fixed rate and 0.33 points under a flexible rate.
  - By content: spending-based measures cost 0.43 points of GDP and tax-based measures 1.29 points. Spending cuts signal commitment and draw a more accommodating central bank. Indirect tax rises create a price shock and the central bank waits or tightens.
  - When monetary policy cannot respond (the continuation on p. 57): a 1-point spending-based consolidation cuts final demand by 0.9 points in the first case and 1.9 points in the second.
  - Why it matters here: euro members have a fixed rate and no national rate cut, so they sit at the costly end of each comparison.

- **Mutualization plus central budget (sect. 5)**: common issuance of bonds/bills (moral hazard contained by the revised stability pact and fiscal compact) AND a minimal central budget of "a few points of GDP" (MacDougall report) with cyclically sensitive revenue and spending such as unemployment benefits.

## Key Concepts
- **Sudden stop**: investors' appetite to finance external and public deficits disappears.
- **Conversion risk**: spread component from fear of euro exit or break-up, beyond liquidity and default risk.
- **Endogenous currency area theory**: OCA features would emerge after adoption (Frankel and Rose 1998). Cycles did converge to 2007 while labour costs and debt diverged.
- **Real devaluation / internal devaluation**: wage and price adjustment substituting for the exchange rate.
- **Consolidation fatigue**: backlash after the effort to meet Maastricht criteria.
- **EB vs TB consolidation**: expenditure-based versus tax-based fiscal adjustment (Alesina et al.).
- **Vertical vs horizontal redistribution**: US federal-to-state transfers versus German transfers across Lander.

## Mental Models
- Treat a euro member as a foreign-currency borrower: the euro removed exchange-rate speculation but not speculation in debt.
- Structural external imbalances inside a union are partly the result of comparative-advantage specialization (tradables north, non-tradables south), not only policy error. Demanding zero external balance for every member denies the point of the union.
- A sovereign-yield bubble differs from an equity bubble: it changes fundamentals (activity, revenue), so a liquidity crunch can become a solvency crisis (note 1).
- For non-euro OECD countries the same approach finds no significant effect of debt ratios on spreads (note 1).

## Anti-patterns
- **Reading spreads as pure fundamentals**: markets ignored fundamentals before 2008 and overshot after. Spread deviations from the fundamental model are serially correlated, "characteristic of bubbles".
- **Stability and Growth Pact as a substitute for fiscal federalism**: unanimity-based sanctions lacked credibility. It ignored private debt. A 3% deficit allowed in good times guarantees a breach in bad times. Spain had a 2.4% surplus and 47% debt, so the pact gave no signal.
- **Asymmetric adjustment**: deficit countries must adjust, surplus countries not.
- **Simultaneous reform plus austerity**: supply-side reform works only through exports, which stall when every country does it at once. Wage and price moderation worsens debt consolidation.

## Reference Tables

Table 1.2, size and speed of adjustment after a supply shock (source: C. de Lucia, BNP Paribas). Values as printed.

| Country | Size | Share adjusted after 2 years |
|---|---|---|
| AT | 0.013 | 99 |
| BE | 0.0150 | 102 |
| DE | 0.1160 | 101 |
| ES | 0.1771 | 104 |
| FI | 0.0257 | 0.98 |
| FR | 0.0089 | 114 |
| GR | 0.1669 | 0.18 |
| IE | 0.0588 | 0.64 |
| IT | 0.0108 | 104 |
| NL | 0.0125 | 104 |
| PT | 0.0165 | 101 |

The text reads Greece as 18% and Ireland as 64% after two years.

Table 1.1 (supply-disturbance correlations), selected cells: DE-IT 0.797, DE-FR 0.556, DE-AT 0.643, DE-ES -0.436, DE-FI -0.760, DE-GR 0.234, DE-IE -0.332, ES-FI 0.553, GR-NL -0.469.

North-South divergence numbers (sect. 3.4):

| Indicator | North | South |
|---|---|---|
| Government spending / GDP, 1999 -> 2007 | ~48% -> 45% | ~48% -> barely moved |
| Government employment, 10-year change | -2.5% | +10.5% |
| Current account, 10 years after launch | +6.5% of GDP | -4% of GDP |
| Net foreign assets | 13% -> 45% of GDP | -5% -> -32% |
| Productivity gains over 10 years | 12% | 5% |

Nominal growth minus interest rate, 2002-2007 average (T-bills / ten-year): Spain 4.8 / 4.0; Greece 4.9 / 3.3; Ireland 5.3 / 4.8; Germany -0.2 / -1.6. Private debt: Spain 100% -> 235% of GDP; Ireland 70% -> 200%; Portugal 75% -> 150%; Greece 35% -> 100%.

Export price elasticities (Artus): Spain 1.04, Italy 0.67, Portugal 0.5, Greece 0, Germany 0.19.

US fiscal federalism (Appendix): federal government collected 54% of tax revenue in 2008. Vertical transfers cover nearly 70% of ex-ante regional deficits (states' average deficit cut from 4.5% to 0.7% of GDP in 2008). Sala-i-Martin and Sachs: a US$1 regional income shock cuts taxes by 33-37 cents and raises transfers by 1-8 cents, so the centre absorbs 35-38 cents. EU members contribute 0.8-0.9% of GDP to the EU budget and receive 0.5-3.5%. State fiscal policy is pro-cyclical (correlation of net lending with output gap -0.38 for states, +0.36 federal).

Fiscal behaviour (Fatas and Mihov 2012): change in cyclically adjusted balance on output gap: -0.25 eurozone (pro-cyclical) versus +0.93 USA. Automatic stabilizers: 0.46 eurozone versus 0.29 USA.

## Worked Example
Adjustment under way by 2014 (sect. 4), read as a painful real devaluation:
1. Fiscal: Greece's cyclically adjusted primary balance moved from -9.9% (2009) to +1.8% (2012); Spain -7.4% to 0%; Portugal -8.9% to +1.1%; Italy +1.2% to +4.3%.
2. External: Greece's current account deficit fell from 18% of GDP (2008) to 2.4% (2014); Spain 9.6 to 2.8; Portugal 12.6 to 0.
3. Unit labour costs 2011-2013, annual average: Greece -4.6%, Spain -1.9%, Portugal -0.7%, Italy +1.6%, against +2.4%, +3.8%, +2%, +2.5% in 2002-2008.
4. Frictions: export prices kept rising in 2011-2012 (weak pass-through). Greek exports did not rebound, given a manufacturing share of 7.5% of GDP and a zero export price elasticity. Periphery manufacturing capacity was 10-15% below its level ten years earlier at mid-2012.

## Key Takeaways
1. Screen for sudden-stop risk with real rate minus growth, private credit growth, construction share and current account, not the fiscal balance.
2. Model spreads on debt service, fiscal effort, growth, liquidity and global risk aversion, then treat a persistent positive residual as non-fundamental stress.
3. Supply-shock correlation and speed of adjustment identify which members fit a single monetary policy. Greece and Ireland did not.
4. Reform arrives in crises, at the worst moment for demand.
5. Expenditure-based consolidations are reported as less contractionary than tax-based ones (Alesina et al.), but d'Arvisenet casts doubt on expansionary consolidation given the 2009-2014 record.
6. Without mutualization and a central budget, the no-bailout clause itself signals absence of solidarity and invites arbitrage across national debts.

## Connects To
- **Ch 2 (Gros, Alcidi)**: the fiscal versus competitiveness trade-off that sect. 3.3 flags.
- **Ch 6 (De Grauwe)**: the same De Grauwe-Ji evidence that spreads detached from fundamentals.
- **Ch 8 (Mathieu, Sterdyniak)** and **Ch 9 (Bernoth, Engler)**: mutualization and a transfer mechanism in detail.
- **Ch 10 (Mody)**: disagrees. Mody treats fiscal union as politically unavailable and wants contingent debt instead.

## Extraction Notes
- All 22 figures are image placeholders. Figure 1.12 has no caption in the extraction.
- The debt-dynamics identity and the spread equation were unreadable in the extraction and were recovered from PDF pp. 39-40.
- The boxed insert on fiscal multipliers was missing from the extraction apart from its last lines. Its first page was recovered from PDF p. 56. The two cases behind the 0.9 and 1.9 figures straddle the page break and were not re-read on p. 57.
- Source inconsistencies kept as printed: the liquidity coefficient is -0.102 but the text says 2 bp per 1%; the risk coefficient is 0.25 but the text says 20 bp; Table 1.2 mixes percent and fraction units; "3% in Greece" for low-skilled share looks like a misprint; "the EMS has finally been adopted" appears to mean the ESM; the Greek deficit is given as 1.6% for both 2014 and 2015.
