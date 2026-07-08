---
title: "MCP Server Discovery — July 3, 2026"
description: "Daily scan of mcp.so and mcpservers.org. 6 new business-relevant MCP servers across scheduling, meeting notes, finance, ecommerce, and social media categories."
category: mcp
tags: [mcp-servers, daily-scan, july-2026]
last_updated: 2026-07-08
---

# MCP Server Discovery — July 3, 2026

**Source:** mcpservers.org (featured + latest), mcp.so, GitHub API
**Method:** Multi-source sweep (directory listing, GitHub search, community signals)
**Date:** July 3, 2026
**Prior scan:** [July 2 evening](/hermes/mcp/servers/external/scan-results-2026-07-02-evening/)

## Summary

| Metric | Count |
|--------|-------|
| Total servers screened | 30 (mcpservers.org) + 155 (mcp.so) |
| Already catalogued (prior scans/guides) | 40 |
| Well-known/skipped | 18 |
| **New business-relevant** | **6** |
| **Full integration guides created** | **6** |

## Priority Servers — Full Integration Guides Created

| # | Server | Category | Description | Source |
|---|--------|----------|-------------|--------|
| 1 | **Cal.com MCP** | Scheduling & Productivity | Official Cal.com MCP for AI-powered scheduling. Create event types, check availability, book meetings from AI agents. Remote endpoint at `mcp.cal.com`. | mcpservers.org |
| 2 | **Granola MCP** | Meeting Notes & Productivity | Official Granola MCP for AI meeting notes. Search transcripts, extract action items, query meeting history from AI agents. | mcpservers.org |
| 3 | **Co-Invest MCP** | Finance & Investing | Invest with AI agents. Market research, portfolio analysis, trade execution, strategy backtesting. Built on Liquid Trade infrastructure. | mcpservers.org |
| 4 | **Alpha Vantage MCP** | Finance & Market Data | 20+ years of financial data via MCP. Stocks, ETFs, forex, crypto, commodities, 50+ technical indicators, fundamentals. Free tier available. | mcpservers.org |
| 5 | **Webotee Amazon MCP** | Ecommerce & Amazon Intelligence | Amazon seller research MCP. Buy-box history, competitor analysis, niche discovery, brand intelligence. Built for Amazon operators. | mcpservers.org |
| 6 | **OpenTweet MCP** | Social Media & Marketing | X/Twitter management MCP. Post, search, engage, analyze — complete X presence management from AI agents. | mcpservers.org |

## Additional Notable Servers (Indexed, No Individual Guide)

| Server | Category | Description | Source |
|--------|----------|-------------|--------|
| **NotebookLM MCP** | Research & Productivity | Google NotebookLM via MCP — source-grounded answers from your notebooks. | mcpservers.org |
| **getmcpauth** | Infrastructure & Auth | Hosted OAuth 2.1 + Dynamic Client Registration (RFC 7591) for MCP servers. | mcpservers.org |
| **memo (jagoff/memo)** | AI Infrastructure | Local-first long-term memory for coding agents — MLX/CPU embeddings, hybrid vector+BM25 search. | mcpservers.org |
| **CloudMesh AI** | DevOps & Infrastructure | Vendor-neutral gate between AI agents and production infrastructure with human-in-the-loop approval. | mcpservers.org |

## GitHub API Results

GitHub search for `topic:mcp-server pushed:>2026-07-02` returned 0 new results — no new MCP servers pushed to GitHub since the July 2 evening scan. The July 2 scans captured the pipeworx-io batch (18+ servers) and other discoveries comprehensively.

## Trends

- **Scheduling goes MCP-native**: Cal.com MCP represents the first major scheduling platform to release an official MCP server. Expect Calendly, SavvyCal, and others to follow.
- **Meeting notes become queryable**: Granola MCP transforms meeting notes from passive records to active knowledge bases accessible by AI agents. This is the "second brain" pattern — institutional knowledge that agents can query.
- **Finance vertical deepens**: With Co-Invest MCP, Alpha Vantage MCP, plus existing SentiSense, Kalshi, and HPSILab Quant, operators now have a complete AI-driven investment stack — research, analysis, sentiment, execution, and prediction markets.
- **Amazon sellers get AI-native tools**: Webotee Amazon MCP signals that ecommerce intelligence tools are adopting MCP as a distribution channel. This is a major underserved market — 2M+ Amazon sellers need better research tools.
- **Social media management goes agentic**: OpenTweet MCP represents a shift from dashboard-based social media management to agentic workflows. The "compose thread, schedule, monitor engagement" loop moves entirely into AI conversations.
- **Infrastructure & auth MCPs emerge**: getmcpauth and CloudMesh AI represent the "picks and shovels" layer — infrastructure that makes MCP servers easier to build and deploy securely.

## Actions Taken

- 6 full integration guides created for priority servers (see individual `.md` files in this directory):
  - `calcom-mcp.md`
  - `granola-mcp.md`
  - `coinvest-mcp.md`
  - `alphavantage-mcp.md`
  - `webotee-amazon-mcp.md`
  - `opentweet-mcp.md`
- 4 additional servers noted (indexed, no individual guide — too niche or infrastructure-layer)
- Index.md updated with new server entries

## Non-Business Servers (Not Catalogued)

- Safari MCP (Apple) — developer tooling, not business-operations
- webear/web perception — developer debugging tool
- Various browser automation MCPs (Browserbase, Cloudflare) — developer tools
- MiniMax MCP — AI media generation (creative, not business operations)
- Devin/DeepWiki — developer codebase context
- Next.js DevTools MCP, Proxyman MCP, Railway MCP — developer infrastructure
- XcodeBuildMCP — iOS development
