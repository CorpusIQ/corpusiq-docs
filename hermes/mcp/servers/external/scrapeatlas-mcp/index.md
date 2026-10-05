---
title: "ScrapeAtlas MCP - Social Data Access for Agents"
description: "291 tools over 40 social platforms on one HTTP endpoint: public profiles, posts, videos and conversations, with source context and coverage flags."
category: Data & Analytics / Market Intelligence
stars: n/a (hosted API, scrapeatlas.com)
added: 2026-10-05
source: "chatmcp/mcpso issue #4745 (OD. Media & Technology LLC)"
relevance: ★★
tags: [social-media, web-scraping, data, research, reddit, api, remote-mcp]
---

# ScrapeAtlas MCP

**One endpoint for the public social web.** ScrapeAtlas turns its social scraping API into 291 discoverable tools covering 40 platforms: agents fetch public profiles, posts, videos and conversations through the same contracts as the REST API, with a single customer key. Source context comes back with the results, including the source URLs and an honest signal when a result is partial.

```
Server type: Remote (Streamable HTTP)
Auth: Bearer token (ScrapeAtlas customer API key)
Endpoint: https://api.scrapeatlas.com/mcp
Tools: 291 endpoint tools across 40 cataloged platforms
Registry: io.github.OnlineDopamine/scrapeatlas (official MCP Registry)
Docs: https://scrapeatlas.com/mcp/ (preview)
Built by: OD. Media & Technology LLC
```

## Why This Matters for Operators

Social research is usually a chain of one-platform scrapers and CSV exports. ScrapeAtlas collapses it into one connection with one key: find public conversations about a topic, pull a profile, read posts and comments, or collect a platform's videos, all returning source URLs the operator can cite. Because the tool layer is generated from the API's own contracts, the same coverage the REST API advertises is reachable from Claude, Cursor or any other MCP client.

## Tool Surface

The 291 tools map the REST API catalogs one to one. Representative shapes:

| Shape | Examples |
|---|---|
| Global search | redditGlobalSearch to find public discussions by topic |
| Threads and replies | redditGetComments to bring the available comments into research |
| Profiles and posts | Public profiles, posts, videos and conversations across the covered platforms |

Results carry source context and coverage flags, so an agent can tell when a result is partial instead of presenting it as complete.

## Authentication

A ScrapeAtlas customer API key, sent as a bearer credential in the Authorization header. Keys come from the ScrapeAtlas account; the MCP server uses the same key as the REST API. The endpoint answers a bare GET with 405 and instructs clients to use Streamable HTTP POST.

## Installation

```bash
claude mcp add --transport http scrapeatlas https://api.scrapeatlas.com/mcp
```

Cursor and other clients:

```json
{
  "mcpServers": {
    "scrapeatlas": {
      "url": "https://api.scrapeatlas.com/mcp"
    }
  }
}
```

Attach the API key as a bearer credential in the Authorization header; the docs page shows the full setup and the tool explorer.

## Business Relevance

- **Market researchers** pull public conversations across platforms into one working context instead of juggling per-platform tools.
- **Content and social teams** ground decisions in actual public posts and comments, with source URLs for citation.
- **Competitive analysts** collect profiles, posts and videos across the covered platform set through a single key.

## Integration with CorpusIQ

CorpusIQ answers business questions from first-party data (revenue, ads, analytics); ScrapeAtlas answers them from the public web. Composed, an operator can cross-examine a pattern in their own numbers with what customers are saying publicly, or size a competitor's social footprint next to ad-library and search data from the CorpusIQ side, all from one agent session.

## Limitations

- Paid API; a customer key is required and usage is metered by the vendor's REST pricing.
- Public data only: profiles, posts and conversations that the platforms expose publicly.
- Some results may be partial; the response flags coverage rather than filling gaps silently.
- The docs page is marked preview; exact tool names vary by platform catalog and are best discovered from the built-in explorer.

## FAQ

### Is one key enough for all platforms?

Yes. One ScrapeAtlas customer key gives the MCP server the same catalog as the REST API across the covered platforms.

### How does an agent know a result is incomplete?

Responses include source context and coverage signals; the agent can see when a result is partial instead of treating it as complete.

### Does it need a separate scraper per platform?

No. The 291 tools are generated from the same contracts as the API, so platform coverage ships through the single endpoint.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [RedReplier MCP - Social Lead Monitoring and Reply Drafts](/hermes/mcp/servers/external/redreplier-mcp/)
- [HasData MCP - Marketplace and Web Data Gateway for Agents](/hermes/mcp/servers/external/hasdata-mcp/)
- [TwitterXAPI MCP - X Data for Agents](/hermes/mcp/servers/external/twitterxapi-mcp/)
