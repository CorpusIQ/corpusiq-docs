---
title: "Connect Shopify to Perplexity via MCP"
description: "Connect Shopify to Perplexity through CorpusIQ MCP. Ask about orders, products, customers and payouts and get answers cited to your own store data"
category: Perplexity Integrations
tags: ["connect Shopify to Perplexity", "Shopify Perplexity integration", "MCP Shopify connector", "Shopify data to AI", "ask Shopify in plain English", "CorpusIQ MCP"]
last_updated: "2026-11-11"
canonical: "https://www.corpusiq.io/docs/connect-shopify-to-perplexity"
robots: "index,follow"
---

# How to Connect Shopify to Perplexity with CorpusIQ MCP

A Shopify store answers most questions with a screen. A date range, a filter, a CSV.

Perplexity answers with words. Ask it about conversion benchmarks and you get the industry figure. Ask it about your own store and it has nothing to read.

Connecting Shopify through CorpusIQ MCP closes that gap. Your orders, products, customers and payouts become readable inside a Perplexity thread, read-only, with the answer naming the data it used.

### Why Connect Shopify to Perplexity?

- **Sales against benchmarks.** "Our AOV is 84 dollars. How does that compare to stores in our category?"
- **Product performance.** "Which five products drove the most revenue last month, and which have the highest return rate?"
- **Customer questions.** "How many repeat customers did we have this quarter, and what share of revenue came from them?"
- **Traffic and demand context.** Pair a real conversion rate with whatever changed in the market that week.
- **Payout reconciliation.** "Which payouts landed this month, and what do they cover?"
- **Read-only by scope.** The grant covers orders, products, customers and analytics. It cannot edit a product or issue a refund.

### How It Works

1. **Connect Shopify to CorpusIQ** through Shopify's OAuth consent screen, granting read-only access.
2. **Add CorpusIQ to Perplexity** as a custom remote MCP server, using the endpoint from your CorpusIQ account settings.
3. **CorpusIQ reads** the orders, products, customers and analytics that answer the question.
4. **Perplexity answers** with your figures plus the market context it already knows.

Direct MCP retrieval is read-only. It does not retain raw customer files or full connector response payloads; operational logs are kept for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log into your dashboard and open **Connectors**.
2. Select **Shopify** and click **Connect Shopify**.
3. You are redirected to Shopify's OAuth consent screen. Review the read-only scopes (Orders, Products, Customers, Analytics) and approve.
4. Return to CorpusIQ. The connection is active immediately.

**In Perplexity**

5. Open **Settings** and find the **MCP servers** section.
6. Add a custom MCP server and paste the endpoint:

```
https://mcp2.corpusiq.io/mcp
```

7. Connect and approve the CorpusIQ authorization page once.
8. Start a new thread and ask a question about the store.

No webhooks to configure and no code to deploy.

### Example Perplexity Questions

**Revenue and margin**

- "What was revenue last month, and how does our AOV compare to stores in our category?"
- "Which product collection has the highest revenue per order?"
- "What share of revenue came from returning customers this quarter?"

**Products**

- "Which products sold out fastest in the last 60 days?"
- "Which SKUs have inventory left but no sales in three weeks?"
- "Which products have the highest return rate, and what is a normal rate for this category?"

**Market context**

- "Did our week-over-week sales move with the retail trend or against it?"
- "Our conversion rate is 1.9 percent. Where does that sit for a store at our traffic level?"

**Cross-source**

- "Do the customers with unpaid invoices in accounting still have open orders in Shopify?" (requires the accounting connector)
- "Compare Shopify refunds to Stripe disputes for the same period." (requires the Stripe connector)

### Security

- **Read-only retrieval tools.** The tools documented on this page are marked read-only, and the encrypted token carries read access to orders, products, customers and analytics. There is no write path from Perplexity into the store.
- **One store per grant.** Connect a second store and it carries its own authorization, so a question only reaches stores you approved.
- **Scoped direct-MCP retention.** Raw customer files and full connector payloads are not retained. Operational logs keep query text and bounded outcome summaries for up to 30 days.
- **Revocable at any time** from the Shopify admin or from CorpusIQ.
- **TLS in transit** between Shopify, CorpusIQ and Perplexity.

### Comparison: Shopify Analytics vs Shopify in Perplexity

| Aspect | Shopify analytics | CorpusIQ MCP with Perplexity |
|---|---|---|
| Input | A report and a date range | A question in plain language |
| Output | Charts and tables | An answer with the period named |
| Market context | Look it up separately | Same thread, same answer |
| Cross-system | Export and join by hand | Asked across connectors |
| Follow-up | Rebuild the report | Ask the next question |
| Write access | Yes, by you | None, read-only |

### FAQ: Common Questions

<details>
<summary><strong>Can Perplexity edit products or refund orders?</strong></summary>

No. The retrieval tools are marked read-only, so the connection cannot edit a product or issue a refund. Orders, products, customers and inventory are untouched.
</details>

<details>
<summary><strong>Does it read customer personal data?</strong></summary>

It reads customer records inside the granted scope, which is how questions about repeat purchase and lifetime value are answered. Direct requests fetch live, and raw customer files and full connector response payloads are not retained.
</details>

<details>
<summary><strong>Does this work with Shopify Plus?</strong></summary>

Yes. The connection is made through the Shopify admin OAuth flow, which Plus stores support the same way.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Live. An order placed a minute ago is visible to the next question. There is no nightly export.
</details>

<details>
<summary><strong>Does this work only in Perplexity?</strong></summary>

No. Shopify is exposed to ChatGPT, Claude and Perplexity through the same endpoint on the same subscription.
</details>

<details>
<summary><strong>Can I limit it to one store?</strong></summary>

Yes. Each Shopify store is a separate connection, and only connected stores are readable.
</details>

<details>
<summary><strong>Where is the Shopify data stored?</strong></summary>

CorpusIQ does not retain raw customer files or full connector response payloads. Operational logs may persist for up to 30 days. See the [read-only and security documentation](/hermes/security/read-only-and-security).
</details>

---

**Next steps:** [Connect Shopify to Perplexity now](https://corpusiq.io/connect/shopify-with-perplexity)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.CorpusIQ.io).*
