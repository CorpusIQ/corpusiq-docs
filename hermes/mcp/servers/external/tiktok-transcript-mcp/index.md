---
title: TikTok Transcript MCP - AI Transcriptions of Public TikTok
description: "Remote MCP server that transcribes public TikTok videos with an AI speech model across 90+ languages: clean punctuated text, word and sentence timings, speaker labels for duets and interviews, SRT and VTT subtitle files, confidence scores, and optional post metadata, hosted on the Apify MCP gateway with your own token or Apify OAuth."
category: Content & Research
stars: n/a (new listing, github.com/deapi-ai/tiktok-transcript-mcp)
added: 2026-08-28
source: mcp.so homepage new arrivals
relevance: ★★
tags: [mcp-server, tiktok, transcription, content-research, apify, remote-mcp]
---

# TikTok Transcript MCP

**Remote MCP server that transcribes public TikTok videos by listening to the audio with an AI speech model, not by copying TikTok's auto-captions.** Because it runs speech recognition itself, it works on videos with no captions at all and across the 90+ languages TikTok creators actually post in. Per video it returns clean punctuated text, word- or sentence-level timings, speaker labels for duets and interviews, ready-to-use SRT and VTT subtitle files, per-segment confidence scores, and optional post metadata (author, hashtags, views, likes).

```
Server type: Remote (Streamable HTTP) on the Apify MCP gateway
Auth: Your own Apify token or Apify OAuth (no anonymous mode)
Endpoint: https://mcp.apify.com?tools=deapi/tiktok-transcript-scraper
Tools: 1 actor surface (transcription with rich per-video output)
Pricing: Apify actor runs; private, deleted, and region-locked videos return failed rows and are not charged
Category: Content & Research / Social content intelligence
Built by: deapi-ai (GitHub deapi-ai/tiktok-transcript-mcp, registry io.github.deapi-ai)
```

## Why This Matters for Operators

TikTok is where competitor messaging, creator language, and category narratives move first, but it is a video wall: nothing is greppable, and captions only exist when the creator adds them. Transcription converts that wall into text an assistant can search, summarize, and trend over. A content operator can pull transcripts from a competitor's last twenty videos and ask for recurring hooks, pricing mentions, and objection language; a market researcher can track how a category is being talked about week over week.

The output format matters too. Speaker labels handle duets and interview formats, and the SRT/VTT files mean the transcripts drop straight into editing and subtitling workflows. The failure model is operator-friendly: private, deleted, and region-locked videos come back as failed rows and are not charged.

**TikTok content becomes readable, searchable research material.**

## Tools & Capabilities

Capability-level table from the repository documentation; the endpoint requires Apify authentication (verified: unauthenticated requests are rejected with 401 before the MCP handshake).

| Tool | Capability |
|---|---|
| tiktok-transcript-scraper | Transcribe public TikTok videos by URL: punctuated text, timings, speaker labels, SRT and VTT subtitles, confidence scores, and optional metadata (author, hashtags, views, likes) |

## Installation

```bash
claude mcp add tiktok-transcript --transport http "https://mcp.apify.com?tools=deapi/tiktok-transcript-scraper"
```

Authenticate with a token from Apify Console, Settings, API and Integrations, or let the client open Apify's OAuth flow.

## Configuration

```json
{
  "mcpServers": {
    "tiktok-transcript": {
      "type": "http",
      "url": "https://mcp.apify.com?tools=deapi/tiktok-transcript-scraper",
      "headers": {
        "Authorization": "Bearer <your-apify-token>"
      }
    }
  }
}
```

## Business Relevance

- **Content operators** transcribe competitor feeds to mine hooks, offers, and objection language.
- **Market researchers** track how a category is discussed on TikTok across languages and weeks.
- **Brand teams** audit creator mentions of their product with metadata like views and hashtags attached.
- **Agencies** pull SRT/VTT subtitle files straight into edit workflows for repurposing.
- **SEO and content teams** feed transcripts into topic research for short-form and long-form content alike.

## Integration with CorpusIQ

The transcript MCP turns TikTok into text; CorpusIQ turns that text into business context. A composed workflow: the assistant transcribes a competitor's recent feed, then joins the trending topics with Shopify sales by product and GA4 landing-page traffic via CorpusIQ connectors to see which narratives actually moved revenue. Social listening and business results in one conversation.

## Limitations

- No anonymous mode: every request needs an Apify token or OAuth session.
- One actor surface: transcription only, no comments, profiles, or follower-graph data.
- Apify actor runs are metered; batch pulls accumulate cost (capped budgets recommended).
- Private, deleted, and region-locked videos fail by design and return failed rows.
- Young listing: repo created Aug 27, 2026, 0 stars, no license declared in the GitHub metadata.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [BulkTranscripts MCP - Hosted YouTube Transcripts and Channel Research](/docs/hermes/mcp/servers/external/bulktranscripts-mcp)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
