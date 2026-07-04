---
title: "MCP Server Discovery — July 4, 2026 (Evening)"
description: "Daily scan of mcpservers.org and mcp.so for new business-relevant MCP servers. 5 new servers across communication, knowledge management, design, productivity, and security categories."
category: mcp
tags: [mcp-servers, daily-scan, july-2026]
last_updated: 2026-07-04
---

# MCP Server Discovery — July 4, 2026 (Evening)

**Source:** mcpservers.org (homepage), mcp.so (homepage)
**Method:** Scrape both directories, cross-reference against 47 existing catalogued servers
**Date:** July 4, 2026 (evening)
**Prior scan:** [July 3 evening](/hermes/mcp/servers/external/scan-results-2026-07-03-evening/)

## Summary

| Metric | Count |
|--------|-------|
| New servers discovered on mcpservers.org (latest) | 8 |
| Already catalogued or developer-only | 3 |
| **New business-relevant** | **5** |
| **Full integration guides created** | **3** |
| Noted (niche or early-stage) | 2 |

## Priority Servers — Full Integration Guides Created

| # | Server | Category | Description | Source |
|---|--------|----------|-------------|--------|
| 1 | **Plaud MCP** | Communication & Meetings | Connect Plaud.ai recordings to AI agents. Search recordings, read transcripts, generate summaries and documents. Essential for operators who record client calls, team meetings, and partner conversations. | mcpservers.org |
| 2 | **Astucia Wiki MCP** | Knowledge Management | AI-native team wiki with semantic search, auto-organization, and MCP-native read/write access. Finally, a wiki your AI agent can actually use — not a graveyard of unsearchable pages. | mcpservers.org |
| 3 | **Design Context Bridge** | Product Design & Development | Turns AI agents into frontend developers that read Figma files natively — components, design tokens, routes, icons, and states. Faithful design-to-code, not screenshot guessing. | mcpservers.org |

## Additional Notable Servers (Indexed, No Individual Guide)

| Server | Category | Description | Source |
|--------|----------|-------------|--------|
| **Synaplan Multimodal Gateway** | Productivity | Multimodal MCP gateway from metadist — early-stage, sparse documentation. Watched for future development. | mcpservers.org |
| **Creed Space** | AI Safety & Security | Constitutional-AI safety guardrails for any LLM. 16 stdio tools for persona and constitution management. Infrastructure-layer security — less relevant for business operators directly. | mcpservers.org |

## Already Catalogued (No Action)

| Server | Status |
|--------|--------|
| Mowgli | Already documented — `mowgli-mcp.md` (July 3) |
| Periscope MCP | Already documented — `periscope-mcp.md` (July 2) |
| SaferAgenticAI MCP | Already documented — `saferagenticai-mcp.md` (July 1) |

## mcp.so Scan Results

mcp.so homepage scanned — no net-new business-relevant servers beyond what mcpservers.org captured. Most new entries were China-market (Amap Maps, Baidu Map), developer-tooling (EdgeOne Pages, AgentQL, Jina AI), or already well-known (Playwright, Firecrawl, PostgreSQL, Redis). No new integration guides created from mcp.so this session.

## Trends

- **Recording intelligence**: Plaud MCP represents a growing category — meeting/recording platforms adding MCP access. This follows Granola MCP (July 3) and signals that "queryable meeting memory" is becoming table stakes for AI-native operators.
- **Wiki reimagined for AI**: Astucia Wiki isn't just another wiki with an API — it's built from the ground up assuming AI agents are primary consumers of wiki content. The "agent-first wiki" pattern may redefine how teams manage institutional knowledge.
- **Design tools go MCP-native (continued)**: Design Context Bridge extends last session's trend of design tools that don't just show designs but let AI agents read, modify, and transform them. Combined with Mowgli (July 3), we're seeing a design-tool stack purpose-built for AI-assisted development.

## Actions Taken

- 3 full integration guides created:
  - `plaud-mcp.md`
  - `astucia-wiki-mcp.md`
  - `design-context-bridge-mcp.md`
- 2 additional servers noted (indexed, no individual guide — early-stage or infra-layer)
- Scan report created and catalog updated
- Changes pushed to GitHub (corpusiq-docs)

## Non-Business Servers (Not Catalogued)

- Synaplan Multimodal Gateway — too early stage, minimal documentation
- Creed Space — AI safety infrastructure (security/LLM governance layer, not operator-facing)
- Various China-market map/data tools (Amap, Baidu Map) — regional
- Developer tooling servers (EdgeOne Pages, AgentQL, Jina AI) — developer-focused

---

*← [Previous Scan (July 3 evening)](/hermes/mcp/servers/external/scan-results-2026-07-03-evening/) | [External MCP Catalog](/hermes/mcp/servers/external/) →*
