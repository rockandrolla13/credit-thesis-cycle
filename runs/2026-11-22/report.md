# Credit scenario grid, as of 2026-11-22

Horizon: 2027-05-22 (6 months). Moves are spread changes in basis points.

**These are proposed scenarios, not engine output.** Probabilities are judgement unless marked `evidence_weighted`. This grid stops before trades.

## Findings

1. The market already prices AI supply in the top ratings. AA spreads rose from 0.47 to 0.58 of BBB spreads in a year, and the A-minus-AA gap fell from 18bp to 10bp. That ratio is the axis for the supply question. It rises to about 0.64 if supply grinds on and falls to about 0.46 if capex is cut.
2. A capex cut splits credit in two. It helps the bonds of the large AI spenders, because they borrow less. It hurts everyone who lent against the build-out: HY technology, HY power producers, HY real estate and non-bank lenders.
3. Today's spreads are fair only if calm is about twice as likely as judged here. IG at 94bp needs a 58% weight on 'Supply absorbed', against 28% here.
4. Most of the expected widening comes from two tail scenarios. Hard landing and funding accident carry 17% of the probability and about three quarters of the expected IG move. The two most likely scenarios move IG by -12bp to +14bp.
5. IG income covers only 7bp of widening over six months. Four of the five scenarios exceed that. HY income covers 57bp before default losses.
6. This agrees with the two Willer and Saunders rules checked on 22 Nov 2026. The volatility rule and the lending-standards rule both say not to hold credit spread risk.

## Limits

1. Every probability and spread move is judgement. The script checks coherence, not correctness.
2. Free data has no sector spread levels. Sector rows are changes from today, and the weights are rough index shares.
3. Spread durations of 6.6 years for IG and 3.1 years for HY are assumptions, not index data.
4. Carry cover ignores default losses. For HY the true cushion is smaller.
5. The fair-value weights assume today's spread equals the expected future spread. That ignores the risk premium.
6. Several news facts rest on one source each. Examples are the construction-loan force majeure and the 20bp tech premium.

## Spine: the shared macro scenarios

Apply the tests in order. The first test that is true names the scenario.

| Id | Scenario | Probability | Source | Test | Observable and threshold |
|---|---|---|---|---|---|
| S1 | Supply absorbed | 28% | PM_assumption | Otherwise. Capex holds, growth holds, and the Fed stops at 4.25% or lower. | FRED DFEDTARU: 4.25 or lower on 2027-05-22, and no earlier test is true |
| S2 | Higher rates, supply grind | 37% | evidence_weighted | Fourth. The Fed funds upper bound is 4.50% or higher on the horizon date. | FRED DFEDTARU: 4.50 or higher on 2027-05-22 / AA to BBB spread ratio (FRED BAMLC0A2CAA / BAMLC0A4CBBB): above 0.62 |
| S3 | AI digestion | 18% | PM_assumption | Third. The five largest AI spenders guide combined 2027 capex to $900bn or less, or two of the five cut guidance. | Fourth-quarter earnings guidance, late January to early February 2027: combined 2027 capex of $900bn or less, against a consensus above $1,000bn |
| S4 | Hard landing | 10% | PM_assumption | Second. The manufacturing ISM prints under 50 for two months in a row, or the Sahm rule reaches 0.50. | ISM manufacturing PMI: under 50 for two consecutive months / Sahm rule (FRED SAHMREALTIME): 0.50 or higher |
| S5 | Funding accident | 7% | PM_assumption | First. A bank or insurer with over $50bn of assets fails or is rescued, or the Fed opens an emergency facility, or the IG primary market shuts for five business days. | Fed H.4.1 release: a new emergency facility appears / IG primary market calendar: five straight business days with no deals, outside holidays |

Evidence used for the probabilities:

- S1: Oil fell from $110 to $90 in a month and 10-year breakeven inflation is at a three-year low of 2.15% (FRED DCOILWTICO, T10YIE).
- S1: The October SLOOS is near neutral at 1.7% net tightening (FRED DRTSCILM).
- S2: Futures price a December hike at about 95%. The October minutes say almost all participants favour further hikes (CNBC, 18 Nov 2026).
- S2: The 2-year Treasury yields 4.76% against a 4.00% policy ceiling (FRED DGS2, DFEDTARU).
- S2: Goldman forecasts $420bn of hyperscaler IG issuance in 2027. SanCap forecasts up to $450bn.
- S3: Nvidia lost about half its market value in six weeks. Reuters reported an SEC accounting probe on 20 Nov 2026.
- S3: Tech IG borrowing costs are the highest since 2009 by one report. The 2027 funding gap is put at about $291bn (SanCap, 20 Nov 2026).
- S3: Against: strong Nvidia earnings in November show demand had not yet dropped.
- S4: Against: the October ISM is 55.5 and rising, after ten months of expansion.
- S4: For: the Fed is hiking into an equity fall of 8% on the S&P 500 and 13% on the Nasdaq.
- S5: CCC spreads are at a three-year high of 1361bp (FRED BAMLH0A3HYC). CoreWeave bonds yield about 16% (CNBC, 6 Nov 2026).
- S5: One source reports a force majeure notice on an $18bn data-centre construction loan held by about 20 banks.
- S5: Against: aggregate corporate debt fell from 50.8% to 48.2% of GDP in three years (Fed Z.1).

