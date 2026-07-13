---
title: "MCP Server Scan Results — July 12, 2026"
description: "Daily MCP server discovery scan from mcp.so/feed. 14 new business-relevant servers found."
category: mcp
tags: [mcp-scan, discovery, mcp-servers]
last_updated: 2026-07-12
---

# MCP Server Scan — July 12, 2026

**Source:** mcp.so/feed (curl extraction — SPA text parsing)
**Date:** July 12, 2026
**Previous scan:** July 4, 2026 (evening)
**GitHub API:** Unavailable (search rate-limited — "User flagged as spammy")
**mcpservers.org:** Unavailable (SolidJS SPA, no server data in initial HTML)

## Methodology

mcp.so changed its frontend from Next.js RSC payloads (`__next_f.push`) to a fully client-rendered React SPA. Raw HTML extraction of the `/feed` page via text stripping was used. The feed contains the ~30 most recent submissions. No pagination was available.

## New Servers Found: 28 total, 14 business-relevant

### Category: Content & Marketing

| Server | Description | Guide |
|--------|-------------|-------|
| **Substack Publisher MCP** ★ | Queries Substack posts, engagement analytics, subscriber counts through Publisher API | [Guide](/hermes/mcp/servers/external/substack-publisher-mcp/) |
| **Prompt Improver MCP** | Turns rough requests into Role/Task/Context/Format prompts. Thai + English. | INDEX-ONLY |

### Category: Financial Data

| Server | Description | Guide |
|--------|-------------|-------|
| **Financial News MCP** ★ | Real-time financial news: search by ticker, source, language, with sentiment and entity data | [Guide](/hermes/mcp/servers/external/financial-news-mcp/) |
| **Seiche** ★ | Free open source funding stress terminal for US money markets. 22 engines, backtests. Fed/NY Fed/OFR/Treasury public APIs. | [Guide](/hermes/mcp/servers/external/seiche-finance-mcp/) |

### Category: Security & Infrastructure

| Server | Description | Guide |
|--------|-------------|-------|
| **shieldly-io** ★ | AI-Powered Security Analysis for AWS — IAM policies and CloudFormation templates | [Guide](/hermes/mcp/servers/external/shieldly-aws-mcp/) |
| **Agent Coherence** ★ | Stop AI agents from silently overwriting shared files — TLA+-verified coherence guard | [Guide](/hermes/mcp/servers/external/agent-coherence-mcp/) |

### Category: Research & Search

| Server | Description | Guide |
|--------|-------------|-------|
| **CrustAPI MCP** ★ | Live Google Search, Maps, News, Images and Reviews. Pay only for results. | [Guide](/hermes/mcp/servers/external/crustapi-mcp/) |

### Category: Compliance & Legal

| Server | Description | Guide |
|--------|-------------|-------|
| **EU Textile Sustainability MCP** | Free search engine for EU textile sustainability law (ESPR, DPP, CSRD, CBAM, CWA 18291) | INDEX-ONLY |

### Category: Development & Operations

| Server | Description | Guide |
|--------|-------------|-------|
| **Selenium MCP** | 39 browser automation tools with page snapshots, multi-session, batched execution | INDEX-ONLY |
| **E2LLM / SiFR Browser MCP** | Structured perception (SiFR) + browser action for AI agents | INDEX-ONLY |
| **MCP Time Server** | Zero-dependency clock + drift guard for Claude Desktop/Code/claude.ai | INDEX-ONLY |

### Category: Product & Business Intelligence

| Server | Description | Guide |
|--------|-------------|-------|
| **HelpScout-ProductLift Triangulator** | Triangulates HelpScout tickets + ProductLift feature requests into prioritized product plans | INDEX-ONLY |
| **BreckenWander Travel** | Keyless travel MCP connector — search flights, hotels at all-in prices | INDEX-ONLY |
| **deman-maker MCP Marketplace** | MCP marketplace — connect to everything in one click | INDEX-ONLY |

### Skipped (not business-relevant)
- Jmpy Mcp Server (no description)
- Computer Use Omni (Windows desktop automation — dev tool)
- YouTube Runbook MCP (video-to-runbook — niche)
- VeraData (Latin American data — niche, crypto paywall)
- 1C MCP Metacode (Russian enterprise config — niche)
- HPT.SU MCP Server (no description)
- BananaBanana Media MCP (image/video gen — commodity)
- Similarity Search API SDK (FORGE-generated — low quality)
- BuyWhere Product Price SDK (Singapore-specific)

## Trends

1. **Financial data MCPs accelerating:** Seiche (money markets) + Financial News MCP (real-time ticker/sentiment) — operators increasingly want live financial context for agents
2. **Compliance MCPs emerging:** EU Textile Sustainability Law MCP targets a specific regulation (ESPR/DPP/CSRD) — pattern of regulation-specific MCP servers
3. **Agent governance maturing:** Agent Coherence (file conflict prevention, TLA+-verified) + Human-in-the-loop approval — operators need infrastructure to manage multi-agent systems
4. **"Live search" becoming a category:** CrustAPI joins existing search MCPs with a pay-per-result model — competition in the agent-search space

## Actions Taken

1. Created 6 integration guides for highest-value servers
2. Updated `index.md` with entries for all 14 business-relevant servers
3. Cross-referenced all servers against existing catalog (47+ guides)

## GitHub API Note

GitHub search API returned "User flagged as spammy" for all queries. Token at `secrets/github.token` may need rotation. All discovery was via mcp.so/feed only.
