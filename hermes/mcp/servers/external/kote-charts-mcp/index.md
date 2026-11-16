---
title: "Kote Charts MCP - Bitcoin On-Chain Metrics"
description: "A keyless MCP server over 114 Bitcoin on-chain charts, each with its formula, units, cadence, limitations and a citation."
category: Finance
stars: "0 (remote Streamable HTTP, keyless; four tools, all four driven)"
added: 2026-11-16
source: "the chatmcp/mcp-directory submission queue entry #7473 filed 2026-11-16T17:48:24Z, and a driven session on 2026-11-16 in which all four tools, both prompts and the resource surface were called over Streamable HTTP"
relevance: ★★
tags: [bitcoin, on-chain, crypto-analytics, market-data, keyless, citations, data-provenance, remote, mcp]
last_updated: "2026-11-16"
---

# Kote Charts MCP

**An assistant asked where Bitcoin sits in its cycle will answer from a number it cannot defend.** The metric is either wrong, or right and unsourced, and in both cases the operator has no way to check it. The gap is not the model. It is that on-chain metrics travel without their definitions: an MVRV Z-Score means one thing at one vendor and something slightly different at the next, and the units, the update cadence and the known blind spots are exactly what a caller needs before quoting the number in a report.

Kote Charts is the version of that answer that ships its own working. **114 charts** in **13** categories, computed from the vendor's own Bitcoin full node, free and keyless, and every one of them carries the **formula**, the **payload fields with units**, the **input categories**, the **update cadence**, the **known limitations**, the **analysed block height** and a **ready-made citation string**. The pass below drove all **four** tools through **17** `tools/call` requests, called both prompts, listed the resource surface, and reproduced one chart's figures from the other's.

```
Server type:   remote Streamable HTTP
Endpoint:      https://kotecharts.com/api/v1/mcp
Server:        kote-analytics, version 1.1.0, title "Kote Charts - Bitcoin on-chain analytics"
Protocol:      2025-06-18
Auth:          none (60 requests a minute per IP); an optional free key raises the REST tier to 3 requests a second
Tools:         4 (list_charts, describe_chart, get_chart, get_latest)
Resources:     116 (catalog, methodology, and one per chart)
Prompts:       2 (explain_metric, cycle_position_brief)
Registry:      com.kotecharts/charts, versions 1.1.0 and 1.1.1 published
Repo:          github.com/kote-charts/kote-charts (code MIT; data under separate terms)
Listed on:     the mcp.so submission queue as #7473
```

## The evidence tier

**Keyless and driven.** No credential was needed at any point. `initialize` answered **200** as `kote-analytics` **1.1.0** on protocol **2025-06-18**, `tools/list` returned **four** closed schemas, `resources/list` returned **116** entries of which **114** are per-chart methodology documents, and `prompts/list` returned **two**. Calls made: `list_charts` twice (once bare, once with `query: "sopr"`), `describe_chart` on `mvrv-z-score`, `get_latest` on `mvrv-z-score` and on `etf-flows`, `get_chart` on a full history, on a date range and on weekly granularity, plus four deliberate failures run to see whether the server refuses or invents.

## The tool surface

| Tool | Arguments | What it returns |
|---|---|---|
| `list_charts` | `query` (optional substring, 80 characters) | Every public chart with `id`, title, one-line blurb, category, formula, plus the total count. `query: "sopr"` narrowed **114** charts to **4** (`adjusted-sopr`, `sopr`, `sopr-ratio`, `sth-lth-sopr`). |
| `describe_chart` | `id` (required) | The metric's formula, what it shows, how to read it, caveats, fields with units, input data categories, update cadence, known limitations, data window, analysed block height, methodology URL, metric URL and chart page URL. |
| `get_chart` | `id` (required), `from`, `to`, `granularity`, `includePartial`, `exchange`, `maxPoints` | Historical rows shaped `{t, ...fields}` with the units defined by `describe_chart`. |
| `get_latest` | `id` (required), `exchange` | The most recent point plus the previous point, wrapped in an `asOf` block carrying `lastT`, `publishedAt`, `processedAt` and `analysedBlockHeight`, and a `cite` string. |

## 114 charts, and the category count closes

`list_charts` returned **114** charts, and the per-category counts sum to that total exactly:

