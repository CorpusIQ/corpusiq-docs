---
title: "Sweep Report - September 2, 2026 - CorpusIQ Docs"
description: "Night MCP catalog sweep: chatmcp/mcpso issues #3892-#3906 plus registry and homepage surfaces, cataloging 8 new servers with guides (jp-payroll-mcp, Fruit Stand Fund Returns, Valuation API, Fallax, mcp-sanctions, BulkPublish, China Hot Trending and more); catalog now 493 servers / 379 guides."
date: 2026-09-02T19:01:00-07:00
sources: [chatmcp/mcpso, mcpservers.org, mcp.so]
status: complete
last_updated: "2026-10-24"
---

# Sweep Report - September 2, 2026 - Night Cron Sweep

**Run:** 2026-09-03T02:01Z (19:01 MST, Sep 2)
**Shift label:** September 2, 2026 - Night Cron Sweep (8 New, 8 Guides)
**Sources:** chatmcp/mcpso issues #3892-#3906 (fresh window past #3891), mcpservers.org /all pages 1-3 (90 slugs), mcp.so homepage recentServers, mcpservers.org homepage
**Result:** 8 new servers catalogued with guides; catalog now 493 servers (+379 guides)

## Catalogued (8)

| # | Server | Issue / Source | Verification | Category |
|---|---|---|---|---|
| 1 | jp-payroll-mcp | #3906 | npm v0.4.3, MIT, repo kishida-devil/jp-payroll-mcp, 29 tools from mcp/README, HTTP API root fetched | Business Operations |
| 2 | Fruit Stand Fund Returns | #3903 | 401 liveness (No Authorization Header), registry dev.fruitstand/fund-returns v1.0.0, llms.txt | Finance |
| 3 | Valuation API | #3900 | LIVE keyless probe: v0.3.0, 6 tools (calculate_irr/npv/moic/dcf/wacc, irr_sensitivity) | Finance |
| 4 | Fallax | #3899 | 401 liveness (OAuth), docs page: 12 tools enumerated | Security |
| 5 | mcp-sanctions | #3896 | PyPI atomno-mcp-sanctions v0.1.1, MIT, 4 tools from README | Compliance |
| 6 | BulkPublish | #3893 | npm @bulkpublish/mcp-server v1.18.0, MIT, ~50 tools from README | Marketing |
| 7 | China Hot Trending | #3905 | LIVE keyless probe: v1.29.0, 2 tools (query_hot_trending, list_platforms) | Content & Research |
| 8 | ReelDrop | mcpservers.org /all | 401 liveness (OAuth), vendor /features/mcp page, Glama io.reeldrop/reeldrop | Social Media Management |

## Skipped (also identified, not catalogued)

- **#3904 SparkVibeAI** - multi-model spec committee for coding agents, $29/mo Pro - dev utility class
- **#3901 Santismm Knowledge** - educational knowledge base (agentic AI patterns, governance, Homeric lit), 30 tools live-probed keyless - educational class (Noodle/Hispanic Legacy precedent)
- **#3898 Lamdis Exchange** - physical-work task marketplace (agents pay people for verified real-world tasks) - TaskMarket class (Daytime Agent Market precedent)
- **#3897 Lodestar Stamp** - agent trust attestation receipts, REST discovery path, early stage - agent infra class
- **#3895 PeppyNeuron Confession** - behavioural novelty experiment - consumer class
- **#3894 HeyYumi** - Korean restaurant venue data and reservations - consumer class
- **#3905 remaining four** (12306 train tickets, weather, exchange rates, IP location) - consumer/dev utilities
- **/all catch-ups:** AI Commander (outbound shell), Bonizu (beauty shopping), Pergamos (Calibre ebooks), Chapa (dev profiles), ShotAnvil (capture infra), AginxBrowser (browser automation), 429 Throttle (dev proxy), Walletwatch (consumer crypto), CoreFlows (dev orchestrator), TooHardBasket (task marketplace), Deep Art (image gen), Sirro (agent memory), VenuNite (consumer events), Live Entity Verification (x402 entity checks, thin docs)

## Notes

- Fresh issue window was thin on catalogue-worthy submissions; 8/15 fresh issues were class-skips (consistent with prior same-day sweeps).
- Santismm and hot-trending both probed keyless live; Santismm skipped on the educational-content doctrine despite a healthy 30-tool surface.
- mcp.so homepage recentServers was 8/8 prior-sweep dispositions except Furrow Forms (Developer Tools; not evaluated this sweep - dev-adjacent listing, pending detail fetch in a future cycle).
- No report file existed for the Sep 2 midday sweep (its section in index.md is the source of record).
