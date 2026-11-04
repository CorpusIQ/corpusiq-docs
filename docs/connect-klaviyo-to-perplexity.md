---
title: "Connect Klaviyo to Perplexity via MCP"
description: "Connect Klaviyo to Perplexity through CorpusIQ MCP. Ask what email and SMS actually earned, which flows recover carts and how the list is growing."
category: Perplexity Integrations
tags: ["connect Klaviyo to Perplexity", "Klaviyo Perplexity integration", "MCP Klaviyo connector", "email revenue attribution", "Klaviyo data to AI", "CorpusIQ MCP"]
last_updated: "2026-11-04"
canonical: "https://www.corpusiq.io/docs/connect-klaviyo-to-perplexity"
robots: "index,follow"
---

# How to Connect Klaviyo to Perplexity with CorpusIQ MCP

For an ecommerce brand, Klaviyo is where email and SMS revenue actually gets attributed. Campaigns, flows, abandoned carts, list health, predictive values.

The dashboard shows you the numbers it decided to show you. The question you actually have usually needs three of them at once, plus Shopify.

Connecting Klaviyo through CorpusIQ MCP makes that answerable inside a Perplexity thread, read-only.

### Why Connect Klaviyo to Perplexity?

- **Attribution.** "How much revenue did email and SMS drive last month, split campaigns and flows?"
- **Flow health.** "Which abandoned cart flow earns the most, and what is its conversion rate?"
- **List quality.** "Is the list growing or shrinking, and how many profiles are engaged?"
- **Campaign comparison.** "Which three campaigns had the highest revenue per recipient this quarter?"
- **Cross-source truth.** "Compare email-attributed revenue against Shopify totals for the same period."
- **Read-only by scope.** The private key carries read scopes. It cannot send, edit, or delete anything.

### How It Works

1. **Connect Klaviyo to CorpusIQ** with a private API key that has read scopes on the objects you want queried.
2. **Add CorpusIQ to Perplexity** as a custom remote MCP server, using the endpoint from your CorpusIQ account settings.
3. **CorpusIQ queries** campaigns, flows, lists, segments, profiles, metrics, forms, and events as the question requires.
4. **Perplexity answers** from those results and names the period it measured.

Direct MCP retrieval is read-only. It does not retain raw customer files or full connector response payloads; operational query logs are retained for up to 30 days.

### Setup Steps

**In Klaviyo**

1. Go to **Account, Settings, API keys** and create a private API key.
2. Give it read scopes on Campaigns, Flows, Lists, Segments, Profiles, Metrics, Forms, and Events.

**In CorpusIQ**

3. Open your dashboard, find **Klaviyo**, and click **Connect**.
4. Paste the private key and save.

**In Perplexity**

5. Open **Settings** and find the **MCP servers** section.
6. Add a custom MCP server and paste the endpoint:

```
https://mcp2.corpusiq.io/mcp
```

7. Connect and approve the CorpusIQ authorization page once.
8. Start a new thread and ask a revenue question.

A `403 Forbidden` on the first question means the key is missing a read scope. Recreate it with every scope listed above rather than guessing which one is missing.

### Example Perplexity Questions

**Revenue and attribution**

- "How much revenue did email drive last month, split campaigns and flows?"
- "Which campaign had the best revenue per recipient this quarter?"
- "How much SMS revenue did we book in the last 90 days?"

**Flows**

- "Which abandoned cart flow earns the most, and what is its conversion rate?"
- "How many profiles entered the welcome flow this month, and how many converted?"
- "Which flow has the highest revenue per recipient?"

**List health**

- "Is the list growing or shrinking this quarter?"
- "How many profiles are engaged versus dormant?"
- "Which segments have grown fastest in 90 days?"

**Cross-source**

- "Compare email-attributed revenue to Shopify totals for last month." (requires the Shopify connector)
- "Which email-attributed orders are missing from GA4 sessions?" (requires the GA4 connector)

### Security

- **Read scopes only.** The private key carries read permissions on the listed objects. There is no path from Perplexity that sends, edits, or deletes anything in Klaviyo.
- **Revocable at any time.** Delete the key in Klaviyo and the connection ends immediately.
- **Account-scoped.** Access follows the key. A Klaviyo account you have not connected stays out of reach.
- **Scoped direct-MCP retention.** Raw customer files and full connector payloads are not retained. Operational logs keep query text and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Klaviyo, CorpusIQ, and Perplexity.

### Comparison: Klaviyo Dashboards vs Klaviyo in Perplexity

| Aspect | Klaviyo reporting | CorpusIQ MCP with Perplexity |
|---|---|---|
| Input | Pick a report and configure it | A question about performance |
| Output | Metrics you then interpret | An answer with the period named |
| Cross-period | Rebuild the report | Asked as a comparison |
| Cross-source | Export to a spreadsheet | Asked across connectors |
| Ad-hoc questions | New report or an export | Just ask |
| Write access | Full, by you | None, read scopes only |

Reports are built for recurring views. The connector is for the question that arrives once.

### FAQ: Common Questions

<details>
<summary><strong>Can Perplexity send or edit a campaign?</strong></summary>

No. The key carries read scopes and the connector has no send or write tool. Campaigns, flows, and lists are read-only.
</details>

<details>
<summary><strong>Why do I get a 403 Forbidden?</strong></summary>

The private key is missing at least one read scope. Recreate the key with read access on Campaigns, Flows, Lists, Segments, Profiles, Metrics, Forms, and Events.
</details>

<details>
<summary><strong>How far back can I ask about revenue?</strong></summary>

Over the range you specify, as far back as the Klaviyo account retains the data. Naming a period gives the tightest answer.
</details>

<details>
<summary><strong>Does "email revenue" mean the same thing as Shopify revenue?</strong></summary>

No, and that gap is the usual source of confusion. Klaviyo attributes revenue to the message that drove the session, while Shopify records the order. Asking both connectors the same question is how you see the difference instead of arguing about it.
</details>

<details>
<summary><strong>Can it segment by campaign and by flow in one answer?</strong></summary>

Yes. Campaigns and flows are separate objects, and one question can ask for both and get them split in the reply.
</details>

<details>
<summary><strong>Does this work only in Perplexity?</strong></summary>

No. Klaviyo is exposed to ChatGPT, Claude, and Perplexity through the same endpoint on the same subscription.
</details>

<details>
<summary><strong>Where is the Klaviyo data stored?</strong></summary>

CorpusIQ does not retain raw customer files or full connector response payloads. Operational logs may persist for up to 30 days. See the [security documentation](/hermes/security/read-only-and-security).
</details>

---

**Next steps:** [Connect Klaviyo to Perplexity now](https://corpusiq.io/connect/klaviyo-with-perplexity)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
