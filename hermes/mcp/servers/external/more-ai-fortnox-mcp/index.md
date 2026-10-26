---
title: "More AI Fortnox MCP - Swedish Books, Approved Writes"
description: "Fortnox accounting over MCP: fifteen tools that read Swedish books, propose the exact entry, and post only what a person approved with a token."
category: Finance / Accounting
stars: n/a (commercial, Fortnox App Market, 119 SEK per company per month)
added: 2026-10-25
source: "mcp.so feed card 2026-10-25T19:19:49Z + mcp.so tool listing (15 tools) + live probes on accounting.amore.cloud (401 invalid_token) + RFC 9728 protected resource + official MCP registry cloud.amore.accounting/fortnox 1.0.2 + vendor pricing and security pages"
relevance: ★★★
tags: [fortnox, sweden, accounting, bookkeeping, erp, vat, sie, approval-gate, idempotency, finance-ops]
---

# More AI Fortnox MCP

**Accounting is the one system where a wrong write is not a bad answer, it is a bad year.** Every assistant that touches a ledger eventually has to answer a harder question than "can the model read the books": can it be stopped from writing something nobody approved. This server is built around that stop.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://accounting.amore.cloud/mcp
Transport:   JSON-RPC 2.0 over HTTP
Auth:        OAuth sign-in through Fortnox
Scopes:      fortnox:read, fortnox:write
Tools:       15
Built by:    Starberg & More Solutions AB (Sweden)
Registry:    cloud.amore.accounting/fortnox 1.0.2
```

## Why This Matters for Operators

Fortnox is the accounting system a Swedish company actually runs on: invoices, supplier invoices, VAT returns, payroll basis, the year end. It is not a side tool, and no operator wants a language model improvising inside it.

The design here answers that with two separations. Reads are free-form: ask about overdue receivables, payables aging, cash forecast, profit and loss, balance sheet, key figures against last year, VAT return boxes, missing receipts, possible duplicate invoices. Writes are staged: the assistant proposes the exact request, the person approves that exact content, and only then does a commit call carry an approval token and an idempotency key.

That is the shape a finance process needs. It also happens to be the shape most MCP servers in this catalog do not have.

## What It Actually Does

The endpoint is gated, and the gate is published. `initialize` and `tools/list` on `https://accounting.amore.cloud/mcp` both returned HTTP 401 `{"error":"invalid_token"}` without a Fortnox sign-in, and `https://accounting.amore.cloud/.well-known/oauth-protected-resource` returned the resource, one authorization server, bearer tokens in a header, and exactly two scopes: `fortnox:read` and `fortnox:write`, with `resource_name` set to the server's own name.

The mcp.so listing carries the tool set: fifteen tools over one Fortnox company or several.

| Capability | What the description says |
|---|---|
| Company context | Returns the company the connection is working with, and is meant to be called first when the person has not named one |
| List companies | Every company the connection reaches, and which one is active |
| Propose a company switch | Reading needs no switch, so a switch is proposed and waits for a yes |
| Switch after approval | Only called after the person agreed to that exact switch |
| Connect another company | Returns a link the person opens to attach a company that is not yet connected, and explicitly is not the page for managing the existing connection |
| Document download | A link the person opens for an invoice, offer or order PDF, an SIE export, an archive or inbox file, and any list, summary or computed view as an Excel workbook |
| Read a document | Reads the text of an invoice, offer, order, archive file or SIE export so the assistant can check what it says, rather than handing the person a file |
| Upload into bookkeeping | Receipts, invoices and files attached in chat are placed in the company's Fortnox inbox, ready to book |
| Find supported operations | Lists live operation ids, then returns one operation's parameters and a field guide for its request body |
| `read_fortnox` | Runs a validated read for the authenticated company, one page at a time, with `fields` to narrow columns and `summarize` to group and total |
| Chart read | The same read rendered as an interactive chart and table where the client supports it, for trends, rankings, ageing and per-customer or per-account totals |
| `propose_fortnox_write` | Builds the exact request that would be sent and sends nothing; irreversible operations such as crediting or cancelling also need `confirm: true` |
| Commit the approved write | Sends the exact change already approved, using the `approval_token` and `idempotency_key` from the proposal, and refuses to be called twice for the same approval |
| Ambiguous outcome check | Reads Fortnox to find out what happened to a write that ended unclear, and never resends it |
| Write history | Lists the writes recorded for the company, newest first, including unresolved ones, fifty at a time |

Two details are worth naming because they are where finance integrations usually fail. The commit path takes an idempotency key, so a retried call after a timeout does not post the entry twice. And the ambiguous case has its own tool that reads the ledger to establish what happened instead of guessing or resending.

## What It Does Not Do

- **It is Swedish accounting.** Fortnox is a Swedish system, SIE is the Swedish standard export format, VAT boxes are Swedish VAT boxes. An operator outside Sweden gains nothing from it.
- **No copy of the books is stored**, per the vendor's security page, and each company can be set to read-only. That claim is the vendor's; this sweep could not test it from outside an account.
- **The tool schemas were not read directly.** The endpoint needs a Fortnox sign-in, so the fifteen descriptions above come from the vendor listing rather than from a live `tools/list`, and exact argument names were confirmed only where the descriptions quote them.
- **Pricing is per company, not per seat.** 119 SEK per company per month excluding VAT, all users in the company included, first 30 days free, billed through the Fortnox App Market where this is a published integration.
- **An accounting-firm edition exists separately** as `cloud.amore.byra/fortnox`, described as every consultant reaching every client with each change approved. It is a different registry entry with different economics, so firm buyers should ask for it by name.

## FAQ

### Does the agent write to the books on its own?
No. A write is a two-step exchange: `propose_fortnox_write` returns the exact request body and sends nothing, and the commit call only accepts the approval token and idempotency key from that proposal. Irreversible operations such as crediting or cancelling also require an explicit confirmation flag inside the proposal.

### What is SIE and why does it matter?
SIE is the standard Swedish file format for accounting data, the thing an auditor, an accountant or a buyer asks for at year end. The server can export an SIE file to a link the person opens, which turns a request that normally takes an email chain into one tool call.

### Can one connection span several companies?
Yes, and the server keeps the distinction explicit: reading needs no switch, but writing is bound to one active company, and changing it is proposed and confirmed rather than silently applied.

### What happens if a write times out mid-flight?
There is a dedicated tool for it. It reads Fortnox to establish whether the entry landed and never resends the change, and the write history list shows anything still unresolved.

## The Operator Test

Ask for a payables ageing report and then ask it to book one receipt from the Fortnox inbox. The first answer shows whether the reads are real; the second shows whether the approval gate holds, because a correct implementation stops and shows you the exact entry before anything is written.
