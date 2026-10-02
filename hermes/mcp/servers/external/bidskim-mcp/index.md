---
title: "BidSkim MCP - UK Tenders and Procurement Intelligence"
description: "Hosted remote MCP over UK public procurement: 8 read-only tools search live tenders, expiring contract renewals with incumbent suppliers, and buyer/supplier profiles across Find a Tender, Contracts Finder, Public Contracts Scotland and Sell2Wales, entity-resolved to one record per opportunity. OAuth 2.1 or an x-api-key header."
category: Compliance
stars: n/a (hosted; docs-only repo)
added: 2026-08-27
source: "mcp.so feed (bidskim-uk-tenders-contract-renewals)"
relevance: ★★★
tags: [procurement, tenders, uk-government, sales-intelligence, public-data, remote-mcp]
---

# BidSkim MCP

**Hosted remote MCP server (Streamable HTTP, OAuth 2.1 or API key) for UK public procurement intelligence.** Eight read-only tools over Find a Tender, Contracts Finder, Public Contracts Scotland and Sell2Wales, entity-resolved and deduplicated to one record per opportunity: keyword/CPV/region/value searches, meaning-based semantic search, full notice detail, expiring contract renewals with incumbent suppliers, buyer and supplier profiles with award histories, and a signed-in pipeline of saved tenders. The endpoint answered a live anonymous initialize with HTTP 401 and full auth instructions (OAuth, or an API key minted in BidSkim Settings sent as an `x-api-key` header), confirming the gate. Official registry name `com.bidskim/mcp`; the server itself is closed-source and hosted - nothing to install.

```
Server type: Remote (Streamable HTTP, stateless; MCP spec 2026-07-28 with 2025-client fallback)
Auth: OAuth 2.1 (RFC 9728 discovery) or API key sent as x-api-key header
Endpoint: https://mcp.bidskim.com/mcp
Registry: com.bidskim/mcp
Tools: 8 (all read-only)
Access: Included with the BidSkim Predict plan
Docs: https://bidskim.com/mcp
Repo: github.com/23shim/bidskim-mcp (public docs, server closed-source)
Category: Compliance
```

## Why This Matters for Operators

Public-sector revenue is a pipeline problem: tenders published across four UK portals in four formats, contract renewals buried in award notices, and incumbent relationships invisible until the notice drops. BidSkim normalizes the entire surface into one entity-resolved record per opportunity, then exposes it to AI agents with tools that answer the money questions directly: which contracts in my space expire in the next six months and who holds them, what has a given buyer awarded recently and to whom, and where does a given supplier already have a footprint. For B2B sales teams, consultancies and public-sector suppliers, this converts procurement research from portal-hopping into agent queries.

## Tools & Capabilities

| Tool | What it answers |
|---|---|
| `search_tenders` | Live and historical tenders by keyword, CPV, region, value, deadline |
| `semantic_search` | "Find tenders like this" - meaning-based search over live tenders |
| `get_tender` | Full detail for one notice, including framework and certification context |
| `search_renewals` | Contracts expiring soon: expiry dates, incumbent suppliers, recurrence evidence |
| `search_organisations` | Find buyers and suppliers by name |
| `get_buyer` | A buyer's award history, spend patterns and top suppliers |
| `get_supplier` | A supplier's wins, buyers served and market footprint |
| `my_pipeline` | The signed-in user's saved tenders and matches |

Typical prompts: "Which contracts in my space expire in the next six months, and who holds them?", "Find live tenders for commercial cleaning in the North West closing this month", "What has Manchester City Council awarded recently, and to whom?"

## Installation

```bash
# Claude Code
claude mcp add -t http bidskim https://mcp.bidskim.com/mcp
```

Claude web/desktop: Settings, Connectors, Add custom connector, paste `https://mcp.bidskim.com/mcp`. Cursor, VS Code, Windsurf and Cline: add a remote MCP server with the same URL - the OAuth sign-in opens in the browser, and signed-in BidSkim users connect with one approval click. Alternatively mint an API key in BidSkim, Settings, Account and send it as the `x-api-key` header.

## Configuration

- **OAuth 2.1 (RFC 9728)** discovery handles most clients; API keys are the fallback for non-interactive agents and CI.
- **Transport:** stateless Streamable HTTP on the 2026-07-28 spec, with fallback for 2025-era clients.
- **Access:** read-only, included with the BidSkim Predict plan. No anonymous or free tier documented.
- **Coverage:** Find a Tender, Contracts Finder, Public Contracts Scotland and Sell2Wales, entity-resolved and deduplicated.

## Business Relevance

- **Public-sector B2B sales teams** build renewal pipelines from `search_renewals` with expiry dates and incumbents, before the tender is republished.
- **Consultancies and bid teams** profile buyers via award history and spend patterns before writing the proposal.
- **Market analysts** map supplier footprints across the UK public sector from a single interface.

## Integration with CorpusIQ

Complements CorpusIQ's business-data connectors with the public-sector demand side: an agent can use CorpusIQ to understand a prospect's own financials and operations, then use BidSkim to find the public-sector opportunities and incumbent relationships relevant to that prospect. Both surfaces are read-only, matching CorpusIQ's connector philosophy.

## Limitations

- UK public procurement only - no EU TED or US SAM.gov coverage in this surface.
- Read-only and account-gated: the full tool list requires OAuth sign-in or an API key; anonymous enumeration is refused by design.
- Closed-source hosted service; the GitHub repo is documentation only, and license/roadmap visibility is limited to the vendor's docs at bidskim.com/mcp.
- Brand new listing (repo created Aug 27, 2026); tool behavior is vendor-documented and 401-verified live, not anonymously probed.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [GovGazette MCP - Federal Contract and Award Intelligence](/hermes/mcp/servers/external/govgazette-mcp)
- [TEOS WARN Act Layoff Intelligence MCP](/hermes/mcp/servers/external/teos-warn-act-mcp)
- [CorpusIQ Connectors](/hermes/mcp/servers)
