---
title: Connect YouTube to ChatGPT via MCP
description: "Connect YouTube to ChatGPT through CorpusIQ MCP. Ask which videos earned watch time, where viewers came from and what the comments say, read-only."
category: ChatGPT Integrations
tags: ["connect YouTube to ChatGPT", "YouTube MCP", "YouTube ChatGPT integration", "YouTube analytics in ChatGPT", "channel analytics questions", "CorpusIQ MCP"]
last_updated: "2026-10-23"
canonical: "https://www.corpusiq.io/docs/connect-youtube-to-chatgpt"
robots: "index,follow"
---

# How to Connect YouTube to ChatGPT with CorpusIQ MCP

YouTube Studio answers channel questions one tab at a time. It cannot tell you whether the video that earned 8,000 views also moved the store, and it cannot read the comments back to you as a summary of what buyers are asking. **Connecting YouTube to ChatGPT through CorpusIQ MCP** puts channel analytics in the same conversation as your store, your ads and your analytics, read-only.

Direct MCP retrieval is read-only and does not retain raw customer files or full connector response payloads; operational query logs are retained for up to 30 days.

## What Questions Can You Ask?

- "What are my top videos this quarter by watch time?"
- "Where are most of my viewers coming from?"
- "Which upload drove the most referred traffic to the store last month?"
- "Summarize the transcript of my latest upload."
- "What are people asking in the comments on the launch video?"

The useful question is rarely about one video. It is about whether the channel is earning attention that turns into revenue, which needs YouTube data beside Shopify, Google Analytics and the ad accounts.

## FAQ: Common Questions

<details>
<summary><strong>Is this read-only?</strong></summary>

Yes. The connector reads channel totals, your uploaded videos, per-video analytics, viewer geography, transcripts, comments on public videos and general YouTube search results. It never uploads, edits or deletes a video, never replies to a comment, and never changes a channel setting.
</details>

<details>
<summary><strong>Does it work with a Brand Account?</strong></summary>

Yes. Personal channels and Brand Account channels both work. When several channels are available under one Google account, the connection asks which channel to read, and you can pick the one that matters.
</details>

<details>
<summary><strong>Do I need a separate connection for YouTube?</strong></summary>

Not always. If you already connected Google Workspace, YouTube may already be authorized under the same Google connection. Otherwise YouTube connects on its own with the same Google sign-in.
</details>

<details>
<summary><strong>Can it reply to comments or moderate them?</strong></summary>

No. Comments are read, not managed. The connector can summarize what viewers are asking, which is often more useful than another inbox, but the replying happens in YouTube.
</details>

<details>
<summary><strong>Is this different from YouTube Studio?</strong></summary>

Studio reports on the channel. This answers questions across the channel and the rest of the business, in the same conversation, with the video named in the answer so the number can be checked.
</details>

<details>
<summary><strong>How current is the analytics?</strong></summary>

Channel and video totals are read live from the YouTube API. YouTube's own analytics reporting can lag behind the view count, so a very recent upload may show partial figures for a few hours.
</details>

<details>
<summary><strong>Where is my data stored?</strong></summary>

CorpusIQ does not retain raw customer files or full connector response payloads. Retrieval happens on demand. Operational query logs may persist for up to 30 days. See our [security documentation](../security/) for the detail.
</details>

## How It Works

1. You sign in with the Google account that owns or manages the channel.
2. You pick the channel you want visible, which matters when Brand Accounts are involved.
3. You add the CorpusIQ MCP server to ChatGPT. See the [Quick Start guide](quick-start.md).
4. ChatGPT calls the YouTube tools when a question needs channel data, transcripts or comments.
5. Answers name the channel, video and metric they came from.

## Setup Guide

1. **Sign up** at [corpusiq.io](https://www.corpusiq.io). The 30-day trial needs no credit card.
2. **Connect YouTube** in the CorpusIQ dashboard and approve the Google consent screen.
3. **Pick the channel** from the list if the account manages more than one.
4. **Connect ChatGPT.** Add the CorpusIQ MCP server per the [Quick Start guide](quick-start.md).
5. **Verify.** Ask "what are my latest uploads". If the titles match the channel, the right channel is connected.
6. **Explore.** Then ask which video actually earned the traffic you paid for.

## Related Pages

- [YouTube connector reference](connectors/youtube.md) - what is visible, and the read-only boundary
- [Connect Google Analytics to ChatGPT](connect-google-analytics-to-chatgpt.md) - the site side of the same funnel
- [Connect Shopify to ChatGPT](connect-shopify-to-chatgpt.md) - put the store next to the channel
- [Connect Google Ads to ChatGPT](connect-google-ads-to-chatgpt.md) - paid and organic attention in one answer
- [Connect Meta Ads to ChatGPT](connect-meta-ads-to-chatgpt.md) - the other video surface
- [MCP for Marketing](mcp-for-marketing.md) - the operating argument for marketing teams
- [Browse all CorpusIQ connectors](connectors.md) - the full list
- [How to Connect Business Data to ChatGPT](how-to-connect-business-data-to-chatgpt.md) - the general setup

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*
