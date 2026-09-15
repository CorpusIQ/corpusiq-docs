---
title: Wafeq MCP - Accounting Books for Agents
description: Run Wafeq accounting books from Claude, Cursor or any MCP client - all 251 API endpoints as safety-categorized MCP tools over stdio or Streamable HTTP, MIT licensed.
category: Finance
stars: n/a (new listing)
added: 2026-09-09
source: mcpservers.org
relevance: ★★
tags: [accounting, invoicing, bookkeeping, uae-business, vat, financial-operations, erp, self-hosted]
---

# Wafeq MCP

**Community MCP server (stdio or Streamable HTTP, MIT)** - run Wafeq accounting books in plain language from any MCP client. All 251 Wafeq API endpoints become spec-generated tools, each tagged with a safety category so the assistant knows what an action does before it calls it.

```
Server type: Self-hosted (stdio for local, Streamable HTTP via Docker)
Auth: Wafeq API key or OAuth2 token (in server env), optional bearer on HTTP
Endpoint: localhost:8765 (docker compose default)
Tools: 253 (251 spec-generated from the Wafeq Public API + 2 handwritten)
Pricing: Free (MIT); requires a Wafeq organization with API access
Category: Finance
Built by: ohneben (community), registry io.github.ohneben/wafeq-mcp
```

## Why This Matters for Operators

Accounting APIs are dangerous surfaces for LLMs: "save invoice" and "file invoice with the tax authority" look identical in a CRUD-shaped wrapper, but one is reversible and the other is permanent. **Wafeq MCP fixes that with nine safety categories, not four** - read-only, write, state-change and irreversible tiers, plus machine-readable annotations (readOnlyHint, destructiveHint) that hosts like Claude honor for auto-trust and confirmation gates.

The engineering discipline is unusual for a community server: whole-period validation before sending reports, automatic idempotency keys on all 146 write endpoints, retries with backoff, and tenant verification at startup so a mis-set key fails loudly against the right organization instead of silently writing to the wrong books.

## Tools & Capabilities

| Area | Coverage |
|---|---|
| Sales and purchasing | Invoices, bills, quotes, credit and debit notes |
| Money movement | Payments, banking, journals, payroll |
| Reporting | Balance sheet, profit-and-loss, cash flow, trial balance with per-report schemas |
| Operations | Projects, inventory, files (multipart upload, binary PDF handling) |

Exact tool names are generated from the bundled OpenAPI spec - one tool per endpoint, safety-categorized.

## Installation

```bash
cp .env.example .env   # set WAFEQ_API_KEY
docker compose up -d --build
```

Then point any MCP client at http://localhost:8765 (or run from source with Node.js 20+ for stdio).

## Configuration

```json
{
  "mcpServers": {
    "wafeq": {
      "type": "http",
      "url": "http://localhost:8765"
    }
  }
}
```

The Wafeq credential lives in the server's environment and is injected per request - the model never sees the key. Set MCP_SHARED_TOKEN if the endpoint is reachable beyond localhost.

## Business Relevance

- **Wafeq users (UAE-region businesses)** get their full books - invoices to reports - readable from any AI assistant.
- **Bookkeepers** hand the assistant read-only queries while writes stay gated by safety categories.
- **Operators who fear LLM accounting errors** get confirmation gates on the 44 destructive tools and plain-language report parameters that validate locally.
- **Teams running one shared assistant** use the Streamable HTTP mode so every client hits the same live books.

## Integration with CorpusIQ

Wafeq MCP is a regional-accounting complement to CorpusIQ's connector surface: where CorpusIQ pulls QuickBooks or Stripe data for reporting and automation, Wafeq MCP serves Wafeq-ledger businesses (UAE VAT compliance, invoicing, journals). A composed workflow: the assistant reads outstanding invoices through Wafeq MCP, cross-checks them against Stripe payments in CorpusIQ, and flags mismatches for the operator - two ledgers, one reconciliation loop.

## Limitations

- Community project, not an official Wafeq connector - check the repo before relying on it for compliance workflows.
- Requires a Wafeq organization with API access; the value is zero without a Wafeq subscription.
- 253 tools is a large surface - rely on the safety categories and keep writes scoped.
- Docker quick start binds to localhost only; team use needs the optional bearer-token auth.

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
