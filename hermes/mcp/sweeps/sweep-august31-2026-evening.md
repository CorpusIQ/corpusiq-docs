---
title: "Sweep Report - August 31, 2026 - CorpusIQ Docs"
description: "Evening MCP catalog sweep: mcp.so recentServers + mcpservers.org latest, cataloging new servers into the CorpusIQ MCP ecosystem directory."
date: 2026-08-31T19:00:00-07:00
sources: [mcp.so, mcpservers.org]
status: complete
last_updated: "2026-10-24"
---

# Sweep Report - August 31, 2026 (Evening Cron Sweep)

- **Shift:** Evening (run ~19:00 MST, ~02:00 UTC Sep 1)
- **Fresh window:** mcp.so homepage recentServers array (createdAt-filtered) + mcpservers.org homepage latest array (7 newest ids)
- **Prior sweep cutoff:** afternoon sweep stamp 18:09 UTC, dispositions respected
- **Outcome:** 2 new servers catalogued with guides; 1 live-verified over JSON-RPC

## Catalogued (2)

| Server | Source | Verification chain |
|--------|--------|--------------------|
| CarChat Inventory MCP | mcp.so recentServers (newest, listed after afternoon sweep) | Live probe carchat.io/mcp: serverInfo carchat v1.0.0, protocol 2025-06-18, all 6 tools captured with schemas. Discovery card at carchat.io/.well-known/mcp.json. Repo Carchat-io/mcp (MIT, 0 stars, created Aug 31). No auth, free. |
| ConsentStack MCP | mcpservers.org homepage latest (id 12463) | Endpoint app.consentstack.io/api/mcp 401-verified live (invalid_token, OAuth 2.1 gate enforced as documented). 22 tools per vendor docs (site creation, draft-staged banner config, publish, install snippet, compliance scans, tracker categorization). Registry io.consentstack/cookie-consent. Free Basic tier. |

## Skipped (mcpservers.org latest)

- **GridCarbon (github-com-gridcarbon-clients-tree-main-mcp)** - grid carbon intensity (gCO2eq/kWh) for 45 zones from ENTSO-E, EIA-930, NESO. Pre-alpha single-dataset utility class (fetch-cwe-list precedent).
- **Onchain Diary (theonchaindiary-com-mcp)** - read-only Web3 on-chain security knowledge base, 97 articles + 220 glossary terms, EN+ZH. Niche educational class (Hispanic Legacy precedent).
- **CordFind (gokimedia/cordfind-mcp)** - generator guide search and extension-cord sizing. Consumer DIY class.
- **Vaanzari Commerce (vaanzari/vaanzari-commerce-mcp)** - Banarasi saree discovery and shopping workflows. Consumer commerce class.
- **Firefly III (yakupemreyerli/mcp-firefly-iii)** - self-hosted personal finance with scoped read/write/delete tools. Personal-finance class.
- **SigVest (www-getsigvest-com-mcp)** - 14 personal portfolio tools (analysis, news impact, tax harvesting). Consumer investing class.

## Skipped (mcp.so recentServers repeats)

- file2markdown, BiGapi, DrillerDB, MagicPixel.art, Forency, TikTok Transcript MCP, CrawlForge - all prior-sweep dispositions or earlier catalog entries (verified against index prose).

## Notable dispositions

- **mcpservers.org homepage latest array is the freshest non-issues signal:** the 7 newest ids (12458-12464) were absent from the afternoon sweep's /all page-1 dispositions, confirming they were indexed after the 18:09 UTC stamp. The array carries no timestamps in the current hydration format; freshness was inferred from the strictly increasing id sequence plus absence from prior dispositions.
- **Consumer-platform rule applied to CarChat:** the product is a consumer car-shopping assistant, but its data tools (get_market_prices, list_dealers, search_inventory) answer operator questions with live dealer-sourced market data - catalogued on the Worklittle precedent (data tools serve operator questions even when the product shell is consumer).
- **Rule-15 liveness signal for OAuth endpoints:** ConsentStack's unauthenticated initialize returned a clean 401 invalid_token - endpoint live, auth gate enforced exactly as documented, no keyless probe possible by design.

## Commit

- Guides: carchat-inventory-mcp, consentstack-mcp
- Index: top section + tail block + last-updated line (453 servers, +339 guides)
- Validation: 2/2 guides clean (YAML, lengths, em-dash, credential-guard, See Also dirs + labels); repo validate_frontmatter.py gate green
