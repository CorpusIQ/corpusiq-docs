---
title: Go Rocket MCP - URL to AI Video Ads
description: "Go Rocket turns any website URL into a 9:16 AI video ad with a photoreal presenter, sampling in chat before checkout."
category: Content
stars: n/a (new listing)
added: 2026-09-27
source: "mcpservers.org + go-rocket.ai"
relevance: ★★★
tags: [video-ads, ai-video, url-to-video, vertical-video, ad-creative, presenter, remote-mcp]
---

# Go Rocket MCP

**From URL to finished 9:16 video ad in one conversation.** Go Rocket's remote MCP server takes a website URL and produces a vertical AI video ad with a photoreal presenter available in 21 languages. The agent shows a blurred sample in the chat for approval, then hands back a checkout link for the finished video. The server is remote at `https://www.go-rocket.ai/mcp/` with no auth requirement for the MCP surface.

```
Server type: Remote
Auth: none for the MCP endpoint (checkout for finished videos)
Endpoint: https://www.go-rocket.ai/mcp/
Tools: URL-to-video generation, sample preview, language selection
Pricing: per-video checkout after the sample
Category: Content / Video Ads
Built by: Go Rocket (go-rocket.ai)
```

## Why This Matters for Operators

Video ad production normally costs either money for freelancers or hours of editing time, and the brief-to-first-cut loop can stretch for days. Go Rocket compresses it to a prompt: paste a URL, get a blurred sample in chat to judge direction, then pay for the finished render. The presenter-plus-21-languages surface makes it practical for operators running the same ad across markets without re-shooting anything.

The blurred-sample-first flow is the operator-friendly detail: direction is validated cheaply before any spend, which is how production should work when an agent is driving it.

## Tools & Capabilities

| Tool area | Purpose |
|---|---|
| URL to video | Convert any website into a 9:16 vertical ad |
| Sample preview | Blurred in-chat sample before purchase |
| Presenter | Photoreal presenter in 21 languages |
| Checkout | Link to buy the finished video |

## Installation

```bash
claude mcp add --transport http go-rocket https://www.go-rocket.ai/mcp/
```

No key is needed for the MCP surface; the finished video is purchased through the checkout link the agent receives.

## Configuration

```json
{
  "mcpServers": {
    "go-rocket": {
      "type": "http",
      "url": "https://www.go-rocket.ai/mcp/"
    }
  }
}
```

## Business Relevance

- **Performance marketers** get quick vertical ad variants for testing
- **E-commerce operators** turn product pages into ads without an editor
- **Agencies** localize one concept into 21 languages
- **Founders** validate ad creative direction before paying for production

## Integration with CorpusIQ

Go Rocket fits the CorpusIQ UGC video pipeline: the daily UGC video series produces organic vertical video, while Go Rocket produces paid-style ad variants from the same landing pages. Ad performance from Meta Ads or Google Ads connectors in CorpusIQ can tell the agent which pages deserve a Go Rocket variant next.

## Limitations

- The MCP surface returns samples; the finished video is a paid checkout step
- Creative control is bounded by the presenter and template system
- No self-hosted rendering option
- New listing; output quality should be judged on the sample before purchase

## FAQ

### Do I pay before seeing the video?

No. The agent shows a blurred sample in chat first; checkout happens only for the finished video.

### How many languages does the presenter support?

Twenty-one languages, from the same URL input.

### Is there an API key?

No key is needed for the MCP surface; purchase flows through the checkout link.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
