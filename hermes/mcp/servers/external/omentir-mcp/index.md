---
title: "Omentir MCP - Lead Discovery and Outreach Workspace"
description: "Omentir gives AI assistants a workspace-scoped lead discovery and outreach interface: product profile, lead finders and live inbox replies."
category: Marketing
stars: n/a (new listing)
added: 2026-09-29
source: "mcpservers.org server page + omentir.com/agents.md"
relevance: ★★★
tags: [linkedin, lead-generation, sales, outreach, oauth, open-source, remote-mcp]
---

# Omentir MCP

**A workspace-scoped sales motion for AI assistants.** Omentir hosts an MCP server so an assistant can operate the whole outreach workspace: the product profile, lead finders, qualified LinkedIn leads, activity, send schedules, live inbox replies and workspace switching - all under MIT open source.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (chat apps) or Bearer token (coding agents)
Endpoint: https://omentir.com/api/agent/v1/mcp
Tools: product profile, lead finders, leads, activity, send schedules, inbox replies
Pricing: not published on the listing
Category: Marketing
Built by: Omentir (open source, github.com/vanshyadav1408/Omentir)
```

## Why This Matters for Operators

Most sales tools give an AI assistant read-only dashboards. Omentir gives it an operational interface: the assistant reads the product profile and ICP, configures lead finders including CSV outreach and custom sequences, inspects qualified LinkedIn leads, runs or stops queued sends, and reads and replies in the live LinkedIn inbox from existing threads.

The vendor publishes a full agent guide at omentir.com/agents.md plus a machine-readable capability map at omentir.com/agent.json, so tool behavior is documented rather than guessed. Because the codebase is MIT open source, any unclear tool behavior can be read directly in the implementation. Account, billing, LinkedIn connection and API-key minting deliberately stay with the human.

## Tools & Capabilities

| Capability | Purpose |
|---|---|
| Product profile | Understand the product and ICP the workspace sells into |
| Lead finders | Configure finders, CSV outreach and custom sequences |
| Leads | Inspect qualified LinkedIn leads in the workspace |
| Activity | Read engagement history across campaigns |
| Send schedules | Run or stop queued sends |
| Inbox replies | Read the live LinkedIn inbox and reply in existing threads |
| Workspace switching | The same token can switch to another owned workspace |

Tool names are served from the endpoint; the vendor's agent guide documents the catalog.

## Installation

Chat apps (Claude, ChatGPT, Grok) use the connector URL with OAuth:

```bash
claude mcp add omentir --transport http https://omentir.com/api/agent/v1/mcp
```

Coding agents use the same hosted endpoint with a Bearer token from the API page, sending the Authorization header on every call.

## Configuration

```json
{
  "mcpServers": {
    "omentir": {
      "type": "http",
      "url": "https://omentir.com/api/agent/v1/mcp"
    }
  }
}
```

## Business Relevance

- **Founders and solo operators** delegate lead discovery and inbox replies while keeping the account, billing and LinkedIn connection human-owned
- **Sales teams** run queued sends and reply from existing threads through any MCP client
- **Agencies** switch one token across client workspaces the owner already has
- **Builders** fork the MIT codebase for self-hosted workflows

## Integration with CorpusIQ

Omentir operates the outbound workspace while CorpusIQ answers business questions from live systems. An assistant can qualify an Omentir lead against Stripe revenue history, QuickBooks balances or CRM deal stage through CorpusIQ connectors, then write the follow-up in the same session from the lead's actual engagement history.

## Limitations

- Brand new listing, no track record yet
- Pricing is not published on the directory listing
- Account creation, LinkedIn connection and API-key minting stay with the human by design
- LinkedIn access depends on the workspace's own LinkedIn connection

## FAQ

### What is the endpoint?

The hosted MCP server is at omentir.com/api/agent/v1/mcp. Chat apps connect with OAuth; coding agents use a Bearer token from the API page.

### Is it open source?

Yes, under the MIT license. The full application code, including the Agent API and MCP server, is public at github.com/vanshyadav1408/Omentir.

### What stays with the human?

Account creation, subscription changes, LinkedIn connection, workspace creation or deletion and API-key minting. The assistant operates the workspace but never owns the account.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
