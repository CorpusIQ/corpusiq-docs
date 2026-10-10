---
title: "NormAPI MCP - German E-Invoices for Your Agent"
description: "Validate and generate XRechnung and ZUGFeRD invoices against the official KoSIT rules from chat; 25 free invoices, nothing stored."
category: Finance
stars: n/a (new listing)
added: 2026-10-09
source: "mcpservers.org /all + chatmcp/mcpso issues (October 9, 2026 evening sweep)"
relevance: ★★★
tags: [e-invoicing, invoicing, germany, xrechnung, zugferd, compliance, oauth, remote-mcp]
---

# NormAPI MCP

**Hosted and local MCP server for German e-invoices** - validate an XRechnung or ZUGFeRD document against the official KoSIT rules, or generate a compliant invoice from raw data, without leaving the chat. Validation needs no account; documents are never stored.

```
Server type: Remote (Streamable HTTP at https://normapi.com/mcp), plus stdio via npx @normapi/mcp
Auth: OAuth 2.1 from connectors, or an API key (Bearer header; NORMAPI_API_KEY for stdio)
Tools: 3 - validate_invoice, generate_invoice, explain_rule
Limits: documents up to 5 MB; 25 free generated invoices a month; validation never counts against the allowance
Privacy: invoices are processed in memory and never stored, by the MCP server or the API
Category: Finance
Built by: NormAPI (normapi.com)
```

## Why This Matters for Operators

German B2B invoicing runs on structured formats now: XRechnung and ZUGFeRD documents that must satisfy the KoSIT rule set before a client, portal or tax office accepts them. A rejected invoice means a delayed payment and a round of email.

NormAPI turns that check into a sentence. **"Validate this invoice" returns the verdict, the rule set version and every finding, each with a plain-language explanation of what the rule requires and how to fix it** - which matters because business-rule codes like BR-DE-15 mean nothing to the person who has to fix the document at 6 PM.

## Tools & Capabilities

| Tool | What it does | Account |
|---|---|---|
| `validate_invoice` | Checks an XRechnung (UBL or CII, as text) or a ZUGFeRD/Factur-X PDF against the official KoSIT rules and returns every finding with an explanation | No |
| `generate_invoice` | Produces an XRechnung (UBL or CII) or a ZUGFeRD PDF from invoice data, with totals computed server-side in decimal arithmetic, and validates the document before returning it | Yes, counts against the allowance |
| `explain_rule` | Explains a rule by code (BR-DE-15, BR-CO-10, PEPPOL-EN16931-R010 and the rest) with a link to its full page | No |

## Installation

```bash
claude mcp add --transport http normapi https://normapi.com/mcp
```

For stdio clients, run `npx -y @normapi/mcp` with `NORMAPI_API_KEY` set; for header-based clients use `Authorization: Bearer nk_live_...`. The first generated invoice signs connector clients in through OAuth, which creates an app-named API key you can revoke from your account.

## Configuration and Safety

- Three sign-in paths: OAuth 2.1 for connector clients, a Bearer API key for config-file clients, and the environment variable for stdio.
- Invoices are processed in memory and never stored; generation is metered (25 free a month), validation is not.
- Documents up to 5 MB; calls without a key run under anonymous limits.
- This is technical rule validation, not tax or legal advice.

## Business Relevance

- **Finance teams** catch KoSIT rule violations before an invoice leaves the building, instead of after a portal rejection.
- **Accounting firms** validate client documents in the assistant where the rest of the work happens.
- **ERP and billing owners** generate compliant XRechnung or ZUGFeRD documents from data already in the conversation.

## Integration with CorpusIQ

Pull the underlying numbers from CorpusIQ - revenue, invoices and customer records from QuickBooks, Stripe or your ERP connector - then hand them to NormAPI to produce and validate the compliant document in the same chat. CorpusIQ keeps the business figure consistent across systems; NormAPI makes the German e-invoice that leaves the building correct.

## Limitations

- German formats only: XRechnung, ZUGFeRD and Factur-X, validated against the KoSIT rule set.
- Generation is metered (25 free invoices a month); high-volume billing needs a plan.
- Validation is rule-based; it does not replace tax advice.
- The hosted server is proprietary; the npm package is the client-side stdio bridge to it.

## FAQ

### What formats does it validate?

XRechnung in UBL or CII syntax (as text) and ZUGFeRD or Factur-X PDFs (base64), against the official KoSIT rules.

### Does validation cost anything?

No. Validation and rule explanations need no account and never count against the allowance; only generated invoices are metered.

### Are my invoices stored anywhere?

No. Documents are processed in memory and never stored, by the MCP server or the API.

## See Also

- [Factur-X by Orvel MCP - Hosted French E-Invoicing for Agents](/hermes/mcp/servers/external/facturx-orvel-mcp/)
- [gofact MCP - Local French E-Invoicing with Legal Numbering](/hermes/mcp/servers/external/gofact-mcp/)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
