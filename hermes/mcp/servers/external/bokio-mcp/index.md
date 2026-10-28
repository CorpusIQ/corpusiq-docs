---
title: "bokio-mcp - Read Your Books Without Writing Them"
description: "Sixty tools over the Bokio accounting API, read-only until an environment variable is set, with VAT, ledger and double-booking checks computed in code."
category: Finance / Accounting
stars: 1 (GitHub, MIT, npm 0.5.0)
added: 2026-10-27
source: "npm registry record for bokio-mcp 0.5.0 read 2026-10-28, the repository diblaze/bokio-mcp README and its pushed_at 2026-10-27T22:12:08Z, the Metis-style tool table in the chatmcp/mcpso submission #6248 filed 2026-10-27T20:10:58Z, and the Bokio API limits stated in the README"
relevance: ★★★
tags: [accounting, bookkeeping, sweden, sie, vat, reconciliation, read-only, stdio, npm, small-business]
last_updated: "2026-10-27"
---

# bokio-mcp

**Most accounting integrations ask an operator to trust an agent with write access on day one. This one ships the write tools hidden behind an environment variable, and puts the arithmetic that matters in code.**

```
Server type:  Local (stdio), npm package
Package:      npx -y bokio-mcp (npm bokio-mcp 0.5.0, MIT)
Repository:   github.com/diblaze/bokio-mcp
Auth:         BOKIO_TOKEN private integration token, BOKIO_COMPANY_ID
Tools:        60, of which 36 are read-only and 24 stay hidden
              unless BOKIO_ALLOW_WRITES=1
Market:       Sweden (Bokio), one company per server instance
Runtime:      Node.js 22 or later
```

## Why This Matters for Operators

The question a founder actually asks is not "show me my ledger". It is "what is on the bank account at the end of the month", "which customer invoices are still unpaid", "what does the VAT for last quarter add up to", and "has anything been booked twice". A generic model answers the last one badly, because double bookings are a pattern across rows rather than a fact in any row.

This server answers them by computing rather than reasoning. It pulls the SIE export, which is the standard Swedish accounting data interchange file, and works on it directly: balances at a date, a ledger for one account, VAT and profit and loss for a period, open items, suspected double bookings, and a reconciliation against a bank statement. The README states the arithmetic is done in whole ore and finished numbers are handed back, so the same question returns the same answer every time instead of a freshly reasoned one.

That is the correct division of labour. A language model should not be doing VAT arithmetic over a hundred journal lines and it should not be trusted to notice a duplicate.

## The Read-Only Default

Write tools are not permissioned per call. They are absent from the tool surface until `BOKIO_ALLOW_WRITES=1` is set in the environment, which means the containment lives in the process configuration rather than in a prompt, a policy or an approval step. For an operator who wants an assistant to answer questions about live books, this is the shape that makes the connection acceptable at all: the agent cannot post a journal entry because the tool to post one does not exist in its list.

The trade is that it is a process-wide switch. Turning it on for one correction turns it on for every call in that session, so the honest advice is to run two configurations if both behaviours are needed, and to treat the write-enabled one as the higher-risk credential.

## What It Covers

Read surface, from the vendor's own tool table: journal entries, invoices, credit notes, customers, suppliers, supplier invoices, items, uploads, bank payments (read only), chart of accounts, fiscal years and the SIE export. Computed surface, built on the export: balances at a date, ledger per account, VAT and profit and loss for a period, open items, possible double bookings, and bank statement reconciliation.

Setup is three facts an operator already has: a Bokio private integration token created under Integrations in Bokio, the company id taken from the Bokio URL, and Node 22 or later. The vendor also publishes `LLM.md`, a plain-text install brief meant to be pasted into an agent so the agent performs its own installation, which is a small but real convenience for anyone wiring this on a laptop.

## Limits Worth Recording

- **Sweden only.** Bokio is Swedish accounting and the SIE export is a Swedish format. Nothing here reads a UK or US chart of accounts.
- **No hosted endpoint.** It speaks MCP over stdio, so a browser client such as claude.ai or the ChatGPT web connector cannot attach it. It runs where the client runs.
- **One company per instance.** The company id is configuration, so an operator with several Bokio companies needs several server entries, and each one holds the token.
- **Rate limits are the vendor's.** Bokio allows 5,000 requests per company per month and 200 per minute, which is generous for questions and thin for a bulk export loop.
- **No call was executed in this pass.** Without a Bokio account and token the server cannot start, so the tool count, the read-only default and the computed tools are the published record. The npm package and the repository were read directly.
- **Recent and lightly used.** One star and a first publication in the same week as this sweep. The API surface is real; the operational history is not.

## Wiring It Up

```json
{"mcpServers": {"bokio": {
  "command": "npx",
  "args": ["-y", "bokio-mcp"],
  "env": {"BOKIO_TOKEN": "YOUR_TOKEN", "BOKIO_COMPANY_ID": "YOUR_ID"}
}}}
```

Leave `BOKIO_ALLOW_WRITES` unset for the first weeks. The questions that justify the connection are all read-only ones.

## FAQ

### Can the agent change my books?

Only if `BOKIO_ALLOW_WRITES=1` is set in the server's environment. Without it, the twenty-four write tools are not registered at all, so an agent asking for a posting tool gets a tool-not-found rather than a refusal.

### Why compute VAT instead of letting the model add it up?

Because the model is the wrong instrument for it. The computed tools run over the SIE export in code, in whole ore, and return a finished figure, which is both reproducible and checkable. A model summing journal lines is neither.

### Does it work with accounting systems other than Bokio?

No. The server wraps the Bokio API and reads Bokio's SIE export. The pattern is what generalises, not the connector.

### Which questions does it answer best?

Balances at a date, unpaid customer invoices, VAT for a period, open items, suspected duplicates, and a bank reconciliation. Each is an aggregate question where a wrong answer is expensive and where reading the underlying rows is the only way to be right.
