---
title: Steroids OpenAI Image Gen  --  Hermes Plugin Setup Guide
description: Install and configure the steroids-openai-image-gen provider plugin for Hermes Agent  --  OpenAI-compatible endpoints or direct Codex Auth image generation.
---

# Steroids OpenAI Image Gen  --  Setup Guide

**Plugin:** `eve-ai-dev/steroids-openai-image-gen`  
**Purpose:** Hermes image generation using OpenAI-compatible endpoints or Codex OAuth  
**License:** MIT | **Language:** Python | **Stars:** 2

---

## What It Does

Adds a Hermes image generation provider with two modes:

1. **OpenAI-compatible**  --  any endpoint with `/v1/images/generations` and `/v1/images/edits` routes
2. **Codex Auth**  --  uses Codex/OpenAI OAuth token directly

Also provides `image_generate_background` for batch/slow jobs via Hermes' process registry completion queue.

---

## Installation

```bash
# Clone into Hermes plugin root
cd "${HERMES_HOME:-$HOME/.hermes}/plugins"
git clone https://github.com/eve-ai-dev/steroids-openai-image-gen.git
hermes plugins enable steroids-openai-image-gen

# Restart gateway
hermes gateway restart
```

For profile-specific installs:
```bash
cd "${HERMES_HOME:-$HOME/.hermes}/profiles/<profile>/plugins"
git clone https://github.com/eve-ai-dev/steroids-openai-image-gen.git
```

---

## Configuration

### Mode 1: OpenAI-Compatible Endpoint

```yaml
# config.yaml
image_gen:
  provider: steroids-openai
  model: gpt-image-2
  steroids-openai:
    mode: openai-compatible
    base_url: ${OPENAI_BASE_URL}
    api_key_env: OPENAI_API_KEY
    model: gpt-image-2
    quality: medium
    max_reference_images: 16
```

- Text-only prompts → `POST {base_url}/images/generations`
- Edits/references → `POST {base_url}/images/edits` (multipart)
- Expected response: `{"data": [{"b64_json": "...", "revised_prompt": "optional"}]}`
- URL responses are accepted and cached locally

### Mode 2: Direct Codex Auth

```yaml
image_gen:
  provider: steroids-openai
  model: gpt-image-2
  steroids-openai:
    mode: codex-auth
    model: gpt-image-2
    quality: medium
    max_reference_images: 16
```

Uses Hermes' internal Codex auth helper  --  no external image endpoint needed.

---

## Enhanced Tool Schema

The plugin registers an extended `image_generate` schema:

```json
{
  "prompt": "make the red square blue",
  "aspect_ratio": "square",
  "quality": "medium",
  "image_url": "/path/source.png",
  "reference_image_urls": ["/path/ref.png"]
}
```

---

## Background Job Processing

```json
// Single job
{
  "prompt": "generate hero image for landing page",
  "aspect_ratio": "landscape"
}

// Batch jobs
{
  "jobs": [
    {"prompt": "hero image", "aspect_ratio": "landscape"},
    {"prompt": "logo variant", "aspect_ratio": "square"}
  ]
}
```

Jobs persist at `${HERMES_HOME}/steroids_openai_image_gen/jobs/<job_id>/`:
- `status.json`  --  current state
- `result.json`  --  on completion
- `delivery_event.json`  --  routing metadata

Check job status with `image_generate_background_status` using the returned `job_id`.

---

## Compatibility Notes

- **Model:** Use `gpt-image-2` (not `gpt-image-2-medium`); `quality` is a separate parameter
- **Edit Endpoints:** Must support multipart `image` + `image[]` and return `b64_json`
- **Env Expansion:** The plugin handles `${ENV_VAR}` expansion in config itself

---

## Verification

```bash
# Check plugin loaded
hermes plugins list | grep steroids

# Test via chat
hermes chat
> Generate a simple blue square image
```

---

*Repo: [eve-ai-dev/steroids-openai-image-gen](https://github.com/eve-ai-dev/steroids-openai-image-gen)*
