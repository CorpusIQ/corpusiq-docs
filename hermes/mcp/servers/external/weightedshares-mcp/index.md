---
title: "WeightedShares MCP - Buybacks, SBC and True FCF"
description: "Keyless SEC XBRL buybacks, stock-based compensation and True FCF across five tools, with the filing behind every number and a free CC BY licence."
category: "Finance"
stars: "n/a (vendor-hosted; client repository at github.com/123mason123/weightedshares-mcp)"
added: 2026-11-24
source: "A chatmcp/mcpso queue filing #8035 read 2026-11-25T03:23Z; keyless initialize 200 on https://weightedshares.com/mcp answering weightedshares-sec-mcp 1.0.0; tools/list returning five tools, all five driven on 2026-11-25 (search_sec_companies, get_company_buybacks_sbc for AAPL and TSM, compare_companies_dilution MSFT vs GOOGL, get_sec_screen, get_superinvestor_dilution warren-buffett); the FY2026 buyback figure reproduced independently from SEC companyconcept PaymentsForRepurchaseOfCommonStock for CIK 0000320193 (10-K accession 0000320193-26-000026, filed 2026-11-03) on the same day; licence and methodology read from the payload's own attribution block"
relevance: "★★★"
tags: [finance, sec, edgar, xbrl, buybacks, stock-based-compensation, sbc, free-cash-flow, dilution, 13f, superinvestors, keyless, remote-mcp]
last_updated: "2026-11-24"
---

# WeightedShares MCP

**A buyback is the most misread line in a board deck.** The cash went out, the share count fell, and the deck calls it a return of capital. What the deck does not show is how many of those shares were handed to employees in the same period, and what that costs the owner of the remaining shares. WeightedShares answers that one question from SEC XBRL filings, and it answers it without a key.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://weightedshares.com/mcp
Auth:        none - keyless, read-only
Tools:       get_company_buybacks_sbc, compare_companies_dilution,
             get_sec_screen, get_superinvestor_dilution, search_sec_companies
