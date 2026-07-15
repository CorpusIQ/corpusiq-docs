---
title: "MCP Server Scan Supplement — July 14, 2026 (Evening)"
description: "Supplemental scan from mcpservers.org (newly accessible) + mcp.so re-scan. 10 additional servers found, 3 business-relevant guides created."
category: mcp
tags: [mcp-scan, discovery, mcp-servers]
last_updated: 2026-07-14
---

# MCP Server Scan Supplement — July 14, 2026 (Evening)

**Sources:** mcpservers.org (JSON payload accessible with browser UA) + mcp.so re-scan
**Date:** July 14, 2026 (evening)
**Previous scan:** July 14, 2026 (morning — 16 servers found)
**GitHub API:** Direct repo queries working; search endpoint still rate-limited

## Methodology

The morning July 14 scan reported mcpservers.org as "Unavailable (SolidJS SPA, no server data in initial HTML)." This supplement used a browser-identifying User-Agent in curl, which returned the full TanStack Router hydration payload with inline server data. Additionally, mcp.so was re-scanned for servers submitted since the morning scan.

## New Since Morning Scan: 10 servers, 3 guides created

### Guide-Worthy (Business-Relevant)

| Server | Source | Description | Guide |
|--------|--------|-------------|-------|
| **Google Search Console MCP** ★ | mcp.so | OAuth-protected GSC analytics for AI agents. Clicks, impressions, rankings, indexing, sitemaps. Hosted or self-host on Cloudflare Workers. By digestseo.com. 2★ | [Guide](/hermes/mcp/servers/external/google-search-console-mcp/) |
| **ComparEdge LLM Cost** ★ | mcpservers.org | Token cost math for 69 models across 17 providers. Free, no API key. Prices verified by ComparEdge. 1★ | [Guide](/hermes/mcp/servers/external/comparedge-llm-cost-mcp/) |
| **Scrivener MCP** ★ | mcp.so | Connect Scrivener manuscripts to AI. 53 tools: document management, writing analysis, semantic search, character/plot tracking. Offline embeddings. 33★ | [Guide](/hermes/mcp/servers/external/scrivener-mcp/) |

### INDEX-ONLY (Business-Adjacent or Niche)

| Server | Source | Description |
|--------|--------|-------------|
| **ComparEdge Price Watch** | mcpservers.org | SaaS price-change history and watch-log for AI assistants. Free, no API key. Companion to LLM Cost MCP. |
| **RedirectBoss** | mcpservers.org | Manage hosts, redirects, SSL, and traffic analytics from AI assistants. Marketing/devops tool. |
| **Dino Markets** | mcp.so | Matched Kalshi and Polymarket prediction market data over MCP. Finance niche. |
| **Jade Note** | mcpservers.org | Notes as AI memory. Memory category already saturated (3+ existing guides). |
| **SelfLabbs Base Intel** | mcpservers.org | Keyless read-only Base on-chain intelligence: wallet balances, token metadata, gas. Crypto niche. |
| **SelfLabbs Security Intel (x402)** | mcpservers.org | Pay-per-call CVE and package-vulnerability lookups via USDC on Base. Security/crypto niche. |
| **Listen (Microphone MCP)** | mcp.so | Microphone capture + speech-to-text for MCP agents. By Decibri. 5★. Agent infrastructure. |

### SKIPPED

| Server | Source | Reason |
|--------|--------|--------|
| **GovAuctions** | mcpservers.org | Government surplus auctions — too narrow for business operators (already skipped in morning scan) |
| **payperlabs** | mcp.so | No description available — cannot evaluate |

## Previously Covered (Morning Scan)

These servers from the morning scan map to the supplement finds:

| Morning Scan Name | Supplement Find | Relationship |
|-------------------|-----------------|--------------|
| SaaS & AI Pricing API | ComparEdge Pricing | Same server — morning scan documented as saas-pricing-mcp.md |
| Writing Style Checker (WSC) | WSC (mcp.so) | Same server — morning scan indexed it |
| Microphone & Speech-to-Text MCP | Listen (mcp.so) | Same server — morning scan indexed it |
| Government Surplus Auction Data | GovAuctions | Same server — morning scan skipped it |

## New Discovery Channel: mcpservers.org

**Important:** mcpservers.org is now accessible for data extraction. The morning scan reported it as unavailable due to raw curl returning only SolidJS shell HTML. A browser-identifying User-Agent (`Mozilla/5.0 Chrome/120.0.0.0`) triggers the server to include the full hydration payload with inline data. This unlocks a second discovery channel beyond mcp.so.

**Pattern for future scans:**
```bash
curl -sL -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" \
  "https://mcpservers.org" | grep -oP '"latest":\K[^]]+\]'
```

mcpservers.org lists 9,800+ servers vs mcp.so's ~500. The `latest` array provides the most recent submissions, complementing mcp.so's feed.

## Trends (Supplemental)

1. **SEO tools enter MCP:** Google Search Console MCP is the first dedicated SEO analytics MCP server. This signals MCP expansion beyond developer tools into marketing operations.
2. **AI cost management category forming:** ComparEdge now has 3 MCP servers (Pricing, LLM Cost, Price Watch) — a suite approach to AI spend intelligence. Watch for this becoming a standalone category.
3. **Professional tool integration:** Scrivener MCP (33★) shows demand for bridging established professional tools (not just developer tools) to AI agents.
4. **Prediction markets via MCP:** Dino Markets brings Kalshi/Polymarket data to MCP — first prediction market connector.

## Actions Taken

- ✅ 3 integration guides created: Google Search Console MCP, ComparEdge LLM Cost, Scrivener MCP
- ✅ 7 INDEX-ONLY entries documented
- ✅ 2 servers skipped (niche/no data)
- ✅ mcpservers.org extraction method documented for future scans
- ✅ Supplemental scan report published

---

*Next scan: July 15, 2026. mcpservers.org now viable as second discovery channel.*