## Summary: spread change by scenario

| Row | Now | S1 | S2 | S3 | S4 | S5 | Expected | Chance wider | Wide/tight ratio |
|---|---|---|---|---|---|---|---|---|---|
| IG | 94 | -12 | +14 | +18 | +56 | +116 | +19 | 72% | 6.6 |
| HY | 352 | -52 | +18 | +108 | +248 | +498 | +71 | 72% | 5.9 |
| IG.AA | 68 | -8 | +16 | -2 | +30 | +75 | +12 | 54% | 5.5 |
| IG.A | 78 | -10 | +12 | +12 | +45 | +100 | +15 | 72% | 6.5 |
| IG.BBB | 117 | -15 | +14 | +26 | +75 | +145 | +23 | 72% | 6.5 |
| HY.BB | 210 | -30 | +18 | +55 | +150 | +310 | +45 | 72% | 6.3 |
| HY.B | 380 | -55 | +20 | +110 | +270 | +540 | +77 | 72% | 6.0 |
| HY.CCC | 1361 | -150 | +30 | +340 | +620 | +1200 | +176 | 72% | 5.2 |
| IG.Banking | n/a | -14 | +8 | +22 | +60 | +150 | +20 | 72% | 6.0 |
| IG.Insurance and other financials | n/a | -14 | +12 | +30 | +70 | +170 | +25 | 72% | 7.4 |
| IG.REITs | n/a | -14 | +18 | +30 | +70 | +150 | +26 | 72% | 7.5 |
| IG.Technology | n/a | -14 | +28 | +14 | +50 | +125 | +23 | 61% | 6.0 |
| IG.Communications | n/a | -13 | +20 | +16 | +60 | +115 | +21 | 72% | 6.7 |
| IG.Consumer cyclical | n/a | -14 | +18 | +20 | +85 | +135 | +24 | 72% | 7.2 |
| IG.Consumer non-cyclical | n/a | -10 | +10 | +8 | +35 | +75 | +11 | 72% | 5.0 |
| IG.Energy | n/a | -14 | +8 | +20 | +85 | +140 | +21 | 72% | 6.3 |
| IG.Industrials | n/a | -13 | +10 | +24 | +75 | +115 | +20 | 72% | 6.5 |
| IG.Utilities | n/a | -11 | +20 | +10 | +40 | +85 | +16 | 72% | 6.2 |
| HY.Energy | n/a | -45 | +5 | +70 | +300 | +560 | +71 | 72% | 6.6 |
| HY.Communications | n/a | -70 | +30 | +110 | +270 | +510 | +74 | 72% | 4.8 |
| HY.Technology | n/a | -110 | +50 | +292 | +360 | +850 | +136 | 72% | 5.4 |
| HY.Healthcare | n/a | -50 | +30 | +60 | +170 | +400 | +53 | 72% | 4.8 |
| HY.Consumer cyclical | n/a | -60 | +22 | +85 | +290 | +500 | +71 | 72% | 5.2 |
| HY.Consumer non-cyclical and services | n/a | -45 | +15 | +65 | +180 | +410 | +51 | 72% | 5.1 |
| HY.Basic industry and capital goods | n/a | -55 | +15 | +105 | +280 | +490 | +71 | 72% | 5.6 |
| HY.Financial services | n/a | -60 | +25 | +130 | +270 | +680 | +90 | 72% | 6.4 |
| HY.Real estate and homebuilders | n/a | -55 | +40 | +150 | +270 | +580 | +94 | 72% | 7.1 |
| HY.Utilities and power | n/a | -45 | +10 | +170 | +200 | +430 | +72 | 72% | 6.7 |

## Relations between rows

