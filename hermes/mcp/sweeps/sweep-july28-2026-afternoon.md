---
title: "MCP Server Sweep — July 28, 2026 (Afternoon)"
description: "Afternoon sweep of mcpservers.org sitemaps and mcp.so for new business-relevant MCP servers. Major finds: LinkedIn MCP, Apollo.io MCP, Browserless MCP."
date: 2026-07-28
type: sweep
sources: ["mcpservers.org/sitemaps/servers/5.xml", "mcpservers.org/sitemaps/servers/6.xml", "mcpservers.org/sitemaps/priority-servers.xml"]
new_servers: 5
new_guides: 5
---

# MCP Server Sweep — July 28, 2026 Afternoon

**Run time:** ~17:00 UTC, July 28, 2026
**Previous sweep:** July 28, 2026 07:10 UTC (morning)
**Method:** mcpservers.org sitemap parsing (servers 5 & 6 + priority-servers), mcp.so SSR extraction
**Total new servers scanned:** 46 across today's sitemaps
**Business-relevant discovered:** 5

## Methodology

Since Firecrawl remains DOWN, this sweep used:
1. **mcpservers.org sitemaps** — fetched `/sitemaps/servers/5.xml` and `/sitemaps/servers/6.xml` (newest entries), plus `/sitemaps/priority-servers.xml`. Filtered for `lastmod` dates of July 28, 2026.
2. **mcp.so /servers** — SSR extraction of dehydrated TanStack state. 76 servers extracted.
3. **Cross-reference** — compared all server slugs against existing catalog (254 entries in `servers/external/`).

## New Servers Discovered (Afternoon)

### LinkedIn MCP by GTM API ★★★ Major Find
- **Source:** mcpservers.org sitemap 6 (lastmod: 2026-07-28T15:39:51Z)
- **GitHub:** `github.com/gtm-api/linkedin-mcp`
- **What it is:** Managed LinkedIn MCP server for AI agents — search, connect, message, and enrich on LinkedIn from any MCP client. 20,000+ accounts managed at <1% ban rate. Purpose-built proxy infrastructure with rotating residential IPs, browser fingerprinting, and session management.
- **Why it matters:** First production-grade LinkedIn MCP with ban-resistance at scale. Previous LinkedIn MCPs were either simple API wrappers (limited to Company Pages) or fragile cookie-based scrapers. This is a managed service that handles the entire anti-bot layer — the AI agent just calls tools.
- **Transport:** Streamable HTTP (managed endpoint)
- **Auth:** API key (GTM API platform)
- **Pricing:** Freemium with paid tiers for volume
- **Business relevance:** Critical for B2B operators — AI agents can now do lead gen, relationship management, and competitive research on LinkedIn without human copy-paste workflows.
- **Guide:** [linkedin-mcp-gtm/index.md](/hermes/mcp/servers/external/linkedin-mcp-gtm/index.md)

### Apollo.io MCP ★★★ Major Find
- **Source:** mcpservers.org sitemap 5 (lastmod: 2026-07-28T01:10:28Z)
- **GitHub:** `github.com/Inferensys/apollo-io-mcp`
- **What it is:** MCP server for Apollo.io's full API — 45+ tools covering lead search, contact enrichment, sequence management, and CRM operations. Integrates Apollo's database of 275M+ contacts and 30M+ companies directly into AI agent workflows.
- **Why it matters:** Apollo.io is the dominant B2B contact data platform. This MCP allows AI agents to search, qualify, and act on leads without leaving the agent interface. Combined with the LinkedIn MCP, it creates an end-to-end AI-powered outbound pipeline.
- **Transport:** stdio (local) via npx
- **Auth:** Apollo.io API key
- **Pricing:** Requires Apollo.io plan (Free: limited, Basic: $59/mo, Professional: $99/mo)
- **Business relevance:** Essential for operators doing any B2B outbound — AI agents can now qualify leads against firmographics, pull direct dials/emails, and push to sequences.
- **Guide:** [apollo-io-mcp/index.md](/hermes/mcp/servers/external/apollo-io-mcp/index.md)

### Browserless MCP ★★ Official
- **Source:** mcpservers.org sitemap 5 (lastmod: 2026-07-28T09:45:08Z)
- **GitHub:** `github.com/browserless/browserless-mcp`
- **What it is:** Official Browserless MCP server — navigate, scrape, screenshot, and automate any website through headless Chrome at scale. Built by the Browserless team (the leading headless browser SaaS).
- **Why it matters:** Browserless is the de facto standard for production headless Chrome (used by Apify, n8n, and thousands of operators). This official MCP server makes it accessible to AI agents without writing Playwright scripts — agents describe what they want and Browserless executes it on their global infrastructure.
- **Transport:** Streamable HTTP (remote) + stdio fallback
- **Auth:** Browserless API token
- **Pricing:** Free tier (1,000 sessions/mo), paid from $49/mo
- **Business relevance:** Operators can now ask AI agents to "check if our competitor changed pricing" or "screenshot the top 10 Google results for X" and get browser-automated results.
- **Guide:** [browserless-mcp/index.md](/hermes/mcp/servers/external/browserless-mcp/index.md)

