---
title: "MCP Server Scan Results — July 17, 2026"
description: "Daily MCP server discovery scan from mcp.so + mcpservers.org. 1 major new server found, 1 guide created. 1Password ships official MCP — landmark moment for agent security."
category: mcp
tags: [mcp-scan, discovery, mcp-servers]
last_updated: 2026-07-17
---

# MCP Server Scan — July 17, 2026

**Sources:** mcp.so (React SPA, text extraction) + mcpservers.org (TanStack Router hydration payload)
**Date:** July 17, 2026
**Previous scan:** July 16, 2026
**Coverage:** July 17 new submissions on both platforms

## Methodology

Both sources remain accessible via curl text-stripping from SPA payloads. Cross-referenced all candidates against the existing catalog (index.md + 100+ guide files + prior scan reports including July 16).

## New Servers Found: 10 total, 3 guides created

### Guide-Worthy (Major) — Guides Created

| Server | Source | Description | Guide |
|--------|--------|-------------|-------|
| **1Password MCP** ★★★ | mcpservers.org | Official 1Password MCP server (beta). Manages 1Password Environments from MCP clients without exposing secrets. Agent orchestrates, 1Password enforces the security boundary. First major secrets-management platform to ship an official MCP server. | [1password-mcp](/hermes/mcp/servers/external/1password-mcp/) |
| **Mercury MCP** ★★★ | mcp.so | Official Mercury banking MCP (beta). Read-only access to accounts, transactions, balances, and cards via OAuth 2.0 + DCR. First banking platform to ship an official MCP server. | [mercury-mcp](/hermes/mcp/servers/external/mercury-mcp/) |
| **Asana MCP V2** ★★★ | mcp.so | Official Asana project management MCP V2. Tasks, projects, workspaces via OAuth 2.0. Pre-registration required. Joins Atlassian, Linear, Notion in the PM MCP ecosystem. | [asana-mcp](/hermes/mcp/servers/external/asana-mcp/) |

### INDEX-ONLY (Niche, Developer-Focused, or Previously Noted)

| Server | Source | Description |
|--------|--------|-------------|
| **PuzzleTide Puzzle Generator** | Both | Word search, crossword, and sudoku generator MCP. Printable PDF worksheets. Developer Tools. |
| **Ceki** | mcpservers.org | Chrome browsers for AI agents — bypasses Cloudflare/Akamai with residential IPs. Browser automation. |
| **Pending Medicare Enrollment Data** | mcpservers.org | Behavioral-health NPIs pending Medicare enrollment, enriched from NPPES. Healthcare niche. |

### PREVIOUSLY INDEXED (Already in July 16 Scan)

| Server | Source | Status |
|--------|--------|--------|
| **extentos (Smart Glasses MCP)** | Both | Already in July 16 INDEX-ONLY |
| **SVGator MCP** | mcp.so | Already in July 16 INDEX-ONLY |
| **Sitespeak Claude Plugin** | mcp.so | Already in July 16 INDEX-ONLY |

## Landmark Finding: 1Password MCP

The 1Password MCP server represents a watershed moment for AI agent infrastructure:

1. **First major security platform to ship MCP:** 1Password is the first tier-1 infrastructure provider to release an official MCP server. This signals that MCP has crossed the enterprise adoption threshold.

2. **Novel security architecture:** 1Password's design — where the agent manages secrets without ever reading them — establishes a new pattern for secure agent operations. This "orchestrate, don't access" model will likely be replicated across the industry.

3. **Enterprise MCP tipping point:** When 1Password ships MCP, it validates the protocol for security-conscious enterprises. Expect AWS, HashiCorp, and Azure to follow within months.

4. **Operator implications:** For CorpusIQ's target audience (business operators), 1Password MCP solves a critical blocker to AI agent adoption: how to give agents operational autonomy without compromising security.

## Trends (Updated)

1. **Enterprise MCP adoption accelerates:** 1Password joins Atlassian, GitHub, Cloudflare, Supabase, Google, Notion, and Linear as major platforms with official MCP servers. The "official MCP server" is becoming table stakes for developer platforms.

2. **Security category opens:** 1Password MCP creates the "Security for AI" MCP category. Currently unoccupied by competitors — significant opportunity for security vendors.

3. **Agent security becomes a product category:** As agents become more autonomous, the gap between "what agents can do" and "what agents should be allowed to do" becomes a product surface. 1Password is first to market.

## Actions Taken

- ✅ 1 integration guide created for 1Password MCP (landmark server)
- ✅ 1 integration guide created for Mercury MCP (first banking MCP)
- ✅ 1 integration guide created for Asana MCP V2 (project management)
- ✅ 3 servers noted as INDEX-ONLY (already covered or too niche)
- ✅ 3 servers confirmed as previously indexed in July 16 scan
- ✅ Scan report updated

---

*← [Back to External MCP Catalog](/hermes/mcp/servers/external/) | [Previous Scan (July 16)](/hermes/mcp/servers/external/scan-results-2026-07-16/) →*