| Relation | Now | S1 | S2 | S3 | S4 | S5 | Expected |
|---|---|---|---|---|---|---|---|
| HY minus IG (bp) | 258 | 218 | 262 | 348 | 450 | 640 | 310 |
| HY to IG ratio | 3.74 | 3.66 | 3.43 | 4.11 | 4.00 | 4.05 | 3.71 |
| BB minus BBB (bp) | 93 | 78 | 97 | 122 | 168 | 258 | 115 |
| CCC minus BB (bp) | 1151 | 1031 | 1163 | 1436 | 1621 | 2041 | 1282 |
| A minus AA (bp) | 10 | 8 | 6 | 24 | 25 | 35 | 14 |
| AA to BBB ratio (price of AI supply) | 0.58 | 0.59 | 0.64 | 0.46 | 0.51 | 0.55 | 0.57 |

## Each row in detail

### IG

Axis: ICE BofA US Corporate OAS (FRED BAMLC0A0CM). Driver: Hyperscaler supply, the Fed path, growth.

| Scenario | Drawn from | Probability | Change | Level | Why | Own observable |
|---|---|---|---|---|---|---|
| Supply absorbed | S1 | 28% | -12 | 82 | Rate volatility falls. Yield buyers take the January supply without extra concession. | spine test |
| Higher rates, supply grind | S2 | 37% | +14 | 108 | The Fed keeps hiking. Hyperscaler issuance runs above the 2026 pace. Widening starts in the top ratings. | spine test |
| AI digestion | S3 | 18% | +18 | 112 | Less hyperscaler supply helps the top tier. BBB names and lenders to the build-out widen. | spine test |
| Hard landing | S4 | 10% | +56 | 150 | Earnings and ratings fall. Cyclical sectors lead. | spine test |
| Funding accident | S5 | 7% | +116 | 210 | Forced liquidation. Financials lead. | spine test |

Expected change +19bp. Chance of wider spreads 72%. Carry covers 7bp of widening over the horizon.
Weights that make today's spread fair, given these outcomes: Supply absorbed 58% (mine 28%), Higher rates, supply grind 28% (mine 37%), AI digestion 12% (mine 18%), Hard landing 1% (mine 10%), Funding accident 0% (mine 7%).

### HY

Axis: ICE BofA US High Yield OAS (FRED BAMLH0A0HYM2). Driver: Default expectations, refinancing access, equity volatility.

| Scenario | Drawn from | Probability | Change | Level | Why | Own observable |
|---|---|---|---|---|---|---|
| Supply absorbed | S1 | 28% | -52 | 300 | Equity volatility fades. Stress stays inside a few CCC names. | spine test |
| Higher rates, supply grind | S2 | 37% | +18 | 370 | Coupons reset higher. Income absorbs most of it. BB feels the rate move. | spine test |
| AI digestion | S3 | 18% | +108 | 460 | GPU-cloud and data-centre borrowers reprice. It spreads to suppliers and power producers. | spine test |
| Hard landing | S4 | 10% | +248 | 600 | Default expectations rise across cyclical sectors. | spine test |
| Funding accident | S5 | 7% | +498 | 850 | The primary market closes. CCC borrowers cannot refinance. | spine test |

Expected change +71bp. Chance of wider spreads 72%. Carry covers 57bp of widening over the horizon.
Weights that make today's spread fair, given these outcomes: Supply absorbed 48% (mine 28%), Higher rates, supply grind 39% (mine 37%), AI digestion 10% (mine 18%), Hard landing 2% (mine 10%), Funding accident 0% (mine 7%).

### IG.AA

Axis: ICE BofA AA US Corporate OAS (FRED BAMLC0A2CAA). Driver: Hyperscaler supply. Most large AI issuers are rated AA or AAA.

| Scenario | Drawn from | Probability | Change | Level | Why | Own observable |
|---|---|---|---|---|---|---|
| Supply absorbed | S1 | 28% | -8 | 60 | Concessions on hyperscaler bonds shrink a little. | spine test |
| Higher rates, supply grind | S2 | 37% | +16 | 84 | The supply lands here. | spine test |
| AI digestion | S3 | 18% | -2 | 66 | Less supply offsets weaker sentiment. | spine test |
| Hard landing | S4 | 10% | +30 | 98 | High quality widens least. | spine test |
| Funding accident | S5 | 7% | +75 | 143 | High quality widens least, but supply overhang remains. | spine test |

Expected change +12bp. Chance of wider spreads 54%.

### IG.A

Axis: ICE BofA Single-A US Corporate OAS (FRED BAMLC0A3CA). Driver: Banks dominate this tier.

