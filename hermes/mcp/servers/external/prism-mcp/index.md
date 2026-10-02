---
title: "Prism MCP - Contract Deadline Reader for AI Agents"
description: "Remote MCP server that reads contracts and returns every deadline: the exact date, what happens if it is missed, and the sentence it came from. Dates are computed from the contract's own rules (notice windows, renewal terms), not estimated. Reads residential and commercial leases, mortgages, insurance policies and HOA documents. 8 tools, OAuth or API key, 3 free contracts then $0.50 per contract."
category: IP/Legal
stars: n/a (new listing)
added: 2026-09-14
source: "mcp.so feed (Sep 14 evening, submitted 7h before sweep) + vendor docs at mcp.so/clients/prism"
relevance: ★★★
tags: [contracts, legal, deadlines, lease, mortgage, insurance, hoa, document-intelligence, oauth, remote-mcp]
---

# Prism MCP

**Every deadline in a contract, before it bites.** Prism reads contracts and returns each deadline with the exact date, what happens if it is missed, and the sentence of the contract it came from. Dates are computed from the contract's own rules - notice windows, renewal terms, "60 days before the end of the term" - rather than estimated. It covers residential and commercial leases, mortgages, insurance policies and HOA documents.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (browser sign-in on first use) or a Bearer API key from the Prism billing page
Endpoint: https://prism.parad1gm.com/api/prism-mcp (401-verified live, Sep 14 2026)
Tools: 8 (read and spend tools marked separately)
Pricing: 3 free contracts per new account; $0.50 per contract, charged once when full results are delivered; credit packs of 20+
Category: IP/Legal / Document Intelligence
```

## Why This Matters for Operators

Commercial leases auto-renew, insurance policies require notice to cancel, loans have rate-reset windows - and the cost of a missed deadline is rarely just money. It is a lease that renewed for another year at a higher rent, or coverage that lapsed quietly. The information is all in the contract; nobody reads 40 pages to find the five dates that matter.

Prism turns a contract into a deadline register an assistant can hold: send the document (URL, text, PDF or photo), wait about a minute, and get structured deadlines plus risks, each one anchored to its source sentence so the claim can be checked. The most common failure mode disappears: a date that was never on a calendar.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `prism_review_contract` | Send a contract by URL, text or file (PDF or photo); returns a contractId immediately |
| `prism_get_contract` | Status and results: summary, deadlines (kind, due date, days until due, consequence, source sentence) and risks; never spends credits |
| `prism_unlock_contract` | Spend 1 credit ($0.50) to get every deadline and risk; free if already unlocked |
| `prism_upcoming_deadlines` | Open deadlines across every contract, soonest first |
| `prism_list_contracts` | Every contract in the account, and which are unlocked |
| `prism_get_account` | Credits remaining and prices |
| `prism_buy_credits` | Returns a Stripe checkout link to hand to the user; it cannot pay on its own |
| `prism_send_feedback` | Report a wrong or missing result; a person reads every message |

Sending the same document again returns the same contract and it is never charged twice. Previews, re-reads and documents Prism cannot read are free.

## Example Deadline Output

> **Notice deadline: December 31.** If you do nothing, the lease auto-renews for another 12 months at up to 5% more rent. _"...written notice of non-renewal at least 90 days before the then-current expiration date."_

## Installation

**Claude Code:**

```bash
claude mcp add --transport http prism https://prism.parad1gm.com/api/prism-mcp
```

**Claude (web and desktop):** Settings, Connectors, add a custom connector and paste the server URL.

**Cursor and other config-file clients:**

```json
{
  "mcpServers": {
    "prism": { "url": "https://prism.parad1gm.com/api/prism-mcp" }
  }
}
```

Without OAuth: create an API key on the Prism billing page and send it as a Bearer token.

## Business Relevance

- **Business owners** keep a live register of lease, insurance and loan deadlines instead of a folder of PDFs.
- **Property managers and multi-site operators** track deadlines across many leases in one query, soonest first.
- **Founders signing their first commercial lease** get the renewal and notice traps extracted before they sign.
- **Ops leads** route "what is due in the next 60 days" to the assistant instead of to a spreadsheet someone maintains by hand.

## Integration with CorpusIQ

Prism extracts obligations; CorpusIQ supplies the numbers that decide what to do about them. Connect CorpusIQ and the same assistant reads revenue, orders, payroll and pipeline data (Stripe, Shopify, QuickBooks, HubSpot, GA4) with source-cited answers. That turns a deadline alert into a decision: a renewal decision priced against actual store performance, an insurance review timed to the quarter the data says is tightest. Both are read-oriented flows: Prism reads contracts, CorpusIQ reads business systems.

## Limitations

- **New listing** with no public track record at catalog time.
- **US document types** are the documented scope (leases, mortgages, insurance, HOA); other contract families are not claimed.
- **Credit-based pricing**: $0.50 per contract after the 3 free ones, and the buy-credits tool can only hand you a checkout link.
- **A contract read takes about a minute**; the flow is submit, poll, unlock.
- **Not legal advice** - it extracts deadlines and risks, not a legal opinion.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
