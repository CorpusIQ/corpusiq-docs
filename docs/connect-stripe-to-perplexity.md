---
title: "Connect Stripe to Perplexity via MCP"
description: "Connect Stripe to Perplexity through CorpusIQ MCP. Ask about charges, subscriptions, churn and payouts and get answers from your own payment data"
category: Perplexity Integrations
tags: ["connect Stripe to Perplexity", "Stripe Perplexity integration", "MCP Stripe connector", "Stripe data to AI", "ask Stripe in plain English", "CorpusIQ MCP"]
last_updated: "2026-11-12"
canonical: "https://www.corpusiq.io/docs/connect-stripe-to-perplexity"
robots: "index,follow"
---

# How to Connect Stripe to Perplexity with CorpusIQ MCP

Stripe holds the clearest record of what your business actually earns. Charges, subscriptions, refunds, disputes, payouts.

Reading it means the dashboard, a date filter, an export, and someone to interpret it.

Connecting Stripe through CorpusIQ MCP makes those records answerable in a Perplexity thread, read-only, with the answer naming the period it covers.

### Why Connect Stripe to Perplexity?

- **Revenue and churn in one answer.** "What was MRR at the start and end of last month, and how much churn happened in between?"
- **Payment failures.** "Which customers had a failed charge in the last two weeks, and did any recover?"
- **Dispute triage.** "How many disputes are open, what is the total value, and what type are they?"
- **Payout reconciliation.** "Which payouts landed this month, and what charges do they cover?"
- **Benchmark context.** "Our voluntary churn is 2.1 percent monthly. What is normal for self-serve SaaS at our price point?"
- **Read-only by key.** A restricted key with read permissions cannot create a charge, issue a refund or change a customer.

### How It Works

1. **Create a restricted Stripe key** with read-only permissions and paste it into the CorpusIQ connector.
2. **Add CorpusIQ to Perplexity** as a custom remote MCP server, using the endpoint from your CorpusIQ account settings.
3. **CorpusIQ reads** balances, charges, customers, subscriptions, payouts, refunds and disputes.
4. **Perplexity answers** with your figures plus the outside context you asked for.

Direct MCP retrieval is read-only. It does not retain raw customer files or full connector response payloads; operational query logs are kept for up to 30 days.

### Setup Steps

**In Stripe**

1. Open **Developers**, then **API keys**, and create a **restricted key**.
2. Grant read-only permissions for Charges, Customers, Subscriptions, Payouts, Balance, Refunds and Disputes.
3. Copy the key.

**In CorpusIQ**

4. Open your dashboard and go to **Connectors**.
5. Select **Stripe**, paste the restricted key and save. The connector turns green.

**In Perplexity**

6. Open **Settings** and find the **MCP servers** section.
7. Add a custom MCP server and paste the endpoint:

```
https://mcp2.corpusiq.io/mcp
```

8. Connect and approve the CorpusIQ authorization page once.
9. Start a new thread and ask a payment question.

A restricted key is narrower than an account key at every level. Grant only the resources a question would read.

### Example Perplexity Questions

**Revenue**

- "What was gross revenue last month, and how much came from new versus returning customers?"
- "What is the total value of active subscriptions right now, and how has it moved over 90 days?"
- "Which plans generate the most revenue per customer?"

**Churn and recovery**

- "How many subscriptions canceled last month, and what was the churned MRR?"
- "Which failed charges recovered after a retry, and which did not?"
- "Our monthly churn is 2.1 percent. How does that compare to self-serve SaaS at our price point?"

**Operations**

- "How many disputes are open, of what type, and what value?"
- "Which refunds were issued in the last 30 days, and by which customer?"

**Cross-source**

- "Do the customers who churned in Stripe still have open deals in the CRM?" (requires the CRM connector)
- "Compare Stripe revenue to Shopify payouts for the same month." (requires the Shopify connector)

### Security

- **Restricted API key.** Read-only permissions on named resources. A resource you did not grant is unreadable, and the key cannot move money.
- **Encrypted at rest.** The key is stored encrypted and used only for retrieval.
- **Revocable in seconds.** Roll or delete the restricted key in Stripe and the connection ends immediately.
- **Scoped direct-MCP retention.** Raw customer files and full connector payloads are not retained. Operational logs keep query text and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Stripe, CorpusIQ and Perplexity.

### Comparison: Stripe Dashboard vs Stripe in Perplexity

| Aspect | Stripe dashboard | CorpusIQ MCP with Perplexity |
|---|---|---|
| Input | A filter and a date range | A question in plain language |
| Output | Charts and transaction lists | An answer with the period named |
| Benchmark context | Look it up separately | Same thread, same answer |
| Cross-system | Export and join by hand | Asked across connectors |
| Follow-up | Rebuild the filter | Ask the next question |
| Write access | Yes, by you | None, read-only |

### FAQ: Common Questions

<details>
<summary><strong>Can Perplexity issue a refund or create a charge?</strong></summary>

No. The restricted key carries read permissions only. Money movement is impossible through this connection.
</details>

<details>
<summary><strong>Should I use my account secret key?</strong></summary>

No. Use a restricted key scoped to the resources the questions need. An account secret key is broader than the connector requires.
</details>

<details>
<summary><strong>Does it read customer card data?</strong></summary>

No. Payment credentials live with Stripe and are never exposed through the API surface the connector reads.
</details>

<details>
<summary><strong>Does it cover multiple Stripe accounts?</strong></summary>

Each Stripe account is a separate connection with its own key. A question only reaches accounts you connected.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Live. A charge created a minute ago is visible to the next question.
</details>

<details>
<summary><strong>Does this work only in Perplexity?</strong></summary>

No. Stripe is exposed to ChatGPT, Claude and Perplexity through the same endpoint on the same subscription.
</details>

<details>
<summary><strong>Where is the payment data stored?</strong></summary>

CorpusIQ does not retain raw customer files or full connector response payloads. Operational logs may persist for up to 30 days. See the [read-only and security documentation](/hermes/security/read-only-and-security).
</details>

---

**Next steps:** [Connect Stripe to Perplexity now](https://www.corpusiq.io/connectors/perplexity)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.CorpusIQ.io).*
