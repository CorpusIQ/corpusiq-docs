---
title: Worthbase MCP - Net Worth and Portfolio Tracking for Agents
description: "OAuth remote MCP server with 28 tools for household net worth, portfolios, cost bases and gains, with every write previewed and undoable."
category: Finance
stars: n/a (hosted service, worthbase.app)
added: 2026-10-01
source: "mcpservers.org /all (worthbase-app-developers)"
relevance: ★★
tags: [finance, net-worth, portfolio, investments, accounting, oauth, remote-mcp]
---

# Worthbase MCP

**A net worth tracker the agent keeps, not the person.** Worthbase maintains a household or entity balance sheet - shares, crypto, metals, super, property, cash and loans - and exposes it over MCP with 28 tools. Assets can be owned by people, trusts or companies; prices are refreshed daily; cost bases and gains are exact; and every write is previewed and undoable.

```
Server type: Remote (Streamable HTTP, stateless)
Auth: OAuth 2.1 (authorization code + PKCE), Clerk as the authorization server
Endpoint: https://worthbase.app/mcp
Tools: 28 (read and write, with MCP annotations for approval rules)
Pricing: requires an active trial or subscription
Category: Finance
Built by: Worthbase
```

## Why This Matters for Operators

Most net worth trackers depend on the person doing the boring part: entering holdings, updating prices, reconciling cost bases. Worthbase inverts that by exposing the whole balance sheet to an agent, so a founder can ask "what am I worth today" or "rebalance this" and have the agent read and adjust the model - with a preview and an undo on every write.

The design details are what make it safe for agents. The server sends instructions on initialise telling the agent how to read, write and stay safe; tools carry MCP annotations (read-only, destructive, open-world) so clients can set approval rules; and writes are previewed and reversible. IDs are prefixed ULIDs, so every result is addressable and traceable.

## Tools & Capabilities

| Group | Purpose |
|---|---|
| Read tools | Read the balance sheet, holdings, valuations and reports |
| Write tools | Add and edit assets, transactions and valuations (previewed and undoable) |
| Workspaces | Operate across multiple workspaces via an optional `ws_…` id |

Twenty-eight tools total, most taking an optional `workspace` argument; without it, the user's default workspace is used. The vendor publishes the count and annotations but not the full identifier list on the public page, so the guide describes the surface by group.

## Installation

```
claude mcp add --transport http worthbase https://worthbase.app/mcp
```

Clients identify themselves with a Client ID Metadata Document, so there is no client ID or secret to paste. Works with Claude (web, desktop, mobile), ChatGPT (developer mode), Cursor, Claude Code and any client supporting remote MCP over OAuth.

## Configuration

```json
{
  "mcpServers": {
    "worthbase": {
      "type": "http",
      "url": "https://worthbase.app/mcp"
    }
  }
}
```

## Business Relevance

- **Founders and operators** can track personal and entity balance sheets through the same agent they use for the business.
- **Family offices and trusts** can model assets held by people, trusts or companies in one workspace.
- **Finance-adjacent workflows** get exact cost bases and gains rather than approximate portfolio values.
- **AI agents** get a write-safe financial surface where every change is previewed and reversible.

## Integration with CorpusIQ

Worthbase covers the owner side of the balance sheet; CorpusIQ covers the business side. An agent can read company performance from CorpusIQ's connectors and personal or entity holdings from Worthbase, then answer a question about overall position - business cash flow and personal net worth in one response, composed from two grounded sources.

## Limitations

- Requires an active Worthbase trial or subscription for the workspace to be readable or writable.
- Aimed at personal and household net worth tracking; it is not a business accounting ledger.
- Clients that only support local stdio servers cannot connect directly; a remote-MCP-with-OAuth client is required.
- The public listing publishes the tool count and annotations rather than every identifier.

## FAQ

### What does the Worthbase MCP server do?

It gives an AI agent read and write access to a Worthbase net worth and portfolio tracker, with 28 tools over holdings, valuations, cost bases and gains, and every write previewed and undoable.

### How does authentication work?

OAuth 2.1 with PKCE, using Clerk as the authorization server and Client ID Metadata Documents so no secret is pasted. A token acts as the signed-in user with that user's role in each workspace.

### Can an agent make changes without approval?

Tools carry MCP annotations, and writes are previewed and undoable, so clients can set approval rules and any change can be reversed.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ](https://corpusiq.io) - 40+ business data connectors for AI agents
