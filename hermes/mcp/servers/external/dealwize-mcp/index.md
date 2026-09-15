---
title: "Dealwize MCP - B2B Deal Intelligence for AI Agents"
description: B2B deal intelligence for sales teams - deal health analysis, stakeholder and risk surfacing, Mutual Action Plans and Dealboards built from meeting transcripts, served to any MCP client
category: Sales & Outreach
stars: n/a (new listing)
added: 2026-09-04
source: "mcp.so feed"
relevance: ★★★
tags: [deal-intelligence, b2b-sales, sales-intelligence, meddic, mutual-action-plans, crm, remote-mcp]
---

# Dealwize MCP

**Remote MCP server (Streamable HTTP, OAuth) for B2B deal intelligence - deal health, stakeholder maps, risk surfacing, North Star and next-step actions over live sales opportunities.** Built for Account Executives, Sales Leaders, Founders and revenue teams working complex B2B deals. Instead of exposing raw CRM records, Dealwize analyses the context of an opportunity and surfaces the insight plus the action that moves it forward. Listed in the MCP registry as `co.dealwize/dealwize`.

```
Server type: Remote (Streamable HTTP, SSE also available)
Auth: OAuth browser sign-in, or Bearer API key (dw_live_)
Endpoint: https://api.dealwize.co/api/v1/mcp
Tools: Capability surface per vendor docs (live tool list served from the endpoint)
Pricing: Requires a Dealwize account (dealwize.co)
Category: Sales & Competitive Intelligence
Built by: Dealwize
```

## Why This Matters for Operators

The pre-call homework that decides whether a complex deal closes - who really matters, what could derail it, and what the single most important next action is - usually lives in the AE's head and three disconnected tools. Dealwize compresses it into one endpoint an agent can call mid-conversation. The deal-health read is the operator-friendly part: ask "what could stop my Acme deal from closing" and get risks, gaps and the stakeholders you are missing, instead of re-reading your CRM notes.

**Mutual Action Plans and Dealboards make the deal motion explicit.** Dealwize builds them from sales conversations and transcripts, so the plan of record is derived from what was actually said - not what someone remembered to type into a spreadsheet afterwards. MEDDIC-style deal qualification becomes a query, not a ritual.

## Tools & Capabilities

The listing reports no live-extractable tool list - capabilities below are from the vendor's published overview; the live tool list is served from the endpoint.

| Capability | What it does |
|---|---|
| Deal health analysis | Understand deal health and the factors affecting an opportunity |
| Stakeholder identification | Identify key stakeholders and who is missing from the buying decision |
| Risk and gap surfacing | Surface risks and gaps that could prevent progression |
| North Star | Find the critical outcome required to progress and win |
| Deal strategy review | Review strategy using the context captured in Dealwize |
| Mutual Action Plans | Work with MAPs and the activities required to move the deal forward |
| Dealboards | Create and update Dealboards from sales conversations and transcripts |

Example prompts: "Who are the key stakeholders, and who are we missing?", "What's the most important thing I should do next?", "Give me the brutal truth about this opportunity."

## Installation

```bash
claude mcp add dealwize --transport http https://api.dealwize.co/api/v1/mcp --header "Authorization: Bearer dw_live_YOUR_API_KEY"
```

The same endpoint works in Claude Code, Codex, Cursor, VS Code and any Streamable HTTP MCP client.

## Configuration

```json
{
  "mcpServers": {
    "dealwize": {
      "type": "http",
      "url": "https://api.dealwize.co/api/v1/mcp"
    }
  }
}
```

On first connect the client opens a browser window for OAuth sign-in and reuses the credentials for later sessions. For headless flows, mint an API key at Dealwize → Settings → Integrations and pass it as a Bearer header.

## Business Relevance

- **Founders and revenue leaders** get a standing deal-review function inside their agent - every pipeline opportunity can be interrogated for risks, stakeholders and next actions before a forecast call
- **Account Executives** replace fragmented deal notes with a single source of truth their agent reads and updates, including Dealboards generated from call transcripts
- **Sales managers** run deal health checks across the pipeline without manual CRM archaeology

## Integration with CorpusIQ

CorpusIQ connects your own business systems (HubSpot, Salesforce-style CRM data, commerce, finance) as read-only context. Dealwize adds the deal-strategy layer on top: opportunity risks, stakeholder maps and Mutual Action Plans. Together they give an agent both sides of a revenue decision - internal pipeline reality from CorpusIQ connectors, deal-level strategy and next actions from Dealwize - in one conversation.

## Limitations

- Brand new listing - no track record yet
- No public tool list; capability names may differ from live tools
- Requires a Dealwize account; no self-host option
- Cloud-only - deal data leaves your CRM instance

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [Klarix Intelligence Engine MCP - B2B Competitive Intelligence](/docs/hermes/mcp/servers/external/klarix-intelligence-engine-mcp)
- [Apollo.io MCP - Lead Search and Contact Enrichment](/docs/hermes/mcp/servers/external/apollo-io-mcp)
- [CampaignStack MCP - Safe LinkedIn and Email Outreach](/docs/hermes/mcp/servers/external/campaignstack-mcp)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
