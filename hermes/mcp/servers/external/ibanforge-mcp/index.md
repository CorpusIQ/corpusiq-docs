---
title: IBANforge MCP Server
description: IBAN validation, BIC/SWIFT lookup, Swiss clearing, and EMI/vIBAN classification via MCP for AI agents
category: Finance
rating: ★★
source: mcp.so + GitHub
date: 2026-07-30
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/ibanforge-mcp/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

# IBANforge MCP Server

IBANforge brings banking validation and compliance tools to AI agents through MCP. Validate IBANs, look up BIC/SWIFT codes, check Swiss clearing numbers, and classify EMI/vIBAN accounts — all from any MCP-compatible client.

## What It Does

IBANforge exposes 6 tools for banking operations:

| Tool | Description |
|------|-------------|
| `validate-iban` | Validate IBAN format and checksum for 80+ countries |
| `lookup-swift` | Resolve BIC/SWIFT codes to bank details |
| `lookup-iban` | Reverse-lookup bank info from IBAN |
| `swiss-clearing` | Validate Swiss clearing numbers (BC-Nummer) |
| `classify-emi` | Classify EMI (Electronic Money Institution) accounts |
| `classify-viban` | Classify virtual IBAN accounts |

## Why Operators Need This

International payments fail constantly from bad bank details. IBANforge lets your AI agent catch validation errors before they become payment rejections. For e-commerce operators processing SEPA payments, fintech operators doing KYC/compliance, or accounting teams reconciling international transactions, this eliminates a manual validation step that costs 2-5 minutes per transaction.

## Quick Setup

**Transport:** Streamable HTTP (remote)
**Auth:** API key (free tier available)
**Endpoint:** `https://ibanforge.com/mcp`

### Claude Code

```bash
claude mcp add ibanforge https://ibanforge.com/mcp
```

### Cursor / VS Code

```json
{
  "mcpServers": {
    "ibanforge": {
      "url": "https://ibanforge.com/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

## Pricing

Free tier available with rate limits. Paid tiers for production volume. See [ibanforge.com](https://ibanforge.com) for current pricing.

## Repository

`github.com/cammac-creator/ibanforge` — 2⭐, TypeScript (Hono), SQLite-backed. Updated July 2026.

## See Also

- [[honest-vies-mcp]] — EU VAT number validation
- [[sanctions-screening-mcp]] — OFAC/EU/UK/UN sanctions screening
- [[stripe-mcp]] — Payment processing
