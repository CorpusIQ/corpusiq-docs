---
title: "MCP Server Scan — July 21, 2026"
description: "Daily MCP server discovery scan. No new awesome-mcp-servers PRs merged since July 13. mcpservers.org shows 16+ new direct-submission servers. Web search unavailable; full details pending Firecrawl restoration."
category: mcp
tags: [mcp-scan, discovery, mcp-servers]
last_updated: 2026-07-21
---

# MCP Server Scan — July 21, 2026

**Sources:** mcpservers.org /all page (10,079+ servers), awesome-mcp-servers PR queue (punkpeye/awesome-mcp-servers), mcp.so (unreachable — 502)
**Date:** July 21, 2026, 03:02 MST
**Previous scan:** [July 20 Sweep](/hermes/mcp/servers/external/scan-results-2026-07-19/) (last scan-results file)
**Coverage:** New submissions since July 20 sweep

## Methodology

Web tools (Firecrawl) unavailable on this node. GitHub search (`gh search repos`) blocked with "User flagged as spammy" on all date-filtered queries. Used:

1. **awesome-mcp-servers PR queue** — `gh api repos/punkpeye/awesome-mcp-servers/pulls?state=closed` — **zero merged PRs since July 13**
2. **mcpservers.org /all page** — SSR extraction via Python urllib (Accept-Encoding: identity); 30 newest-listed servers extracted
3. **Cross-reference** — All candidates checked against existing catalog (169 entries in `servers/external/`)

## Key Finding: mcpservers.org Direct Submissions Outpacing awesome-mcp-servers PRs

The mcpservers.org directory accepts direct submissions via `/submit` (free + premium $39 tier) that bypass the awesome-mcp-servers PR queue entirely. This creates two discovery vectors:

1. **awesome-mcp-servers PR queue** → merged → appears in both mcp.so AND mcpservers.org (traditional path)
2. **mcpservers.org direct submit** → appears only on mcpservers.org (new path, growing faster)

### New Servers Detected on mcpservers.org /all Page (Not in Existing Catalog)

| # | Server | Business-Relevant? | Notes |
|---|--------|-------------------|-------|
| 1 | **Feedier** | Yes (feedback/surveys) | Customer feedback platform — likely SaaS |
| 2 | **GReminders** | Yes (scheduling) | Appointment reminder automation |
| 3 | **Hound Web MCP** | Yes (web scraping) | Web data extraction |
| 4 | **Panella** | Unknown | — |
| 5 | **BasedOnBusiness** | Yes (business data) | Name suggests business intelligence |
| 6 | **Quizzz MCP Connector** | Low (quizzes) | — |
| 7 | **datamcp** | Yes (data) | Generic data connector |
| 8 | **TBit** | Unknown | — |
| 9 | **Talamus** | Unknown | — |
| 10 | **Google Maps Scraper** | Yes (lead gen) | Maps data extraction for sales |
| 11 | **Scalix Cloud** | Yes (cloud) | Cloud platform MCP |
| 12 | **Laioutr** | Low (design) | Layout/design tool |
| 13 | **GeezerKeeper** | Unknown | — |
| 14 | **txtcel-mcp** | Low (text/Excel) | Text/Excel processing |
| 15 | **codicil** | Yes (legal) | Legal document MCP — potentially wills/trusts |
| 16 | **LastPing MCP** | Yes (monitoring) | Uptime/status monitoring |
| 17 | **Mermail** | Yes (email) | Email MCP |
| 18 | **AgentCouch** | Unknown | — |
| 19 | **MailStream** | Yes (email) | Email streaming/processing |
| 20 | **InvestSights Indian Stock Research MCP** | Yes (finance) | Indian stock market research |
| 21 | **PreTestAds** | Yes (advertising) | Ad testing platform |
| 22 | **OpenInvestOp** | Yes (finance) | Open investment operations |
| 23 | **BTC War Live Crypto Prices** | Yes (crypto) | Real-time crypto pricing |
| 24 | **MailFixture** | Yes (email) | Email testing/dev |
| 25 | **Latchshot** | Unknown | — |
| 26 | **squirrelscan** | Unknown | — |
| 27 | **Live Tennis API** | Low (sports) | Sports data |

## Limitations & Next Steps

1. **Full details unavailable:** mcpservers.org server pages return 404 (client-side rendered React/Next.js). Individual server descriptions not extractable without browser automation or Firecrawl.
2. **GitHub repos unknown:** None of these servers appear in the awesome-mcp-servers README (direct submission path). GitHub search blocked. Repo ownership cannot be determined from current node.
3. **Recommendation:** Re-run scan when Firecrawl is available, or use Mac Mini Playwright to scrape mcpservers.org server detail pages. Prioritize: **Feedier, GReminders, BasedOnBusiness, Google Maps Scraper, Scalix Cloud, codicil, LastPing MCP, InvestSights** — these have direct business-operator relevance.

## mcp.so Status

mcp.so returned HTTP 502 on all attempted endpoints (API + web). SPA not accessible. Backend repo `chatmcp/mcpso` (2,025⭐) — no new CorpusIQ issues since #3248 (July 20).

## Repository Health

- **Existing catalog:** 169 server guides + index.md (2,690 lines)
- **Last push:** July 20 sweep — 8 new business-operator MCP servers
- **No new guides created this scan** due to scraping limitations
