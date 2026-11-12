---
title: "Connect ActiveCampaign to Perplexity via MCP"
description: "Connect ActiveCampaign to Perplexity through CorpusIQ MCP. Ask which campaigns earned, which automations carry the pipeline and how deals are moving."
category: Perplexity Integrations
tags: ["connect ActiveCampaign to Perplexity", "ActiveCampaign Perplexity integration", "MCP ActiveCampaign connector", "email campaign performance", "automation health", "CorpusIQ MCP"]
last_updated: "2026-11-08"
canonical: "https://www.corpusiq.io/docs/connect-activecampaign-to-perplexity"
robots: "index,follow"
---

# How to Connect ActiveCampaign to Perplexity with CorpusIQ MCP

ActiveCampaign holds the moving part of a sales and marketing motion. Contacts, lists, tags, campaigns, automations, and the deals sitting in your pipeline.

Most teams can see one of those at a time. The campaign report lives in one screen, the automation list in another, the deals in a third, and the question you actually have spans all three.

Connecting ActiveCampaign through CorpusIQ MCP makes that question answerable inside a Perplexity thread, read-only.

### Why Connect ActiveCampaign to Perplexity?

- **Campaign performance.** "How did last month's newsletter perform, by opens, clicks and unsubscribes?"
- **Automation weight.** "Which automations have the most active contacts right now?"
- **Pipeline age.** "Show me deals that have been open longer than 30 days."
- **List shape.** "How big is each list, and which tags are used most?"
- **Contact lookup.** "Find every contact tagged 'webinar-april'."
- **Cross-source truth.** "Compare email-attributed revenue against Shopify totals for the same period."
- **Read-only by scope.** The API key is read access. It cannot send mail, edit a contact, or change an automation.

### How It Works

1. **Connect ActiveCampaign to CorpusIQ** with your account API URL and API key.
2. **Add CorpusIQ to Perplexity** as a custom remote MCP server, using the endpoint from your CorpusIQ account settings.
3. **CorpusIQ queries** contacts, lists, tags, campaigns, automations, deals, and account details as the question requires.
4. **Perplexity answers** from those results and names the period it measured.

Direct MCP retrieval is read-only. It does not retain raw customer files or full connector response payloads; operational query logs are retained for up to 30 days.

### Setup Steps

**In ActiveCampaign**

1. Sign in and go to **Settings**, then **Developer**.
2. Copy your **API URL** and your **API key**.

**In CorpusIQ**

3. Open your dashboard, find **ActiveCampaign**, and click **Connect**.
4. Paste the API URL and the API key, then save.

**In Perplexity**

5. Open **Settings** and find the **MCP servers** section.
6. Add a custom MCP server and paste the endpoint:

```
https://mcp2.corpusiq.io/mcp
```

7. Connect and approve the CorpusIQ authorization page once.
8. Start a new thread and ask a campaign question.

The API URL is your full account URL, in the form `https://youraccount.api-us1.com`. A dashboard URL pasted into that field is the most common reason a connection refuses to save.

### Example Perplexity Questions

**Campaign performance**

- "How did my last campaign perform on opens, clicks and unsubscribes?"
- "Which three campaigns had the best click rate this quarter?"
- "How many contacts did we unsubscribe last month, and from which list?"

**Automations**

- "Which automations have the most active contacts right now?"
- "List every automation and the list it is attached to."
- "Which automation has not changed in the longest time?"

**Pipeline**

- "Show me deals open longer than 30 days, with their values."
- "How many deals moved stage this month?"
- "What is the total value of deals in each stage?"

**Lists and contacts**

- "How big is each list, and how many are engaged?"
- "Find every contact tagged 'webinar-april'."
- "Which tags are applied most often across the account?"

**Cross-source**

- "Compare email-attributed revenue against Shopify totals for last month." (requires the Shopify connector)
- "Which contacts in ActiveCampaign also exist as customers in Stripe?" (requires the Stripe connector)

### Security

- **Read access only.** The API key reads the objects listed above. There is no path from Perplexity that sends mail, edits a contact, or changes an automation.
- **Revocable at any time.** Regenerate or delete the key in ActiveCampaign and the connection ends immediately.
- **Account-scoped.** Access follows the key and the API URL. An ActiveCampaign account you have not connected stays out of reach.
- **Scoped direct-MCP retention.** Raw customer files and full connector payloads are not retained. Operational logs keep query text and bounded outcome summaries for up to 30 days.
- **TLS in transit** between ActiveCampaign, CorpusIQ, and Perplexity.

### Comparison: ActiveCampaign Screens vs ActiveCampaign in Perplexity

| Aspect | ActiveCampaign reporting | CorpusIQ MCP with Perplexity |
|---|---|---|
| Input | Pick a report and configure it | A question about performance |
| Output | Metrics you then interpret | An answer with the period named |
| Cross-object | Switch between contacts, campaigns and deals | Asked in one question |
| Cross-source | Export to a spreadsheet | Asked across connectors |
| Ad-hoc questions | New report or an export | Just ask |
| Write access | Full, by you | None, read access only |

The screens are built for recurring views. The connector is for the question that arrives once.

### FAQ: Common Questions

<details>
<summary><strong>Can Perplexity send an email or change an automation?</strong></summary>

No. The key carries read access and the connector has no send or write tool. Campaigns, automations, contacts, and deals are read-only.
</details>

<details>
<summary><strong>Why does the connection refuse my API key?</strong></summary>

Two fields have to be right. The key itself is under Settings, Developer, and the API URL must be the full account URL in the form `https://youraccount.api-us1.com`, not the dashboard address you use in a browser.
</details>

<details>
<summary><strong>Why is a campaign list empty?</strong></summary>

The API user behind the key may not have permission for the campaign view. Switch to an admin-level key and reconnect.
</details>

<details>
<summary><strong>Can it tell me which automation is actually working?</strong></summary>

It can tell you what the account records: how many contacts sit in each automation and how they move. Revenue attribution depends on whether you have revenue tracking configured in ActiveCampaign, so ask both the automation question and the revenue question when you need the second one.
</details>

<details>
<summary><strong>Does this work only in Perplexity?</strong></summary>

No. ActiveCampaign is exposed to ChatGPT, Claude, and Perplexity through the same endpoint on the same subscription.
</details>

<details>
<summary><strong>Where is the ActiveCampaign data stored?</strong></summary>

CorpusIQ does not retain raw customer files or full connector response payloads. Operational logs may persist for up to 30 days. See the [security documentation](/hermes/security/read-only-and-security).
</details>

---

**Next steps:** [Connect ActiveCampaign to Perplexity now](https://corpusiq.io/connect/activecampaign-with-perplexity)

**Also in ChatGPT:** [Connect ActiveCampaign to ChatGPT](connect-activecampaign-to-chatgpt.md) - campaign, automation and pipeline questions inside a ChatGPT thread.

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
