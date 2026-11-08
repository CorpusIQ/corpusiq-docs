---
title: Connect TikTok to ChatGPT via MCP
description: "Connect TikTok to ChatGPT through CorpusIQ MCP. Ask which videos carried the account, what engagement per view looks like and how the channel trends."
category: ChatGPT Integrations
tags: ["connect TikTok to ChatGPT", "TikTok MCP", "TikTok ChatGPT integration", "ask ChatGPT about TikTok analytics", "video performance in ChatGPT", "CorpusIQ MCP"]
last_updated: "2026-11-08"
canonical: "https://www.corpusiq.io/docs/connect-tiktok-to-chatgpt"
robots: "index,follow"
---

# How to Connect TikTok to ChatGPT with CorpusIQ MCP

TikTok reports views, likes, comments and shares one video at a time. It will not tell you which of the last forty carried the account, and it cannot rank those videos against the channels you fund beside it.

Connecting TikTok through CorpusIQ MCP makes those questions answerable inside a ChatGPT thread. The connection is read-only, and every answer names the period it measured.

## What Questions Can You Ask?

**Per-video performance**

- "What are my top ten TikTok videos by views this quarter?"
- "Which videos drove the most engagement per view?"
- "How did last Tuesday's video perform against my median?"

**Account health**

- "Show my follower count, total video count and verified status."
- "How many likes did the account collect this month?"
- "Is follower growth accelerating or flattening over the last six months?"

**Content patterns**

- "Do my videos with a question in the first line outperform the others?"
- "Which posting window gets the most views per video?"
- "Which videos have the highest comment-to-view ratio?"

**Cross-source**

- "Which TikTok videos produced sessions in GA4, and how many converted?" (requires the GA4 connector)
- "How does TikTok engagement compare to the same clip on Instagram?" (requires the Instagram connector)

## FAQ: Common Questions

<details>
<summary><strong>Can ChatGPT post to TikTok or comment on videos?</strong></summary>

No. The connection carries analytics scopes and the connector exposes no posting, commenting or following tool. Reading is the whole surface.
</details>

<details>
<summary><strong>Why did authorization fail?</strong></summary>

TikTok requires every requested scope to be approved on the consent screen. A partial approval fails the connection. Reconnect and accept the full set rather than deselecting any permission.
</details>

<details>
<summary><strong>A video I posted today is missing. Why?</strong></summary>

Newly posted videos take a few hours to appear in TikTok's API. Ask again later instead of reconnecting, which changes nothing about the data.
</details>

<details>
<summary><strong>It connected the wrong TikTok account. How do I fix that?</strong></summary>

Disconnect TikTok in the CorpusIQ dashboard, sign in to the account you want in the TikTok web app, then reconnect. Access follows the account you authorized, so a different account stays out of reach.
</details>

<details>
<summary><strong>Can it show TikTok Shop or ad revenue?</strong></summary>

No. The connector reads the profile, the posted video list with per-video metrics, and aggregate account analytics. Shop sales and ad spend sit in TikTok's separate surfaces and are not part of this connection.
</details>

<details>
<summary><strong>Does this only work in ChatGPT?</strong></summary>

No. TikTok is exposed to ChatGPT, Claude and Perplexity through the same endpoint on the same subscription. The [Perplexity version](connect-tiktok-to-perplexity.md) covers that client.
</details>

<details>
<summary><strong>What is retained after a query?</strong></summary>

Direct MCP retrieval is read-only. Raw customer files and full connector response payloads are not retained; operational query logs keep query text and bounded outcome summaries for up to 30 days. See the [read-only and security documentation](/hermes/security/read-only-and-security).
</details>

## How It Works

1. You connect TikTok in the CorpusIQ dashboard and approve the analytics scopes on TikTok's consent screen.
2. CorpusIQ exposes the TikTok profile, the posted video list and the account-level analytics as MCP tools.
3. You add the CorpusIQ MCP server to ChatGPT. See the [Quick Start guide](quick-start.md).
4. ChatGPT picks the tool the question needs, for example listing videos with metrics when you ask for a ranking.
5. The answer states the period it covers, so a ranking can be checked against TikTok's own numbers.

## Setup Guide

1. **Sign up** at [corpusiq.io](https://www.corpusiq.io). The 30-day trial needs no credit card.
2. **Connect TikTok.** Dashboard, then Connections, then TikTok, then sign in and approve the profile, video list and video analytics scopes.
3. **Connect ChatGPT.** Add the CorpusIQ MCP server per the [Quick Start guide](quick-start.md).
4. **Verify.** Ask "show my follower count and total video count". Correct-looking numbers mean the TikTok scopes took.
5. **Explore.** Then ask the question you would otherwise answer by opening forty videos and counting.

## Related Pages

- [TikTok connector reference](connectors/tiktok.md) - what the connection can see and how the scopes work
- [Connect TikTok to Perplexity](connect-tiktok-to-perplexity.md) - the same analytics inside a Perplexity thread
- [Connect Google Analytics to ChatGPT](connect-google-analytics-to-chatgpt.md) - put session and conversion data beside the views
- [Connect Meta Ads to ChatGPT](connect-meta-ads-to-chatgpt.md) - paid reach against organic reach
- [Browse all CorpusIQ connectors](connectors.md) - the full list
- [How to Connect Business Data to ChatGPT](how-to-connect-business-data-to-chatgpt.md) - the general setup
- [MCP vs API Integrations](mcp-vs-api-integrations.md) - why the access model differs

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*
