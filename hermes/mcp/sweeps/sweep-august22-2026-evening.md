---
title: "MCP Discovery Sweep - August 22, 2026 (Evening)"
date: 2026-08-22
tags: [mcp-sweep, discovery, catalog]
description: "mcp.so Feed (newest 30) + mcpservers.org /all pages 1-3 + live endpoint probes; 4 catalogued with guides, 10 skipped"
---

# MCP Discovery Sweep - August 22, 2026 (Evening)

- **Cutoff:** prior sweep (morning) evaluated the mcp.so Feed and mcpservers.org /all through ~07:49 UTC
- **Fresh window:** mcp.so Feed submissions from the last ~4 days (newest 30), mcpservers.org /all pages 1-3 (~50 newest slugs), all 4 catalogued endpoints live-probed
- **Result:** 4 catalogued with guides, 10 skipped

## Catalogued (4 guides)

| Server | Stars | Category | Source |
|---|---|---|---|
| Antwork MCP (hosted social publishing: 35 tools across identity, workspaces, social accounts, voice profiles, posts, publishing, analytics, media; 8 platforms incl. Pinterest and YouTube; OAuth 2.1 PKCE+DCR with read/write/publish/media scopes; endpoint api.antwork.io/mcp, HTTP 401 auth gate confirmed live; free plan, Pro/Business tiers) | n/a (v1.0 May 2026) | Social Media Management | mcpservers.org /all p1 |
| Gex Live MCP (measurement-only SPX dealer positioning: zero-gamma flip, call/put walls, hold band, 1000+ sessions; 3 free keyless tools live-probed + 5 Lab tools; endpoint mcp.gex.live/mcp, anonymous tools/list 200) | n/a | Finance | mcpservers.org /all p1 |
| Sprkly MCP (shortform publishing to TikTok/FB/IG/YouTube/Threads with queue-based approvals: 16 tools live-probed, no publish-now, agent-read-only published posts, per-account scoped keys; endpoint sprkly.app/api/mcp, anonymous tools/list 200) | n/a | Social Media Management | mcpservers.org /all p1 |
| ship.page MCP (zero-config HTML deployment: 7 tools live-probed (deploy_html, deploy_files, list_drops, claim_drop, delete_drop, get_limits, get_account); endpoint ship.page/mcp, anonymous tools/list 200; free anonymous tier, Pro $4/mo; Bitgate, the lucid.page team) | n/a | Content & Publishing | mcp.so Feed |

## Skipped (10)

- **Taskfolk** - project management MCP already catalogued Aug 20 overnight. Repeat.
- **BCMS** - agentic headless CMS listed on mcp.so as a CLIENT with marketing copy and no MCP server surface. Thin docs.
- **Atoa** - UK payments platform; mcpservers.org slug is a GitHub org page listing SDK repos with no MCP endpoint or tool list. Thin docs. Revisit if Atoa publishes a real MCP repo.
- **Gifi** - AI-text-watermark inspection and rewriting. Not business tooling.
- **Agent Conductor / CodeSentinel** - AGENTS.md contract parser + SKILL.md registry and codebase-health tools from one author (icohangar-ops). Dev/agent infra, consistent with Kin and Wondel skips.
- **FaceSign** - step-up verification SDK for developers. Dev infra.
- **Booking.com Hotel Search** - consumer travel, consistent with TravelAnimator and osm-mcp skips.
- **Seedfast** - PostgreSQL synthetic test-data generator. Dev tool.
- **Opportunity Atlas** - Northeast Ohio construction opportunity data. Geo-niche.

## Feed and /all repeats (previously evaluated)

mcp.so Feed repeats already catalogued or previously skipped: Dados B3, One, Signal Nodus, AskRentAI, Hermoso, RADAAR, Upfirst, Webz.io, Simplepages, Xverum, SavePropTax, Waqi, lucid.page, LinkedIn Ghostwriter, Riddle Quiz Maker, AdminLanding, QR Planet, CSOAI GSPC, 3gpp-mcp, Skycloak, Parse.bot, Roboterradar, DPF, My AskAI, UnificAlly, HTML/CSS to Image. mcpservers.org /all slugs already catalogued or previously skipped: caribooks, claudenews-online, doc-2328-io, bifrost, maxcrawl, bestappify, hostdefi, maevesocial, registly, signalsprint, toolyour, newsmind, giggal, vital-care-finder, 60fps-design, mindmapai, riverscript, tradebrite, upfirst, simplepages, thefomite, livesend.

## Endpoint probes (this sweep)

- api.antwork.io/mcp: HTTP 401 `{"error":"unauthorized"}` - auth gate as expected
- mcp.gex.live/mcp: HTTP 200, anonymous tools/list returned list_sessions, get_session, get_levels
- sprkly.app/api/mcp: HTTP 200, anonymous tools/list returned 16 sprkly_* tools
- ship.page/mcp: HTTP 200, anonymous tools/list returned all 7 tools
