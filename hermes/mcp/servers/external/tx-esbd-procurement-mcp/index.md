---
title: TX ESBD Procurement MCP - Texas Government Contract
description: "Hosted MCP server over Texas ESBD state procurement data: search, look up, and monitor roughly 60,000 solicitations with structured NIGP commodity codes, an agency dictionary, before and after date windows, and old-value to new-value change tracking, served on the Apify MCP gateway with your own Apify token."
category: Data & Analytics
stars: n/a (Apify-hosted actors)
added: 2026-08-28
source: "mcp.so GitHub issue #3805"
relevance: ★★★
tags: [mcp-server, procurement, government, texas, apify, contracting, remote-mcp]
---

# TX ESBD Procurement MCP

**Remote MCP server over the Texas Electronic State Business Daily (ESBD), the state's procurement portal.** Three tools let an assistant search the full roughly 60,000-solicitation corpus with structured NIGP commodity codes, read one solicitation in detail, and poll a change feed that reports old and new values per field. It runs on Apify's MCP gateway, so auth is your own Apify token and pricing is the underlying actor runs, from $0.01 with capped budgets.

```
Server type: Remote (Streamable HTTP) on the Apify MCP gateway
Auth: Your own Apify API token (sent as a Bearer authorization header)
Endpoint: https://mcp.apify.com?tools=j0401/tx-esbd-search,j0401/tx-esbd-get,j0401/tx-esbd-changes
Tools: 3 (search, detail lookup, change monitoring)
Pricing: Actor runs from $0.01, capped; token via Apify Console
Category: Data & Analytics / Government procurement
Built by: Apify actor publisher j0401
```

## Why This Matters for Operators

State procurement is a standing revenue channel most operators ignore because the ESBD interface is a form-heavy portal built for compliance officers, not for opportunity scanning. This MCP flattens it into a queryable corpus: search by NIGP code or description to find solicitations in your exact commodity category, filter by published-after and published-before windows to build a pipeline of fresh opportunities, and let a change feed watch for amendments instead of manually re-checking listings.

The structured NIGP codes are the differentiator. Raw keyword search over procurement text surfaces noise; NIGP filtering lands on the commodity taxonomy Texas itself uses, so the assistant can say "show me IT services solicitations published since Monday, watch for changes" and get a clean, monitorable list.

**A Texas operator gets a standing government-contract pipeline in one MCP connection.**

## Tools & Capabilities

Capability-level table from the submission and actor documentation; the endpoint requires an Apify token so anonymous enumeration is refused (verified live, 401 with an invalid-token error).

| Tool | Capability |
|---|---|
| tx-esbd-search | Search the full ~60k solicitation corpus: NIGP code filter, description search, agency dictionary, publishedAfter and publishedBefore date windows |
| tx-esbd-get | Full detail lookup for one solicitation |
| tx-esbd-changes | Change monitoring with old and new values per field, for tracking amendments and awards |

## Installation

```bash
claude mcp add tx-esbd --transport http "https://mcp.apify.com?tools=j0401/tx-esbd-search,j0401/tx-esbd-get,j0401/tx-esbd-changes"
```

Create an Apify token in Apify Console under Settings, API and Integrations.

## Configuration

```json
{
  "mcpServers": {
    "tx-esbd": {
      "type": "http",
      "url": "https://mcp.apify.com?tools=j0401/tx-esbd-search,j0401/tx-esbd-get,j0401/tx-esbd-changes",
      "headers": {
        "Authorization": "Bearer <your-apify-token>"
      }
    }
  }
}
```

Set a capped run budget on the token in Apify Console so a runaway search loop cannot exceed your ceiling; the actors price from $0.01 per run.

## Business Relevance

- **Texas operators** find and bid on solicitations in their commodity category instead of relying on portal email alerts.
- **Procurement teams** get structured NIGP-coded searches with date windows for weekly pipeline building.
- **Competitive intelligence** reads the change feed to track amendments and award activity around specific opportunities.
- **Sales teams** use the agency dictionary to identify which state agencies buy in their category and when.

## Integration with CorpusIQ

TX ESBD supplies the opportunity data; CorpusIQ supplies the operational read behind each bid. A composed workflow: the assistant pulls a week of new solicitations in your NIGP category from TX ESBD, then uses CorpusIQ connectors to check QuickBooks cash position and recent HubSpot pipeline before recommending which bids to pursue. Procurement pipeline joined to real business health in one conversation.

## Limitations

- Requires your own Apify token; there is no anonymous tier.
- Capability-level tool table: exact tool schemas require an authenticated session.
- Single-state coverage (Texas only); no federal or other-state data.
- Actor-run pricing accumulates per call; budget caps are the operator's responsibility.
- Change feed reflects ESBD publication cadence, not real-time portal state.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [SAM.gov MCP - US Government Contracting](/hermes/mcp/servers/external/sam-gov-mcp)
- [LiveDataLink MCP - Live Public Data for AI Agents](/hermes/mcp/servers/external/livedatalink-mcp)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
