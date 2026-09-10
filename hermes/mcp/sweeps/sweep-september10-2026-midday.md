---
title: "MCP Server Discovery - September 10, 2026 (Midday Sweep)"
description: "Midday sweep over chatmcp/mcpso issues #4033-#4035 plus mcpservers.org /all pages 1-2 via the r.jina.ai reader proxy and the mcp.so homepage. 1 new business-relevant server catalogued with a guide: APIzone MCP (keyless hosted status and uptime monitoring for 294 popular third-party APIs, live-verified over JSON-RPC)."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-09-10
---

# MCP Server Discovery - September 10, 2026 (Midday Sweep)

**Source:** chatmcp/mcpso issues #4033-#4035 (fresh window past the 03:00 MST sweep's cutoff at #4031; issue #4032 was deleted and never served content), mcpservers.org /all pages 1-2 (r.jina.ai reader proxy, 60 slugs re-classified), mcp.so homepage (featured/trending surfaces only, no recentServers blocks)
**Method:** GitHub issues API, /all slug extraction via reader proxy, JSON-RPC initialize + tools/list probes, live tools/call verification
**Date:** September 10, 2026 ~11:05 MST (18:05 UTC)

## Summary

| Metric | Count |
|---|---|
| New GitHub issues evaluated | 3 (#4033, #4034, #4035) |
| mcpservers.org /all slugs re-classified | 60 (pages 1-2) |
| New servers catalogued | 1 |
| Integration guides written | 1 |
| Skipped (not catalogued) | 9 new names; page-1 names all carry Sep 9 night dispositions |

## New Business-Relevant Servers (1 guide)

| Server | Slug | Class | Verification |
|---|---|---|---|
| APIzone MCP | apizone-mcp | Keyless hosted status and uptime monitoring for 294 popular third-party APIs, probed independently every ~5 minutes | Live-verified: unauthenticated initialize (apizone 1.0.0, protocol 2024-11-05) + tools/list returned all 5 read-only schemas; live get_api_status call for Stripe returned "operational (last response 59ms)" with structured data. No public repo. |

## Findings

- **APIzone MCP**: 5 read-only tools - list_apis (19 category filters), get_api_status, check_apis (batch up to 25), get_api_uptime (24h/7d/30d/90d with median + p95 latency), list_recent_incidents. Every answer carries last-measured latency, last-check timestamp and a per-API status-page URL. RealUptime precedent class (Sep 7 catalogue). Category: Business Operations.

## Skipped (also identified, not catalogued)

- **Hundo #4033** - personal finance ledger for consumers over remote MCP with OAuth 2.1 propose-then-confirm writes; consumer personal-finance class (SavingsLast/SigVest precedent).
- **Cronjob.de #4034** - hosted web-cron automation (URL callbacks on a schedule) with OAuth 2.1 + PKCE; dev infra class (woodpecker-ci/ntfy-mcp precedent).
- **Execution Evidence Lab** - Python failure/evidence reproduction utility; dev utility class.
- **OpenIndex** - AI-agent knowledge wiki; educational class (Santismm precedent).
- **Synap** - long-term agent memory service; agent memory infra class (Memwyre precedent).
- **mcp-azure-selfhosted** - Azure DevOps self-host MCP; dev infra class.
- **mwemu** - x86/OS binary emulation; dev utility class.
- **Glitch Toolkit** - repository guardrail checks; dev utility (abstractglitch shell per prior sweep).
- /all page-1 names all carry Sep 9 night dispositions; page-2 names repeat the prior sweep's skip set.

## Convention Notes

- The prior (03:00 MST) sweep labeled itself "Night Cron Sweep" and did not write a sweep report file or a sweeps/index.md entry. This midday sweep follows the shift-label rule (03:00 MST = Morning of the calendar date; ~11:00 MST = Midday) and writes the missing report convention for its own slot only.
- Counts on the Last updated line use the rolling sweep-cumulative convention: 620 + 1 = 621 servers, 506 + 1 = 507 guides.
