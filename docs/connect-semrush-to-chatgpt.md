---
title: Connect Semrush to ChatGPT via MCP
description: "Connect Semrush to ChatGPT through CorpusIQ MCP. Ask which keywords a competitor ranks for, what a click costs and where you lose ground."
category: ChatGPT Integrations
tags: ["connect Semrush to ChatGPT", "Semrush MCP", "Semrush ChatGPT integration", "ask ChatGPT about SEO data", "competitor keywords in ChatGPT", "CorpusIQ MCP"]
last_updated: "2026-11-08"
canonical: "https://www.corpusiq.io/docs/connect-semrush-to-chatgpt"
robots: "index,follow"
---

# How to Connect Semrush to ChatGPT with CorpusIQ MCP

Semrush holds organic positions, paid positions, backlinks and month by month domain history. The reports are exhaustive and, for that reason, awkward to hold in your head when the question is comparative.

Connecting Semrush through CorpusIQ MCP puts those records behind read-only tools, so ChatGPT can answer "where are we losing ground" with the domains and dates named.

## What Questions Can You Ask?

**Organic**

- "What organic keywords does competitor.com rank for?"
- "Show me my domain's SEO overview."
- "Which of my top keywords dropped out of the first page this month?"

**Paid**

- "Which paid keywords does competitor.com bid on?"
- "What is the estimated paid traffic for my domain against theirs?"

**Backlinks**

- "How does my backlink profile compare to competitor.com?"
- "Which referring domains do they have that I do not?"

**Demand and competitor set**

- "What is the search volume and CPC for 'enterprise CRM'?"
- "Who are my top organic competitors?"
- "Show the month by month organic history for my domain and two competitors."

## FAQ: Common Questions

<details>
<summary><strong>Which Semrush plan does this need?</strong></summary>

The API requires a Business plan or higher. A lower-tier plan produces a key the API rejects, and the connector reports an invalid key.
</details>

<details>
<summary><strong>Does each question cost API units?</strong></summary>

Yes. Semrush meters its API in units and every query spends some. Ask narrow questions when you are exploring and broad ones once you know what you need.
</details>

<details>
<summary><strong>Can ChatGPT change anything in Semrush?</strong></summary>

No. The connector reads domain overviews, keyword lists, competitor lists, backlink summaries and domain history. It cannot create projects, edit campaigns or spend budget.
</details>

<details>
<summary><strong>Why is a domain missing data?</strong></summary>

Semrush data lags reality, and very new domains may not be indexed yet. Try an established domain to confirm the key works before treating an empty result as a fault.
</details>

<details>
<summary><strong>How is this different from the Semrush dashboard?</strong></summary>

The dashboard is built for browsing one report at a time. The connector is built for answering a question that spans reports, and for putting the answer beside your own Search Console and analytics data.
</details>

<details>
<summary><strong>What is retained after a query?</strong></summary>

Direct MCP retrieval is read-only. Raw customer files and full connector response payloads are not retained; operational query logs keep query text and bounded outcome summaries for up to 30 days.
</details>

## How It Works

1. You paste your Semrush API key into the CorpusIQ connector form and save.
2. CorpusIQ verifies the key and exposes domain overview, keyword, competitor, backlink and history lookups as read-only MCP tools.
3. You add the CorpusIQ MCP server to ChatGPT. See the [Quick Start guide](quick-start.md).
4. ChatGPT calls the lookup the question needs and answers from the returned rows.
5. The answer names the domain and period it read.

## Setup Guide

1. **Sign up** at [corpusiq.io](https://www.corpusiq.io). The 30-day trial needs no credit card.
2. **Connect Semrush.** In Semrush open your profile, then Subscription info, then API units, and copy the key. In CorpusIQ open Dashboard, then Connections, find Semrush, paste the key and save.
3. **Connect ChatGPT.** Add the CorpusIQ MCP server per the [Quick Start guide](quick-start.md).
4. **Verify.** Ask "show me my domain's SEO overview". A traffic figure means the key works.
5. **Explore.** Then ask the comparison question that has meant three exports and a spreadsheet.

## Related Pages

- [Semrush connector reference](connectors/semrush.md) - what the connection can see and the unit costs
- [Connect Semrush to Perplexity](connect-semrush-to-perplexity.md) - the same data inside a Perplexity thread
- [Connect Ahrefs to ChatGPT](connect-ahrefs-to-chatgpt.md) - the second SEO dataset, same questions
- [Connect Google Search Console to ChatGPT](connect-google-search-console-to-chatgpt.md) - measured clicks beside estimated traffic
- [Connect Google Analytics to ChatGPT](connect-google-analytics-to-chatgpt.md) - what the organic sessions did next
- [Browse all CorpusIQ connectors](connectors.md) - the full list
- [MCP vs API Integrations](mcp-vs-api-integrations.md) - why the access model differs

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*
