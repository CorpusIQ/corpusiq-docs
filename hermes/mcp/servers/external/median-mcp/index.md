---
title: Median MCP - Read-Only Financial Reporting for Agents
description: "Read-only MCP server giving an AI agent plain-language access to a Median customer's ledger, financial reports and transactions."
category: Finance
stars: n/a (hosted service, medianfi.com)
added: 2026-10-01
source: "mcpservers.org /all (medianfi-com-claude-cowork)"
relevance: ★★★
tags: [finance, accounting, bookkeeping, financial-reports, pnl, ledger, remote-mcp]
---

# Median MCP

**Financials without the dashboard tour.** Median keeps a business's books and exposes them to Claude through a read-only remote MCP server. An operator asks for a P&L for the last quarter or a list of transactions in plain language and gets the number back, without opening the accounting tool.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth sign-in to the Median account
Endpoint: https://medianfi.com/mcp
Tools: read-only (list transactions, get P&L reports, query financial data)
Pricing: requires a Median account
Category: Finance
Built by: Median
```

## Why This Matters for Operators

Accounting software assumes the person with the question knows where to click. Median's MCP server flips that: the question goes to the agent, the agent reads the ledger, and the answer comes back in the conversation where the operator already works. The connection is read-only, so nothing an agent does can change the books.

The freshness point is the one that matters most day to day. Month-end reports are stale by the time they are published; Median posts new activity every business day, so what the agent reads is the current picture rather than the closed-period snapshot. For a founder who needs a revenue or expense figure mid-meeting, that is the difference between an answer and a follow-up email.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `get_pl_report` | Pull a profit-and-loss report for a date range |
| transaction reads | List and query transactions in the account |
| report queries | Ask plain-language questions over the financial data the account exposes |

The directory listing exposed the P&L report call by name and describes the rest as read-only financial queries against the account. The guide describes capabilities rather than inventing tool identifiers that the public listing did not publish.

## Installation

```
claude mcp add --transport http median https://medianfi.com/mcp
```

Sign in with the Median account when prompted; the server authenticates with OAuth and connects read-only.

## Configuration

```json
{
  "mcpServers": {
    "median": {
      "type": "http",
      "url": "https://medianfi.com/mcp"
    }
  }
}
```

## Business Relevance

- **Founders and operators** can ask for a P&L or a transaction list without leaving the conversation they are already in.
- **Finance and bookkeeping teams** can answer ad-hoc questions from a current ledger rather than waiting on a report run.
- **Advisors and fractional CFOs** can pull client figures through the same read-only surface, with no write access to risk.
- **AI agents** get a grounded financial source they can query in natural language and cite back to the account.

## Integration with CorpusIQ

Median supplies the accounting truth; CorpusIQ's connector set supplies the operating data around it. An agent can read the revenue figure from Median, then pull the customer, pipeline or marketing numbers from CorpusIQ and answer the operator's question with both sides of the business in one response - the closes figure and the work that produced it, composed in a single workflow.

## Limitations

- Read-only by design: agents can query financial data but cannot post, edit or reconcile anything.
- Requires an active Median account with a connected ledger; there is nothing to read without one.
- The public listing exposes the P&L tool by name and describes the rest at a capabilities level, so the exact tool set is narrower than the marketing page implies.
- Financial data is sensitive; the read-only scope limits the blast radius but the token still carries the user's own access to the account.

## FAQ

### What does the Median MCP server do?

It gives an AI agent read-only access to a Median customer's ledger, financial reports and transactions, so plain-language finance questions can be answered with current account data.

### Can an agent change the books through Median MCP?

No. The connection is read-only; agents can query and report but cannot write to the account.

### Does it need an API key?

No. It authenticates with OAuth against the Median account.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ](https://corpusiq.io) - 40+ business data connectors for AI agents
