---
title: "Sweep Report — July 29, 2026 (Morning)"
date: 2026-07-29
sources: mcpservers.org sitemaps, mcp.so SSR
status: complete
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-july29-2026-morning/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["mcp server", "model context protocol", "hermes mcp"]
description: "Sweep of mcpservers.org sitemaps (servers/1-6.xml + priority-servers.xml) and mcp.so SSR extraction."

---

# MCP Directory Sweep — July 29, 2026 (Morning)

## Summary

Sweep of mcpservers.org sitemaps (servers/1-6.xml + priority-servers.xml) and mcp.so SSR extraction. Firecrawl + web_search DOWN — used curl-based sitemap scraping (proven fallback pattern). Scanned 175 servers with `lastmod=2026-07-29`, cross-referenced against existing 229-entry catalog.

**Result:** 3 business-critical servers discovered (all absent from catalog), 4 secondary finds noted. 161 false positives (re-indexed existing pages with today's `lastmod`).

---

## ★★★ Business-Critical (3 Guides Written)

### Tableau MCP ★★★ Official — July 29
**Official Tableau MCP server — 315⭐, TypeScript. Created May 2025.** AI agents connect directly to Tableau Cloud/Server to query data sources, list workbooks, execute calculated fields, and retrieve visualizations. The second major BI platform to ship MCP after Metabase (July 26). Remote Streamable HTTP. `github.com/tableau/tableau-mcp` · [Guide →](/hermes/mcp/servers/external/tableau-mcp/)

### Meta Ads MCP ★★★ — July 29
**Pipeboard Meta Ads MCP — 1,112⭐, Python.** Connect AI agents to Facebook/Instagram Ads: campaign management, ad set optimization, creative analysis, audience insights, and performance reporting. Part of Pipeboard's 5-platform advertising family (also Google, TikTok, Snap, Reddit). Hosted remote MCP with Meta Business verification badge. Essential for e-commerce and DTC operators running paid social. `github.com/pipeboard-co/meta-ads-mcp` · [Guide →](/hermes/mcp/servers/external/meta-ads-mcp/)

### Salesforce MCP ★★★ — July 29
**Community Salesforce MCP connector — 179⭐, Python.** Connect AI agents to Salesforce CRM: accounts, contacts, opportunities, leads, cases, reports, and custom objects via the Salesforce REST API. Not official (community-maintained by smn2gnt) but well-implemented with comprehensive object coverage. First dedicated Salesforce MCP server. `github.com/smn2gnt/MCP-Salesforce` · [Guide →](/hermes/mcp/servers/external/salesforce-mcp/)

---

## ★★ Secondary Finds (Noted, No Guides Yet)

| Server | Stars | Official | Category | Notes |
|--------|-------|----------|----------|-------|
| Grafana MCP | 3,299⭐ | ✅ Official | Observability | Major platform. More DevOps than business-ops. `grafana/mcp-grafana` |
| Netlify MCP | 49⭐ | ✅ Official | Hosting/Deploy | Platform deployment from AI agents. `netlify/netlify-mcp` |
| Buildkite MCP | 52⭐ | ✅ Official | CI/CD | Pipeline management from AI agents. `buildkite/buildkite-mcp-server` |
| Help Scout MCP | 46⭐ | Community | Customer Support | Search conversations, threads, inboxes. `drewburchfield/help-scout-mcp-server` |

---

## ★ Noted (No Guides)

| Server | Stars | Notes |
|--------|-------|-------|
| Socket MCP | 121⭐ | Security vulnerability scanning |
| Couchbase MCP | 34⭐ | NoSQL database operations |
| Opal Security MCP | 3⭐ | Access governance |
| AgentMail MCP | 59⭐ | Email for AI agents |
| Longbridge MCP | 12⭐ | Financial trading (HK/US stocks) |

---

## Developer Frameworks (Skipped)

Significant framework/toolkit updates noted but excluded from business-ops catalog:
- **FastMCP** (26,932⭐) — Python MCP framework by PrefectHQ. Developer tool.
- **mcp-use** (10,423⭐) — Fullstack MCP app framework. Developer tool.
- **IBM Context Forge** (4,154⭐) — AI Gateway/proxy for MCP/A2A/REST. Infrastructure.
- **CUA** (20,744⭐) — Computer Use Agent framework. Developer/research tool.

---

## Sources Down / Fallback Used

- ❌ Firecrawl API: not configured
- ❌ web_search: not configured  
- ❌ web_extract: not configured
- ✅ mcpservers.org sitemaps: curl + XML parsing — worked
- ✅ mcp.so SSR: curl + binary-stripping + regex — worked (60 entries)
- ✅ GitHub API: enrichment successful (token auth)

---

## Stats

| Metric | Value |
|--------|-------|
| mcpservers.org sitemap pages scanned | 175 with lastmod 2026-07-29 |
| Genuinely new (not in catalog) | ~164 raw hits |
| False positives (re-indexed) | ~161 |
| Business-critical new finds | 3 (Tableau, Meta Ads, Salesforce) |
| Secondary finds | 4 (Grafana, Netlify, Buildkite, Help Scout) |
| Guides written | 3 |
| Total catalog after sweep | 232 entries |
