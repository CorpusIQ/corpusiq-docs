---
title: Site Passport MCP - AI-Agent Readiness Checks for Websites
description: Live-checked AI-agent readiness for WordPress and other sites - llms.txt, AI-crawler robots.txt directives, schema.org markup and WebMCP manifest checks, keyless.
category: SEO
stars: n/a (new listing)
added: 2026-09-09
source: mcpservers.org
relevance: ★★
tags: [aeo, llms-txt, geo, ai-readiness, seo, schema-org, webmcp, remote-mcp]
---

# Site Passport MCP

**Remote MCP server (Streamable HTTP WebMCP, keyless)** - live-checked AI-agent readiness for any website: llms.txt presence, AI-crawler directives in robots.txt, schema.org markup and a WebMCP capability manifest. One tool, no auth, verified against the live site every call.

```
Server type: Remote (Streamable HTTP, WebMCP manifest)
Auth: None (keyless)
Endpoint: https://sitepassport.org/.well-known/mcp.json
Tools: 1 (check_wordpress_agent_readiness)
Pricing: Free
Category: SEO
Built by: Site Passport (sitepassport.org, independent index)
```

## Why This Matters for Operators

Traffic is shifting from search results to AI assistants, and most sites are invisible to the agents doing the answering: no llms.txt, robots.txt that blocks AI crawlers, no structured data for the assistant to quote. **Site Passport turns that visibility gap into a checklist an agent can run for you** - each check is performed against the live site, never against self-reported metadata, so a "ready" verdict means the site is actually crawlable and quotable.

For WordPress operators specifically, the check lands where the decisions land: plugins, robots settings and theme schema markup are all one tool call away from a verdict.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `check_wordpress_agent_readiness` | Live-check a site for llms.txt, AI-crawler robots.txt directives, schema.org markup and a WebMCP manifest |

The tool is published as a WebMCP manifest at the endpoint itself - POST JSON-RPC 2.0 initialize / tools/list / tools/call to the same URL.

## Installation

```bash
claude mcp add site-passport --transport http https://sitepassport.org/.well-known/mcp.json
```

## Configuration

```json
{
  "mcpServers": {
    "site-passport": {
      "type": "http",
      "url": "https://sitepassport.org/.well-known/mcp.json"
    }
  }
}
```

No key, no signup - the endpoint serves its own manifest and answers tool calls directly.

## Business Relevance

- **Operators with WordPress or marketing sites** learn in one call whether AI assistants can find and quote them.
- **Agencies running many client sites** batch readiness checks instead of manually auditing llms.txt and robots files.
- **SEO and AEO teams** get the pre-flight gate before investing in AI-visibility work.
- **Anyone publishing content** verifies the schema.org markup assistants cite before trusting "AI-ready" claims.

## Integration with CorpusIQ

Site Passport pairs with CorpusIQ's AI-visibility tooling: while CorpusIQ surfaces business data to AI engines through its own MCP surface, Site Passport audits whether the operator's public website is ready for AI agents at all. A composed workflow: the assistant checks the site's AI-readiness, then drives the fixes - llms.txt generation, robots directives, schema markup - and re-checks until the verdict flips. Audit, fix, verify, in one loop.

## Limitations

- Brand new - no track record yet.
- Single tool today - a readiness check, not a full SEO or AEO suite.
- WordPress-oriented; generic sites get the same checks but WordPress-specific signals may be deeper.
- Free and keyless now; the index is independent and its long-term shape is unproven.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
