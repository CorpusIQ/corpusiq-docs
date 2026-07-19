---
title: "endoflife.ai MCP — Integration Guide"
description: "Connect AI agents to endoflife.ai for software end-of-life intelligence — EOL dates, support status, and CVE risk scores across 485+ tracked products."
category: mcp
tags: [mcp-server, devops, security, eol, risk-management]
last_updated: 2026-07-19
---

# endoflife.ai MCP — Integration Guide

**Source:** mcp.so (remote MCP server, verified)  
**Author:** endoflife-ai  
**Transport:** Remote MCP (Streamable HTTP)  
**Auth:** None required (free, no signup)  
**Website:** [endoflife.ai](https://endoflife.ai)

## What It Does

endoflife.ai is the authoritative EOL (end-of-life) database for software. The MCP server exposes EOL dates, support status, and the 0-100 **EOL Risk Score** across **485+ tracked products and 8,000+ versions** — Node.js, Python, PHP, RHEL, Ubuntu, Java, Kubernetes, and more. Updated daily. Free, no signup.

AI agents can:
- Check a single version's EOL date and support status
- Pull a product's full lifecycle schedule
- Assess EOL risk across an entire tech stack
- Get upgrade path recommendations before security patches stop

Think of it as "software dependency health monitoring" — operators can ask their AI assistant "what in our stack is going EOL this quarter?" and get an immediate, sourced answer.

## Why This Matters for Operators

1. **Operational risk management:** Running EOL software means no security patches. For business operators managing web applications, APIs, or infrastructure, knowing when dependencies go EOL is critical.

2. **Compliance readiness:** SOC 2, ISO 27001, and other frameworks require running supported software. endoflife.ai provides auditable evidence.

3. **Upgrade planning:** Instead of manually checking EOL dates across dozens of dependencies, operators ask one question and get a full stack assessment.

4. **Zero-cost, zero-config:** Remote MCP, no API key, instant queries. Operators can assess their stack risk in one conversation.

## Setup

### Prerequisites

- An MCP-compatible client (Claude, ChatGPT, Cursor, Hermes, etc.)
- No API key or signup required

### MCP Client Configuration

Add this to your MCP client's server configuration:

```json
{
  "mcpServers": {
    "endoflife": {
      "type": "http",
      "url": "https://mcp.endoflife.ai"
    }
  }
}
```

For Claude Code:
```bash
claude mcp add endoflife https://mcp.endoflife.ai
```

For Hermes Agent (config.yaml):
```yaml
mcp_servers:
  endoflife:
    transport: http
    url: https://mcp.endoflife.ai
```

### Usage

Once connected, ask your AI assistant:

- *"What versions of Node.js are still supported?"*
- *"Check our stack for EOL risks — we run Python 3.8, PostgreSQL 12, and Ubuntu 20.04"*
- *"When does Kubernetes 1.27 go end-of-life?"*
- *"What should we upgrade before Q4? List all EOL dates for our dependencies."*
- *"Give me an EOL risk score for our infrastructure stack."*

## Tools

The MCP server exposes these primary capabilities:

| Tool | Description |
|------|-------------|
| **Check Version** | Look up EOL date and support status for a specific product + version |
| **Product Lifecycle** | Pull the full lifecycle schedule (release, active support, security support, EOL) for a product |
| **EOL Risk Score** | 0-100 score indicating how close a version is to EOL |
| **Stack Audit** | Bulk-check multiple products/versions in one call |
| **Upgrade Path** | Recommended upgrade target for EOL versions |

## Operator Use Cases

### DevOps / Infrastructure Operators
"Before our SOC 2 audit next month, check every service in our docker-compose for EOL runtimes."

### CTOs / Engineering Leaders
"What's going EOL in our stack this quarter? Prioritize the list by risk score and give me upgrade timelines."

### Agency Operators
"Audit all our client projects for EOL dependencies. Flag anything going EOL within 6 months."

### Security Operators
"Cross-reference our dependency list against known CVEs on EOL versions."

## Status

- **Listed on mcp.so:** July 19, 2026 (verified, featured)
- **Category:** Developer Tools
- **Transport:** Remote MCP (no local install)
- **Auth:** None (free, no signup)
- **Data freshness:** Updated daily

## See Also

- [[vibgrate-mcp/index]] — Dependency drift and CVE scanning MCP
- [[docker-mcp/index]] — Docker container management
- [[shieldly-aws-mcp]] — AWS security analysis MCP
- [endoflife.ai website](https://endoflife.ai) — Full product database

---

*Discovered during [July 19, 2026 MCP scan](/hermes/mcp/servers/external/scan-results-2026-07-19/). Added to catalog same day.*
