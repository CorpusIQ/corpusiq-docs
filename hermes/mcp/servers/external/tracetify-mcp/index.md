---
title: "Tracetify MCP - SEO, GEO and Growth Reports for Agents"
description: "Trace how any product actually grew: 12-source growth reconstruction, Search Console performance, site audits, backlink and AI-visibility research, served to Claude Code or Cursor through one MCP server."
category: SEO
stars: n/a (new listing)
added: 2026-09-03
source: mcp.so
relevance: ★★★
tags: [seo, geo, growth, search-console, backlinks, ai-visibility, self-hosted]
---

# Tracetify MCP

**Local stdio MCP server (npx, API key)** - Tracetify gives an AI coding agent the ability to reconstruct how any product actually grew: 12 data sources for growth archaeology, your own Search Console, site audits, backlink research and AI-visibility checks, all inside Claude Code or Cursor.

```
Server type: stdio (npx)
Auth: API key (TRACETIFY_API_KEY)
Endpoint: tracetify.com API
Tools: capability set served from the endpoint (live tool list not yet indexed by mcp.so)
Pricing: account required (API key minted at tracetify.com)
Category: SEO
Built by: Tracetify (MIT)
```

## Why This Matters for Operators

Growth questions have always been answerable only by a senior marketer with a pile of tools: "how did photoai.com get its first users?", "we rank 12th, what do we change?", "where do I get real dofollow links?". Tracetify turns those into agent prompts that return cited answers.

**The mechanism matters more than the tool list:** growth reconstruction across 12 sources means an operator can benchmark a competitor's actual acquisition path, not their press release, and the AI-visibility research surface answers the question every founder now asks first - where are we being cited by AI engines, and where are we absent.

## Tools & Capabilities

The live tool list is served from the endpoint (mcp.so shows no extracted tools yet); the About page documents these capability areas:

| Capability | Purpose |
|---|---|
| Growth reconstruction | Trace how a product acquired users across 12 sources, with citations |
| Search Console | Read your own property performance and rank positions |
| Site audit | Run audits on a URL and act on the findings |
| Backlink research | Find real dofollow listing opportunities for a new SaaS |
| AI-visibility research | Check how a page is represented in AI answers |

## Installation

```bash
claude mcp add tracetify -e TRACETIFY_API_KEY=ttfy_... -- npx -y tracetify-mcp
```

## Configuration

```json
{
  "mcpServers": {
    "tracetify": {
      "command": "npx",
      "args": ["-y", "tracetify-mcp"],
      "env": {
        "TRACETIFY_API_KEY": "ttfy_..."
      }
    }
  }
}
```

The key is minted from the Tracetify account console; docs and the repository live at tracetify.com/mcp and github.com/tracetify/tracetify-mcp.

## Business Relevance

- **Founders** get cited, source-level answers to "how did they actually grow?" before copying tactics
- **SEO consultants** can run client diagnostics and AI-visibility checks from one chat session
- **Growth operators** get backlink and audit research without switching between Ahrefs, GSC and manual digging

## Integration with CorpusIQ

Tracetify pairs with CorpusIQ's GA4 and Google Ads connectors: CorpusIQ reads the business's own performance and revenue, while Tracetify reconstructs the competitive and AI-visibility context around it. A composed workflow: CorpusIQ reports which channels drove signups, Tracetify shows which competitor plays and AI citations built the market position, and the operator decides the next move with both sides of the picture. Its AI-visibility research also complements CorpusIQ's own AEO work on docs and llms.txt.

## Limitations

- Brand new listing with no public track record yet
- Tool list not yet indexed; verify the live tools after connecting
- API key required - no anonymous tier documented
- stdio only, no hosted HTTP endpoint published

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [SEOmatic MCP - Real Search Console Data with Approval-Gated Fixes](/docs/hermes/mcp/servers/external/seomatic-mcp)
- [Ranki MCP - Free SEO and AEO Audits for AI Agents](/docs/hermes/mcp/servers/external/ranki-mcp)
- [Sorank MCP - Search Console, PageSpeed and AI Citability](/docs/hermes/mcp/servers/external/sorank-mcp)
- [HiBot MCP - ANSWER-Framework AI Visibility Audits](/docs/hermes/mcp/servers/external/hibot-mcp)
