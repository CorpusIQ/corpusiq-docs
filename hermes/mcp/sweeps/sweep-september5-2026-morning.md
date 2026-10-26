---
title: "Sweep Report - September 5, 2026 (Morning) - CorpusIQ Docs"
description: "Morning MCP catalog sweep: mcpservers.org /all pages 1-3 plus the mcp.so feed, cataloging 4 new servers with guides (Ryze Meta Ads, Abyssale, Elium, PostBazooka); catalog now 543 servers / 429 guides."
date: 2026-09-05T03:10:00-07:00
sources: [mcpservers.org, mcp.so]
status: complete
last_updated: "2026-10-19"
---

# September 5, 2026 - Morning Cron Sweep

**Shift:** Morning (~03:00 MST)
**Prior cutoff:** Sep 4 evening sweep (chatmcp/mcpso issues #3918-3937, mcp.so feed, /all pages 1-3)
**Fresh window evaluated:** mcpservers.org /all pages 1-3 (47 slugs batch-classified, pages shifted vs the evening's 90), mcp.so feed (30 entries, all catalogued repeats or prior dispositions)
**Surfaces:** /all pages via curl + slug extraction, detail pages via curl + title/meta batch classification, vendor docs via curl (getryze.ai, developers.abyssale.com, help.elium.com, postbazooka.com/mcp.md)
**Result:** 4 new servers catalogued (4 guides), catalog now 543 servers / 429 guides

## Catalogued (4)

| Server | Slug | Source | Verification |
|---|---|---|---|
| Ryze Meta Ads | ryze-meta-ads-mcp | mcpservers.org /all | Vendor spec fully mapped: endpoint connector.get-ryze.ai/mcp, Facebook OAuth sign-in with server-side token exchange, 12 tools (9 read, 3 write approval-gated), no developer app or token required, sibling of the catalogued Ryze Google Ads server on the same endpoint |
| Abyssale MCP | abyssale-mcp | mcpservers.org /all | Changelog v1.0.0 (2026-09-01) mapped: 16 tools across identity, discovery, generation and design import, endpoint mcp.abyssale.com/mcp, Streamable HTTP POST-only stateless, OAuth with per-client scopes, registered clients Claude Code CLI, Claude.ai, ChatGPT/Codex, Cursor |
| Elium MCP | elium-mcp | mcpservers.org /all | Vendor docs mapped: per-instance endpoint your-platform-name.elium.com/services/mcp, OAuth, 5 read-only tools (findRelevantArticles, findSpecificArticles, readArticle, findSpaces, findTemplates) running with authenticated-user permissions, EUR 15/mo per user Team tier, ISO 27001 EU-hosted |
| PostBazooka MCP | postbazooka-mcp | mcpservers.org /all | Vendor mcp.md mapped: endpoint postbazooka.com/mcp, OAuth, 26-tool workflow-gated schema, structured commit-confirmation protocol on every mutation, per-destination publishing modes, media provenance requirements, eight networks |

## Not catalogued (skip prose)

- **AI Schema Gen:** WordPress schema-markup plugin whose /all listing claims an MCP surface (AI-readiness check plus fixes) but publishes no endpoint or tool list - thin MCP docs.
- **SpreadFront:** Google Sheet to storefront builder exposing WebMCP tools to browser shopping agents - agentic-commerce storefront class, operators do not consume MCP tools.
- **The Ai Daily:** business AI news briefing - media/news class.
- **Football Charts:** consumer sports statistics across 93 leagues.
- **Liminality (physea-ai):** remote MCP solve-engine that breaks requests into checkable sub-questions - agent infra class.
- **Promethic:** prompt manager and library with per-model dials - dev utility class.
- **Polimake:** generic team-ideas shell - thin docs.
- **Soar Flights:** consumer flight booking class.
- **AgentBrief (mcpchannel.ai):** cite-backed research briefs at $0.02 per call - x402 pay-per-call infra class.
- **Povento:** coding-agent portfolio and project context - dev tool.
- **Fortrabbit:** PHP hosting management - dev infra class.
- **Great Arrow:** connector and shared-memory orchestration - agent infra class.
- **Verbasil:** company memory layer - agent memory infra class (Memwyre precedent).
- **WebMatrices Browser MCP:** social scraping through existing Chrome sessions - saturated scraping class.
- **MAK Immigration Source Guide:** consumer regional niche.
- **AI2SQL:** SQL generation and tuning - dev utility class.

## Feed

All 30 mcp.so feed entries were catalogued repeats (Veriroute, Velarion, Lawstronaut, Klarix, Strac DLP, Tracetify, Extend, iubenda, Sorank, HiBot, Furrow Forms, Dealwize, Factanker, Nizh, miniOrange, MarketCode, PostMCP, OSIR Domain, Trendos, Koongo) or prior dispositions (DB Planner, Alien Probe who, PriceMyRepair, pdfAssistant, FLORA, RAVN, Neither, QuantumProxies, Voibe, dot.tools).

## Repo state

Pushed from the primary working clone. Index frontmatter `last_updated` untouched (docs SEO cron territory). Frontmatter gate run locally before commit.
