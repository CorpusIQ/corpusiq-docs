---
title: "MCP Server Scan — July 23, 2026"
description: "Daily MCP server discovery scan. 22 newly merged awesome-mcp-servers PRs. 4 high-value business-operator MCP servers identified with integration guides."
category: mcp
tags: [mcp-scan, discovery, awesome-mcp-servers]
last_updated: 2026-07-23
---

# MCP Server Scan — July 23, 2026

**Sources:** awesome-mcp-servers PR queue (punkpeye/awesome-mcp-servers), mcpservers.org /all page, Smithery registry
**Date:** July 23, 2026, 03:03 MST
**Previous scan:** [July 21 Sweep](/hermes/mcp/servers/external/scan-results-2026-07-21/)
**Coverage:** New server submissions since July 21 sweep

## Methodology

1. **awesome-mcp-servers PR queue** — `gh api repos/punkpeye/awesome-mcp-servers/pulls?state=closed` — 22 merged PRs since July 21
2. **mcpservers.org /all SSR** — 186K chars extracted, 30 featured server names from server-side render
3. **Smithery registry** — 7,318 servers indexed, API accessible
4. **Cross-reference** — All candidates checked against existing catalog (126 entries in `servers/external/`)

## Key Finding: 22 New Servers from awesome-mcp-servers PR Queue

Between July 22-23, 2026, 22 PRs were merged into the awesome-mcp-servers repository. None of these servers are currently in the CorpusIQ external catalog.

### Business-Operator Relevant (Integration Guides Created)

| # | Server | Category | Value | Guide |
|---|--------|----------|-------|-------|
| 1 | **hermoso-ai/hermoso** | Marketing/Advertising | ★★★★★ | [hermoso-mcp.md](/hermes/mcp/servers/external/hermoso-mcp/) |
| 2 | **Correctover/mcp-server** | Legal/API Infrastructure | ★★★★ | [correctover-mcp.md](/hermes/mcp/servers/external/correctover-mcp/) |
| 3 | **lmaniraruta/license-verify-mcp** | Legal/Operations | ★★★★ | [license-verify-mcp.md](/hermes/mcp/servers/external/license-verify-mcp/) |
| 4 | **szp2005/llm-prices-cn** | Finance/Cost Optimization | ★★★ | [llm-prices-cn-mcp.md](/hermes/mcp/servers/external/llm-prices-cn-mcp/) |

### Other New Servers (Catalogued, No Guides Yet)

| # | Server | Category | Notes |
|---|--------|----------|-------|
| 5 | hipvlady/agent-coherence | File Systems | Stale write guard for filesystem agents |
| 6 | Proofpane | Aggregators | Governance proxy |
| 7 | klanex | Developer Tools | — |
| 8 | trustscoreagent | Security | Agent trust scoring |
| 9 | Haunt | Search & Data Extraction | — |
| 10 | turk-hukuku-mevzuat-mcp | Legal | Turkish legislation |
| 11 | GroundTruth-MCP | Developer Tools | — |
| 12 | trainrouter-atlas | Travel & Transportation | — |
| 13 | vectr | Developer Tools | — |
| 14 | CallLint | Security | Pre-flight MCP security linter |
| 15 | server-ops-mcp | DevOps | Server operations |
| 16 | conorbronsdon/podcastindex-mcp | Podcasts | Podcast index access |
| 17 | Appwrite MCP | Development | Official Appwrite MCP server |
| 18 | SeaMeet | Communication | Meeting MCP server |
| 19 | obsideo-mcp | File Systems | — |
| 20 | Booboo | Knowledge & Memory | 3D system graph over MCP |
| 21 | corroborate-mcp | Search & Data Extraction | — |
| 22 | covalent-bond | Communication | — |

## Highlight: hermoso — AI Ad Studio for Agents

**Repo:** [hermoso-ai/hermoso](https://github.com/hermoso-ai/hermoso)
**Install:** `npx -y hermoso mcp` or hosted at `app.hermoso.ai/mcp`

This is the highest-value business-operator MCP server discovered this scan. 52 tools for:
- Generating finished video, image, and UGC avatar ads for any brand
- Script writing, voiceover, music, brand end cards
- Competitor ad research across Meta, Google, and LinkedIn ad libraries
- TikTok/Instagram/YouTube organic content analysis
- Free signup grant, no card required

**Operator use case:** A business operator can tell their AI agent "Research what ads our top 3 competitors are running on Meta and Google, then generate 5 UGC-style video ads for our product using those insights." The agent researches via hermoso, generates the ads, and delivers finished MP4 files — all in one workflow.

## mcpservers.org Direct Submissions (Not in Catalog)

The mcpservers.org /all page (10,139 servers) SSR extraction captured 30 featured servers. 27 are not in our catalog:

| Server | Business-Relevant? |
|--------|-------------------|
| Taplio | Yes (LinkedIn/social) |
| BuiltWith | Yes (tech stack data) |
| FreshBooks MCP | Yes (accounting) |
| KPI Depot | Yes (analytics) |
| FeatureBoard | Yes (product management) |
| Routara LLM Gateway | Yes (API gateway) |
| Santiment | Yes (crypto analytics) |
| Confluence to Markdown MCP Server | Yes (documentation) |
| Index One | Yes (indexing) |
| AIQUAA Playwright MCP Server | Yes (browser automation) |
| Reelier | Low |
| Outside Agent | Unknown |
| Fixou | Unknown |
| Argus Testing | Unknown |
| BountyVerdict Agent Decision Tools | Unknown |
| Retasc | Unknown |
| Agent Browser MCP | Unknown |
| Fable MCP | Unknown |
| KoreanAds | Unknown |
| Peil-mcp | Unknown |
| Google Image MCP | Unknown |
| Grok Chat MCP | Unknown |
| Actvt | Unknown |
| Snipara | Unknown |
| Claude Chat MCP | Unknown |
| BBW Belles Formalwear Evidence | Unknown |
| iGaming Tools | Unknown |
| TaskerArmy Agent | Unknown |
| AI Consensus | Unknown |

**Note:** These 27 servers were extracted from SSR HTML only — descriptions and GitHub repos are not available without browser automation. Full details pending Firecrawl restoration or Mac Mini Playwright scraping.

## Repository Health

- **Existing catalog:** 126 server entries + index.md
- **Last push:** July 20 sweep — 8 new business-operator MCP servers
- **New guides this scan:** 4 (hermoso, correctover, license-verify, llm-prices-cn)

## Next Steps

1. Create integration guides for high-value mcpservers.org servers (Taplio, BuiltWith, FreshBooks, KPI Depot) — requires browser automation for detail pages
2. Monitor awesome-mcp-servers PR queue daily for new business-operator servers
3. Investigate mcpservers.org direct-submission API path for automated discovery
