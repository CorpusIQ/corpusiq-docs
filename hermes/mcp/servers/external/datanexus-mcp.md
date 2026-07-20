---
title: "DataNexus MCP — Public Data Intelligence (55 Tools)"
description: "DataNexus MCP server provides 55 tools for verified public data — CVE vulnerabilities, patents, federal contracts, NPI provider data, nonprofits, and domain intelligence. 8,000+ calls on Smithery. Live at datanexusmcp.com."
category: mcp
tags: [mcp-server, data-intelligence, public-data, cve, patents, federal-contracts, open-data]
last_updated: 2026-07-19
---

# DataNexus MCP Server — Public Data Intelligence

DataNexus MCP is a public data intelligence server with 55 tools spanning CVE security vulnerabilities, patent databases, federal contracts, NPI healthcare provider data, nonprofit registries, and domain intelligence. It's live at datanexusmcp.com with over 8,000 calls on Smithery and listed on Glama.

**Source:** awesome-mcp-servers PR #9117 (discovered July 19, 2026)
**Category:** Data Intelligence / Research
**Author:** DataNexus
**Website:** https://datanexusmcp.com
**Smithery:** Listed, 8,000+ calls
**Status:** Active, verified on Smithery

## Why This Matters for Operators

Operators making business decisions need external intelligence — Is a vendor vulnerable to a known CVE? Has a competitor filed new patents? Are there federal contracts in our space? Who are the key nonprofits in our market? DataNexus answers all of these from a single MCP server with verified, structured data. No more cobbling together 5 different APIs.

## Installation

```bash
# Via npm
npm install -g datanexus-mcp

# Or run directly
npx datanexus-mcp
```

## Claude Desktop / Hermes Configuration

```json
{
  "mcpServers": {
    "datanexus": {
      "command": "npx",
      "args": ["datanexus-mcp"],
      "env": {
        "DATANEXUS_API_KEY": "your-api-key"
      }
    }
  }
}
```

## Tool Categories (55 Tools Total)

| Category | Tools | Use Case |
|----------|-------|----------|
| CVE / Vulnerabilities | 10+ | Vendor security audits, supply chain risk |
| Patents | 10+ | Competitive intelligence, IP landscape |
| Federal Contracts | 10+ | Government sales opportunities |
| NPI Provider Data | 8+ | Healthcare market analysis |
| Nonprofits | 8+ | Partnership discovery, grant research |
| Domain Intelligence | 5+ | WHOIS, DNS, domain reputation |

## Authentication

Requires a DataNexus API key. Sign up at [datanexusmcp.com](https://datanexusmcp.com). Free tier available.

## CorpusIQ Angle

DataNexus's public data tools complement CorpusIQ's private business data connectors (QuickBooks, Shopify, Stripe). Together they form a complete business intelligence layer: private financials via CorpusIQ + public market intelligence via DataNexus. Patent and federal contract data could specifically fuel lead intelligence for B2B operators.

## See Also

- [[sweeps/sweep-july19-2026]]
- [[fastcrw]]
