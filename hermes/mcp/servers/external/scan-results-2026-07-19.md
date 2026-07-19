---
title: "MCP Server Scan — July 19, 2026"
description: "Daily MCP server discovery scan. 1 integration guide created: endoflife.ai (EOL intelligence). 3 GitHub-origin servers noted for future tracking. mcpservers.org yielded no new additions beyond mcp.so feed."
category: mcp
tags: [mcp-scan, discovery, mcp-servers]
last_updated: 2026-07-19
---

# MCP Server Scan — July 19, 2026

**Sources:** mcp.so feed (6,457 servers), GitHub topic:mcp-server (created >2026-07-18), mcpservers.org (9,300+ servers)
**Date:** July 19, 2026
**Previous scan:** [Late Night Sweep (July 18)](/hermes/mcp/servers/external/scan-results-2026-07-18-late-night/)
**Coverage:** New submissions since July 18 late-night sweep

## Methodology

Web tools (Firecrawl) unavailable on this node. Used:
1. **mcp.so feed** — SPA hydration payload extracted via curl + regex; 6,457 servers in feed, sorted by submission date
2. **GitHub API** — Searched `topic:mcp-server created:>2026-07-18`; 11 repos found
3. **Cross-reference** — All candidates checked against existing catalog (index.md + 145+ guide files + all prior scan reports)

## New Guide Created: 1

| Server | Source | Description | Guide |
|--------|--------|-------------|-------|
| **endoflife.ai** ★★★ | mcp.so | Authoritative EOL database — end-of-life dates, CVE risk scores, and upgrade paths for 485+ products and 8,000+ versions (Node.js, Python, PHP, RHEL, Ubuntu, Java, Kubernetes, etc.). Remote MCP, free, no signup, updated daily. Submitted July 19, 10:52 AM by endoflife-ai. Verified + Featured. | [endoflife-mcp](/hermes/mcp/servers/external/endoflife-mcp/) |

## Index-Only (New Servers Without Guides)

| Server | Source | Description |
|--------|--------|-------------|
| **edi-mcp** | GitHub | MCP server for EDI — parse, validate, and acknowledge X12/EDIFACT documents. Supply chain operators. `github.com/heocoi/edi-mcp` ⭐0, created July 19. |
| **velocms-mcp** | GitHub | Blog/CMS publishing from Claude Code, Claude Desktop, or Cursor. `github.com/VeloCMS/velocms-mcp` ⭐0, created July 19. |
| **mcp-realbrowser** | GitHub | Connect AI agents to real Chrome via CDP — preserves logins, cookies, sessions. 9 tools. `github.com/obbbba/mcp-realbrowser` ⭐1, created July 19. |
| **openapi-mcp-gateway** | GitHub | Turn any OpenAPI spec into a remote MCP server over SSE. `github.com/notsariedo/openapi-mcp-gateway` ⭐0, created July 19. |
| **comidoc-mcp** | GitHub | Verified Udemy coupon and course data with live redemption. `github.com/Amorem/comidoc-mcp` ⭐0, created July 19. |
| **scern-mcp** | GitHub | US packaged food evaluation — health scores, ingredient safety, recall history. `github.com/elcoryel/scern-mcp` ⭐1, created July 19. |
| **lazy-media-mcp** | GitHub | Local media compression for AI vision agents. `github.com/leaf76/lazy-media-mcp` ⭐0, created July 19. |
| **provenio** | GitHub | Art provenance MCP — 282K-node knowledge graph. `github.com/mildo-ai/provenio` ⭐0, created July 19. |
| **iTechSmart UAIO MCP** | GitHub | ProofLink verification and autonomous IT operations. `github.com/iTechSmartINC/mcp-server` ⭐0, created July 19. |
| **kcs** | GitHub | Container controller (simpler k3s). `github.com/TitiSkywalker/kcs` ⭐0, created July 19. |
| **my-heb-proxy** | GitHub | H-E-B grocery app API proxy + MCP server. `github.com/ALLMarvelous/my-heb-proxy` ⭐0, created July 19. |

## Key Finding: EOL Intelligence — The Missing DevOps MCP

**endoflife.ai** fills a gap in the MCP ecosystem: software lifecycle intelligence. While the DevOps MCP stack is well-developed (Docker MCP at 494★, Kubernetes MCP at 1,814★, Shieldly AWS at growing stars), no existing MCP server provides EOL dates and risk scoring:

1. **Operational risk made conversational:** Instead of manually checking EOL dates across dozens of dependencies, operators ask one question and get a full stack assessment with risk scores.

2. **Compliance-ready:** SOC 2, ISO 27001, and other frameworks require running supported software. endoflife.ai provides auditable EOL evidence through AI conversation.

3. **Zero-friction adoption:** Remote MCP, free, no API key, updated daily. The lowest possible barrier for operators to start monitoring their stack's EOL risk.

4. **Complementary to Vibgrate MCP:** Vibgrate covers CVE scanning and dependency drift for your own codebases. endoflife.ai covers the underlying runtimes and platforms your code runs ON. Together they form a complete software health MCP stack.

## Trends

1. **DevOps MCP stack completes:** With endoflife.ai joining Docker MCP, Kubernetes MCP, Shieldly AWS, and Vibgrate MCP, the DevOps MCP ecosystem now covers containers, orchestration, security scanning, AND lifecycle management. Operators can manage their entire infrastructure from AI conversation.

2. **EDI enters MCP:** heocoi/edi-mcp is the first MCP server for Electronic Data Interchange (X12/EDIFACT). While brand new (0 stars), it signals that supply chain and B2B commerce workflows are entering the MCP ecosystem.

3. **CMS/blog MCP emerges:** VeloCMS MCP represents a new category — content management through MCP. Content operators can now publish and manage blogs from their AI assistant.

4. **Remote MCP remains dominant:** All mcp.so submissions this period are remote MCP servers. The zero-install, cloud-hosted pattern is now the default.

## Actions Taken

- ✅ 1 integration guide created (endoflife.ai)
- ✅ 11 servers noted as INDEX-ONLY
- ✅ Scan report created
- ⏳ Index entries to be added
- ⏳ Push to GitHub

---

*← [Back to External MCP Catalog](/hermes/mcp/servers/external/) | [Late Night Sweep (July 18)](/hermes/mcp/servers/external/scan-results-2026-07-18-late-night/) →*