| Scenario | Drawn from | Probability | Change | Level | Why | Own observable |
|---|---|---|---|---|---|---|
| Supply absorbed | S1 | 28% | -10 | 68 | Moves with the index. | spine test |
| Higher rates, supply grind | S2 | 37% | +12 | 90 | Banks gain from higher rates and issue less than tech. | spine test |
| AI digestion | S3 | 18% | +12 | 90 | Questions on bank lending to the build-out. | spine test |
| Hard landing | S4 | 10% | +45 | 123 | Loan losses rise. | spine test |
| Funding accident | S5 | 7% | +100 | 178 | Banks sit at the centre of funding stress. | spine test |

Expected change +15bp. Chance of wider spreads 72%.

### IG.BBB

Axis: ICE BofA BBB US Corporate OAS (FRED BAMLC0A4CBBB). Driver: Downgrade risk and cyclical exposure.

| Scenario | Drawn from | Probability | Change | Level | Why | Own observable |
|---|---|---|---|---|---|---|
| Supply absorbed | S1 | 28% | -15 | 102 | Highest beta in a rally. | spine test |
| Higher rates, supply grind | S2 | 37% | +14 | 131 | Moves with the index. | spine test |
| AI digestion | S3 | 18% | +26 | 143 | Lower-rated AI borrowers and cyclicals carry the downgrade risk. | spine test |
| Hard landing | S4 | 10% | +75 | 192 | Fallen-angel fear returns. | spine test |
| Funding accident | S5 | 7% | +145 | 262 | Forced sellers of downgraded bonds. | spine test |

Expected change +23bp. Chance of wider spreads 72%.

### HY.BB

Axis: ICE BofA BB US High Yield OAS (FRED BAMLH0A1HYBB). Driver: Rates and crossover demand.

| Scenario | Drawn from | Probability | Change | Level | Why | Own observable |
|---|---|---|---|---|---|---|
| Supply absorbed | S1 | 28% | -30 | 180 | Modest rally from already tight levels. | spine test |
| Higher rates, supply grind | S2 | 37% | +18 | 228 | Longest duration in HY. Feels the rate move. | spine test |
| AI digestion | S3 | 18% | +55 | 265 | Limited direct AI exposure. | spine test |
| Hard landing | S4 | 10% | +150 | 360 | Downgrades from IG add supply. | spine test |
| Funding accident | S5 | 7% | +310 | 520 | Wide, but refinancing stays possible. | spine test |

Expected change +45bp. Chance of wider spreads 72%.

### HY.B

Axis: ICE BofA Single-B US High Yield OAS (FRED BAMLH0A2HYB). Driver: Refinancing cost and earnings.

| Scenario | Drawn from | Probability | Change | Level | Why | Own observable |
|---|---|---|---|---|---|---|
| Supply absorbed | S1 | 28% | -55 | 325 | Moves with the index. | spine test |
| Higher rates, supply grind | S2 | 37% | +20 | 400 | Higher coupons at refinancing. | spine test |
| AI digestion | S3 | 18% | +110 | 490 | Holds most of the leveraged tech and supplier names. | spine test |
| Hard landing | S4 | 10% | +270 | 650 | Earnings fall against high interest cost. | spine test |
| Funding accident | S5 | 7% | +540 | 920 | Refinancing window shuts. | spine test |

Expected change +77bp. Chance of wider spreads 72%.

### HY.CCC

Axis: ICE BofA CCC and lower US High Yield OAS (FRED BAMLH0A3HYC). Driver: A few distressed issuers. Four names carry about 30% of the spread (Vanguard, 10 Nov 2026).

| Scenario | Drawn from | Probability | Change | Level | Why | Own observable |
|---|---|---|---|---|---|---|
| Supply absorbed | S1 | 28% | -150 | 1211 | Distressed names bounce, but restructurings continue. | spine test |
| Higher rates, supply grind | S2 | 37% | +30 | 1391 | Already priced for distress. Rates add little. | spine test |
| AI digestion | S3 | 18% | +340 | 1701 | A large restructuring in AI-linked debt. | spine test |
| Hard landing | S4 | 10% | +620 | 1981 | Defaults rise broadly. | spine test |
| Funding accident | S5 | 7% | +1200 | 2561 | No refinancing at any price. | spine test |

Expected change +176bp. Chance of wider spreads 72%.

### IG.Banking

Axis: Sector OAS change against today. No free level data.. Driver: Funding markets, the curve, loan losses, lending to non-bank funds.

