---
title: MCP Server Sweep — July 27, 2026 (Evening)
description: "Setup and usage guide for MCP Server Sweep — July 27, 2026 (Evening). Part of the Hermes resource directory."
last_updated: 2026-08-12
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-july27-2026-evening/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

# MCP Server Sweep — July 27, 2026 (Evening)

**Run:** 2026-07-28T02:20 UTC  
**Sources checked:** mcp.so servers sitemaps (pages 18-19, newest), mcpservers.org priority-servers.xml (Jul 27 updates), mcpservers.org servers/1.xml  
**Previous sweep:** sweep-july27-2026-midday.md (2026-07-27T18:05 UTC)

## Summary

| Metric | Count |
|--------|-------|
| Total scanned (post-midday delta) | ~1,500 entries |
| Already cataloged | vast majority |
| New servers (business-relevant) | 5 |
| Integration guides written | 2 |
| Listed only | 13 |

---

## 🔥 MAJOR FIND — Atlassian MCP Server ★★★ Official

**Official Atlassian MCP server** (911⭐). Securely connects Jira, Confluence, Jira Service Management, Bitbucket, and Compass to Claude, ChatGPT, Cursor, VS Code, and other AI tools. OAuth 2.1 or API tokens. `github.com/atlassian/atlassian-mcp-server` (JavaScript). This is the biggest single find of the July 27 sweep cycle — a major enterprise platform shipping an official MCP server. Created August 2025, now at 911 stars with 15+ topic tags. [Guide →](/hermes/mcp/servers/external/atlassian-mcp/)

---

## New Servers — Integration Guides Written (2)

### Atlassian MCP ★★★ Official — July 27 (evening)
Official remote MCP server from Atlassian. Jira, Confluence, JSM, Bitbucket, Compass. OAuth 2.1 + API token auth. 911 stars. `github.com/atlassian/atlassian-mcp-server` · [Guide →](/hermes/mcp/servers/external/atlassian-mcp/)

### GoLogin MCP ★★ — July 27 (evening)
Official GoLogin MCP — browser profile management for multi-account operations. Create, configure, and control GoLogin browser profiles through AI conversations. 18 stars. `github.com/gologinapp/gologin-mcp` · [Guide →](/hermes/mcp/servers/external/gologin-mcp/)

---

## New Servers — Listed Only (13)

### Business-Relevant (no guide — low stars or incomplete)

| Server | Stars | Created | Notes |
|--------|-------|---------|-------|
| **Lusha MCP** | N/A | Jul 27, 2026 | B2B contact enrichment — listed on mcp.so via chatmcp/mcp-directory. Lusha is a real company with an API but no dedicated MCP repo found. |
| **PayPal MCP by CData** | 0 | Jun 2025 | Read-only PayPal data via JDBC driver. CData is a legitimate integration company but this is a low-effort read-only wrapper. Full CRUD available via CData Connect AI (paid). |
| **Salestools MCP** | 0 | May 2026 | Sales prospecting tools — `github.com/akhilkannur/salestools-mcp`. No description, zero stars. |
| **YNAB MCP** | N/A | Jul 27, 2026 | You Need A Budget personal finance — `github.com/Jtewen/ynab-mcp`. Personal finance, not business ops. |
| **Confluence MCP Server** | N/A | Jul 27, 2026 | Third-party Confluence test — `github.com/KS-GEN-AI/confluence-mcp-server`. Described as "a test of confluence mcp server." Superseded by official Atlassian MCP. |

### Niche / Non-Business (no guide)

- **BugBug MCP** — Test automation platform (unofficial). QA tool, not operator-facing.
- **Memora** — Generic memory tool. Low quality, no description.
- **CogMemAI MCP** — AI cognitive memory. Niche.
- **GoLogin MCP** — Already covered above.
- **Accessibility AI** — Web accessibility testing. Dev tool.
- **Propline MCP** — Real estate proptech. Niche.
- **Legal Docs MCP** — Legal document processing. Potentially interesting but no repo found.
- **Disclosure Alpha** — Unknown. No description available.

### CData Series (multiple MCPs by CData Software)

CData has published a series of read-only MCP servers wrapping their JDBC drivers. All follow the same pattern: read-only, Java, free tier, full CRUD via CData Connect AI (paid). These appeared on mcp.so pages 18-19:
- PayPal MCP Server by CData (0⭐)
- Google Data Catalog MCP Server by CData
- Zoho Projects MCP Server by CData

These are not individually cataloged — they're part of CData's broader MCP strategy. The free tier is read-only; write access requires the paid CData Connect AI platform.

---

## Delta from Midday Sweep

The midday sweep (18:05 UTC) processed mcpservers.org /all and mcp.so issues. This evening sweep found:

- **mcp.so pages 18-19** — 80+ servers, of which ~5 are business-relevant and genuinely new (Lusha, Mailchimp, Pagos, YNAB, various CData wrappers). Most are niche, test repos, or duplicates.
- **mcpservers.org priority-servers.xml** — Atlassian MCP Server was listed with a Jul 27 lastmod (19:14 UTC). This is a re-crawl of an existing page — the server has been live since Aug 2025 and is not "new." However, it was MISSING from our catalog. This is the most important find: we had no guide for Atlassian's official MCP.
- **mcpservers.org servers/1.xml** — Mostly re-crawls of existing pages. Stripe, n8n, Apify, and Ahrefs (all cataloged in July 26 evening sweep) showed Jul 27 lastmod dates consistent with re-crawls.

## Source Health

| Source | Status | Notes |
|--------|--------|-------|
| mcp.so servers sitemap | ✅ Healthy | Pages 18-19 fetched, 80+ new entries since morning |
| mcpservers.org priority | ✅ Healthy | 249 entries, 11 with Jul 27 lastmod (mostly re-crawls) |
| mcpservers.org servers/1 | ✅ Healthy | 4,375 entries — re-crawls, not new creations |
| Firecrawl (web_extract) | ❌ Not configured | curl + sitemap used as fallback |
| GBrain | ❌ Command not found | Not impacting this sweep |

---

## git Push Status
Pending — will push after all guides written.
