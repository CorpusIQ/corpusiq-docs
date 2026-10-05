---
title: "Accountable MCP - AI Bookkeeping for Startups"
description: "AI bookkeeping for startups over MCP. Read and update the books from Claude or ChatGPT, with role-based write limits, audit logging and one-click undo."
category: Finance
stars: n/a (hosted platform, accountable.im)
added: 2026-10-05
source: "mcpservers.org /all (shadowwalker2014/accountable-plugin, resolved listing)"
relevance: ★★★
tags: [finance, accounting, bookkeeping, startups, oauth, guardrails, multi-company, remote-mcp]
---

# Accountable MCP

**A startup's books behind one MCP endpoint.** Accountable is AI bookkeeping for startups: it categorises every transaction and checks every account against the bank on its own, with cash and accrual side by side. Through its MCP server, Claude, ChatGPT or Cursor can read those books and, on paid plans, change them within limits the owner sets. One connection reaches several companies, and it never moves money.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (account sign-in; scopes books:read, books:write, offline_access)
Endpoint: https://accountable.im/mcp
Clients: Claude and ChatGPT plugins, Cursor, any MCP client
Guardrails: role-based writes, owner approval for $5,000+ entries and closed-month reopen, full audit log with undo
Pricing: Free for one company (read-only), $149/mo for two companies, $49 for each extra
Built by: accountable.im
```

## Why This Matters for Operators

Founders do not want to open the accounting app to answer a finance question, and they should not need to for the agent to be useful. Accountable keeps the books current daily and closes every month against the bank, so an agent asking "what did we spend on software last quarter?" reads numbers that match what the CPA and investors will see.

The write path is deliberately narrow. Agents can preview and run changes, undo them, and read or upload documents, but writes only exist on paid plans, sensitive actions wait for a human owner, and every change is logged with the app's name. That is the shape an operator wants from an agent touching the books: useful, bounded and reversible.

## Tool Surface

The vendor documents the server as capability groups rather than a raw tool list:

| Group | What it covers | Access |
|---|---|---|
| Reports | Financial reports over the books | Read (all plans) |
| Cash and runway | Cash position and runway views | Read (all plans) |
| Transactions and bills | Transactions, bills and invoices | Read (all plans) |
| Month close | The current month's close state | Read (all plans) |
| Changes | Preview, run and undo changes; upload documents | Write (Pro and Holding) |

Exact tool identifiers are discoverable at connect time; capabilities come from the vendor's published plugin and help documentation.

## Authentication and Guardrails

OAuth only: in Accountable, Settings, "AI and agents" shows the server URL and the connection steps. The client signs the user in, the user picks the companies and what the app may do, and approves. The endpoint answers unauthenticated requests with a 401 and the published scopes `books:read books:write offline_access`.

Guardrails that always apply:

- On Free, agents can read but never change anything; writes need Pro or Holding.
- Entries of $5,000 or more, and reopening a closed month, wait for an owner.
- Every agent change is logged as the app via the connection and can be undone.
- Agents never approve changes, including their own.

## Installation

Claude Code:

```bash
claude mcp add --transport http accountable https://accountable.im/mcp
```

The hosted server also installs through the vendor's one-liner:

```bash
npx add-mcp 'https://accountable.im/mcp'
```

Cursor and other HTTP-capable clients:

```json
{
  "mcpServers": {
    "accountable": {
      "url": "https://accountable.im/mcp"
    }
  }
}
```

In Claude and ChatGPT, add the vendor's plugin (the claude-plugin and chatgpt-plugin ship in the Accountable plugin repository), which connects to the same server and bundles bookkeeping skills.

## Business Relevance

- **Founders** get cash, runway and spend answers without opening the accounting app, in the same conversation where other business questions are asked.
- **Finance leads and fractional CFOs** read reports and transactions, and stage changes with an owner approval path.
- **Operators running more than one company** reach several companies through one connection instead of one login per entity.

## Integration with CorpusIQ

The books answer "what did we spend", and CorpusIQ's connectors answer "what did it earn". Composed: Accountable reports spend, cash and runway from the ledger, while CorpusIQ reads Stripe, GA4 and the ad platforms, so an agent can put acquisition cost and revenue next to the cash position in one answer. Both surfaces run read-only from the agent's side, so the comparison never touches money or production systems.

## Limitations

- Writes require a paid plan (Pro or Holding); the free tier is read-only.
- Owner approval gates ($5,000+ entries, closed-month reopen) can pause an agent's change even when the credential allows writes.
- The published capability list is grouped; exact tool identifiers surface at connect time.
- The vendor states the service never moves money; it is a bookkeeping surface, not a payments one.

## FAQ

### Can an agent write to the books?

Only on Pro or Holding plans, only within the permissions chosen at connect time, and never past the owner gates for large entries or a closed month.

### How does one connection cover several companies?

The OAuth consent screen lets the user pick the companies the connection may reach; a connection can cover more than one.

### Can a change be reversed?

Yes. Every agent change is logged and can be undone, and agents cannot approve their own changes.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [SuperBooks MCP - Bookkeeping for Agents](/hermes/mcp/servers/external/superbooks-mcp/)
- [Median MCP - Read-Only Financial Reporting for Agents](/hermes/mcp/servers/external/median-mcp/)
- [Wafeq MCP - Accounting Books for Agents](/hermes/mcp/servers/external/wafeq-mcp/)
