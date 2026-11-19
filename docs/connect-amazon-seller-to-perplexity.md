---
title: "Connect Amazon Seller to Perplexity via MCP"
description: "Connect Amazon Seller Central to Perplexity through CorpusIQ MCP. Ask about orders, FBA inventory and payouts across marketplaces, from live data."
category: Perplexity Integrations
tags: ["connect Amazon Seller to Perplexity", "Amazon Seller Central Perplexity", "MCP Amazon connector", "Amazon marketplace analytics", "FBA inventory questions", "CorpusIQ MCP"]
last_updated: "2026-11-19"
canonical: "https://www.corpusiq.io/docs/connect-amazon-seller-to-perplexity"
robots: "index,follow"
---

# How to Connect Amazon Seller Central to Perplexity with CorpusIQ MCP

Marketplace revenue arrives in pieces: orders in one report, fulfilment inventory in another, fees and settlements in a third, and a payout number at the end that nobody reconciles against the books. **Connecting Amazon Seller to Perplexity through CorpusIQ MCP** makes the marketplace answerable in a sentence, across marketplaces, instead of one report at a time.

Perplexity is strong on the public record and blind to your Seller Central account. Authorising the connector once is what turns "how is Amazon doing" into a question with numbers behind it, next to your own store and your accounting.

### Why Connect Amazon Seller to Perplexity?

- **Volume by marketplace.** "How many units did we sell this month, by marketplace?"
- **Stockout risk.** "Which products are at risk of a stockout based on recent sales velocity?"
- **Order state.** "Which orders from the last 24 hours have not shipped yet?"
- **Settlement expectations.** "What settlement amount is expected from the current payout period, and which fee events drive it?"
- **Marketplace mix.** "Which marketplace is growing fastest, and which is declining?"
- **Read-only by capability.** The retrieval tools documented on this page return orders, inventory and financial events to the assistant. They never create a listing, change a price or refund an order.

### How It Works

1. **Connect Amazon Seller to CorpusIQ.** Sign in to Seller Central as an account with app-authorisation rights and follow the Amazon SP-API authorisation flow.
2. **Add CorpusIQ to Perplexity** as a custom remote MCP server, using the endpoint from your CorpusIQ account settings.
3. **Ask a marketplace question.** CorpusIQ resolves the date range, the marketplace and the objects the question needs, then returns the numbers with the period attached.
4. **Perplexity answers** with the marketplace and period named in the reply, beside the outside context it already provides.

Direct MCP retrieval is read-only. It does not retain raw customer files or full connector response payloads; operational logs keep query text, per-user tool-call metadata and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log in and open **Connectors**.
2. Select **Amazon Seller** and click Connect.
3. Sign in to Seller Central when prompted and follow the standard Amazon SP-API authorisation flow. Use the primary account, not a sub-user without app-authorisation rights.
4. Approve the access the consent screen lists and wait for the connector to turn green.

**In Perplexity**

5. Open **Settings** and find the **MCP servers** section.
6. Add a custom MCP server and paste the endpoint:

```
https://mcp2.corpusiq.io/mcp
```

Then ask something the marketplace can answer, for example how many orders came in last week. The date range and the marketplace region decide what comes back, so name both when the answer matters.

### Example Perplexity Questions

**Sales and orders**

- "How many units did we sell this month, by marketplace?"
- "What was average order value on Amazon last quarter?"
- "Which orders from the last 24 hours have not shipped yet?"

**Inventory and fulfilment**

- "Which products are at risk of a stockout based on recent sales velocity?"
- "What is my FBA inventory position right now, and which SKUs are below two weeks of cover?"
- "Which SKUs sold nothing in 60 days but still hold inventory?"

**Money**

- "What settlement amount is expected from the current payout period?"
- "Which fee events made up last month's payout?"
- "Which marketplace contributed the most revenue after fees?"

**Cross-source**

- "Compare Amazon revenue with Shopify for the same period." (requires a store connector)
- "Reconcile this month's Amazon payouts against the deposits in QuickBooks." (requires a finance connector)
- "How does Amazon ad-attributed sales compare with what the orders show?" (requires an ads connector)

### Security

- **Retrieval tools only.** The tools documented on this page read orders, fulfilment inventory, sales metrics, financial events and marketplace participations.
- **The marketplace is not modified.** No listing is created, no inventory is edited, no order is refunded and no price is changed through these tools.
- **Amazon authorisation stays yours.** CorpusIQ holds the encrypted grant; revoking it in Seller Central ends the connection's reach.
- **Scoped direct-MCP retention.** Raw customer files and full connector payloads are not retained. Operational logs keep query text, tool-call metadata and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Amazon, CorpusIQ and Perplexity.

### Comparison: Seller Central reports and a marketplace question

| Aspect | Seller Central reports | CorpusIQ MCP with Perplexity |
|---|---|---|
| Input | A report type, a date range, one marketplace | A question across marketplaces |
| Shape | Rows to pivot | An answer with the period attached |
| Inventory | Separate fulfilment report | Same answer as the sales question |
| Settlement | Fee events in their own view | Payout expectation beside the orders behind it |
| Cross-system | Export and join by hand | Asked across connectors |
| Write access | Yes, by your users in Seller Central | None through the retrieval tools |

A report answers the question you had yesterday. A question in the thread answers the one you have now.

### FAQ: Common Questions

<details>
<summary><strong>Can Perplexity change listings or prices?</strong></summary>

No. The retrieval tools documented on this page read orders, inventory and financial events. Listing, pricing, fulfilment and refund actions stay in Seller Central.
</details>

<details>
<summary><strong>Why are no orders coming back?</strong></summary>

Check the date range first. Amazon exposes orders from the marketplace region tied to the account, so a range outside that region or outside the account's marketplaces returns nothing.
</details>

<details>
<summary><strong>Why is inventory empty?</strong></summary>

If you do not use FBA, inventory is empty by design. Track sell-through from orders instead.
</details>

<details>
<summary><strong>Does it cover every marketplace?</strong></summary>

The connector reads the marketplaces the account participates in, and multi-marketplace questions are answerable. Which ones appear is decided by your Seller Central account.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Read live from the Amazon API at question time. Amazon's own reporting layers can lag settlement figures, so the most recent payout period may still be moving.
</details>

<details>
<summary><strong>Does this work in ChatGPT or Claude too?</strong></summary>

Yes. Amazon Seller is exposed to ChatGPT, Claude and Perplexity through the same endpoint on the same subscription.
</details>

### See Also

- [Connect Amazon Seller to ChatGPT](connect-amazon-seller-to-chatgpt.md) - the same marketplace questions, asked in ChatGPT
- [Amazon Seller connector reference](connectors/amazon_seller.md) - what is visible, and the boundary
- [Connect Shopify to Perplexity](connect-shopify-to-perplexity.md) - your own store beside the marketplace
- [Connect QuickBooks to Perplexity](connect-quickbooks-to-perplexity.md) - reconcile the payouts
- [Browse all CorpusIQ connectors](connectors.md) - the full list

---

**Next steps:** [Add CorpusIQ to Perplexity now](https://www.corpusiq.io/connectors/perplexity)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.CorpusIQ.io).*

