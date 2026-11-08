---
title: "Connect Ahrefs to Perplexity via MCP"
description: "Connect Ahrefs to Perplexity through CorpusIQ MCP. Ask about domain ratings, ranking keywords and referring domains and get the numbers cited to the source."
category: Perplexity Integrations
tags: ["connect Ahrefs to Perplexity", "Ahrefs Perplexity integration", "MCP Ahrefs connector", "SEO data to AI", "backlink analysis with AI", "CorpusIQ MCP"]
last_updated: "2026-11-04"
canonical: "https://www.corpusiq.io/docs/connect-ahrefs-to-perplexity"
robots: "index,follow"
---

# How to Connect Ahrefs to Perplexity with CorpusIQ MCP

SEO work runs on numbers that live in one place and reasoning that happens in another. The numbers are in Ahrefs. The reasoning happens in whatever tool you think in.

Getting from one to the other usually means an export, a screenshot, or a manual copy into a chat.

Connecting Ahrefs through CorpusIQ MCP removes that step. You ask the question in a Perplexity thread, the connector pulls the metric, and the answer names the domain and the period it measured.

### Why Connect Ahrefs to Perplexity?

- **Competitor framing.** "How does our Domain Rating compare with these three competitors?"
- **Keyword surface.** "Which keywords does our domain rank for in the top ten?"
- **Link gap.** "Which referring domains link to the competitor but not to us?"
- **Content bets.** "What are the highest-traffic pages on their site?"
- **Research plus data.** A Perplexity thread can search the web and check your Ahrefs numbers in the same answer.
- **Read-only by scope.** The token reads. It cannot change anything in your Ahrefs account.

### How It Works

1. **Connect Ahrefs to CorpusIQ** by pasting an API token from your Ahrefs account.
2. **Add CorpusIQ to Perplexity** as a custom remote MCP server, using the endpoint from your CorpusIQ account settings.
3. **CorpusIQ queries** the Ahrefs endpoints that answer the question: domain overview, organic keywords, backlinks, referring domains, competitors, top pages, or keyword metrics.
4. **Perplexity answers** from those results, naming the domain measured.

Read-only. CorpusIQ does not consume Ahrefs API rows beyond the queries you ask for, and direct MCP does not retain full connector response payloads.

### Setup Steps

**In Ahrefs**

1. Go to **Settings, API** and copy your API token. API access requires the Advanced plan or higher.

**In CorpusIQ**

2. Open your dashboard, find **Ahrefs**, and click **Connect**.
3. Paste the token and save. The connector turns green.

**In Perplexity**

4. Open **Settings** and find the **MCP servers** section.
5. Add a custom MCP server and paste the endpoint:

```
https://mcp2.corpusiq.io/mcp
```

6. Connect and approve the CorpusIQ authorization page once.
7. Start a new thread and ask an SEO question.

An "API token invalid" response almost always means the plan does not include API access, or the token was rotated after it was pasted.

### Example Perplexity Questions

**Domain and authority**

- "What is the Domain Rating for competitor.com, and how many referring domains does it have?"
- "Compare our Domain Rating to these three competitors."
- "Which domains gained the most referring domains this quarter?"

**Keywords**

- "Which keywords does our domain rank for in the top ten, with volume and position?"
- "What is the keyword difficulty and CPC for these five terms?"
- "Which keywords does the competitor rank for that we do not?"

**Links**

- "Show the top referring domains linking to our site, with Domain Rating for each."
- "Which referring domains link to the competitor but not to us?"
- "What is our total backlink count and how has it changed?"

**Content**

- "What are the highest-traffic pages on competitor.com?"
- "Who are our top organic competitors?"

### Security

- **Read-only.** The connector queries Ahrefs data. Nothing in your Ahrefs account is modified.
- **Query-scoped consumption.** Only the API rows your questions require are read. There is no bulk crawl of the account.
- **Revocable at any time.** Rotate or delete the token in Ahrefs and the connection ends immediately.
- **Scoped direct-MCP retention.** Full connector response payloads are not retained. Operational logs keep query text and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Ahrefs, CorpusIQ, and Perplexity.

### Comparison: Ahrefs UI vs Ahrefs in Perplexity

| Aspect | Ahrefs interface | CorpusIQ MCP with Perplexity |
|---|---|---|
| Input | Navigate a report and set filters | A question in plain language |
| Output | A table you interpret | A summarized answer with the domain named |
| Multi-domain | One report per domain | Several domains in one question |
| Web context | Separate tab | Same thread as the research |
| Repeat questions | Rebuild the view | Just ask again |
| Write access | Account settings | None, read-only token |

The Ahrefs interface is built for exploration. The connector is built for the question you already have.

### FAQ: Common Questions

<details>
<summary><strong>Do I need an Ahrefs API plan?</strong></summary>

Yes. API access requires the Advanced plan or higher. The connector uses the same API token your account already issues.
</details>

<details>
<summary><strong>Is the data live or cached?</strong></summary>

Each question queries Ahrefs through the API, so the answer reflects the data Ahrefs holds at that moment. Ahrefs' own index refresh cadence still applies to the underlying metrics.
</details>

<details>
<summary><strong>Can it compare several competitors in one question?</strong></summary>

Yes. Naming the domains in the question is enough, and the answer comes back with each one identified rather than merged.
</details>

<details>
<summary><strong>Does Perplexity's web search interfere with the numbers?</strong></summary>

No. The metrics come from Ahrefs through the connector. Perplexity can still search the web in the same thread, and the two are distinguishable in the answer because the metric values trace to the connector.
</details>

<details>
<summary><strong>Can it write keywords or change targets in Ahrefs?</strong></summary>

No. The token is read-only and the connector has no write tool.
</details>

<details>
<summary><strong>Does this work only in Perplexity?</strong></summary>

No. Ahrefs is exposed to ChatGPT, Claude, and Perplexity through the same endpoint on the same subscription.
</details>

<details>
<summary><strong>Where is the Ahrefs data stored?</strong></summary>

CorpusIQ does not retain full connector response payloads. Operational logs may persist for up to 30 days. See the [security documentation](/hermes/security/read-only-and-security).
</details>

---

**Next steps:** [Connect Ahrefs to Perplexity now](https://corpusiq.io/connect/ahrefs-with-perplexity)

**Also in ChatGPT:** [Connect Ahrefs to ChatGPT](connect-ahrefs-to-chatgpt.md) - domain ratings, keyword and backlink questions inside a ChatGPT thread.

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
