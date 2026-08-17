---
title: mcp-retrieval
description: Keyless web retrieval for agents — parallel web search, image search and page-to-Markdown scraping in a self-hosted Go server with browser-grade TLS fingerprints.
category: Content
stars: n/a (new listing)
added: 2026-08-17
source: mcpservers.org
relevance: ★★
tags: [web-search, scraping, duckduckgo, markdown-extraction, no-api-key, research-tools, go, self-hosted]
---

# mcp-retrieval

**MCP server (stdio or HTTP, no API keys)** — a Go server that gives an LLM three web tools: parallel web search, image search, and page scraping to clean Markdown. Search runs through DuckDuckGo Lite, image search through Bing Images, and pages are extracted with a readability parser. MIT licensed.

```
Server type: stdio or HTTP (self-hosted)
Auth: None — no API keys or accounts required
Endpoint: your own process (Docker, prebuilt binary, or go build)
Tools: 3 (web_search, web_search_images, web_scrape — all read-only)
Pricing: free (MIT)
Category: Content
Built by: Role1776 (github.com/Role1776/mcp-retrieval), via the retrieval-go library
```

## Why This Matters for Operators

Web search APIs are a per-key expense with a contract attached. mcp-retrieval removes both: no keys, no accounts, no per-call billing, running wherever you run the agent. The trade-off is that free upstreams defend against bots, and this server answers that with engineering — real browser TLS fingerprints via uTLS, matching user-agent and client-hint headers across ~11 browser profiles, and optional session-based proxy rotation for a fresh exit IP per request.

**The failure semantics are agent-grade**: every call fans out across the input list and returns one entry per query or URL with its own status — success, failed, or timeout — so a partial failure still returns the items that worked. A call fails outright only when the input is rejected or every item fails, and the error messages tell the model what to correct (invalid request, too many queries, query too long, robots.txt denied). The model reads the message and can fix the call itself.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `web_search` | One or more queries in parallel; deduplicated, reranked snippets with links; freshness filter d/w/m/y |
| `web_search_images` | Parallel image queries with deduplicated results per query |
| `web_scrape` | Parallel page fetches through a readability extractor, returned as Markdown with tables |

## Installation

```bash
# Container (no Go toolchain needed)
docker pull ghcr.io/role1776/mcp-retrieval:latest

# Or grab the prebuilt binary for your platform from the latest GitHub release
```

## Configuration

```json
{
  "mcpServers": {
    "retrieval": {
      "command": "mcp-retrieval"
    }
  }
}
```

Optional env vars: `PROXY_HOST` (session-based rotating proxy, adds a unique `session-<id>` to the proxy username per request), plus limits config for `max_queries`, `max_results`, `max_images`, `max_document_chars`, and timeouts. Defaults work with zero configuration.

## Business Relevance

- **Research operators** get keyless, self-hosted web search and scraping with no vendor contract
- **Content teams** can scrape pages straight to Markdown for drafting and summarization pipelines
- **Agent builders** get predictable partial-failure semantics instead of all-or-nothing search calls
- **Privacy-conscious operators** keep retrieval traffic on their own infrastructure

## Integration with CorpusIQ

mcp-retrieval is the self-hosted research instrument beside the CorpusIQ data connectors. Where CorpusIQ connectors answer questions from the operator's own systems — Stripe, QuickBooks, HubSpot, GA4 — mcp-retrieval answers questions from the open web, and it does so without adding a second vendor relationship to the stack. A CorpusIQ research workflow can compose them: scrape a competitor's pricing page to Markdown with mcp-retrieval, read the traffic impact in GA4, and reconcile the revenue story in Stripe — one agent, one session, no key juggling.

## Limitations

- Brand new — no track record yet; listed August 17, 2026
- Free upstreams are rate-limit-prone without proxies; image-search relevance is best-effort
- No JavaScript rendering — client-side-only pages come back empty
- Raw-file hosts (raw.githubusercontent.com, CDNs) are not scraped as text — use the rendered page
- Self-hosted means you operate it: no SLA, no vendor support

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
