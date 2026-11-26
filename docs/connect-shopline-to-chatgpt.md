---
title: Connect SHOPLINE to ChatGPT via MCP
description: "Connect SHOPLINE to ChatGPT through CorpusIQ MCP. Ask about orders, inventory, refunds and repeat customers in the same thread as the rest of your numbers."
category: ChatGPT Integrations
tags: ["connect SHOPLINE to ChatGPT", "SHOPLINE MCP", "SHOPLINE ChatGPT integration", "ask ChatGPT about SHOPLINE orders", "SHOPLINE store analytics", "CorpusIQ MCP"]
last_updated: "2026-11-26"
canonical: "https://www.corpusiq.io/docs/connect-shopline-to-chatgpt"
robots: "index,follow"
---

# How to Connect SHOPLINE to ChatGPT with CorpusIQ MCP

A SHOPLINE store answers every question on a different screen. Orders sit under one menu, inventory under another, refunds somewhere else again, and the customer history is a search box you have to know how to use. By the time you have read three of them, the question has changed.

Connecting SHOPLINE through CorpusIQ MCP lets you ask about the store in one ChatGPT thread, read-only, and get an answer that names the orders, products and periods behind it.

## What Questions Can You Ask?

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

## FAQ: Common Questions

<details>
<summary><strong>Can ChatGPT change a product, price or order?</strong></summary>

No. The connection exposes retrieval tools only. It does not create or edit products, change prices, fulfil orders, issue refunds or message customers.
</details>

<details>
<summary><strong>I run more than one SHOPLINE store.</strong></summary>

Each connection is scoped to the store that authorised it. Connect each store separately so an answer stays attached to the store you asked about.
</details>

<details>
<summary><strong>An order I know exists does not come back.</strong></summary>

Order lists are paged. Ask for a narrower period or a specific order number so the matching record is inside the first page of results.
</details>

<details>
<summary><strong>Inventory levels look different from the admin panel.</strong></summary>

Inventory is reported per location. If you have more than one location, ask for the location you mean or the totals will read as a mismatch.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Orders, refunds and inventory are read from your store at the moment you ask, so the figure reflects the store as it stands.
</details>

<details>
<summary><strong>What is retained after a query?</strong></summary>

Direct MCP retrieval does not retain raw customer files or full connector response payloads. Operational query logs keep query text and bounded outcome summaries for up to 30 days.
</details>

## How It Works

1. You connect SHOPLINE in the CorpusIQ dashboard and approve the read-only permissions on SHOPLINE's consent screen.
2. CorpusIQ exposes orders, order summaries, refunds, products, inventory items and levels, locations, customers, returns, fulfillment orders and discount code price rules as MCP tools.
3. You add the CorpusIQ MCP server to ChatGPT. See the [Quick Start guide](quick-start.md).
4. ChatGPT retrieves the records and answers from them.
5. The answer names the orders, products or periods behind it, so the number can be checked in the admin panel.

## Setup Guide

1. **Sign up** at [corpusiq.io](https://www.corpusiq.io). The 30-day trial needs no credit card.
2. **Connect SHOPLINE.** Dashboard, then Connectors, then SHOPLINE, then sign in as the store admin and approve the permissions.
3. **Connect ChatGPT.** Add the CorpusIQ MCP server per the [Quick Start guide](quick-start.md).
4. **Verify.** Ask "how many orders came in last week". A real count with a real total means the connection is live.
5. **Explore.** Then ask which products are below ten units on hand, which is the question the admin panel leaves you to work out by hand.

## Related Pages

- [SHOPLINE connector reference](connectors/shopline.md) - what the connection can see, the permissions it needs and how stores are scoped
- [Connect SHOPLINE to Claude](connect-shopline-to-claude.md) - the same questions in Claude Desktop, with the device-login setup
- [Connect SHOPLINE to Perplexity](connect-shopline-to-perplexity.md) - the same questions asked from Perplexity
- [Connect Shopify to ChatGPT](connect-shopify-to-chatgpt.md) - the same commerce questions on the other storefront platform
- [Connect Stripe to ChatGPT](connect-stripe-to-chatgpt.md) - check store revenue against what actually settled
- [Connect QuickBooks to ChatGPT](connect-quickbooks-to-chatgpt.md) - put store revenue into the books view
- [Browse all CorpusIQ connectors](connectors.md) - the full list
- [How to Connect Business Data to ChatGPT](how-to-connect-business-data-to-chatgpt.md) - the general setup

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.CorpusIQ.io).*
