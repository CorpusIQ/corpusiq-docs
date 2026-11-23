---
title: "Connect eBay to Perplexity via MCP"
description: "Connect eBay to Perplexity through CorpusIQ MCP. Ask about GMV, fees, seller standards and funds on hold in the same thread as your other channels."
category: Perplexity Integrations
tags: ["connect eBay to Perplexity", "eBay Perplexity integration", "MCP eBay connector", "eBay seller analytics to AI", "ask about eBay GMV in plain English", "CorpusIQ MCP"]
last_updated: "2026-11-23"
canonical: "https://www.corpusiq.io/docs/connect-ebay-to-perplexity"
robots: "index,follow"
---

# How to Connect eBay to Perplexity with CorpusIQ MCP

An eBay seller's numbers live in Seller Hub, and Seller Hub is a set of screens. Orders in one, transactions and fees in another, seller standards in a third, listing traffic somewhere else. Each carries its own date filter, and none of them answers the question you opened them for.

The question is usually a comparison. What fees did those orders actually cost me. Is my holdback growing faster than my volume. Which listings earn impressions and no sales.

Connecting eBay through CorpusIQ MCP puts Seller Hub behind a question. Perplexity reads orders, transactions, seller standards, traffic and the funds summary, and names the period and the listings behind the answer.

### Why Connect eBay to Perplexity?

- **Marketplace revenue.** "What is my eBay GMV for the last 30 days, and how does it compare with the same month last year?"
- **Fees and settlement.** "What did eBay charge me in fees last month, broken down by type, and how much has settled this week?"
- **Cash position.** "Show me eBay funds on hold right now next to my total balance."
- **Seller health.** "How are my seller standards trending, and what is my INAD rate this quarter?"
- **Traffic quality.** "Which listings got the most impressions last week but no sales?"
- **Read-only by capability.** The retrieval tools documented on this page read orders, transactions, standards, traffic and funds. They do not list items, edit listings, refund buyers or move money.

### How It Works

1. **Connect eBay to CorpusIQ.** Sign in on eBay's own consent screen and approve the seller permissions it requests.
2. **Add CorpusIQ to Perplexity** as a custom remote MCP server, using the endpoint from your CorpusIQ account settings.
3. **CorpusIQ queries** orders, financial transactions, the seller standards profile, service metrics, traffic reports and the funds summary for the account you authorised.
4. **Perplexity answers** from the returned records, with the period and the listings named so the figure can be checked in Seller Hub.

Direct MCP retrieval is read-only. It does not retain raw customer files or full connector response payloads; operational logs keep query text, per-user tool-call metadata and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Sign up at [corpusiq.io](https://www.corpusiq.io). The 30-day trial needs no credit card.
2. Open **Dashboard**, then **Connectors**, and find **eBay**.
3. Click **Connect** and sign in to eBay when the consent screen appears.
4. Approve the seller permissions. One of them, `sell.finances`, is what makes the funds summary readable, so approve the full set rather than a subset.
5. The eBay card turns from gray to green.

**In Perplexity**

6. Open **Settings** and find the **MCP servers** section.
7. Add a custom MCP server and paste the endpoint:

```
https://mcp2.corpusiq.io/mcp
```

8. Connect and approve the CorpusIQ authorisation page once. Then start a new thread and ask for a figure by name.

Running more than one store changes only step 3: connect each seller account separately, because each connection is scoped to the account you authorised, and the answers stay tied to the store you asked about.

### Example Perplexity Questions

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
- "Put eBay fees next to the marketplace fees in QuickBooks for last quarter." (requires the QuickBooks connector)

### Security

- **Read-only retrieval tools.** The tools documented on this page read orders, transactions, seller standards, service metrics, traffic reports and the funds summary. They do not alter a listing, refund a buyer or move money.
- **Approved on eBay's own screen.** The permissions are granted during the eBay sign-in flow, and the set you approve is visible there before anything is read.
- **Account-scoped.** A connection reads the single seller account that authorised it.
- **Revocable.** Disconnecting in CorpusIQ ends the connection, and eBay's own authorised-applications settings list it too.
- **Scoped direct-MCP retention.** Raw customer files and full connector payloads are not retained. Operational logs keep query text, tool-call metadata and bounded outcome summaries for up to 30 days.
- **TLS in transit** between eBay, CorpusIQ and Perplexity.

### Comparison: eBay Seller Hub

| Aspect | eBay Seller Hub | CorpusIQ MCP with Perplexity |
|---|---|---|
| Input | A report, a date range, a filter | A question |
| Scope | One screen at a time | Orders, fees, standards, traffic and funds together |
| Follow-ups | Rebuild the report | Ask the next question in the same thread |
| Outside context | Open a second tab | Same thread, same answer |
| Cross-system | Export to a sheet | Asked across connectors |
| Write access | Yes, by you | None through the retrieval tools |

Seller Hub tells you what each screen holds. It does not tell you whether the fee line is eating the margin.

### FAQ: Common Questions

<details>
<summary><strong>Can Perplexity change anything on my eBay account?</strong></summary>

No. The retrieval tools documented on this page read orders, transactions, seller standards, service metrics, traffic and the funds summary. Nothing is listed, edited, refunded or moved.
</details>

<details>
<summary><strong>The funds summary is empty or missing.</strong></summary>

That summary needs the `sell.finances` permission, which is requested during the eBay sign-in flow. Disconnect and reconnect so the full set is approved, then ask again.
</details>

<details>
<summary><strong>The traffic report is empty for today.</strong></summary>

eBay's traffic data runs 24 to 48 hours behind. Ask about yesterday or earlier rather than today.
</details>

<details>
<summary><strong>The seller standards profile comes back blank.</strong></summary>

New sellers do not have a standards profile until they pass eBay's minimum order volume. A blank answer there is accurate, not a failed connection.
</details>

<details>
<summary><strong>Does it work with more than one eBay account?</strong></summary>

Yes, one connection each. Every connection is scoped to the account that authorised it, so you connect the stores you want and the answer stays attached to the one you asked about.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Live, read at question time. Orders and transactions are current; the traffic report carries eBay's own lag.
</details>

<details>
<summary><strong>Does this work only in Perplexity?</strong></summary>

No. eBay is exposed to ChatGPT, Claude and Perplexity through the same endpoint on the same subscription.
</details>

### See Also

- [Connect eBay to ChatGPT](connect-ebay-to-chatgpt.md) - the same GMV and fee questions, asked from ChatGPT
- [eBay connector reference](connectors/ebay.md) - what the connection can see, the permissions it needs and the traffic lag
- [Connect Amazon Seller to Perplexity](connect-amazon-seller-to-perplexity.md) - the other marketplace in the same answer
- [Connect Shopify to Perplexity](connect-shopify-to-perplexity.md) - the store you run on your own domain

---

**Next steps:** [Add CorpusIQ to Perplexity now](https://www.corpusiq.io/connectors/perplexity)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.CorpusIQ.io).*
