---
title: "MCP Server Scan Results — July 13, 2026"
description: "Daily MCP server discovery scan from mcp.so/feed. 7 new servers found today (all from July 13)."
category: mcp
tags: [mcp-scan, discovery, mcp-servers]
last_updated: 2026-07-13
---

# MCP Server Scan — July 13, 2026

**Source:** mcp.so (curl extraction — SPA inline JSON parsing)
**Date:** July 13, 2026
**Previous scan:** July 12, 2026
**GitHub API:** Unavailable (rate-limited as of July 12)
**mcpservers.org:** Unavailable (SolidJS SPA, no server data in initial HTML)

## Methodology

mcp.so frontend loads all server data as inline JSON in the initial HTML payload (`$R` references in the TanStack Router hydration script). Server entries were extracted by parsing the `createdAt` fields and filtering for today's date (July 13, 2026).

## New Servers Found: 7 total, 4 business-relevant

### Category: AI & Agents

| Server | Description | Guide |
|--------|-------------|-------|
| **AI Localization Agent** ★ | Stop wasting AI tokens on localization. By l10n.dev. 3 GitHub stars. | [Guide](/hermes/mcp/servers/external/ai-localization-agent/) |
| **HTML Pub** ★ | Publish AI-generated HTML to a live page on your own domain. Remote server by Leadpages. MCP-native content publishing. | [Guide](/hermes/mcp/servers/external/htmlpub-mcp/) |
| **Horizon AI Intelligence** ★ | Free AI-industry intelligence for agents: briefings, regulation tracker & regional lenses. By system-alchemist. | [Guide](/hermes/mcp/servers/external/horizon-mcp/) |
| **AppAmbit MCP** ★ | All-in-one platform for mobile app analytics, crash reporting, build distribution, managed databases, serverless functions, and CMS. 10 GitHub stars. | [Guide](/hermes/mcp/servers/external/appambit-mcp/) |

### Category: Developer Tools

| Server | Description | Guide |
|--------|-------------|-------|
| **Bothread** | Local room where AI coding agents collaborate on one codebase via MCP — collisions prevented, human in command. By AdamACE9. | INDEX-ONLY |
| **ResolveMesh Compatibility Intelligence** | Hosted ResolveMesh compatibility MCP server — read-only, source-backed compatibility lookups for AI agents. By mo-sharif. | INDEX-ONLY |

### Category: Finance & Commerce

| Server | Description | Guide |
|--------|-------------|-------|
| **Toolzy** | French tool rental marketplace — search and rent tools between individuals. By Toolzy-2. Niche regional. | INDEX-ONLY |

## Skipped

None — all 7 servers documented. Bothread and ResolveMesh are developer-tool focused; Toolzy is a French-only regional marketplace.

## Trends

1. **Content publishing via MCP emerging:** HTML Pub by Leadpages is notable — a major SaaS company (Leadpages) shipping an MCP server for AI-generated content publishing. Signals that established martech companies see MCP as a distribution channel.
2. **Localization as an MCP category:** AI Localization Agent targets the growing problem of AI token waste in localization workflows. First dedicated localization MCP.
3. **Mobile app ecosystem MCP:** AppAmbit brings the full mobile dev lifecycle (analytics, crash reporting, build distribution, CMS) into MCP — first comprehensive mobile-dev MCP server.
4. **AI industry intelligence:** Horizon provides free AI regulation tracking and regional briefings — fills a gap for operators who need to track AI policy changes.

## Actions Taken

1. Created 4 integration guides for highest-value servers: AI Localization Agent, HTML Pub, Horizon AI Intelligence, AppAmbit MCP
2. Updated `index.md` with entries for all 7 servers
3. Push to `https://github.com/CorpusIQ/corpusiq-docs` (main)
