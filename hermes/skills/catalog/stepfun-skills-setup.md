---
title: StepFun (阶跃星辰) — Full Setup Guide for Hermes Agents
description: Install and configure the StepFun API skills from fengjunlu618/stepfun-skills. First Chinese LLM provider for Hermes Agent — multimodal reasoning, TTS, ASR, image generation, real-time voice, and RAG via Step Plan subscription.
---

# StepFun (阶跃星辰) — Setup Guide

**Source:** [fengjunlu618/stepfun-skills](https://github.com/fengjunlu618/stepfun-skills)
**Category:** LLM Provider / Multimodal

The first Chinese LLM provider skill suite for Hermes Agent. Provides access to StepFun's full model lineup — multimodal reasoning, text-to-speech, speech recognition, image generation, real-time voice, and search/RAG — all through a Step Plan subscription channel (separate from standard API billing).

---

## Installation

```bash
# Clone the repo
git clone https://github.com/fengjunlu618/stepfun-skills.git
mkdir -p ~/.hermes/skills/llm-providers/stepfun
cp -a stepfun-skills/* ~/.hermes/skills/llm-providers/stepfun/
```

Individual skills:

| Skill | Command |
|---|---|
| **stepfun-chat** | Chat Completions — text reasoning, multimodal, Tool Call, routing |
| **stepfun-tts** | TTS + voice cloning — Contextual TTS, 19 official voices |
| **stepfun-image** | Text-to-image + image editing — 1-2s generation |
| **stepfun-asr** | Speech recognition — async file + streaming |
| **stepfun-realtime** | Real-time voice conversation — speech ↔ speech |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **StepFun Account** | Register at [platform.stepfun.com](https://platform.stepfun.com) |
| **Step Plan Subscription** | Required — calls go through Step Plan (not standard API credit) |
| **STEPFUN_API_KEY** | Set in `~/.hermes/.env`: `STEPFUN_API_KEY=sk-...` |
| **Hermes Agent** | v0.15.0+ |

---

## Key Capabilities

### Model Lineup

| Model | Type | Price | Capability |
|---|---|---|---|
| `step-3.7-flash` | Multimodal Reasoning | ¥1.35/1M tokens | Native multimodal (image/video) + reasoning + agent + Tool Call |
| `step-3.5-flash-2603` | Agent Optimized | ¥0.7/1M tokens | Reasoning + agent + low-reasoning mode |
| `step-3.5-flash` | Flagship Reasoning | ¥0.7/1M tokens | Reasoning + Tool Call |
| `step-router-v1` | Smart Router | Per-hit billing | Pro + Flash dual engine |
| `step-1o-turbo-vision` | Vision Understanding | ¥2.5/1M tokens | Image/video understanding |
| `stepaudio-2.5-tts` | Speech Synthesis | ¥5.8/10K chars | Contextual TTS |
| `step-tts-mini` | Speech Synthesis | ¥0.9/10K chars | CN/EN/JP/Cantonese/Sichuan |
| `stepaudio-2.5-asr` | Speech Recognition | ¥0.15/hour | 4B MTP ultra-fast |
| `stepaudio-2.5-realtime` | Real-time Voice | ¥10/1M tokens | Speech ↔ speech |
| `step-image-edit-2` | Image Gen/Edit | ¥0.02/image | Text-to-image + editing |
| `step-2x-large` | Text-to-Image | ¥0.1/image | Strong text rendering |

### Core Features

| Capability | How to Trigger | Notes |
|---|---|---|
| **Chat/Multimodal** | Load `stepfun-chat` skill, use natural language | Supports image + video input |
| **Text-to-Speech** | Load `stepfun-tts` skill, "Generate speech from [text]" | 19 official voices + voice cloning |
| **Image Generation** | Load `stepfun-image` skill, "Generate image of [description]" | 1-2s generation, text-in-image support |
| **Speech Recognition** | Load `stepfun-asr` skill, "Transcribe [audio file]" | Async file + streaming modes |
| **Real-time Voice** | Load `stepfun-realtime` skill | Speech ↔ speech conversation |

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Multilingual Content** | Use StepFun for Chinese market content generation and analysis |
| **Voice Agent Pipeline** | ASR → Chat → TTS for autonomous phone/voice operations |
| **Cost Optimization** | Route Chinese-language tasks to StepFun (¥0.7/1M tokens vs GPT-4 pricing) |
| **Video Analysis** | `step-1o-turbo-vision` for Chinese video content understanding |
| **Image Generation** | `step-image-edit-2` for social media assets at ¥0.02/image |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| 401 Unauthorized | Verify `STEPFUN_API_KEY` in `~/.hermes/.env` |
| Billing errors | Ensure Step Plan subscription is active (not standard API credit) |
| Model not found | Check model name exactly — StepFun model IDs are case-sensitive |
| Rate limiting | Step Plan has per-minute quotas; stagger requests |

## Verification

```bash
# Verify skill installed
hermes skills list | grep stepfun

# Test API key
curl -s -H "Authorization: Bearer $STEPFUN_API_KEY" \
  "https://api.stepfun.com/v1/models" | head -20
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Discovery Page](/hermes/skills/marketplace/new-june23-2026/) →*
*Powered by CorpusIQ*
