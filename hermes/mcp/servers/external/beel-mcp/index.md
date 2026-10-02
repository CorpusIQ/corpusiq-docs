---
title: "BeeL MCP - Spanish VeriFactu E-Invoicing Compliance"
description: "Official BeeL MCP server for Spanish electronic invoicing with VeriFactu (AEAT) compliance: issue F1/F2 invoices and R1-R5 correctives, manage companies and customers, validate NIFs, and register fiscal documents from any AI agent. OAuth remote or stdio."
category: Compliance
stars: 0
added: 2026-08-25
source: mcpservers.org /all listing
relevance: ★★★
tags: [mcp-server, invoicing, verifactu, spain, aeat, e-invoicing, compliance]
---

# BeeL MCP

**Legally compliant Spanish e-invoicing inside your agent.** BeeL (beel.es) provides an MCP server for Spanish electronic invoicing with VeriFactu registration with AEAT (the Spanish tax authority). Agents can issue F1/F2 invoices, R1-R5 corrective invoices, manage companies and customers, validate NIFs against the census, and read fiscal data, with fiscal guardrails that stop non-compliant requests before they become fiscal documents.

```
Server type: Remote Streamable HTTP (hosted) or local stdio
Endpoint: https://mcp.beel.es/mcp (remote, OAuth one login per user)
Stdio: npm package @beel_es/mcp (API key auth for headless use)
Tools: ~120 tools derived from the public OpenAPI contract
Repo: github.com/beel-es/beel-mcp (MIT, actively maintained)
```

## Why This Matters for Operators

Spanish invoicing compliance is the kind of work that is both mandatory and tedious: regime keys, series management, corrective invoice chains, and NIF validation all have exact rules, and VeriFactu adds registration requirements with AEAT. BeeL turns it into agent-native operations. Tools are derived from the vendor's public OpenAPI contract, so each tool's input schema is the real operation schema, and a tool-inclusion policy excludes binary downloads, multipart uploads, and deprecated operations. Fiscal guardrails travel with the tools as both documentation and pre-flight checks.

## Tools & Capabilities

| Tool group | What it does |
|---|---|
| `beel_create_company_invoice`, `beel_issue_company_invoice`, `beel_send_company_invoice` | Create, issue, and send compliant invoices |
| `beel_create_company_corrective_invoice` | R1-R5 corrective invoice chains |
| `beel_validate_nif` | Validate NIF against the census |
| `beel_create_company_customer`, `beel_list_company_customers` | Customer management with NIF records |
| `beel_create_company_recurring_invoice`, `beel_set_company_invoice_schedule` | Recurring and scheduled invoices |
| `beel_get_company_fiscal_summary`, `beel_list_company_stats` | Fiscal summaries and statistics |
| `beel_get_company_veri_factu_configuration`, `beel_update_company_veri_factu_configuration` | VeriFactu configuration |
| `beel_generate_company_representation`, `beel_download_company_representation_document` | Fiscal representation documents |
| `beel_create_company_product`, `beel_list_company_products` | Product catalog with tax regimes |
| `beel_create_company_series`, `beel_set_company_default_series` | Invoice series management |
| `beel_initiate_payment_connection`, `beel_list_company_payment_events` | Payment connections and events |
| `beel_get_account_usage`, `beel_provision_account` | Account management |

The full surface (about 120 tools) covers companies, customers, invoices, recurring invoices, series, products, tax configuration, payment events, webhooks, and account administration. Docs tools (`beel_docs_search`, `beel_docs_get`) let the agent pull the fiscal rules it needs mid-task.

## Installation

Remote (Streamable HTTP + OAuth):

```json
{
  "mcpServers": {
    "beel": { "type": "http", "url": "https://mcp.beel.es/mcp" }
  }
}
```

Local stdio for headless use (API key instead of browser login):

```bash
npx -y @beel_es/mcp
```

## Configuration

Remote: sign in once per user through the client's OAuth flow. Stdio: supply a BeeL API key via the client's secret environment configuration. Guides at docs.beel.es/mcp cover Claude Code, ChatGPT, Cursor, and VS Code.

## Business Relevance

- **Compliance automation:** VeriFactu registration and regime keys handled by rule, not memory.
- **Invoicing throughput:** issue, correct, and schedule invoices from chat.
- **Fiscal safety:** pre-flight guardrails reject non-compliant requests before they become documents.
- **Spanish market operations:** NIF validation and census checks built into the workflow.

## Integration with CorpusIQ

BeeL's structured invoice output pairs with CorpusIQ connectors for the accounting side: reconcile issued invoices against payments in your accounting system (QuickBooks via CorpusIQ), track Spanish customers in your CRM, and monitor invoice volume with dashboards rendered from the connector data.

## Limitations

- Remote endpoint requires OAuth; anonymous enumeration is refused (401 confirmed live).
- The full tool surface is large; the vendor's inclusion policy trims plumbing but clients should still pin the tools they need.
- Spanish-market specific; no multi-country invoicing surface.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [Candor Finance MCP](/hermes/mcp/servers/external/candor-finance-mcp)