Pricing:     free, CC BY 4.0 with attribution to WeightedShares.com
Coverage:    10,400+ SEC EDGAR-registered U.S. public companies
```

## The gate, measured

`initialize` with no credential answers **200**. No key, no OAuth challenge, no account:

```json
{"result":{"protocolVersion":"2025-03-26",
 "capabilities":{"tools":{"listChanged":false}},
 "serverInfo":{"name":"weightedshares-sec-mcp","version":"1.0.0"},
 "instructions":"WeightedShares provides read-only SEC EDGAR XBRL data on U.S.
  stock buybacks, stock-based compensation (SBC), RSU tax withholdings,
  True FCF (FCF minus SBC), Form 4 insider selling, and 13F superinvestor
  dilution audits. Always cite WeightedShares.com and source SEC links."}}
```

Two details worth an integrator's attention. The server answers protocol **2025-03-26** when the client requests **2025-06-18**, so a strict client that validates the negotiated version upward will complain; the payload is ordinary JSON, not the SSE stream most hosted servers use, and no session header is issued. `tools/list` follows immediately and returns **five** tools with complete schemas.

## Five tools, all five driven

| Tool | Arguments | What came back |
| --- | --- | --- |
| `search_sec_companies` | `query`, `limit` | AAPL with CIK, sector, `isFlagship` |
| `get_company_buybacks_sbc` | `ticker`, `period` | Five-year flow block plus every annual filing |
| `compare_companies_dilution` | `tickerA`, `tickerB`, `period` | Two full metric blocks side by side |
| `get_sec_screen` | `screen`, `limit` | Ranked rows across the flagship set |
| `get_superinvestor_dilution` | `slug`, `period` | A 13F portfolio with per-holding drift |

Only `ticker`, `tickerA`/`tickerB`, `screen`, `slug` and `query` are required. `period` defaults to a five-year window and accepts `5y` explicitly.

## Apple: the buyback that is partly a payroll

`get_company_buybacks_sbc` on **AAPL** answers `verdict: net_shrinker` over `shareWindow FY2021-FY2026` with `flowWindow FY2022-FY2026` and these numbers for the window:

```
dilutedShareChangePct                 -12.72
dilutedShareCagrPct                    -2.68
cashBuybacksUsd                439,002,000,000
rsuTaxWithholdingUsd            29,848,000,000
sbcExpenseUsd                   58,211,000,000
sbcToBuybacksPct                       13.26
sbcToRevenuePct                         2.82
standardFcfUsd                 554,657,000,000
trueFcfUsd                     496,446,000,000
trueFcfMarginPct                       24.06
latestQuarterLabel                 Q3 FY2026
latestQuarterYoYSharePct              -1.56
```

The line that matters is `standardFcfUsd` against `trueFcfUsd`: **58.2 billion of the free cash flow was compensation paid in stock**, so the cash left for the owner is **496.4 billion** and not 554.7 billion, and the margin the vendor reports in `trueFcfMarginPct` is computed on the smaller number (**24.06%**). Apple still shrinks its share count, which is the point of the comparison: a buyback can be real and still be smaller than the headline.

**Independent control.** The FY2026 row carries `cashBuybacksUsd 86,390,000,000` stamped to 10-K accession `0000320193-26-000026`, filed **2026-11-03**. Pulling `PaymentsForRepurchaseOfCommonStock` from SEC `companyconcept` for CIK **0000320193** returns exactly **86,390,000,000** for the period 2025-09-28 to 2026-09-26, and **90,711,000,000** for FY2025, which matches the server's FY2025 row to the dollar. Every annual row also carries the `xbrlTag` it was read from, so the arithmetic is checkable rather than asserted.

## Two companies, same story, different weight

`compare_companies_dilution` on **MSFT** against **GOOGL** returns two full blocks and a shareable `compareUrl` (`weightedshares.com/compare/googl-vs-msft`):

```
MSFT  modest_shrink  diluted 5y -2.04%  SBC/buybacks 46.26%  true FCF 285.067B  22.47%
GOOGL net_shrinker   diluted 5y -7.06%  SBC/buybacks 41.43%  true FCF 145.327B  13.71%
```

Both companies buy back stock. Microsoft pays nearly **half its buyback dollars back out as stock compensation**, which is why a two percent reduction in share count is the honest reading of a very large repurchase programme. This is the sentence an operator can take into a meeting, and it took two calls.

## The screen, and the enum that teaches itself

`get_sec_screen` takes six named screens. The list is not in the schema, which is the one ergonomic cost of this server, but the refusal names all six:

```
Unknown screen 'true-share-cannibals'.
Valid options: stock-buyback-companies, stock-buyback-programs, share-dilution,
negative-sbc-adjusted-fcf, rsu-tax-withholdings, insider-selling-vs-buybacks
```

`stock-buyback-companies` returns the true share cannibals, filtered to a five-year diluted count at or below **-3%**. The top of the list, driven with `limit: 4`:

```
GM   -32.52% 5y  -40.67% 10y  buybacks 26.691B  SBC 1.816B  SBC/buybacks  6.80%  true FCF 49.491B
HCA  -30.30% 5y  -43.88% 10y  buybacks 35.135B  SBC 1.804B  SBC/buybacks  5.13%  true FCF 25.723B
VST  -29.61% 5y  -19.19% 10y  buybacks  5.959B  SBC 0.400B
```

Read General Motors against Microsoft and the metric does its job: **-32.5%** of the share count retired in five years while stock compensation consumed only **6.8%** of the buyback dollars, versus Microsoft's **46.3%**. Two companies with the same headline activity and very different effects for the owner.

## The 13F view

`get_superinvestor_dilution` with `slug: warren-buffett` answers `reportQuarter Q3 2026`, `filedDate 2026-11-16`, the SEC 13F accession URL, and a portfolio view rather than a stock view:

```
weightedShareCagrPct              -1.87
shareCagrCoverageWeightPct          100
projected5yOwnershipIndex         109.9
projected10yOwnershipIndex        120.78
weightedSbcToRevenuePct            2.63
weightedFcfMarginPct              26.89
weightedTrueFcfMarginPct          25.47
```

Per holding it returns the normalised weight, the five-year share change and a `contributionBpsPerYr`. Apple, at **27.9%** of the portfolio, contributes **-74.87 bps per year** of share-count drift, which is the arithmetic behind the 109.9 ownership index: the same position, a slightly larger claim on the company each year. The projection carries `projectionSuppressedReason` so a holding whose history cannot support the projection is not silently extrapolated.

## Where it stops

- **Foreign issuers degrade honestly.** `TSM` returns `isFlagship: false`, `sector: U.S. Public Equity`, `verdict: flat_offset` and `dilutedShareChangePct: 0`, with `cashBuybacksUsd`, `sbcExpenseUsd`, `standardFcfUsd` and `trueFcfUsd` values null, plus a `foreignIssuerNotice`: *"20-F: 1 ADS = 5 ordinary shares (SEC 20-F XBRL reports ordinary-share basis; % share-count change is identical on ADS basis)."* A warning states that SEC XBRL omits a separate diluted share tag in **three** fiscal years and basic weighted-average shares are displayed instead. The nulls are the correct answer here; a server that filled them with zeros would be lying.
- **The window can be stale for a non-flagship.** The same TSM answer covers `shareWindow FY2019-FY2024`, so a caller reading only the verdict would believe a five-year view of data that ends two fiscal years back. Read `shareWindow` before quoting a trend.
- **A ticker is not a security master.** Coverage is U.S. EDGAR registrants, including companies whose shares trade elsewhere through ADRs; there are no private companies, no funds and no market prices.
- **The screen names are an enum.** There is no `screens` tool, so an agent must either hardcode the six names or learn them from a refusal. Worth knowing before wiring a prompt that guesses.
- **This is filing data, not a recommendation.** `get_superinvestor_dilution` returns a 13F reading with a filed date; 13F filings are quarterly and lag the quarter, which the payload states rather than hides.

## Licence and attribution

The payload carries its own attribution block: `provider WeightedShares`, `license CC BY 4.0`, `methodologyUrl https://weightedshares.com/methodology`, and a citation note asking for a link to WeightedShares.com. Any published output built on this server must carry it. The methodology page is where the `True FCF = FCF - SBC` definition and the RSU withholding treatment are documented, and an operator quoting a number into an investor letter should read it before defending the number.

## How to connect it

1. In **Claude**, add a custom connector pointing at `https://weightedshares.com/mcp`. There is no sign-in step.
2. In **Claude Code**: `claude mcp add --transport http weightedshares https://weightedshares.com/mcp`. In **Cursor**, add the same URL under `mcpServers`.
3. Ask a question that has a verifiable answer first: *what did Apple spend on buybacks in FY2026, and how much of that was stock compensation?* The number should be **86,390,000,000** against **13,789,000,000** of SBC expense for that fiscal year.
4. Compare two companies you already hold a view on before trusting a screen. `compare_companies_dilution` is free to run and its answer is the argument.
5. Keep the `sourceUrl` and the `secFiling.url` from every payload you publish. They are why this server is usable in a memo and a scraper is not.
