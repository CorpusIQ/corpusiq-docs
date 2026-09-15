---
title: Encited MCP - SEO and AI Visibility for Agents
description: Hosted MCP for Google Search Console mining, technical SEO audits and AI answer-engine visibility. Agents surface CTR gaps, decaying pages and cannibalization, pull the fan-out queries behind ChatGPT and Perplexity answers, and turn citation gaps into page-by-page content plans. OAuth sign-in, free tier to start.
category: SEO
stars: n/a (new listing)
added: 2026-09-06
source: mcpservers.org
relevance: ★★★
tags: [seo, ai-visibility, geo, aeo, search-console, content-planning, technical-audit, remote-mcp]
---

# Encited MCP - SEO and AI Visibility for Agents

**Remote MCP server (Streamable HTTP, OAuth browser sign-in)** - a hosted SEO and AI-search operating layer from Encited (encited.com) that lets an agent run the full organic-growth stack from chat: up to a year of Search Console history mined for CTR gaps, deep technical crawls with ranked fixes, and AI answer-engine visibility that shows which ChatGPT and Perplexity answers cite you, which prompts you are missing from, and where to get cited. Listed in the official Claude connector directory and used by 4,000+ brands and agencies.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (browser sign-in on first connect, no key handling)
Endpoint: https://encited.com/api/mcp
Tools: Capability groups over live Search Console, crawl, audit, ranking and AI-visibility data (live tool list served from the endpoint; groups below from vendor docs)
Pricing: Free tier to start, then paid plans (contact sales for agency tiers)
Category: SEO
Built by: Encited (encited.com)
```

## Why This Matters for Operators

SEO today means winning two rankings at once: the classic blue links and the answers AI engines assemble from your space. Encited collapses both into one agent workflow. Instead of exporting Search Console spreadsheets and eyeballing crawl reports, an operator asks the agent to mine a year of query data for CTR gaps, keyword cannibalization and pages sliding off page one, then hand back a ranked fix plan it can start working through in the same chat.

**The AI-visibility side is the differentiator: the agent pulls the fan-out searches AI actually runs behind its answers, finds the prompts where the brand never gets mentioned, and turns those gaps into a page-by-page content plan with off-site citation targets.** The plan is grounded in the sources AI already cites in the space, so the off-site work is targeted at domains that already influence answers rather than a generic link-building list. For operators chasing GEO (generative engine optimization), this is the missing measurement layer.

The audit side is equally agent-native: a deep crawl of every sitemap URL with issues ranked by severity, sitemap pages Google has not indexed matched against last Googlebot visits, and per-page diagnostics an agent can fix directly in a Cursor codebase.

## Tools & Capabilities

| Group | What the agent does |
|---|---|
| Search Console mining | Pulls up to a year of query history in one run; finds CTR gaps, cannibalization, decaying pages and featured-snippet targets; builds a prioritized fix plan; refreshes pages sitting in positions 4-30; rewrites titles and H1s against top queries; weekly digests via scheduled tasks |
| AI visibility | Tracks AI mentions across engines; pulls fan-out queries behind answers; clusters gaps into pillars and topics; ranks the domains AI already cites; marks competitors from the brand book |
| Content planning | Builds page-by-page content plans from visibility gaps; researches what ranks for a fan-out query and writes the page; finds Reddit, LinkedIn and Facebook threads AI cites for promotion |
| Technical audit | Deep crawls every sitemap URL with issues by severity; inspects URLs in Search Console; checks index status with Index Rush; adds Crawl Analytics last-visit context; names pages to link from |

## Installation

```bash
claude mcp add --transport http encited https://encited.com/api/mcp
```

Then run `/mcp` inside a session and select `encited` to sign in. For hosted clients, install from the official Claude connector directory (`claude.ai/directory/encited`) or add `https://encited.com/api/mcp` as a custom connector; the browser sign-in window opens on first use.

## Configuration

```json
{
  "mcpServers": {
    "encited": {
      "type": "http",
      "url": "https://encited.com/api/mcp"
    }
  }
}
```

No API key to copy: authentication is OAuth browser sign-in against the Encited account, which holds the Search Console connection, crawl history and tracked brand set.

## Business Relevance

- **SEO managers and agencies** get a year of Search Console data mined in one run with a ranked fix plan instead of a day of spreadsheet work.
- **Growth operators** see exactly which AI prompts their brand loses and a content plan to win them back.
- **Content teams** get research, drafting and optimization workflows from a single prompt, grounded in what already ranks.
- **Founders running vibe-coded or SPA sites** get technical audits and indexing diagnostics for sites Google struggles to crawl.

## Integration with CorpusIQ

Encited reads the search and AI-visibility surface the way CorpusIQ reads business systems. A composed workflow: CorpusIQ GA4 and Search Console connectors provide the revenue and search-query evidence, while Encited's agent workflow digs the CTR gaps, decaying pages and technical issues behind that data and returns the fix plan. For AI-visibility strategy, Encited's fan-out query and citation data pairs with CorpusIQ's source-cited business answers: the operator knows which prompts to win and can then answer them with authoritative, connector-backed numbers instead of marketing prose. Both are read-only surfaces for the agent's first pass; the human approves before anything ships.

## Limitations

- Brand new to this catalog (mcpservers.org listing, no public repo or star history to assess).
- Commercial cloud service - no self-hosting; data flows through Encited's platform.
- Free tier to start, with paid plans beyond it (agency pricing via sales).
- Tool names are not published in vendor docs; the live tool list is served from the endpoint after sign-in.
- Search Console history caps at roughly a year of query data.

## See Also

- [Sorank MCP - Search Console, PageSpeed and AI Citability](/docs/hermes/mcp/servers/external/sorank-mcp)
- [HiBot MCP - ANSWER-Framework AI Visibility Audits](/docs/hermes/mcp/servers/external/hibot-mcp)
- [Tracetify MCP - SEO, GEO and Growth Reports for Agents](/docs/hermes/mcp/servers/external/tracetify-mcp)
- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
