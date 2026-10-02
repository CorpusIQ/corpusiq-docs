---
title: "Hilead MCP - Signal-Based B2B Prospecting for Agents"
description: "Remote MCP server for Hilead, a signal-based B2B prospecting platform. An assistant discovers fresh leads from buying signals - funding rounds, key hires, hiring activity, expansion and technology changes - browses audiences, campaigns and companies, and reads reports and reply threads. Launch, send and enrichment stay out of the agent's reach by design. OAuth 2.1 at api.app.hilead.co/mcp, from $49/month."
category: Sales & Outreach
stars: n/a (new listing)
added: 2026-09-14
source: "chatmcp/mcpso issue #4099 + vendor site hilead.co"
relevance: ★★
tags: [sales, prospecting, leads, b2b, gtm, signals, oauth, remote-mcp]
---

# Hilead MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1 with dynamic client registration)** - the agent interface for Hilead, a signal-based B2B prospecting platform. Instead of asking an agent to invent a lead list, Hilead starts from buying signals - funding rounds, key hires, hiring activity, expansion and technology changes - and lets the assistant work that queue: discover fresh leads, browse audiences, campaigns and companies, read campaign reports, analytics and reply threads, and search the existing lead pool. Critically, the dangerous verbs are deliberately absent: campaign launches, message sending and contact enrichment are not exposed, so an agent cannot send on your behalf, burn enrichment credits, or reveal an email or a phone number. The endpoint answers an anonymous initialize with HTTP 401, confirming a live, OAuth-gated server.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 with PKCE and dynamic client registration (scopes: read, read_write)
Endpoint: https://api.app.hilead.co/mcp
Registry: co.hilead/hilead (official MCP Registry)
Tools: capability set documented (discover, browse, read); sending and enrichment intentionally not exposed
Pricing: from $49/month with a 7-day trial
Category: Sales & Outreach
Built by: Hilead (hilead.co)
```

## Why This Matters for Operators

Cold lists go stale the moment they are built; signals do not. The difference between a good week and a wasted one in B2B outreach is usually timing - a company that just raised, just hired a sales leader or just switched its stack is measurably more receptive, and that window is short. Hilead puts signal-led discovery behind the assistant, so building a target list becomes part of the working session rather than a separate tool trip. Two design choices matter for operators. Discovery runs against the live people-discovery provider but is bounded by the workspace quota, a cost cap and a per-call maximum, so an enthusiastic agent cannot blow the budget. And because sending and enrichment are outside the agent's reach, the assistant can research and draft while humans keep control of outbound sends and contact data.

## Tools & Capabilities

| Area | Coverage |
|---|---|
| Lead discovery | fresh leads from buying signals: funding rounds, key hires, hiring activity, expansion, technology changes |
| Pool search | search the existing lead pool with workspace context |
| Browse | audiences, campaigns and companies in the workspace |
| Read | campaign reports, analytics and reply threads |
| Boundaries | campaign launch, message sending and contact enrichment are not exposed to the agent |

Discovery calls are metered by the workspace quota and capped per call; the live tool list is served from the authorized connection.

## Installation

```bash
claude mcp add hilead --transport http https://api.app.hilead.co/mcp
```

Sign in with a Hilead account through the OAuth flow (PKCE with dynamic client registration). The server is published under the official MCP Registry name `co.hilead/hilead`. The `read_write` scope exists for workspace-settings operations; tools that would send or enrich are deliberately out of scope for agents.

## Configuration

```json
{
  "mcpServers": {
    "hilead": {
      "type": "http",
      "url": "https://api.app.hilead.co/mcp"
    }
  }
}
```

## Business Relevance

- **SDR and sales teams** start the day from live signals instead of a static export, with reports and reply threads in the same session.
- **Founders doing their own outbound** build focused lists around funding and hiring triggers.
- **Agencies** run per-client prospecting workspaces with the same guardrails.
- **Revops** keeps cost exposure bounded by the workspace quota and per-call caps.

## Integration with CorpusIQ

Hilead answers "who should we talk to next"; CorpusIQ answers "what do we know about them and how are we doing". An agent can read pipeline, customers and revenue through CorpusIQ (HubSpot, Stripe, QuickBooks) and cross-reference Hilead's signal-led prospects against existing accounts, so outreach focuses on net-new targets and expansion signals rather than the same names the CRM already tracks. The read-focused scope split also composes cleanly with CorpusIQ's read-only connector model: both sides keep writes and sends in human hands.

## Limitations

- Sending is not exposed: pair with your own sequencer or CRM for actual outbound.
- Tool names are not enumerated in the submission; the live list is served from the authorized connection.
- Paid from $49/month after a 7-day trial; discovery is quota- and cost-capped.
- Brand new listing: no public repo and no long track record.
- Signal coverage depends on Hilead's data providers and refresh cadence.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [GoodLeads MCP - New-Business Leads for Agent Outreach](/hermes/mcp/servers/external/goodleads-mcp)
- [MentionAgent MCP - Publisher Outreach and Backlink Placements for Agents](/hermes/mcp/servers/external/mentionagent-mcp)
