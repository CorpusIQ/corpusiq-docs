---
title: "OpenAdLibrary MCP - Ad Library Data for Agents"
description: "Remote MCP over the OpenAdLibrary public ad corpus, so agents can search live and historical creative without leaving the conversation."
category: "Business Operations"
stars: n/a (hosted platform, openadlibrary.com)
added: 2026-10-03
source: "mcp.so server page (openadlibrary)"
relevance: ★★
tags: [ads, advertising, creative, marketing, competitive-research, remote-mcp]
---

# OpenAdLibrary MCP

**Remote MCP server (Streamable HTTP, public-data key)** - OpenAdLibrary exposes a public ad corpus to any MCP client at `https://mcp.openadlibrary.com/mcp`, so an agent can pull live and historical ad creative for competitor and market research without a browser session.

```
Server type: Remote (Streamable HTTP)
Auth: Public-data key (Authorization: Bearer or x-api-key header), or OAuth
Endpoint: https://mcp.openadlibrary.com/mcp
Tools: Ad-library search and retrieval tools (live list via the server endpoint)
Pricing: Free public-data tier (key required)
Category: Business Operations
Built by: OpenAdLibrary (openadlibrary.com)
```

## Why This Matters for Operators

Competitive ad research is usually a manual sport: open the platforms' ad libraries, screenshot what is running, guess at what it means. OpenAdLibrary packages the same public ad data behind an MCP endpoint, so an agent can search by advertiser, keyword or theme and reason over the results in the same conversation where the rest of the campaign work happens.

**The differentiator is that the data is public by design.** This is a library of ads that platforms already publish for transparency, so an operator is researching in the open rather than scraping behind a login. The server returns the corpus; the interpretation stays with the operator.

## Tools & Capabilities

The server exposes OpenAdLibrary's ad-search surface to MCP clients, covering:

- **Search across the public ad corpus** - find ads by advertiser, keyword or theme
- **Retrieve creative and metadata** - pull the ad units and their accompanying details
- **Competitive research in-loop** - compare live competitor creative without a separate tool

The authoritative tool list is fetched live from `https://mcp.openadlibrary.com/mcp`.

## Installation

```bash
claude mcp add openadlibrary --transport http https://mcp.openadlibrary.com/mcp
```

The same endpoint works in Cursor, VS Code and any client that supports remote Streamable HTTP MCP servers.

## Configuration

```json
{
  "mcpServers": {
    "openadlibrary": {
      "type": "http",
      "url": "https://mcp.openadlibrary.com/mcp",
      "headers": {
        "x-api-key": "${OPENADLIBRARY_KEY}"
      }
    }
  }
}
```

A public-data key is required. The server accepts the key either as an `Authorization: Bearer` header or an `x-api-key` header; a request without one is refused with an authentication error. OAuth is also supported.

## Business Relevance

- **Marketing and growth teams** pull live competitor creative into the same session where they draft their own, instead of screenshotting by hand.
- **Brand teams** track how a category talks about itself to spot messaging that is oversaturated or open.
- **Agencies** research a client's competitive set quickly and bring the actual ad units, not a summary of them.
- **Founders** sanity-check positioning against what established players are already running before committing budget.
- **Analysts** build ad-creative datasets from a public corpus without maintaining their own scraper.
