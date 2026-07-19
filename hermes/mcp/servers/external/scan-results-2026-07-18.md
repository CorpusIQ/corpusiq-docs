---
title: "MCP Server Scan Results — July 18, 2026"
description: "Daily MCP server discovery scan from mcp.so + mcpservers.org. 4 new servers found, 2 guides created: Vibgrate MCP (dependency drift/CVE intelligence) and Octolens (brand monitoring across 15+ platforms)."
category: mcp
tags: [mcp-scan, discovery, mcp-servers]
last_updated: 2026-07-18
---

# MCP Server Scan — July 18, 2026

**Sources:** mcp.so (React SPA, text extraction) + mcpservers.org (TanStack Router hydration payload)
**Date:** July 18, 2026
**Previous scan:** July 17, 2026 (evening supplement)
**Coverage:** July 18 new submissions on both platforms, plus catch-up on July 15-17 servers missed in prior scans

## Methodology

Both sources accessed via curl text-stripping from SPA hydration payloads (Firecrawl unavailable on this node). Cross-referenced all candidates against the existing catalog (index.md + 100+ guide files + prior scan reports including July 17 evening supplement). Four servers identified as net-new — two from July 18, two missed from July 15-17.

## New Servers Found: 4 total, 2 guides created

### Guide-Worthy (Major) — Guides Created

| Server | Source | Description | Guide |
|--------|--------|-------------|-------|
| **Vibgrate MCP** ★★★ | mcp.so | Dependency drift, CVE vulnerability scanning, and EOL runtime detection for AI agents. 51 tools across 14 groups — DriftScores, blast-radius analysis, upgrade paths, org catalog management. OAuth 2.1, scoped tokens, metadata-only (source code never leaves your environment). Apache 2.0. | [vibgrate-mcp](/hermes/mcp/servers/external/vibgrate-mcp/) |
| **Octolens** ★★★ | mcp.so | Brand monitoring across 15+ platforms (Reddit, X, LinkedIn, HN, YouTube, Bluesky, GitHub, Stack Overflow, podcasts, newsletters, TikTok). AI-filtered mentions with sentiment scoring. Remote MCP via Streamable HTTP + OAuth. Used by Vercel, PostHog, Prisma. | [octolens](/hermes/mcp/servers/external/octolens/) |

### INDEX-ONLY (Niche or Previously Noted)

| Server | Source | Description |
|--------|--------|-------------|
| **Lumify Sports Intelligence** | mcp.so | Real-time sports schedules, live scores, odds, betting splits, and AI bet intelligence. Niche (sports betting). |
| **BetterBugs** | mcp.so | Bug report loading for AI agents — connect BetterBugs reports to Cursor, VS Code, and other MCP clients. Developer testing niche. |

## Key Finding: Vibgrate MCP — Supply Chain Security Goes MCP-Native

Vibgrate MCP is the first MCP server dedicated to software supply chain security. It bridges the gap between AI coding agents and infrastructure health data:

1. **New MCP category:** "Dependency Intelligence" — no existing MCP server covers this surface. Vibgrate is first to market.

2. **Security-first architecture:** The MCP server exposes only metadata (DriftScores, CVE IDs, EOL dates) — source code never leaves the developer's environment. OAuth 2.1 with scoped, revocable tokens.

3. **Operator relevance:** Any business running production software needs to track dependency drift and CVEs. Vibgrate turns this from a periodic scanner run into a conversational workflow — operators can ask their AI assistant directly.

4. **Dual deployment:** Vibgrate Cloud (remote MCP) for team-wide visibility + Vibgrate AI Context (`vg serve`) for local-first, offline code intelligence.

## Key Finding: Octolens — Brand Monitoring Enters the MCP Era

Octolens represents the first MCP-native brand monitoring solution, covering 15+ platforms:

1. **Marketing operator tool:** Directly useful for CorpusIQ's core audience — marketers and operators who need to track brand mentions without logging into dashboards.

2. **AI-first architecture:** Every mention is AI-filtered for relevance and sentiment-scored before the agent sees it. No raw firehose — structured, actionable intelligence.

3. **SQL-powered:** Agents can run SQL queries over the entire mention history, enabling complex analysis (sentiment trends, platform breakdowns, competitor comparisons) directly in conversation.

4. **Enterprise validation:** Used by Vercel, PostHog, and Prisma — strong signal of production readiness.

## Trends

1. **Remote MCP servers dominate new submissions:** Both major finds are remote MCP servers (Streamable HTTP + OAuth), continuing the trend away from local stdio servers. The MCP ecosystem is maturing toward cloud-hosted, zero-install experiences.

2. **Operational tools arrive:** Octolens (brand monitoring) and Vibgrate (supply chain security) represent a new class of MCP servers — tools for business operators, not just developers. The MCP ecosystem is expanding beyond its developer-tools origins.

3. **Supply chain security emerges:** Vibgrate opens a new MCP category. With software supply chain attacks rising, expect more security-focused MCP servers.

## Actions Taken

- ✅ 1 integration guide created for Vibgrate MCP (supply chain security — new category)
- ✅ 1 integration guide created for Octolens (brand monitoring — marketing ops)
- ✅ 2 servers noted as INDEX-ONLY (Lumify Sports, BetterBugs)
- ✅ Scan report created
- ✅ Index entries added

---

*← [Back to External MCP Catalog](/hermes/mcp/servers/external/) | [Previous Scan (July 17 Evening)](/hermes/mcp/servers/external/scan-results-2026-07-17-supplement/) →*
