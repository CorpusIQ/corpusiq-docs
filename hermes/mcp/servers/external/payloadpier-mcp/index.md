---
title: "PayloadPier MCP - Supplier Price Drift for Purchasing"
description: "Purchasing MCP server: compare two supplier price-list snapshots by exact SKU and catch unit-cost rises hidden by pack-size or minimum-order changes."
category: "Procurement / Finance"
stars: n/a (new listing)
added: 2026-10-18
source: "chatmcp/mcpso issue #5685 + mcpservers.org /all (October 18, 2026 night sweep)"
relevance: ★★★
tags: [procurement, purchasing, supplier-pricing, cogs, unit-cost, margin, finance, api-key, remote-mcp]
last_updated: "2026-10-24"
---

# PayloadPier MCP

**A supplier price-list comparator for purchasing teams. PayloadPier takes two snapshots of the same supplier price file and compares them by exact SKU, so the change an agent reports is the change in unit cost, not the change in the case price. A case that stays at $120 while its pack size drops from 12 units to 10 is a 20 percent unit-cost increase, and that is the number the tool returns.**

```
Server type: Hosted (Streamable HTTP, JSON-RPC 2.0)
Endpoint: https://payloadpier.com/api/mcp
Auth: Scoped API key in the Authorization header (Bearer); OAuth client discovery still being verified
Tools: 4 - compare_supplier_prices (billable), get_account_balance, get_referral_link, claim_referral
Pricing: One included comparison unit, then $0.25 prepaid per comparison
Docs: payloadpier.com/docs/mcp; discovery manifest payloadpier.com/api/discovery; registry manifest payloadpier.com/server.json
Publisher: PayloadPier (payloadpier.com); integration examples github.com/DomicoSupply/payloadpier-examples
Listing: chatmcp/mcpso issue #5685 and the mcpservers.org entry (October 18, 2026)
```

## Why This Matters for Operators

Supplier price files are reissued constantly, and they are built to be read by people who already know the product. A line keeps its SKU and its headline cost while the case count, the minimum order or the pack configuration quietly changes underneath. The number that matters for margin is cost per usable unit, and it is the number nobody re-derives line by line across a few thousand rows.

That is a reading task an agent can do correctly if it is given the right comparison rule, and it is exactly the task a chat assistant gets wrong when it is handed two spreadsheets and asked to eyeball them. PayloadPier puts the rule in the tool: exact SKU matching, pack-size normalisation, minimum-order differences, and the margin impact of the delta. The output is a priced change, not a narrative.

## What You Can Do Today

| Capability | What it does |
|---|---|
| Compare two price snapshots | `compare_supplier_prices` takes an `operation_id` and a comparison object with `old_rows` and `new_rows` in the documented JSON shape |
| Catch hidden increases | Detects unit-cost increases caused by pack-size changes, not just headline price moves |
| Read minimum-order effects | Reports minimum-order differences alongside the unit-cost change |
| Quantify margin impact | Optionally reports the gross-margin effect of the change on a supplied margin |
| Idempotent billing | A repeated `operation_id` returns a usage reference instead of a second charge |
| Check funding first | `get_account_balance` reads prepaid balance and active subscription units before a paid run |

## Business Relevance

- **Purchasing and finance teams** get a repeatable read on every price-file revision instead of a spot check on the lines someone happened to open
- **COGS drift is caught in the file, not in the quarterly close:** a 20 percent unit-cost rise behind an unchanged case price is the kind of change that survives several invoice cycles unnoticed
- **Agents answer a cost question with a computed figure:** the comparison runs server-side, so the assistant reports the served result rather than estimating from a pasted table
- **Scoped keys:** the supplier-price scope is separate from account-read and referrals, and tool arguments never carry the key
- **Cheap per run:** one included unit, then $0.25 per comparison, which is priced for a monthly price-file review rather than a continuous loop

## Integration with CorpusIQ

The supplier file is one side of a margin question; the other side is what was actually bought. CorpusIQ's connectors cover the accounting and commerce systems where that truth lives, so an agent can read purchase history from QuickBooks or a commerce platform over read-only tools, run the price-file comparison through PayloadPier, and put the two together in one answer: what the supplier changed, and what it is about to cost.

## Limitations

- **You supply the snapshots:** PayloadPier compares files you provide in its documented row shape; it is not a supplier catalogue and it does not fetch price lists for you
- **Paid after the included unit:** comparisons draw prepaid balance at $0.25 each; the free-path is the balance check, not the comparison
- **API key first:** the documented route is a scoped API key in the header, and OAuth client discovery is described by the vendor as still being verified
- **Narrow surface:** four tools, one of which does the work; there is no supplier directory, no PO workflow and no invoice matching
- **New listing:** published in October 2026; treat the tool surface as current for that revision

## FAQ

### Does it read supplier PDFs or spreadsheets directly?

No. The tool takes structured rows in its documented JSON shape (`old_rows`, `new_rows`), so the extraction step happens in your client or your own pipeline before the comparison runs.

### What stops a retried call from being billed twice?

The `operation_id` you pass is the idempotency key. A recorded repeat returns a usage reference without a second charge, though the vendor notes it does not replay the stored result, so preserve the operation id after a timeout rather than inventing a new one.
