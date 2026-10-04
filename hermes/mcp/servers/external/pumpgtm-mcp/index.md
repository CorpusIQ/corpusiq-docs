---
title: PumpGTM MCP - AI SDR Outreach for Agents
description: Hosted MCP that finds buyers showing intent and runs LinkedIn, email and X outreach from your own accounts, handing every reply back to a human.
category: Marketing
stars: n/a (new listing)
added: 2026-10-04
source: mcpservers.org
relevance: ★★★
tags: [marketing, sales, gtm, outreach, linkedin, lead-generation, remote-mcp, oauth]
---

# PumpGTM MCP

**Hosted MCP server (Streamable HTTP, OAuth 2.1 or workspace key)** - the official PumpGTM server that turns an AI client into an SDR scoped to one workspace. It finds buyers showing intent this week, drafts and sends LinkedIn, email and X outreach from the team's own accounts inside each platform's limits, and hands every reply back to a human. The dashboard is API-first, so everything it does is available through MCP.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 (DCR + PKCE) or a workspace key
Endpoint: https://mcp.pumpgtm.com/mcp
Tools: Buyer-intent discovery, LinkedIn/email/X outreach, reply handoff (full schema at /mcp/tools.json)
Pricing: PumpGTM workspace plan
Category: Marketing
Built by: PumpGTM
```

## Why This Matters for Operators

Outbound breaks when the operator is the bottleneck between "who should I talk to" and "send the message." PumpGTM's mechanism is a **single governed pipeline**: the agent identifies intent-signalled buyers, drafts and sends outreach from the team's own accounts while respecting each platform's sending limits, and routes every reply back to a person rather than auto-answering.

For founders and sales operators, that means outbound runs continuously without tool-switching or a dozen browser tabs, and human attention lands only where a reply exists. Because the server is scoped to one workspace and sits behind OAuth, access stays bounded to the accounts and limits the team has configured.

**The key advantage is intent-to-outreach automation that runs from your own accounts and stops at the human reply.**

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| Buyer discovery | Surfaces buyers showing intent for the week |
| Outreach | Drafts and sends LinkedIn, email and X messages from your own accounts |
| Reply handoff | Returns every reply to a human instead of auto-replying |
| Workspace reads | Everything in the dashboard, scoped to one workspace |

The live tool schema is mirrored at pumpgtm.com/mcp/tools.json, and a REST API covers the same workspace.

## Installation

```bash
claude mcp add --transport http pumpgtm https://mcp.pumpgtm.com/mcp
```

OAuth 2.1 with dynamic client registration covers Claude, Claude Code, Codex, Cursor and ChatGPT; a workspace key covers custom agents. Access tokens last 30 days, refresh tokens 90.

## Configuration

```json
{
  "mcpServers": {
    "pumpgtm": {
      "type": "http",
      "url": "https://mcp.pumpgtm.com/mcp"
    }
  }
}
```

OAuth metadata is published at pumpgtm.com/.well-known/oauth-authorization-server. Platform limits are enforced by PumpGTM, not left to the caller.

## Business Relevance

- **Founders and solo GTM** can run outbound without hiring an SDR or babysitting three tools.
- **Sales teams** get intent-ranked buyers and platform-safe sending from their own accounts.
- **Agencies** can run outbound per client workspace via the platforms endpoint.
- **Growth operators** can pair outreach with their own analytics to see what converts.
- **RevOps** keeps access bounded: one workspace, OAuth-scoped, replies always human.

## Integration with CorpusIQ

PumpGTM is the outreach engine downstream of CorpusIQ's pipeline data. Where CorpusIQ holds the CRM-shaped lead pipeline and analytics (HubSpot, GA4, Stripe), PumpGTM turns the qualified slice into live outreach, so an assistant can go from "these accounts fitted the ICP and visited pricing" to "here is the draft and the send status."

A composed workflow: pull a qualified segment from CorpusIQ's lead pipeline, have PumpGTM find intent-matched buyers and draft outreach from the team's accounts, then write results back so the assistant can report reply rates alongside conversion. CorpusIQ reads the funnel; PumpGTM works the top of it.

## Limitations

- Requires a PumpGTM workspace plan; not a free surface.
- Sending respects each platform's limits, which caps volume by design.
- Hosted and proprietary; no self-hosting.
- Human-in-the-loop by design: replies are handed back, not auto-answered.
- Best value when the team already sends outbound from real accounts.

## FAQ

### Does PumpGTM auto-reply to prospects?

No. It drafts and sends outreach, then hands every reply back to a human.

### Which channels does PumpGTM cover?

LinkedIn, email and X, sent from the team's own accounts within platform limits.

### How do I authenticate PumpGTM?

OAuth 2.1 with dynamic client registration for major clients, or a workspace key for custom agents.

### Can agencies run multiple clients?

Yes. A platforms endpoint is documented for agencies and platforms running many workspaces.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
