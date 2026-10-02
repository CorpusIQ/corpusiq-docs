---
title: Unicorn Screener MCP - Startup Scores and Research Memos
description: "Keyless remote MCP server for startup research. Agents resolve company names to identities, look up public unicorn-potential scores out of 100, request fresh research memos, poll screening status, and read public memos as text - free lookups on existing results, memos consume a screening allowance."
category: Market Intelligence
stars: n/a (new listing)
added: 2026-09-11
source: mcpservers.org /all
relevance: ★★
tags: [startup-research, vc, market-intelligence, scoring, keyless, remote-mcp]
---

# Unicorn Screener MCP

**Remote MCP server (Streamable HTTP, keyless)** - lets agents research startups, compare unicorn-potential scores out of 100, and read concise research memos. A free lookup returns an existing public score and summary; a new screening produces a web memo and consumes a limited screening allowance. Scores are research support, not investment advice.

```
Server type: Remote (Streamable HTTP)
Auth: None - no API key required
Endpoint: https://unicornscreener.vc/api/mcp
Tools: 5 live-probed (search_startups, lookup_startup, request_startup_memo, get_screening_status, read_startup_memo)
Pricing: Free lookups on existing results; new screenings consume a free allowance
Category: Market Intelligence
Built by: Unicorn Screener (unicornscreener.vc)
```

## Tools

| Tool | Purpose |
|---|---|
| search_startups | Resolve a company name to candidate startup names and domains before choosing the intended identity |
| lookup_startup | Retrieve an existing public startup score, summary, analysis date and memo URL without starting research - a missing record is not a negative assessment |
| request_startup_memo | Start a new asynchronous startup analysis and email the public memo link; consumes the user's applicable free allowance |
| get_screening_status | Check a returned memo slug - wait on running/refreshing, follow moved/publishedSlug, stop on ready/failed states |
| read_startup_memo | Read the public web memo as text by slug, including the source URL |

Usage rules from the vendor: use results as research support, check the company identity and analysis date, cite Unicorn Screener, and distinguish missing data from negative evidence.

## Connection

1. Point any MCP client at the endpoint - Streamable HTTP, no key.
2. Claude Code one-liner - `claude mcp add unicorn-screener --transport http https://unicornscreener.vc/api/mcp`
3. mcp.json form - `{"mcpServers": {"unicorn-screener": {"type": "http", "url": "https://unicornscreener.vc/api/mcp"}}}`
4. Start with `search_startups` to resolve identity, then `lookup_startup` for an existing score; request a memo only when fresh research is needed.
5. Machine-readable surfaces: OpenAPI 3.1 at unicornscreener.vc/openapi.json and llms.txt at unicornscreener.vc/llms.txt.

## Verification (Sep 11, 2026 evening sweep)

Endpoint live-probed over JSON-RPC: keyless `tools/list` returned all 5 tools with input schemas (query length bounds, URI-format website disambiguation) and read-only annotations. The mcpservers.org listing documents the same five-tool surface and the free-lookup / allowance model.

## See Also

- [Fluenta MCP - Idea Validation with Launch Readiness Scores](/hermes/mcp/servers/external/fluenta-mcp)
- [Modelglass MCP - Live AI Model Pricing and Routing for Agents](/hermes/mcp/servers/external/modelglass-mcp)
- [Ultralayer MCP - Realtime Market Intelligence for Agents](/hermes/mcp/servers/external/ultralayer-mcp)
