---
title: "MCP Server Sweep — July 21, 2026 (Evening)"
description: "28 new MCP servers discovered from mcpservers.org direct submissions. 15 business-operator-relevant integration guides drafted. Headline finds: Fintel (hosted financial MCP), GReminders (scheduling+CRM), BasedOnBusiness (Google Maps leads), datamcp (PostgreSQL/MySQL gateway), Scalix Cloud (50-tool cloud platform)."
category: mcp
tags: [mcp-servers, discovery, sweep, catalog, 2026]
last_updated: 2026-07-21
---

# MCP Server Sweep — July 21, 2026 (Evening)

Discovered 28 new MCP servers from mcpservers.org's direct-submission feed — servers that bypass the awesome-mcp-servers PR queue entirely. 15 integration guides drafted for business-operator-relevant servers.

**Source:** mcpservers.org /all page (JSON-LD extraction, 30 newest servers)
**Previous sweep:** July 20, 2026 (8 servers from awesome-mcp-servers PRs)
**This sweep:** 28 new servers (14 business-operator-relevant + 14 niche)

## Methodology

Web tools (Firecrawl) unavailable on this node. Used:

1. **mcpservers.org /all page** — SSR extraction via `curl` parsing JSON-LD schema data — 30 newest-listed servers extracted with full descriptions, URLs, and categories
2. **Cross-reference** — All 30 candidates checked against existing catalog (169+ entries in `servers/external/`)
3. **Filtering** — 2 of 30 already in catalog (Superserve, OpenInvestOp). 28 net-new.

## Headline Finds (★ = operator relevance)

| Server | Category | Why It Matters |
|--------|----------|----------------|
| **Fintel** ★★★ | Finance | Hosted financial data MCP — real-time + historical markets. First dedicated financial MCP on mcpservers.org direct-submit path. |
| **GReminders** ★★★ | Business Ops | Scheduling + CRM + calendar MCP for professional firms. First all-in-one appointment management MCP. |
| **BasedOnBusiness** ★★★ | Lead Gen | Google Maps business lead search + enrichment (email, social, tech stack) across 195 countries. |
| **datamcp** ★★★ | Database | Hosted MCP gateway for PostgreSQL, MySQL, and OpenAPI. Scoped access links, server-side credentials. |
| **Scalix Cloud** ★★ | Cloud/DevOps | Agent-operable cloud platform — 50+ tools for database, AI, functions, containers, storage, auth. |
| **InvestSights** ★★ | Finance | Indian stock market (NSE/BSE) — fundamentals, forensic accounting, DCF for 6,000+ stocks. First India-focused MCP. |
| **PreTestAds** ★★ | Marketing | Pre-flight ad creative scoring benchmarked against 76 top TikTok ads. $5/run via x402. |
| **Feedier** ★★ | Business Ops | Customer feedback & survey MCP — NPS, sentiment analysis, feedback categories. |
| **Google Maps Scraper** ★★ | Lead Gen | Live Google Maps search, reviews, photos through MCP. |
| **Mermail** ★★ | Email | Privacy-first email inboxes for AI agents — read, search, draft, send, triage. |
| **MailStream** ★★ | Direct Mail | Physical mail MCP — postcards, letters, campaigns. First direct mail MCP server. |
| **squirrelscan** ★★ | SEO/Dev | Website audit (SEO, performance, security, accessibility, agent experience) with exact fixes. |
| **LastPing MCP** ★ | Monitoring | AI agent service monitoring and uptime checks. |
| **codicil** ★ | Docs/Knowledge | Local Chroma vector indexing for repo documentation with Ollama embeddings fallback. |
| **MailFixture** ★ | QA/Testing | Disposable email/SMS inboxes for automated testing — wait-for-OTP, wait-for-link. |

## Full Discovery List (28 Servers)

