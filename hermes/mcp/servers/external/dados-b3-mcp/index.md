---
title: "Dados B3 MCP - Auditable Brazilian Stock Fundamentals"
description: "Point-in-time fundamentals for the Brazilian stock market (B3) with public methodology: ROIC, ROE, margins, multiples, dividends and Piotroski F-Scores for 402 listed companies plus Brazilian REIT rankings, every figure traceable to the CVM filing it came from."
category: Finance
stars: n/a (new listing)
added: 2026-08-22
source: "mcp.so GitHub issue #3684"
relevance: ★★★
tags: [stocks, fundamentals, brazil, b3, screener, dividends, remote-mcp]
---

# Dados B3 MCP

**A remote MCP server for auditable fundamentals of the Brazilian stock market (B3), 2010 to today.** Dados B3 serves 14 tools over Streamable HTTP covering 402 listed companies and Brazilian real-estate funds (FIIs), with a property most data vendors only claim: every multiple is point-in-time by construction - the price used is the first trading session after the filing's real publication date, so backtests carry no look-ahead. Endpoint live-probed (server v1.29.0, all 14 tools confirmed). The free tier is keyless.

```
Server type: Remote (Streamable HTTP)
Auth: None for the free tier; chave_api or DADOS_B3_API_KEY for full coverage
Endpoint: https://dadosb3.com/mcp/
Registry: io.github.Val7h/dados-b3
Tools: 14 (companies, annual indicators, point-in-time multiples, dividends, scores, republications, screeners, FIIs, methodology)
Pricing: Free tier (WEGE3 and full methodology open); free or paid keys for other companies
Built by: Val7h (dadosb3.com); repo github.com/Val7h/dados-b3-mcp, MIT
```

## Why This Matters for Operators

Brazilian fundamentals data is notoriously messy: restated balance sheets, filings that change after publication, and multiples computed with prices from before the numbers were public. **Dados B3 makes every figure traceable back to the CVM account it was derived from, and publishes the formula for each indicator instead of describing it.** The `reapresentacoes` tool even surfaces republished balance sheets, showing when a company quietly changed a number between the original filing and the republication.

For analysts and operators running screeners or backtests, the point-in-time design is the point of the project: a multiple is never computed with a price from before the balance sheet was public. Piotroski F-Scores come with each of the nine criteria auditable, not just the final number.

## Tools & Capabilities

All 14 tools verified live against dadosb3.com/mcp/ (server v1.29.0).

| Tool | Purpose |
|---|---|
| `listar_empresas` | List the 402 available Brazilian listed companies (name, CNPJ, ticker); free, no key |
| `indicadores_anuais` | Annual series (2010-today) of ROIC, ROE, margins, growth and net debt/EBITDA per company |
| `multiplos` | Point-in-time multiples (annual P/E, P/BV, EV/EBITDA; quarterly TTM P/E) priced on the first session after each filing's publication |
| `dividendos` | Cash payout history (dividends and JCP): per-share value, approval date, ex-date |
| `scores` | Ready-made fundamental scores with open math: Piotroski F-Score (0-9, each criterion auditable) plus criteria detail |
| `reapresentacoes` | Republished balance sheets: which numbers changed between a company's original filing and its republication |
| `fatos_contabeis` | Standardized accounts (revenue, EBIT, profit, equity, debt, cash) with the source CVM account for each number |
| `metodologia` | Public indicator methodology; lists pages, or returns full text by name (e.g. 'roic') |
| `dicionario` | Indicator methodology as JSON: formula, CVM accounts and the profit base for each |
| `screener` | Filter the 402 companies by indicator ranges (e.g. roic_min 0.15, dl_ebitda_max 2) |
| `fiis_ranking` | Brazilian REIT (FII) rankings: most discounted by P/BV, top 12-month dividend payers, P/BV median |
| `fii` | Detail for one FII: registration, latest report (unitholders, equity, period), point-in-time P/BV history |
| `screener_fiis` | Filter FIIs by ranges (pvp_max, dy_min, segment, unitholder counts) |
| `saude` | Database coverage counts and last ingestion date; free |

## Installation

```bash
claude mcp add --transport http dados-b3 https://dadosb3.com/mcp/
```

The free tier works with no key: WEGE3 and the whole methodology are open. Other companies need a key issued at dadosb3.com (the free key requires no card).

## Configuration

```json
{
  "mcpServers": {
    "dados-b3": {
      "type": "http",
      "url": "https://dadosb3.com/mcp/",
      "headers": {
        "Authorization": "Bearer chave_api"
      }
    }
  }
}
```

The key is passed as `chave_api` or the `DADOS_B3_API_KEY` environment variable.

## Business Relevance

- **Equity analysts** run point-in-time screeners across 402 Brazilian companies without look-ahead contamination
- **Fund managers and family offices** rank 179 liquid Brazilian REITs by P/BV and 12-month dividend yield
- **Compliance and audit teams** trace every figure back to its CVM source account and catch quiet restatements
- **Backtest builders** get series that are point-in-time by construction, not by post-processing

## Integration with CorpusIQ

Dados B3 is the Brazilian equity layer; CorpusIQ is the books-and-traffic layer. An analyst can screen B3 companies in Dados B3, then read portfolio cash flows from Stripe and QuickBooks through CorpusIQ connectors to model position sizing against real liquidity. Funds tracking Brazilian exposures can pair Dados B3 fundamentals with CorpusIQ's GA4 and HubSpot reads to correlate their own investor funnel with market conditions - or simply keep one audit trail across external market data (Dados B3) and internal business data (CorpusIQ).

## Limitations

- Brazil-only coverage (B3 listed companies and FIIs)
- Brand new listing (Aug 2026); repo created Aug 2026 with no stars yet
- Free tier covers one company (WEGE3) plus methodology; full coverage needs a key
- Portuguese tool names and descriptions - agents need the `dicionario`/`metodologia` tools to map indicators correctly
- Single maintainer project (Val7h), MIT license

## See Also

- [Signal Nodus SEC Filings MCP](/hermes/mcp/servers/external/signal-nodus-mcp/)
- [AskRentAI MCP](/hermes/mcp/servers/external/askrentai-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
