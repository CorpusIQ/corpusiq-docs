---
title: "MCP Server Scan Supplement — July 18, 2026 (Evening)"
description: "Evening supplement to the daily MCP server discovery scan. 4 new integration guides created: SocialBu (social media management), Velarion (executive compensation), Backengine (customer context), Docker MCP (container management)."
category: mcp
tags: [mcp-scan, discovery, mcp-servers]
last_updated: 2026-07-18
---

# MCP Server Scan Supplement — July 18, 2026 (Evening)

**Source:** mcp.so feed (123KB, 30 servers listed)
**Date:** July 18, 2026 (evening sweep)
**Morning scan:** [scan-results-2026-07-18.md](/hermes/mcp/servers/external/scan-results-2026-07-18/)
**GitHub API:** Broken (search returns 0 results — "spammy" flag, tracked issue)

## Methodology

Firecrawl/web_extract unavailable on this node. Used direct curl to mcp.so/feed (123KB response) — extracted server names and descriptions from h3 blocks. Cross-referenced all 30 candidates against existing catalog (index.md + 140+ guide files). GitHub API search non-functional (returns 0 results regardless of query, likely "spammy" flag). Individual repo lookups via unauthenticated API calls.

## New Guides Created: 4

| Server | Source | Stars | Description | Guide |
|--------|--------|-------|-------------|-------|
| **SocialBu MCP** ★★ | mcp.so | 0 | Social media management for AI agents — connect Claude, ChatGPT, Cursor, Hermes to SocialBu. Post, schedule, analyze across all platforms. | [socialbu-mcp](/hermes/mcp/servers/external/socialbu-mcp/) |
| **Velarion MCP** ★★ | mcp.so | 0 | Executive compensation & governance intelligence for ~3,000 US public companies. SEC-sourced, deterministic. 8 tools. | [velarion-mcp](/hermes/mcp/servers/external/velarion-mcp/) |
| **Backengine MCP** ★★ | mcp.so | 1 | Customer context layer for revenue teams — query Slack, email, call transcripts, support tickets from MCP clients. | [backengine-mcp](/hermes/mcp/servers/external/backengine-mcp/) |
| **Docker MCP Server** ★★★ | mcp.so | 494 | Complete Docker management — containers, images, networks, volumes, Swarm services. Production-hardened, MIT licensed. | [docker-mcp](/hermes/mcp/servers/external/docker-mcp/) |

## Index-Only (New Servers Without Guides)

| Server | Description |
|--------|-------------|
| Banks to AI | 12,000+ financial institutions, read-only bank data. upx.com. No GitHub repo found. |
| Synci | Bank/brokerage/crypto read-only access via MCP. No GitHub repo found. Niche. |
| Shippo MCP | Shipping/logistics wrapper for Hal (Retell admin agent). Wrapper, not primary. edoswald/shippo-mcp-wrapper. |
| Cosmik MCP | Space data: rocket launches, ISS passes, launch news. crashedfox/cosmik-mcp. Niche. |
| PuzzleTide | Word search, crossword, sudoku generator. Caravaca-Labs. Not operator-relevant. |
| PoYo.ai | API key aggregator for 500+ AI models. poyo.ai. Not operator-relevant. |
| Pending Medicare | CMS behavioral health enrollment data. unitedideas. Healthcare niche. |
| extentos | Smart glasses dev platform. Niche. Already noted in prior scans. |
| APIMart | API marketplace. apimart.ai. Already noted in prior scans. |
| Sitespeak | Claude Plugin for sitespeakai. Already noted in prior scans. |
| Gocosmik | Space data (same as Cosmik MCP). Already noted in prior scans. |
| SVGator | Design tool. Already noted in prior scans. |
| Savi Tools | AI Innovation Labs tools. Already noted in prior scans. |
| CKG - AgentForce | Healthcare knowledge graph. GraphifyMD.com. Niche. |
| Charming | tambo-labs. Unknown capability. |

## Trends (Evening Sweep)

1. **Social media MCPs multiplying**: SocialBu joins OpenTweet as the second social media management MCP server. Social media operators now have MCP-native alternatives to dashboard-based tools.

2. **Financial governance emerges**: Velarion opens a new MCP subcategory — corporate governance data. Following Mercury MCP (banking) and Alpha Vantage (market data), the financial MCP ecosystem now spans banking, markets, and governance.

3. **Revenue operations goes MCP**: Backengine represents the first MCP server purpose-built for revenue team workflows. Customer context — previously scattered across Slack, email, and support tools — is now queryable through AI conversation.

4. **Infrastructure MCP matures**: Docker MCP at 494 stars demonstrates that infrastructure management is one of the most mature MCP categories. Kubernetes MCP (1,814★) and Devopness MCP (434★) round out a production-ready DevOps MCP stack.

## Actions Taken

- ✅ 4 integration guides created (SocialBu, Velarion, Backengine, Docker MCP)
- ✅ 15 servers noted as INDEX-ONLY
- ✅ Index entries added to all relevant sections
- ✅ Index last_updated timestamp updated to evening supplement
- ✅ Scan supplement report created
- ⏳ Push to GitHub pending

---

*← [Back to MCP Scan Reports](/hermes/mcp/servers/external/) | [Morning Scan (July 18)](/hermes/mcp/servers/external/scan-results-2026-07-18/) →*
