---
title: "PageToVid MCP - Website to Narrated Video"
description: "PageToVid films a real web page, writes the script, voices it in 13 languages and returns a captioned MP4 in 16:9, 9:16 or 1:1."
category: Marketing
stars: n/a (no public repo)
added: 2026-10-21
source: "mcp.so /feed page 1 (card posted 2026-10-21T09:31:16Z)"
relevance: ★★★
tags: [video-generation, website-to-video, product-demo, screen-recording, text-to-speech, marketing-content, remote-mcp, oauth]
last_updated: "2026-10-24"
---

# PageToVid MCP

**Most video tools generate a synthetic scene. PageToVid opens the actual page in a real browser, films it, and returns a narrated MP4, so what the viewer sees is the product rather than a rendering of it.**

```
Server type: Remote (Streamable HTTP) at https://pagetovid.com/mcp
Auth: OAuth on first connect; free plan available
Live check: POST initialize returned HTTP 200 (serverInfo pagetovid 0.32.0, protocol 2025-06-18, tools and prompts capabilities); tools/list returned 82 tools
Tools: 82 (video creation, storyboard editing, animation, brand kit, review links, webhooks, format validation)
Pricing: first film free, 3 free films per website with a badge; $3.90 per film; Creator $19/mo (25 films), Pro $49/mo (75 films, 3 seats), Scale $99/mo (200 films)
Vendor: PageToVid (pagetovid.com)
```

## Why This Matters for Operators

A product demo video is the highest-leverage asset most businesses never make. The reason is not budget, it is the process: someone has to record the screen, write a script that matches what is on it, record a voice, add captions, and redo all four when the page changes. So the homepage screenshot sits in a folder and the launch goes out with a static image.

Capturing the live site changes the economics. The page is the source of truth, so the asset regenerates when the page changes instead of going stale. Narration in 13 languages means the same film covers markets that would otherwise need a local producer.

## What It Actually Does

Give it a public URL and it ranks what is worth filming on that page (calls to action, product shots, pricing, search boxes), writes a storyboard, records the site in a real browser, adds an AI voice-over with captions and music, and renders an MP4 in 16:9, 9:16 or 1:1, typically in minutes.

The tool surface is a full production pipeline rather than a one-shot generator. `create_video` and `generate_site_videos` start from a URL; `get_storyboard` and `update_storyboard` let the agent revise what will be filmed before rendering; `get_timeline`, `get_frames` and `save_scene` expose the edit; `approve` and `cancel_video` control the run. For content that is not a page, `create_animation` films a storyboard the agent writes, with scene visuals for charts, timelines, pricing grids, quotes and message threads, and `create_object`, `create_character`, `create_format` and `create_motion` manage the reusable pieces.

Operations tools come with it: `get_brand_kit` and `set_brand_kit` and `detect_brand` keep films on-brand, `translate_video` re-voices an existing film, `create_review_link` produces a shareable review URL, `create_upload` and `upload_asset` handle source media, `set_webhook` and `rotate_webhook_secret` push completion events, `get_audit_log` records what ran, and `validate_format` and `validate_motion_spec` check a spec before it burns credits.

## Installation

```bash
claude mcp add pagetovid --transport http https://pagetovid.com/mcp
```

Sign in through OAuth on the first call. No API key is required for the standard flow.

## Configuration

```json
{
  "mcpServers": {
    "pagetovid": {
      "type": "http",
      "url": "https://pagetovid.com/mcp"
    }
  }
}
```

## Business Relevance

- **Marketing leads** produce launch, pricing and feature films from the live site without a video editor in the loop.
- **Founders and solo operators** get a narrated demo for the homepage and for social in the time it takes to write a post.
- **Agencies** generate one film per client site, with brand kits and review links that fit an approval process.
- **Localized go-to-market** teams re-voice the same film instead of commissioning one per language.
- **Sales teams** turn a product page or a campaign landing page into a short walkthrough for outbound.

## Integration with CorpusIQ

The natural flow starts in CorpusIQ: ask it for the pages that earn traffic from the Search Console and GA4 connectors, or for the product pages a Shopify connector shows are converting, then hand those URLs to PageToVid so the films follow evidence rather than guesswork. After rendering, the completion webhook plus the Drive connector puts the MP4 where the team already looks, and the same link can go out through the social tooling.

On the other side, the film is a new data source for the business: PageToVid's audit log and storyboard output describe what the site claims, which is exactly what a positioning or AEO question needs, and CorpusIQ can compare the claim in the film with the claim on the page.

## Limitations

- New listing with no independent track record.
- Free films carry a badge; badge-free output needs a paid plan or a credit pack.
- Credits meter the work: a finished film is 40 credits, an AI image 40, a standard AI clip 311, so heavy animation work depletes a plan faster than plain page films.
- It films public pages. Pages behind a login need the capture-session feature, which is on the Scale plan and above.
- Rendering is asynchronous, so an agent must poll or use the webhook rather than expect a film back in one call.

## FAQ

### How is this different from an AI avatar video tool?

An avatar tool generates a person and a background. PageToVid records the real site in a browser, which is why the output matches the product as it is today and stops being accurate the moment the page changes and the film is not regenerated.

### Do I need a paid plan to evaluate it?

No. The first film is free on any website and a website gets 3 free films, no card required, with a small badge on the output. Paid plans start at $19 a month.

### Can the agent edit the film before it renders?

Yes. The storyboard is readable and writable through `get_storyboard` and `update_storyboard`, the timeline and frames are exposed, and a render can be approved or cancelled, so the agent can revise the plan before spending credits.

### Which output formats are supported?

16:9, 9:16 and 1:1, with voice-over and captions in 13 languages.

## See Also

- [Go Rocket MCP - URL to AI Video Ads](/hermes/mcp/servers/external/go-rocket-mcp)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
