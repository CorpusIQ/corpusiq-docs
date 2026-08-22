---
title: "MCP Discovery Sweep - August 22, 2026 (Docs Maintenance)"
date: 2026-08-22
tags: [mcp-sweep, discovery, catalog]
description: "chatmcp/mcpso issues #3689-#3698 (Aug 22 06:24-18:02 UTC); 2 catalogued with guides (Corpus Law, Breakreach), 6 skipped"
---

# MCP Discovery Sweep - August 22, 2026 (Docs Maintenance)

- **Cutoff:** evening cron sweep evaluated mcp.so Feed newest 30 + mcpservers.org /all pages 1-3 through ~18:00 UTC
- **Fresh window:** chatmcp/mcpso issues #3689-#3698 (Aug 22 06:24-18:02 UTC)
- **Result:** 2 catalogued with guides, 6 skipped

## Catalogued (2 guides)

| Server | Stars | Category | Source |
|---|---|---|---|
| Corpus Law MCP (US legal search + business formation: 551,201+ provisions of federal/state/municipal law across 18 jurisdictions (16 searchable), verbatim citations with full-text lookup; formation intake checklists per state, NAICS lookup, prefilled filing handoffs; anonymous free tier 100 searches/month/IP, no OAuth, no session state; endpoint corpuslaw.us/api/mcp, live-probed v1.2.1, 7 tools) | n/a (new listing) | IP/Legal | GH issue #3698 |
| Breakreach MCP (AI-native social scheduling across 12 platforms: create, schedule, analyze posts, best-time slots, media upload, unified analytics; endpoint api.breakreach.com/mcp, live HTTP 401 auth gate confirmed; Bearer API key) | n/a (new listing) | Social Media Management | GH issue #3691 |

## Skipped (6)

- **Mangii (#3696)** - remote manga image generator (BYOK credits). Consumer media generation, same class as UnificAlly skip.
- **CCS Runtime Evidence (#3695)** - npx-installed security runtime verification with Ed25519 receipts. Local dev tool, not business data.
- **Secret MCP (#3694)** - GDWEB evidence-grounded web design analysis producing DESIGN_INDEX specs. Dev utility.
- **Adtivity (#3693)** - analytics + churn-prediction "Founder OS" that auto-installs an SDK into codebases. Dev tool class (installs into repos, not a remote data surface).
- **a11y-toolkit (#3692)** - local WCAG 2.2 accessibility suite (stdio, zero deps). Dev/QA tool.
- **Lachesis (#3689)** - compiler-precise code property graph over MCP (stdio/Docker). Dev infrastructure, same class as prior Lachesis evaluation.

## Notes

- Corpus Law endpoint probed twice: initialize returned protocol 2025-06-18, serverInfo corpus-legal v1.2.1, and anonymous tools/list returned all 7 tools.
- Breakreach returns HTTP 401 "Missing or invalid API key" for anonymous callers - auth gate confirmed, same pattern as Antwork.
- Catalog index updated: 318 → 320 servers (+204 → +206 guides).
