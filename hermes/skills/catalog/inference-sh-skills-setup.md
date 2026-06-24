---
title: inference.sh/skills — Full Setup Guide for Hermes Agents
description: Install and configure inference.sh agent skills — 85 skills for AI image/video generation, web search, Twitter automation, LLM access, and growth tools. 706K installs across halt-catch-fire/skills.
---

# inference.sh/skills — Setup Guide

**Source:** [halt-catch-fire/skills](https://skills.sh/halt-catch-fire/skills) (706.2K total installs)
**Category:** Agent Tools / Growth / Media Generation

A collection of 85 agent skills for AI image and video generation, web search, social media automation, LLM access, and growth workflows. Powered by inference.sh CLI (250+ models). Covers the full agent toolchain — from content creation to distribution.

---

## Installation

```bash
npx skills add halt-catch-fire/skills
```

### CLI Setup (required for media generation)

```bash
# Install inference.sh CLI
curl -sL https://inference.sh/install | bash
belt login
belt app store
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | v0.16.0+ |
| **Node.js** | v18+ for `npx` install |
| **inference.sh CLI** | Required for image/video generation skills |
| **X/Twitter API** | Required for `twitter-automation` |

---

## Key Skills

### Media Generation

| Skill | What It Does |
|---|---|
| **`ai-image-generation`** | 50+ image models (FLUX, Gemini, Reve, Qwen, etc.) |
| **`ai-video-generation`** | 40+ video models (Veo, Seedance, Wan, etc.) |
| **`ai-avatar-video`** | AI avatar video creation |
| **`remotion-render`** | Programmatic video rendering with Remotion |
| **`image-to-video`** | Convert images to animated video |
| **`image-upscaling`** | AI-powered image upscaling |
| **`text-to-speech`** | ElevenLabs dialogue generation |
| **`speech-to-text`** | Audio transcription |

### Agent Tools

| Skill | What It Does |
|---|---|
| **`agent-browser`** | AI-powered browser automation |
| **`web-search`** | Tavily + Exa search integration |
| **`python-executor`** | Agent-controlled Python code execution |
| **`llm-models`** | Access to Claude, Gemini, Kimi, GLM via inference.sh |
| **`data-visualization`** | Chart and graph generation |

### Growth & Marketing

| Skill | What It Does |
|---|---|
| **`twitter-automation`** | X/Twitter API — post, search, engage |
| **`landing-page-design`** | AI landing page generation |
| **`competitor-teardown`** | Competitive analysis framework |
| **`product-hunt-launch`** | PH launch strategy and execution |
| **`customer-persona`** | Buyer persona generation |
| **`social-media-carousel`** | AI carousel creation |
| **`ai-content-pipeline`** | End-to-end content pipeline |
| **`product-photography`** | AI product image generation |

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Content creation pipeline** | Use `ai-image-generation` + `ai-content-pipeline` for social media assets |
| **Competitor research** | Use `competitor-teardown` + `web-search` for market intelligence |
| **Launch campaigns** | Use `product-hunt-launch` + `twitter-automation` for coordinated launches |
| **Video marketing** | Use `ai-avatar-video` + `remotion-render` for UGC-style content |
| **Automated research** | Use `agent-browser` + `web-search` + `python-executor` for deep research |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| **belt CLI not found** | Install: `curl -sL https://inference.sh/install | bash` |
| **Media generation fails** | Run `belt login` — requires inference.sh account |
| **Twitter automation blocked** | Check X API credentials in `~/.inference.sh/config` |
| **Web search returns empty** | Verify Tavily/Exa API keys are configured |

## Verification

```bash
# Verify CLI
belt --version

# List available models
belt app store

# Test image generation
# In agent: "Generate an image using ai-image-generation"
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*
*Powered by CorpusIQ*
---

*
---
*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
