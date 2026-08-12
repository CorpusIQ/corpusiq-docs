---
title: "Clipkit MCP — Video Infra for AI Agents"
description: "Compose motion-graphics video from JSON documents via MCP. Open protocol, validation-first, deterministic GPU rendering."
date: 2026-08-12
source: mcp.so
source_url: https://mcp.so/servers/clipkit
category: Content & Media
rating: ★★★
status: active
---

# Clipkit MCP Server

## What is Clipkit?

Clipkit is the video infrastructure for AI agents. It turns a JSON timeline (the open Clipkit Protocol) into rendered video on a GPU. Describe a video as structured data; get an MP4. Agents compose, validate, preview, and render — no video editing skills required.

**Category:** Content & Media  
**License:** Apache-2.0 (protocol + tooling), BSL (runtime, free production tier)  
**Author:** clipkit-video  
**Added:** August 12, 2026

## Why It Matters for Operators

Video content production is consistently one of the top-3 pain points for business operators. Clipkit reduces the video creation workflow to something an AI agent can execute: describe the video in JSON, validate it, preview frames, and render. This is the closest thing to "agent-native video production" observed in the MCP ecosystem.

For CorpusIQ operators, this means:
- **Product demos**: Describe your product in structured data; get a rendered explainer video
- **Launch videos**: Templated promo compositions from structured inputs
- **Data stories**: Turn metrics/analytics into motion-graphics narratives
- **A/B creative testing**: Generate variants by modifying JSON parameters

Different from AI Video MCP by AITuber (TikTok/social focus) or ViewMade (YouTube focus) — Clipkit is protocol-first with deterministic output, making it suitable for production pipelines.

## Connection Details

### Hosted (Recommended)
```json
{
  "mcpServers": {
    "clipkit": {
      "type": "streamable-http",
      "url": "https://www.clipkit.dev/mcp"
    }
  }
}
```

### Local (stdio)
```json
{
  "mcpServers": {
    "clipkit": {
      "command": "npx",
      "args": ["-y", "@clipkit/mcp-server"]
    }
  }
}
```

**Transport:** Streamable HTTP (hosted) or stdio (local)  
**Auth:** None required for compose/validate/preview. API key only for cloud rendering.  
**Pricing:** Free tier for composition + validation + preview. Paid cloud rendering for 4K/ProRes/AV1.

## Key Tools (16 total)

| Tool | Description | Free/Paid |
|------|-------------|-----------|
| `compose` | Author a full video composition from JSON | Free |
| `validate` | Validate composition against schema before rendering | Free |
| `preview` | Generate PNG still from any frame in-chat | Free |
| `edit` | Modify individual elements (text, timing, transitions) | Free |
| `caption` | Add captions to media elements | Free |
| `assemble_promo` | Build templated promo from structured data | Free |
| `open_in_editor` | Share a browser editor link for human review | Free |
| `render` | Render final MP4 on GPU runtime | Paid (cloud) |

## Verified Use Cases

1. **AI-Generated Product Demos** — Ask Claude/Cursor to describe your SaaS workflow in JSON; Clipkit renders a motion-graphics walkthrough
2. **Automated Launch Videos** — Templated promo compositions from product name, features, and CTA
3. **Data-Driven Video Reports** — Turn analytics dashboards into animated video summaries
4. **Pipeline Video Generation** — Render MP4s from JSON in CI/CD or automated workflows via REST API

## CorpusIQ Integration Opportunity

**Priority: HIGH.** Clipkit fills a gap in our content production pipeline. Combined with:
- **HeyGen** for talking-head UGC video
- **ViewMade** for YouTube research + SEO video
- **Clipkit** for motion-graphics product demos + explainers

This creates a three-tier video production stack: UGC (HeyGen), YouTube SEO (ViewMade), and motion graphics (Clipkit). An agent can orchestrate across all three.

## Verdict

**★★★★★ Production-ready video infrastructure for agents.** The protocol-first approach (JSON → validate → preview → render) is well-designed for agent workflows. Deterministic GPU rendering means same JSON always produces same MP4 — critical for production pipelines. Free tier covers the entire creative workflow; only final render is paid. Strongly recommended for operators who want AI-generated video content without a video team.

## Resources

- **Homepage:** https://www.clipkit.dev/
- **Documentation:** https://www.clipkit.dev/docs
- **MCP Docs:** https://www.clipkit.dev/docs/mcp
- **Repository:** https://github.com/clipkit-video/clipkit
- **mcp.so:** https://mcp.so/servers/clipkit
