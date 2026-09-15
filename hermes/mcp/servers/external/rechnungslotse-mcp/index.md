---
title: Rechnungslotse MCP - German E-Invoicing for Agents
description: "Hosted German electronic invoicing server with 18 tools. Seven run keyless: validate XRechnung and ZUGFeRD against EN 16931 and the full KoSIT rule set with plain-language fixes, read invoices into structured data, explain rejection rule IDs, and check the German e-invoicing mandate, § 14 UStG fields, Leitweg-ID check digits and small-business thresholds. Eleven OAuth account tools create invoices, capture work logs, record payments and prepare VAT returns."
category: Finance & Accounting
stars: n/a (hosted server)
added: 2026-09-07
source: mcpservers.org
relevance: ★★★
tags: [e-invoicing, xrechnung, zugferd, en16931, german-tax, invoicing, vat, remote-mcp]
---

# Rechnungslotse MCP - German E-Invoicing for Agents

**Remote MCP server (Streamable HTTP, OAuth 2.1 + keyless tools)** - a hosted German electronic invoicing server from AOS Digital (aos-digital.de) that covers the whole XRechnung and ZUGFeRD lifecycle: create, validate against EN 16931 plus the full KoSIT rule set, and read into structured data. Seven of eighteen tools run with no account and no key; the remaining eleven operate inside one connected business over OAuth 2.1.

```
Server type: Remote (Streamable HTTP)
Auth: None for 7 tools (tools/list works unauthenticated); OAuth 2.1 with PKCE and dynamic client registration for the 11 account tools
Endpoint: https://rechnungslotse.de/api/mcp
Tools: 18 (7 keyless: validation, reading, mandate, § 14 UStG, Leitweg-ID, small-business checks; 11 account: create, search, work logs, payments, VAT return)
Pricing: Free plan with 3 invoices per month; rate limits on the free tools
Category: Finance & Accounting
Built by: AOS Digital, Germany (rechnungslotse.de)
```

## Why This Matters for Operators

Germany's e-invoicing mandate phases in from 2025 (receiving) through 2027/2028 (issuing), and rejections from public-sector buyers cite KoSIT rule IDs that most people cannot decode. Rechnungslotse turns that into plain language: every validation violation comes back with its rule ID, a plain-language explanation, and a link to a page explaining that rule - so the agent can tell you what BR-CO-15 means and how to fix it, not just that validation failed.

**The German specifics are built in, which generic EN 16931 validators miss**: Leitweg-ID check digits (MOD 97-10), the mandatory fields of § 14 UStG, the small-business thresholds of § 19 UStG (EUR 25,000 previous year, EUR 100,000 current year), small-amount invoices under § 33 UStDV, and the exact dates of the staged mandate. Files are never stored - they exist in memory for the duration of the call and are discarded, which matters for operators who do not want customer invoices parked on a third-party server.

The tool list was probe-verified keyless: the seven free tools return full schemas with `readOnlyHint` annotations, and calling an account tool without a token returns 401 with OAuth protected-resource metadata pointing at the standard well-known discovery documents.

## Tools & Capabilities

| Group | Tools |
|---|---|
| Validation and reading (keyless) | `rechnung_pruefen` (EN 16931 + KoSIT validation with rule IDs and plain text), `rechnung_lesen` (structured sender, recipient, line items, totals, due date, bank details), `fehler_erklaeren` (explain a rejection rule ID: what it requires, common causes, how to fix) |
| Mandate and statutory checks (keyless) | `pflicht_pruefen` (when a specific German business must issue e-invoices, with dates and statutes), `pflichtangaben_pruefen` (§ 14 UStG mandatory fields, works on Word or PDF invoices), `leitweg_pruefen` (Leitweg-ID parts and MOD 97-10 check digit), `kleinunternehmer_pruefen` (§ 19 UStG turnover limits) |
| Account operations (OAuth) | `rechnung_erstellen` (create a validated XRechnung, PDF or ZUGFeRD, idempotent by order number), `rechnung_datei`, `rechnungen_suchen` (by state, period or term, with open amounts and overdue flags), `kunden_suchen`, `betrieb_lesen` |
| Work logging and billing (OAuth) | `leistung_erfassen` (hours, material, flat rates, travel), `leistungen_offen`, `leistungen_abrechnen` (turn one customer's open items into a validated e-invoice) |
| Cash and VAT (OAuth) | `zahlung_erfassen` (record incoming payments), `offene_posten` (overdue invoices with dunning levels), `umsatzsteuer_aufstellung` (net and tax totals per rate with ELSTER field numbers) |

## Installation

```bash
claude mcp add --transport http rechnungslotse https://rechnungslotse.de/api/mcp
```

The seven free tools need no key, no signup and no stored data. For the account tools, the first call opens a browser window for OAuth login with the business's Rechnungslotse account; consent decides which permissions the client receives.

## Configuration

```json
{
  "mcpServers": {
    "rechnungslotse": {
      "type": "http",
      "url": "https://rechnungslotse.de/api/mcp"
    }
  }
}
```

OAuth 2.1 discovery is published at `https://rechnungslotse.de/.well-known/oauth-protected-resource` and `.../oauth-authorization-server`, with PKCE and dynamic client registration supported. The official MCP registry namespace is `de.rechnungslotse/e-rechnung`.

## Business Relevance

- **German SMBs and freelancers** validate outgoing XRechnung and ZUGFeRD files before buyers reject them, and check mandate dates against their own turnover.
- **Accountants and tax advisers** run § 14 UStG field checks and read invoices into structured data without opening PDFs by hand.
- **Billing teams** create invoices, log work, record payments and pull VAT return numbers with ELSTER field numbers from one connected account.
- **Software vendors** let their agents fix invoice rejections by pasting the rule ID and getting the plain-language remedy back.

## Integration with CorpusIQ

Rechnungslotse pairs with CorpusIQ's financial connectors: when a German operator's accounting stack (DATEV, sevDesk or Excel books synced through CorpusIQ) flags a rejected XRechnung, the CorpusIQ agent calls `rechnung_pruefen` to confirm the violation and `fehler_erklaeren` to produce the plain-language fix, then writes the corrected invoice back via `rechnung_erstellen` - idempotent by order number, so retries never duplicate. The VAT figures from `umsatzsteuer_aufstellung` feed the monthly close reports CorpusIQ assembles for the operator, with every ELSTER field number traceable to the underlying invoice data.

## Limitations

- German-law scope: mandate logic, Leitweg-ID and § 14 UStG checks are Germany-specific; EN 16931 validation itself is European.
- Not tax advice - the tools report what the rules say; edge cases belong with a tax adviser.
- Free plan is capped at three invoices per month; rate limits apply to the free tools.
- Hosted server only - the repository documents the hosted product, not a self-host build.
- No file storage by design - invoices exist only for the duration of the call.

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
