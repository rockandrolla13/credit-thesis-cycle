# Patterns: Trading Global Macro Markets

Every figure is a backtest result the authors report, usually without transaction costs and often on a small sample. Chapter files give sample periods and caveats.

## Moving-average regime filter (the house template)
**When to use**: any time an asset has one dominant driver.
**How**: hold the asset only when the driver is above (or below) its 55dma, lagged one day (two for cross-time-zone pairs). Report the active IR against buy-and-hold.
**Trade-offs**: lower total return, lower drawdown. Fails when a one-day lag removes the edge (gold vs DXY and real rates, Ch 14).

## Event study around Fed turning points
**When to use**: positioning rates, equities, credit or the USD for the first hike, last hike, first cut, last cut.
**How**: date cycles after 1986. Plot median and percentile paths from about 75 days before to after the event. Position in the windows that are consistent (Ch 5, Ch 8, Ch 11, Ch 13).
**Trade-offs**: seven or eight cycles. High-inflation cycles (1970s, 2022) break the pattern.

## Event-day momentum
**When to use**: FOMC days, payroll days, US election day, OPEC meetings, large relative up-days in China.
**How**: score the event by price, not by text. Act on moves of 2 standard deviations or more. Follow the closing direction (Ch 4, Ch 6, Ch 10, Ch 14). Full intraday reversals count too: USDMXN active IR 1.41 over nine days (Ch 13).
**Trade-offs**: asymmetric. Rates sell-offs on payrolls and equity sell-offs on FOMC days do not follow through. Wait for the close.

## Volatility risk premium dip buying
**When to use**: after an equity sell-off or an implied-volatility spike.
**How**: buy the SPX when VIX minus one-month realized volatility is 2 standard deviations above its one-year norm. Hold 22 days. Active IR almost 1.1 (Ch 9).
**Trade-offs**: triggers cluster across countries, so little diversification (Ch 10).

## Maximum-volatility cut-out
**When to use**: holding credit spread risk or FX carry.
**How**: take the largest one-year z-score among VIX, MOVE, OVX, FX volatility and HY spreads. Exit above 2. Re-enter below 2. Credit IR 1.11 vs 0.42. Carry 1.30 vs 0.89 (Ch 11, Ch 12).
**Trade-offs**: out of the market over 40% of the time in credit. Carry stays positive until a 4 standard deviation spike.

## Receive on short-leg inversion
**When to use**: late in a hiking cycle.
**How**: receive when 6m/2s or 3m/10s inverts, or when FF6 minus FF1 prices more than 12.5bp of cuts, or when the one-year swap trades below the floating rate. Stop if the one-year trades back above the fix (Ch 3, Ch 5).
**Trade-offs**: lags of 1 to 23 months. Fails when inflation is high.

## FX-hedged carry at extremes
**When to use**: choosing between UST, Bunds, gilts and JGBs.
**How**: go with the market whose FX-hedged yield pickup is in its extreme percentile (Ch 7).
**Trade-offs**: sideways in bond bear markets.

## Signal agreement composite
**When to use**: FX, where each driver is weak.
**How**: score BTP-Bund spread, relative equities, relative data change and five-year differential as +1 or -1. Trade EUR only at +4 or -4. Active IR 1.75, on 16% of the time (Ch 12).
**Trade-offs**: rarely on. Idiosyncratic shocks are not handled.

## Volatility-adjusted carry basket
**When to use**: default FX risk position, mainly EM.
**How**: rank by carry to vol, long top five, short bottom five, size by three-month volatility. IR 0.89 (Ch 12).
**Trade-offs**: hurt by a falling USDJPY, a volatility spike with crowded positioning, and carry below 400bp.

## Fallen angel capture
**When to use**: structural credit allocation.
**How**: buy issuers after downgrade from IG to HY, when forced selling has passed (Ch 11).
**Trade-offs**: large drawdowns in crises. It took about 3.5 years on average to regain IG between 2000 and 2021.

## Credit-confirmed equity de-risking
**When to use**: a VIX jump of 3 points or more.
**How**: cut SPX risk for a month only if HY spreads were wider over the prior six months at the SPX high. Active IR 0.94 vs 0.53 (Ch 11).
**Trade-offs**: none of the benefit comes from the VIX jump alone.

## Bubble riding with the generals rule
**When to use**: price more than two standard deviations above real trend.
**How**: stay long. Cut when the fourth of seven leaders holds below its 200dma for five days, or the index falls 15% from its peak (Ch 8).
**Trade-offs**: false positives. Tested on few bubbles.

## Contrarian extremes
**When to use**: sentiment or revisions at tails.
**How**: buy equities when the global ERI is below its 5th percentile (active IR 0.73 to 0.83), AAII is below -20, leveraged CFTC positioning is below -2 z (1.37), or POLLS is below 8. Sell when POLLS is above 18 for two days (Ch 8, Ch 9).
**Trade-offs**: early in 2000 and 2008. Fading extremes does not work in bonds, commodities or CTA positioning (Ch 15).

## Commodity backwardation carry
**When to use**: commodity allocation.
**How**: long the most backwardated, short the most contangoed of 7 to 10 markets, volatility adjusted. IR 1.11 (0.75 if BCOM weighted). Risk-adjusted curve carry: 2.04 (Ch 14).
**Trade-offs**: seasonal spreads. Weaker since the early 2000s.

## 200dma asset switch
**When to use**: equity vs bond allocation.
**How**: equities if above their 200dma, else bonds if above theirs (scaled to equity risk), else T-bills. IR 0.59 vs 0.46 for the SPX (Ch 15).
**Trade-offs**: late at bottoms. Pair with the dip-buying rules.

## Nearest-neighbour regime playbook
**When to use**: setting cross-asset return expectations.
**How**: describe today by levels and changes of growth, inflation and financial conditions plus volatility. Weight the most similar past periods. Read their forward returns (Ch 15).
**Trade-offs**: less interpretable than quadrants. The clustering version (10 clusters) adds labels.

## Reverse optimization for a new asset
**When to use**: sizing Bitcoin or any asset with a biased history.
**How**: solve for the expected return that justifies a weight given current volatility and correlations. 1% Bitcoin needs about 12% (Ch 16).
**Trade-offs**: depends on the calibration portfolio.