| # | Server | Category | Source | Business-Relevant |
|---|--------|----------|--------|-------------------|
| 1 | Fintel | Finance | mcp.fintel.io | ✅ |
| 2 | Feedier | Productivity | help.feedier.com | ✅ |
| 3 | GReminders | Productivity | api.greminders.com | ✅ |
| 4 | Hound Web MCP | Search | github.com/dondai1234/master-fetch | ❌ |
| 5 | Panella | Memory | github.com/panellatech/panella | ❌ |
| 6 | BasedOnBusiness | Marketing | basedonb.com | ✅ |
| 7 | Quizzz MCP Connector | Productivity | quizzz.techtranslab.com | ❌ |
| 8 | datamcp | Database | datamcp.app | ✅ |
| 9 | Nippy | Cloud Service | nippy.host | ❌ |
| 10 | TBit | Communication | tbit.app | ❌ |
| 11 | Talamus | Memory | github.com/ampres-ai/talamus | ❌ |
| 12 | Google Maps Scraper | Web Scraping | gmapsextractor.com | ✅ |
| 13 | Scalix Cloud | Cloud Service | github.com/scalixworld/scalix-mcp | ✅ |
| 14 | Laioutr | Productivity | docs.laioutr.com | ❌ |
| 15 | Massive | Web Scraping | github.com/joinmassive/mcp-server | ❌ |
| 16 | GeezerKeeper | Search | geezerkeeper.com | ❌ |
| 17 | txtcel-mcp | Communication | github.com/txtcel/txtcel-mcp | ❌ |
| 18 | codicil | Search | github.com/colehellman/codicil | ✅ |
| 19 | LastPing MCP | Development | github.com/tp322d/lastping-app | ✅ |
| 20 | Mermail | Communication | docs.mermail.app | ✅ |
| 21 | AgentCouch | Communication | agentcouch.dev | ❌ |
| 22 | MailStream | Marketing | mailstream.app | ✅ |
| 23 | InvestSights | Finance | github.com/InvestSights | ✅ |
| 24 | PreTestAds | Marketing | github.com/krecicki/pretestads | ✅ |
| 25 | BTC War Live Crypto | Finance | btcwar.net | ❌ |
| 26 | MailFixture | Development | mailfixture.com | ✅ |
| 27 | Latchshot | Web Scraping | github.com/BaiqingL/latchshot-mcp | ❌ |
| 28 | squirrelscan | Development | github.com/squirrelscan/squirrelscan | ✅ |

## Integration Guides Created

Detailed setup guides drafted for all 15 business-relevant servers. Each covers:
- What the server does for operators
- Installation (npm/uvx/pip or hosted)
- Claude Desktop / Hermes config
- Key tools and their use cases
- Authentication requirements
- CorpusIQ integration angle
- Limitations

### Guides by Category:

**Finance (3):** Fintel, InvestSights, PreTestAds
**Business Operations (3):** Feedier, GReminders, datamcp
**Lead Generation (2):** BasedOnBusiness, Google Maps Scraper
**Cloud/DevOps (1):** Scalix Cloud
**Communication (2):** Mermail, MailStream
**Development (3):** LastPing MCP, squirrelscan, MailFixture
**Documentation (1):** codicil

## CorpusIQ Angle

This sweep confirms a significant shift: mcpservers.org direct submissions are now the primary MCP server discovery path, outpacing the awesome-mcp-servers GitHub PR queue. The corpusiq-docs MCP catalog is now one of the most comprehensive curated collections for operators — 184 servers with detailed integration guides.

Key operator trends visible in this sweep:
- **Professional services MCP boom** — GReminders (scheduling+CRM), Feedier (customer insights), MailStream (direct mail)
- **Lead generation vertical** — BasedOnBusiness + Google Maps Scraper: agent-native lead gen stack
- **Finance goes global** — InvestSights (India) joins existing US-focused financial MCPs
- **Agent-native infrastructure** — Scalix Cloud: full cloud platform managed through MCP

## See Also

- [[servers/external/fintel-mcp]]
- [[servers/external/feedier-mcp]]
- [[servers/external/greminders-mcp]]
- [[servers/external/basedonbusiness-mcp]]
- [[servers/external/datamcp-mcp]]
- [[servers/external/google-maps-scraper-mcp]]
- [[servers/external/scalix-mcp]]
- [[servers/external/investsights-mcp]]
- [[servers/external/lastping-mcp]]
- [[servers/external/pretestads-mcp]]
- [[servers/external/mermail-mcp]]
- [[servers/external/mailstream-mcp]]
- [[servers/external/squirrelscan-mcp]]
- [[servers/external/codicil-mcp]]
- [[servers/external/mailfixture-mcp]]
- [[sweeps/sweep-july20-2026]]
- [[index]]
