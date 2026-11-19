---
title: "Connect YouTube to Perplexity via MCP"
description: "Connect YouTube to Perplexity through CorpusIQ MCP. Ask which videos earned watch time, where viewers came from and what the comments ask, read-only."
category: Perplexity Integrations
tags: ["connect YouTube to Perplexity", "YouTube Perplexity integration", "MCP YouTube connector", "YouTube analytics in Perplexity", "channel analytics questions", "CorpusIQ MCP"]
last_updated: "2026-11-19"
canonical: "https://www.corpusiq.io/docs/connect-youtube-to-perplexity"
robots: "index,follow"
---

# How to Connect YouTube to Perplexity with CorpusIQ MCP

A channel is a business record with no ledger. YouTube Studio answers one tab at a time: views here, watch time there, comments in a third place, and nothing that connects an upload to the traffic it sent to the store. **Connecting YouTube to Perplexity through CorpusIQ MCP** puts the channel in the same thread as the rest of the business, so the question you actually have gets answered instead of navigated.

Perplexity is strong on the public record and blind to your own channel. The connection changes that: Perplexity reads channel totals, per-video analytics, viewer geography, transcripts and comments through CorpusIQ, and names the video it read.

### Why Connect YouTube to Perplexity?

- **Which videos earned attention.** "What are my top videos this quarter by watch time, and what did the top three have in common?"
- **Where the audience is.** "Where are most of my viewers coming from, and did that shift after the last three uploads?"
- **Traffic that converts.** "Which upload drove the most referred traffic to the store last month?" (requires an analytics or store connector)
- **What viewers ask.** "What are people asking in the comments on the launch video, grouped by the question behind the question?"
- **Content without watching it.** "Summarise the transcript of my latest upload, then list the claims that need a source."
- **Read-only by capability.** The retrieval tools documented on this page return channel and video data to the assistant. They never upload, edit or delete a video, and never change a channel setting.

### How It Works

1. **Connect YouTube to CorpusIQ.** Sign in with the Google account that owns or manages the channel, then pick the channel to expose. Brand Account channels work the same way.
2. **Add CorpusIQ to Perplexity** as a custom remote MCP server, using the endpoint from your CorpusIQ account settings.
3. **Ask a channel question.** CorpusIQ calls the YouTube tools that fit the question, whether that is analytics, a transcript or the comments on a public video.
4. **Perplexity answers** with the channel, the video and the metric named in the reply, next to the outside context it already provides.

Direct MCP retrieval is read-only. It does not retain raw customer files or full connector response payloads; operational logs keep query text, per-user tool-call metadata and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log in and open **Connectors**.
2. Select **YouTube** and sign in with the Google account that manages the channel.
3. Pick the channel if the account manages more than one. With Brand Accounts this step decides which channel is visible.
4. Approve the consent screen and wait for the connector to turn green. If Google Workspace is already connected, YouTube may already be authorised under that same Google connection.

**In Perplexity**

5. Open **Settings** and find the **MCP servers** section.
6. Add a custom MCP server and paste the endpoint:

```
https://mcp2.corpusiq.io/mcp
```

Then start a new thread and ask something the channel can answer, for example which video earned the most watch time last month. Which channel is reachable is decided by the channel you picked at connect time; nothing outside it is read.

### Example Perplexity Questions

**Channel performance**

- "What are my top videos this quarter by watch time?"
- "Which upload has the highest average view duration, and how does it compare with my channel average?"
- "How did subscriber count move in the last 90 days, and which uploads came before the jumps?"

**Audience**

- "Where are most of my viewers coming from geographically?"
- "Did the geography of my audience change after the last three uploads?"
- "Which language or market is growing fastest for the channel?"

**Comments and content**

- "Summarise what viewers ask in the comments on the launch video."
- "Which questions repeat across my last ten uploads?"
- "Pull the transcript of my latest upload and list every claim that needs a citation."

**Cross-source**

- "Which upload drove the most referred traffic to the store last month?" (requires Google Analytics or a store connector)
- "Compare YouTube-attributed sessions with paid social for the same period." (requires an ads connector)
- "Which products mentioned in the comments match SKUs in the catalog?" (requires a commerce connector)

### Security

- **Read tools only.** The retrieval tools documented on this page read channel totals, uploaded videos, per-video analytics, viewer geography, transcripts, comments on public videos and general YouTube search results.
- **Nothing on the channel changes.** No upload, edit, delete, comment reply or channel setting change is available through these tools.
- **Your Google grant stays yours.** CorpusIQ holds the encrypted grant; you can revoke it from your Google account at any time.
- **Scoped direct-MCP retention.** Raw customer files and full connector payloads are not retained. Operational logs keep query text, tool-call metadata and bounded outcome summaries for up to 30 days.
- **TLS in transit** between YouTube, CorpusIQ and Perplexity.

### Comparison: YouTube Studio and a channel question

| Aspect | YouTube Studio | CorpusIQ MCP with Perplexity |
|---|---|---|
| Input | A tab, a date range and a metric | A question in the thread you are already working in |
| Scope | One report at a time | Channel, video, transcript and comments in one answer |
| Comments | Opened and read by hand | Summarised, with the video named |
| Outside context | Open a second tab | Same thread, same answer |
| Cross-system | Export and join by hand | Asked across connectors |
| Write access | Yes, by your users in Studio | None through the retrieval tools |

Studio reports on the channel. The question is usually whether the channel is earning attention that turns into revenue, and that answer lives in two systems.

### FAQ: Common Questions

<details>
<summary><strong>Can Perplexity upload or edit a video?</strong></summary>

No. The retrieval tools documented on this page read channel and video data. Uploads, edits, deletions, comment replies and channel settings are outside the connection.
</details>

<details>
<summary><strong>Does it work with a Brand Account?</strong></summary>

Yes. Personal channels and Brand Account channels both connect. When one Google account manages several channels, the connection asks which channel to read.
</details>

<details>
<summary><strong>Do I need a separate connection for YouTube?</strong></summary>

Not always. If Google Workspace is already connected, YouTube may already be authorised under that same Google connection. Otherwise YouTube connects on its own with the same Google sign-in.
</details>

<details>
<summary><strong>Does it read the comments on other people's videos?</strong></summary>

It reads comments on public videos, which includes the videos that matter to your own market. Replying and moderating happen in YouTube, not here.
</details>

<details>
<summary><strong>How current is the analytics?</strong></summary>

Channel and video totals are read live from the YouTube API. YouTube's own analytics can lag the view count, so a very recent upload may show partial figures for a few hours.
</details>

<details>
<summary><strong>Does this work in ChatGPT or Claude too?</strong></summary>

Yes. YouTube is exposed to ChatGPT, Claude and Perplexity through the same endpoint on the same subscription.
</details>

### See Also

- [Connect YouTube to ChatGPT](connect-youtube-to-chatgpt.md) - the same channel questions, asked in ChatGPT
- [YouTube connector reference](connectors/youtube.md) - what is visible, and the boundary
- [Connect Google Analytics to Perplexity](connect-google-analytics-to-perplexity.md) - the site side of the same funnel
- [Connect TikTok to Perplexity](connect-tiktok-to-perplexity.md) - the other short-form surface
- [Connect Meta Ads to Perplexity](connect-meta-ads-to-perplexity.md) - paid attention beside organic
- [Browse all CorpusIQ connectors](connectors.md) - the full list

---

**Next steps:** [Add CorpusIQ to Perplexity now](https://www.corpusiq.io/connectors/perplexity)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.CorpusIQ.io).*

