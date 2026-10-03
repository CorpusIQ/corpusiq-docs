---
title: "Dock MCP - Agent Workspace for Docs and Tables"
description: "Official MCP for Dock: workspaces of docs, tables and HTML surfaces, plus agent messaging, search and comments behind OAuth."
category: "Business Operations"
stars: n/a (hosted platform, trydock.ai)
added: 2026-10-02
source: "mcpservers.org server page (try-dock-ai/mcp)"
relevance: ★★★
tags: [workspace, docs, tables, collaboration, agents, project-management, remote-mcp]
---

# Dock MCP

**Remote MCP server (Streamable HTTP, OAuth) plus a local stdio bridge** - Dock is a workspace where humans and agents work as teammates, and its official MCP server exposes that workspace to any agent so documents, tables and HTML surfaces become something an assistant reads and writes alongside the team.

```
Server type: Remote (Streamable HTTP) plus local stdio bridge (npx)
Auth: OAuth (remote) or an API key (stdio bridge)
Endpoint: https://trydock.ai/api/mcp
Tools: 8 in the stdio bridge, with 71 capabilities documented on the hosted server
Pricing: Dock account required
Category: Business Operations
Built by: Vector Apps, Inc. (trydock.ai)
```

## Why This Matters for Operators

Most agent work dies in a chat window. Dock gives the output a home: a workspace of docs, tables and interactive HTML surfaces that agents and people share, version and comment on. The MCP server turns that home into something an assistant can act on directly, so a summary an agent drafts lands in the same table the team reviews rather than in a transcript nobody opens again.

**The point is the shared surface.** A table-mode workspace is a structured store an agent can query and update row by row, and the activity log records who changed what, which is what makes autonomous writes auditable rather than opaque.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `list_workspaces` | Enumerate workspaces you can access |
| `get_workspace` | Fetch a workspace by slug |
| `list_rows` | Read rows from a table-mode workspace |
| `create_row` | Append a row |
| `update_row` | Partial-merge update to a row |
| `delete_row` | Remove a row |
| `create_workspace` | Create a new workspace |
| `get_recent_events` | Read the workspace activity log |

The hosted server documents 71 capabilities across docs, tables, HTML surfaces, search, comments and agent messaging; the stdio bridge forwards the eight above.

## Installation

For agents that speak local stdio MCP (Claude Desktop, Cursor, Windsurf, Zed, Cline, Continue):

```bash
npx -y @trydock/mcp
```

Pass `DOCK_API_KEY` in the environment. For clients that support remote connectors (Claude.ai web and Projects), add `https://trydock.ai/api/mcp` directly and complete the OAuth flow.

## Configuration

```json
{
  "mcpServers": {
    "dock": {
      "command": "npx",
      "args": ["-y", "@trydock/mcp"],
      "env": {
        "DOCK_API_KEY": "dk_..."
      }
    }
  }
}
```

The bridge is a small Node process that forwards each JSON-RPC message over HTTPS to the hosted server, which owns authentication, rate limits, audit and tool execution. Keys are stored as SHA-256 hashes server-side and can be rotated in Settings, where revocation returns 401 immediately.

## Business Relevance

- **Operations teams** keep tables of vendors, projects or inventory in a workspace an agent can read and update directly.
- **Project managers** get agent-drafted plans and status docs written into the same shared surface the team works in.
- **Founders** use HTML surfaces as lightweight internal tools an assistant can populate without a separate app.
- **Support teams** let an agent message other agents and log work in the workspace activity trail.
- **Any operator running several agents** gets per-agent access control and one auditable change log.

## Integration with CorpusIQ

Dock gives an agent a durable place to write, and CorpusIQ gives it the business data to write about. A QuickBooks or Stripe read runs across the connectors, the agent drafts a monthly revenue table, and Dock stores it as a workspace the finance team reviews and comments on. A HubSpot pipeline pull becomes a Dock table for the sales stand-up; a Shopify inventory read becomes an ops workspace. CorpusIQ supplies the numbers, Dock supplies the collaborative surface they land on, and neither has to reinvent the other.

## Limitations

- Brand new, with no long track record.
- Requires a Dock account, and the hosted server is the only execution path.
- The stdio bridge is a thin forwarder, so anything the hosted server does not expose is unavailable.
- Table operations are row-level, so large analytical queries belong in a warehouse rather than a workspace.
- The API key lives in the agent's environment, so it needs the same secret hygiene as any credential.

## FAQ

### Does Dock MCP support remote connectors or only local stdio?

Both. Clients with remote connector support can point at `https://trydock.ai/api/mcp` and use OAuth; stdio-only clients use the `@trydock/mcp` bridge with an API key.

### How many tools does it expose?

The stdio bridge forwards eight tools (workspace and row operations plus the activity log); the hosted server documents 71 capabilities across docs, tables, HTML surfaces, search, comments and agent messaging.

### Is agent activity auditable?

Yes. The workspace keeps an activity log readable through `get_recent_events`, and the hosted server records audit and rate-limit information.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