| Scenario | Drawn from | Probability | Change | Level | Why | Own observable |
|---|---|---|---|---|---|---|
| Calm funding | S1 | 28% | -14 | n/a | Bank supply after January earnings clears easily. | spine test |
| Haven from tech supply | S2 | 37% | +8 | n/a | Higher rates lift margins. Bank net supply is lower than tech supply. | spine test |
| AI loan-book questions | S3 | 18% | +22 | n/a | Investors ask about construction loans and lending to private-credit funds. | spine test |
| Credit-cost cycle | S4 | 10% | +60 | n/a | Loan losses rise. Banks widen a little more than the index. | spine test |
| Systemic stress | S5 | 7% | +150 | n/a | Banks sit at the centre of any funding accident. | spine test |

Expected change +20bp. Chance of wider spreads 72%.

### IG.Insurance and other financials

Axis: Sector OAS change against today. No free level data.. Driver: Private-credit holdings and lending-fund asset quality.

| Scenario | Drawn from | Probability | Change | Level | Why | Own observable |
|---|---|---|---|---|---|---|
| Calm | S1 | 28% | -14 | n/a | Higher yields help life insurers reinvest. | spine test |
| Yield tailwind | S2 | 37% | +12 | n/a | Insurers are natural buyers of the new supply. | spine test |
| Private-credit marks contained | 65% of S3 | 12% | +20 | n/a | Insurers hold AI debt, but marks move slowly. | Rated lending funds report non-accruals under 3% of assets |
| Lending-fund and insurer scrutiny | 35% of S3 | 6% | +50 | n/a | Lending funds report bad loans. Insurers disclose data-centre holdings. | Non-accruals above 3% at two large rated lending funds, or a fund limits withdrawals |
| Macro stress | S4, S5 | 17% | +111 | n/a | Asset managers and insurers carry the private-credit link in a downturn. | spine test |

Expected change +25bp. Chance of wider spreads 72%.

### IG.REITs

Axis: Sector OAS change against today. No free level data.. Driver: Treasury yields and data-centre development funding.

| Scenario | Drawn from | Probability | Change | Level | Why | Own observable |
|---|---|---|---|---|---|---|
| Rates relief | S1 | 28% | -14 | n/a | Lower rate volatility helps a rate-sensitive sector. | spine test |
| Rate drag | S2 | 37% | +18 | n/a | Data-centre REITs need funding while yields stay near 5%. | spine test |
| Leasing slowdown | S3 | 18% | +30 | n/a | Data-centre leasing slows after capex cuts. | spine test |
| Property downturn | S4 | 10% | +70 | n/a | Property values fall with growth. | spine test |
| Funding stress | S5 | 7% | +150 | n/a | Development funding stops. | spine test |

Expected change +26bp. Chance of wider spreads 72%.

### IG.Technology

Axis: Sector OAS change against today. No free level data.. Driver: Net bond supply and capex against cash flow. About 20bp wide of the index on 2 Nov 2026 by one report.

| Scenario | Drawn from | Probability | Change | Level | Why | Own observable |
|---|---|---|---|---|---|---|
| Supply absorbed | S1 | 28% | -14 | n/a | Buyers accept current concessions. The premium to the index holds. | spine test |
| Supply grind | S2 | 37% | +28 | n/a | 2027 issuance near $420bn to $450bn meets a tired buyer base. | spine test |
| Capex cut, balance sheets protected | 60% of S3 | 11% | -6 | n/a | Less borrowing. Bondholders gain what shareholders lose. | Hyperscaler bond issuance in Q1 2027 under $60bn, and no rating action |
| Capex cut with a credit event | 40% of S3 | 7% | +45 | n/a | A lower-rated AI borrower loses its IG rating, or the accounting probe widens. | A rating agency moves a large AI borrower to negative outlook at BBB-, or a second issuer discloses a probe |
| Macro stress | S4, S5 | 17% | +81 | n/a | Tech no longer acts as the safe sector, because it now carries the debt. | spine test |

Expected change +23bp. Chance of wider spreads 61%.

### IG.Communications

Axis: Sector OAS change against today. No free level data.. Driver: Leverage and demand for long bonds.

| Scenario | Drawn from | Probability | Change | Level | Why | Own observable |
|---|---|---|---|---|---|---|
| Calm | S1 | 28% | -13 | n/a | Moves with the index. | spine test |
| Long-bond competition | S2 | 37% | +20 | n/a | Long-dated BBB telecom debt competes with hyperscaler long bonds. | spine test |
| Defensive cash flows | S3 | 18% | +16 | n/a | Subscription revenue holds. | spine test |
| Leverage worry | S4 | 10% | +60 | n/a | High leverage meets weaker revenue. | spine test |
| Stress | S5 | 7% | +115 | n/a | Large capital structures widen with the index. | spine test |

Expected change +21bp. Chance of wider spreads 72%.

### IG.Consumer cyclical

Axis: Sector OAS change against today. No free level data.. Driver: Consumer spending and rates on car and home loans.

