---
title: Factur-X by Orvel MCP - Hosted French E-Invoicing for Agents
description: Hosted e-invoicing MCP server that generates, validates and extracts Factur-X / EN 16931 e-invoices (PDF/A-3, CII, UBL 2.1 with French fr-ctc rules) from any MCP client. EU-hosted with a free tier of 50 documents per month, no card required, and a keyless initialize so agents can inspect the server before choosing a plan.
category: Finance / Accounting
stars: n/a (hosted service)
added: 2026-09-04
source: mcpservers.org
relevance: ★★★
tags: [e-invoicing, factur-x, en-16931, ubl, french-compliance, streamable-http, remote-mcp]
---

# Factur-X by Orvel MCP

**Remote MCP server (Streamable HTTP, stateless)** - a hosted engine that lets an AI agent generate, validate and read Factur-X / EN 16931 e-invoices from Claude, Cursor, VS Code, ChatGPT or a custom app. France makes e-invoicing mandatory for all VAT-registered businesses (receiving from September 2026, issuing 2026-2027), and this server removes the integration work.

```
Server type: Remote (Streamable HTTP, stateless)
Auth: Bearer API key (free key, no card); initialize, tools/list and resources are keyless
Endpoint: https://facturx.orvel.dev/mcp
Tools: 4 (generate_invoice, embed_xml, validate_invoice, extract_invoice) + 2 resources
Pricing: Free plan 50 documents/month, no card
Registry: io.github.LeBorgneAntoine/facturx (official MCP registry)
Hosting: EU (Railway, Amsterdam)
Built by: Orvel (Antoine Le Borgne, France)
```

## Why This Matters for Operators

The French e-invoicing reform is the largest structural change in European B2B billing in a decade, and it arrives in phases from September 2026. Every business that invoices French counterparties needs Factur-X output that passes EN 16931 schematron plus the French fr-ctc rules. Orvel's server gives an operator four verified tools instead of a document-integration project: generate a compliant invoice from structured JSON, attach XML to an existing PDF, validate any supplier invoice against the full rule chain with rule identifiers in the findings, and extract structured data back out of received invoices. All four tools were live-probed and confirmed in this sweep.

Validation output names the failing rule ids, so an agent can explain to an operator exactly which EN 16931 rule a draft violates and how to fix it - useful both for issuing and for auditing incoming supplier invoices.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `generate_invoice` | Invoice JSON to Factur-X PDF/A-3, CII XML or UBL XML; profiles MINIMUM to EXTENDED, EN 16931, FR/EN rendering |
| `embed_xml` | Attach a Factur-X XML to your own PDF and produce a valid PDF/A-3 |
| `validate_invoice` | XSD + EN 16931 schematron + French fr-ctc validation with structured findings carrying rule ids |
| `extract_invoice` | Read a PDF or XML e-invoice: parties, totals, VAT breakdown, lines |

Resources: `facturx://schema/invoice` (JSON Schema of the invoice object) and `facturx://guide/french-reform`. All tools are readOnlyHint / idempotentHint; nothing is stored server-side.

## Installation

```bash
claude mcp add --transport http facturx https://facturx.orvel.dev/mcp
```

The initialize and tools/list calls work without a key, so the agent can inspect the full server surface before any signup. Get a key at facturx.orvel.dev/docs/pricing (free plan, no card) and attach it as a bearer authorization header.

## Configuration

```json
{
  "mcpServers": {
    "facturx": {
      "url": "https://facturx.orvel.dev/mcp",
      "headers": { "Authorization": "Bearer YOUR_KEY" }
    }
  }
}
```

Claude Desktop users (custom connectors cannot send headers yet) can bridge with `mcp-remote` and an `FACTURX_KEY` env var. The same engine is available as a REST API (`/v1/invoices/generate`, `/v1/validate`, `/v1/extract`, OpenAPI at `/openapi.json`) sharing one key and one quota.

## Business Relevance

- **French B2B issuers** produce reform-compliant invoices from a chat prompt during the 2026-2027 rollout.
- **Accounts payable teams** validate incoming supplier invoices against EN 16931 and fr-ctc before payment.
- **Finance integrations** extract totals, VAT breakdowns and parties from received e-invoices into JSON for reconciliation.
- **Multi-format shops** output CII or UBL 2.1 XML as well as PDF/A-3, covering platform-specific submission requirements.

## Integration with CorpusIQ

CorpusIQ reads business data from accounting and payment connectors; Factur-X by Orvel is the issuance and validation layer for the French mandate. A CorpusIQ dashboard can flag which customers are subject to the French reform, and Orvel then generates the compliant invoice and validates supplier documents the same workflow receives. The two systems share the same boundary: CorpusIQ reconciles the ledger, Orvel guarantees the document format.

## Limitations

- Closed-source engine; the public repo holds only the manifest, brand assets and client examples.
- Stateless by design - no document storage; operators keep their own archive (which the French rules require anyway).
- Free tier is 50 documents/month; volumes beyond that are paid (see pricing page).
- Bearer-key auth only; no OAuth browser flow for interactive clients.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [gofact MCP - Local French E-Invoicing with Legal Numbering](/hermes/mcp/servers/external/gofact-mcp)
- [ISO 20022 Generator MCP - SEPA XML and SWIFT MT103 from Chat](/hermes/mcp/servers/external/iso-20022-generator-mcp)
- [QuickBooks MCP Server - CorpusIQ Docs](/hermes/mcp/servers/external/quickbooks-mcp)
