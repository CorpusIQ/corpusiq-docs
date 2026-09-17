---
title: "Sweep Report - August 25, 2026 (evening cron sweep)"
description: "MCP ecosystem discovery sweep report: newly catalogued servers, evaluation notes, and skip classifications. Part of the Hermes resource directory."
last_updated: 2026-09-17
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-august25-2026-evening/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp", "ecosystem sweep"]
---

# Sweep Report - August 25, 2026 (evening cron sweep)

**Sources:** chatmcp/mcpso issues #3746-#3749 (Aug 25 10:47 - 16:48 UTC), mcp.so homepage + feed (38 slugs), mcpservers.org homepage (15 slugs), mcpservers.org /all pages 1-3 (90 slugs, broad + narrow regex)
**Prior sweep cutoff:** Aug 25 morning sweep (issues through #3745, .last-sweep 2026-08-25T10:13:27Z)
**Run location:** Spark (Mac Mini not required this cycle; gh CLI Ben-Home)

## Catalogued (9 new, 9 guides)

| Server | Repo / Endpoint | Verification | Category | Relevance |
|---|---|---|---|---|
| Alpha Sophia | github.com/alphasophia/claude-plugins (proprietary, 0 stars) / api.alphasophia.com/v1/mcp | 401 = OAuth gate live; tools from plugin README (resolve_entity, search/count/market_size, clinical-trial search); official healthcare provider/HCO data | Data & Analytics | ★★★ |
| BeeL | github.com/beel-es/beel-mcp (MIT, active Aug 24) / mcp.beel.es/mcp + stdio npm @beel_es/mcp | 401 = OAuth gate live; ~120 tool names extracted from docs.beel.es/mcp tools page; OpenAPI-derived surface | Compliance | ★★★ |
| CivicDataForge | github.com/equinoxaifinance-rgb/civicdataforge-mcp (MIT, active Aug 24) / civicdataforge.pages.dev/mcp | LIVE PROBE v1.4.0: 14 tools captured (10 evidence + 4 Apify plumbing); X-Apify-Token auth; public discovery | Compliance | ★★★ |
| Partsgraph | hosted, no repo / partsgraph.ai/api/mcp | LIVE PROBE v1.4.0: initialize + .well-known/mcp.json (11 tools); keyless demo catalogue, 35 part records, 3 builds | Business Operations | ★★ |
| Nacha MCP | github.com/msuresh007/nacha-mcp (MIT, created Aug 23) / stdio | README verified: 2 tools (parse_nacha_file, summarize_nacha_file); structural + arithmetic validation, IAT | Finance | ★★ |
| 1Lookup | hosted / app.1lookup.io/api/mcp | 401 = OAuth 2.1 gate live; 5 tools from issue #3747; registry io.1lookup/1lookup active | Compliance | ★★ |
| HostTracker | github.com/HostTracker/mcp (MIT, 1 star) / mcp.host-tracker.com/mcp | Vendor page + repo README: 65 tools, 10 check types, 300+ checkpoints, Bearer token; monitoring since 2004 | DevOps | ★★ |
| SenderKit | hosted / mcp.senderkit.com + local stdio | Docs extracted: 18 senderkit_* tool names confirmed; outputSchema structured results | Communication & Email | ★★ |
| More Good Reviews | hosted, per-project URL | Vendor GitBook docs: capability-level table (customers, review requests, reviews, Google/Facebook replies with confirm gate); agency variant noted | Marketing | ★★ |

## Skipped

- **ParlayAPI** (#3749) - sports odds, player props, should-I-bet layer - consumer gambling class (Batru precedent).
- **BlinkCodes** (#3746) - x402 gift-card/top-up/eSIM store - purchase plumbing, not business data (agent-wallet precedent).
- **dsh-verify** (#3748) - real-browser acceptance testing - dev tool; resubmission of the Aug 18 skip, adds nothing.
- **QuanticData** (mcp.so homepage, created Aug 11) - single-file web-access utility - generic web-access class, catch-up.
- **AgentRisk M2M** (homepage, created Jul 28) - x402 pre-trade risk for DeFi agents - agent infra class.
- **Windframe** (feed, created Jul 9) - AI UI design tool - dev/design class.
- **OAIA Arena** (feed, created Jul 31) - trading-agent public scoreboard - agent infra class.
- **Context.dev** (feed, created Aug 5) - web-data infra for AI products - dev utility class.
- **Agent Conductor** (feed) - AGENTS.md/SKILL.md decision engine - already evaluated Aug 23.
- **/all pages 1-3 never-seen slugs:** AgentsGetPaid (x402 payment kit - payagents class, already noted), CLSTR (already skipped Aug 23, news covered by Webz.io/NewsMind), More Good Reviews (catalogued), SenderKit (catalogued), DotLy ID (domain/biolink registrar - consumer), Fresh Jots (thin-docs notes app), Gofrantic/Frantic (already noted Aug 24), Lacuna Music (AI song generator - consumer media), ORANO (personal workspace/memory - agent infra), Partsgraph (catalogued), PublicSignalData (Polymarket/whale-trade signals - crypto signals class), TwitterAPIs (commercial X API wrapper - thin wrapper), Xi Pe (pastebin - consumer), VehicleFeeCalc ("AI skills" listing not an MCP server - skills-catalog class), BeeL (catalogued), EasyGroupFlights (group airfare booking - travel booking class), CivicDataForge (catalogued), PennyOCR (paid OCR dev utility), XGuard (MCP discovery gateway - agent infra), Nacha (catalogued), amem (local agent memory - agent infra), dockndevai 7-server infra family (already noted Aug 24), ADA Turbo (agency OS visualizer - agent infra), Roast My Design System (design audit - dev tool), ADSBiq (community aircraft lookup - niche aviation), secret_mcp (design analysis - dev tool).

## Notes

- 4 fresh issues this window; 1 catalogue-worthy (1Lookup), 3 class-skips. The /all pages yielded the bigger harvest: 5 of 9 catalogued servers came from mcpservers.org /all pages 1-3 never-seen domain/author-repo slugs (BeeL, CivicDataForge, Partsgraph, Nacha, More Good Reviews, SenderKit), proving the catch-up doctrine - business-data servers that predate the sweep window still catalogue when they carry operator-relevant data.
- 3 live probes executed this sweep: CivicDataForge (14 tools, v1.4.0), Partsgraph (11 tools via manifest + initialize, v1.4.0), plus 401-liveness confirmations for Alpha Sophia, BeeL, and 1Lookup (all OAuth-gated, treated as liveness proof per doctrine).
- BeeL tool names recovered by grepping `beel_[a-z0-9_]+` from the Docusaurus tools page - the vendor docs enumerate the full OpenAPI-derived surface; the guide lists representative groups, not all ~120 names.
- More Good Reviews and SenderKit Tools tables: SenderKit has 18 exact names from vendor docs; More Good Reviews publishes capability-level docs only, so the guide uses the capability-level table with the explicit caveat line per doctrine.
- All 9 guides passed the per-guide gate (YAML parse, title 30-70, description >= 100, no em dashes, See Also dirs verified) and `scripts/validate_frontmatter.py` (3454 files, all valid).
- Index patched with the atomic patcher (asserted anchors, EOF trim); top section uses the morning sweep's link-line format (closest precedent by count), tail block appended after the morning section's last link with the /docs/ prefix.
