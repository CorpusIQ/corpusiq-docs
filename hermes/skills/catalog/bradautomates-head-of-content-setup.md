---
title: Brad Automates Head of Content — Social Media Research for Hermes Agents
description: Instagram, TikTok, and video content research skills with 2.8K+ combined installs. Fetch and analyze social media content, identify viral outliers, and extract trending patterns using Apify + Gemini.
---

# Brad Automates Head of Content — Setup Guide

**Source:** [bradautomates/head-of-content](https://skills.sh/bradautomates/head-of-content) (2.8K+ combined installs)
**Category:** Growth Operations / Social Media
**Quality Tier:** 🟡 Beta

Agent-driven social media research toolkit. Fetch Instagram and TikTok content via Apify, analyze posts for viral outliers against statistical thresholds, and extract trending topics, hashtags, and patterns. Uses Gemini for content analysis. Built for content creators and growth operators who need data-driven social media intelligence.

---

## Installation

```bash
npx skills add bradautomates/head-of-content --skill instagram-research
npx skills add bradautomates/head-of-content --skill tiktok-research
npx skills add bradautomates/head-of-content --skill video-content-analyzer
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **instagram-research** | 1.1K | Fetch Instagram posts/reels/stories via Apify, identify viral outliers, extract trending topics |
| **tiktok-research** | 1.0K | TikTok content analysis — fetch, analyze patterns, detect viral trends |
| **video-content-analyzer** | 664 | Analyze video content with Gemini — transcripts, visual elements, engagement patterns |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Apify token** | Set `APIFY_TOKEN` in `.env` — powers social media data extraction |
| **Gemini API key** | Set `GEMINI_API_KEY` in `.env` — powers content analysis |
| **Python packages** | `apify-client`, `google-genai`, `python-dotenv` |
| **Instagram accounts** | Configure target accounts in `.claude/context/instagram-accounts.md` |

---

## Key Capabilities

### Instagram Research
- Fetch posts, reels, or stories from any public account (30-day window, configurable)
- Statistical outlier detection — identify posts performing 2x+ above account baseline
- Hashtag and keyword extraction from top-performing content
- Multi-account batch analysis

### TikTok Research
- Content pattern analysis across TikTok accounts
- Viral trend detection and pattern extraction
- Engagement metrics and growth signals

### Video Content Analysis
- Gemini-powered transcript analysis
- Visual element identification
- Engagement pattern correlation

---

## Quick Start

```bash
# 1. Verify prerequisites
python3 -c "
import os
from dotenv import load_dotenv; load_dotenv()
from apify_client import ApifyClient
from google import genai
assert os.environ.get('APIFY_TOKEN'), 'APIFY_TOKEN not set'
assert os.environ.get('GEMINI_API_KEY'), 'GEMINI_API_KEY not set'
print('Prerequisites OK')
"

# 2. Run Instagram research
RUN_FOLDER="instagram-research/$(date +%Y-%m-%d_%H%M%S)" && mkdir -p "$RUN_FOLDER"
python3 .claude/skills/instagram-research/scripts/fetch_instagram.py \
  --type reels --days 30 --limit 50 --output "$RUN_FOLDER/raw.json"
python3 .claude/skills/instagram-research/scripts/analyze_posts.py \
  --input "$RUN_FOLDER/raw.json" --output "$RUN_FOLDER/outliers.json" --threshold 2.0
```

---

## Verification

```bash
npx skills list | grep bradautomates/head-of-content
python3 -c "from apify_client import ApifyClient; print('Apify OK')"
```

---

## Notes

- Requires Apify (paid) and Gemini API (free tier available) — budget consideration for automation
- Outlier threshold of 2.0 (2x above average) identifies truly viral content vs noise
- Instagram accounts file at `.claude/context/instagram-accounts.md` must be manually populated
- Directly useful for CorpusIQ social media strategy — competitor content analysis, trend detection
- Complements `corpusiq-instagram-dm-outreach` and `corpusiq-social-cadence-engine` for full social workflow
