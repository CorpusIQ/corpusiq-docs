---
title: "MCP Directory Sweep Report - Aug 26, 2026 (Afternoon)"
description: "MCP ecosystem discovery sweep report: newly catalogued servers, evaluation notes, and skip classifications. Part of the Hermes resource directory."
last_updated: 2026-09-17
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-aug26-2026-afternoon/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp", "ecosystem sweep"]
---

# MCP Directory Sweep Report - Aug 26, 2026 (Afternoon)

**Shift:** Afternoon cron sweep, 12:35 MST start
**Issue cutoff for next shift:** chatmcp/mcpso issue #3779 (Aug 26 19:08 UTC) - start the next shift's issue scan at #3780
**Sources:** chatmcp/mcpso issues (cutoff #3778 -> #3779), mcp.so feed page 1 (curl)
**Pushed from:** Spark

## Catalogued (1 new, 1 guide)

| Server | Issue | Relevance | Category | Endpoint | Verification |
|---|---|---|---|---|---|
| 3dlogo MCP | #3779 | ★★★ | Content Creation & Creative | 3dlogo.io/api/mcp (public: /api/mcp/public) | INIT 200 -> serverInfo 3dlogo v1.0.0; main endpoint HTTP 401 = OAuth gate live |

Guide: 3dlogo-mcp.
Catalog counts: 381 -> 382 servers, 267 -> 268 guides.

## Skipped (evaluated, not catalogued)

- mcp.so feed page 1: all entries were morning/midday-sweep repeats or already evaluated (SocialRobot, LM Legion, fhirHydrant, YouTube Transcript AI, QuanticData, Windframe, Alpha Sophia, HostTracker, Routebase, Agentic Atlas, RE Data Refinery, AgentRisk M2M, OAIA Arena, ReactVision, uxgen, BitBrowser, Shotstack, Agency AI MCP, SSH MCP Server). Cross-referenced each against catalog - all present or previously evaluated-and-skipped.
- LM Legion (feed, 3h ago): multi-model LLM deliberation councils - agent infra class, already evaluated and skipped in the Aug 26 morning sweep.

## Notes

- Only one new issue (#3779, 3dlogo.io) landed since the midday sweep's cutoff at #3778. Feed repeats confirm the morning and midday sweeps had complete coverage of today's new listings.
- 3dlogo MCP: anonymous tier exposes 5 read-only tools (list_materials, list_coin_looks, build_logo_editor_link, build_coin_studio_link, get_plans); OAuth tier adds project management, share pages, invite links, and AI image-to-3D generation with polling. Registered in the official MCP registry as io.github.cottom/3dlogo. Public endpoint verified via tools/list (5 tools, all with readOnly annotations).
- No other GitHub issues, no mcpservers.org sitemap additions beyond what the midday shift already scanned.
