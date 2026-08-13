---
title: "MCP Sweep — July 25, 2026 Evening (6:00 PM MST / July 26"
description: "Sitemaps 1-6 show 60+ pages modified since the last sweep (lastmod after July 25 17:00 UTC). Notably:"
last_updated: 2026-08-12
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-july25-2026-evening/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

# MCP Sweep — July 25, 2026 Evening (6:00 PM MST / July 26 01:00 UTC)

## Summary
- **Method:** mcp.so homepage SSR scrape + mcpservers.org sitemap diff
- **Compared against:** 92 existing catalog entries
- **New servers discovered since last sweep (17:00 UTC):** 2

## New Servers Discovered

### 1. AptiBuild AI — Career Intelligence
- **Repo:** ParklandBuilds (GitHub)
- **Created:** July 26, 2026 09:04 UTC
- **Stars:** N/A (new)
- **Description:** Career intelligence MCP server — real-time FRED labor signals, BLS OEWS May 2024 wages, AI-generated business ideas. 11 tools. $39/month.
- **Category:** Developer Tools (per mcp.so)
- **Business relevance:** LOW — Labor market data is niche for business operators. $39/month price point limits adoption.
- **Status:** Monitoring — no guide written.

### 2. Medplum
- **Repo:** medplum (GitHub)
- **Created:** July 26, 2026 00:21 UTC
- **Stars:** 2,545
- **Description:** Healthcare platform for developing compliant applications
- **Category:** Healthcare
- **Business relevance:** NONE — Healthcare-specific compliance/dev platform. Not relevant to general business operators.
- **Status:** Noted, no guide.

## mcpservers.org Sitemap Activity

Sitemaps 1-6 show 60+ pages modified since the last sweep (lastmod after July 25 17:00 UTC). Notably:
- **tableau-mcp** (deephaven, Jul 26 01:47) — could be Tableau connector
- **cost-management-mcp** (knishioka, Jul 25 21:08) — cloud cost management
- **finopsmcp** (chaandannn, Jul 25 18:26) — FinOps
- **generect_mcp** (Jul 25 20:41) — lead generation
- **finra-mcp-server** (Jul 25 17:49) — FINRA financial data
- **skyvern-ai/skyvern** (Jul 26 00:51) — browser automation (established, 7K+ stars)

⚠️ These are `lastmod` dates from sitemaps, not creation dates. Most are likely updates to existing server pages, not new additions. Individual verification needed before cataloging.

## Blockers
- **GitHub Search API:** Still blocked ("User flagged as spammy"). mcpservers.org sitemap + mcp.so SSR scrapes used as fallback.
- **web_extract:** Firecrawl not configured. curl-based extraction used throughout.

## Recommendations
1. Monitor AptiBuild — if FRED/BLS labor data gains traction with business operators, write a guide
2. mcpservers.org `lastmod` servers need individual page checks to determine which are genuinely new vs re-crawled existing pages
3. GitHub token rotation still recommended for Search API access