| Category | Charts | Category | Charts |
|---|---|---|---|
| Hot Charts | 25 | Realized | 15 |
| Flows & Whales | 23 | Valuation | 11 |
| Holders | 7 | Cross-Asset | 7 |
| Coin Age | 6 | Network | 5 |
| Supply & Issuance | 4 | Value & Volume | 4 |
| Addresses | 3 | Fees | 3 |
| Entities | 1 | **Total** | **114** |

The submission advertises *110+ charts*, so the count is honest and slightly understated. The set covers the metrics an operator would ask for by name (MVRV and its deviation bands, NUPL, SOPR and its adjusted and long-term variants, realized cap and realized price by age band, coin days destroyed, dormancy, Puell multiple, Mayer multiple, NVT, S2F reversion, SSR, spot ETF flows and ETF market cap against new supply) and the ones that exist because an analyst needed a comparison rather than a level (`dxy-vs-btc`, `btc-gold`, `tether-supply-yoy`, `spot-vs-derivative-volume`).

## `describe_chart` is the reason a number can be quoted

`describe_chart` on `mvrv-z-score` returned the working, not just the series:

- **Formula and family:** market cap minus realized cap, divided by the standard deviation of market cap; data family `realized`, source described as `mix · onchain + price`, `onChain: true`.
- **Fields with units:** `mvrvZ` and `mvrvZMa365` in `zscore`, `usd` in `usd`. That is the difference between a table that can be labelled and a table that has to be guessed at.
- **Cadence and coverage:** `updateCadence` is *daily (closed UTC days)*, granularities are `day`, `3day`, `week`, `month` and `year`, and the data window runs from **2009-01-03** to **2026-11-16** on **block height 976,137**.
- **Limitations, in the vendor's own words:** cost basis uses the daily close of the day each output was created rather than the exact trade price, lost or burned coins still count at their creation price, exchange-internal and off-chain transfers are invisible, and BTC/USD prices for 2009 and 2010 are sparse and partly reconstructed so early price-based values are approximate.

A limitation list that names its own weakest interval is worth more than a longer feature list, because the operator can now write the caveat into the note instead of discovering it in a review.

## Two tools, one number

The pair that has to agree is `get_latest` and `get_chart`, and it does. `get_chart` with `from: 2026-11-01` and `to: 2026-11-16` returned **15** rows closing on `2026-11-15`, and the final row is byte-identical to the `latest` block of `get_latest`:

| Field | `get_latest` | Last row of the range |
|---|---|---|
| `t` | 2026-11-15 | 2026-11-15 |
| `usd` | 64,119.34 | 64,119.34 |
| `mvrvZ` | 0.335 | 0.335 |
| `mvrvZMa365` | 0.723 | 0.723 |

The previous point was `2026-11-14` at **0.466** with the price at **68,232.31**, so over one day the price fell **6.03%** (68,232.31 down to 64,119.34) while the z-score fell **0.131** and the one-year average barely moved (**0.726** to **0.723**). An operator quoting *Bitcoin is not in a euphoric regime* now has the number, the definition of the number, and the date it is true for.

## A second chart, checked by subtraction

`get_latest` on `etf-flows` returned the spot ETF line for `2026-11-13`: `netFlowBtc` of **-587.1** against a `cumulativeHeldBtc` of **1,329,077.2**, with the previous point at **-691.8** and **1,329,664.3**. The arithmetic closes: **1,329,664.3** minus **587.1** is **1,329,077.2**, which is the cumulative the next day reports. A flow series that reconciles internally is a series an agent can chain across days without a correction step.

## Resources and prompts

`resources/list` returned **116** items: `kote://catalog` (every chart with formula, fields, input categories and limitations as JSON), `kote://methodology` (sources by category, units, cadence, limitations and citation policy), and **114** per-chart documents at `kote://charts/{id}`. `resources/templates/list` confirms the `kote://charts/{id}` template.

`prompts/list` returned **two**: `explain_metric` (takes a required `id`) and `cycle_position_brief` (no arguments), the latter described as a short sourced read of cycle position using MVRV Z-Score, NUPL, SOPR and exchange flows. Both are editable prompt surfaces a client can invoke without the operator writing the prompt.

## Downsampling, argument names and the defects

Four things are worth knowing before integrating, and three of them are recorded because they were measured rather than read:

