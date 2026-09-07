---
title: "MCP Server Discovery - September 7, 2026 (Midday Sweep)"
description: "Midday sweep over chatmcp/mcpso issues #3938-3990, the mcp.so feed and homepage recentServers, and mcpservers.org /all page 1. 19 new business-relevant servers catalogued with guides across marketing, SEO/GEO, real estate, monitoring, email, productivity, social publishing, marketplace and lead-gen classes."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-09-07
---

# MCP Server Discovery - September 7, 2026 (Midday Sweep)

**Source:** chatmcp/mcpso issues #3938-#3990, mcp.so feed and homepage recentServers, mcpservers.org /all page 1 (r.jina.ai reader proxy)
**Method:** GitHub issues API (100-issue window with bodies), feed $R-stream parsing, parse-homepages.py, batch-probe.py endpoint probes (12 endpoints), GitHub API repo checks, npm/PyPI registry checks, vendor README extraction
**Date:** September 7, 2026 ~18:00-19:00 UTC

## Summary

| Metric | Count |
|---|---|
| Fresh issue window | 53 issues (#3938-#3990), 25 bodies read |
| mcp.so feed fresh blocks | 4 (1 consumer skip, 3 evaluated) |
| mcpservers.org /all page 1 | 30 entries (all classified) |
| Endpoints probed | 12 (4 keyless with captured tool lists, 8 auth-gated liveness) |
| New servers catalogued | 19 |
| Integration guides written | 19 |
| Skipped (not catalogued) | 33 classes plus 1 premature (fr-legal-kit) |

## New Business-Relevant Servers (19 guides)

| Server | Slug | Class | Verification |
|---|---|---|---|
| LoomaScale Google Ads | loomascale-google-ads-mcp | Marketing | 42 tools from repo google-ads README; api.loomascale.com/mcp 401-live; MIT; budget caps + no-silent-activation |
| Beamtrace | beamtrace-mcp | SEO | 5 tools from repo README; beamtrace.com/api/mcp 401-live; built by Elfsight |
| AuraCite | auracite-mcp | SEO | OAuth 2.1 PKCE; auracite.de/mcp/rpc 401 invalid_token with mcp:read scope; repo getauracite/claude-plugins |
| PropRaven | propraven-mcp | Real Estate | propraven.com/mcp 401-live (OAuth or pz_ key); 8 stdio tools + 40-endpoint OpenAPI; npm @propraven/mcp Apache-2.0 |
| RealUptime | realuptime-mcp | Business Operations | Keyless mcp.realuptime.io/public served 7 tools (serverInfo realuptime-outages v0.1.0); keyed endpoint 401 RU-1001 |
| RankCLI | rankcli-mcp | SEO | npm @rankcli/mcp-server 0.0.7; repo integrallis/rankcli-cli MIT; 280+ checks |
| CuePrecise | cueprecise-mcp | Content & Research | 10 tools from issue + README; repo Nattentia/cueprecise MIT; not on PyPI |
| smtp-mcp | smtp-mcp | Communication & Email | npm @ni-c/smtp-mcp 0.2.0; imap-mcp outbound counterpart; 4-point guardrail design |
| caldav-mcp | caldav-mcp | Productivity | npm @ni-c/caldav-mcp 0.1.3; 22 tools; read-only mode and calendar fencing |
| carddav-mcp | carddav-mcp | Productivity | npm @ni-c/carddav-mcp 0.1.1; 17 tools; group-convention aware |
| Ambassly | ambassly-mcp | Marketing | ambassly.com/api/mcp 401 invalid_token; scoped company/affiliate keys; hosted, no repo |
| PendPost | pendpost-mcp | Social Media Management | npm pendpost 2.3.0; repo 7 stars MIT; 11 platforms; approval gate |
| TimeToPost | timetopost-mcp | Social Media Management | api.timetopost.co/mcp 401; 30+ tools from README; draft approvals + AutoSEO |
| Chirpie | chirpie-mcp | Social Media Management | chirpie.ai/mcp 401 JSON-RPC; npm @chirpie/mcp 1.0.35; 22 tools; 14 platforms |
| marketplaces-mcp-ru | marketplaces-mcp-ru | Commerce & E-Commerce | PyPI 0.5.2; repo 25 stars MIT; 793 methods WB/Ozon/YM/Avito |
| LinkDigest | linkdigest-mcp | Content & Research | linkdigest.dev/mcp keyless tool surface (1 tool); MIT repo |
| VetAgent | vetagent-mcp | Finance | vetagent.dev/mcp keyless, 3 tools captured; MIT; fail-closed verdicts |
| Crawdar | crawdar-mcp | Lead Generation & Web Scraping | crawdar.com/api/mcp keyless, 9 tools captured; async lead jobs |
| Kuudo Amazon suite | amazon-kuudo-mcp-suite | Commerce & E-Commerce | SP-API + Vendor Central catalogs; BYOC deployment; registry + MIT metadata repos |

## Skipped (Not Catalogued)

| Class | Servers |
|---|---|
| Premature (endpoint dead) | fr-legal-kit #3985 (Cloudflare Error 1042, worker not deployed at probe time) |
| x402 gateway / pay-per-call infra | Synergy #3973, AgentBIT #3968 |
| Media/news | AllNewsAPI #3974 |
| Dev utility / personal | loci #3967, dataset-mcp #3981, rebuild-dossier #3957, hdply #3946, OrcaReplay #3979, Codex Cursor Subagent #3949, Ritwik Joshi #3942 |
| Agent infra / memory | ContextStream #3954, Pod #3948, Wyrm #3965, Flow Agent Bus #3984, PersonalKnowHow #3988 |
| Directory / gateway infra | optigate #3989, MCPX #3976, Toolfound |
| Consumer | create-prints, Polymarket #3990, AIm Workout Journal, MyFlohmarkt, Solana Sniper #3945/#3939 |
| Resubmissions | assistantmail-mcp #3952, Antwork #3986 |
| AI-text rewrite QA | Pain in the Agent #3983 |
| Page-1 class skips | notifyd, NarcoScope, LiquiLens, ZettaQuant, AskAgent, HTML Table Maker, jira-alerts, NavisCoord, Council of AI GSPC, Tetrees, InvokeWorks, docs2mcp, Otito, getdeck, BlackForge, SnowSignals, Undertow (last three recorded as catch-up candidates) |

## Catch-up candidates for future sweeps

- reddapi.dev MCP (Reddit semantic search and lead discovery, free tier, endpoint reddapi.dev/api/mcp)
- BlackForge (crypto spot market data across 9 venues)
- SnowSignals TrendVane (crypto market-phase data)
- Undertow (market-liquidity research with exit-cost context)

## Actions Taken

- 19 guides written to hermes/mcp/servers/external/<slug>/index.md
- Index updated: last-updated line (580 servers, +466 guides), top midday sweep section, tail block entry
- `.last-sweep` stamped
- validate-guides.py 19/19 PASS, repo frontmatter gate 4,002 files green, See Also dir + label checks clean
