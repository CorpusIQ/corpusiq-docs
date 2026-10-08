---
title: "AssetLab MCP - CMMS and Asset Management for Agents"
description: "Official hosted MCP for the AssetLab CMMS: work orders, preventive maintenance, assets, capital projects and budgets in 480+ tools."
category: Business Operations
stars: n/a (new listing)
added: 2026-10-07
source: "mcp.so /feed (Oct 7, 2026 evening sweep)"
relevance: ★★★
tags: [cmms, asset-management, maintenance, work-orders, facilities, public-works]
---

# AssetLab MCP

**Official hosted MCP server for AssetLab, the Canadian asset management and CMMS platform** - connect Claude, ChatGPT, Microsoft Copilot or any MCP client to your AssetLab account and work with your data in plain language: work orders, preventive maintenance schedules, assets, condition assessments, capital projects, budgets, contracts and linear infrastructure networks. 480+ tools across 100+ resources, read and write.

```
Server type: Remote (Streamable HTTP at https://mcp.assetlab.ca/mcp)
Auth: Scoped API keys (read-only by default, bound to your organization, revocable any time)
Core profile: add ?profile=core for a 28-tool surface sized for clients that cap tool counts, such as Microsoft Copilot Studio
Access: Requires an AssetLab account; create a key under Settings > API Keys
Tools: 480+ across work orders, PM schedules, assets, condition, capital projects, budgets, contracts and linear infrastructure
Category: Business Operations
Built by: AssetLab
```

## Why This Matters for Operators

Maintenance and asset teams run their day from a CMMS, but the questions arrive everywhere else: in email, in chat, in the meeting where someone asks which pumps are overdue or what a watermain replacement will cost. This server puts the whole CMMS behind an MCP endpoint, so any AI client can answer from the live system - and create or update records without leaving the conversation. The scoped-key design keeps it operator-safe: keys are read-only by default, bound to your organization, and revocable at any time.

## Tools & Capabilities

| Domain | What the agent can work with |
|---|---|
| Work orders | show overdue or open work, create a work order for an asset or location |
| Preventive maintenance | what PM schedules are due this month, schedule views |
| Assets | asset records, condition assessments, cost history per asset |
| Capital planning | projects, at-risk or delayed projects, budgets |
| Contracts | contract records tied to the asset estate |
| Linear infrastructure | networks such as watermains, including condition filters |
| Administration | users, permissions and the account surface behind the scoped key |

The 480+ tool surface spans 100+ resources; the vendor suggests the `?profile=core` variant (28 tools) for clients with tool-count caps.

## Installation

```bash
claude mcp add assetlab --transport http https://mcp.assetlab.ca/mcp
```

Or add the URL in any MCP client that supports remote Streamable HTTP servers. Example prompts from the vendor: "Show me all overdue work orders", "Create a work order for the broken pump in Building 3", "List watermains over 500 mm in poor condition".

## Configuration

1. Sign in to AssetLab and create an API key under Settings > API Keys.
2. Add the server URL to your client, with the key as the bearer token (or let the client prompt for it).
3. For tool-capped clients, append `?profile=core` to the URL to load only the 28 core tools.

## Business Relevance

- **Facilities teams:** answer "what is overdue, what is due, what did this asset cost us" from the live CMMS without dashboard hunting.
- **Municipal and public works:** work across assets, condition assessments, capital projects and linear networks from the same conversation.
- **Fleet and property managers:** create and update records in plain language while keeping the audit trail in the system of record.

## Integration with CorpusIQ

CorpusIQ reads your business systems - accounting, CRM, analytics - and keeps the numbers consistent across AI clients. AssetLab covers the physical estate: ask CorpusIQ for the spend context, then ask AssetLab which assets are driving it, in the same conversation.

## Limitations

- Requires an AssetLab account; the server reads and writes your organization's data only through scoped keys you create and can revoke.
- Write access depends on the key's scopes; keys are read-only by default.
- Brand new listing - the endpoint is documented and live (probe: 401 bearer-token required) but there is no third-party track record yet.

## FAQ

### Can the agent change data in the CMMS?

It can, but only within what the API key allows. Keys are read-only by default and scoped to your organization; grant more only when you want the agent to create or update records.

### What is the core profile for?

Some clients (for example Microsoft Copilot Studio) cap how many tools a server can expose. Adding ?profile=core loads a 28-tool surface instead of the full 480+.

### Do I need a developer to set this up?

No - create an API key in Settings > API Keys, add the URL to your MCP client, and go. The vendor's setup line is one `claude mcp add` command.

### Does it work with any AI client?

Any MCP-compatible client. The vendor names Claude, ChatGPT and Microsoft Copilot; tool-capped clients should use the core profile.

## See Also

- [A4B CMMS MCP - Asset & Maintenance Management](/hermes/mcp/servers/external/a4b-cmms-mcp)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