- **The required argument is `id`, not `chart`.** A call using `chart` was refused by JSON-schema validation with a message naming `id` as required, which is the correct behaviour and a fast correction for a caller working from prose. The submission text and the vendor's marketing copy both speak about "the chart" rather than the argument name.
- **`additionalProperties: false` is declared but not enforced, and the downsample argument is `maxPoints`.** Two calls passing `points` (**6** and then **100000**) were both accepted and silently dropped, and both returned the default **500** rows. `maxPoints` is documented **10** to **2000** with a default of **500**. Anyone who reads the submission's *downsampled to the points you ask for* and passes `points` will get 500 rows every time and no error, so this is the one place where a caller can be wrong without being told.
- **The running instance is behind its own registry record.** `initialize` reports `kote-analytics` **1.1.0** while the official registry lists **1.1.1** as the latest published version. Nothing measured here failed, but a version skew between the deployed server and its published record is worth knowing when a later call behaves differently from the registry entry.
- **Freshness is per chart, and it is reported honestly.** Both `get_latest` answers were published at **2026-11-16T14:16Z** from the same processing run at **13:53Z** on block **976,137**, yet the MVRV Z-Score ran through **2026-11-15** while spot ETF flows stopped at **2026-11-13**. The `asOf.lastT` field carries the difference, so a caller that always reads `lastT` instead of assuming *today* will not overstate the freshness of the flow line.

The refusals are clean: `get_latest` on an unknown id answered with an error naming the bad id and telling the caller to run `list_charts` to discover valid ones, rather than returning an empty series that reads as a zero or a gap.

## Installation

Claude Code:

```bash
claude mcp add --transport http kote-charts https://kotecharts.com/api/v1/mcp
```

Any client that takes a JSON config:

```json
{"mcpServers": {"kote-charts": {"type": "streamable-http", "url": "https://kotecharts.com/api/v1/mcp"}}}
```

Local stdio bridge for a client that cannot reach a remote server:

```bash
npx -y kotecharts-mcp
```

If the operator would rather call REST directly, the same data is at `https://kotecharts.com/api/v1/public/charts/{id}` behind a free key from `kotecharts.com/account` at **3 requests a second**, and the metric catalog is open at `/api/v1/metrics/{id}` with no key at all. Python (`pip install kotecharts`) and TypeScript (`npm i kotecharts`) clients are published beside it.

## Limitations

- **The data licence is not the code licence.** The repository's code is MIT, but the data served by the site, the REST API and this MCP server is governed by the vendor's terms: free for personal, educational, research and other **non-commercial** purposes, with attribution, and commercial redistribution requires contacting the vendor. Each response carries a `cite` string such as `Kote Charts - "MVRV Z-Score", https://kotecharts.com/c/mvrv-z-score`, and the attribution is part of the licence rather than a courtesy.
- **One asset.** This is Bitcoin on-chain analytics only. There is no Ethereum, no stablecoin supply beyond the Tether comparison chart, and no equity, ETF or macro series except the cross-asset comparisons the catalog names.
- **Heuristic estimates inside a precise-looking surface.** The vendor states that metrics are heuristic estimates, entity labels in particular, and asks that the `limitations` be read before conclusions are drawn. Coverage of exchange and entity attribution depends on clustering heuristics that off-chain flows defeat by construction.
- **Rate limits are the free tier.** **60** requests a minute per IP keyless, or **3** requests a second with a free key on REST. A loop over 114 charts, or a nightly sweep of every metric, will hit the keyless ceiling and needs pacing or a key.
- **The full-history call is downsampled by default.** Asking for a chart with no range returned exactly **500** rows spanning **2010-08-18** to **2026-11-15**, which is even downsampling and not the raw daily series. The catalog's `minDate` of **2009-01-03** is the data window, while the first populated MVRV row is **2010-08-18** because early price data supports values only from there. A caller that needs every day must page with `from` and `to` or raise `maxPoints` to its ceiling of **2000**.

## See Also

- [CryptoStruct Market Data MCP - Historical Crypto & Prediction-Market Data](/hermes/mcp/servers/external/cryptostruct-mcp/) for cross-venue market data where this server carries derived on-chain metrics
- [CryptoExchangeIn MCP - True Trading Cost and Country Rules](/hermes/mcp/servers/external/cryptoexchangein-mcp/) for the trading-cost side of the same asset class
- [World Monitor MCP - Global Intelligence: Markets, Risk, Supply Chains & Procurement](/hermes/mcp/servers/external/world-monitor-mcp/) for macro and cross-asset context beside a single-asset series
