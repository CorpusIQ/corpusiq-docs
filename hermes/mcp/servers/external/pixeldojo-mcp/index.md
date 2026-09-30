---
title: "PixelDojo MCP - 140+ Generative Models for Agents"
description: "Agent access to 140+ image, video and audio models: generate, edit, upscale and run multi-step studio pipelines for product ads, campaigns and short films."
category: Creative
stars: 0 (MIT, blovett80/pixeldojo-mcp)
added: 2026-09-30
source: "mcp.so feed #1 (pixeldojo-3159cd)"
relevance: ★★
tags: [creative, image-generation, video-generation, audio, media-pipeline, remote-mcp, stdio, oauth, mit]
---

# PixelDojo MCP

**Media generation behind one endpoint.** PixelDojo gives an MCP client access to 140+ generative models for images, video and audio, plus the studio workflows built on top of them. An agent can generate a still, edit or upscale it, cut a product video ad, run a multi-step campaign, keep a character consistent across shots, or produce a faceless explainer episode and a music video, with the model chosen per prompt and a download link returned.

```
Server type: Remote (Streamable HTTP) and local (stdio)
Auth: OAuth 2.0 browser sign-in, or a Bearer API key (keys start with pd_)
Endpoint: https://pixeldojo.ai/mcp
Local: npx -y @pixeldojo/mcp (v0.16.3)
Tools: 19 in the server, 18 over the hosted endpoint
Pricing: Lite 10 USD per month (160 credits), Pro 25 USD (500), Pro Max 50 USD (1,100)
Category: Creative
Built by: BLOVE INC, d/b/a Pixel Dojo (Brian Lovett)
```

## What it exposes

Nineteen tools ship in the server. The planning tools are free: `pixeldojo_from_url` takes a public media URL as input, and the estimate step inside `pixeldojo_film` and `pixeldojo_episode` costs nothing.

Generation and editing cover the single-shot work: `pixeldojo_generate`, `pixeldojo_edit`, `pixeldojo_character`, `pixeldojo_upscale`, `pixeldojo_audio` and `pixeldojo_video`.

The studio tools wrap multi-step pipelines: `pixeldojo_storyboard` and `pixeldojo_ad` for product video ads, `pixeldojo_campaign` with `pixeldojo_campaign_status` for a full campaign, and `pixeldojo_film` for short films.

Workflow and library tools make the output reusable: `pixeldojo_save_workflow`, `pixeldojo_run_workflow`, `pixeldojo_list_workflows`, `pixeldojo_status` for long-running jobs and `pixeldojo_library` for finished assets.

One tool is stdio-only: `pixeldojo_upload` reads from the local filesystem, so the hosted endpoint does not offer it. That leaves 18 tools over `https://pixeldojo.ai/mcp`, a fact worth knowing if a directory listing reports fewer. Third-party directories generally cannot enumerate the tool list at all, because the endpoint refuses unauthenticated calls.

## Connecting

For Claude Code, add the hosted transport:

```
claude mcp add --transport http pixeldojo https://pixeldojo.ai/mcp
```

Then sign in through the browser when the client prompts, or paste an API key created at pixeldojo.ai in the API platform section. Any other client that speaks Streamable HTTP takes the same URL; the endpoint advertises OAuth protected-resource metadata at `https://pixeldojo.ai/.well-known/oauth-protected-resource/mcp`, so clients with automatic discovery handle the sign-in themselves.

For a local run, `npx -y @pixeldojo/mcp` starts the stdio server on Node 18 or newer, reading `PIXELDOJO_API_KEY` from the environment. Running locally is the only way to get `pixeldojo_upload` and the only way to feed the server a file that is not already reachable on the public web.

## Notes

Asset URLs expire one hour after creation, so anything worth keeping should be downloaded immediately or left in the library, where finished films persist. Generation calls wait 30 seconds before returning a `jobId`; a longer render is picked up with `pixeldojo_status` rather than by holding the connection open.

Pricing is credit-based and every call spends credits, with failed jobs refunded. Model rosters at this layer move quickly, so treat the specific model list as a snapshot rather than a fixed catalogue. The server reports its own origin on each request through a source header, which is useful when auditing where generation spend came from.

## See Also

- [External MCP server catalog](/hermes/mcp/servers/external/)
- [Creative and media MCP servers](/hermes/mcp/servers/external/)