| Scenario | Drawn from | Probability | Change | Level | Why | Own observable |
|---|---|---|---|---|---|---|
| Consumer holds | S1 | 28% | -14 | n/a | Lower oil helps spending. | spine test |
| Rate squeeze | S2 | 37% | +18 | n/a | Car finance and housing feel 5% Treasury yields. | spine test |
| Wealth effect | S3 | 18% | +20 | n/a | A deeper equity fall trims high-end spending. | spine test |
| Consumer recession | S4 | 10% | +85 | n/a | Autos and retail lead. Fallen-angel risk rises. | spine test |
| Stress | S5 | 7% | +135 | n/a | Cyclical names widen more than the index. | spine test |

Expected change +24bp. Chance of wider spreads 72%.

### IG.Consumer non-cyclical

Axis: Sector OAS change against today. No free level data.. Driver: Debt-funded mergers and drug-price policy. No direct AI link.

| Scenario | Drawn from | Probability | Change | Level | Why | Own observable |
|---|---|---|---|---|---|---|
| Lags the rally | S1 | 28% | -10 | n/a | Defensive sectors gain least when risk appetite returns. | spine test |
| Defensive haven | S2, S3 | 55% | +9 | n/a | Stable cash flows. The sector does not tell these two scenarios apart. | spine test |
| Mild widening | S4 | 10% | +35 | n/a | Demand for staples and medicine holds in a downturn. | spine test |
| Stress, still defensive | S5 | 7% | +75 | n/a | Widens least of all IG sectors. | spine test |

Expected change +11bp. Chance of wider spreads 72%.

### IG.Energy

Axis: Sector OAS change against today. No free level data.. Driver: Oil and gas prices. Power demand from data centres.

| Scenario | Drawn from | Probability | Change | Level | Why | Own observable |
|---|---|---|---|---|---|---|
| Oil steady | S1 | 28% | -14 | n/a | Oil near $90 keeps cash flow strong. | spine test |
| Inflation hedge | S2 | 37% | +8 | n/a | Firm oil goes with firm inflation. Net supply is low. | spine test |
| Power-demand rethink | S3 | 18% | +20 | n/a | Gas pipeline names priced for data-centre demand give some back. | spine test |
| Oil slump | S4 | 10% | +85 | n/a | A demand fall takes oil under $65. | spine test |
| Stress | S5 | 7% | +140 | n/a | High beta to a global growth shock. | spine test |

Expected change +21bp. Chance of wider spreads 72%.

### IG.Industrials

Axis: Sector OAS change against today. No free level data.. Driver: Manufacturing surveys and capital-spending orders. Covers basic industry, capital goods and transport.

| Scenario | Drawn from | Probability | Change | Level | Why | Own observable |
|---|---|---|---|---|---|---|
| Orders hold | S1 | 28% | -13 | n/a | ISM stays above 50. | spine test |
| Steady | S2 | 37% | +10 | n/a | Strong factories offset higher rates. | spine test |
| Equipment orders cut | S3 | 18% | +24 | n/a | Makers of power and cooling equipment lose data-centre orders. | spine test |
| Cyclical downturn | S4 | 10% | +75 | n/a | Orders fall with the ISM. | spine test |
| Stress | S5 | 7% | +115 | n/a | Cyclical names widen with the index. | spine test |

Expected change +20bp. Chance of wider spreads 72%.

### IG.Utilities

Axis: Sector OAS change against today. No free level data.. Driver: Capex-funded supply, long-bond rates and load forecasts.

| Scenario | Drawn from | Probability | Change | Level | Why | Own observable |
|---|---|---|---|---|---|---|
| Calm | S1 | 28% | -11 | n/a | Heavy utility supply limits the rally. | spine test |
| Capex supply | S2 | 37% | +20 | n/a | Utilities borrow heavily for grid and generation. Long bonds feel rates. | spine test |
| Load-growth rethink | S3 | 18% | +10 | n/a | Lower load forecasts mean less borrowing. Regulated cash flow holds. | spine test |
| Defensive | S4 | 10% | +40 | n/a | Regulated revenue holds in a downturn. | spine test |
| Stress, still defensive | S5 | 7% | +85 | n/a | Widens less than the index. | spine test |

Expected change +16bp. Chance of wider spreads 72%.

### HY.Energy

Axis: Sector OAS change against today. No free level data.. Driver: Oil and gas prices.

