---
title: "camt053-mcp — ISO 20022 Bank Statement Parser MCP"
description: "Parse & reconcile ISO 20022 camt.053 bank-to-customer statements from MCP clients. 19 tools, CBPR+/HVPS+ readiness, SLSA-L3 provenance. Part of the ISO 20022 MCP Suite by sebastienrousseau."
source: github.com/sebastienrousseau/camt053-mcp
stars: 1
language: Python
transport: stdio
auth: None (processes local files)
category: Finance & Fintech
last_updated: 2026-07-20
---

# camt053-mcp — ISO 20022 Bank Statement Parser

**Parse, validate, and reconcile ISO 20022 camt.053 bank-to-customer statements from any MCP client.** Part of the [ISO 20022 MCP Suite](https://github.com/sebastienrousseau) — the emerging standard library for financial messaging in AI agent workflows.

## What It Does for Operators

If your business receives camt.053 statements from banks (standard in EU, UK, CH, and migrating globally under CBPR+), this server lets AI agents:

- **Parse statements** — Extract transactions, balances, and metadata from camt.053 XML
- **Validate against XSD** — Ensure statements conform to ISO 20022 schema
- **Reconcile entries** — Match statement entries against internal records
- **Generate reversing entries** — One-shot XML generation for corrections/reversals
- **Export to accounting** — Native journal export to Xero and QuickBooks Online
- **CBPR+ readiness check** — November 2026 cliff assessment for cross-border payments

## Installation

```bash
pip install camt053-mcp
# Run the MCP server
camt053-mcp
```

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "camt053": {
      "command": "camt053-mcp"
    }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `parse_statement` | Parse a camt.053 XML file — extract all entries, balances, metadata |
| `validate_xsd` | Validate statement against ISO 20022 XSD schema |
| `reconcile` | Match statement entries against a provided list of expected transactions |
| `generate_reversal` | Generate a reversing entry XML for a given transaction |
| `export_xero` | Export entries as Xero journal import format |
| `export_qbo` | Export entries as QuickBooks Online journal import format |
| `cbpr_readiness` | Check a statement for November 2026 CBPR+ compliance |
| `classify_entry` | LLM-driven transaction classification via MCP Sampling |

## Operator Use Cases

1. **Finance Teams** — Automate monthly bank statement reconciliation. Feed camt.053 files to your AI agent and get matched/unmatched entries, exported to Xero/QBO.

2. **Treasury Operations** — Validate incoming statements for CBPR+ readiness before the November 2026 deadline. Flag non-compliant fields.

3. **Fintech Builders** — Use the parsing + validation pipeline as a building block for AI-powered banking workflows.

4. **Auditors** — Batch-validate historical statements. Generate reversing entries for corrections with full audit trail.

## ISO 20022 MCP Suite

camt053-mcp is part of a growing suite of ISO 20022 MCP servers:

| Server | Standard | Purpose |
|--------|----------|---------|
| **camt053-mcp** | camt.053 | Bank-to-customer statement |
| **pacs008-mcp** | pacs.008 | FI-to-FI credit transfer |
| *(more planned)* | pacs.002, camt.029, camt.056 | Status reports, resolutions |

## CorpusIQ Angle

ISO 20022 is the global standard for financial messaging — every bank migration is underway with the CBPR+ deadline approaching. This MCP suite gives operators programmatic access to banking messages from AI agents. Pairs naturally with CorpusIQ's financial connectors (Stripe, QuickBooks, etc.) for end-to-end financial automation.

## Limitations

- Python-only
- Requires camt.053 XML files as input — does not fetch statements from banks directly
- Early-stage (1⭐). Test thoroughly before production use.
- CBPR+ readiness checks reference November 2026 rules — will need updates post-deadline
