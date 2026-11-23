import json, sys
def pure(names, dxs, whys):
    return [{"name": n, "from": {f"S{i+1}": d}, "why": w} for i, (n, d, w) in enumerate(zip(names, dxs, whys))]
def sec(id_, parent, weight, driver, scen, group="sector", now=None, axis=None):
    r = {"id": id_, "level": "rating" if group == "rating" else "sector", "parent": parent, "group": group, "weight": weight,
         "axis": axis or "Sector OAS change against today. No free level data.", "driver": driver, "scenarios": scen}
    if now is not None: r["now"] = now
    return r
spine = [
 {"id":"S1","name":"Supply absorbed","p":0.28,"p_source":"PM_assumption",
  "test":"Otherwise. Capex holds, growth holds, and the Fed stops at 4.25% or lower.",
  "observables":[{"series":"FRED DFEDTARU","threshold":"4.25 or lower on 2027-05-22, and no earlier test is true"}],
  "evidence":["Oil fell from $110 to $90 in a month and 10-year breakeven inflation is at a three-year low of 2.15% (FRED DCOILWTICO, T10YIE).",
              "The October SLOOS is near neutral at 1.7% net tightening (FRED DRTSCILM)."]},
 {"id":"S2","name":"Higher rates, supply grind","p":0.37,"p_source":"evidence_weighted",
  "test":"Fourth. The Fed funds upper bound is 4.50% or higher on the horizon date.",
  "observables":[{"series":"FRED DFEDTARU","threshold":"4.50 or higher on 2027-05-22"},
                 {"series":"AA to BBB spread ratio (FRED BAMLC0A2CAA / BAMLC0A4CBBB)","threshold":"above 0.62"}],
  "evidence":["Futures price a December hike at about 95%. The October minutes say almost all participants favour further hikes (CNBC, 18 Nov 2026).",
              "The 2-year Treasury yields 4.76% against a 4.00% policy ceiling (FRED DGS2, DFEDTARU).",
              "Goldman forecasts $420bn of hyperscaler IG issuance in 2027. SanCap forecasts up to $450bn."]},
 {"id":"S3","name":"AI digestion","p":0.18,"p_source":"PM_assumption",
  "test":"Third. The five largest AI spenders guide combined 2027 capex to $900bn or less, or two of the five cut guidance.",
  "observables":[{"series":"Fourth-quarter earnings guidance, late January to early February 2027","threshold":"combined 2027 capex of $900bn or less, against a consensus above $1,000bn"}],
  "evidence":["Nvidia lost about half its market value in six weeks. Reuters reported an SEC accounting probe on 20 Nov 2026.",
              "Tech IG borrowing costs are the highest since 2009 by one report. The 2027 funding gap is put at about $291bn (SanCap, 20 Nov 2026).",
              "Against: strong Nvidia earnings in November show demand had not yet dropped."]},
 {"id":"S4","name":"Hard landing","p":0.10,"p_source":"PM_assumption",
  "test":"Second. The manufacturing ISM prints under 50 for two months in a row, or the Sahm rule reaches 0.50.",
  "observables":[{"series":"ISM manufacturing PMI","threshold":"under 50 for two consecutive months"},{"series":"Sahm rule (FRED SAHMREALTIME)","threshold":"0.50 or higher"}],
  "evidence":["Against: the October ISM is 55.5 and rising, after ten months of expansion.","For: the Fed is hiking into an equity fall of 8% on the S&P 500 and 13% on the Nasdaq."]},
 {"id":"S5","name":"Funding accident","p":0.07,"p_source":"PM_assumption",
  "test":"First. A bank or insurer with over $50bn of assets fails or is rescued, or the Fed opens an emergency facility, or the IG primary market shuts for five business days.",
  "observables":[{"series":"Fed H.4.1 release","threshold":"a new emergency facility appears"},{"series":"IG primary market calendar","threshold":"five straight business days with no deals, outside holidays"}],
  "evidence":["CCC spreads are at a three-year high of 1361bp (FRED BAMLH0A3HYC). CoreWeave bonds yield about 16% (CNBC, 6 Nov 2026).",
              "One source reports a force majeure notice on an $18bn data-centre construction loan held by about 20 banks.",
              "Against: aggregate corporate debt fell from 50.8% to 48.2% of GDP in three years (Fed Z.1)."]},
]
N = ["Supply absorbed","Higher rates, supply grind","AI digestion","Hard landing","Funding accident"]
rows = [
 {"id":"IG","level":"asset_class","axis":"ICE BofA US Corporate OAS (FRED BAMLC0A0CM)","driver":"Hyperscaler supply, the Fed path, growth.","now":94,"spread_duration":6.6,"recon_tol_bp":5,
  "scenarios":pure(N,[-12,14,18,56,116],
   ["Rate volatility falls. Yield buyers take the January supply without extra concession.",
    "The Fed keeps hiking. Hyperscaler issuance runs above the 2026 pace. Widening starts in the top ratings.",
    "Less hyperscaler supply helps the top tier. BBB names and lenders to the build-out widen.",
    "Earnings and ratings fall. Cyclical sectors lead.",
    "Forced liquidation. Financials lead."])},
 {"id":"HY","level":"asset_class","axis":"ICE BofA US High Yield OAS (FRED BAMLH0A0HYM2)","driver":"Default expectations, refinancing access, equity volatility.","now":352,"spread_duration":3.1,"recon_tol_bp":25,
  "scenarios":pure(N,[-52,18,108,248,498],
   ["Equity volatility fades. Stress stays inside a few CCC names.",
    "Coupons reset higher. Income absorbs most of it. BB feels the rate move.",
    "GPU-cloud and data-centre borrowers reprice. It spreads to suppliers and power producers.",
    "Default expectations rise across cyclical sectors.",
    "The primary market closes. CCC borrowers cannot refinance."])},
 sec("IG.AA","IG",0.12,"Hyperscaler supply. Most large AI issuers are rated AA or AAA.",pure(N,[-8,16,-2,30,75],
   ["Concessions on hyperscaler bonds shrink a little.","The supply lands here.","Less supply offsets weaker sentiment.","High quality widens least.","High quality widens least, but supply overhang remains."]),"rating",68,"ICE BofA AA US Corporate OAS (FRED BAMLC0A2CAA)"),
 sec("IG.A","IG",0.43,"Banks dominate this tier.",pure(N,[-10,12,12,45,100],
   ["Moves with the index.","Banks gain from higher rates and issue less than tech.","Questions on bank lending to the build-out.","Loan losses rise.","Banks sit at the centre of funding stress."]),"rating",78,"ICE BofA Single-A US Corporate OAS (FRED BAMLC0A3CA)"),
 sec("IG.BBB","IG",0.45,"Downgrade risk and cyclical exposure.",pure(N,[-15,14,26,75,145],
   ["Highest beta in a rally.","Moves with the index.","Lower-rated AI borrowers and cyclicals carry the downgrade risk.","Fallen-angel fear returns.","Forced sellers of downgraded bonds."]),"rating",117,"ICE BofA BBB US Corporate OAS (FRED BAMLC0A4CBBB)"),
 sec("HY.BB","HY",0.52,"Rates and crossover demand.",pure(N,[-30,18,55,150,310],
   ["Modest rally from already tight levels.","Longest duration in HY. Feels the rate move.","Limited direct AI exposure.","Downgrades from IG add supply.","Wide, but refinancing stays possible."]),"rating",210,"ICE BofA BB US High Yield OAS (FRED BAMLH0A1HYBB)"),
 sec("HY.B","HY",0.36,"Refinancing cost and earnings.",pure(N,[-55,20,110,270,540],
   ["Moves with the index.","Higher coupons at refinancing.","Holds most of the leveraged tech and supplier names.","Earnings fall against high interest cost.","Refinancing window shuts."]),"rating",380,"ICE BofA Single-B US High Yield OAS (FRED BAMLH0A2HYB)"),
 sec("HY.CCC","HY",0.12,"A few distressed issuers. Four names carry about 30% of the spread (Vanguard, 10 Nov 2026).",pure(N,[-150,30,340,620,1200],
   ["Distressed names bounce, but restructurings continue.","Already priced for distress. Rates add little.","A large restructuring in AI-linked debt.","Defaults rise broadly.","No refinancing at any price."]),"rating",1361,"ICE BofA CCC and lower US High Yield OAS (FRED BAMLH0A3HYC)"),
 # ---- IG sectors
 sec("IG.Banking","IG",0.22,"Funding markets, the curve, loan losses, lending to non-bank funds.",pure(
   ["Calm funding","Haven from tech supply","AI loan-book questions","Credit-cost cycle","Systemic stress"],[-14,8,22,60,150],
   ["Bank supply after January earnings clears easily.","Higher rates lift margins. Bank net supply is lower than tech supply.","Investors ask about construction loans and lending to private-credit funds.","Loan losses rise. Banks widen a little more than the index.","Banks sit at the centre of any funding accident."])),
 sec("IG.Insurance and other financials","IG",0.09,"Private-credit holdings and lending-fund asset quality.",[
   {"name":"Calm","from":{"S1":-14},"why":"Higher yields help life insurers reinvest."},
   {"name":"Yield tailwind","from":{"S2":12},"why":"Insurers are natural buyers of the new supply."},
   {"name":"Private-credit marks contained","from":{"S3":{"frac":0.65,"dx":20}},"why":"Insurers hold AI debt, but marks move slowly.","observable":"Rated lending funds report non-accruals under 3% of assets"},
   {"name":"Lending-fund and insurer scrutiny","from":{"S3":{"frac":0.35,"dx":50}},"why":"Lending funds report bad loans. Insurers disclose data-centre holdings.","observable":"Non-accruals above 3% at two large rated lending funds, or a fund limits withdrawals"},
   {"name":"Macro stress","from":{"S4":70,"S5":170},"why":"Asset managers and insurers carry the private-credit link in a downturn."}]),
 sec("IG.REITs","IG",0.03,"Treasury yields and data-centre development funding.",pure(
   ["Rates relief","Rate drag","Leasing slowdown","Property downturn","Funding stress"],[-14,18,30,70,150],
   ["Lower rate volatility helps a rate-sensitive sector.","Data-centre REITs need funding while yields stay near 5%.","Data-centre leasing slows after capex cuts.","Property values fall with growth.","Development funding stops."])),
 sec("IG.Technology","IG",0.11,"Net bond supply and capex against cash flow. About 20bp wide of the index on 2 Nov 2026 by one report.",[
   {"name":"Supply absorbed","from":{"S1":-14},"why":"Buyers accept current concessions. The premium to the index holds."},
   {"name":"Supply grind","from":{"S2":28},"why":"2027 issuance near $420bn to $450bn meets a tired buyer base."},
   {"name":"Capex cut, balance sheets protected","from":{"S3":{"frac":0.6,"dx":-6}},"why":"Less borrowing. Bondholders gain what shareholders lose.","observable":"Hyperscaler bond issuance in Q1 2027 under $60bn, and no rating action"},
   {"name":"Capex cut with a credit event","from":{"S3":{"frac":0.4,"dx":45}},"why":"A lower-rated AI borrower loses its IG rating, or the accounting probe widens.","observable":"A rating agency moves a large AI borrower to negative outlook at BBB-, or a second issuer discloses a probe"},
   {"name":"Macro stress","from":{"S4":50,"S5":125},"why":"Tech no longer acts as the safe sector, because it now carries the debt."}]),
 sec("IG.Communications","IG",0.08,"Leverage and demand for long bonds.",pure(
   ["Calm","Long-bond competition","Defensive cash flows","Leverage worry","Stress"],[-13,20,16,60,115],
   ["Moves with the index.","Long-dated BBB telecom debt competes with hyperscaler long bonds.","Subscription revenue holds.","High leverage meets weaker revenue.","Large capital structures widen with the index."])),
 sec("IG.Consumer cyclical","IG",0.07,"Consumer spending and rates on car and home loans.",pure(
   ["Consumer holds","Rate squeeze","Wealth effect","Consumer recession","Stress"],[-14,18,20,85,135],
   ["Lower oil helps spending.","Car finance and housing feel 5% Treasury yields.","A deeper equity fall trims high-end spending.","Autos and retail lead. Fallen-angel risk rises.","Cyclical names widen more than the index."])),
 sec("IG.Consumer non-cyclical","IG",0.14,"Debt-funded mergers and drug-price policy. No direct AI link.",[
   {"name":"Lags the rally","from":{"S1":-10},"why":"Defensive sectors gain least when risk appetite returns."},
   {"name":"Defensive haven","from":{"S2":10,"S3":8},"why":"Stable cash flows. The sector does not tell these two scenarios apart."},
   {"name":"Mild widening","from":{"S4":35},"why":"Demand for staples and medicine holds in a downturn."},
   {"name":"Stress, still defensive","from":{"S5":75},"why":"Widens least of all IG sectors."}]),
 sec("IG.Energy","IG",0.07,"Oil and gas prices. Power demand from data centres.",pure(
   ["Oil steady","Inflation hedge","Power-demand rethink","Oil slump","Stress"],[-14,8,20,85,140],
   ["Oil near $90 keeps cash flow strong.","Firm oil goes with firm inflation. Net supply is low.","Gas pipeline names priced for data-centre demand give some back.","A demand fall takes oil under $65.","High beta to a global growth shock."])),
 sec("IG.Industrials","IG",0.10,"Manufacturing surveys and capital-spending orders. Covers basic industry, capital goods and transport.",pure(
   ["Orders hold","Steady","Equipment orders cut","Cyclical downturn","Stress"],[-13,10,24,75,115],
   ["ISM stays above 50.","Strong factories offset higher rates.","Makers of power and cooling equipment lose data-centre orders.","Orders fall with the ISM.","Cyclical names widen with the index."])),
 sec("IG.Utilities","IG",0.09,"Capex-funded supply, long-bond rates and load forecasts.",pure(
   ["Calm","Capex supply","Load-growth rethink","Defensive","Stress, still defensive"],[-11,20,10,40,85],
   ["Heavy utility supply limits the rally.","Utilities borrow heavily for grid and generation. Long bonds feel rates.","Lower load forecasts mean less borrowing. Regulated cash flow holds.","Regulated revenue holds in a downturn.","Widens less than the index."])),
 # ---- HY sectors
 sec("HY.Energy","HY",0.11,"Oil and gas prices.",pure(
   ["Oil steady","Inflation hedge","Low AI link","Oil slump","Stress"],[-45,5,70,300,560],
   ["Balance sheets are strong after a year of high oil.","Firm oil protects cash flow.","Only gas and power names are exposed.","Oil under $65 in a demand slump.","High beta to a growth shock."])),
 sec("HY.Communications","HY",0.13,"Leverage, declining legacy revenue, debt exchanges. About a quarter of the CCC index.",pure(
   ["Relief","Refinancing cost","Fibre story fades","Restructuring wave","Stress"],[-70,30,110,270,510],
   ["Distressed capital structures bounce the most.","Large maturities meet higher coupons.","Fibre builders lose the AI traffic story.","More debt exchanges and defaults.","No market access for leveraged names."])),
 sec("HY.Technology","HY",0.08,"Refinancing cost and customer contracts at GPU-cloud and software borrowers.",[
   {"name":"Funding reopens","from":{"S1":-110},"why":"The most beaten-down sector bounces the most."},
   {"name":"Costly funding, no default","from":{"S2":50},"why":"GPU-cloud borrowers refinance at 12% to 16%. Nobody defaults."},
   {"name":"GPU-cloud restructuring","from":{"S3":{"frac":0.6,"dx":380}},"why":"A large GPU-cloud borrower restructures after customers cut orders.","observable":"A GPU-cloud borrower with over $10bn of debt misses a payment or launches a debt exchange"},
   {"name":"Contracts honoured","from":{"S3":{"frac":0.4,"dx":160}},"why":"Take-or-pay contracts with investment-grade customers hold.","observable":"Large customers reaffirm contracted spending in writing"},
   {"name":"Macro stress","from":{"S4":360,"S5":850},"why":"Leveraged software and GPU-cloud debt has the least cushion."}]),
 sec("HY.Healthcare","HY",0.08,"Labour cost, government payment policy, floating-rate debt.",pure(
   ["Calm","Leverage and rates","No AI link","Defensive demand","Stress, still defensive"],[-50,30,60,170,400],
   ["Moves with the index.","High leverage meets higher rates.","Widens only with the index.","Demand for care holds.","Widens less than the index."])),
 sec("HY.Consumer cyclical","HY",0.20,"Consumer spending, fuel cost, equity wealth. Covers retail, autos, leisure, gaming, airlines.",pure(
   ["Consumer holds","Rate squeeze","Wealth effect","Consumer recession","Stress"],[-60,22,85,290,500],
   ["Lower fuel cost helps travel and leisure.","Higher rates trim big-ticket spending.","A deeper equity fall trims leisure spending.","The largest HY sector leads the widening.","Cyclical names lose market access."])),
 sec("HY.Consumer non-cyclical and services","HY",0.11,"Input costs and contract revenue.",pure(
   ["Calm","Steady","Mild contagion","Downturn, defensive","Stress"],[-45,15,65,180,410],
   ["Moves a little less than the index.","Stable revenue.","No direct AI link.","Staples and services hold up.","Widens less than the index."])),
 sec("HY.Basic industry and capital goods","HY",0.15,"Manufacturing surveys, construction, commodity prices.",pure(
   ["Orders hold","Steady","Build-out suppliers hit","Cyclical downturn","Stress"],[-55,15,105,280,490],
   ["ISM stays above 50.","Strong factories offset higher rates.","Building-material and electrical suppliers lose data-centre work.","Orders fall with the ISM.","Cyclical names widen with the index."])),
 sec("HY.Financial services","HY",0.06,"Market funding access and asset marks at non-bank lenders.",pure(
   ["Funding open","Higher funding cost","Private-credit marks","Loss cycle","Funding shut"],[-60,25,130,270,680],
   ["Non-bank lenders refinance easily.","Funding cost rises faster than loan yields.","Lenders against GPUs and data centres mark loans down.","Consumer and business loan losses rise.","Non-bank lenders depend on market funding."])),
 sec("HY.Real estate and homebuilders","HY",0.05,"Mortgage rates and construction loans on data-centre projects.",[
   {"name":"Rates relief","from":{"S1":-55},"why":"Lower rate volatility helps housing."},
   {"name":"Mortgage-rate drag","from":{"S2":40},"why":"A 5% Treasury yield keeps mortgage rates high."},
   {"name":"Construction loans extended","from":{"S3":{"frac":0.5,"dx":90}},"why":"Banks extend terms and projects finish late.","observable":"Lenders amend and extend the large data-centre construction loans"},
   {"name":"Projects halted","from":{"S3":{"frac":0.5,"dx":210}},"why":"Lenders take over unfinished data-centre projects.","observable":"A lender group declares default on a data-centre construction loan above $5bn"},
   {"name":"Macro stress","from":{"S4":270,"S5":580},"why":"Housing and development both stop."}]),
 sec("HY.Utilities and power","HY",0.03,"Power prices and contracted demand from data centres.",pure(
   ["Power demand firm","Pass-through","Load-growth rethink","Defensive","Stress"],[-45,10,170,200,430],
   ["Power prices stay high.","Power prices rise with inflation.","Power producers priced for AI demand reprice.","Power demand is stable in a downturn.","Widens less than the index."])),
]
g = {"as_of":"2026-11-22","horizon":"2027-05-22","horizon_months":6,
 "findings": json.load(open(sys.argv[2])) if len(sys.argv) > 2 else [],
 "limits":[
  "Every probability and spread move is judgement. The script checks coherence, not correctness.",
  "Free data has no sector spread levels. Sector rows are changes from today, and the weights are rough index shares.",
  "Spread durations of 6.6 years for IG and 3.1 years for HY are assumptions, not index data.",
  "Carry cover ignores default losses. For HY the true cushion is smaller.",
  "The fair-value weights assume today's spread equals the expected future spread. That ignores the risk premium.",
  "Several news facts rest on one source each. Examples are the construction-loan force majeure and the 20bp tech premium."],
 "calibration":[
  "April 2025 peak: IG 121bp, HY 461bp (FRED). Used as the size of a growth scare without recession.",
  "One-year range to 19 Nov 2026: IG 73 to 94bp, HY 260 to 352bp (FRED). Used for the calm scenario.",
  "Willer and Saunders ch03 Table 3.5: median recession widening of 124bp for IG and about 785bp for HY. Used to cap the accident scenario.",
  "2022 hiking-cycle peaks near IG 165bp and HY 600bp. From memory, not checked against data."],
 "spine":spine,
 "relations":[{"name":"HY minus IG (bp)","a":"HY","b":"IG","op":"diff"},{"name":"HY to IG ratio","a":"HY","b":"IG","op":"ratio"},
  {"name":"BB minus BBB (bp)","a":"HY.BB","b":"IG.BBB","op":"diff"},{"name":"CCC minus BB (bp)","a":"HY.CCC","b":"HY.BB","op":"diff"},
  {"name":"A minus AA (bp)","a":"IG.A","b":"IG.AA","op":"diff"},{"name":"AA to BBB ratio (price of AI supply)","a":"IG.AA","b":"IG.BBB","op":"ratio"}],
 "rows":rows}
json.dump(g, open(sys.argv[1], "w"), indent=1)
