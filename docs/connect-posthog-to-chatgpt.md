---
title: Connect PostHog to ChatGPT via MCP
description: "Connect PostHog to ChatGPT through CorpusIQ MCP. Ask about events, funnels, person records and HogQL in plain English, read-only."
category: ChatGPT Integrations
tags: ["connect PostHog to ChatGPT", "PostHog MCP", "PostHog ChatGPT integration", "product analytics in ChatGPT", "HogQL questions", "CorpusIQ MCP"]
last_updated: "2026-10-23"
canonical: "https://www.corpusiq.io/docs/connect-posthog-to-chatgpt"
robots: "index,follow"
---

# How to Connect PostHog to ChatGPT with CorpusIQ MCP

PostHog answers the product question. The revenue question needs the same facts next to the CRM, the billing system and the support desk, and that is where the answer usually stops. **Connecting PostHog to ChatGPT through CorpusIQ MCP** makes events, funnels, person records and HogQL queries available in the same conversation as everything else you run the business on.

Direct MCP retrieval is read-only and does not retain raw customer files or full connector response payloads; operational query logs are retained for up to 30 days.

## What Questions Can You Ask?

- "How many users completed the onboarding funnel this week?"
- "What is the conversion rate from signup to first data source connected?"
- "Which events fired most in the last 24 hours?"
- "Which accounts signed up last month and are still active today?"
- "Run a HogQL query that groups weekly active accounts by plan."

The question that pays for the connection is usually the join question. Product usage sits in PostHog, the contract sits in Stripe, the conversation sits in the CRM. One question across all three is the reason to connect the project at all.

## FAQ: Common Questions

<details>
<summary><strong>Is this read-only?</strong></summary>

Yes. The connector reads events and event definitions, person records, funnel conversion data and HogQL query results. It cannot capture an event, change a person record, alter a feature flag, or touch session recordings.
</details>

<details>
<summary><strong>How does the connection authenticate?</strong></summary>

With a PostHog personal API key plus the project ID you want visible. Both are created in PostHog under Settings, then Personal API keys. Anything the key cannot reach is invisible to the connector, and revoking the key in PostHog ends access immediately.
</details>

<details>
<summary><strong>Can I restrict which project is visible?</strong></summary>

Yes. The connection carries one project ID. Use a key scoped to the project your questions are about, and create a second connection if a different project needs to be visible to a different set of people.
</details>

<details>
<summary><strong>Can it join PostHog data with billing and CRM data?</strong></summary>

Yes. Connect Stripe, HubSpot or your database alongside PostHog and ask one question across them, for example "which accounts activated last month but have an open invoice" in a single answer.
</details>

<details>
<summary><strong>Does it read session recordings or feature flags?</strong></summary>

No. Recordings are not exposed, and feature flags are read as configuration at most, never changed. If a flag decision needs context, ask for the event volume behind the flag instead.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Live. When you ask, the connector reads the project as it stands. An event captured a minute ago is visible to the next question.
</details>

<details>
<summary><strong>Where is my data stored?</strong></summary>

CorpusIQ does not retain raw customer files or full connector response payloads. Retrieval happens on demand. Operational query logs may persist for up to 30 days. See our [security documentation](../security/) for the detail.
</details>

## How It Works

1. You create a PostHog personal API key and note the project ID.
2. You paste both into CorpusIQ and the PostHog connector turns green.
3. You add the CorpusIQ MCP server to ChatGPT. See the [Quick Start guide](quick-start.md).
4. ChatGPT discovers the PostHog tools and calls them when a question needs product data.
5. Answers name the events, funnel steps or HogQL query they came from, so the number can be checked.

## Setup Guide

1. **Sign up** at [corpusiq.io](https://www.corpusiq.io). The 30-day trial needs no credit card.
2. **Create the key.** In PostHog, open Settings, then Personal API keys, and create a key for this connection.
3. **Find the project ID.** It is shown in the project settings, and it is the number the connector needs.
4. **Connect PostHog** in the CorpusIQ dashboard with the key and the project ID.
5. **Connect ChatGPT.** Add the CorpusIQ MCP server per the [Quick Start guide](quick-start.md).
6. **Verify.** Ask "which events fired in the last hour". If the event names look right, the project is right.
7. **Explore.** Then ask the activation question that has been a manual dashboard read for months.

## Related Pages

- [PostHog connector reference](connectors/posthog.md) - visible data, prompts and the read-only boundary
- [Connect Google Analytics to ChatGPT](connect-google-analytics-to-chatgpt.md) - traffic alongside product usage
- [Connect Stripe to ChatGPT](connect-stripe-to-chatgpt.md) - put revenue next to activation
- [Connect HubSpot to ChatGPT](connect-hubspot-to-chatgpt.md) - join usage to the account record
- [Connect PostgreSQL to ChatGPT](connect-postgresql-to-chatgpt.md) - the warehouse side of the same question
- [Browse all CorpusIQ connectors](connectors.md) - the full list
- [How to Connect Business Data to ChatGPT](how-to-connect-business-data-to-chatgpt.md) - the general setup
- [MCP vs API Integrations](mcp-vs-api-integrations.md) - why the access model differs
- [Benefits of MCP for Business](benefits-of-mcp-for-business.md) - the operating argument

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*
