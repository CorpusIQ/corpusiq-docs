---
title: "LinkDigest MCP - Social Post to LLM-Readable Text"
description: "LinkDigest MCP turns social post URLs into text an agent can actually read: transcript, on-screen text, per-image descriptions, caption and metadata as Markdown or JSON. Works on Xiaohongshu, Douyin, TikTok, YouTube, X and ordinary web pages. Hosted Streamable HTTP endpoint, one digest_url tool with job-id polling for long media."
category: Content & Research
stars: 0
added: 2026-09-07
source: "chatmcp/mcpso issue #3941"
relevance: ★★
tags: [content-extraction, social-media, transcription, ocr, remote-mcp, research]
---

# LinkDigest MCP - Social Post to LLM-Readable Text

**Remote MCP server (Streamable HTTP)** - LinkDigest solves the "agents cannot read social links" problem: a Xiaohongshu share URL returns an app-download shell, and a Douyin or TikTok post is video with no transcript in the page. LinkDigest fetches the post, transcribes the audio, describes and OCRs each image, and returns Markdown or JSON.

```
Server type: Remote (Streamable HTTP)
Auth: API key for digest calls; anonymous initialize exposes the tool surface (probe-verified)
Endpoint: https://linkdigest.dev/mcp (probe-verified live; tools/list served anonymously)
Tools: 1 (digest_url with job-id polling for long media)
Pricing: Free tier available; plans at linkdigest.dev
Category: Content & Research
Built by: LinkDigest (linkdigest.dev); repo github.com/jcaiagent7143-ui/linkdigest-mcp
```

## Why This Matters for Operators

Competitor and market research increasingly lives inside social video and image posts that link-share badly. LinkDigest converts any of those links into agent-readable context: the spoken transcript, the text on screen, what each image shows, and the post metadata. The agent can then reason over the actual content instead of the platform shell.

**The single-tool design is honest about scope: digest_url takes a URL and format and returns structured content, with a job-id return for long media so a second call collects the result instead of timing out.**

## Tools & Capabilities

| Platform | Status |
|---|---|
| Xiaohongshu | Works: image and video notes, no login |
| Douyin | Works: video posts and image notes |
| TikTok | Works: short links resolve; rate-limits under load |
| YouTube | Works: native captions where published |
| X | Works: posts with video or images |
| Web articles | Works |
| Bilibili | Blocked: returns HTTP 412 to the server's address |
| Instagram | Wired but not verified end to end |

## Installation

Create a LinkDigest account and key at linkdigest.dev, then add the endpoint to any Streamable HTTP client. Long media exceeds a single request, so calls can return a job id to collect on a second call.

```json
{
  "mcpServers": {
    "linkdigest": {
      "type": "http",
      "url": "https://linkdigest.dev/mcp"
    }
  }
}
```

## Configuration

Attach the LinkDigest key as the bearer authorization header for digest calls. Anonymous initialize against the endpoint returned the tool surface, which is useful for wiring the client before the key is added.

## Business Relevance

- **Market researchers** read competitor posts on Xiaohongshu and Douyin without app access.
- **Content teams** convert viral posts into structured briefs (transcript plus image descriptions).
- **Growth teams** mine social video for messaging and positioning evidence.
- **PR teams** capture citations and context from social posts into research files.

## Integration with CorpusIQ

LinkDigest extracts the signal; CorpusIQ measures the market. A composed workflow: the agent digests competitor social posts with LinkDigest, logs the claims, then checks CorpusIQ's GA4 and Stripe data to see whether the market responded - turning social observation into business intelligence.

## Limitations

- Brand new listing (issue #3941, Sep 5, 2026); 0-star repo created Sep 3, 2026.
- One tool; everything is the digest_url surface with job-id polling.
- Bilibili is blocked upstream and Instagram is not verified end to end.
- Rate limits under load on TikTok are documented by the vendor.

## See Also

- [BulkTranscripts MCP - Hosted YouTube Transcripts and Channel Research](/docs/hermes/mcp/servers/external/bulktranscripts-mcp)
- [TikTok Transcript MCP - AI Transcriptions of Public TikTok Videos](/docs/hermes/mcp/servers/external/tiktok-transcript-mcp)
- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
