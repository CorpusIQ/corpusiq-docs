---
title: "RunAPI CLI Skill Setup Guide - CorpusIQ Docs"
description: Install and configure runapi-ai/cli-skill — unified CLI for AI image, video, music/audio, and model API jobs from Hermes Agent.
category: media-ai
publisher: runapi-ai
maturity: beta
source: https://github.com/runapi-ai/cli-skill
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/runapi-cli-skill-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# RunAPI CLI Skill — Setup Guide

Unified AI media API CLI for agents by [runapi-ai](https://github.com/runapi-ai/cli-skill). Consolidates AI image generation, video creation, music/audio synthesis, and model API access under a single CLI — eliminating the need for separate integration skills per provider.

## What It Provides

- **AI Image Generation** — DALL-E, Stable Diffusion, Flux, Midjourney (via API)
- **AI Video** — Runway, Pika, Kling, HeyGen
- **AI Music/Audio** — Suno, Udio, ElevenLabs TTS
- **AI Model APIs** — OpenAI, Anthropic, Google, DeepSeek, local Ollama
- **Job Queue** — async job submission with status polling
- **Cost Tracking** — per-provider usage and cost breakdown

## Installation

```bash
# Install via skills.sh
npx skills add https://github.com/runapi-ai/cli-skill

# Manual clone
git clone https://github.com/runapi-ai/cli-skill.git ~/.hermes/skills/runapi-cli
```

## Configuration

```yaml
runapi:
  providers:
    openai:
      api_key: "${OPENAI_API_KEY}"
      models: ["dall-e-3", "gpt-4o"]
    fal:
      api_key: "${FAL_KEY}"
      models: ["flux-pro", "stable-diffusion-3"]
    heygen:
      api_key: "${HEYGEN_API_KEY}"
    elevenlabs:
      api_key: "${ELEVENLABS_API_KEY}"
    runway:
      api_key: "${RUNWAY_API_KEY}"
    suno:
      api_key: "${SUNO_API_KEY}"
  defaults:
    image_model: "dall-e-3"
    image_size: "1024x1024"
    tts_voice: "alloy"
  cost_tracking: true
  max_concurrent_jobs: 3
```

## Supported Providers

| Category | Providers |
|----------|-----------|
| Image | OpenAI (DALL-E), FAL (Flux/SD), Replicate, Midjourney API |
| Video | Runway Gen-3, Pika, Kling, HeyGen |
| Music | Suno, Udio, Stable Audio |
| TTS | ElevenLabs, OpenAI TTS, Play.ht |
| LLM | OpenAI, Anthropic, Google, DeepSeek, Ollama |

## Key Workflows

### Generate an image

```
Generate a 1024x1024 image of "a futuristic AI operations dashboard" using Flux Pro.
```

### Create a video

```
Create a 10-second video clip showing a data pipeline animation using Runway.
```

### Generate a voiceover

```
Convert this script to audio using ElevenLabs with voice "Adam":
"CorpusIQ helps business operators automate their workflows with AI agents."
```

### Check job status

```
What's the status of my image generation job?
Show me my RunAPI cost breakdown for this month.
```

## Verification

```bash
# List available providers
hermes chat -q "List all configured RunAPI providers and their status"

# Test image generation
hermes chat -q "Generate a simple test image using the cheapest provider"
```

## Pitfalls

- **⚠️ API costs**: AI media APIs are expensive. A single video generation can cost $1-5. Set `cost_tracking: true` and monitor usage.
- **⚠️ API key sprawl**: This skill requires many API keys. Use a `.env` file or secrets manager — never hardcode keys in config.
- **Async jobs**: Video and music generation are async (minutes to hours). Use the job queue to check status. Don't block the session waiting.
- **Rate limits**: Free-tier API keys have severe rate limits. For production use, upgrade to paid tiers.
- **Model availability**: Some models (Kling, Midjourney API) have geographic restrictions or waitlists. Test availability before relying on them.
- **Output storage**: Generated media is stored locally. Large outputs can fill disk space. Set an output size cap and auto-cleanup policy.

## See Also

- [runapi-ai/cli-skill repo](https://github.com/runapi-ai/cli-skill)
- [AI Video Generation Setup](/hermes/skills/catalog/ai-video-generation-setup/)
- [HyperFrames Setup](/hermes/skills/catalog/hyperframes-setup/)
- [Media Use Setup](/hermes/skills/catalog/media-use-setup/)

---

*Setup guide by CorpusIQ. Source: [runapi-ai/cli-skill](https://github.com/runapi-ai/cli-skill).*
