---
title: "One MCP — One Hosted Server for Gmail, Slack, Stripe, Shopify, HubSpot and More"
description: "Hosted MCP server connecting AI agents to the apps teams already use — Gmail, Slack, Stripe, Shopify, HubSpot, Notion, Linear, Salesforce, QuickBooks and more — through one OAuth sign-in with no API keys to manage. Actions are discovered on demand with their real API documentation."
category: Integration & Automation
stars: n/a (new listing)
added: 2026-08-21
source: mcp.so
relevance: ★★★
tags: [integration, oauth, automation, multi-app, crm, payments, productivity, remote-mcp]
---

# One MCP

**One hosted MCP server, one OAuth sign-in, every app the team already uses — no API keys to manage and no per-platform SDKs to learn.** One (withone.ai) connects agents to Gmail, Slack, Stripe, Shopify, HubSpot, Notion, Linear, Salesforce, QuickBooks and more through a four-tool discovery-and-execute model: the agent lists what the user has connected, searches the platform's action catalog, reads the action's knowledge document, then executes. Every action is scoped by the grant the user approved, so the agent works from each platform's actual schema instead of a guess.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (user:connections:read / user:connections:write scopes)
Endpoint: https://mcp.withone.ai/mcp
Tools: 4 (discovery + execution model)
Pricing: not published on listing
Category: Integration & Automation
Built by: withone.ai (github.com/withoneai/mcp)
```

## Why This Matters for Operators

The classic multi-app agent setup means minting API keys in ten dashboards, pasting them into ten configs, and watching the agent guess at field names. **One collapses that into a single OAuth flow, then makes the agent read each action's real API documentation before it executes** — required parameters, validation rules and platform caveats are fetched per action, so the failure mode of "the agent invented an endpoint" is designed out of the loop.

The permission model is the second differentiator: each connection carries a grant — full access, allowed HTTP methods, or a specific action list — and the agent can only run what the grant permits.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `list_one_integrations` | Which platforms the user connected, each with its connection key and access grant |
| `search_one_platform_actions` | Search a platform's action catalog (e.g. "send an email" on Gmail); up to 5 matches with actionId, method and path |
| `get_one_action_knowledge` | Fetch the action's knowledge doc — required parameters, validation rules, platform caveats |
| `execute_one_action` | Run the action against the connected platform; confirm irreversible operations first |

## Installation

```bash
claude mcp add one --transport http https://mcp.withone.ai/mcp
```

First connect opens a browser OAuth flow to sign in and authorize app connections. After that, the four tools above are the whole interface — no per-app configuration.

## Configuration

```json
{
  "mcpServers": {
    "one": {
      "type": "http",
      "url": "https://mcp.withone.ai/mcp"
    }
  }
}
```

Two OAuth scopes gate the surface: `user:connections:read` for discovery and knowledge, `user:connections:write` for execution. A knowledge-only grant can still refuse a write call, and irreversible operations should be confirmed with the user before `execute_one_action`.

## Business Relevance

- **Operators without a developer** connect business apps to an agent in one OAuth flow instead of ten API consoles
- **Revenue teams** let the agent read Stripe or QuickBooks and act in HubSpot or Salesforce under a scoped grant
- **Founders** run cross-app automation (Slack alert → Notion page → Gmail draft) from any MCP client
- **Security-conscious teams** get per-connection grants: action-scoped access instead of full API keys

## Integration with CorpusIQ

One overlaps with CorpusIQ's connector surface (QuickBooks, Stripe, HubSpot, Salesforce appear in both), which makes it the natural comparison and the useful complement: CorpusIQ's connectors are purpose-built for business questions with aggregated reporting, while One's action model is general-purpose execution across many apps. Teams can hold the analytical layer in CorpusIQ — books, ads, CRM reporting — and route transactional write actions through One's scoped grants, keeping read-heavy intelligence on the platform built for it.

## Limitations

- Brand new (Aug 2026 listing), no track record yet; pricing not published on the listing
- Four-tool discovery model means every action needs a search + knowledge read before execution (more round-trips than a fixed tool catalog)
- Access is only as broad as the OAuth grants the user approved; scoped grants can refuse calls
- Hosted service — platform risk sits with withone.ai
- Execution requires the write scope; discovery-only connections cannot act

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
