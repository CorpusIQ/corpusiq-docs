---
title: "Sweep Report - August 29, 2026 (Night Cron Sweep)"
description: "MCP ecosystem discovery sweep report: newly catalogued servers, evaluation notes, and skip classifications. Part of the Hermes resource directory."
last_updated: 2026-09-17
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-august29-2026-night/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp", "ecosystem sweep"]
---

# Sweep Report - August 29, 2026 (Night Cron Sweep)

## Summary

1 new server catalogued with a guide. 6 skipped. Sources: chatmcp/mcpso issues #3809-#3810, mcp.so homepage new arrivals + feed (30 slugs), mcpservers.org homepage (29 slugs).

## Catalogued (1 guide)

| Server | Source | Endpoint | Verification | Relevance |
|---|---|---|---|---|
| Packy Tracking | mcpservers.org homepage (packy-tracking/packy-tracking-mcp) | mcp.parceltracking.app/mcp | 401 liveness, /health + /ready 200, README tools table | ★★ |

Packy Tracking MCP is the official hosted MCP for the Packy parcel-tracking API: 10 tools mapped onto the Tracking API (trackings_create/list/get/delete, couriers_list, courier_detections_create, webhooks_list/create/update/delete). OAuth 2.1 with API-key fallback (bearer or X-API-Key header). Credit-based pricing: 1 credit per unique tracking number on trackings_create only; reads, courier detection, and webhook tools are free. Public liveness endpoints (/health, /ready) require no key. Repo (packy-tracking/packy-tracking-mcp) is integration docs only, 0 stars, license not declared, no official registry record yet. Catalogued on the Ship24 precedent (parcel tracking + webhooks = operator logistics data), Commerce & E-Commerce category.

## Skipped

- compteparticulier #3809 - French consumer login-guide knowledge base (read-only search over how-to guides for consumer portals); consumer content class, no operator data.
- Unofficial Apple Music for macOS #3810 - local macOS consumer media utility (MusicKit playback); consumer media utility class.
- MagicPixel.art - AI pixel-art generator for game assets (Unity/Godot sync); creative utility class.
- PickADive MCP (afiliptsov/pickadive-mcp) - recreational dive-conditions data; consumer class.
- XcodeBuildMCP (getsentry, 6,309 stars) - iOS/macOS build tooling; dev-tool class.
- TouchDesigner Bridge MCP (eviscerations/touchdesigner-bridge-mcp) - creative production software bridge; creative class.

## Homepage dispositions

- mcp.so recentServers: DrillerDB (catalogued Aug 27 evening), MagicPixel.art (skip above), Forency + TikTok Transcript (catalogued Aug 28 evening), CrawlForge, Ransack, Foremerge, Katto (prior-sweep dispositions).
- mcp.so feed (30 slugs): all remaining slugs were prior-sweep dispositions or already-catalogued servers (youb, agendaforge, bidskim, orbitwan, uwear, graviti, omnisocials, speccy-x402, jitsu, hologrow, openlore, socialrobot, legion, fhirhydrant, youtube-transcript, quanticdata, windframe, alpha-sophia, hosttracker, batru, magic-hour, ice-juice, drillerdb, magicpixel, packy).
- mcpservers.org homepage: famous-name re-indexes (atlassian, blender, calcom, chrome-devtools, cloudflare, context7, exa, firecrawl, github, google/mcp, granola, minimax, playwright, proxyman, railway, supabase, vercel/next-devtools, browserbase, sentry XcodeBuildMCP) plus prior-sweep dispositions (agentcloud, count-nanocorp, floot, runbear, transcriptfetch) and the skips above (pickadive, touchdesigner, notebooklm - prior disposition, deepwiki - prior disposition).

## Commit

docs: catalog Packy Tracking MCP from mcpservers.org homepage with guide (10 tools, OAuth + API key, credit-priced trackings, health endpoints)
