---
title: "Connect Airtable to Perplexity via MCP"
description: "Connect Airtable to Perplexity through CorpusIQ MCP. Ask about roadmaps, hiring pipelines and trackers and get answers cited to the base and table used."
category: Perplexity Integrations
tags: ["connect Airtable to Perplexity", "Airtable Perplexity integration", "MCP Airtable connector", "Airtable data to AI", "query Airtable in plain English", "CorpusIQ MCP"]
last_updated: "2026-11-04"
canonical: "https://www.corpusiq.io/docs/connect-airtable-to-perplexity"
robots: "index,follow"
---

# How to Connect Airtable to Perplexity with CorpusIQ MCP

Airtable holds the operating data that never made it into a real SaaS tool. The content calendar, the hiring pipeline, the partnership tracker, the product roadmap.

None of it reaches your other systems, and none of it reaches your AI unless somebody exports a view.

Connecting Airtable through CorpusIQ MCP makes those bases answerable inside a Perplexity thread, read-only, with the answer naming the base and table it came from.

### Why Connect Airtable to Perplexity?

- **Roadmap truth.** "What is shipping this month and what is still blocked?"
- **Pipeline reads.** "Which candidates are in final round, and how long have they been there?"
- **Tracker questions.** "Which partnership conversations have no activity in 21 days?"
- **Content operations.** "How many posts are scheduled for next month, by channel?"
- **Cross-system answers.** "Do the accounts marked at-risk in Airtable have open support tickets?"
- **Read-only by scope.** The token grants read on records and schema. It cannot write, edit, or delete.

### How It Works

1. **Connect Airtable to CorpusIQ** by pasting a personal access token scoped to the bases you want visible.
2. **Add CorpusIQ to Perplexity** as a custom remote MCP server, using the endpoint from your CorpusIQ account settings.
3. **CorpusIQ reads** the records that answer the question, from the bases the token can see.
4. **Perplexity answers** from those records, naming the base and table used.

Direct MCP retrieval is read-only. It does not retain raw customer files or full connector response payloads; operational query logs are retained for up to 30 days.

### Setup Steps

**In Airtable**

1. Go to `airtable.com/create/tokens` and create a personal access token.
2. Give it the scopes `data.records:read` and `schema.bases:read`.
3. Grant access to the specific bases you want CorpusIQ to see, not all of them.

**In CorpusIQ**

4. Open your dashboard, find **Airtable**, and click **Connect**.
5. Paste the token and save. The connector turns green.

**In Perplexity**

6. Open **Settings** and find the **MCP servers** section.
7. Add a custom MCP server and paste the endpoint:

```
https://mcp2.corpusiq.io/mcp
```

8. Connect and approve the CorpusIQ authorization page once.
9. Start a new thread and ask a question about a base.

Scoping the token to named bases is the strongest control you have here. A base you did not grant stays invisible to the connector.

### Example Perplexity Questions

**Product and roadmap**

- "What is shipping this month, and which items are blocked?"
- "Which roadmap items have no owner?"
- "What changed in the roadmap since last month?"

**Hiring**

- "How many candidates are in final round, and who has been waiting longest?"
- "Which roles have zero candidates in the last two weeks?"

**Partnerships and accounts**

- "Which partnership conversations have had no activity in 21 days?"
- "List accounts marked at-risk with the owner for each."

**Content operations**

- "How many posts are scheduled next month, by channel?"
- "Which drafts are past their due date?"

**Cross-source**

- "Do the at-risk accounts in Airtable have open invoices in billing?" (requires the billing connector)

### Security

- **Read-only scopes.** The token carries `data.records:read` and `schema.bases:read`. There is no write path from Perplexity into Airtable.
- **Base-level scoping.** Grant only the bases a question would use. Everything else is out of reach.
- **Revocable at any time.** Delete the token in Airtable and the connection ends immediately.
- **Scoped direct-MCP retention.** Raw customer files and full connector payloads are not retained. Operational logs keep query text and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Airtable, CorpusIQ, and Perplexity.

### Comparison: Airtable Views vs Airtable in Perplexity

| Aspect | Airtable views and filters | CorpusIQ MCP with Perplexity |
|---|---|---|
| Input | A filter you configure | A question in plain language |
| Output | Rows to read | A summarized answer naming the table |
| Across bases | One base at a time | Asked across granted bases |
| Cross-system | Export and join manually | Asked across connectors |
| Time-based questions | Manual date filters | Asked as a range |
| Write access | Yes, by you | None, read-only |

A view answers a question you already knew how to filter. A connected Airtable answers the one you did not.

### FAQ: Common Questions

<details>
<summary><strong>Can Perplexity change my Airtable records?</strong></summary>

No. The token is read-only by scope. Records, fields, and schema are untouched.
</details>

<details>
<summary><strong>Does it need access to every base?</strong></summary>

No, and it should not have it. Airtable lets you grant a token access to specific bases. Only those bases are readable through the connector.
</details>

<details>
<summary><strong>What happens when the token is rotated?</strong></summary>

The connection stops working until the new token is pasted into CorpusIQ. That is the intended behaviour of a revocable credential.
</details>

<details>
<summary><strong>Are linked records and attachments readable?</strong></summary>

Records and their field values are readable within the granted scopes. Linked records appear as their references, so a question that spans two linked tables can be answered in one go.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Live. A record edited a minute ago is visible to the next question. There is no nightly copy.
</details>

<details>
<summary><strong>Does this work only in Perplexity?</strong></summary>

No. Airtable is exposed to ChatGPT, Claude, and Perplexity through the same endpoint on the same subscription.
</details>

<details>
<summary><strong>Where is the Airtable data stored?</strong></summary>

CorpusIQ does not retain raw customer files or full connector response payloads. Operational logs may persist for up to 30 days. See the [security documentation](/hermes/security/read-only-and-security).
</details>

---

**Next steps:** [Connect Airtable to Perplexity now](https://corpusiq.io/connect/airtable-with-perplexity)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
