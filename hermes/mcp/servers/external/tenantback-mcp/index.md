---
title: "Tenantback MCP - CAM Reconciliation Audit"
description: "Tenantback audits a landlord's CAM reconciliation against your lease, cites the clause behind every overcharge and drafts the dispute."
category: Finance
stars: n/a (no public repo)
added: 2026-10-21
source: "mcp.so /feed page 1 (card posted 2026-10-21T06:51:31Z)"
relevance: ★★★
tags: [commercial-real-estate, lease-audit, cam-reconciliation, property-management, expense-recovery, finance-ops, remote-mcp, a2a]
---

# Tenantback MCP

**The landlord sends an operating expense reconciliation once a year and the tenant has 30 to 90 days to object. Tenantback reads the lease, finds the overcharges clause by clause, and hands back the arithmetic the tenant needs to object before the window closes.**

```
Server type: Remote (Streamable HTTP) at https://tenantback.com/mcp
Auth: none for audits; a workspace API key (Authorization: Bearer) adds portfolio tools
Live check: POST initialize returned HTTP 200 (serverInfo tenantback 1.0.0, protocol 2025-06-18, tools capability)
Tools: 2 without a key, 9 more with a workspace key
Pricing: audits free; recovery plan 25% of money actually recovered; portfolio $49 per location per month plus 12% of recoveries
Vendor: Tenantback (tenantback.com)
```

## Why This Matters for Operators

A commercial lease is one of the largest recurring costs a multi-location business carries, and the annual CAM true-up is the one bill nobody checks. The tenant gets a statement of common area maintenance, insurance and tax expense, a pro-rata share, and a balance due, usually with a short objection window attached. Reading it properly means holding the lease's caps, exclusions and denominator rules in your head while checking line items against them, which is why most tenants pay what the landlord computed.

The three errors that recover real money are structural, not arithmetic. A denominator that shrank after an anchor tenant left inflates every tenant's share. A management fee charged on taxes and insurance the lease excludes from the fee base bills you twice for the same cost. A gross-up applied below the occupancy threshold charges you for vacancy. Each is visible only when the lease language and the statement line sit side by side.

Tenantback is built for that comparison and nothing else, which is why it is worth a catalog entry while generic document tools are not. Every finding quotes the lease word for word, verified against the source page, shows the statement line, and shows the calculation. The model reads, the code computes, and the two are kept separate on purpose.

## What It Actually Does

The audit checks nine things: pro-rata share and its denominator, CAM caps on controllable costs whether cumulative or non-cumulative, administrative and management fee rate and base, excluded costs the lease lists (capital repairs and replacements, landlord overhead, leasing costs, insurance deductibles), gross-up above the occupancy threshold, year-over-year variance, the balance due, and late statement delivery.

Two tools work with no account at all. `audit_cam_reconciliation` takes the lease text and the reconciliation text you read from the user's files (or HTTPS links to them) plus the user's work email; `get_audit_result` returns the findings, citations and arithmetic as JSON.

A workspace key adds the recovery workflow: `portfolio_overview`, `list_locations`, `get_lease_abstract`, `search_lease_documents`, `list_findings`, `list_deadlines`, `get_statement`, `request_audit`, `get_audit_request` and `draft_dispute`. The last one drafts only. Nothing reaches a landlord without a person approving it, and every action lands in an append-only audit log.

There is an A2A endpoint as well, agent card at `/.well-known/agent-card.json`, for agent-to-agent handoff, and an email path: forward a lease and a reconciliation to audit@tenantback.com and the findings come back by email, subject to DMARC or aligned DKIM on the sender's domain.

## Installation

```bash
claude mcp add tenantback --transport http https://tenantback.com/mcp
```

No key is needed for the audit tools, so the connector works in ChatGPT or Claude as a custom connector on first use.

## Configuration

```json
{
  "mcpServers": {
    "tenantback": {
      "type": "http",
      "url": "https://tenantback.com/mcp"
    }
  }
}
```

With a workspace key, add `"headers": {"Authorization": "Bearer <key>"}` and the portfolio tools appear.

## Business Relevance

- **Multi-location retail, restaurant and clinic operators** recover overcharges on every location's statement, not just the one someone had time to read.
- **Controllers and finance teams** get a findings list with clause citations and arithmetic they can attach to a dispute instead of retyping a spreadsheet.
- **Property and lease administrators** track objection deadlines across the portfolio, which is the part that gets missed.
- **CFOs** see the recurring overcharge pattern across landlords rather than a single one-off variance.
- **CPAs and tenant reps** have a partner path for running audits on client leases.

## Integration with CorpusIQ

QuickBooks, Xero and Stripe connectors carry what the business actually paid; Tenantback carries what the lease says it should have paid. Ask CorpusIQ for the CAM expense lines and the payment history, hand the reconciliation and the lease to Tenantback, and the difference between the two is the recoverable amount. Pair the findings with the Drive connector to keep the lease, the statement and the findings report in one folder, and with Calendar to put the objection deadline on the operator's calendar at the moment the finding is produced.

The composition matters because each side holds half the answer. CorpusIQ cannot read a lease clause; Tenantback has no view of what was actually booked and paid. Together the question "did we overpay this landlord" becomes answerable in one conversation.

## Limitations

- Brand new, no public track record. The free audit is the evaluation path.
- Audits are free but capped: 5 per sender per day, a daily cap on new free workspaces, 10 files per request and 20 MB per file.
- The recovery model is contingency pricing (25% of what is recovered), so the cost scales with the win rather than being a flat subscription.
- The free audit tools need the lease and statement text supplied by the calling agent, and the workspace tools need a key minted in the product.
- Scope is commercial CAM and operating expense reconciliations. It is not a general lease administration system, and it does not contact a landlord without human approval.

## FAQ

### Is this just a document reader with a prompt?

No. Both steps exist but stay separate: the model reads the lease and locates the clauses, and the arithmetic is computed in code, so a finding either balances against the statement or it does not. The output carries the clause, the statement line and the calculation together.

### What does it cost to try?

Nothing. Audits are free with no card, up to 5 per sender per day. Paid recovery work is 25% of the money actually recovered, and the portfolio plan is $49 per location per month plus 12% of recoveries.

### Can an agent send the dispute to the landlord?

Not by default. `draft_dispute` produces the draft and a person approves sending. Disputes, follow-ups and recorded recoveries all sit behind human approval with an append-only log.

### Which businesses actually benefit?

Commercial tenants with more than one location, where statements arrive annually and the objection windows overlap. A single small lease is usually cheaper to eyeball than to onboard.

## See Also

- [Hercules Property MCP](/hermes/mcp/servers/external/hercules-property-mcp)
- [Dutch Property Context MCP](/hermes/mcp/servers/external/dutch-property-context)
- [fynk MCP - Contract Lifecycle Management for Agents](/hermes/mcp/servers/external/fynk-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
