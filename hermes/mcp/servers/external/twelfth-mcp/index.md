---
title: "Twelfth MCP - Read-Only Workspace Access"
description: "Read-only remote MCP endpoint that connects any MCP client to a Twelfth workspace using an OAuth user token or a workspace bearer key."
category: "Productivity"
stars: n/a (hosted platform, twelfth.ai)
added: 2026-10-03
source: "mcpservers.org server page (twelfth-ai-developers-mcp)"
relevance: ★★
tags: [productivity, workspace, read-only, oauth, remote-mcp]
---

# Twelfth MCP

**Hosted MCP server** - Twelfth exposes a read-only MCP endpoint so any client that speaks MCP can connect to a workspace, even clients not covered by Twelfth's named integrations.

```
Server type: Hosted (remote)
Auth: OAuth user token or workspace bearer key
Endpoint: https://api.twelfth.ai/mcp
Category: Productivity
Built by: Twelfth (twelfth.ai)
```

## Why This Matters for Operators

Twelfth ships first-party setup for Claude, ChatGPT, Gemini, Grok, Glean and Cursor, but the generic MCP endpoint is the escape hatch for everything else: a custom agent, an internal tool, an IDE the vendor has not listed. It is read-only and accepts either an OAuth user token or a workspace bearer key, so a workspace admin can hand an agent scoped read access to the workspace's data without building a bespoke integration.

For an operator standardizing on MCP, a vendor that publishes a client-agnostic endpoint is the low-friction case. Setup lives under Settings, AI and agents, Generic MCP in the workspace, which keeps the connection path inside the product rather than a support ticket.

## Connect

Point any MCP client at `https://api.twelfth.ai/mcp`, authenticating with an OAuth user token or a workspace bearer key. Reach the setup guide from Settings, AI and agents, Generic MCP inside Twelfth.

## Limitations

- Read-only; no write or action tools.
- Requires a Twelfth workspace and a valid token or key.
- Data visible to the agent is bounded by the workspace and the token's scope.

## FAQ

### Can an agent write to Twelfth through this endpoint?

No. The endpoint is read-only by design.

### When should I use this instead of the first-party connectors?

Use it when your client is not covered by Twelfth's named integrations. The endpoint is client-agnostic.

### How do I authenticate?

With an OAuth user token or a workspace bearer key; setup is under Settings, AI and agents, Generic MCP.

## Related

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - the curated catalog
- [MCP Ecosystem Sweeps](/hermes/mcp/sweeps/) - all sweep reports
