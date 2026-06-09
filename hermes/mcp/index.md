---
title: MCP Integration
description: Model Context Protocol guide for CorpusIQ Hermes agents. 54 connectors, authentication, tool discovery, server management.
---

# MCP Integration

Model Context Protocol connects Hermes agents to 54 SaaS tools, databases, and platforms through the CorpusIQ MCP server — the intelligence layer between Hermes and business systems.

## Community Hub

This is part of the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes) — the largest collection of Hermes resources on GitHub. 33 pages, 140+ tools, 158 skills.

## CorpusIQ + Hermes

CorpusIQ acts as the MCP connectivity layer for Hermes agents:

| Capability | What It Enables |
|-----------|----------------|
| **54 MCP Connectors** | GA4, Stripe, Shopify, QuickBooks, HubSpot, Klaviyo, Google Ads, Meta Ads, Ahrefs, Semrush, Gmail, Slack, Notion, and 40+ more |
| **Full Connector Catalog** | [Browse all 54 connectors →](/hermes/mcp/connectors/) |

## MCP Architecture

```text
Hermes Agent → MCP Client → CorpusIQ MCP Server → OAuth → SaaS APIs
                                     ↓
                            Tool Discovery (54 tools)
                                     ↓
                            Data Retrieval + Analysis
```

## Key Concepts

### Tool Discovery

When connected to CorpusIQ MCP, Hermes agents automatically discover available tools. The `get_connector_status` action shows every connector's auth state — green dot means ready, grey means needs OAuth.

### Single-Source vs Cross-Source

Questions fall into two categories:

1. **Single-source**: "Show my GA4 traffic this week" — goes directly to one connector
2. **Cross-source**: "How's business doing?" — the skills router dispatches a runbook that calls multiple connectors

### Skills Router

For broad business questions, the `select_runbook` action auto-classifies the intent and returns the best pre-built analysis runbook. The agent follows it step-by-step, calling the right connectors in sequence.

## Available Connectors

54 connectors across 11 categories. See the **[Connector Catalog](/hermes/mcp/connectors/)** for full details.

| Category | Count |
|----------|:----:|
| Marketing & Analytics | 9 |
| Email & Marketing Automation | 6 |
| CRM & Sales | 3 |
| Commerce & Payments | 7 |
| Communication & Collaboration | 5 |
| Email & Calendar | 4 |
| File Storage | 3 |
| Content & Social | 2 |
| Databases | 4 |
| Platform Management | 6 |
| Knowledge & Governance | 5 |

## Connecting New Sources

```bash
# Check what's available
hermes mcp corpusiq get_connector_status

# Follow the OAuth link for any grey-dot connector
# Green dot = authenticated and ready
```

---

## External MCP Resources

- [MCP Hub](https://mcp.so) — community MCP server directory
- [mcpservers.org](https://mcpservers.org) — MCP server catalog
- [modelcontextprotocol.io](https://modelcontextprotocol.io) — protocol specification
- [FastMCP](https://github.com/jlowin/fastmcp) — Python MCP framework

---

*← [Skills](/hermes/skills/) | [Connector Catalog](/hermes/mcp/connectors/) → | ↑ [Home](/hermes/)*
