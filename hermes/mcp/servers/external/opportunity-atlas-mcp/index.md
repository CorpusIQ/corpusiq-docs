---
title: "Opportunity Atlas MCP - Northeast Ohio Construction Opportunity Intelligence"
description: "Remote MCP server for verified Northeast Ohio construction opportunity intelligence: free project previews through a hosted endpoint, with registered-agent access to the full project pipeline at capped request rates"
category: Sales & Outreach
stars: n/a (new listing)
added: 2026-08-20
source: mcpservers.org
relevance: ★★
tags: [construction, b2b-opportunities, ohio, project-intelligence, lead-generation, subcontracting, public-beta, remote-mcp]
---

# Opportunity Atlas MCP

**Remote MCP server (Streamable HTTP, registered API key) — verified Northeast Ohio construction opportunity intelligence for AI agents.** Opportunity Atlas distills construction project intelligence for the region into an agent-facing endpoint with a free preview tier: `scout_capabilities` and `scout_preview` work keyless, and registering an agent unlocks the full opportunity surface at capped rates. The operator value is a pipeline feed an agent can watch and act on, instead of a bidding portal a person has to check.

```
Server type: Hosted remote (Streamable HTTP, Supabase function)
Auth: registered agent key (hashed at rest, 90-day expiry)
Endpoint: https://zmxwkvmxcfjgwbrtxxhl.supabase.co/functions/v1/scout-mcp
Tools: 2 free (scout_capabilities, scout_preview) + registered surface
Rate limits: 20 requests/min, 100/day (registered agents)
Pricing: free public beta; no paid services enabled
Category: Sales & Outreach / Construction
Built by: Opportunity Atlas (supabase-hosted, public beta)
```

## Why This Matters for Operators

Construction business development runs on early project signals: who is planning, who won the permit, who needs a sub. The traditional sources are spread across permitting systems, bidding boards, and word of mouth, and the cost of watching them is a person checking portals daily. Opportunity Atlas MCP turns that into an agent-callable feed — `scout_preview` returns free project previews so a sales agent can sample the dataset before committing anything, and `scout_capabilities` tells the agent exactly what the scout covers. A registered agent then works the full pipeline: query opportunities, watch new entries, and route them into a CRM while a human decides which to pursue.

The access model is deliberately careful, which matters for an agent-facing beta: keys are displayed once, stored only as hashes, expire after 90 days, and are capped at 20 requests per minute and 100 per day. No payments exist. That is the right shape for early construction-data plumbing — generous enough to be useful, bounded enough to be safe.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `scout_capabilities` | What the scout covers — regions, project types, and data fields (free, no key) |
| `scout_preview` | Free project previews from the opportunity set (free, no key) |
| Registered-agent tools | Full opportunity search and project detail surface (names served from the endpoint after registration) |

Registration: POST `register_agent` with an agent name to the scout-agent-api endpoint; the key is returned once and must be stored by the operator's agent.

## Installation

```bash
# Register an agent first (key returned once, shown only at registration):
curl -X POST https://zmxwkvmxcfjgwbrtxxhl.supabase.co/functions/v1/scout-agent-api \
  -H "content-type: application/json" \
  -d '{"tool":"register_agent","arguments":{"agent_name":"your-agent-name"}}'

# Connect the MCP endpoint:
claude mcp add opportunity-atlas --transport http \
  https://zmxwkvmxcfjgwbrtxxhl.supabase.co/functions/v1/scout-mcp
```

## Configuration

```json
{
  "mcpServers": {
    "opportunity-atlas": {
      "type": "http",
      "url": "https://zmxwkvmxcfjgwbrtxxhl.supabase.co/functions/v1/scout-mcp"
    }
  }
}
```

Auth note: the free tools answer without a key; registered access requires the one-time key from `register_agent`. Keys expire after 90 days, are capped at 20 requests per minute and 100 per day, and are stored hashed server-side.

## Business Relevance

- **General contractors and subcontractors** in Northeast Ohio get an agent-watchable project feed instead of portal-checking
- **Material suppliers and equipment firms** see project activity early enough to quote before awards
- **Business developers** can sample the dataset free via previews before committing an agent to the full surface
- **Regional service operators** (survey, haulage, restoration) filter for projects matching their trade

## Integration with CorpusIQ

Opportunity Atlas MCP is the top-of-funnel feed for a construction pipeline that CorpusIQ reads at every later stage. The agent pulls new opportunities through the MCP endpoint, qualifies them against the operator's trade and territory, and creates the ones that matter as deals in the CorpusIQ HubSpot or Close connector — the CRM then holds the pursuit, and the CorpusIQ QuickBooks connector tracks the revenue when a project wins. Because the feed is rate-capped and preview-first, the agent can run a daily watch without burning budget. The direction of flow: Opportunity Atlas MCP supplies the project intelligence; CorpusIQ reads the CRM and accounting systems the wins land in.

## Limitations

- Northeast Ohio only — regional scope is the product, not a bug, but it is a boundary
- Free public beta — the full registered surface and tool names are served from the endpoint and may change
- Strict rate caps (20/min, 100/day) and 90-day key expiry mean the agent must cache and schedule, not stream
- Supabase-hosted endpoint — no vendor SLA yet, and no payments layer exists to buy more access
- Brand new listing — no community track record yet

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
