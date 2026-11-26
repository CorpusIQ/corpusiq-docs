---
title: Connect SHOPLINE to Claude via MCP
description: "Connect SHOPLINE to Claude through CorpusIQ MCP. Ask about orders, stock levels, refunds and repeat customers in plain English, read-only, records cited."
category: Claude Integrations
tags: ["connect SHOPLINE to Claude", "SHOPLINE Claude integration", "MCP SHOPLINE connector", "SHOPLINE data to Claude", "SHOPLINE store analytics", "CorpusIQ MCP"]
last_updated: "2026-11-26"
canonical: "https://www.corpusiq.io/docs/connect-shopline-to-claude"
robots: "index,follow"
---

# How to Connect SHOPLINE to Claude with CorpusIQ MCP

Your store data exists, but it exists one list at a time. Orders, products, inventory, customers, returns and discount rules each have their own view, and none of them answers a question that crosses two of those views.

Connecting SHOPLINE to Claude through CorpusIQ MCP replaces the list-hopping with a question. You ask in plain language, Claude reads your live store data, and the answer names the orders, products and periods it used. Read-only, with no exporter in between.

### Why Connect SHOPLINE to Claude?

SHOPLINE is where the transactions happen and one of the harder places to audit them. Claude gives you a way to ask about the store in the same conversation as the rest of the business.

- **Orders without the date filter.** "How many orders came in last week, and what did they total?" One question instead of a list plus a calculator.
- **Stock that is about to run out.** "Which SKUs are below ten units on hand?" The answer is a list you can act on, per location if you ask.
- **Refunds in context.** "How many refunds did I issue last quarter, and on which products?" Refund records and the products behind them in one answer.
- **Repeat customers.** "Which customers ordered more than once in the last 90 days?" Retention read out of the customer records rather than guessed.
- **Discount effectiveness.** "Which discount codes did customers use most this quarter?" Price rules matched against the orders they produced.
- **Cross-source context.** Pair SHOPLINE with Stripe or QuickBooks in one thread, so store revenue and the books agree.

### How It Works

1. **Connect SHOPLINE to CorpusIQ.** Authorise read-only access to your store and approve the permissions on SHOPLINE's consent screen.
2. **Connect CorpusIQ to Claude** as an MCP server, using the config block from your CorpusIQ account settings.
3. **CorpusIQ translates** your question into SHOPLINE Admin API calls, handles pagination and field mapping, and retrieves the matching orders, products, inventory or customer records.
4. **Claude answers** from that retrieved content, with the orders, products or periods it used attached to the answer.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log in and open **Connectors**.
2. Select **SHOPLINE**.
3. Click Connect, sign in as the store admin, and approve the requested permissions on the consent screen.
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

**Orders and revenue**

- "How many SHOPLINE orders came in last week, and what did they total?"
- "What is my average order value this month compared with last month?"
- "Which orders are still unfulfilled right now?"
- "How many refunds did I issue last quarter, and on which products?"

**Inventory and merchandising**

- "Which SKUs are below ten units on hand?"
- "Show me inventory by location so I can see what to transfer."
- "Which products sold out last month and are still out of stock?"
- "Which discount codes did customers use most this quarter?"

**Customers and retention**

- "Which customers ordered more than once in the last 90 days?"
- "What did my ten highest-spending customers buy?"
- "How many new customers did I add this month?"
- "Which returns came from repeat customers?"

**Cross-source**

- "Compare SHOPLINE revenue with Stripe payouts for the same week. (requires the Stripe connector)"
- "Do the SHOPLINE refunds match what the books show in QuickBooks? (requires the QuickBooks connector)"
- "Put SHOPLINE revenue next to my ad spend for last month. (requires a paid-media connector)"

### Security

- **Read-only by permission.** The connection requests read access to orders, refunds, products, inventory, locations, customers, returns, fulfillment orders and discount code price rules. There is no path for Claude to edit a product, change a price, fulfil an order or message a customer.
- **Enforced in two places.** The permissions approved on SHOPLINE's consent screen and the MCP tool set both refuse writes, so a write attempt fails rather than silently succeeding.
- **Revocable at any time.** Disconnecting SHOPLINE in CorpusIQ ends the connection immediately.
- **Scoped direct-MCP retention.** Direct MCP retrieval is read-only. Raw customer files and full connector payloads are not retained. Operational logs keep query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.
- **TLS in transit** between SHOPLINE, CorpusIQ and Claude.

### Comparison: SHOPLINE Admin vs SHOPLINE Through Claude

| Aspect | SHOPLINE admin | CorpusIQ MCP with Claude |
|---|---|---|
| Input | A screen, a filter, a date range | A question |
| Scope | Orders, products, inventory or customers, one at a time | All of them in one answer |
| Follow-ups | Rebuild the view | Ask the next question in the same thread |
| Outside context | Open a second tab | Same thread, same answer |
| Cross-system | Export to a sheet | Asked across connectors |
| Write access | Yes, by you | None through the retrieval tools |

The admin panel shows you each list. It does not answer which products are selling and which are quietly tying up cash.

### FAQ: Common Questions

<details>
<summary><strong>Can Claude create products or change prices?</strong></summary>

No. The retrieval tools documented on this page read orders, refunds, products, inventory, locations, customers, returns, fulfilment orders and discount rules. Nothing is created, edited, fulfilled or refunded.
</details>

<details>
<summary><strong>My store has several locations.</strong></summary>

Inventory is reported per location on SHOPLINE's side. Ask for the location you mean, or ask for totals so the numbers are added rather than compared across locations.
</details>

<details>
<summary><strong>An order I know exists does not come back.</strong></summary>

Order lists are paged. Narrow the period or name the order number so the record is inside the first page of results.
</details>

<details>
<summary><strong>Does this work only in Claude?</strong></summary>

No. SHOPLINE is exposed to ChatGPT, Claude and Perplexity through the same endpoint on the same subscription.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Orders, refunds and inventory are read from your store at the moment you ask, so the figure reflects the store as it stands.
</details>

<details>
<summary><strong>What is retained after a query?</strong></summary>

Direct MCP retrieval does not retain raw customer files or full connector response payloads. Operational query logs keep query text and bounded outcome summaries for up to 30 days.
</details>

---

**Next steps:** [Connect SHOPLINE to Claude now](https://www.corpusiq.io/connectors)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.CorpusIQ.io).*
