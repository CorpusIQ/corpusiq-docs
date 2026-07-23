---
title: "MCP Server Sweep — July 22-23, 2026 (Cron Discovery)"
description: "Cron-triggered sweep of mcp.so and mcpservers.org. 14 net-new servers discovered (8 not in any prior sweep). 8 integration guides drafted for business-operator-relevant servers. Headline finds: Goalie Trademark Search (14M USPTO records), FeatureBoard (agentic governance), Routara LLM Gateway (787+ models), Confluence2MD (offline Confluence search)."
category: mcp
tags: [mcp-servers, discovery, sweep, catalog, 2026, cron]
last_updated: 2026-07-22
---

# MCP Server Sweep — July 22-23, 2026 (Cron Discovery)

Automated cron-triggered sweep of mcp.so and mcpservers.org, cross-referenced against the existing 196-server catalog. 14 net-new servers identified, 8 integration guides drafted for business-operator-relevant finds.

**Source:** mcp.so (homepage SSR data) + mcpservers.org (homepage SSR data)
**Previous sweeps:** July 22 morning (8 from mcp.so), July 22 evening (47 from GitHub API)
**This sweep:** 14 net-new, 8 high-value guides created
**Total catalog:** 204+ servers now tracked

## Methodology

1. Scraped mcp.so homepage — extracted recent + featured servers from SSR JSON payload
2. Scraped mcpservers.org homepage — extracted latest + featured servers from SSR JSON payload
3. Cross-referenced all candidates against existing catalog (`servers/external/`)
4. Filtered duplicates (already in evening sweep, already in morning sweep)
5. Prioritized business-operator-relevant servers for guide creation

## Headline Finds (★ = operator relevance)

| Server | Source | Category | Why It Matters |
|--------|--------|----------|----------------|
| **Goalie Trademark Search MCP** ★★★ | mcp.so | IP/Legal | 14M+ USPTO trademark records. First dedicated trademark MCP. Brand clearance + competitive IP monitoring from any agent. |
| **FeatureBoard MCP** ★★★ | mcpservers.org | AI Operations | Agentic governance + orchestration + task planning. First MCP server specifically for managing AI agent operations. |
| **Routara LLM Gateway** ★★ | mcpservers.org | AI Infrastructure | 787+ chat/image/video models behind one OpenAI-compatible MCP endpoint. Single config for multi-model access. |
| **Outside Agent** ★★ | mcpservers.org | AI Agents | Build + deploy production AI agents to web, SMS, and phone from your coding agent. Multi-channel from one definition. |
| **Confluence to Markdown MCP** ★★★ | mcpservers.org | Knowledge Management | Hybrid search over locally-synced Confluence content. Offline-capable, no API rate limits. |
| **Reelier** ★★★ | mcp.so | AI Operations | Agent workflow recording + deterministic replay at zero tokens. Drift detection, compliance audit trail. |
| **Moxie Docs** ★★ | mcp.so | Documentation | Auto-generated codebase docs, MCP context for agents, doc drift detection, Friday Cleanup PRs. |
| **FT Optix MCP** ★★ | mcp.so | Industrial | First industrial automation MCP — connects FT Optix Studio (SCADA/HMI/IoT) to LLMs. |

## Full Discovery List (14 Servers)

### New from mcp.so (not in prior sweeps)

| # | Server | Category | Stars | Guide |
|---|--------|----------|-------|-------|
| 1 | goalie-trademark-search-mcp | IP/Legal | 0★ | ✅ |
| 2 | twocents | Productivity | 0★ | ❌ |
| 3 | reelier-mcp | AI Operations | 0★ | ✅ |

### New from mcpservers.org (not in prior sweeps)

| # | Server | Category | Stars | Guide |
|---|--------|----------|-------|-------|
| 4 | featureboard-mcp | AI Operations | 0★ | ✅ |
| 5 | routara-llm-gateway | AI Infrastructure | 0★ | ✅ |
| 6 | outside-agent-mcp | AI Agents | 0★ | ✅ |
| 7 | confluence2md-mcp | Knowledge Management | 0★ | ✅ |
| 8 | fixou | Other | 0★ | ❌ |
| 9 | argus-testing | Testing/QA | 0★ | ❌ |
| 10 | koreanads | Marketing | 0★ | ❌ |
| 11 | bbw-belles | Search | 0★ | ❌ |

### From morning sweep (July 22) — now with guides

| # | Server | Category | Stars | Guide |
|---|--------|----------|-------|-------|
| 12 | moxie-docs-mcp | Documentation | 1★ | ✅ |
| 13 | ft-optix-mcp | Industrial | 0★ | ✅ |
| 14 | yandex-wiki-search-mcp | Knowledge | 0★ | ❌ |

## Integration Guides Created (8)

1. **Goalie Trademark Search MCP** — 14M USPTO records. Brand clearance + competitor IP monitoring.
2. **FeatureBoard MCP** — Agentic governance, orchestration, task planning. First agent ops MCP.
3. **Routara LLM Gateway MCP** — 787+ models, OpenAI-compatible. Multi-model routing.
4. **Outside Agent MCP** — Deploy agents to web/SMS/phone. Multi-channel production.
5. **Confluence to Markdown MCP** — Offline Confluence search. No API rate limits.
6. **Reelier MCP** — Agent workflow recording + deterministic replay. Audit trail.
7. **Moxie Docs MCP** — Auto-generated docs + drift detection + cleanup PRs.
8. **FT Optix MCP** — Industrial automation. SCADA/HMI to LLM bridge.

## Key Observations

1. **Agent operations tooling is emerging as a category.** FeatureBoard (governance) + Reelier (audit/replay) represent a new MCP subcategory: tools for managing AI agents themselves, not just tools for AI agents to use. This is the beginning of the "agent ops" layer.

2. **IP and legal MCPs are arriving.** Goalie Trademark Search is the first dedicated IP MCP server, following Patsnap (patent search, morning sweep) and Lawstronaut (legal research). Legal/compliance is becoming a distinct MCP vertical.

3. **Industrial MCP is real.** FT Optix MCP bridges the OT/IT gap — factory floor data accessible from AI agents. Combined with OPC UA MCP (otgate, evening sweep), industrial automation is emerging as an MCP vertical.

4. **Remote MCP adoption growing.** Outside Agent and Routara both use remote MCP (HTTP endpoints). The ratio of remote vs local MCP servers is shifting as managed platforms enter the ecosystem.

5. **Catalog now at 204+ servers.** Growth rate: ~28 new servers/day across all discovery sources. mcp.so is the fastest-turnaround listing platform; mcpservers.org has the deeper catalog. Both should be monitored.

## CorpusIQ Angle

The catalog now covers 204+ MCP servers — the most operator-focused collection available. New additions this sweep that are directly relevant:

- **FeatureBoard** is architecturally adjacent to CorpusIQ's multi-agent operations. Worth evaluating as a potential integration or partnership.
- **Confluence2MD** fills a gap for enterprise operators who live in Atlassian. Pairs with existing Atlassian MCP guide.
- **Reelier** addresses the compliance/audit requirement that enterprise operators increasingly need for AI agent operations.

## See Also

- [[sweeps/sweep-july22-2026-evening]]
- [[sweeps/sweep-july22-2026]]
- [[sweeps/sweep-july21-2026-late-night]]
- [[index]]
