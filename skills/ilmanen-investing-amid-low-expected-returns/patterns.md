# Patterns: Investing Amid Low Expected Returns (Ilmanen)

## Valuation-neutral historical premium
**When to use**: before using any historical average as an expected return. (Ch 2, Ch 10)
**How**: (1) Regress periodic excess returns on contemporaneous changes in the asset's own yield or valuation ratio. (2) Read the slope as empirical duration. (3) Slope × net yield change ÷ years = annual windfall. (4) Use the annualized intercept as the neutral premium. (5) Then check whether today's yield is below the sample average.
**Trade-offs**: weak for long/short factors where valuation change and return are loosely linked. Understates bond convexity.

## Yield-based expected return (income plus growth)
**When to use**: 5-10 year return assumptions for an asset class. (Ch 4, Ch 10)
**How**: real return = income yield + real growth + valuation change. The author's default weights are 1, 1 and 0. Equities: dividend yield + 1.5%, or CAEY. Bonds: starting yield. Real estate: net rental yield (gross less one third) + zero real growth. Add expected inflation for nominal.
**Trade-offs**: wide uncertainty bands. Not a timing tool (Ch 16).

## Three-way yield decomposition
**When to use**: explaining a move in government bond yields. (Ch 4)
**How**: 10-year yield = expected average inflation + expected average real short rate + bond risk premium. Use survey forecasts of future short rates and inflation. The premium is the residual.
**Trade-offs**: survey-based premium is cleaner in logic. The plain curve slope has predicted near-term returns better.

## Credit spread-to-premium conversion
**When to use**: turning a credit spread into an expected excess return. (Ch 4)
**How**: (1) Start from OAS. (2) Subtract expected default loss: 15-25bp for IG, 200-250bp for HY on history. (3) Allow for IG downgrade bias, at most 30bp with defaults. (4) Allow for index leakage from forced fallen-angel sales. (5) Compare with historical spread capture: about 56% IG and 54% HY to 2020.
**Trade-offs**: capture depends heavily on the spread level at sample end. It was 25% for IG in a sample ending 2009.

## Fallen-angel and front-end credit tilts
**When to use**: harvesting forced-selling and leverage-aversion effects in corporate bonds. (Ch 4)
**How**: buy bonds soon after downgrade from IG to HY. Separately, favour 1-3 year corporates, levered.
**Trade-offs**: front-end credit is hit hardest when default risk jumps. It only pays if financing spreads are well inside bond spreads.

## Illiquid asset de-smoothing check
**When to use**: before putting private assets in an optimizer or a risk report. (Ch 5, Ch 12, Ch 13)
**How**: (1) Use annual, not quarterly, returns. (2) Include lagged equity betas. (3) Compare with a listed proxy: REITs for property, levered small-cap value for buyouts. (4) Replace reported volatility and beta with realistic ones (for PE the author suggests near 20% and 1.3 against reported 9% and 0.5). (5) Cap the allocation top-down.
**Trade-offs**: reported smooth numbers still drive regulation and organizational patience.

## Style premium admission test
**When to use**: deciding whether a factor belongs in a strategic portfolio. (Ch 6, Ch 9)
**How**: require it to be persistent (in and out of sample), pervasive (several asset classes), robust (several specifications), with an economic rationale and an identifiable other side.
**Trade-offs**: well-known factors pass and carry crowding risk. Novel ones carry overfitting risk.

## Backtest discounting
**When to use**: converting a gross backtest into a forward assumption. (Ch 9)
**How**: start by halving the gross Sharpe ratio. Or estimate trading costs separately and apply a smaller discount after. Discount more for older data and more complex strategies.
**Trade-offs**: "an art, not a science".

## Demystifying regression
**When to use**: judging what a manager, a hedge fund sleeve or a whole portfolio is paid for. (Ch 7, Ch 15)
**How**: regress excess returns on market factors and style factors. Contribution = beta × factor premium. Intercept = alpha. Compare the fee with the active, non-beta risk.
**Trade-offs**: model- and sample-specific. Use holdings for illiquid or fast-changing portfolios.

## Risk-balanced multi-premia portfolio
**When to use**: strategic allocation when shorting and leverage are allowed to some degree. (Ch 11, Ch 12)
**How**: (1) Set the illiquid share and other constraints top-down. (2) Start from equal volatility across lowly correlated premia. (3) Tilt to higher Sharpe ratios and better diversifiers. (4) Lever to the target volatility. (5) Track risk allocations beside capital allocations.
**Trade-offs**: leverage, unconventionality, no story. The full version is unrealistic for a total portfolio.

## Often-but-little rebalancing
**When to use**: keeping a liquid multi-asset portfolio near targets. (Ch 11)
**How**: each quarter move one quarter of the way to target.
**Trade-offs**: like all contrarian rules it is short structural change.

## Tail protection choice: trend versus puts
**When to use**: equity risk dominates and a drawdown would threaten survival. (Ch 13)
**How**: diversify first. Then prefer trend following for slow, protracted bear markets and index puts for fast gaps. Keep either small. Add drawdown rules as a last line.
**Trade-offs**: puts bled about 6% a year at 10% volatility over 1985-2020. Trend can miss sudden falls and was flat in the 2010s.

## Humble timing ("sin a little")
**When to use**: tactical tilts around a strategic portfolio. (Ch 16)
**How**: use out-of-sample signals. Combine value with momentum and yield curve slope. Keep exposure changes modest (the tested rule ranged 0.5 to 1.5). Spread across several markets.
**Trade-offs**: Sharpe ratios of 0.3-0.4 at best. Contrarian signals are early.

## Patience protocol
**When to use**: a strategy or manager has underperformed for one to five years. (Ch 9, Ch 17)
**How**: (1) Check the probability table for its Sharpe ratio. (2) Ask whether valuations cheapened or richened during the loss. (3) Check process, exposures and controls. (4) Review at portfolio level, rarely. (5) Follow the written plan.
**Trade-offs**: patience is wrong when fees are persistently high or the structure has truly changed.
