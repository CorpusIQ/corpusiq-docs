---
title: Candor Finance MCP
description: Personal finance workspace for AI agents — accounts, budgets, goals and investments with evidence behind every number, read-only toward banks with OAuth 2.1.
category: Finance
stars: n/a (new listing)
added: 2026-08-17
source: mcpservers.org
relevance: ★★
tags: [personal-finance, budgeting, investments, evidence-trail, read-only, oauth, finance-workspace, remote-mcp]
---

# Candor Finance MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1)** — Candor gives an AI agent an organized personal-finance workspace: accounts, balances, transactions, recurring items, budgets, goals, holdings, and debts — every number carrying freshness, coverage, and evidence handles. Registered as `money.candor/candor-finance` on the official MCP Registry, served at `api.candor.money/mcp`.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 with dynamic client registration
Endpoint: https://api.candor.money/mcp
Tools: workspace schema + bounded record reads with progressive disclosure; no money-moving tools
Pricing: included in a Candor subscription (pricing shown before checkout)
Category: Finance
Built by: Candor (candor.money)
```

## Why This Matters for Operators

Personal books are where AI finance tools usually fail: they either hallucinate balances or demand read-write access to accounts nobody should hand over. Candor's design attacks both. The connection is read-only toward banks, bank credentials never pass through the agent, and every financial read records a concise reason.

**Evidence handles are the core mechanism**: each record carries freshness, coverage, and an evidence handle so the agent can distinguish what the records establish from what still needs judgment. Approved workspace changes stay inside Candor; outside financial actions remain under the human's control. The agent gets judgment support, not spending power.

## Tools & Capabilities

The server uses progressive disclosure: the agent opens the workspace with `candor_open`, then asks for the schema or the bounded records a task needs, keeping large or unrelated financial data out of the conversation. Domain coverage published by the vendor:

| Area | Purpose |
|---|---|
| Accounts & balances | Normalized accounts with freshness and coverage handles |
| Transactions & recurring items | Spending history with duplicate-charge investigation support |
| Budgets & goals | Approved budget maintenance and goal tracking |
| Holdings, debts, notes | Investment positions, debts, and factual change records |
| Prior financial-impact records | Follow-through history with evidence |

## Installation

```bash
claude mcp add candor-finance --transport http https://api.candor.money/mcp
```

The client handles the OAuth challenge; you sign in and approve the client on Candor's secure page. A CLI route (`candor setup`) exists for non-MCP workflows.

## Configuration

```json
{
  "mcpServers": {
    "candor-finance": {
      "type": "http",
      "url": "https://api.candor.money/mcp"
    }
  }
}
```

OAuth 2.1 with dynamic client registration — you approve each client on Candor's page, and bank credentials, access tokens, full account numbers, and verification codes never belong in chat.

## Business Relevance

- **Founders** get a personal-books workspace their agent can read without ever holding spending power.
- **Operators** get budget and goal tracking where the agent checks coverage before answering instead of inventing numbers.
- **Finance-adjacent professionals** get a review-ready trail: every read is logged and access is revocable anytime.
- **Anyone burned by AI finance errors** gets a model where the answer and its evidence ship together.

## Integration with CorpusIQ

Candor occupies the personal side of the money picture that CorpusIQ's business connectors leave open. Operators can run business books in QuickBooks and Stripe while Candor holds the personal workspace, and the agent keeps the two separated by design. The evidence-handle pattern also mirrors CorpusIQ's data accuracy contract — treat only returned fields as verified — so a Candor-connected agent can follow the same provenance discipline across personal and business financial data without retraining.

## Limitations

- Brand new — no track record yet; listing appeared August 17, 2026.
- Personal finance only — not a business accounting system.
- Read-only toward banks by design; no payments, transfers, or brokerage orders.
- Requires a Candor subscription; per-seat pricing is shown at checkout, not in the docs.
- OAuth flow needs an MCP client that supports remote Streamable HTTP with OAuth challenges.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
