---
title: "ATLASS OS MCP - CorpusIQ Docs"
description: Field-service business platform with a native MCP surface — CRM, scheduling, double-entry books, GST, payroll, payables, and inventory as 58 scoped, audited agent tools
category: ERP
stars: n/a (no public repo)
added: 2026-08-12
source: mcpservers.org
relevance: ★★★
tags: [erp, field-service, construction, accounting, crm, scheduling, payroll, double-entry, remote-mcp]
---

# ATLASS OS MCP

**Hosted MCP surface for ATLASS OS** — a business platform for construction trades (CRM, scheduling, jobs, and real double-entry books in one ledger) with a native MCP surface: 58 working tools, 35 write-capable, 32 permission scopes, machine-censused as of August 10, 2026. Tokens are minted in-app with scoped permissions, every financial write posts as balanced double-entry on an append-only audit log, and there is deliberately no payment rail — nothing in ATLASS, agent or human, moves a dollar. Built by a roofing company owner who runs his real business on it every day.

```
Server type: Remote (hosted MCP surface)
Auth: In-app token minting, 32 permission scopes
Endpoint: https://app.atlass-os.com/mcp
Tools: 58 (35 write-capable) as of the Aug 10, 2026 census
Rate limit: 120 reads + 20 writes per minute per token
Category: ERP / Field Service / Construction
Stage: Founding-stage rollout in Alberta, Canada (founding@atlass-os.com)
```

## Why This Matters for Operators

Every field-service operator runs the same stack split: CRM here, scheduling there, books somewhere else — and the agent tooling glued on top can only read one slice at a time. ATLASS OS is the first field-service platform to ship a native MCP surface where the agent that books the job is the same agent that watches the invoice get paid — one ledger, nothing to sync, every action audited in one place. The security shape is the differentiator: agents can only hold permissions the token minter already holds, permissions are re-checked on every call, and the money math (balanced entries, books locks, audit records, duplicate guards) is enforced server-side, not by an env var on a process you're trusted to run. As of August 2026, no major field-service platform ships an official MCP surface — ATLASS checked, with citations.

## Tools & Capabilities

| Area | What the agent can do |
|---|---|
| Customers & leads | Intake a new customer (contact, job site, project) in one call; list, search, qualify |
| Scheduling | Read the crew calendar and slot work |
| Inbox & outreach | Claim, reply, close; send outreach that logs itself |
| Payments & receivables | Record payments against invoices; see open AR |
| Banking | Import feeds, categorize, reconcile, finalize with books lock; transfers, deposits, NSF, cheque voids, petty cash, opening balances |
| GST (Canada) | Prepare and file the return period |
| Payables | Record and pay bills, vendor credits, apply credits |
| Payroll | Advances, remittance filing, pay schedules |
| Products & inventory | Catalog, inventory adjustments, purchase orders created and received |

Every write is tenant-scoped; every financial write posts as balanced double-entry with a record on an append-only audit log.

## Installation

There is no developer account, no OAuth playground, and no local server process. Create a token in-app with the permission scopes your agent needs, then point any MCP-capable client at the hosted surface:

```json
{
  "mcpServers": {
    "atlass-os": {
      "type": "http",
      "url": "https://app.atlass-os.com/mcp"
    }
  }
}
```

You bring your own AI subscription; ATLASS charges no per-conversation AI fee.

## Business Relevance

- **Construction and trade operators** get one audited ledger — the agent that books the job watches the invoice get paid, with CRM, scheduling, and books in the same surface
- **Bookkeepers and fractional CFOs** get scoped agents: grant the books and nothing else; reads without writes; revoke instantly in-app
- **Owners who self-administer** get server-enforced money math — duplicate guards on bill payments, bank imports, and tax filings that no agent prompt can bypass
- **Operators outgrowing QuickBooks Desktop** get a full migration target (books + CRM + field ops on one MCP surface) — Intuit ships no MCP for Desktop

## Integration with CorpusIQ

ATLASS OS and CorpusIQ attack the same operator problem from opposite ends, and they compose cleanly. CorpusIQ connects AI agents to 40+ existing business systems (QuickBooks Online, Shopify, Stripe, HubSpot) read-only across a whole stack; ATLASS is a single all-in-one ledger where the agent can also *write* — under scoped permissions and an append-only audit trail. An operator on ATLASS still sells on Shopify or takes payments on Stripe, and CorpusIQ covers those edges read-only while ATLASS owns the books, the crews, and the jobs. For multi-entity operators, CorpusIQ's connectors aggregate the external revenue and marketing data that feeds the ATLASS ledger's audit trail — the composition is the closest thing today to an agent-run field-service back office with an evidence chain a CFO can defend.

## Limitations

- Founding-stage rollout in Alberta, Canada — not yet broadly available elsewhere
- Construction/field-service vertical — not a general-purpose ERP
- Rate-limited per token (120 reads / 20 writes per minute)
- No payment rail by design — payments are recorded, not moved; you still need a bank/processor
- No public repository; the tool surface is documented on their own census page

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