| Scenario | Drawn from | Probability | Change | Level | Why | Own observable |
|---|---|---|---|---|---|---|
| Oil steady | S1 | 28% | -45 | n/a | Balance sheets are strong after a year of high oil. | spine test |
| Inflation hedge | S2 | 37% | +5 | n/a | Firm oil protects cash flow. | spine test |
| Low AI link | S3 | 18% | +70 | n/a | Only gas and power names are exposed. | spine test |
| Oil slump | S4 | 10% | +300 | n/a | Oil under $65 in a demand slump. | spine test |
| Stress | S5 | 7% | +560 | n/a | High beta to a growth shock. | spine test |

Expected change +71bp. Chance of wider spreads 72%.

### HY.Communications

Axis: Sector OAS change against today. No free level data.. Driver: Leverage, declining legacy revenue, debt exchanges. About a quarter of the CCC index.

| Scenario | Drawn from | Probability | Change | Level | Why | Own observable |
|---|---|---|---|---|---|---|
| Relief | S1 | 28% | -70 | n/a | Distressed capital structures bounce the most. | spine test |
| Refinancing cost | S2 | 37% | +30 | n/a | Large maturities meet higher coupons. | spine test |
| Fibre story fades | S3 | 18% | +110 | n/a | Fibre builders lose the AI traffic story. | spine test |
| Restructuring wave | S4 | 10% | +270 | n/a | More debt exchanges and defaults. | spine test |
| Stress | S5 | 7% | +510 | n/a | No market access for leveraged names. | spine test |

Expected change +74bp. Chance of wider spreads 72%.

### HY.Technology

Axis: Sector OAS change against today. No free level data.. Driver: Refinancing cost and customer contracts at GPU-cloud and software borrowers.

| Scenario | Drawn from | Probability | Change | Level | Why | Own observable |
|---|---|---|---|---|---|---|
| Funding reopens | S1 | 28% | -110 | n/a | The most beaten-down sector bounces the most. | spine test |
| Costly funding, no default | S2 | 37% | +50 | n/a | GPU-cloud borrowers refinance at 12% to 16%. Nobody defaults. | spine test |
| GPU-cloud restructuring | 60% of S3 | 11% | +380 | n/a | A large GPU-cloud borrower restructures after customers cut orders. | A GPU-cloud borrower with over $10bn of debt misses a payment or launches a debt exchange |
| Contracts honoured | 40% of S3 | 7% | +160 | n/a | Take-or-pay contracts with investment-grade customers hold. | Large customers reaffirm contracted spending in writing |
| Macro stress | S4, S5 | 17% | +562 | n/a | Leveraged software and GPU-cloud debt has the least cushion. | spine test |

Expected change +136bp. Chance of wider spreads 72%.

### HY.Healthcare

Axis: Sector OAS change against today. No free level data.. Driver: Labour cost, government payment policy, floating-rate debt.

| Scenario | Drawn from | Probability | Change | Level | Why | Own observable |
|---|---|---|---|---|---|---|
| Calm | S1 | 28% | -50 | n/a | Moves with the index. | spine test |
| Leverage and rates | S2 | 37% | +30 | n/a | High leverage meets higher rates. | spine test |
| No AI link | S3 | 18% | +60 | n/a | Widens only with the index. | spine test |
| Defensive demand | S4 | 10% | +170 | n/a | Demand for care holds. | spine test |
| Stress, still defensive | S5 | 7% | +400 | n/a | Widens less than the index. | spine test |

Expected change +53bp. Chance of wider spreads 72%.

### HY.Consumer cyclical

Axis: Sector OAS change against today. No free level data.. Driver: Consumer spending, fuel cost, equity wealth. Covers retail, autos, leisure, gaming, airlines.

| Scenario | Drawn from | Probability | Change | Level | Why | Own observable |
|---|---|---|---|---|---|---|
| Consumer holds | S1 | 28% | -60 | n/a | Lower fuel cost helps travel and leisure. | spine test |
| Rate squeeze | S2 | 37% | +22 | n/a | Higher rates trim big-ticket spending. | spine test |
| Wealth effect | S3 | 18% | +85 | n/a | A deeper equity fall trims leisure spending. | spine test |
| Consumer recession | S4 | 10% | +290 | n/a | The largest HY sector leads the widening. | spine test |
| Stress | S5 | 7% | +500 | n/a | Cyclical names lose market access. | spine test |

Expected change +71bp. Chance of wider spreads 72%.

### HY.Consumer non-cyclical and services

Axis: Sector OAS change against today. No free level data.. Driver: Input costs and contract revenue.

