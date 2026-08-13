---
title: "MCP Sweep — July 31, 2026 (Early Morning)"
description: "Early morning sweep following the July 30 afternoon AfterLaunch find. Checked mcp.so GitHub issues, mcp.so /servers SSR, and mcpservers.org sitemaps."
date: 2026-07-31T03:02:00-07:00
sources: [mcp.so, chatmcp/mcpso, mcpservers.org]
status: complete
finds: 3
guides: 3
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-july31-2026-early/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

# MCP Server Discovery Sweep — July 31, 2026 Early Morning

## Summary

- **3 genuinely new business-relevant servers found** — The Bot Wire, Pangolinfo Amazon Data MCP, Primate Intelligence
- **3 integration guides written**
- **Cross-referenced against 197 existing catalog entries**
- **mcpservers.org sitemaps continue to show re-indexes** — all existing servers with July 31 lastmod dates
- **Firecrawl/web_extract still DOWN** — used curl-based discovery throughout

## Methodology

1. **mcp.so GitHub issues (chatmcp/mcpso):** Checked 15 most recent open issues sorted by creation date. This remains the best signal for genuinely new servers.
2. **mcp.so /servers page (SSR extraction):** Extracted server name/slug pairs from TanStack SSR state. Cross-referenced against existing catalog.
3. **mcpservers.org sitemaps (1-6 + priority):** Scanned all sitemaps for new slugs and July 31 lastmod dates. All ~25+ with July 31 lastmod were re-indexes of existing well-known servers.

## Findings

### ★★★ The Bot Wire — Catalogued with Guide

**What:** 40 real-time primary-source data wires covering SEC EDGAR filings, Federal Register rules, federal court opinions (Supreme Court, 2nd/9th/Federal Circuits), congressional bills, SEC/FTC enforcement actions, DOJ announcements, FDA approvals, Federal Reserve/FOMC statements, ECB policy releases, BLS/BEA economic releases, CISA CVEs, and cloud provider status.

**Why it matters:** First MCP that reads primary regulatory/legal/economic sources directly instead of coverage of them. AI agents can answer questions about post-cutoff events with original-source citations. Essential for compliance officers, financial analysts, competitive intelligence teams, and legal researchers. No news aggregation layer — reads original documents.

**Details:**
- Remote MCP: `https://thebotwire.com/mcp` (Streamable HTTP)
- GitHub: `ArasPasha/botwire-mcp` (0★, created July 27, 2026)
- npm: `npx botwire-mcp`
- Registry: `io.github.ArasPasha/botwire-mcp`
- Free tier available

**Guide:** `/hermes/mcp/servers/external/botwire-mcp/`

---

### ★★ Pangolinfo Amazon Data MCP — Catalogued with Guide

**What:** 19 e-commerce and IP-compliance data tools — Amazon product/review/search/niche/bestseller data, AI SERP & keyword trends, local Maps POI data, WIPO trademark search, and PACER patent litigation.

**Why it matters:** Consolidates Amazon marketplace intelligence + IP legal tools in a single MCP. E-commerce operators get product research and competitive analysis; IP lawyers get trademark/patent search without switching platforms. First MCP to bridge marketplace operations and IP compliance.

**Details:**
- Remote MCP: `https://mcp.pangolinfo.com/mcp` (Streamable HTTP)
- GitHub: `Pangolin-spg/pangolinfo-mcp` (0★, created July 31, 2026 — same day)
- Docs: `docs.pangolinfo.com`
- PyPI: `pangolinfo-mcp` (Python client)
- Free API key: `tool.pangolinfo.com`

**Guide:** `/hermes/mcp/servers/external/pangolinfo-mcp/`

---

### ★★ Primate Intelligence — Catalogued with Guide

**What:** Real-time video analysis and scene understanding for AI agents via predictive world models. Register videos by URL, ask questions in plain English, get deterministic yes/no/indeterminate answers with confidence scores and clip timestamps. No hallucinated descriptions.

**Why it matters:** First MCP for video scene understanding with auditable results. Content monitoring teams can check competitor videos for claims/messaging. Operations teams can verify video content at scale without watching. Uses predictive world models — deterministic instead of hallucinated.

**Details:**
- Remote MCP: `https://api.primateintelligence.ai/mcp` (OAuth 2.1 + Dynamic Client Registration + PKCE)
- GitHub: `Primate-Intelligence/primate-intelligence-mcp` (0★, created July 26, 2026)
- npm: `@primate-intelligence/mcp`
- 10 tools with MCP annotations

**Guide:** `/hermes/mcp/servers/external/primate-intelligence-mcp/`

---

### Other Submissions (Not Catalogued)

| Server | Type | Reason Skipped |
|--------|------|----------------|
| ClawJob (#3373) | Agent task marketplace | Dev tool — not business-operations |
| GoodMemory (#3374) | Local-first memory | Dev tool — agent infrastructure |
| bomly (#3380) | Dependency graphs for coding | Dev tool — software development |
| NameWhisper (#3381) | ENS intelligence | Crypto niche — narrow audience |
| plori (#3377) | Cloud computers for agents | Dev tool — agent infrastructure |

### mcpservers.org Sitemap Re-Indexes

~25+ servers with July 31 lastmod dates across sitemaps 1-6 and priority. All confirmed as re-indexes of well-known existing servers (Storybook, Microsoft, Qdrant, ClickUp, Metabase, Sentry, Stripe, StackOverflow, etc.) — not new creations. The `lastmod` field continues to reflect re-crawl date, not creation date.

## Catalog Status After Sweep

- **Servers:** 128 (+3 from July 30 afternoon)
- **Guides:** 28 (+3 from July 30 afternoon)
- **This sweep's additions:** The Bot Wire (★★★), Pangolinfo (★★), Primate Intelligence (★★)

## Notes

- mcp.so GitHub issues remain the best signal for genuinely new servers — all 3 catalogued servers appeared there first
- mcpservers.org sitemaps continue to show re-indexes with current dates — every July 31 lastmod was an existing server, not a new creation
- The Bot Wire fills a major gap: primary-source regulatory/legal/economic data for AI agents. No other MCP reads SEC EDGAR, Federal Register, federal court opinions, and Fed statements directly
- Pangolinfo represents a growing trend: MCP servers consolidating multiple previously-separate tool categories (marketplace intelligence + IP law)
- Primate Intelligence is the first MCP with predictive world models for video — fundamentally different approach from vision AI wrappers
- Firecrawl/web_extract continue to be DOWN — used curl-based SSR, GitHub API, and native HTTPS throughout
