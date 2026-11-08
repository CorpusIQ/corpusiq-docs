---
title: "Connect Semrush to Perplexity via MCP"
description: "Connect Semrush to Perplexity through CorpusIQ MCP. Ask which keywords a competitor ranks for, who links to them and where your organic ground is going."
category: Perplexity Integrations
tags: ["connect Semrush to Perplexity", "Semrush Perplexity integration", "MCP Semrush connector", "keyword research", "backlink profile", "CorpusIQ MCP"]
last_updated: "2026-11-05"
canonical: "https://www.corpusiq.io/docs/connect-semrush-to-perplexity"
robots: "index,follow"
---

# How to Connect Semrush to Perplexity with CorpusIQ MCP

Semrush answers questions about search that no other surface in the business can answer. Which keywords a competitor holds, who links to them, what a term costs to bid on, and which pages are losing ground month by month.

The interface is built around choosing a report first. Most real questions start somewhere else, with a domain and a suspicion.

Connecting Semrush through CorpusIQ MCP puts that data in a Perplexity thread where the question comes first, read-only.

### Why Connect Semrush to Perplexity?

- **Competitor keywords.** "What organic keywords does competitor.com rank for that we do not?"
- **Own position.** "Show me my domain's organic and paid traffic trend for the last six months."
- **Backlinks.** "How does our referring domain count compare to competitor.com?"
- **Demand sizing.** "What is the search volume and CPC for a term we are considering?"
- **Competitive set.** "Who are our top organic competitors, and how far ahead are they?"
- **History.** "Which of our pages lost the most organic traffic between these two snapshots?"
- **Read-only by scope.** The API key reads report data. It cannot change a project, a campaign, or a listing.

### How It Works

1. **Connect Semrush to CorpusIQ** with an API key from an account whose plan includes API access.
2. **Add CorpusIQ to Perplexity** as a custom remote MCP server, using the endpoint from your CorpusIQ account settings.
3. **CorpusIQ queries** domain overview, organic and paid keywords, the organic competitor list, backlink overview, keyword research, and domain history as the question requires.
4. **Perplexity answers** from those reports and names the domain and period it measured.

Direct MCP retrieval is read-only. It does not retain raw customer files or full connector response payloads; operational query logs are retained for up to 30 days.

### Setup Steps

**In Semrush**

1. Open your profile and go to **Subscription info**, then **API units**.
2. Copy the API key. API access requires the Business plan or higher.

**In CorpusIQ**

3. Open your dashboard, find **Semrush**, and click **Connect**.
4. Paste the API key and save.

**In Perplexity**

5. Open **Settings** and find the **MCP servers** section.
6. Add a custom MCP server and paste the endpoint:

```
https://mcp2.corpusiq.io/mcp
```

7. Connect and approve the CorpusIQ authorization page once.
8. Start a new thread and ask a competitor question.

Semrush bills each report in API units. A narrow question, one domain and one metric family, costs less than a broad one and usually answers more precisely.

### Example Perplexity Questions

**Competitor keywords**

- "What organic keywords does competitor.com rank for that we do not?"
- "Which competitor pages rank in the top three for our head terms?"
- "Show me the paid keywords competitor.com bids on."

**Own organic position**

- "Show me my domain's SEO overview for the last six months."
- "Which of my pages lost the most organic traffic between these snapshots?"
- "What is our estimated organic traffic split by country?"

**Backlinks**

- "How does our referring domain count compare to competitor.com?"
- "Which sites link to both domains?"
- "Has our authority score moved in the last quarter?"

**Demand and planning**

- "What is the search volume, CPC and difficulty for a term we are considering?"
- "Which related terms have volume above a threshold and difficulty below one?"
- "How seasonal is this term across twelve months?"

**Cross-source**

- "Does the organic traffic in Semrush match the sessions Search Console reports for last quarter?" (requires the Google Search Console connector)
- "Which Semrush keyword gaps map to pages our sitemap already covers?" (requires a sitemap read)

### Security

- **Read access only.** The key reads report data. There is no path from Perplexity that edits a project, a campaign, or a listing.
- **Revocable at any time.** Regenerate the key in Semrush and the connection ends immediately.
- **Account-scoped.** Access follows the key. A Semrush account you have not connected stays out of reach.
- **Unit budget stays yours.** CorpusIQ only spends units on the queries you ask for. There is no background crawl.
- **Scoped direct-MCP retention.** Raw customer files and full connector payloads are not retained. Operational logs keep query text and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Semrush, CorpusIQ, and Perplexity.

### Comparison: Semrush Reports vs Semrush in Perplexity

| Aspect | Semrush reports | CorpusIQ MCP with Perplexity |
|---|---|---|
| Input | Choose a report and a domain | A question about a domain |
| Output | Tables you then interpret | An answer with the domain named |
| Across domains | One report per domain | Asked as a comparison |
| Cross-source | Export and reconcile by hand | Asked across connectors |
| Ad-hoc questions | Build a new report | Just ask |
| Write access | Full, by you | None, read only |

Reports are built for tracking a plan. The connector is for the question that starts with a suspicion.

### FAQ: Common Questions

<details>
<summary><strong>Why does Semrush say the API key is invalid?</strong></summary>

API access requires the Business plan or higher, and the account must have API units left. Both conditions fail with the same message.
</details>

<details>
<summary><strong>Will asking questions burn my API units?</strong></summary>

Yes, each report costs units. Ask narrow questions: one domain, one metric family, one period. That is cheaper and more precise than a broad sweep.
</details>

<details>
<summary><strong>Why is there no data for a domain?</strong></summary>

Semrush data lags reality, and very new domains may not be indexed yet. Check the domain in the Semrush interface before assuming a connection problem.
</details>

<details>
<summary><strong>Can it change anything in Semrush?</strong></summary>

No. The key reads report data and the connector has no write tool. Projects, campaigns, and listings are untouched.
</details>

<details>
<summary><strong>Does this work only in Perplexity?</strong></summary>

No. Semrush is exposed to ChatGPT, Claude, and Perplexity through the same endpoint on the same subscription.
</details>

<details>
<summary><strong>Where is the Semrush data stored?</strong></summary>

CorpusIQ does not retain raw customer files or full connector response payloads. Operational logs may persist for up to 30 days. See the [security documentation](/hermes/security/read-only-and-security).
</details>

---

**Next steps:** [Connect Semrush to Perplexity now](https://corpusiq.io/connect/semrush-with-perplexity)

**Also in ChatGPT:** [Connect Semrush to ChatGPT](connect-semrush-to-chatgpt.md) - competitor keywords, backlinks and demand sizing inside a ChatGPT thread.

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
