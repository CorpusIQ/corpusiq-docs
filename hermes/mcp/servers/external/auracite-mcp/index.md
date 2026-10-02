---
title: "AuraCite MCP - AI Visibility and GEO Data for Agents"
description: "AuraCite MCP gives agents read-only access to AI-visibility data: how ChatGPT, Gemini, Perplexity and Claude mention, cite and recommend a brand, including share of voice, visibility scores, per-engine breakdowns, AI-crawler access and Google Search Console performance. OAuth 2.1 PKCE with an API-key fallback."
category: SEO
stars: 0
added: 2026-09-07
source: "chatmcp/mcpso issue #3972"
relevance: ★★★
tags: [geo, ai-visibility, brand-mentions, share-of-voice, oauth, remote-mcp, search-console]
---

# AuraCite MCP - AI Visibility and GEO Data for Agents

**Remote MCP server (Streamable HTTP, OAuth 2.1 / read-only API key)** - AuraCite measures how AI engines mention, cite and recommend brands, and exposes that data to MCP clients read-only: tracked brands, AI mentions, citations of the operator's pages, share of voice, visibility scores, competitor comparisons, per-engine breakdowns, AI-crawler access patterns and Google Search Console performance.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 authorization code flow with PKCE S256 and DCR (RFC 7591); read-only AuraCite API key fallback
Endpoint: https://auracite.de/mcp/rpc (probe-verified live; 401 invalid_token with scope mcp:read)
Tools: read-only brand visibility, mentions, citations, share of voice, competitors, trends, crawler access, GSC data
Pricing: AuraCite plans at auracite.de
Category: SEO
Built by: AuraCite (auracite.de); repo github.com/getauracite/claude-plugins
```

## Why This Matters for Operators

AI answer engines are now a distribution channel, and most brands have no instrumentation on whether they are being cited, recommended or ignored in them. AuraCite MCP puts the full measurement surface into the agent: the operator asks "who cites us, where are we losing share, and which engines' crawlers can even reach our pages" and gets numbers, not guesses.

**The scope discipline is notable: the default credential is mcp:read, and mutating, cost-bearing and admin tools are filtered out of tools/list server-side, so a misconfigured client cannot buy anything or change anything.**

## Tools & Capabilities

| Group | What the agent reads |
|---|---|
| Brand tracking | Tracked brands, AI mentions and citations of the operator's pages as sources |
| Share of voice | Visibility scores and share-of-voice comparisons against competitors |
| Per-engine breakdown | Mentions and citations split by ChatGPT, Gemini, Perplexity and Claude |
| Trends | Trend lines over time per brand and topic |
| Crawler access | Which AI bots fetch which pages, exposing indexability gaps |
| Search Console | Top queries, per-page rows, country and device breakdowns from GSC |

## Installation

Connect through the OAuth flow from any OAuth-capable MCP client; discovery documents are served at the well-known OAuth endpoints on auracite.de. Clients without OAuth support can send a read-only API key as the bearer authorization header or X-API-Key header.

```json
{
  "mcpServers": {
    "auracite": {
      "type": "http",
      "url": "https://auracite.de/mcp/rpc"
    }
  }
}
```

## Configuration

The OAuth flow handles token exchange automatically in supporting clients. For key-based access, mint the read-only key in the AuraCite dashboard and attach it as the authorization header. The probe confirms the endpoint enforces auth with a JSON-RPC invalid_token error naming the required scope.

## Business Relevance

- **SEO teams** replace manual AI-engine spot checks with a queryable share-of-voice dataset.
- **Brand teams** track when competitors start being recommended in the same category.
- **Content teams** see which pages AI engines cite as sources and which crawlers cannot reach the site.
- **Agencies** monitor multiple client brands through one read-only connector.

## Integration with CorpusIQ

AuraCite supplies the AI-visibility half of the measurement loop; CorpusIQ supplies the revenue half. The agent correlates AuraCite citation gains with CorpusIQ's GA4 and Stripe signals to prove which visibility fixes moved traffic and revenue, then feeds winning topics back into the content calendar.

## Limitations

- Brand new listing (issue #3972, Sep 6, 2026); the reference repo is a plugin package with 0 stars and no declared license.
- Read-only surface by design; campaign and admin functions stay in the AuraCite web app.
- Coverage is limited to the engines AuraCite instruments (ChatGPT, Gemini, Perplexity, Claude).

## See Also

- [Encited MCP - SEO and AI Visibility for Agents](/hermes/mcp/servers/external/encited-mcp)
- [Ranki MCP - SEO and AEO Audits](/hermes/mcp/servers/external/ranki-mcp)
- [CiteRank MCP - AI Search Visibility Audits](/hermes/mcp/servers/external/citerank-mcp)
- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
