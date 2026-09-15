---
title: CN Intel Board MCP - China Hard-Tech Supply Chain
description: "Hosted MCP server serving structured China hard-tech supply chain intelligence: 33 information-gap signals across semiconductors, solid-state batteries, eVTOL, and innovative drugs, an H1 2026 earnings tracker, and natural-language edge Q&A through 6 tools."
category: Data & Analytics
stars: n/a (new listing, github.com/lory69060/cn-intel-board)
added: 2026-08-29
source: "mcp.so GitHub issue #3814"
relevance: ★★
tags: [mcp-server, supply-chain, china, semiconductors, research, market-intelligence, finance, remote-mcp]
---

# CN Intel Board MCP

**A hosted MCP server over China hard-tech supply chain intelligence: structured information-gap signals (semiconductors, solid-state batteries, low-altitude economy and eVTOL, innovative drugs), timestamped prediction and verification records, an H1 2026 earnings tracker, and natural-language edge Q&A.** The project assembles key China supply chain data from public financial reports, company announcements, and industry reports, and marks what mainstream narratives have not noticed - every signal is traceable to source and carries the opposing view. All data is published as machine-readable JSON for agents.

```
Server type: Remote (Streamable HTTP), hosted on Cloudflare Workers
Auth: Bearer token (trial token rate-limited to 200 requests/day)
Endpoint: https://cn-intel-mcp.lory69060.workers.dev/mcp
Tools: 6 (read_signal_board, read_earnings_tracker, get_track_record, ask_edge, list_articles, read_article)
Pricing: Trial token free (200 req/day); listed as finance/supply-chain research
Category: Data & Analytics / Market Intelligence
Built by: lory69060; repo github.com/lory69060/cn-intel-board, license not declared
```

## Why This Matters for Operators

China supply chain questions are expensive to answer manually: what is the actual photoresist localization rate, how do eVTOL battery costs compare with automotive cells, which H1 2026 earnings surprised. The answers live scattered across filings, exchange disclosures, and industry reports, mostly in Chinese, and mostly behind analyst paywalls. CN Intel Board compresses that into a queryable board: 33 high-confidence information-gap signals with strength, basis, and dates, an earnings tracker updated daily through the August reporting season, and a track record of timestamped predictions with verification outcomes.

The ask_edge tool is the operator-relevant surface: natural-language questions about the covered sectors answered from the board's sourced data rather than from model memory. For procurement, competitive intelligence, or investment research teams with China exposure, that is a standing research assistant over a dated, traceable dataset instead of ad-hoc searches.

**China supply chain signals with sourced evidence become a queryable dataset, prediction track record included.**

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| read_signal_board | Read the structured signal board: 33 high-confidence information-gap signals with industry, signal, strength, basis, and date |
| read_earnings_tracker | H1 2026 earnings tracking (forecasts and official disclosures for covered companies, updated daily to Aug 31) |
| get_track_record | Timestamped prediction and verification records for the board's calls |
| ask_edge | Natural-language edge Q&A over the board's sourced data |
| list_articles | List published research notes (Chinese and English) |
| read_article | Read one research note in full |

## Installation

Hosted endpoint - no local install. Request a trial bearer token per the project homepage, then attach it to MCP calls.

```bash
claude mcp add cn-intel --transport http https://cn-intel-mcp.lory69060.workers.dev/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "cn-intel": {
      "type": "http",
      "url": "https://cn-intel-mcp.lory69060.workers.dev/mcp",
      "headers": {
        "Authorization": "Bearer <trial-token>"
      }
    }
  }
}
```

The trial token is rate-limited to 200 requests per day. The endpoint returns 401 without a token, confirming it is live (verified).

## Business Relevance

- **Procurement and supply chain operators** check sourcing-risk signals on semiconductors and batteries against a dated, sourced board.
- **Competitive intelligence teams** get the information-gap framing directly: what the market has not noticed, with the opposing view attached.
- **Investment researchers** follow the H1 2026 earnings tracker during reporting season and audit the board's own prediction track record.
- **Analysts** use ask_edge for quick sourced answers instead of digging through Chinese-language filings.

## Integration with CorpusIQ

CN Intel Board slots into CorpusIQ's research intelligence layer: a CorpusIQ-driven competitive sweep can query read_signal_board and the earnings tracker alongside CorpusIQ's tech-research sweeps and fundable-data sources, so China supply chain signals sit in the same pipeline as Western market data. For operator-facing reports, ask_edge answers feed the same report-rendering path CorpusIQ uses for recap answers, with the board's citations as the evidence block. The prediction-and-verification structure pairs naturally with CorpusIQ's data-driven doctrine - every board claim is timestamped and later verified, which is exactly the attribution discipline CorpusIQ reports require.

## Limitations

- Brand new and single-maintainer - 1 star, no declared license, repo created Aug 11, 2026.
- Trial token is rate-limited (200 requests/day) and commercial terms are not published.
- Coverage is four hard-tech sectors only; it is not a general China market data feed.
- Data is public-source assembly, not primary research - the site states it is informational, not investment advice.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [Jawz MCP - Live Macro Reads and a Disciplined Investing Loop](/docs/hermes/mcp/servers/external/jawz-mcp)
- [Alpha Sophia MCP - US Healthcare Provider and Market Data](/docs/hermes/mcp/servers/external/alpha-sophia-mcp)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
