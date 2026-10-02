---
title: Emailchaser MCP - Cold Email Operations for Agents
description: Official Emailchaser connector that exposes a cold-email workspace as 67 MCP tools - launch campaigns, add leads, watch replies and manage webhooks with scoped, revocable API keys at app.emailchaser.com/api/mcp.
category: Sales & Outreach
stars: n/a (new listing)
added: 2026-09-09
source: mcpservers.org
relevance: ★★★
tags: [cold-email, outreach, campaigns, lead-management, sales, email-automation, deliverability, remote-mcp]
---

# Emailchaser MCP

**Remote MCP server (Streamable HTTP, API key)** - the official Emailchaser cold-email connector. It exposes an entire cold-email workspace as 67 hosted tools (as of September 2026) covering campaigns, leads, replies, sender accounts, ICPs, autopilot, blocklist and webhooks, so an agent can launch a campaign from a one-line instruction instead of clicking through a dashboard. Built by Emailchaser (emailchaser.com).

```
Server type: Remote (Streamable HTTP)
Auth: Scoped API key (Settings → Integrations & API); read-only keys supported
Endpoint: https://app.emailchaser.com/api/mcp
Tools: 67 (10 areas - campaigns, leads, replies, sender accounts, ICPs, autopilot, credits, done-for-you infra, blocklist, webhooks)
Pricing: Emailchaser workspace plan applies; MCP itself is hosted at no extra cost
Category: Sales & Outreach
Built by: Emailchaser (emailchaser.com)
```

## Why This Matters for Operators

Cold email still dies in the dashboard: leads in one tab, campaigns in another, replies in a third, and nobody watching between sends. **Emailchaser MCP collapses the whole loop into the agent's conversation** - add 40 leads, launch the campaign, watch replies and pause the two worst performers, all in plain English, with live stats returned so the agent can read, reason, then act.

Every tool call runs through the Emailchaser API under the same authentication, scopes and rate limits as the web app, so an agent can never do more than the key it was given allows. Give the agent a read-only key for analysis, or a scoped write key for campaigns - and revoke either instantly.

## Tools & Capabilities

The vendor publishes the tool count and the ten covered areas; individual tool names are served from the live endpoint. Workflow example published by the vendor: `add_leads` (40 leads added) then `launch_campaign` (running).

| Area | Coverage |
|---|---|
| Campaigns | Create, launch, pause and monitor campaigns |
| Leads | Add, import and manage lead lists |
| Replies | Watch and handle replies |
| Sender email accounts | Manage connected sender inboxes |
| ICPs | Define and maintain ideal customer profiles |
| Autopilot | Run automated campaign flows |
| Credits | Check and manage account credits |
| Done-for-you infrastructure | Manage DFY sending infrastructure |
| Blocklist | Maintain suppression lists |
| Webhooks | Manage webhook endpoints |

## Installation

```bash
claude mcp add emailchaser --transport http https://app.emailchaser.com/api/mcp
```

Then create the API key in Settings → Integrations & API and pass it as a bearer header. The vendor documents Claude Code, Cursor and generic MCP client setup.

## Configuration

```json
{
  "mcpServers": {
    "emailchaser": {
      "type": "http",
      "url": "https://app.emailchaser.com/api/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_EMAILCHASER_API_KEY"
      }
    }
  }
}
```

Keys are scoped and revocable from the Emailchaser dashboard; a read-only key lets the agent analyze without sending.

## Business Relevance

- **Founders** run outbound from chat: launch, monitor and kill campaigns without a dashboard session
- **Sales teams** get live reply rates and campaign stats inside the agent's reasoning loop
- **Growth operators** connect lead sources to campaigns end-to-end with webhook management
- **Agencies** use per-client scoped keys so no client's workspace bleeds into another

## Integration with CorpusIQ

Emailchaser MCP is the outbound half of a CorpusIQ loop: CorpusIQ's CRM and lead sources identify who to contact, Emailchaser runs the campaign and watches the replies, and CorpusIQ's analytics connectors read back which campaigns converted to pipeline. It pairs with the catalogued lead-research servers (Crawdar, YouSpot, Ultimate Web Scraper) - research the list, push it into Emailchaser as leads, launch from the same conversation.

## Limitations

- Requires an Emailchaser workspace and API key
- 67 tools is a vendor-claimed count; names are served from the live endpoint
- Cold-email compliance (spam laws, warming, allowlists) remains the operator's responsibility
- Hosted only - nothing runs locally
- New MCP listing, so no independent track record yet

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
