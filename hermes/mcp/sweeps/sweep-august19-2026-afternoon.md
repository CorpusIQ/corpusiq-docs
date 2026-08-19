---
title: "Sweep Report — August 19, 2026 (Afternoon Cron Sweep)"
description: "chatmcp/mcpso GitHub issues filed Aug 19 10:55 through 16:03 UTC; 4 catalogued with guides, 1 skipped (sports data)"
---

# Sweep Report — August 19, 2026 (Afternoon Cron Sweep)

**Shift:** Afternoon (~16:20 UTC)
**Sources scanned:**
- chatmcp/mcpso GitHub issues — 5 fresh submissions after the morning cutoff #3644 (filed Aug 19 10:55 through 16:03 UTC)
- mcp.so homepage SSR (`recentServers`) — 5 entries, all repeats (CSOAI org previously noted July 3; Waqi, Bitroad, FineData, TravelAnimator already catalogued/skipped)
- mcpservers.org homepage — 17 slugs, all previously reviewed in the morning sweep (Austin MLS, My AskAI, a9n9, eCourts India) or famous names

**Result:** 4 new servers catalogued with guides, 1 skipped (sports data precedent), index updated.

## Catalogued (4 new, 4 guides)

| Server | Stars | Category | Signal |
|---|---|---|---|
| MCPGRAM MCP (OAuth 2.1 gateway: Slack, GitHub, Google, Salesforce + 30 apps, per-workspace consent and token isolation) | 0★ | Connectivity | GH issue #3646 |
| WaveSpeed MCP (official media generation: image/video/audio/3D catalog, schema introspection, pre-spend price quotes) | 30★ | Media Generation | GH issue #3647 |
| RE Data Refinery MCP (pay-per-query real estate: Zillow + county enrichment, flip/wholesale/rental scoring, $0.25–$0.50 USDC x402) | 0★ | Real Estate | GH issue #3648 |
| SYNTHORA MCP (30 verified multi-source intelligence tools, Ed25519-signed verdicts, x402 USDC on Base) | hosted | Intelligence & Compliance | GH issue #3649 |

All four verified live: repos exist (WaveSpeedAI/mcp-server 30★ MIT, areshms/re-refinery-mcp MIT created Aug 19, Aryan418-dev/mcpgram repos pushed Aug 19 — no license declared, honestly noted), SYNTHORA catalog.json + agent.json + llms.txt all resolve at hergertsynthora.com.

## Already noted / skipped (evaluated, not re-catalogued)

- footballcharts-mcp — sports data (league tables, model probabilities, Monte Carlo projections for 93 football leagues); consistent with the livetennisapi consumer-sports skip (Aug 18 afternoon)
- CSOAI GSPC measurement — csoai-org compliance infrastructure, previously noted in the July 3 scan results
- Feed repeats: Waqi, Bitroad, FineData.ai, TravelAnimator — all already catalogued or previously skipped

## Verification

- Frontmatter validator: `scripts/validate_frontmatter.py` green (3190 files, all valid)
- Push verified: local HEAD == remote main
- Catalog count: 268 → 272 servers, 158 → 162 guides
