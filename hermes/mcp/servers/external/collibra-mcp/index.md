---
title: Collibra MCP Server
subtitle: Enterprise Data Governance through MCP
source: mcp-collibra
github: https://github.com/rajivdatta/mcp-collibra
created: 2026-07-22
category: Data Governance
stars: 0
tags: [collibra, data-governance, enterprise, metadata, power-bi]
---

# Collibra MCP Server

MCP server for the **Collibra Core REST API 2.0**. Enables AI agents to read and write Collibra assets, attributes, and relations — bringing enterprise data governance into the MCP ecosystem. Pairs with Power BI MCP servers to push semantic model lineage data.

## What It Does

Collibra is the dominant enterprise data governance platform (used by 550+ Fortune 500 companies). This MCP server wraps the Collibra Core REST API 2.0, giving AI agents:

- **Asset Discovery** — Search and read Collibra assets (tables, columns, reports, glossaries)
- **Attribute Management** — Read/write asset attributes for metadata enrichment
- **Relation Traversal** — Navigate asset relationships (lineage, composition, association)
- **Semantic Lineage** — Pair with Power BI MCP to push model-to-report lineage

## Business Operator Use Cases

| Use Case | Value |
|----------|-------|
| **Data Catalog Search** | "Find all tables containing PII data" → instant asset list with attributes |
| **Impact Analysis** | "What reports would break if we rename this column?" → upstream/downstream traversal |
| **Compliance Audit** | "Show me all assets without data classification tags" → gap analysis |
| **Power BI Integration** | Push semantic model lineage from Power BI to Collibra automatically |

## Installation

```bash
# Clone + install
git clone https://github.com/rajivdatta/mcp-collibra
cd mcp-collibra
npm install
```

## Configuration

Add to your MCP client config:

```json
{
  "mcpServers": {
    "collibra": {
      "command": "node",
      "args": ["path/to/mcp-collibra/index.js"],
      "env": {
        "COLLIBRA_BASE_URL": "https://your-instance.collibra.com",
        "COLLIBRA_USERNAME": "your-username",
        "COLLIBRA_PASSWORD": "your-password"
      }
    }
  }
}
```

## Auth

Collibra Core REST API 2.0 uses basic auth (username/password). The MCP server reads credentials from environment variables.

## Tools Provided

- `search_assets` — Full-text search across Collibra assets
- `get_asset` — Retrieve asset details by ID
- `get_attributes` — Read attributes for an asset
- `set_attribute` — Write/update an attribute value
- `get_relations` — Navigate asset relationships
- `create_relation` — Create new asset relationships

## Limitations

- **0 stars, brand new** — Created July 22, 2026. Unproven in production.
- **Basic auth only** — No OAuth or SSO support yet.
- **Collibra license required** — You need a Collibra instance. Not free.
- **No pagination** — Large catalogs may hit API limits.

## Operator Verdict

★★★ **High potential, early stage.** Collibra is the enterprise standard for data governance. This MCP server opens the door for AI agents to participate in metadata management workflows. If you run Collibra, this is a 15-minute setup with meaningful ROI. Wait for >50 stars or first release tag before production use.
