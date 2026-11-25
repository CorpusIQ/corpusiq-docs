---
title: Connect Etsy to ChatGPT via MCP
description: "Connect Etsy to ChatGPT through CorpusIQ MCP. Ask which listings convert, how orders trend and what reviewers keep mentioning."
category: ChatGPT Integrations
tags: ["connect Etsy to ChatGPT", "Etsy MCP", "Etsy ChatGPT integration", "ask ChatGPT about Etsy sales", "Etsy shop analytics", "CorpusIQ MCP"]
last_updated: "2026-11-24"
canonical: "https://www.corpusiq.io/docs/connect-etsy-to-chatgpt"
robots: "index,follow"
---

# How to Connect Etsy to ChatGPT with CorpusIQ MCP

An Etsy shop produces a lot of signal. Views, visits, orders, revenue, reviews. The shop dashboard shows each one on its own screen, for its own period, and forgets it as soon as you close the tab.

Connecting Etsy through CorpusIQ MCP lets you ask across those numbers in plain English inside ChatGPT, read-only, and get an answer that names the listings behind it.

## What Questions Can You Ask?

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

## FAQ: Common Questions

<details>
<summary><strong>Can ChatGPT change prices, edit listings or refund an order?</strong></summary>

No. The connection carries read access and the connector exposes retrieval tools only. It does not edit listings, change prices, refund orders or message buyers.
</details>

<details>
<summary><strong>It says no shop was found.</strong></summary>

The Etsy account you authorized does not own a shop. Sign in with the shop owner account and reconnect.
</details>

<details>
<summary><strong>My most recent orders are missing.</strong></summary>

Recent orders can take a few hours to appear. If a full day passes with no new orders, disconnect and reconnect the connector.
</details>

<details>
<summary><strong>I run more than one shop. How does that work?</strong></summary>

Connect each shop separately, so every answer stays scoped to the store you asked about rather than blending two shops together.
</details>

<details>
<summary><strong>Does it read buyer names and addresses?</strong></summary>

Order retrieval returns receipt-level detail for orders placed in the shop, including what Etsy exposes on the receipt. Ask only for the fields you need, and keep buyer personal data out of the question when totals are enough.
</details>

<details>
<summary><strong>What is retained after a query?</strong></summary>

Direct MCP retrieval does not retain raw customer files or full connector response payloads. Operational query logs keep query text and bounded outcome summaries for up to 30 days.
</details>

## How It Works

1. You connect Etsy in the CorpusIQ dashboard and approve the read permissions on Etsy's consent screen.
2. CorpusIQ exposes shop performance, listings, receipts and review trends as MCP tools.
3. You add the CorpusIQ MCP server to ChatGPT. See the [Quick Start guide](quick-start.md).
4. ChatGPT retrieves the figures and answers from them.
5. The answer names the listings or periods it used, so the number can be checked against the shop dashboard.

## Setup Guide

1. **Sign up** at [corpusiq.io](https://www.corpusiq.io). The 30-day trial needs no credit card.
2. **Connect Etsy.** Dashboard, then Connectors, then Etsy, then sign in with the shop owner account and approve read access.
3. **Connect ChatGPT.** Add the CorpusIQ MCP server per the [Quick Start guide](quick-start.md).
4. **Verify.** Ask "which Etsy listings sold best in the last 30 days". Real listing names mean the connection is live.
5. **Explore.** Then ask which listings get views and no orders, which is the question the shop dashboard never answers directly.

## Related Pages

- [Etsy connector reference](connectors/etsy.md) - what the connection can see and the shop-scoping rules
- [Connect eBay to ChatGPT](connect-ebay-to-chatgpt.md) - the marketplace numbers beside the handmade ones
- [Connect Etsy to Claude](connect-etsy-to-claude.md) - the same listing and review questions in Claude Desktop
- [Connect Amazon Seller to ChatGPT](connect-amazon-seller-to-chatgpt.md) - the third channel in the same answer
- [Connect Shopify to ChatGPT](connect-shopify-to-chatgpt.md) - the store you run on your own domain
- [Connect Stripe to ChatGPT](connect-stripe-to-chatgpt.md) - payouts and fees against the order totals
- [Browse all CorpusIQ connectors](connectors.md) - the full list
- [How to Connect Business Data to ChatGPT](how-to-connect-business-data-to-chatgpt.md) - the general setup

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*
