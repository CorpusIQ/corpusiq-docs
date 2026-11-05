---
title: "Connect Amazon Seller to Claude via MCP - Orders"
description: "Connect Amazon Seller Central to Claude through CorpusIQ MCP. Ask about orders, inventory and settlements in plain English, read-only."
category: Claude Integrations
tags: ["connect Amazon Seller to Claude", "Amazon Seller Central Claude", "MCP Amazon connector", "Amazon data to Claude", "AI for marketplace sellers", "CorpusIQ MCP"]
last_updated: "2026-11-04"
canonical: https://www.corpusiq.io/docs/connect-amazon-seller-to-claude
robots: index,follow
---

# How to Connect Amazon Seller to Claude with CorpusIQ MCP

Amazon Seller Central holds your marketplace orders, your fulfilment inventory, and the financial events behind your payouts. The reporting is powerful and slow: one report, one date range, one marketplace at a time. By the time the export lands you have forgotten the question.

Connecting Amazon Seller to Claude through CorpusIQ MCP gives you a faster way to ask. Authorize read-only access once, and the next question is answered from live marketplace data with the period and the marketplace named.

### Why Connect Amazon Seller to Claude?

- **Orders without a report.** "How many units did we sell this month, by marketplace?" One question instead of a scheduled export.
- **Stockouts before they happen.** "Which products are at risk of a stockout based on recent sales velocity?" The answer needs orders and inventory together, which is exactly what one export does not give you.
- **Settlement clarity.** "What settlement amount is expected from the current payout period?" Financial events are readable instead of buried.
- **Marketplace comparison.** "Which marketplace is growing fastest, and which is declining?" Multi-marketplace questions become answerable because the account's participations are known.
- **The cross-source question that matters.** "What is our true margin per unit once Amazon fees, freight, and cost of goods are included?" Amazon data beside accounting and order data.
- **Read-only by scope.** The connector reads. It never changes a listing, adjusts inventory, or touches a settlement.

### How It Works

1. **Connect Amazon Seller to CorpusIQ** by authorizing read-only access to your Seller Central account.
2. **Connect CorpusIQ to Claude** as an MCP server, using the config block from your CorpusIQ account settings.
3. **CorpusIQ retrieves** orders, sales metrics, fulfilment inventory, financial events, and marketplace participations for the window you ask about.
4. **Claude answers** from that retrieved content, naming the marketplace and the date range.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log in and open **Connectors**.
2. Select **Amazon Seller**.
3. Authorize read-only access to your Seller Central account and confirm the marketplaces you want covered.
4. Copy the MCP config block shown under **Settings, Integrations, Claude Desktop**.

**In Claude Desktop**

5. Open **Settings, Developer, Edit Config**. This opens `claude_desktop_config.json`.
6. Add the CorpusIQ entry:

```json
{
  "mcpServers": {
    "corpusiq": {
      "command": "npx",
      "args": [
        "-y", "mcp-remote",
        "https://mcp2.corpusiq.io/mcp"
      ]
    }
  }
}
```

7. Save the file and fully quit Claude Desktop. Not just the window: quit the application.
8. Reopen Claude, complete the device login when prompted, and the tools indicator appears next to the message box.

If the tools indicator does not appear, work through [Claude can't see CorpusIQ](troubleshooting/claude-cant-see-corpusiq.md) before changing anything else.

### Example Claude Questions

**Sales**

- "How many units did we sell this month, by marketplace?"
- "Which marketplace is growing fastest, and which is declining?"
- "What is our average order value on Amazon compared with our own store?" (requires the commerce connector)

**Operations**

- "Which orders from the last 24 hours have not shipped yet?"
- "Which products are at risk of a stockout based on recent sales velocity?"
- "Show me the SKUs with the highest unit growth in the last 14 days."

**Money**

- "What settlement amount is expected from the current payout period?"
- "Reconcile this month's Amazon payouts against what accounting recorded as deposits." (requires the accounting connector)
- "Which fee events grew faster than sales this month?"

**Marketplace and cross-source**

- "How do our Amazon sales compare with eBay and Shopify for the same period?" (requires the other commerce connectors)
- "Compare Amazon advertising-attributed sales with what the orders actually show." (requires the ads connector)
- "Which Amazon customers are also repeat buyers on our own store?" (requires the commerce connector)

### Security

- **Read-only by scope.** The connector reads orders, sales metrics, inventory, financial events, and marketplace participations. It cannot create listings, adjust inventory, issue refunds, or change account settings.
- **Account-scoped.** Only the marketplaces and data visible to the authorized Seller Central account are reachable.
- **Revocable at any time.** Removing the application authorization in Seller Central ends the connection.
- **Scoped direct-MCP retention.** Direct MCP retrieval is read-only. Raw customer files and full connector payloads are not retained. Operational logs keep query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Amazon, CorpusIQ, and Claude.

### Comparison: Seller Central Reports vs Amazon Through Claude

| Aspect | Seller Central reports | CorpusIQ MCP with Claude |
|---|---|---|
| Input | Pick a report, a range, one marketplace | A question in plain language |
| Speed | Minutes to hours for large ranges | The answer to the question you asked |
| Multiple marketplaces | Separate reports | Compared in one answer |
| Orders plus inventory | Two reports, joined by hand | One question |
| Settlements | Financial event reports | Readable on request |
| Write access | Yes, by you | None, read-only |

Reports are the right tool when you need a file for an accountant. Claude is the right tool when you need an answer now.

### FAQ: Common Questions

<details>
<summary><strong>Is this read-only?</strong></summary>

Yes. Every Amazon Seller tool exposed to Claude is read-only. Listings, inventory, pricing, refunds, and account settings cannot be changed through this connection.
</details>

<details>
<summary><strong>Does it work with multiple marketplaces?</strong></summary>

Yes, for the marketplaces the authorized account participates in. The connector reads the participation list first, so a question can be answered per marketplace or compared across them.
</details>

<details>
<summary><strong>Which Amazon account should I authorize?</strong></summary>

The Seller Central account that owns the data you want to read. Access follows that account, so a user without permission to a marketplace will not see its data through Claude either.
</details>

<details>
<summary><strong>Can I see settlement and fee detail, not just sales totals?</strong></summary>

Yes. Financial events are readable, which is what makes payout reconciliation and fee analysis possible without downloading a settlement report.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Every question is answered against Seller Central at the moment you ask. There is no nightly copy of your marketplace data behind the answers.
</details>

<details>
<summary><strong>Does this replace my accounting connection?</strong></summary>

No, it complements it. Amazon data describes the marketplace; accounting describes the books. The most useful questions need both, which is why they can be connected side by side.
</details>

---

**Next steps:** [Connect Amazon Seller to Claude now](https://www.corpusiq.io/connectors)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*
---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
