---
title: RentSeek Evidence MCP - Executive Compensation with Source
description: "No-auth remote MCP endpoint that returns latest-FY named executive compensation for public companies by ticker or CIK, with pay components, totals and filing source URLs. Two tools: get_executive_compensation and list_available_tickers. Free public endpoint."
category: Finance
stars: n/a (hosted)
added: 2026-08-25
source: "mcp.so GitHub issue #3738"
relevance: ★★
tags: [mcp-server, executive-compensation, proxy-data, finance, research, public-companies]
---

# RentSeek Evidence MCP

**Latest-FY executive compensation, source-linked and free.** RentSeek Evidence is a remote MCP endpoint that returns published annual named-executive compensation rows for public companies, identified by ticker or CIK, with pay components, totals, and the filing source URL for every figure. The public endpoint requires no API key and no credits.

```
Server type: Remote Streamable HTTP
Endpoint: https://rentseek.ing/mcp/public-facts (no auth)
Auth: None on the public endpoint; history, dossiers, and material changes are on
  the authenticated /mcp endpoint
Tools: 2 verified by live probe (get_executive_compensation, list_available_tickers)
Docs: rentseek.ing/developers and rentseek.ing/llms.txt
```

## Why This Matters for Operators

Executive compensation is a core input for investor relations, competitive benchmarking, and governance research, but the raw data lives in DEF 14A filings that are slow to parse by hand. RentSeek Evidence collapses that to a single tool call: ask for a ticker or CIK and get the latest published pay rows with component breakdowns and the exact filing URL for citation. For operators benchmarking comp plans against public peers, or for analysts writing company briefs, every number is traceable to its source document.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `get_executive_compensation` | Returns the latest published annual named-executive compensation rows for a company identified by ticker or CIK, including pay components, totals, and filing source URLs |
| `list_available_tickers` | Returns the ticker symbols for companies with published RentSeek executive-compensation data |

## Installation

No installation required. Connect any MCP client to the public endpoint:

```bash
claude mcp add --transport http rentseek https://rentseek.ing/mcp/public-facts
```

The endpoint is Streamable HTTP and returns plain JSON; standard MCP clients work unchanged.

## Configuration

No credentials for the public endpoint. If you need historical rows, dossiers, or material-change tracking, the authenticated `/mcp` endpoint covers those surfaces; see rentseek.ing/developers for scopes and setup.

## Business Relevance

- **Comp benchmarking:** compare a peer group's named-executive pay structure before setting your own.
- **Investor research:** attach source-linked comp data to company deep dives.
- **Governance screening:** flag unusual pay structures with citation-ready evidence.

## Integration with CorpusIQ

Combine with CorpusIQ's web fetch or research workflows: pull comp rows from RentSeek for a ticker list, then join against financial fundamentals through CorpusIQ connectors or your warehouse for a combined governance and performance view.

## Limitations

- Public endpoint covers the latest fiscal year only; history requires the authenticated endpoint.
- Coverage is limited to companies with published RentSeek data; check `list_available_tickers` first.
- US public-company executive comp only; no private-company or international-equivalent data.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [Candor Finance MCP](/hermes/mcp/servers/external/candor-finance-mcp)
- [Stock Market MCP Server](/hermes/mcp/servers/external/stock-market-mcp-server)
- [FX Macro Data MCP](/hermes/mcp/servers/external/fxmacrodata-mcp)
