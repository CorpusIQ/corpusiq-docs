---
title: YouTube Content  --  Full Setup Guide for Hermes Agents
description: Extract transcripts from YouTube videos and transform them into summaries, threaded posts, blog articles, and more. Native Hermes Agent media skill with 160+ installs.
---

# YouTube Content  --  Setup Guide

**Source:** [nousresearch/hermes-agent](https://skills.sh/nousresearch/hermes-agent/youtube-content) (160 installs)
**Category:** Media / Content Extraction
**Status:** Native Hermes Agent skill (built-in)

Extract transcripts from any YouTube video and transform them into structured content: chapter breakdowns, summaries, X/Twitter threads, blog posts, and timestamped quotes. Essential for content repurposing, research synthesis, and competitive analysis.

---

## Installation

This is a native Hermes Agent skill  --  it ships with Hermes and is available by default. If you need the standalone skills.sh version:

```bash
npx skills add nousresearch/hermes-agent --skill youtube-content
```

### Dependency Setup

The transcript fetcher uses `youtube-transcript-api`. Install once:

```bash
uv pip install youtube-transcript-api
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | Any version (skill is built-in) |
| **uv** | Python package manager (bundled with Hermes) |
| **youtube-transcript-api** | Install via `uv pip install youtube-transcript-api` |
| **Network access** | Fetching transcripts requires outbound HTTPS to YouTube |

---

## Key Capabilities

### Core Features

| Capability | How to Trigger | Notes |
|---|---|---|
| **Transcript extraction** | Share any YouTube URL  --  full video ID, shorts, youtu.be, embeds, or live links | Returns JSON with metadata: title, channel, duration, language |
| **Chapter breakdown** | "Break this video into chapters" or "timestamped summary" | Auto-detects topic shifts, outputs `HH:MM:SS  --  description` format |
| **Video summary** | "Summarize this video" | 5-10 sentence overview (default output if no format specified) |
| **X/Twitter thread** | "Turn this into a thread" | Numbered posts, each ≤280 characters |
| **Blog post** | "Write a blog post from this video" | Full article with title, sections, key takeaways |
| **Quote extraction** | "Pull out the best quotes" | Notable quotes with timestamps |
| **Multi-language** | Specify `--language tr,en` for fallback chain | Retries without `--language` if specified language unavailable |

### CLI Command Reference

```bash
# JSON output with metadata
uv run python3 SKILL_DIR/scripts/fetch_transcript.py "https://youtube.com/watch?v=VIDEO_ID"

# Plain text for piping
uv run python3 SKILL_DIR/scripts/fetch_transcript.py "URL" --text-only

# Timestamped output
uv run python3 SKILL_DIR/scripts/fetch_transcript.py "URL" --timestamps

# Language fallback chain
uv run python3 SKILL_DIR/scripts/fetch_transcript.py "URL" --language tr,en
```

### Processing Workflow

1. **Fetch**: Run `fetch_transcript.py` with `--text-only --timestamps` via `uv run python3`
2. **Validate**: Confirm non-empty output in expected language; retry without `--language` if empty
3. **Chunk**: Split >50K char transcripts into ~40K overlapping chunks, summarize each, then merge
4. **Transform**: Convert to requested format (summary → chapters → thread → blog post → quotes)
5. **Verify**: Re-read output for coherence, correct timestamps, and completeness

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Competitive video analysis** | Extract transcripts from competitor product demos, founder interviews, and industry panels  --  feed into research pipeline |
| **Content repurposing** | Turn YouTube interviews/podcasts into blog posts for the CorpusIQ content engine, X threads for social, or email newsletter content |
| **Creator partnership research** | Analyze potential creator partners' content  --  extract key talking points, audience engagement patterns, and content quality before outreach |
| **Market intelligence** | Monitor AI agent ecosystem videos  --  product launches, framework comparisons, architecture discussions  --  extract insights for product roadmap |
| **Lead qualification** | When a prospect mentions a YouTube video, extract the transcript and find specific timestamps that match their pain points for personalized follow-up |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| **"Transcript disabled"** | Video owner disabled subtitles. Verify on the YouTube page directly  --  if no CC button, no transcript exists |
| **"Private/unavailable video"** | Ask the user to verify the URL. Private, unlisted-without-link, or region-blocked videos return errors |
| **Wrong language returned** | Retry without `--language` flag to get any available transcript, then note the actual language to the user |
| **Dependency missing** | Run `uv pip install youtube-transcript-api` and retry |
| **Empty transcript** | Retry without `--language` to get any available transcript. If still empty, the video likely has transcripts disabled entirely |
| **Large video times out** | The script handles standard videos. For 3+ hour videos, the transcript may be large  --  the chunking workflow handles this automatically |

## Verification

```bash
# Verify skill is available
hermes skills list | grep youtube-content

# Quick functional test
uv run python3 ~/.hermes/skills/media/youtube-content/scripts/fetch_transcript.py "dQw4w9WgXcQ" --text-only | head -5
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Media Skills](/hermes/skills/#media) →*
*Powered by CorpusIQ*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
