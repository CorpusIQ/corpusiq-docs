---
title: "AuraVMS MCP - SMB Procurement and RFQ Workflows"
description: "Send RFQs, collect supplier quotes with L1-L3 ranking and place purchase orders from Claude, ChatGPT or any MCP client."
category: Business Operations
stars: n/a (new listing)
added: 2026-10-06
source: "mcpservers.org /all"
relevance: ★★
tags: [procurement, rfq, suppliers, purchase-orders, operations, smb, oauth, remote-mcp]
---

# AuraVMS MCP

**Remote MCP server (Streamable HTTP, OAuth)** - procurement for small businesses, worked from the chat. AuraVMS runs the full sourcing loop - define a requirement, invite your suppliers, collect private quotes, compare with automatic L1-L3 ranking and place the purchase order - and its AI connector exposes every step as an MCP tool. It is listed in the Claude connectors directory and connects to ChatGPT and Muse the same way.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (Claude, ChatGPT, Muse connectors) with a scoped workspace key
Endpoint: https://mcp.auravms.com/mcp
Tools: 11 (suppliers, RFQs, quotes, orders)
Pricing: Free trial, no credit card, 15-minute setup; paid plans with annual billing discounts
Built by: AuraVMS
Directory: claude.ai/directory/auravms
```

## Why This Matters for Operators

Small-business procurement rarely lives in a system. A requirement goes out to five suppliers by email, quotes come back as PDFs, spreadsheets and WhatsApp messages, and the comparison happens in someone's head the morning of the award. AuraVMS standardises the middle: suppliers quote through a private link with no account, responses arrive lined up by price, MOQ, lead time and terms, and the award becomes an order record.

**Your team adopts a system; your suppliers only click a link.** That is the adoption trick: no supplier portal training, no external-user rollout. The connector then puts the whole thing in chat - "compare the quotes on our Q4 production materials RFQ and tell me the cheapest supplier for each item", "remind every supplier who hasn't quoted", "place the order for the M8 bolts with the lowest quote".

Tools that act outside the workspace are labelled as such: anything that emails a supplier (`send_rfq`, `send_reminders`, `place_order`) can be set to require approval in the client before it runs, and the connector cannot touch billing, team members or organization settings.

## Tools & Capabilities

| Tool | What it does | Type |
|---|---|---|
| `list_suppliers` / `add_supplier` | Search or list suppliers; add one (existing emails reused, not duplicated) | Read / Write |
| `list_rfqs` / `get_rfq` | List RFQs by status or search; show line items and which suppliers responded | Read |
| `get_quotes` | Compare supplier quotes for a line item with L1/L2/L3 ranking | Read |
| `create_rfq_draft` | Save an RFQ draft with items and invited suppliers; nobody is emailed | Write |
| `send_rfq` | Email a draft RFQ to its suppliers | Emails suppliers |
| `send_reminders` | Remind suppliers who have not quoted (once per RFQ per day) | Emails suppliers |
| `place_order` | Award a line item to a quote and email the purchase order | Emails suppliers |
| `close_rfq` | Close an RFQ to further quotes (cannot be undone) | Irreversible |
| `request_feature` | Send feedback to the AuraVMS team with account context | Write |

## Installation

Connect from the assistant's connector settings: in Claude, open Settings, Connectors, search for AuraVMS and click Connect; in ChatGPT, enable developer mode and add the server URL as an MCP app; in Muse, add it under Connectors. Sign in to AuraVMS and click Allow.

```bash
claude mcp add --transport http auravms https://mcp.auravms.com/mcp
```

AuraVMS account with an active plan or trial required.

## Configuration

The connector is added through each client's connector flow with the server URL above; OAuth handles the rest. To review each outbound tool before it runs, set AuraVMS to **Needs approval** under Settings, Connectors in Claude. Revoke access any time under Settings, API Keys in AuraVMS (the key is named after the assistant).

## Business Relevance

- **Operations leads** run repeat sourcing without rebuilding a comparison spreadsheet per RFQ.
- **Purchasing managers** get supplier history - response rates, delivery and quality - next to the pick list.
- **Manufacturing and construction SMBs** standardise quotes for materials, safety gear, packaging or components.
- **Finance-adjacent owners** see the award trail: original quote, negotiated terms, order, audit log.

## Integration with CorpusIQ

Procurement is spend, and spend is the other half of the operating picture. CorpusIQ reads QuickBooks, Stripe and the books' systems read-only, so an operator can reconcile what was ordered against what was paid, check a supplier's billing against the awarded quote, and bring purchase history into the same conversation as revenue and cash data. AuraVMS runs the sourcing workflow; CorpusIQ is where the financials it feeds get checked.

## Limitations

- Brand new listing: no track record from this catalog yet.
- Outbound tools email real suppliers: use the client's approval setting for `send_rfq`, `send_reminders` and `place_order`.
- `close_rfq` cannot be undone.
- The connector cannot change billing, team members or organization settings by design.
- Supplier side is link-based; suppliers never get accounts inside your workspace.

## FAQ

### Can the assistant contact suppliers without my review?

Only through tools labelled as emailing suppliers, and you can set them to require approval in the client before each run. Nothing sends silently unless you allow it.

### Do suppliers need an AuraVMS account?

No. Each supplier gets a private instant-access link by email or WhatsApp and quotes from mobile or desktop; they never see competing bids.

### Does it place orders?

`place_order` awards a line item to a quote and emails the purchase order, with the original and negotiated terms recorded. Payment remains in your own systems.

### What does it cost?

Free trial with no credit card and 15-minute setup; paid plans are per team with annual billing discounts.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
