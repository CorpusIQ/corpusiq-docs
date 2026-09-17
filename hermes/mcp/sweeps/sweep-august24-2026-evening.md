---
title: "Sweep Report - August 24, 2026 (evening cron sweep)"
description: "MCP ecosystem discovery sweep report: newly catalogued servers, evaluation notes, and skip classifications. Part of the Hermes resource directory."
last_updated: 2026-09-17
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-august24-2026-evening/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp", "ecosystem sweep"]
---

# Sweep Report - August 24, 2026 (evening cron sweep)

**Sources:** mcp.so feed (newest 30 submissions), mcpservers.org /all pages 1-3 (38 slugs)
**Prior sweep cutoff:** chatmcp/mcpso issues #3726-#3734 (midday sweep)

## Catalogued (2 new, 2 guides)

| Server | Repo / Endpoint | Verification | Category | Relevance |
|---|---|---|---|---|
| Ice Juice Trading (Alpaca rules-based strategy automation, OAuth 2.1/API key) | icejuicetrading.com / mcp.icejuicetrading.com/mcp | INIT probe returned HTTP 401 = auth gate live (OAuth 2.1 DCR+PKCE or first-party API key per vendor overview); tool names not published, capability table from vendor overview | Finance | ★★ |
| Agentic Atlas (field-tested agent-system design patterns, keyless) | github.com/aj604/agentic-atlas-plugin / agentic-atlas.dev/mcp | LIVE PROBE v3.4.7, stateless (no session ID): initialize + tools/list returned all 8 tools (atlas_orient, atlas_cards, atlas_read, atlas_links, atlas_provenance, atlas_navigate, atlas_define, atlas_decisions) | AI Agents | ★★ |

## Skipped

- **uxgen** (mcp.so feed, 5h) - e-commerce conversion component library for coding agents - vendor states tool execution is not switched on yet and every call returns an explicit refusal; $29/mo, no trial - dev-asset class.
- **OAIA Arena** (mcp.so feed, 4h) - AI trading-agent track-record scoring against 2,048 coin-flipping monkeys - no published tool list - crypto/verification class, AgentRisk M2M precedent.
- **ReactVision MCP** (mcp.so feed, 4h) - 44-tool ViroReact XR renderer and framework knowledge for coding agents - dev tool class.
- mcpservers.org /all pages 1-3 (38 slugs): all repeats - either catalogued (Agency AI, SalesTouch, PassportCraft, BulkTranscripts, Corpus Law, Den Archi, Kirah, Real Wave, Gex Live, Sprkly, Newsmind, html-css-to-image class) or prior documented skips (MetricFire, Tseha, NobGit, ClipMyApp, Botsify, CLSTR, Meistron, Socializioz, Magichour, Nautilinks, Calaf, Neotic, Claude News, 2328 Docs, Bifrost, Swarme, Frantic, macadress, betadrop, contextstream, geolens, DotLy, Appraisily, Fresh Jots, Public Signal Data, Agents Get Paid).
- Feed repeats already evaluated in Aug 21-24 sweeps: RE Data Refinery, Truth Bear GAUGE, Agent Conductor, CodeSentinel, BitBrowser, Mangii, Hypnothera, Shotstack, Agency AI, TEOS WARN Act, Routebase, SecondSim, Context.dev, Dados B3, AskRentAI, Signal Nodus, lucid.page, Hermoso, QR Planet, HTML/CSS to Image, One MCP (catalogued Aug 21 afternoon, guide one-mcp/).

## Notes

- Ice Juice listing FAQ says "does not require authentication" but the live initialize probe returned HTTP 401 - the auth gate is real and the vendor overview documents OAuth 2.1 DCR+PKCE or first-party API key. Guide written around the verified gate.
- Agentic Atlas initialize returned no Mcp-Session-Id and tools/list succeeded stateless - MCP '26-style stateless server on protocol 2025-06-18, with expected_revision coherence markers in tool schemas.
- Internal worker node unreachable this cycle (SSH timeout) - entire sweep run from Spark per fresher-clone doctrine; Spark catalog was already current (Aug 24 midday, 350 servers) and equal to origin/main.
