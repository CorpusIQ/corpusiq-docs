---
title: "CuePrecise MCP - Evidence-Linked YouTube Video Analysis"
description: "CuePrecise MCP analyzes YouTube videos by original speech, captions, speaker labels and selected frames, returning timestamps that link back to the source video. Agents can find passages, compare speakers and locate on-screen scenes, with the evidence bundle stored locally for follow-up questions. Local stdio Python server."
category: Content & Research
stars: 1
added: 2026-09-07
source: "chatmcp/mcpso issue #3980"
relevance: ★★
tags: [youtube, transcription, video-analysis, research, stdio, local, evidence]
---

# CuePrecise MCP - Evidence-Linked YouTube Video Analysis

**Local stdio MCP server (Python, MIT)** - CuePrecise builds a local evidence bundle from a YouTube video: original speech, captions, speaker labels and selected frames, all indexed so the agent can find the exact passage, compare what two speakers said, and locate the on-screen scene - with every returned timestamp linking back to the source video.

```
Server type: Local (stdio, Python)
Auth: Gemini API key required for new transcription; no hosted account or remote endpoint
Install: From GitHub or GitHub Releases (not on PyPI)
Tools: 10 (register, status, outline, query, summary, set_summary, set_chapter_titles, excerpt, frames, purge)
Pricing: Free software; transcription uses the operator's own Gemini API key
Category: Content & Research
Built by: CuePrecise (github.com/Nattentia/cueprecise)
```

## Why This Matters for Operators

Video is where the claims are, and claims need citations. When a competitor launches, a vendor demos a feature or an earnings call happens, the specifics live inside the footage - but transcripts alone lose the visuals and the attribution. CuePrecise keeps the evidence bundle local and queryable: the agent answers "what exactly did the CEO say about pricing, and where was it on screen" with a timestamp, not a paraphrase.

**The evidence bundle persists locally for later questions, which makes it a research asset rather than a one-shot transcription - the difference between a claim and a citable finding.**

## Tools & Capabilities

| Group | Tools |
|---|---|
| Registration and status | cueprecise_register (ingest a video), cueprecise_status |
| Structure | cueprecise_outline, cueprecise_set_chapter_titles, cueprecise_set_summary |
| Queries | cueprecise_query (passages, speakers, scenes) with timestamps back to the video |
| Extraction | cueprecise_excerpt, cueprecise_frames, cueprecise_summary |
| Lifecycle | cueprecise_purge (remove bundles) |

## Installation

```bash
git clone https://github.com/Nattentia/cueprecise.git
cd cueprecise
pip install -e .
```

## Configuration

```json
{
  "mcpServers": {
    "cueprecise": {
      "command": "python",
      "args": ["cueprecise/src/mcp_server.py", "--bundle-root", "cueprecise/data"],
      "env": {
        "GEMINI_API_KEY": "your_key"
      }
    }
  }
}
```

The Gemini API key is used for new transcription; registered bundles can be queried without new transcription work.

## Business Relevance

- **Market researchers** cite exact competitor statements from video with timestamps.
- **PR teams** verify quotes and context from interviews and presentations.
- **Content teams** mine long-form video into structured briefs with speaker attribution.
- **Due diligence** extracts claims from demos and earnings calls into evidence files.

## Integration with CorpusIQ

CuePrecise turns video claims into citable text; CorpusIQ turns text into business signals. A composed workflow: the agent extracts competitor pricing and feature claims from YouTube with CuePrecise, then checks the market impact through CorpusIQ's Stripe, Shopify and GA4 connectors to see whether the claims moved anything.

## Limitations

- Brand new listing (issue #3980, Sep 7, 2026); 1-star repo created Aug 30, 2026.
- Not on PyPI; install is from GitHub source or releases.
- Transcription depends on the operator's own Gemini API key and quota.
- YouTube-only; no support for other video platforms.

## See Also

- [BulkTranscripts MCP - Hosted YouTube Transcripts and Channel Research](/hermes/mcp/servers/external/bulktranscripts-mcp/)
- [TikTok Transcript MCP - AI Transcriptions of Public TikTok Videos](/hermes/mcp/servers/external/tiktok-transcript-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
