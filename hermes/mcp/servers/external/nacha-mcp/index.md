---
title: "Nacha MCP - ACH File Parsing and Validation"
description: "Local stdio MCP server that parses NACHA/ACH payment files into structured JSON and validates them structurally and arithmetically: entry hashes, debit/credit totals, and addenda counts recomputed against declared controls, with IAT batch support."
category: Finance
stars: 0
added: 2026-08-25
source: mcpservers.org /all listing
relevance: ★★
tags: [mcp-server, ach, nacha, payments, validation, banking, finance-operations]
---

# Nacha MCP

**An MCP server that reads ACH files the way a bank does.** nacha-mcp parses NACHA/ACH payment files into full structured JSON and validates them against the standard's own rules: record lengths, record-type ordering, batch header/control pairing, and arithmetic validation that recomputes entry hashes, debit/credit totals, and entry/addenda counts from the actual entries, then cross-checks them against the declared batch and file control values. Mismatches surface as validation issues instead of being silently accepted.

```
Server type: Local stdio (Node.js)
Transport: stdio over MCP protocol
Tools: 2 (parse_nacha_file, summarize_nacha_file)
Repo: github.com/msuresh007/nacha-mcp (MIT, created Aug 23 2026)
Requires: Node.js 18+, npm
```

## Why This Matters for Operators

ACH files fail in production when a bank rejects a batch that your system wrote hours ago. The failure surface is arithmetic: a wrong entry hash or a debit total that does not match the control record. Nacha MCP gives an agent the tools to inspect any ACH file before submission or when a bank pushes back: parse it into readable JSON, or get a summary with batch count, total debits and credits, SEC codes present, and validation issues. IAT (International ACH Transaction) batches and addenda type codes 10-18 are supported.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `parse_nacha_file` | Parses a NACHA file at a given path into full structured JSON: file header, batches (header, entries with addenda, control), and file control |
| `summarize_nacha_file` | Condensed summary: batch count, total entries, total debit/credit amounts, SEC codes present, and validation issues |

Both tools take a single `file_path` argument (absolute path to the file on disk). Validation includes structural checks (record length, record-type ordering, batch header/control pairing) and arithmetic checks (entry hash, debit/credit totals, entry/addenda counts recomputed from actual entries).

## Installation

```bash
git clone https://github.com/msuresh007/nacha-mcp.git
cd nacha-mcp
npm install
npm run build
```

The server communicates over stdio; point your MCP client at the built server with `node dist/server.mjs` (or the entry the repo's client guide specifies). A sample ACH file at `examples/sample.ach` confirms the setup.

## Configuration

No credentials. Both tools can also be run directly from the command line without an MCP client to verify parsing works before wiring it into an agent.

## Business Relevance

- **Pre-submission checks:** validate ACH batches before sending to the bank.
- **Rejection triage:** parse a rejected file and pinpoint the failing control math.
- **Finance automation:** let agents read payment files in natural language during close and reconciliation.
- **Integration testing:** generate structured ACH JSON for payment system tests.

## Integration with CorpusIQ

Nacha MCP's structured ACH JSON pairs with CorpusIQ connectors for finance operations: compare parsed batch totals against bank feeds in QuickBooks, log validation issues in Airtable for AP follow-up, and render ACH volume dashboards from the parsed summaries.

## Limitations

- Local stdio server only; files must be accessible on the machine running the client.
- Two tools, focused scope: parsing and validation, not ACH file generation.
- 0-star, days-old community repo; validate against your own sample files before production use.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [Candor Finance MCP](/docs/hermes/mcp/servers/external/candor-finance-mcp)
