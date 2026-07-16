---
title: "MCP Server Scan — July 16, 2026"
description: "Automated scan of mcpservers.org (sitemap). 7 new servers found, 4 business-relevant guides created."
category: mcp
tags: [mcp-scan, discovery, mcp-servers]
last_updated: 2026-07-16
---

# MCP Server Scan — July 16, 2026

**Sources:** mcpservers.org (sitemap extraction)
**Date:** July 16, 2026
**Previous scan:** July 15, 2026 (evening supplement — 7 servers from mcp.so)

## Methodology

mcpservers.org sitemap extraction — filtered for servers with `lastmod >= 2026-07-16` across all 5 sitemap files. mcp.so is JS-rendered (SolidJS) in cron environment and was not scanned this cycle (deferred until Firecrawl/Playwright available in cron).

## New Since July 15 Evening Scan: 7 servers, 4 guides created

### Guide-Worthy (Business-Relevant)

| Server | Source | Stars | Description | Guide |
|--------|--------|-------|-------------|-------|
| **Kubernetes MCP Server** ★ | mcpservers.org | 1,814★ | MCP server for Kubernetes and OpenShift. Native binary, npm/Python/Docker. Manage clusters, pods, deployments, configs via MCP. | [Guide](/hermes/mcp/servers/external/kubernetes-mcp-server/) |
| **Devopness** ★ | mcpservers.org | 434★ | AI DevOps on your cloud. Deploy apps, infra and CI/CD. Any cloud/stack, one MCP. Deterministic API. No cloud credentials in AI chats. Free plan. | [Guide](/hermes/mcp/servers/external/devopness-mcp/) |
| **Superserve** ★ | mcpservers.org | 413★ | Sandbox infrastructure for AI Agents — create and control isolated cloud sandboxes via MCP. | [Guide](/hermes/mcp/servers/external/superserve-mcp/) |
| **Agent360 Browser MCP** ★ | mcpservers.org | 22★ | Drive real logged-in Chrome from AI agents. Reads emailed login codes from Gmail, solves CAPTCHAs, 34 tools. MIT, local-only. Works where headless dies. | [Guide](/hermes/mcp/servers/external/browser-mcp-agent360/) |

### INDEX-ONLY (Niche or Developer-Focused)

| Server | Source | Description |
|--------|--------|-------------|
| **Google GenAI Toolbox** | mcpservers.org | Official Google MCP server for databases. Listed as "Official Toolbox For Databases MCP Server" on mcpservers.org. GitHub repo not publicly verifiable — may be internal or upcoming release. |
| **Semiotic** | mcpservers.org | React data visualization library (2,685★). Charts, maps, network visualization. Developer library, not business-operator MCP. |
| **Quokkapix MCP** | mcpservers.org | Private browser image workflows for AI agents (0★). Local-first image processing. Very early stage, narrow scope. |

## Trends

1. **DevOps MCPs accelerating:** Kubernetes MCP (1,814★) and Devopness (434★) both appeared the same day — signaling DevOps/infrastructure automation as a maturing MCP category. These join the cloud sandbox MCP (Superserve) to form a cluster of infrastructure-as-tool for AI agents.

2. **Browser automation diversifying:** Agent360 Browser MCP (22★) takes a different approach from headless — real logged-in Chrome with Gmail OTP reading and CAPTCHA solving. Competitive to browser-use (97K★ Python library) but MCP-native.

3. **Google entering MCP ecosystem:** The Google GenAI Toolbox listing suggests Google is building official MCP servers. Even if the repo isn't public yet, the listing on mcpservers.org under `googleapis/` signals intent.

4. **Volume steady:** 7 new servers/day consistent with the ~10-15/day observed in prior scans (~9,800 total on mcpservers.org).

## Actions Taken

- 4 integration guides drafted for business-relevant servers
- 3 servers indexed (too niche or unverifiable for full guides)
- Scan methodology: mcpservers.org sitemap extraction, mcp.so deferred
- index.md updated with all new entries

---

*Next scan: July 17, 2026. Continue dual-source approach when mcp.so is scannable.*
