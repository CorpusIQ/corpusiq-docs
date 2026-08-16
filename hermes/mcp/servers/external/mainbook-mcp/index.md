---
title: MainBook MCP
description: Bank-statement conversion over MCP — turn PDF bank statements into checked Excel, CSV or JSON with balance validation. One job, five tools, folder-scoped local access, page-credit pricing.
category: Finance / Accounting
stars: n/a (new listing)
added: 2026-08-16
source: mcpservers.org
relevance: ★★
tags: [bank-statements, bookkeeping, accounting, pdf, data-extraction, finance]
---

# MainBook MCP

**Local bookkeeping-conversion server (stdio, API key)** — MainBook scopes itself to one job and does it well: converting PDF bank statements into checked JSON, Excel, or CSV with balance validation. It runs locally with a MainBook API key, talks to api.mainbook.ai for the conversion engine, and refuses to touch anything outside the folders the operator names.

```
Server type: Local (stdio via uvx or pip)
Auth: Account API key (MAINBOOK_API_KEY, mb_live_...)
Endpoint: api.mainbook.ai (REST under the local server)
Tools: convert_bank_statement, get_conversion, list_conversions, get_balance, output_folder
Pricing: 1 PDF page = 1 credit; 20-page signup grant; packages bought in the web app
Category: Finance / Accounting
Built by: mainbook.ai
```

## Why This Matters for Operators

Bank statements are the worst part of bookkeeping: every bank exports differently, PDFs resist parsing, and a wrong number poisons reconciliation. MainBook turns the chore into one tool call — "convert ~/Downloads/march-statement.pdf and save the Excel next to it" — and returns 63 transactions with opening and closing totals reconciled against the statement. If the totals do not match, nothing is silently accepted; the validation flags it.

The boundary design is the trust story: the server can only read and write inside the folders passed as arguments or set in `MAINBOOK_ALLOWED_DIRS`, and it has no tool for buying credits, handling payments, or deleting anything. It cannot spend money it was not given.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `convert_bank_statement` | Upload one PDF, run a conversion job, poll 30–900s, return reviewed JSON or write XLSX/CSV to disk |
| `get_conversion` | Pick up a job after a client timeout, write results to a chosen destination |
| `list_conversions` | Cursor-paged account job history |
| `get_balance` | Total, reserved, and available page credits |
| `output_folder` | Read or change the default local result folder |

Operating limits: 500 pages and 50MB per PDF, 6 in-flight jobs per key, 90-day document retention. A client timeout does not kill the job — `get_conversion` picks it up by job ID.

## Installation

```json
{
  "mcpServers": {
    "mainbook": {
      "command": "uvx",
      "args": ["mainbook-mcp", "~/Downloads", "~/Desktop", "~/Documents"],
      "env": { "MAINBOOK_API_KEY": "mb_live_…" }
    }
  }
}
```

Requires Python 3.11+ (or `pip install mainbook-mcp`). Folder boundary via the `args` list or `MAINBOOK_ALLOWED_DIRS` (colon-separated on macOS/Linux, semicolon on Windows). The account must accept the API Terms or calls fail with `api_terms_not_accepted`.

## Business Relevance

- **Bookkeepers** convert statement PDFs into spreadsheets with reconciliation checks in one prompt
- **Finance teams** keep bank data out of the agent context until it is structured and validated
- **Ops automation** can route statement folders through the agent on a schedule, with the folder boundary as the guardrail
- **Audit prep** gains checked CSV/JSON exports instead of hand-typed entries

## Integration with CorpusIQ

MainBook is the intake step for the accounting layer CorpusIQ already connects: converted statements become clean CSV/JSON that feeds QuickBooks imports or CorpusIQ's financial connectors for reconciliation against live balances. The split of labor is clean — MainBook turns the PDF into checked data, CorpusIQ turns that data into cross-source financial truth.

## Limitations

- One job only — no general accounting, invoicing, or categorization tools
- Page-credit pricing; heavy monthly conversion volumes need a package check
- Local stdio means the folder boundary is only as strong as the operator's configuration
- New listing — the MCP surface has no community track record yet

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
