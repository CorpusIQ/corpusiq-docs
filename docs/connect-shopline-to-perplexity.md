---
title: Connect SHOPLINE to Perplexity via MCP
description: "Connect SHOPLINE to Perplexity through CorpusIQ MCP. Ask about orders, inventory, refunds and repeat customers in one answer, read-only and source-cited."
category: Perplexity Integrations
tags: ["connect SHOPLINE to Perplexity", "SHOPLINE MCP", "SHOPLINE Perplexity integration", "ask Perplexity about SHOPLINE orders", "SHOPLINE store analytics", "CorpusIQ MCP"]
last_updated: "2026-11-26"
canonical: "https://www.corpusiq.io/docs/connect-shopline-to-perplexity"
robots: "index,follow"
---

# How to Connect SHOPLINE to Perplexity with CorpusIQ MCP

A store question rarely lives on one screen. Orders are one list, inventory is another, refunds a third, and a customer's history is a search you have to phrase correctly. Perplexity is good at reasoning across sources, but it cannot see your store unless something hands it the records.

Connecting SHOPLINE through CorpusIQ MCP does exactly that: your live store data becomes readable to Perplexity, one connector among the rest of your business tools, and answers arrive with the orders and periods they came from.

### What Questions Can You Ask?

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

- **Read-only retrieval tools.** The tools documented on this page read orders, order summaries, refunds, products, inventory items and levels, locations, customers, returns, fulfillment orders and discount code price rules. They do not create a product, edit a price, fulfil an order or move money.
- **Approved on SHOPLINE's own screen.** The permissions are granted during the store sign-in flow, and the set you approve is visible there before anything is read.
- **Store-scoped.** A connection reads the single store that authorised it, at the location level you ask about.
- **Revocable.** Disconnecting in CorpusIQ ends the connection, and SHOPLINE's own app settings list it too.
- **Scoped direct-MCP retention.** Raw customer files and full connector payloads are not retained. Operational logs keep query text, tool-call metadata and bounded outcome summaries for up to 30 days.
- **TLS in transit** between SHOPLINE, CorpusIQ and Perplexity.

### Comparison: SHOPLINE Admin

| Aspect | SHOPLINE admin | CorpusIQ MCP with Perplexity |
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
<summary><strong>Can Perplexity change anything in my SHOPLINE store?</strong></summary>

No. The retrieval tools documented on this page read orders, refunds, products, inventory, customers, returns, fulfilment orders and discount rules. Nothing is created, edited, fulfilled or refunded.
</details>

<details>
<summary><strong>Refund totals look lower than the orders they came from.</strong></summary>

Refunds are read as their own record set. Ask for refunds over a period rather than expecting them to be subtracted inside an order total, and the two will reconcile.
</details>

<details>
<summary><strong>Inventory numbers differ between locations.</strong></summary>

Levels are reported per location. Name the location, or ask for the total across locations, so the figure matches what you expect.
</details>

<details>
<summary><strong>Does this work only in Perplexity?</strong></summary>

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

### See Also

- [Connect SHOPLINE to ChatGPT](connect-shopline-to-chatgpt.md) - the same store questions, asked from ChatGPT
- [SHOPLINE connector reference](connectors/shopline.md) - what the connection can see, the permissions it needs and how stores are scoped
- [Connect Shopify to Perplexity](connect-shopify-to-perplexity.md) - the same commerce questions on the other storefront platform
- [Connect Stripe to Perplexity](connect-stripe-to-perplexity.md) - check store revenue against what actually settled

---

**Next steps:** [Add CorpusIQ to Perplexity now](https://www.corpusiq.io/connectors/perplexity)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.CorpusIQ.io).*
