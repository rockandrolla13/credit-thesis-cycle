# Sector Cards

Default rows for the grid. Weights are rough index shares. Replace them when you have index data.
Each card names what moves the sector against its index, and the driver that can justify a split.
These cards are method memory. They hold no dated cases.

## Rating rows

| Row | Parent | Weight | Free data (FRED) |
|---|---|---|---|
| IG.AA (includes AAA) | IG | 0.12 | BAMLC0A2CAA |
| IG.A | IG | 0.43 | BAMLC0A3CA |
| IG.BBB | IG | 0.45 | BAMLC0A4CBBB |
| HY.BB | HY | 0.52 | BAMLH0A1HYBB |
| HY.B | HY | 0.36 | BAMLH0A2HYB |
| HY.CCC | HY | 0.12 | BAMLH0A3HYC |

Index rows: IG is `BAMLC0A0CM`. HY is `BAMLH0A0HYM2`.
Free sector spread levels do not exist. Write sector rows as changes, and leave `now` empty.

## Investment-grade sectors

| Sector | Weight | What moves it against the index | Own driver that can justify a split |
|---|---|---|---|
| Banking | 0.22 | Funding markets, the yield curve, loan losses, bank supply after earnings | Exposure to one lending book |
| Insurance and other financials | 0.09 | Reinvestment yields, private-credit holdings, lending-fund asset quality | Marks on private assets |
| REITs | 0.03 | Treasury yields, property type, development funding | One property type |
| Technology | 0.11 | Net bond supply, capex against cash flow, mergers, ratings | Whether capex is debt-funded or cut |
| Communications | 0.08 | Leverage, long-bond demand, mergers | A large merger |
| Consumer cyclical | 0.07 | Consumer spending, rates on car and home loans, tariffs | Fallen-angel risk at one large issuer |
| Consumer non-cyclical | 0.14 | Debt-funded mergers, drug-price policy | A large merger |
| Energy | 0.07 | Oil and gas prices, power demand | Oil price path |
| Industrials (basic, capital goods, transport) | 0.10 | Manufacturing surveys, capital-spending orders, commodity prices | One end market |
| Utilities | 0.09 | Capex-funded supply, long-bond rates, load forecasts, regulation | Load-growth forecasts |

## High-yield sectors

| Sector | Weight | What moves it against the index | Own driver that can justify a split |
|---|---|---|---|
| Energy | 0.11 | Oil and gas prices, hedging | Oil price path |
| Communications | 0.13 | Leverage, declining legacy revenue, debt exchanges | One large restructuring |
| Technology | 0.08 | Refinancing cost, customer contracts, software revenue | Solvency of one large borrower |
| Healthcare | 0.08 | Labour cost, government payment policy, floating-rate debt | Policy change |
| Consumer cyclical | 0.20 | Consumer spending, fuel cost, equity wealth | One sub-sector |
| Consumer non-cyclical and services | 0.11 | Input costs, contract revenue | None common |
| Basic industry and capital goods | 0.15 | Manufacturing surveys, construction, commodity prices | One end market |
| Financial services | 0.06 | Market funding access, loan losses, asset marks | Funding access |
| Real estate and homebuilders | 0.05 | Mortgage rates, construction loans, development pipelines | Construction-loan outcomes |
| Utilities and power | 0.03 | Power prices, capacity auctions, contracted demand | Demand forecasts |

## Rules for splits and merges

- A row keeps 4 or 5 scenarios.
- Merge two spine scenarios when the sector does not tell them apart.
- Split one spine scenario when a sector driver decides the outcome inside it.
- A split needs its own observable. A merged or unsplit scenario inherits the spine test.
- Give a spread change for each spine scenario a row scenario draws from. The script blends them.
