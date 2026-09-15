---
title: Google Search Console MCP (ni-c) - Property Setup and Search
description: "Open-source stdio MCP server that sets up and operates Google Search Console: property creation and verification, sitemap submission, URL index checks, and Performance report queries across three Google APIs."
category: Marketing
stars: n/a (new listing, ni-c/google-search-console-mcp)
added: 2026-08-29
source: "chatmcp/mcpso issue #3824"
relevance: ★★
tags: [mcp-server, google-search-console, seo, sitemaps, indexing, search-analytics, marketing, self-hosted]
---

# Google Search Console MCP (ni-c)

**An open-source stdio MCP server that operates Google Search Console across three Google APIs - Search Console v1, Site Verification, and the Indexing API - so an agent can create a property from nothing, prove ownership, submit sitemaps, and query the Performance report.** The differentiator is write-side setup: because the server also speaks Site Verification and Indexing APIs, it can do the four-step ownership dance (token, DNS/page placement, verify, add) and tell the operator exactly which step is missing via a setup_site tool. MIT-licensed, published on npm with provenance and as a multi-arch container.

```
Server type: Local (stdio) - npm package @ni-c/google-search-console-mcp
Auth: Google OAuth (Search Console, Site Verification, Indexing scopes)
Endpoint: n/a (stdio; talks to three Google APIs over HTTPS)
Tools: 21 (setup_site, verify_site, submit_sitemap, inspect_url, query_search_analytics, more)
Pricing: Free open source (MIT); Google API quotas are your own
Category: Marketing / SEO
Built by: ni-c/google-search-console-mcp; MIT
```

## Why This Matters for Operators

Search Console v1 has no notion of ownership, so a server built on it alone can only read properties somebody already verified by hand. This server closes that gap: setup_site compares the two ownership lists, names the missing step, and hands over the exact DNS record to paste. The irreversible operations sit behind a confirmation token, and the write tools can be switched off entirely with an environment variable.

The Performance report query returns a compact table with CTR computed from totals rather than averaged across rows, and URL inspection works singly or in batches. For an operator standing up a new domain or fixing indexing, the whole flow - token, verify, add property, sitemap, index check - becomes a conversation instead of a console crawl.

**Property creation and sitemap submission become agent tasks, with the dangerous steps gated behind confirmation tokens.**

## Tools & Capabilities

21 tools, narrowable via GSC_ALLOW_TOOLS (essential = curated five).

| Tool | Purpose |
|---|---|
| `setup_site` | Walk the four-step ownership flow, compare ownership lists, and hand over the exact DNS record to paste |
| `get_verification_token`, `verify_site` | Obtain and apply Site Verification tokens |
| `get_site`, `get_verified_site`, `list_sites`, `list_verified_sites` | Read property and verified-site state |
| `add_site`, `delete_site`, `unverify_site`, `update_site_owners` | Manage properties and owners (confirmation-token gated) |
| `submit_sitemap`, `submit_sitemaps`, `list_sitemaps`, `delete_sitemap` | Sitemap lifecycle - submitting is an idempotent PUT, so resubmitting is updating |
| `inspect_url`, `inspect_urls`, `get_indexing_status`, `request_indexing` | URL index status and Indexing API requests |
| `query_search_analytics` | Full Performance report as a compact table with totals-derived CTR |

## Installation

```bash
claude mcp add gsc-ni-c --env GSC_ALLOW_TOOLS=essential -- npx -y @ni-c/google-search-console-mcp
```

Full docs at google-search-console-mcp.ni-c.de, including OAuth setup per client and the essential-tool preset. A container image is published at ghcr.io/ni-c/google-search-console-mcp.

## Configuration

```json
{
  "mcpServers": {
    "gsc-ni-c": {
      "command": "npx",
      "args": ["-y", "@ni-c/google-search-console-mcp"],
      "env": { "GSC_ALLOW_TOOLS": "essential" }
    }
  }
}
```

Google OAuth flows on first run for the three API scopes. Set GSC_ALLOW_TOOLS to `essential` for the curated five tools or name specific tools to narrow the surface.

## Business Relevance

- **SEO operators** create and verify new properties without the manual ownership dance, then submit sitemaps in the same conversation.
- **Agencies onboarding new clients** script the four-step property setup across domains with setup_site naming the exact missing step.
- **Content teams** batch-inspect URL index status and request indexing after launches.
- **Analysts** query the Performance report as a clean table with correct CTR instead of exporting from the console.

## Integration with CorpusIQ

This server's read side pairs directly with CorpusIQ's SEO surfaces: CorpusIQ runs the docs SEO/AEO/GEO pass and GA4 signup attribution, and this server adds the GSC write path - property verification, sitemap submission, and indexing requests - that turns a CorpusIQ-generated SEO action list into executed changes. A CorpusIQ workflow can compare query_search_analytics output against CorpusIQ's GA4 connectors to connect search clicks to signups, and hand the corrective actions (new sitemap, indexing request) straight back to the agent through this server's tools.

## Limitations

- Brand new - repo created August 28, 2026, zero stars; npm and container artifacts are published.
- A second Google Search Console server in this catalog (see yusofansari's 43-tool read-only server) - this one differentiates on the write-side setup workflow.
- stdio only - no hosted endpoint; agents run it where they have shell access.
- Google API quotas and OAuth scopes (Search Console, Site Verification, Indexing) apply to your project.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [Google Search Console MCP - Integration Guide](/docs/hermes/mcp/servers/external/google-search-console-mcp)
- [Otto MCP - Live Marketing Data and Website Operations in Chat](/docs/hermes/mcp/servers/external/otto-mcp)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