| Scenario | Drawn from | Probability | Change | Level | Why | Own observable |
|---|---|---|---|---|---|---|
| Calm | S1 | 28% | -45 | n/a | Moves a little less than the index. | spine test |
| Steady | S2 | 37% | +15 | n/a | Stable revenue. | spine test |
| Mild contagion | S3 | 18% | +65 | n/a | No direct AI link. | spine test |
| Downturn, defensive | S4 | 10% | +180 | n/a | Staples and services hold up. | spine test |
| Stress | S5 | 7% | +410 | n/a | Widens less than the index. | spine test |

Expected change +51bp. Chance of wider spreads 72%.

### HY.Basic industry and capital goods

Axis: Sector OAS change against today. No free level data.. Driver: Manufacturing surveys, construction, commodity prices.

| Scenario | Drawn from | Probability | Change | Level | Why | Own observable |
|---|---|---|---|---|---|---|
| Orders hold | S1 | 28% | -55 | n/a | ISM stays above 50. | spine test |
| Steady | S2 | 37% | +15 | n/a | Strong factories offset higher rates. | spine test |
| Build-out suppliers hit | S3 | 18% | +105 | n/a | Building-material and electrical suppliers lose data-centre work. | spine test |
| Cyclical downturn | S4 | 10% | +280 | n/a | Orders fall with the ISM. | spine test |
| Stress | S5 | 7% | +490 | n/a | Cyclical names widen with the index. | spine test |

Expected change +71bp. Chance of wider spreads 72%.

### HY.Financial services

Axis: Sector OAS change against today. No free level data.. Driver: Market funding access and asset marks at non-bank lenders.

| Scenario | Drawn from | Probability | Change | Level | Why | Own observable |
|---|---|---|---|---|---|---|
| Funding open | S1 | 28% | -60 | n/a | Non-bank lenders refinance easily. | spine test |
| Higher funding cost | S2 | 37% | +25 | n/a | Funding cost rises faster than loan yields. | spine test |
| Private-credit marks | S3 | 18% | +130 | n/a | Lenders against GPUs and data centres mark loans down. | spine test |
| Loss cycle | S4 | 10% | +270 | n/a | Consumer and business loan losses rise. | spine test |
| Funding shut | S5 | 7% | +680 | n/a | Non-bank lenders depend on market funding. | spine test |

Expected change +90bp. Chance of wider spreads 72%.

### HY.Real estate and homebuilders

Axis: Sector OAS change against today. No free level data.. Driver: Mortgage rates and construction loans on data-centre projects.

| Scenario | Drawn from | Probability | Change | Level | Why | Own observable |
|---|---|---|---|---|---|---|
| Rates relief | S1 | 28% | -55 | n/a | Lower rate volatility helps housing. | spine test |
| Mortgage-rate drag | S2 | 37% | +40 | n/a | A 5% Treasury yield keeps mortgage rates high. | spine test |
| Construction loans extended | 50% of S3 | 9% | +90 | n/a | Banks extend terms and projects finish late. | Lenders amend and extend the large data-centre construction loans |
| Projects halted | 50% of S3 | 9% | +210 | n/a | Lenders take over unfinished data-centre projects. | A lender group declares default on a data-centre construction loan above $5bn |
| Macro stress | S4, S5 | 17% | +398 | n/a | Housing and development both stop. | spine test |

Expected change +94bp. Chance of wider spreads 72%.

### HY.Utilities and power

Axis: Sector OAS change against today. No free level data.. Driver: Power prices and contracted demand from data centres.

| Scenario | Drawn from | Probability | Change | Level | Why | Own observable |
|---|---|---|---|---|---|---|
| Power demand firm | S1 | 28% | -45 | n/a | Power prices stay high. | spine test |
| Pass-through | S2 | 37% | +10 | n/a | Power prices rise with inflation. | spine test |
| Load-growth rethink | S3 | 18% | +170 | n/a | Power producers priced for AI demand reprice. | spine test |
| Defensive | S4 | 10% | +200 | n/a | Power demand is stable in a downturn. | spine test |
| Stress | S5 | 7% | +430 | n/a | Widens less than the index. | spine test |

Expected change +72bp. Chance of wider spreads 72%.

## Checks

- All hard checks passed. No warnings.
- Reconciliation: 20 of 20 parent-versus-children tests inside tolerance.

## Calibration anchors (case memory, used only for magnitudes)

- April 2025 peak: IG 121bp, HY 461bp (FRED). Used as the size of a growth scare without recession.
- One-year range to 19 Nov 2026: IG 73 to 94bp, HY 260 to 352bp (FRED). Used for the calm scenario.
- Willer and Saunders ch03 Table 3.5: median recession widening of 124bp for IG and about 785bp for HY. Used to cap the accident scenario.
- 2022 hiking-cycle peaks near IG 165bp and HY 600bp. From memory, not checked against data.
