---
title: "Pexo Video Skills — AI Video Generation Suite Setup"
description: "pexoai/pexo-skills — 24 skills, 62.5K total installs. pexo-agent (39.4K), videoagent-video-studio (10.4K), image-studio, audio-studio, Seedance and Veo 3.2 prompters, plus ad/short-form video skills (youtube-short-maker, tiktok-video-ad, saas-video, startup-video, launch-video)."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/pexo-video-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-14"
tags: ["hermes skill", "agent skill", "skill setup", "video generation", "text to video", "seedance", "veo"]
---

# Pexo Video Skills — Setup Guide

**Source:** [pexoai/pexo-skills](https://skills.sh/pexoai/pexo-skills)
**GitHub:** [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills)
**Skills:** 24 skills · 62.5K total installs
**Category:** AI Video Generation & Media Production
**First Seen:** August 14, 2026 evening sweep
**Quality Tier:** 🟡 Beta (community/vendor suite)

Pexo's skill suite centers on agentic video production. The flagship `pexo-agent` skill (39.4K installs) drives the Pexo agent; the `videoagent-*` studios cover video, image, and audio generation pipelines. Dedicated prompter skills wrap video models (Seedance 2.0, Veo 3.2) and there are purpose-built skills for short-form formats — youtube-short-maker, tiktok-video-ad, product-video, video-ad, saas-video, startup-video, launch-video, founder-video, explainer-video — plus text-to-video, image-to-video, and make-a-video workflows.

---

## Installation

```bash
npx skills add pexoai/pexo-skills
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Pexo account** | `pexo-agent` drives the Pexo platform — check account requirements on the GitHub repo |
| **Video model access** | Seedance / Veo 3.2 prompters need access to those models (API keys or platform accounts) |
| **Node.js + npx** | For the `skills add` installer |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| pexo-agent | 39.4K | Primary Pexo agent driver |
| videoagent-video-studio | 10.4K | Video generation studio workflow |
| videoagent-image-studio | 5.5K | Image generation studio workflow |
| videoagent-audio-studio | 3.9K | Audio generation studio workflow |
| seedance-2.0-prompter | 1.2K | Prompting for Seedance 2.0 video model |
| veo-3.2-prompter | 411 | Prompting for Veo 3.2 video model |
| Short-form & ads | 42–55 each | youtube-short-maker, tiktok-video-ad, product-video, video-ad, saas-video, startup-video, launch-video, founder-video |

## Quick Start

1. `npx skills add pexoai/pexo-skills`
2. Set up the Pexo account per the GitHub repo instructions
3. Ask: "generate a 30-second SaaS launch video for CorpusIQ's Open BI Layer"
4. For model-native work: "write a Seedance 2.0 prompt for a product demo clip"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Launch & promo videos** | launch-video, startup-video, and saas-video skills for CorpusIQ product moments |
| **Short-form pipeline** | youtube-short-maker and tiktok-video-ad feeding the social cadence engine |
| **Video model prompting** | Seedance / Veo prompters as a complement to the HeyGen and HyperFrames pipelines |
| **Media experiments** | image/audio studio skills for thumbnail and audio asset generation |

## Limitations / Verification

- Platform-gated: the Pexo agent and model prompters need external account/API access — verify before committing to a pipeline
- Not a replacement for the existing Postiz/HeyGen/HyperFrames stack; evaluate as a complementary model-native route

```bash
npx skills list | grep pexo
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [HyperFrames Video Pipeline](/hermes/skills/catalog/) — existing CorpusIQ video stack
- [RunComfy Agent Skills](/hermes/skills/marketplace/new-aug12-2026-runcomfy/) — prior video suite sweep

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*

*Powered by CorpusIQ*
