---
title: "MCP Server Scan — July 17, 2026 (Evening Supplement)"
description: "Late-evening MCP server discoveries from mcpservers.org. 8 new servers found, 2 major: Official Trello MCP (Atlassian) and Nexly Analytics MCP."
category: mcp
tags: [mcp-scan, discovery, mcp-servers, evening-scan]
last_updated: 2026-07-17
---

# MCP Server Scan — July 17, 2026 (Evening Supplement)

**Source:** mcpservers.org (TanStack Router hydration payload, late evening update)
**Date:** July 17, 2026 (evening batch, ~22:07 UTC)
**Previous scan:** July 17, 2026 (morning)
**Coverage:** 8 new servers added to mcpservers.org in the late evening hours

## Methodology

The mcpservers.org payload was re-fetched in the evening and cross-referenced against the morning scan results and the existing catalog. All 8 candidates are net-new — none were in the morning scan or any prior scan report.

## New Servers Found: 8 total, 2 guides created

### Guide-Worthy (Business-Relevant) — Guides Created

| Server | Source | Description | Guide |
|--------|--------|-------------|-------|
| **Trello MCP Server** ★★★ | mcpservers.org | **Official Atlassian Trello MCP server.** Cloud-hosted bridge for AI tools to access boards, lists, cards, checklists. OAuth 2.0. Streamable HTTP at `https://mcp.trello.com/v1`. Apache 2.0 license. First official Trello MCP — joins Atlassian's existing Jira/Confluence MCP. | [trello-mcp](/hermes/mcp/servers/external/trello-mcp/) |
| **Nexly Analytics MCP** ★★ | mcpservers.org | Read-only product analytics via MCP — traffic, acquisition, custom events, funnels, reports, anomalies, AI-traffic insights. OAuth 2.0. Endpoint: `https://api.nexly.to/mcp`. Supports Claude, Cursor, Codex. | [nexly-mcp](/hermes/mcp/servers/external/nexly-mcp/) |

### INDEX-ONLY (Niche, Developer-Focused, or Specialized)

| Server | Source | Description |
|--------|--------|-------------|
| **Lians Agent Memory** | mcpservers.org | Bitemporal agent memory with point-in-time retrieval, supersession, audit trails, regulated-memory controls. GitHub: Lians-ai/Lians. |
| **Tasklix** | mcpservers.org | Agent-first collaborative project board with MCP server for coordinating agent fleets and humans on shared tasks. |
| **Flowvenue** | mcpservers.org | Governed, deterministic business processes from ChatGPT, Claude, and other AI assistants. |
| **Tischanruf** | mcpservers.org | AI voice agent that books real restaurant tables — even at restaurants that only take phone reservations. |
| **AI Agent Tokenized Stock OS (AATOS)** | mcpservers.org | Non-custodial MCP for AI agents on Robinhood Chain (4663): Stock Tokens, multi-venue quotes, Morpho Earn. |
| **RabbitMQ Connector (data-connectors-ai)** | mcpservers.org | MCP server for RabbitMQ: publish messages, poll from durable quorum queue. Developer infrastructure. |

## Key Finding: Trello MCP Joins Atlassian's MCP Suite

Atlassian continues to expand its official MCP server lineup. After shipping the Jira/Confluence MCP server, they've now released an official Trello MCP server — a cloud-hosted bridge that gives AI tools secure, real-time access to Trello boards, lists, cards, and checklists.

**Significance:**

1. **Atlassian MCP strategy becomes clear:** Atlassian is now shipping official MCP servers for Jira, Confluence, AND Trello — covering the entire project management spectrum from engineering (Jira) to documentation (Confluence) to lightweight task management (Trello).

2. **Operator relevance:** Trello is widely used by business operators, marketing teams, and non-engineering departments. An official Trello MCP makes AI agents useful for the exact audience CorpusIQ targets.

3. **Security model:** OAuth 2.0, workspace-scoped access, no destructive delete operations (archive only). This is enterprise-ready from day one.

4. **Multi-platform:** Supports Claude, ChatGPT, Cursor, VS Code, and Gemini CLI out of the box.

## Key Finding: Nexly Analytics Fills the Analytics MCP Gap

Nexly provides product and web analytics via MCP — a category that's been underserved by official MCP servers. While Google Analytics has community MCP servers, Nexly offers a hosted, OAuth-secured, read-only analytics endpoint designed for AI agents.

**Use cases for operators:**
- Ask AI assistants about traffic trends without logging into dashboards
- Pull funnel conversion data into planning conversations
- Monitor anomalies and AI-traffic insights automatically

## Actions Taken

- ✅ 1 integration guide created for Trello MCP (Official Atlassian, major)
- ✅ 1 integration guide created for Nexly Analytics MCP (analytics, operator-relevant)
- ✅ 6 servers noted as INDEX-ONLY (niche or specialized)
- ✅ Evening supplement scan report created
- ✅ Cross-referenced against morning July 17 scan — all 8 are net-new

---

*← [Back to External MCP Catalog](/hermes/mcp/servers/external/) | [Morning Scan (July 17)](/hermes/mcp/servers/external/scan-results-2026-07-17/) →*