### FXMacroData MCP ★★
- **Source:** mcpservers.org sitemap 5 (lastmod: 2026-07-28T08:29:36Z)
- **GitHub:** `github.com/fxmacrodata/fxmacrodata`
- **What it is:** Macroeconomic and FX data MCP server covering 18 currencies — central bank announcements, economic calendar, COT (Commitment of Traders) data, commodities, and forex rates. Python-based with clean tool interfaces.
- **Why it matters:** Combines multiple premium data sources (COT, central bank calendars, commodity prices) into a single MCP that AI agents can query conversationally. Previously, an operator would need to check 4-5 different websites or pay for a Bloomberg Terminal.
- **Transport:** stdio (local) via Python
- **Auth:** API key (free tier available)
- **Pricing:** Free tier, Pro tier with historical data
- **Business relevance:** Essential for operators in finance, import/export, treasury management, or any business exposed to FX risk.
- **Guide:** [fxmacrodata-mcp/index.md](/hermes/mcp/servers/external/fxmacrodata-mcp/index.md)

### OpenOSINT MCP ★★
- **Source:** mcpservers.org sitemap 5 (lastmod: 2026-07-28T12:47:39Z)
- **GitHub:** `github.com/OpenOSINT/OpenOSINT`
- **What it is:** MCP-native OSINT framework — 9 intelligence tools: email enumeration, username search, breach check (HaveIBeenPwned), WHOIS lookup, IP intelligence, subdomain enumeration, Google dorks, paste search, and phone number intelligence. Also works as standalone Python CLI.
- **Why it matters:** Consolidates what would normally require 5+ separate OSINT tools into a single MCP server. Operators doing vendor due diligence, competitive research, or security assessments can now run comprehensive intelligence gathering from their AI agent.
- **Transport:** stdio (local) via Python
- **Auth:** None required (uses public APIs)
- **Pricing:** Free and open source (MIT)
- **Business relevance:** Vendor due diligence, competitive intelligence, domain research, and security assessments — all invocable from an AI agent without context-switching.
- **Guide:** [openosint-mcp/index.md](/hermes/mcp/servers/external/openosint-mcp/index.md)

## Also Identified (No Guides)

| Server | Source | Reason Skipped |
|--------|--------|----------------|
| Screpy SEO MCP | sitemap6 | Technical SEO audits — niche, not general business-ops |
| AnySearch MCP | sitemap5 | Unified search — developer tool, overlaps with existing search MCPs |
| GetJobzi MCP | sitemap6 | Job search — consumer-focused, not business operations |
| JobVetta MCP | sitemap6 | India-only job search — regional |
| FlatCash MCP | sitemap6 | Crypto bounties — niche |
| TaskMiner Render | sitemap6 | Developer tooling |
| Grabbit MCP | sitemap6 | Data extraction — needs more research |
| Trello Desktop MCP | sitemap5 | Trello integration — overlaps with existing Atlassian MCP |
| MS Planner MCP | sitemap5 | Already in catalog (Microsoft ecosystem) |
| Memory Mesh / Mneme / Vektor Memory | sitemap5/6 | Memory tools — crowded category, no standout differentiation |
| Various (QR, SMS, Voice, Memes) | sitemap6 | Consumer/niche |

## Catalog Stats

| Metric | Morning | Afternoon | Change |
|--------|---------|-----------|--------|
| Total servers tracked | 112 | 117 | +5 |
| Integration guides | 12 | 17 | +5 |
| mcpservers.org total | 10,141 | 10,357+ | +216 |
| mcp.so total | ~22,680 | ~22,680 | unchanged |

## Notes

- **Major finding:** LinkedIn MCP by GTM API is the standout find of this sweep. A production-grade, ban-resistant LinkedIn MCP fills the single biggest gap in B2B operator tooling. Combined with Apollo.io MCP, operators now have an AI-driven outbound pipeline end-to-end.
- **Browserless going MCP-native:** Another major platform (after Stripe, Metabase, Atlassian, n8n, Apify, Ahrefs) shipping official MCP support. The trend of established platforms adopting MCP continues to accelerate.
- **MCP 2.0 RC:** Published today — none of these servers reference it yet. Migration monitoring starts now.
- **Firecrawl still DOWN:** Third consecutive sweep without managed web tools. Sitemap-based discovery is working reliably.
