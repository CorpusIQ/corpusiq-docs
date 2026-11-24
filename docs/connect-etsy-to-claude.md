---
title: "Connect Etsy to Claude via MCP - Listings, Orders, Reviews"
description: "Connect Etsy to Claude through CorpusIQ MCP. Ask which listings convert, how orders trend and what reviewers mention, read-only, with the listings cited."
category: Claude Integrations
tags: ["connect Etsy to Claude", "Etsy Claude integration", "MCP Etsy connector", "Etsy data to Claude", "Etsy shop analytics", "CorpusIQ MCP"]
last_updated: "2026-11-24"
canonical: "https://www.corpusiq.io/docs/connect-etsy-to-claude"
robots: "index,follow"
---

# How to Connect Etsy to Claude with CorpusIQ MCP

An Etsy shop produces more signal than the dashboard can hold together. Views, visits, orders, revenue and reviews each sit on their own screen, for their own period, and the comparison between them is left to you.

Connecting Etsy to Claude through CorpusIQ MCP turns that into a question. You ask in plain language, Claude reads your live shop data, and the answer names the listings behind it. Read-only, with nothing exported out of Etsy first.

### Why Connect Etsy to Claude?

Etsy is a handmade shop, so the signal that matters is which listings earn attention and which of those turn it into orders. That comparison is exactly what a per-screen dashboard does not give you.

- **What sold, and what should have.** "Which Etsy listings sold best in the last 30 days?" and "which listings get views but no orders?" are the same question from two directions.
- **Trend instead of a total.** "How did Etsy revenue trend month over month this year?" Claude reads the order data and returns the series as text you can act on.
- **Stale inventory.** "Show me listings that have not sold in 60 days." Useful before a shop refresh, not after.
- **Pricing spread.** "What is the price range across my active listings?" One answer instead of opening each listing.
- **Review themes.** "What do my recent reviews complain about most?" Ratings and review volume come back as a theme, not a star average.
- **Cross-source context.** Put Etsy beside Shopify, Stripe or QuickBooks in the same conversation, so every channel and the books agree.

### How It Works

1. **Connect Etsy to CorpusIQ.** Authorize read-only access to the shop you want read, using the shop owner account or an account with access to the shop's data.
2. **Connect CorpusIQ to Claude** as an MCP server, using the config block from your CorpusIQ account settings.
3. **CorpusIQ translates** your question into Etsy calls, handles pagination and field mapping, and retrieves the matching shop performance, listings, orders and review data.
4. **Claude answers** from that retrieved content, with the listings it used attached to the answer.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log in and open **Connectors**.
2. Select **Etsy**.
3. Click Connect, sign in to Etsy if you are not already signed in, and approve the read-only permissions on the consent screen.
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

If you run more than one shop, connect each shop separately so the answers stay scoped to the right store. If the tools indicator does not appear, work through [Claude can't see CorpusIQ](troubleshooting/claude-cant-see-corpusiq.md) before changing anything else.

### Example Claude Questions

**Sales and revenue**

- "Which Etsy listings sold best in the last 30 days?"
- "How did Etsy revenue trend month over month this year?"
- "What was my average order value last quarter?"

**Listings**

- "Which listings get views but no orders?"
- "Show me listings that have not sold in 60 days."
- "What is the price range across my active listings?"

**Customers and reviews**

- "What do my recent reviews complain about most?"
- "How has review volume changed over the last six months?"

**Cross-source**

- "Compare Etsy orders with Shopify orders for the same period." (requires the Shopify connector)
- "Which Etsy fees landed in Stripe this month?" (requires the Stripe connector)

### Security

- **Read-only by permission.** The connection requests read access to shop performance, listings, orders and review data. There is no path for Claude to edit a listing, change a price, refund an order or message a buyer.
- **Enforced in two places.** The Etsy consent scopes and the MCP tool set both refuse writes, so a write attempt fails rather than silently succeeding.
- **Revocable at any time.** Disconnecting Etsy in the CorpusIQ dashboard, or revoking the app in Etsy, ends the connection immediately.
- **Scoped direct-MCP retention.** Direct MCP retrieval is read-only. Raw customer files and full connector payloads are not retained. Operational logs keep query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Etsy, CorpusIQ, and Claude.

### Comparison: Etsy Dashboard vs Etsy Through Claude

| Aspect | Etsy shop dashboard | CorpusIQ MCP with Claude |
|---|---|---|
| Input | A screen per metric, a period per screen | A question in plain language |
| Views vs orders | Two screens, compared by hand | Both in one answer |
| Reviews | Star average and a list | Themes across the reviews |
| Mixing sources | Export and reconcile elsewhere | Etsy plus Shopify, Stripe or QuickBooks in one answer |
| Write access | Yes, by you | None, read-only |

Use the dashboard when you want to look at one listing. Use Claude when the question spans listings, periods or channels.

### FAQ: Common Questions

<details>
<summary><strong>It says no shop was found.</strong></summary>

The Etsy account you authorized does not own a shop. Sign in with the shop owner account and reconnect.
</details>

<details>
<summary><strong>My most recent orders are missing.</strong></summary>

Recent orders can take a few hours to appear. If a full day passes with no new orders, disconnect and reconnect the connector.
</details>

<details>
<summary><strong>The wrong shop is connected.</strong></summary>

Disconnect Etsy in the dashboard, switch accounts on etsy.com, then reconnect so the connection points at the store you meant to read.
</details>

<details>
<summary><strong>Can Claude edit a listing, change a price or refund an order?</strong></summary>

No. The connection carries read access and the connector exposes retrieval tools only. It does not edit listings, change prices, refund orders or message buyers.
</details>

<details>
<summary><strong>Which shops can Claude see?</strong></summary>

Only the shop the authorizing account owns or can access. Connect each shop separately when you run more than one, so each answer stays scoped to the store you asked about.
</details>

<details>
<summary><strong>What is retained after a query?</strong></summary>

Direct MCP retrieval does not retain raw customer files or full connector response payloads. Operational query logs keep query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.
</details>

---

**Next steps:** [Connect Etsy to Claude now](https://www.corpusiq.io/connectors)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
