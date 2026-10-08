---
title: "Rivalize MCP - Competitor Teardowns for Agents"
description: "Competitive intelligence for agents: one-call teardowns of a competitor's positioning, pricing, ads, social, reviews, hiring and momentum, cited."
category: Competitive Intelligence
stars: n/a (new listing)
added: 2026-10-08
source: "mcpservers.org /all + mcp.so feed (October 8, 2026 midday sweep)"
relevance: ★★★
tags: [competitive-intelligence, competitor-analysis, market-research, pricing, marketing, battlecards]
---

# Rivalize MCP

**Local MCP server that turns your assistant into a competitive analyst** - tear down a competitor's go-to-market in one call, search the Rivalize universe of tracked companies, and read the projects, reports, battlecards, timelines and evidence in your own account. Thirteen read-only tools plus one opt-in write, every answer sourced and dated.

```
Server type: Local stdio (npx -y @rivalize/mcp)
Auth: Rivalize account + API key (rk_live_..., created in Dashboard > Settings > API Keys)
Package: @rivalize/mcp v0.3.2 on npm (MIT, repo Downshift/rivalize-mcp, MCP Registry entry in server.json)
Tools: 13 read-only + add_competitor (opt-in write via RIVALIZE_MCP_ALLOW_WRITES=1)
Runtime: Node.js 22+
Category: Competitive Intelligence
Built by: Downshift (rivalize.ai)
```

## Why This Matters for Operators

Founders and marketing teams lose hours every week checking what competitors changed: a pricing page, new ads, review sentiment, hiring, momentum. Rivalize collects that continuously, and this server puts it in the chat: a sourced teardown on demand, a landscape view of a market, and sales battlecards your team can quote - with evidence links and freshness dates back to the source, not a model's memory of the space.

## Tools & Capabilities

| Group | Tools |
|---|---|
| Teardown | `teardown_competitor` - one-call strategy read of any domain as Markdown: positioning, pricing, ads, social, reviews, hiring, momentum, weaknesses to attack, with when the data was last refreshed |
| Universe | `list_universe_companies` and `get_universe_company` - search and read the cross-customer dataset of tracked companies (identity, pricing, features, ads, social, reviews, funding, hiring, rankings, signals, momentum) |
| Account reads | `list_projects`, `list_reports`, `get_report` (by section: tldr, biggest-threat, blind-spots, actions, battlecards, competitors, pricing, momentum, ads, tech-stack and more), `list_competitors`, `get_competitor_intelligence`, `get_battlecard`, `get_strategic_timeline`, `get_competitive_landscape`, `get_freshness`, `get_evidence` |
| Write (opt-in) | `add_competitor` - queue 1-10 competitor URLs for analysis; spends credits and only exists for the client when `RIVALIZE_MCP_ALLOW_WRITES` is set |

## Installation

```bash
claude mcp add rivalize -e RIVALIZE_API_KEY=rk_live_your_key -- npx -y @rivalize/mcp
```

```json
{
  "mcpServers": {
    "rivalize": {
      "command": "npx",
      "args": ["-y", "@rivalize/mcp"],
      "env": { "RIVALIZE_API_KEY": "rk_live_your_key" }
    }
  }
}
```

Create an account at rivalize.ai, create an API key under Dashboard > Settings > API Keys, and paste the key into your client's env block. A key from any plan works, including the free plan, which gets rate-limited reads.

## Configuration

- Long responses stay under 25,000 characters with explicit paging: reports split at section boundaries with "Page N of M" and lists return `pagination.next_offset`; nothing is cut silently.
- Provenance is first-class: `get_evidence` returns the URL, the claim it supports and when it was read; `get_freshness` reports when each tracked competitor was last actually observed. Claims the report's fabrication check removed appear as [removed - unverified].
- Artifact check (October 8, 2026): npm serves @rivalize/mcp v0.3.2, the repo Downshift/rivalize-mcp is published under MIT with the MCP Registry manifest in `server.json`, and there is no hosted endpoint - the server runs locally over stdio.

## Example Prompts

- "Tear down linear.app and list the three weaknesses we can attack this quarter."
- "Who are the players in AI developer tools? Rank them by momentum."
- "Show me my competitors' pricing from the latest report, with sources."
- "Give me sales talking points against my top competitor."

## Integration with CorpusIQ

Rivalize reads the outside market; CorpusIQ keeps your own numbers straight. Ask for a competitor pricing teardown from Rivalize and your revenue, customers and pipeline from Stripe, Shopify or HubSpot in the same conversation - outside intelligence plus your cited business data, one chat, no exports.

## Limitations

- Requires a Rivalize account; the API key starts with rk_live_. The free plan is rate-limited and battlecards need a Pro plan.
- Adding a competitor spends credits and queues analysis - it is the only write tool, and it is off by default.
- Coverage is limited to companies Rivalize tracks or accepts; very small or private firms may have thin data.
- Local stdio server: the client machine needs Node.js 22+ and network access on first run (the npx download).

## FAQ

### Does the agent change anything in my account?

No by default. The thirteen read-only tools never modify anything; `add_competitor` is the single write tool and it does not exist for the client unless you set `RIVALIZE_MCP_ALLOW_WRITES`.

### Where does the competitive data come from?

Rivalize's own collection pipeline. Every answer carries dates and sources through `get_evidence` and `get_freshness`, and claims that fail the report's fabrication check are explicitly marked [removed - unverified].

### Can it be used without CorpusIQ?

Yes - Rivalize MCP is an independent server. CorpusIQ is one convenient way to combine market intelligence with your own business numbers in the same chat.

## See Also

- [Debriefing MCP - Competitor Moves with Evidence](/hermes/mcp/servers/external/debriefing-mcp/)
- [Signal Six MCP - Cited Competitive Intelligence](/hermes/mcp/servers/external/signal-six-mcp/)
- [Klarix Intelligence Engine MCP - B2B Competitive Intelligence](/hermes/mcp/servers/external/klarix-intelligence-engine-mcp/)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
