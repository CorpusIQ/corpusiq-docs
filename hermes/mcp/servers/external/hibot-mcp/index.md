---
title: "HiBot MCP - ANSWER-Framework AI Visibility Audits"
description: "Measure how ChatGPT, Perplexity, Google, Claude and Grok surface and recommend your brand with HiBot's ANSWER framework, exposed as seven read-only public MCP tools."
category: SEO
stars: n/a (new listing)
added: 2026-09-03
source: mcp.so
relevance: ★★★
tags: [aeo, ai-visibility, brand-monitoring, answer-engines, marketing, analytics, remote-mcp]
---

# HiBot MCP

**Remote MCP server (Streamable HTTP, no auth on public endpoint)** - HiBot measures how AI answer engines surface, recommend and represent brands, using a proprietary ANSWER framework, and serves that knowledge as seven read-only MCP tools over a public endpoint plus a Bearer-key endpoint for a customer's own delivered audits.

```
Server type: Remote (Streamable HTTP)
Auth: None (public endpoint); Bearer API key (private endpoint)
Endpoint: https://hibot.com/mcp/public (public); https://hibot.com/mcp (private)
Tools: 7 public (methodology, plans, case studies, blog search)
Pricing: Free public endpoint; private audits delivered per engagement
Category: SEO
Built by: HiBot (github.com/flevy-com/hibot-mcp)
```

## Why This Matters for Operators

AI visibility is the new organic search, and it is nearly impossible to self-measure: every answer engine ranks differently, sessions are logged out, and your own prompts bias what you see. HiBot runs audits in logged-out, neutral sessions by human specialists and delivers a scored report plus an actionable plan.

**The public MCP server turns the framework itself into tooling:** an agent can pull the ANSWER methodology (six categories, rubric, weights, score bands), the Pulse and Panorama audit plans, published case studies and research articles, and reason with them directly. The private endpoint then serves a customer's own audit results - scores, what each engine answered, the hallucination log, citations and competitive standing - so an agent can act on them.

## Tools & Capabilities

Seven public tools, all read-only, every result linking back to hibot.com:

| Tool | Purpose |
|---|---|
| get_answer_methodology | The six ANSWER categories, rubric, weights and score bands |
| get_plans | The Pulse and Panorama audit plans |
| list_case_studies / get_case_study | Published audits of real brands |
| list_blog_articles / get_blog_article / search_blog | HiBot's research on AI visibility |

The private endpoint (Bearer key minted at hibot.com/account/api-keys) serves a customer's own audits: scores, engine answers, hallucination log, citations, competitive standing and re-audit trends.

## Installation

```bash
claude mcp add --transport http hibot-public https://hibot.com/mcp/public
```

## Configuration

```json
{
  "mcpServers": {
    "hibot-public": {
      "type": "http",
      "url": "https://hibot.com/mcp/public"
    }
  }
}
```

For a customer's own audits, point the client at https://hibot.com/mcp and attach the API key minted from the HiBot account page as the authorization header.

## Business Relevance

- **Brand marketers** learn whether AI engines recommend their brand and why not
- **Agencies** run ANSWER-framework audits as a client deliverable
- **Content operators** get a concrete rubric for making pages AI-citable

## Integration with CorpusIQ

HiBot reads the AI engines while CorpusIQ reads the business: a composed workflow pairs CorpusIQ's GA4 and revenue connectors with HiBot's audit results to connect AI visibility to actual commercial outcomes - "we gained 40% share of AI answers this quarter, here is the traffic and revenue delta from CorpusIQ." CorpusIQ's own AEO work on docs and llms.txt gets an external measurement loop through the ANSWER framework, turning visibility into a scored, tracked KPI.

## Limitations

- Brand new listing with no public track record yet
- Public endpoint carries methodology and case studies, not your own audit data - that needs the private key and a HiBot engagement
- Audits run on human-specialist timelines, not on demand
- No self-host option

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [Ranki MCP - Free SEO and AEO Audits for AI Agents](/hermes/mcp/servers/external/ranki-mcp)
- [Prognosite MCP - SEO and AEO Intelligence for Publishers](/hermes/mcp/servers/external/prognosite-mcp)
- [Tracetify MCP - SEO, GEO and Growth Reports for Agents](/hermes/mcp/servers/external/tracetify-mcp)
- [Sorank MCP - Search Console, PageSpeed and AI Citability](/hermes/mcp/servers/external/sorank-mcp)
