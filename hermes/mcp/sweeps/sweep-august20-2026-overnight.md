---
title: "MCP Discovery Sweep — August 20, 2026 (Overnight)"
date: 2026-08-20
tags: [mcp-sweep, discovery, catalog]
description: "chatmcp/mcpso GitHub issues filed Aug 19 16:03 through Aug 20 02:00 UTC plus mcp.so and mcpservers.org homepages; 5 catalogued with guides, 6 skipped"
---

# MCP Discovery Sweep — August 20, 2026 (Overnight)

- **Cutoff:** prior sweep evaluated through issue #3649 (Aug 19 16:03 UTC)
- **Fresh window:** issues #3650–#3653, mcp.so homepage arrivals, mcpservers.org homepage slugs
- **Result:** 5 catalogued with guides, 6 skipped

## Catalogued (5 guides)

| Server | Stars | Category | Source |
|---|---|---|---|
| Analytics Legends MCP (SAP analytics market intelligence: firm directory, day-rate P25/P50/P75 benchmarks, contract radar, citation URL on every row, population sizes in every response; hosted at analyticslegends.ai/mcp, 14 tools keyless, 6 subscriber) | n/a | Content & Research | GH issue #3651 |
| SavePropTax MCP (California Prop 8 property tax appeals: free over-assessment checks, county form prep, owner-signed filing at flat $29; keyless remote at saveproptax.com/mcp) | n/a | Finance | mcp.so homepage arrival |
| Dutch Property Context MCP (verified property reports per Dutch address from 9 official sources incl. BAG, energy label, CBS stats, monument status; free keyless remote at property-context.tradebrite.nl/mcp) | n/a | Real Estate | mcpservers.org |
| Dutch Vehicle Context MCP (verified vehicle reports per Dutch plate from 11 registers incl. APK history, recall chain, odometer verdict; free keyless remote at vehicle-context.tradebrite.nl/mcp) | n/a | Commerce & E-Commerce | mcpservers.org |
| Taskfolk MCP (first-party project-management MCP mirroring ~180-op REST API with scoped keys, webhooks, audit views; remote at taskfolk.ai/api/mcp/v1) | n/a | Productivity | mcpservers.org |

## Verification performed

- Analytics Legends: repo live (MIT, created Aug 11, pushed Aug 19), website live, registry ai.analyticslegends/sap-analytics v1.0.6, llms.txt live
- SavePropTax: repo live (MIT, created Aug 19), README parsed for tool table, endpoint live
- Dutch Property Context: live JSON-RPC initialize + tools/list probe — `get_verified_property_context`, server v0.5.0
- Dutch Vehicle Context: live JSON-RPC initialize + tools/list probe — `get_verified_vehicle_context`, server v0.1.0
- Taskfolk: site + /developer page live, MCP endpoint returns 401 (authenticated, expected), ~180-op REST parity documented

## Skipped (evaluated, consistent with prior decisions)

- #3650 Front of Goal Odds Agent — soccer prediction-market data; sports skip precedent (footballcharts, livetennisapi)
- #3652 Vibes-Coded — x402 pay-per-call agent utilities; infrastructure skip precedent (402oracle)
- #3653 Krimskrams Paid APIs — npm package not yet published ("coming soon"), mixed grant-search and marketplace-admin scope, x402 wallet setup, submitted by an autonomous agent
- 60fps Design MCP — motion-reference design niche
- MindMap AI MCP — consumer mind-mapping niche
- FlightPowers hotel support — thin vendor support surface
- CSOAI GSPC measurement — already noted in prior sweeps (July 3 scan, Aug 19 afternoon)

## Catalog state

- Before: 272 servers, 162 guides
- After: 277 servers, 167 guides
- CI frontmatter gate: 3,204 files scanned, all valid
- Next sweep cutoff: issue #3653
