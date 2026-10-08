---
title: "Orla MCP - Finance Back Office and Agent Payments"
description: "Hosted MCP server over Orla: read accounts, transactions, budgets and reports and record reversible bookings from chat, plus a separate agent door whose payments wait for a human signature."
category: Finance
stars: n/a (new listing)
added: 2026-10-08
source: "mcpservers.org /all (October 8, 2026 night sweep)"
relevance: ★★★
tags: [finance, bookkeeping, accounting, payments, budgets, reports, agents]
---

# Orla MCP

**Hosted MCP server that puts your books in your AI assistant, with the signatures kept on the human side.** The personal connection reads accounts, transactions, budgets and reports, and records reversible bookings; by design it cannot move money. A separate agent door mints an agent with its own wallet and hard ceilings, where every payment proposal waits for a person to sign.

```
Server type: Remote (Streamable HTTP - personal door at https://app.orla.finance/api/mcp/personal; agent door at https://app.orla.finance/api/mcp)
Auth: browser sign-in and Orla consent page (per-client revocation; card numbers and IBANs masked by default)
Tools: read accounts, transactions, budgets, net worth, settle-up, the assistant's reports and the approval queue; record transactions, categories, budgets and shared expenses
Pricing: free plan; paid plans from $25/mo; personal connections take no agent seat
Category: Finance
Built by: Orla
```

## Why This Matters for Operators

Finance is where agent access should be most conservative, and Orla writes the rule into the code: "It reads and records. It does not move money." The personal connection's tool list has no payment tools at all, and they are refused again at the endpoint by name. What it can do is genuinely useful - reconcile what you spent by month, read the cash forecast and which bills are due first, settle up a shared space, book yesterday's expense with its category - and everything it writes is reversible with an activity trail. An agent that actually needs to pay is a deliberately different connection: its own wallet whose balance is the whole budget, per-request and per-day ceilings that start closed, payee lists only a person edits, and a payment that is never reported as sent without a reference.

## Tools & Capabilities

| Area | What the connection can do |
|---|---|
| Read | accounts and balances, transactions (with uncategorised filters), budgets and net worth, who owes whom plus the shortest settling transfers, cash forecast, owed and owing, bills due, VAT and tax-year reports, approval queue (read-only), fraud findings |
| Record | book an income or expense with category and payee, correct a category, payee or note, set a budget amount, add a shared expense |
| Agent door (separate) | propose payments that wait for a signature, wallet transfers and x402 purchases inside ceilings, agent history and keys under the agent's own name |

## Installation

```bash
claude mcp add --transport http orla https://app.orla.finance/api/mcp/personal
```

```json
{
  "mcpServers": {
    "orla": {
      "url": "https://app.orla.finance/api/mcp/personal"
    }
  }
}
```

For clients that only speak stdio, the orla-cli package runs as a bridge: `npx -y orla-cli mcp`.

## Configuration

Sign-in opens Orla's own consent page where you tick which spaces the connection may reach; one row in the app revokes every client at once. Reading is unmetered, and recordings come out of the plan's monthly allowance of agent writes. Live probe: POST initialize on the agent door returns 401 "Authorization required", confirming the endpoint is live and auth-gated.

## Example Prompts

- "What did I spend on hosting last quarter, by month?"
- "What does the cash forecast say, and which bills are due first?"
- "Who owes whom after the trip, and what settles it?"
- "Book yesterday's 40 EUR taxi to Transport."

## Integration with CorpusIQ

CorpusIQ keeps revenue, orders and customer numbers consistent across AI clients, read-only and cited. Orla covers the other side of the ledger - spend, budgets and bills - so a single conversation can combine "what came in" with "what goes out" without opening two dashboards.

## Limitations

- The personal connection cannot pay, transfer or swap - payment tools are not on its list, by design.
- An agent that pays must be set up separately in the Orla app with its own wallet and ceilings.
- Lists stop at 200 rows and say so; some verdicts (fraud findings) are reserved to a person.
- New listing - the MCP interface is documented in Orla's skill file at orla.finance/skill.md.

## FAQ

### Can the assistant move my money through this?

No. Payments, transfers, swaps and card details are not in the tool list a personal connection receives, and are refused again at the endpoint if asked for by name.

### Does connecting Claude or Cursor use a paid seat?

No. A personal connection is not an agent, takes no seat and works on the free plan; it shares the same limits any human user has.

### What can it write?

Books and corrections: booking a transaction, categorising one, setting a budget, adding a shared expense. Everything is reversible and appears in the activity trail.

## See Also

- [Booksmate MCP - Invoice Fetching and Spend Reports](/hermes/mcp/servers/external/booksmate-mcp/)
- [Pocket Invoice MCP - Invoices and Estimates from Chat](/hermes/mcp/servers/external/pocket-invoice-mcp/)
- [Accountable MCP - AI Bookkeeping for Startups](/hermes/mcp/servers/external/accountable-mcp/)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
