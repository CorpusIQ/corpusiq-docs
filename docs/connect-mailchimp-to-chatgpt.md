---
title: Connect Mailchimp to ChatGPT via MCP
description: "Connect Mailchimp to ChatGPT through CorpusIQ MCP. Ask whether the newsletter moved revenue, not just opens, read-only and answered from your live campaign data."
category: ChatGPT Integrations
tags: ["connect Mailchimp to ChatGPT", "Mailchimp ChatGPT integration", "MCP Mailchimp connector", "campaign performance in ChatGPT", "email marketing analytics", "CorpusIQ MCP"]
last_updated: "2026-10-29"
canonical: "https://www.corpusiq.io/docs/connect-mailchimp-to-chatgpt"
robots: "index,follow"
---

# How to Connect Mailchimp to ChatGPT with CorpusIQ MCP

Open rates answer a question nobody asked. The question a business owner asks is whether the send moved anything: revenue, pipeline, repeat orders. That answer lives in two systems, and the campaign report only holds half of it. **Connecting Mailchimp to ChatGPT through CorpusIQ MCP** puts the campaign data in the same conversation as the store and the CRM, so one question can ask what the send was worth.

Direct MCP retrieval is read-only and does not retain raw customer files or full connector response payloads; operational query logs are retained for up to 30 days.

## What Questions Can You Ask?

- "Which campaign sent in the last quarter had the highest click rate, and which one had the highest revenue behind it?"
- "Compare opens to orders on the same days for the last six sends."
- "How has the audience grown since January, and how much of that came from the popup form?"
- "Which campaigns went to the full list versus a segment?"
- "Which subscribers are on the list but never opened anything?"

## FAQ: Common Questions

<details>
<summary><strong>Is this read-only?</strong></summary>

Yes. The connector reads campaigns, audiences and campaign reports. It does not send mail, edit a campaign, change a list or move a subscriber.
</details>

<details>
<summary><strong>Which reports come through?</strong></summary>

Campaign level performance, including sends, opens, clicks, bounces and unsubscribes, plus audience and list details such as subscriber counts. If a report you use lives only in the Mailchimp dashboard and not in the API, it will not appear here.
</details>

<details>
<summary><strong>Can it compare Mailchimp to revenue?</strong></summary>

Yes, when a commerce or finance connector is present. "Compare opens to Shopify revenue on the same days" is one question across two systems, and it is the question that tells you whether the list is an asset or a habit.
</details>

<details>
<summary><strong>Why does a campaign not appear?</strong></summary>

Drafts and unsent campaigns are not part of the sent-campaign surface. Confirm the campaign actually sent, then ask again. Accounts with several audiences also need the audience named in the question.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Live. Campaign numbers are read when you ask. A report that is still filling in for a send from this morning will read low, which is a timing fact, not a connector fault.
</details>

<details>
<summary><strong>Where is my data stored?</strong></summary>

CorpusIQ does not retain raw customer files or full connector response payloads. Retrieval happens on demand. Operational query logs may persist for up to 30 days. See our [security documentation](../security/) for the detail.
</details>

## How It Works

1. You connect Mailchimp in CorpusIQ and approve the authorization screen.
2. You add the CorpusIQ MCP server to ChatGPT. See the [Quick Start guide](quick-start.md).
3. ChatGPT discovers the Mailchimp tools and calls them when a question needs campaign data.
4. Answers name the campaign and the period they came from, so a number can be checked against the dashboard.

## Setup Guide

1. **Sign up** at [corpusiq.io](https://www.corpusiq.io). The 30-day trial needs no credit card.
2. **Connect Mailchimp.** In the dashboard, open Connectors, find Mailchimp, connect, then approve access on the Mailchimp screen.
3. **Connect ChatGPT.** Add the CorpusIQ MCP server per the [Quick Start guide](quick-start.md).
4. **Verify.** Ask "how did my last campaign perform" and check one number against Mailchimp itself.
5. **Explore.** Then ask the question the campaign report cannot answer on its own.

## Related Pages

- [Mailchimp connector reference](connectors/mailchimp.md) - what is visible and what to check when it is not
- [Connect Klaviyo to ChatGPT](connect-klaviyo-to-chatgpt.md) - the other email platform, for stores
- [Connect HubSpot to ChatGPT](connect-hubspot-to-chatgpt.md) - lifecycle and pipeline beside the send
- [Connect Shopify to ChatGPT](connect-shopify-to-chatgpt.md) - the revenue side of the comparison
- [Connect Mailchimp to Claude](connect-mailchimp-to-claude.md) - the same campaign questions for Claude Desktop
- [Browse all CorpusIQ connectors](connectors.md) - the full list
- [AI for Marketing Analytics](ai-for-marketing-analytics.md) - the analysis pattern
- [How to Connect Business Data to ChatGPT](how-to-connect-business-data-to-chatgpt.md) - the general setup
- [Benefits of MCP for Business](benefits-of-mcp-for-business.md) - the operating argument

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*
