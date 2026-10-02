---
title: "China Hot Trending MCP - Real-Time Social Trend Boards"
description: "Free keyless hosted MCP server for real-time hot-search and trending boards from eight major Chinese platforms: Weibo, Zhihu, Bilibili, Baidu, Toutiao, Douyin, Tieba and Juejin, in a single tool call. Two tools, live-probed (server v1.29.0). Useful for content teams and market intelligence monitoring Chinese social discourse."
category: Content & Research
stars: 0
added: 2026-09-02
source: "mcp.so GitHub issue #3905"
relevance: ★★
tags: [trending, china, social-listening, weibo, douyin, content-research]
---

# China Hot Trending MCP - Real-Time Social Trend Boards

**Hosted Streamable HTTP MCP server** - real-time hot-search and trending boards from eight major Chinese platforms (Weibo, Zhihu, Bilibili, Baidu, Toutiao, Douyin, Tieba, Juejin) in a single MCP call. Verified live with a keyless probe: serverInfo hot-trending-query v1.29.0, both tools returned.

## Spec Block

| Field | Value |
|---|---|
| Server name | hot-trending-query |
| Endpoint | https://mcp.pianam.cn/hot-mcp/mcp |
| Transport | Streamable HTTP, no auth |
| Repo | github.com/boy-373/hot-trending-mcp |
| License | MIT |
| Stars | 0 (new) |
| Docs | README in English and Chinese; server.json registry manifest included |

## Why This Matters for Operators

Chinese social discourse moves fast and is walled off from Western social-listening tools. This server reads public trending boards from eight platforms at once, giving marketing and content operators a zero-setup signal on what Chinese audiences are discussing right now, without API keys or platform registrations.

## Tools & Capabilities (2 tools)

| Tool | Description |
|---|---|
| query_hot_trending | Fetch the current hot-search or trending board for a platform, with an optional limit |
| list_platforms | List the eight supported platforms |

## Installation

Add as a remote MCP server with the endpoint URL. No API key, no auth: paste the URL into any MCP client. The repo ships server.json, smithery.yaml and glama.json manifests for registry indexing.

## Configuration

None required. Public web endpoints upstream; the server is free and stateless.

## Business Relevance

Useful for: brand and content teams tracking Chinese platform trends, market research on Chinese consumer discourse, and monitoring agents that need a daily trend digest from eight platforms in one call.

## Limitations

Trending boards only: no post content, engagement metrics or historical archives. Part of a five-server free package by the same author (train tickets, weather, exchange rates, IP location); this is the business-relevant member. Brand new repo with zero stars.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [Mysocial MCP - Your Real Social Media History as Agent Memory](/hermes/mcp/servers/external/mysocial-mcp)
- [Newsmind MCP - RSS Semantic Search and News Digests for Agents](/hermes/mcp/servers/external/newsmind-mcp)
