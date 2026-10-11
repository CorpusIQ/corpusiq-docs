---
title: "BoomTax MCP - Tax Filings in Your Assistant"
description: "Read-only access to a company's IRS e-filing: filings by year and form, e-file status and errors, and payer details, answered in chat."
category: Finance & Accounting
stars: n/a (new listing)
added: 2026-10-10
source: "mcpservers.org /all (page 2) + vendor page (api.boomtax.com docs); catalogued at the October 10, 2026 evening sweep"
relevance: ★★★
tags: [tax, e-filing, compliance, accounting, finance, oauth, remote-mcp]
---

# BoomTax MCP

**Official MCP server for BoomTax, the IRS e-filing service** - ask the assistant about a company's filings instead of clicking through a portal: what was filed for a tax year, which form types went out, where each e-file request stands, what errors came back, and the payers on file with masked TINs. Ten read-only tools, hosted endpoint with OAuth, and a hard boundary: the server cannot create, edit, delete or submit anything. The finance-ops find of the October 10 evening sweep, catalogued with the hosted endpoint probed live (initialize returns 401 with an OAuth discovery header).

```
Server type: Remote (Streamable HTTP at https://api.boomtax.com/mcp) or local stdio via npx -y @boomtax/mcp-server
Auth: OAuth with PKCE and dynamic client registration (browser sign-in); local client uses a read-scoped BOOMTAX_CLIENT_ID and BOOMTAX_CLIENT_SECRET
Tools: 10 read-only (list_filings, get_filing_details, get_filing_summary, list_filing_forms, get_form, get_efile_status, get_efile_errors, list_payers, get_payer, list_filing_types)
Category: Finance & Accounting
Built by: BoomTax (boomtax.com; repo github.com/boomtax/mcp-server; published in the official MCP Registry as io.github.boomtax/mcp-server v2.0.0)
```

## Why This Matters for Operators

Tax season turns into an email scavenger hunt: which 1099s went out, whether that one filing was accepted or rejected by the IRS, what the error code meant, which payer TIN is on file. The answers exist inside the e-filing provider, but the questions get asked in chat, by whoever is closest to the process. BoomTax MCP moves the read side of e-filing into the conversation - filing counts by status and form type, the e-file request and response timeline per filing, error messages in context - without granting the assistant any ability to touch a filing. For finance teams and their advisors, review gets faster and nothing gets changed by accident.

## Tools & Capabilities

| Tool | What it covers |
|---|---|
| `list_filings` | Filter filings by year, form type and status; includes the filing system |
| `get_filing_details` | Filing details, payer summary and e-file status |
| `get_filing_summary` | Counts by status and form type |
| `list_filing_forms` | Paginated form metadata within a filing |
| `get_form` | Form metadata, status and dates |
| `get_efile_status` | The e-file request and response timeline |
| `get_efile_errors` | E-file errors and messages |
| `list_payers` | Payers across accessible filings |
| `get_payer` | Payer details with a masked payer TIN |
| `list_filing_types` | Available filing types, tax years and filing systems (ask this rather than relying on a static list that goes stale each tax year) |

## Installation

```json
{
  "mcpServers": {
    "boomtax": {
      "url": "https://api.boomtax.com/mcp"
    }
  }
}
```

Claude Code: `claude mcp add boomtax --transport http https://api.boomtax.com/mcp`, then complete the browser sign-in. The server expects a 401 when opened without authentication - that response carries the OAuth discovery header, so a bare URL in a browser is not a connection test. Local client (version 2, Node.js 22+): clone the repo or run the package when 2.0.0 is published, with a read-scoped API credential in `BOOMTAX_CLIENT_ID` and `BOOMTAX_CLIENT_SECRET`; it fetches short-lived OAuth tokens and never uses account email and password.

## Configuration and Safety

- Read-only by construction: the ten tools cannot create, edit, delete or submit filings. Filing management stays in the BoomTax dashboard, where it belongs.
- The local client forwards only these ten tools to the hosted service and blocks other tool names.
- API access must be enabled on the BoomTax account and credentials should be read-scoped; keep the credential files out of source control.
- OAuth uses DCR with PKCE; CIMD is not supported, so choose automatic registration when a client offers a choice. Organization accounts may require an admin to add the connector first.

## Business Relevance

- **Finance and accounting teams**: month-end and tax-season questions ("did the 941s for Q3 all go out", "what error did that 1099 get") answered from the system of record instead of by phone and email.
- **Bookkeepers and advisors running e-filing for clients**: check counts, statuses and payer details across filings from the same chat where client questions arrive.
- **Operations leads**: a clean audit-friendly read path into filings without handing anyone the ability to submit or change one.

## Integration with CorpusIQ

Filing status is one slice of the financial picture; the rest lives in the connectors. Ask BoomTax MCP what was filed and where it stands, then ask CorpusIQ for the numbers behind it - QuickBooks spend and balances, Stripe revenue, bank and invoice context - and have both answers in one thread, each traceable to its source.

## Limitations

- Read-only: no filing creation, no submissions, no edits. That is the design, not a gap.
- The hosted API must be enabled on the BoomTax account; new accounts may need to contact BoomTax support to turn it on.
- The npm 2.0.0 client was not yet published at cataloguing time - the remote connection or running from the source tree are the current paths; npm 1.0.0 uses a deprecated legacy authentication.
- Error and status detail follows what the IRS e-filing pipeline returns; the server does not add interpretation beyond the messages.

## FAQ

### Can the assistant file or change anything?

No. The server exposes ten read tools and cannot create, edit, delete or submit filings. Local client builds block tool names outside that list.

### Do I need a BoomTax account?

Yes - the connector reads your own organization's filings through OAuth sign-in. API access must be enabled on the account (support@boomtax.com if it is not available yet).

### How do I connect it in Claude or ChatGPT?

Add `https://api.boomtax.com/mcp` as a custom connector and complete the OAuth sign-in with automatic client registration. Organization workspaces may require an owner to add the connector before members connect.

## See Also

- [NormAPI MCP - German E-Invoices for Your Agent](/hermes/mcp/servers/external/normapi-mcp/)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
