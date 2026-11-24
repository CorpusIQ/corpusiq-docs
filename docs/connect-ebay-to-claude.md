---
title: "Connect eBay to Claude via MCP - GMV, Fees, Seller Standards"
description: "Connect eBay to Claude through CorpusIQ MCP. Ask about GMV, fees, funds on hold and seller standards in plain English, read-only, with the listings cited."
category: Claude Integrations
tags: ["connect eBay to Claude", "eBay Claude integration", "MCP eBay connector", "eBay data to Claude", "eBay seller analytics", "CorpusIQ MCP"]
last_updated: "2026-11-24"
canonical: "https://www.corpusiq.io/docs/connect-ebay-to-claude"
robots: "index,follow"
---

# How to Connect eBay to Claude with CorpusIQ MCP

Every figure an eBay seller needs sits in Seller Hub, and each one has its own screen. Orders, transactions, fees, seller standards, listing traffic. One view per question, one date filter per view, and no view that answers the question you actually asked.

Connecting eBay to Claude through CorpusIQ MCP replaces the tab-hopping with a question. You ask in plain language, Claude reads your live Seller Hub data, and the answer names the listings, orders and periods it used. Read-only, with no exporter in between.

### Why Connect eBay to Claude?

eBay is where the money lands and the least readable place to audit it. Claude gives you a way to ask about the marketplace in the same conversation as the rest of the business.

- **Revenue without the date filter.** "What is my eBay GMV for the last 30 days?" One question instead of the payments screen plus a calculator.
- **Fees, broken out.** "What did eBay charge me in fees last month, split by type?" The fee lines are already in the transaction list, so Claude can group them.
- **Cash position.** "Show me eBay funds on hold right now, and how much has settled this week." This is the number sellers check before making a purchase.
- **Seller health trend.** "How are my seller standards trending, and what is my INAD rate this quarter?" Both come from the standards profile and the service metrics.
- **Traffic that explains the gap.** "Which listings got the most impressions last week but no sales?" Views without conversion is the question Seller Hub leaves to you.
- **Cross-source context.** Pair eBay with Amazon Seller, Shopify, Stripe or QuickBooks in one thread, so marketplace revenue and the books agree.

### How It Works

1. **Connect eBay to CorpusIQ.** Authorize read-only access to your seller account and approve the seller scopes on eBay's consent screen.
2. **Connect CorpusIQ to Claude** as an MCP server, using the config block from your CorpusIQ account settings.
3. **CorpusIQ translates** your question into eBay calls, handles pagination and field mapping, and retrieves the matching orders, transactions, standards and traffic data.
4. **Claude answers** from that retrieved content, with the listings, orders or periods it used attached to the answer.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log in and open **Connectors**.
2. Select **eBay**.
3. Click Connect, sign in to eBay, and approve the requested seller scopes on the consent screen.
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

**Revenue and orders**

- "What is my eBay GMV for the last 30 days?"
- "How many orders did I fulfil last week, and how many are still open?"
- "Compare eBay GMV this month with the same month last year."

**Fees and cash**

- "What did eBay charge me in fees last month, broken down by type?"
- "Show me eBay funds on hold right now."
- "How much has settled this week, and what is my total balance?"

**Seller health**

- "How are my seller standards trending?"
- "What is my INAD rate this quarter, and which listings drive it?"
- "Which listings got the most impressions last week?"

**Cross-source**

- "Compare eBay GMV with Amazon sales for the same period." (requires the Amazon Seller connector)
- "Do the eBay refunds in the transaction list match what Stripe shows?" (requires the Stripe connector)

### Security

- **Read-only by permission.** The connection requests read access to orders, financial transactions, seller standards, service metrics, traffic reports and the funds summary. There is no path for Claude to list items, edit a listing, refund a buyer or move funds.
- **Enforced in two places.** The eBay seller scopes and the MCP tool set both refuse writes, so a write attempt fails rather than silently succeeding.
- **Revocable at any time.** Removing the CorpusIQ application in eBay ends the connection immediately.
- **Scoped direct-MCP retention.** Direct MCP retrieval is read-only. Raw customer files and full connector payloads are not retained. Operational logs keep query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.
- **TLS in transit** between eBay, CorpusIQ, and Claude.

### Comparison: Seller Hub vs eBay Through Claude

| Aspect | eBay Seller Hub | CorpusIQ MCP with Claude |
|---|---|---|
| Input | A screen per metric, a date filter per screen | A question in plain language |
| Fees and cash | Payments tab, then arithmetic | Asked directly, grouped by type |
| Seller health | Standards profile page | Trend question answered as text |
| Traffic vs sales | Two views, joined by hand | Both in one answer |
| Mixing sources | Export and reconcile elsewhere | eBay plus Amazon, Stripe or QuickBooks in one answer |
| Write access | Yes, by you | None, read-only |

Seller Hub is the right tool when you know exactly which figure you want. Claude is the right tool when you know the question and not which screen holds it.

### FAQ: Common Questions

<details>
<summary><strong>Does this work with more than one eBay account?</strong></summary>

Each connection is scoped to the seller account you authorized. Connect the accounts you need separately so each answer stays tied to the store you asked about.
</details>

<details>
<summary><strong>The funds summary is empty or missing.</strong></summary>

The funds summary needs the `sell.finances` scope, which is requested during the OAuth flow. Disconnect and reconnect so the scope is granted, then ask again.
</details>

<details>
<summary><strong>The traffic report is empty for today.</strong></summary>

eBay's traffic data has a 24 to 48 hour lag. Ask about yesterday or earlier rather than today.
</details>

<details>
<summary><strong>The seller standards profile comes back blank.</strong></summary>

New sellers do not have a standards profile yet. eBay requires a minimum order volume before the profile exists, so the answer is blank rather than wrong.
</details>

<details>
<summary><strong>Can Claude list an item, edit a listing or refund a buyer?</strong></summary>

No. The connection carries read access and the connector exposes retrieval tools only. It does not list items, edit listings, refund buyers or move funds.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Every question is answered against your seller account at the moment you ask. Orders and transaction lists are live; traffic and standards data carry eBay's own reporting lag, which the answer reflects rather than hides.
</details>

<details>
<summary><strong>What is retained after a query?</strong></summary>

Direct MCP retrieval does not retain raw customer files or full connector response payloads. Operational query logs keep query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.
</details>

---

**Next steps:** [Connect eBay to Claude now](https://www.corpusiq.io/connectors)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
