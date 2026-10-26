---
title: Connect Airtable to ChatGPT via MCP
description: "Connect Airtable to ChatGPT through CorpusIQ MCP. Ask about bases, tables and records in plain English, read-only."
category: ChatGPT Integrations
tags: ["connect Airtable to ChatGPT", "Airtable ChatGPT integration", "MCP Airtable connector", "Airtable records to ChatGPT", "ask questions about Airtable", "CorpusIQ MCP"]
last_updated: "2026-10-24"
canonical: "https://www.corpusiq.io/docs/connect-airtable-to-chatgpt"
robots: "index,follow"
---

# How to Connect Airtable to ChatGPT with CorpusIQ MCP

Airtable holds the work that never makes it into a reporting tool: the content calendar, the hiring pipeline, the partnership tracker, the product roadmap. The records are current and the answers are not, because nobody exports a base to answer one question. **Connecting Airtable to ChatGPT through CorpusIQ MCP** makes those bases queryable in plain English, read-only, against the records as they stand.

Direct MCP retrieval is read-only and does not retain raw customer files or full connector response payloads; operational query logs are retained for up to 30 days.

## What Questions Can You Ask?

- "Which items in the content calendar are still in Draft two weeks before publish?"
- "Show me every record in the hiring pipeline where stage is Onsite."
- "How many partnership conversations are waiting on legal?"
- "Pull the roadmap rows owned by the platform team and list their status."
- "Which Airtable records mention this customer by name?"

The useful questions are usually the join questions. Airtable holds the commitment; the invoice, the ticket and the campaign hold the consequence. One question across both is the reason to connect the base at all.

## FAQ: Common Questions

<details>
<summary><strong>Is this read-only?</strong></summary>

Yes. The connector lists bases, tables, records and single records, and searches records by keyword. It never creates, edits or deletes a record, and it cannot change a base schema.
</details>

<details>
<summary><strong>How does the connection authenticate?</strong></summary>

With an Airtable personal access token that you create. The token carries two read scopes, `data.records:read` and `schema.bases:read`, and it is granted access to specific bases. Anything the token cannot reach, the connector cannot see, which makes the token scope the whole permission model.
</details>

<details>
<summary><strong>Do I need to share every base?</strong></summary>

No, and you probably should not. Grant the token the bases a question would actually use. A base you never ask about is a base you do not need to expose, and revoking it later is an edit to the token rather than a support request.
</details>

<details>
<summary><strong>Can it answer across Airtable and my other systems?</strong></summary>

Yes, and that is the point of putting the base behind an MCP connector rather than opening Airtable in a second tab. "Which blocked roadmap items belong to accounts with an open support ticket" spans Airtable, the CRM and the helpdesk in one answer.
</details>

<details>
<summary><strong>What about views and filters?</strong></summary>

The connector reads records from a table. Where a base uses views to hide archived or test rows, say so in the question, for example "active rows only, not the archive view". A view you rely on for filtering becomes a sentence in the question rather than a hidden default.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Live. When you ask, the connector reads Airtable as it stands. A record edited a minute ago is visible to the next question.
</details>

<details>
<summary><strong>Where is my data stored?</strong></summary>

CorpusIQ does not retain raw customer files or full connector response payloads. Retrieval happens on demand. Operational query logs may persist for up to 30 days. See our [security documentation](../security/) for the detail.
</details>

## How It Works

1. You create an Airtable personal access token, give it the two read scopes and grant it the bases you want visible.
2. You paste the token into CorpusIQ and the connector turns green.
3. You add the CorpusIQ MCP server to ChatGPT. See the [Quick Start guide](quick-start.md).
4. ChatGPT discovers the Airtable tools and calls them when a question needs base data.
5. Answers name the base, table and record they came from.

## Setup Guide

1. **Sign up** at [corpusiq.io](https://www.corpusiq.io). The 30-day trial needs no credit card.
2. **Create the token.** Airtable, Developer hub, Personal access tokens, then add `data.records:read` and `schema.bases:read` and select the bases.
3. **Connect Airtable** in the CorpusIQ dashboard with that token.
4. **Connect ChatGPT.** Add the CorpusIQ MCP server per the [Quick Start guide](quick-start.md).
5. **Verify.** Ask "list my bases" first. If the base list is right, the scope is right.
6. **Explore.** Then ask the pipeline question that has been a manual filter for months.

## Related Pages

- [Airtable connector reference](connectors/airtable.md) - scopes, visible objects and troubleshooting
- [Connect Notion to ChatGPT](connect-notion-to-chatgpt.md) - the other document-shaped knowledge base
- [Connect Monday.com to ChatGPT](connect-monday-com-to-chatgpt.md) - work tracking in ChatGPT
- [Connect HubSpot to ChatGPT](connect-hubspot-to-chatgpt.md) - records that belong to a customer
- [Browse all CorpusIQ connectors](connectors.md) - the full list
- [How to Connect Business Data to ChatGPT](how-to-connect-business-data-to-chatgpt.md) - the general setup
- [MCP vs API Integrations](mcp-vs-api-integrations.md) - why the access model differs
- [Benefits of MCP for Business](benefits-of-mcp-for-business.md) - the operating argument

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*
