---
title: "Sweep Report — July 30, 2026"
date: 2026-07-30
sources: mcpservers.org sitemaps (1-6 + priority), mcp.so /servers SSR
status: complete
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-july30-2026-morning/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["mcp server", "model context protocol", "hermes mcp"]
description: "Morning sweep of mcpservers.org sitemaps (6 server sitemaps + priority sitemap) and mcp.so /servers page (76 servers on first page)."

---

# MCP Directory Sweep — July 30, 2026

## Summary

Morning sweep of mcpservers.org sitemaps (6 server sitemaps + priority sitemap) and mcp.so /servers page (76 servers on first page). Firecrawl + web_extract DOWN — used curl + sitemap scanning (proven fallback). Last comprehensive sweep was July 29 afternoon (~20 hours ago).

**Result:** 1 business-relevant server discovered (IBANforge), ~300+ sitemap re-indexes noted. mcpservers.org still at ~10,377 servers. mcp.so at 18,065 servers.

---

## ★★ Business-Relevant (1 Guide Written)

### IBANforge MCP ★★ — July 30
**IBAN validation, BIC/SWIFT lookup, Swiss clearing, and EMI/vIBAN classification via MCP.** AI agents validate international bank details before initiating payments. 6 tools: validate-iban, lookup-swift, lookup-iban, swiss-clearing, classify-emi, classify-viban. TypeScript (Hono), SQLite-backed, remote Streamable HTTP. Free tier available. First dedicated banking-compliance MCP server. `github.com/cammac-creator/ibanforge` (2⭐) · [Guide →](/hermes/mcp/servers/external/ibanforge-mcp/)

---

## ★ Noted (No Guides)

| Server | Source | Category | Notes |
|--------|--------|----------|-------|
| Orders of Magnitude — x402 API Catalog | mcp.so featured | Agent Infrastructure | 1000+ pay-per-call API endpoints via x402 on Base/USDC. Finance, weather, geography, economic data. Interesting but infrastructure-layer, not direct business tool. `github.com/OrdersOfMagnitudeLLC` |
| Termany | mcp.so featured | Developer Tools | Agent-Native Terminal. Developer-focused, not business-ops. |
| Floors.live | mcp.so featured | Events | Event floor plan designer with 32 tools. Niche (event planning). |
| Glasswarp | mcp.so featured | Infrastructure | See and control a real Windows PC from MCP. BYOH. DevOps/IT, not business-ops. |

---

## Already Covered / Developer Tools / Skipped

- **mcpservers.org priority sitemap (July 30 entries):** All 12 servers are re-indexes of existing major servers (chrome-devtools, context7, github, metabase, n8n, sentry, serena, stripe, supabase, terraform, desktop-commander). No new business servers.
- **mcpservers.org sitemaps 1-6 (300+ unique July 30 slugs):** Overwhelmingly GitHub usernames (individual developer repos). Product-name slugs (cloudflare, grafana, neo4j, figma, thoughtspot, bucketco, etc.) are re-indexes of existing servers, not new creations.
- **mcp.so first page remaining servers:** All previously catalogued or developer/consumer tools (PuzzleTide, Dadan, Kavel, SVGator, Designesy, extentos, etc.)

---

## Notable Ecosystem Observation

The mcpservers.org `lastmod` field does NOT equal creation date. Over 300+ server pages were re-crawled on July 30, but these are overwhelmingly re-indexes of existing pages — not new server submissions. The sitemap-based discovery approach is becoming less useful for finding genuinely new servers; the mcp.so featured/newest page is a better signal for new submissions.

---

## Sources Used

- ✅ mcpservers.org sitemaps (1-6 + priority): curl + grep for July 30 lastmod entries
- ✅ mcp.so /servers: SSR extraction (76 servers on page 1)
- ✅ GitHub API: repo verification for IBANforge
- ✅ Cross-reference: grep against 121+ existing catalog entries
- ❌ Firecrawl API: not configured
- ❌ web_extract: not configured
- ❌ web_search: not configured

---

## Stats

| Metric | Value |
|--------|-------|
| mcpservers.org total servers | ~10,377 (stable) |
| mcp.so total servers | 18,065 (stable) |
| Sitemap pages scanned | 7 (servers/1-6 + priority) |
| July 30 sitemap entries | 300+ (mostly re-indexes) |
| mcp.so page 1 servers checked | 76 |
| New to catalog (not in 121 entries) | 7 (6 niche + 1 business) |
| Business-critical new finds | 0 |
| Business-relevant guides written | 1 (IBANforge) |
| Total catalog after sweep | 122 entries (+1) |
