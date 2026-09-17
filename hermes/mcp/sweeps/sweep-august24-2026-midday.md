---
title: "Sweep Report - August 24, 2026 (midday cron sweep)"
description: "MCP ecosystem discovery sweep report: newly catalogued servers, evaluation notes, and skip classifications. Part of the Hermes resource directory."
last_updated: 2026-09-17
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-august24-2026-midday/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp", "ecosystem sweep"]
---

# Sweep Report - August 24, 2026 (midday cron sweep)

**Sources:** chatmcp/mcpso issues #3726-#3734 (Aug 24 10:50-17:48 UTC), mcp.so homepage recentServers + /feed, mcpservers.org /all page 1
**Prior sweep cutoff:** issues #3719-#3725 (morning sweep, 10:18 UTC stamp)

## Catalogued (4 new, 4 guides)

| Server | Repo / Endpoint | Verification | Category | Relevance |
|---|---|---|---|---|
| Salesbot MCP (LinkedIn + Sales Navigator, 48 tools, x-mcp-api-key) | Kubis010/linkedin-mcp-server-salesbot (MIT, Jun 10 2026) / app.salesbot.cz/api/mcp | Anonymous tools/list returned ALL 48 tool names matching the issue claim exactly | Marketing | ★★★ |
| Social Glass (cultural intelligence: Insights, Posts, Creators, Audiences, OAuth) | Social-Glass-AI/social-glass-agent-plugins (Jun 9 2026) / mcp.socialglass.ai/mcp | 401 Unauthorized = OAuth endpoint live; vendor docs fetched (get_context first, read tools for members, write tools admin-only) | Content & Research | ★★★ |
| SudnoKontrol MCP (Ukrainian vessel registries, keyless) | ailubes/sudnokontrol-mcp (MIT, created Aug 24 2026) / api.sk.ukrfish.org/mcp | LIVE PROBE v1.0.0: 4 tools confirmed (search_vessel_registries, lookup_vessel, get_registry_stats, get_dataset_metadata) | Compliance & Regulatory | ★★ |
| Google Flights Search (real-time fares, BYO RapidAPI key) | mtnrabi/google-flights-mcp (MIT, created Aug 24 2026) / google-flights-mcp.flightpowers.com/mcp | LIVE PROBE v1.0.0: initialize + tools/list on both endpoints (2 tools: search_oneway_flights, search_roundtrip_flights); /health 200; free ad-supported mirror at google-flights-lulu.flightpowers.com/mcp | Content & Research | ★★ |

## Skipped (6 issues + homepage arrivals)

- **#3726 Sentinel Scan** - free CLI for MCP manifest security and prompt-injection testing - dev tool.
- **#3727 ParetoStudio** - local prompt/agent/skill library manager - dev utility class.
- **#3732 Concord MCP** - cross-harness communication for coding agents - dev infra.
- **#3731 54ch10-mcp** - pre-interact wallet/URL risk briefs paid in x402 USDC - x402 infra class.
- **AgentRisk M2M** (homepage arrival, Aug 24) - pre-trade DeFi agent security with x402 micropayments - crypto/x402 class, Magpie Capital precedent.
- **SSH MCP Server** (homepage arrival, future-dated 2026-08-25 = timezone artifact) - developer tools.
- mcpservers.org /all page 1: dockndevai/mcp-* family (kafka, clickhouse, debezium, azure-devops, oci, keycloak, kubernetes) - dev infra family; lvtd-llc/skills (skills catalog), plurality-mcp-server (web3), reqlan, wickedapi, famulor, hireme, diffcontext, m00nreport - previously evaluated or dev-class.
- Feed/homepage repeats already evaluated in Aug 23 sweeps: RE Data Refinery, Truth Bear GAUGE, Agent Conductor, CodeSentinel, BitBrowser, Mangii, Hypnothera, AskRentAI, Signal Nodus, etc.

## Notes

- The Aug 23 skip of Booking.com Hotel Search was the same FlightPowers vendor with a thin listing; the Google Flights product above is fully documented (repo, registry ID com.flightpowers/google-flights, live endpoint, health check), so it clears the thin-docs bar.
- Issue #3728 absent from the open-issues list (closed or deleted between submission windows).
- 4 guides written with probed tool names; capability-level table only for Social Glass (OAuth refuses anonymous enumeration, documented surface used with explicit caveat line).
