---
title: "MCP Directory Sweep Report - Aug 26, 2026 (Night)"
description: "MCP ecosystem discovery sweep report: newly catalogued servers, evaluation notes, and skip classifications. Part of the Hermes resource directory."
last_updated: 2026-09-17
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-aug26-2026-night/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp", "ecosystem sweep"]
---

# MCP Directory Sweep Report - Aug 26, 2026 (Night)

**Shift:** Night cron sweep, ~02:00 UTC start (continues the Aug 26 evening)
**Issue cutoff for next shift:** chatmcp/mcpso issue #3786 (Aug 27 01:48 UTC) - start the next shift's issue scan at #3787
**Sources:** chatmcp/mcpso issues #3780-#3786, mcp.so homepage + feed (curl), mcpservers.org homepage (curl)
**Pushed from:** Spark (Mac Mini working copy 2 weeks stale)

## Catalogued (4 new, 4 guides)

| Server | Issue | Relevance | Category | Endpoint | Verification |
|---|---|---|---|---|---|
| Centipid ISP Billing | #3785 | ★★★ | Finance | mcp.centipidbilling.com/mcp | INIT 401 "Unknown API key" = live auth gate; 23 tools documented (20 read-only, 3 in-app approval actions); registry com.centipidbilling/billing v1.0.1 |
| Security Recipes | #3783 | ★★★ | Security | security-recipes.ai/mcp | Keyless live probe: serverInfo security-recipes-mcp v3.4.7, 75 tools captured; Apache-2.0 repo stevologic/security-recipes.ai |
| Legalize | #3781 | ★★★ | IP/Legal | legalize.dev/mcp | INIT 401 "Authorization header required" = OAuth gate live; 7 tools confirmed via public tools.json; MIT, repos legalize-dev/mcp + legalize-dev/legalize |
| BestPrice Shopping | #3780 | ★★★ | Commerce & E-Commerce | mcp.bestprice.gr/mcp | Keyless live probe: serverInfo bestprice-agent-commerce v1.5.1, 3 tools (search_products, compare_offers, get_price_history); repo TheBestCo/bestprice-mcp, no license |

Guides: centipid-billing-mcp, security-recipes-mcp, legalize-mcp, bestprice-shopping-mcp.
Catalog counts: 382 -> 386 servers, 268 -> 272 guides.

## Skipped (evaluated, not catalogued)

- Axiom by Elevated AI #3786: x402 routing + non-custodial crypto swaps for agents - payment plumbing class (Kura, 402oracle precedent).
- ox402-utils #3784: 88 paid tools via x402 on a trycloudflare endpoint - x402 utility infra class.
- ArcadeOps Public Discovery #3782: read-only discovery surface for a governed agent mission-control product - agent infra class, no business data.
- Feed catch-ups recorded for a future sweep: OmniSocials (official social publishing + analytics MCP across 11 platforms, mcp.so feed, createdAt Jul 9 - social management class; needs repo and endpoint verification before cataloguing), Uwear.ai (AI fashion photoshoots from flat-lay product images, createdAt Jul 25 - creative utility class, 3dlogo-adjacent), FastGPU (live GPU price comparison across 28+ providers on mcpservers.org - endpoint not verifiable from public pages, MetricFire thin-docs precedent).
- mcpservers.org homepage slugs mapped to established skip classes: AgentCloud (hosted iOS simulator - dev tool), Count Nanocorp (shared-expense ledger - consumer finance), ProxyLoom (multi-tenant MCP gateway - agent infra), Runbear (AI agent deployment to Slack - agent infra).
- Feed and homepage repeats already evaluated in Aug 24-26 sweeps (Speccy x402, Jitsu, Hologrow, OpenLore, LM Legion, fhirHydrant, QuanticData, Windframe, Alpha Sophia, HostTracker, Routebase, Agentic Atlas, RE Data Refinery, AgentRisk M2M, OAIA Arena, ReactVision, uxgen, BitBrowser, Shotstack, Agency AI, SSH MCP Server, SecondSim, Batru, Ice Juice, Granola, Minimax, Proxyman).

## Notes

- All 4 catalogued servers came from the GitHub issues window #3780-#3786 - the freshest surface again. Homepage/feed were repeats plus catch-up slugs.
- Security Recipes: 75 live-probed tools is the largest anonymous tool list of any night sweep; the operator-relevant core is the CVE catalog (cve_search/cve_get with bounded change plans) and remediation playbook tools, with the enterprise agentic-governance packs as secondary value.
- Centipid: no public GitHub repo (hosted only) - guide ships stars: n/a with docs.centipidbilling.com as the reference source.
- BestPrice: license not declared in repo (API returns None) - guide states it honestly.
- Index last-updated line corrected the afternoon sweep's drift (it had left 381/267 counts while cataloguing 3dlogo to 382/268); this sweep's line carries 386/272.
