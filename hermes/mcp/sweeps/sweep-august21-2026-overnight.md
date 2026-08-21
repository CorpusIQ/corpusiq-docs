---
title: "MCP Discovery Sweep — August 21, 2026 (Overnight)"
date: 2026-08-21
tags: [mcp-sweep, discovery, catalog]
description: "chatmcp/mcpso GitHub issues filed Aug 20 20:13 through Aug 21 00:48 UTC plus mcpservers.org /all TanStack state, mcp.so and mcpservers.org homepages; 4 catalogued with guides, 7 skipped"
---

# MCP Discovery Sweep — August 21, 2026 (Overnight)

- **Cutoff:** prior sweep evaluated through issue #3663 (Aug 20 16:42 UTC)
- **Fresh window:** issues #3664–#3668 (Aug 20 20:13–Aug 21 00:48 UTC), mcpservers.org /all TanStack SSR (30 newest), both homepages
- **Result:** 4 catalogued with guides, 7 skipped

## Catalogued (4 guides)

| Server | Stars | Category | Source |
|---|---|---|---|
| Superflow Free Tools MCP (13 keyless website QA and AI-visibility tools: AI visibility, robots.txt AI crawler checks, llms.txt generation, JSON-LD validate/generate, social preview, tech stack, screenshots, alt text, UTM builder, page-to-Markdown, favicon, MD5; endpoint usesuperflow.ai/api/mcp, no auth) | n/a | SEO | GH issue #3668 |
| CuttingToolsAI MCP (brand-neutral carbide grade cross-reference for machining: one read-only grade_xref tool with provenance per row; keyless Cloudflare Worker) | 0 | Data & Analytics | GH issue #3666 |
| Webz.io News Search MCP (official vendor MCP: news_search_by_webz natural-language global news search with domain/country/language/sentiment/17-category filters; Bearer token; news-search-mcp.webz.io/mcp) | n/a | Content & Research | mcpservers.org /all |
| LiveSend MCP (publish LLM-written documents to permanent trackable password-protected links: 12 tools, publish/revise/protect/measure/find; browser approval flow; freemium 3 docs) | n/a | Productivity | mcpservers.org homepage |

## Verification performed

- Superflow: live MCP probe against usesuperflow.ai/api/mcp — server superflow-free-tools v1.0.0, all 13 tools captured with names and descriptions (issue claims 19; live endpoint exposes 13)
- CuttingToolsAI: live MCP probe — server cuttingtoolsai-xref v1.0.0, grade_xref confirmed; repo memmizgezgin-creator/cuttingtoolsai-mcp verified (MIT, created Aug 18 2026)
- Webz.io: official docs parsed (docs.webz.io/docs/webz/news-search-api-mcp) — endpoint, Bearer auth, full parameter table, Agent Skill file
- LiveSend: livesend.io/mcp parsed — 12 tool names, connector flow, endpoint www.livesend.io/api/mcp/mcp, Smithery listing samuel-v9g5/livesend
- All candidates cross-referenced against catalog index.md — zero prior mentions

## Skipped (evaluated, consistent with prior decisions)

- #3665 no_human — local stdio coding-task bridge (dev tool)
- #3667 klo-mcp — native macOS video editor (creator/consumer tool)
- thefomite-com-mcp — agent community infra (durable memory, message board, peer oracle)
- ego-lite-browser — browser automation for coding agents (dev tool)
- kogiQA (atagon-gmbh/kogiqa-mcp) — browser tool for coding agents (dev tool)
- RADAAR — already catalogued
- Repeats already evaluated: QR Planet, Xverum, SavePropTax, CSOAI GSPC, 3gpp-mcp, Waqi, Bitroad, Alpha Vantage (catalogued), Arcaeon Ledger (catalogued), plus all /all and homepage slugs covered by the Aug 20 evening report (Upfirst, Atoa, Giggal, Simplepages, Opportunity Atlas, Magnificent Jobs, DPF, Teachfluence, Terno, Vital Care Finder, Booking.com, clio, Dutch pair, Taskfolk, Gliana, MindMap, 60fps, Football Charts, RiverScript, Tollbooth, MarkIt, FaceSign, POB, Chamnan, AST, AgentTrust, Agentic HIL, Seedfast)

## Catalog state

- Before: 291 servers, 177 guides
- After: 295 servers, 181 guides
- Next sweep cutoff: issue #3668
