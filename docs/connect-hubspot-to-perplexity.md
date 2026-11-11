---
title: "Connect HubSpot to Perplexity via MCP"
description: "Connect HubSpot to Perplexity through CorpusIQ MCP. Ask about pipeline, deal health and stalled contacts and get answers cited to your own CRM records"
category: Perplexity Integrations
tags: ["connect HubSpot to Perplexity", "HubSpot Perplexity integration", "MCP HubSpot connector", "CRM data to AI", "ask HubSpot in plain English", "CorpusIQ MCP"]
last_updated: "2026-11-11"
canonical: "https://www.corpusiq.io/docs/connect-hubspot-to-perplexity"
robots: "index,follow"
---

# How to Connect HubSpot to Perplexity with CorpusIQ MCP

Your CRM knows which deals are moving and which have gone quiet. It does not know what happened in the market that explains it.

Perplexity knows the market and nothing about your pipeline.

Connecting HubSpot through CorpusIQ MCP puts the two in the same thread. Pipeline questions are answered from your own records, read-only, with the deal names and stages cited.

### Why Connect HubSpot to Perplexity?

- **Pipeline reviews.** "Which deals over 20 thousand dollars have had no activity in three weeks?"
- **Stage conversion.** "What is our conversion rate from demo to closed won this quarter, and what is normal for our deal size?"
- **Stalled accounts.** "Which companies have an open deal but no contact in the last 14 days?"
- **Forecast framing.** "Our win rate is 22 percent. What close rate is typical for deals at this size?"
- **Owner performance.** "Which reps have the most deals stuck in negotiation?"
- **Read-only by scope.** The OAuth grant covers contacts, companies and deals. It cannot edit a record or move a stage.

### How It Works

1. **Connect HubSpot to CorpusIQ** through HubSpot's OAuth screen, granting read-only access to contacts, companies, deals and associated records.
2. **Add CorpusIQ to Perplexity** as a custom remote MCP server, using the endpoint from your CorpusIQ account settings.
3. **CorpusIQ reads** the deals, companies and contacts that answer the question.
4. **Perplexity answers** with your pipeline figures plus the outside context you asked for.

Direct MCP retrieval is read-only. It does not retain raw customer files or full connector response payloads; operational query logs are kept for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log into your dashboard and open **Connectors**.
2. Select **HubSpot** and click **Connect HubSpot**.
3. You are redirected to HubSpot's OAuth screen. Authorize read-only access to contacts, companies, deals and associated records.
4. Return to CorpusIQ. CRM questions work immediately.

**In Perplexity**

5. Open **Settings** and find the **MCP servers** section.
6. Add a custom MCP server and paste the endpoint:

```
https://mcp2.corpusiq.io/mcp
```

7. Connect and approve the CorpusIQ authorization page once.
8. Start a new thread and ask a question about a deal or a company.

### Example Perplexity Questions

**Pipeline health**

- "Which open deals over 20 thousand dollars have had no activity in 21 days?"
- "What is the total value of deals sitting in negotiation right now?"
- "Which deals have slipped their close date more than once?"

**Conversion and forecast**

- "What is our demo-to-won conversion this quarter, and how does it compare to the same quarter last year?"
- "Our win rate is 22 percent. How does that compare to similar deal sizes in B2B software?"
- "Which stage loses the most deals by value?"

**Owners and activity**

- "Which reps have the highest number of stale deals?"
- "Which companies have an open deal and no logged call in two weeks?"

**Cross-source**

- "Do the companies with stale deals still owe us money in accounting?" (requires the accounting connector)
- "Which stalled accounts have open support tickets?" (requires the support connector)

### Security

- **Read-only retrieval tools.** The tools documented on this page are marked read-only, and the grant covers read access to contacts, companies, deals and associations. There is no write path from Perplexity into the CRM.
- **Object-level scoping.** Marketing Hub and Service Hub objects can require additional scope, so a connection that does not need them does not ask for them.
- **Property-level limits.** HubSpot permission sets can narrow what the OAuth app sees beyond the object scopes.
- **Scoped direct-MCP retention.** Raw customer files and full connector payloads are not retained. Operational logs keep query text and bounded outcome summaries for up to 30 days.
- **TLS in transit** between HubSpot, CorpusIQ and Perplexity.

### Comparison: HubSpot Reports vs HubSpot in Perplexity

| Aspect | HubSpot reports and boards | CorpusIQ MCP with Perplexity |
|---|---|---|
| Input | A report or a saved view | A question in plain language |
| Output | A table of records | An answer naming the deals |
| Outside context | Look it up separately | Same thread, same answer |
| Cross-system | Manual export | Asked across connectors |
| Follow-up | Rebuild the view | Ask the next question |
| Write access | Yes, by you | None, read-only |

### FAQ: Common Questions

<details>
<summary><strong>Can Perplexity change a deal stage or edit a contact?</strong></summary>

No. The retrieval tools are marked read-only, so the connection cannot edit a record or move a stage. Records, associations and pipeline stages are untouched.
</details>

<details>
<summary><strong>Does it read every HubSpot object?</strong></summary>

It reads contacts, companies and deals, plus their associations. Marketing Hub and Service Hub objects may need additional scope before they are visible.
</details>

<details>
<summary><strong>Will it see contacts outside my team's pipeline?</strong></summary>

It sees what the authorizing account can see. If you need a narrower view, use HubSpot permission sets on the OAuth app.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Live. A deal moved a minute ago is reflected in the next answer.
</details>

<details>
<summary><strong>Does this work only in Perplexity?</strong></summary>

No. HubSpot is exposed to ChatGPT, Claude and Perplexity through the same endpoint on the same subscription.
</details>

<details>
<summary><strong>Can I use it for forecasting?</strong></summary>

For reading the pipeline and comparing it to external benchmarks, yes. It does not replace weighted forecasting inside HubSpot, because it never writes back.
</details>

<details>
<summary><strong>Where is the CRM data stored?</strong></summary>

CorpusIQ does not retain raw customer files or full connector response payloads. Operational logs may persist for up to 30 days. See the [read-only and security documentation](/hermes/security/read-only-and-security).
</details>

---

**Next steps:** [Connect HubSpot to Perplexity now](https://corpusiq.io/connect/hubspot-with-perplexity)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.CorpusIQ.io).*
