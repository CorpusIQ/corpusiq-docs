---
title: gofact MCP - Local French E-Invoicing with Legal Numbering
description: Local-first French e-invoicing MCP server that turns an HTML invoice into a compliant Factur-X file (PDF/A-3 with embedded EN 16931 CII XML). Runs entirely on the operator's machine as a Go binary with no account or cloud service, holds the legal invoice numbering in a locked transactional registry, and enforces EN 16931 business rules before anything is written.
category: Finance / Accounting
stars: 5
added: 2026-09-04
source: "mcp.so GitHub issue #3936"
relevance: ★★
tags: [e-invoicing, factur-x, en-16931, french-compliance, invoicing, accounting, stdio, local-first]
---

# gofact MCP

**Local MCP server (stdio, Go binary)** - a single static binary that turns a print-ready HTML invoice into a compliant Factur-X file: a PDF/A-3 with the EN 16931 CII XML embedded byte for byte. Built for the French e-invoicing reform, runs entirely on the operator's machine with no account, no cloud service and no subscription.

```
Server type: Local (stdio) - Go binary, no runtime dependency beyond a Chrome-family browser for rendering
Auth: None (runs locally; PDP credentials only for optional submission)
Package: MCPB bundles on GitHub Releases (linux/darwin/windows, amd64/arm64)
Tools: 11 (only send_invoice is destructive, confirmation required)
Compliance: EN 16931 business rules pre-check + PDF/A-3 self-check; veraPDF verified in CI
License: AGPL-3.0-or-later
Built by: kOlapsis (independent, France)
```

## Why This Matters for Operators

France's e-invoicing mandate makes Factur-X compliance a real cost for every freelancer and small business billing French counterparties. The alternative is a commercial e-invoicing platform subscription or hand-assembling the XML yourself. gofact collapses that into a local binary: the model drafts the invoice content, gofact checks it against the EN 16931 business rules before producing anything, allocates the legal invoice number transactionally, and writes a self-checked Factur-X file. **Compliance does not depend on which model composes the document.**

The legal numbering is the interesting part: the continuous, gap-free, never-reused sequence is held by the server in a locked registry, never by the language model. The model writes a `{{NUMERO}}` token and gofact allocates the real number. The same registry plus a journal.ndjson audit log gives a small business the archival trail the reform requires, locally.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `list_organizations` | List issuing entities (each is a self-contained directory with its own identity, numbering registry and audit log) |
| `get_organization` | Read one organization's configuration |
| `init_organization` | Create a new issuing entity |
| `update_organization` | Update issuer identity, legal mentions or PDP routing |
| `search_client` | Find clients recorded for an organization |
| `get_invoice_template` | Read the default template carrying the mandatory French legal mentions |
| `preview_next_number` | Show the next legal invoice number that would be allocated |
| `list_invoices` | List issued invoices |
| `create_invoice` | HTML invoice + structured data to Factur-X (PDF/A-3 + CII XML embedded verbatim) |
| `send_invoice` | Submit to a French e-invoicing platform (PDP) - the only destructive tool, explicit confirmation required |
| `get_invoice_status` | Read the PDP submission status of an invoice |

Prompt: `nouvelle-facture` ("make me an invoice for ACME, 2 days at EUR 600" is the documented usage pattern).

## Installation

```bash
# Download the static binary for your platform from GitHub Releases, then:
claude mcp add gofact -- /path/to/gofact mcp
```

The binary needs a Chrome, Edge, Brave or Chromium install for HTML-to-PDF rendering (auto-detected; Windows uses preinstalled Edge). Point at a specific executable with `GOFACT_CHROME` or `-chrome` if needed.

## Configuration

```json
{
  "mcpServers": {
    "gofact": {
      "command": "/path/to/gofact",
      "args": ["mcp"]
    }
  }
}
```

Issuer identity, payment IBAN and PDP credentials come from environment variables (or a `.env` file): `GOFACT_SELLER_NAME`, `GOFACT_SELLER_SIRET`, `GOFACT_SELLER_VAT_NUMBER`, `GOFACT_PAYEE_IBAN`, `GOFACT_SELLER_ELECTRONIC_ADDRESS` (Peppol BT-34 routing) and, for `send_invoice` only, the PDP credentials. With no seller configured, gofact fails explicitly rather than issuing an incomplete invoice. Every value can still be overridden per invoice via the JSON payload.

## Business Relevance

- **French freelancers and SMBs** get reform-compliant invoices from a chat prompt with no platform subscription.
- **Accounting pipelines** can treat the local numbering registry and journal.ndjson as the system of record for the legal sequence.
- **Multi-entity operators** keep each issuing organization in a self-contained directory (identity, registry, log, template, invoices).
- **Agencies and bookkeepers** can batch-generate compliant documents without touching a web console.

## Integration with CorpusIQ

CorpusIQ covers the read side of finance (invoices pulled through QuickBooks, Stripe and accounting connectors). gofact is the write side for a jurisdiction CorpusIQ does not cover: French Factur-X issuance. An operator can reconcile paid CorpusIQ data against invoices generated locally by gofact, and use the PDP status tool to track submission through the French network without adding a second SaaS subscription.

## Limitations

- Brand new project (repo created Aug 31, 2026, 5 stars) - the compliance claims are backed by CI tests against veraPDF, but the tool is young.
- gofact is not an accredited PDP: it produces the Factur-X file; an accredited platform transports it. Submission support exists for one PDP (SUPERPDP) via `send_invoice`.
- Needs a Chrome-family browser on the machine for PDF rendering.
- Single-country scope (French e-invoicing rules and legal mentions), though the underlying format is EU-wide Factur-X.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [Factur-X by Orvel MCP - Hosted French E-Invoicing for Agents](/hermes/mcp/servers/external/facturx-orvel-mcp)
- [ISO 20022 Generator MCP - SEPA XML and SWIFT MT103 from Chat](/hermes/mcp/servers/external/iso-20022-generator-mcp)
- [QuickBooks MCP Server - CorpusIQ Docs](/hermes/mcp/servers/external/quickbooks-mcp)
