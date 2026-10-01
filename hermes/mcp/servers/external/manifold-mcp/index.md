---
title: "Manifold MCP - Hosted Marketing Data for Agents"
description: "One hosted endpoint for keyword research, SERPs, backlinks, site audits, AI answer visibility, social and ad-library data plus B2B lead enrichment, billed per call."
category: Marketing
stars: n/a (hosted platform, manifoldmcp.com)
added: 2026-09-30
source: "mcp.so server page (manifold-mcp)"
relevance: ★★★
tags: [marketing, seo, serp, backlinks, ai-visibility, social-data, ad-library, lead-enrichment, remote-mcp]
---

# Manifold MCP

**Hosted marketing data in a single connection.** Manifold MCP gives agents keyword research, SERPs, backlinks and site audits, AI answer visibility across ChatGPT, Perplexity and Google AI Overviews, social data from Reddit, YouTube, TikTok, Instagram, LinkedIn, X and Facebook, ad libraries, and B2B lead enrichment, without bringing your own API keys. Billing is per call, and every new workspace starts with 500 free credits.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth or an API key
Endpoint: https://mcp.manifoldmcp.com/mcp
Tools: multi-surface data tools for SEO, AI visibility, social, ads and B2B enrichment
Pricing: pay per call; 500 free credits per new workspace
Category: Marketing
Built by: manifoldmcp.com
```

## Why This Matters for Operators

Marketing data is normally a stack of keys: one for keywords, one for backlinks, one for ad libraries, one for social listening, one for enrichment. Each has its own pricing page, quota and client setup. Manifold collapses that into one remote endpoint the agent connects to once, with per-call billing instead of five subscriptions: useful for operators who need the data occasionally rather than as a full-time platform seat.

The AI answer visibility surface is the more interesting addition. As buyers shift from search results to AI answers from ChatGPT, Perplexity and Google AI Overviews, knowing whether a brand appears in those answers is a distinct signal from a rank tracker, and it is read here alongside the classic SEO surfaces.

## Tools & Capabilities

| Surface | Data |
|---|---|
| SEO | Keyword research, SERPs, backlinks, site audits |
| AI visibility | Brand presence across ChatGPT, Perplexity and Google AI Overviews |
| Social | Reddit, YouTube, TikTok, Instagram, LinkedIn, X and Facebook |
| Ads | Ad libraries |
| B2B | Lead enrichment |

The server exposes these as MCP tools over a Streamable HTTP endpoint. Manifold is a verified, featured listing on mcp.so.

## Installation

```bash
claude mcp add manifold-mcp --transport http https://mcp.manifoldmcp.com/mcp
```

Connect at `https://mcp.manifoldmcp.com/mcp` using OAuth or an API key. New workspaces start with 500 free credits.

## Configuration

```json
{
  "mcpServers": {
    "manifold-mcp": {
      "type": "http",
      "url": "https://mcp.manifoldmcp.com/mcp"
    }
  }
}
```

Supported clients include Claude Code, Codex, Cursor and VS Code.

## Business Relevance

- **Growth and SEO operators** pull keyword, SERP, backlink and audit data without managing separate keys
- **Brand teams** track presence in ChatGPT, Perplexity and Google AI Overviews alongside classic rankings
- **Social and content leads** read Reddit, YouTube, TikTok, Instagram, LinkedIn, X and Facebook through one connection
- **Outbound teams** enrich B2B leads from the same endpoint that supplies the research

## Integration with CorpusIQ

Research and revenue belong together. A composed workflow: Manifold reports where a brand appears in AI answers and which keywords are moving, and CorpusIQ supplies the signup, revenue and channel attribution behind it from its GA4, Stripe and Google Ads connectors, so an operator can tie an AI-visibility lift to a conversion change. For operators running both, the answer-visibility question and the conversion question sit in one session.

## Limitations

- Pay-per-call billing means cost scales with usage; there is no flat-unlimited tier published
- The mcp.so FAQ states no authentication is required while the vendor overview describes OAuth or an API key, so verify the current auth requirement from the provider before publishing credentials into a client
- The catalog page did not expose a fetchable tool list at catalog time, so surfaces are listed by data area rather than exact tool identifiers
- Coverage of each social platform depends on the provider's upstream sources, which are not enumerated on the listing

## FAQ

### Do I need my own API keys for the underlying data?

No. Manifold hosts the data behind one connection, so you connect once rather than bringing keys for each source.

### How is it billed?

Per call, against the workspace credits. Every new workspace starts with 500 free credits.

### Which clients does it support?

Any MCP-compatible client, including Claude Code, Codex, Cursor and VS Code over the Streamable HTTP endpoint.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Vouched MCP - SEO Data with Provenance for Agents](/hermes/mcp/servers/external/vouched-mcp/)
- [HarborRank MCP - Live SEO Data for AI Agents](/hermes/mcp/servers/external/harborrank-mcp/)
- [Ahrefs MCP - SEO Data for Agents](/hermes/mcp/servers/external/ahrefs-mcp/)
