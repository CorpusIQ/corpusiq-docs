---
title: "Thrume MCP - Authorized Recording Evidence"
description: "Read-only remote MCP that lets a compatible assistant retrieve authorized recording evidence from a Thrume account over OAuth with a recordings read scope."
category: "Productivity"
stars: n/a (hosted platform, thrume.app)
added: 2026-10-03
source: "mcpservers.org server page (thrume-app-docs-mcp)"
relevance: ★★
tags: [productivity, recordings, evidence, compliance, read-only, oauth, remote-mcp]
---

# Thrume MCP

**Hosted MCP server** - Thrume exposes a read-only MCP endpoint that lets a compatible assistant retrieve authorized recording evidence from an account, with the client and connection chosen and approved by the user.

```
Server type: Hosted (streamable HTTP, remote)
Auth: OAuth with PKCE
Scope: recordings:read
Endpoint: https://dash.thrume.app/mcp
Category: Productivity
Built by: Thrume (thrume.app)
```

## Why This Matters for Operators

Recordings are often the evidence behind a decision, a dispute or an audit, and pulling the right one usually means a person digging through an archive. Thrume's MCP turns that into a scoped read: the assistant retrieves authorized recordings under a single `recordings:read` scope, with the user approving the connection from inside the Thrume web app.

The deliberate constraint is the story. There is no write, no edit, no delete. The connection is read-only by scope, the user picks which client to authorize, and setup runs from an AI connections panel inside the authenticated app. For teams handling sensitive recordings, that narrow surface is easier to approve than a broad account integration.

## Connect

Set up from inside the Thrume web app: sign in, open AI connections, and choose your client. Cursor and VS Code open their install prompts; Codex and Claude Code provide setup commands; Claude offers guided connectors. The server URL is `https://dash.thrume.app/mcp` with Streamable HTTP transport and OAuth with PKCE, scope `recordings:read`.

## Limitations

- Read-only: no tool can add, edit or delete recordings.
- Requires an approved Thrume account.
- Client capabilities and account restrictions vary by plan and configuration.

## FAQ

### Can the assistant change anything in my account?

No. The scope is `recordings:read` and the surface is read-only by design.

### Where do I approve the connection?

Inside the Thrume web app, from the AI connections panel, where you also choose which client to authorize.

### Which clients are supported?

Any MCP client that supports remote Streamable HTTP with OAuth; Thrume documents setup for Cursor, VS Code, Codex and Claude Code.

## Related

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - the curated catalog
- [MCP Ecosystem Sweeps](/hermes/mcp/sweeps/) - all sweep reports
