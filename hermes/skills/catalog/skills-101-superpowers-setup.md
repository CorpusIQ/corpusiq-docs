---
title: "Skills-101 Superpowers — AI Media & Automation Pack"
description: "Install skills-101/superpowers (488.4K combined installs) — 86 skills: AI video/image/avatar generation, ElevenLabs audio cluster, twitter automation, agent browser, Remotion rendering, and growth playbooks."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/skills-101-superpowers-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Skills-101 Superpowers — Setup Guide

**Source:** [skills-101/superpowers](https://www.skills.sh/skills-101/superpowers) (488.4K combined installs)
**GitHub:** [github.com/skills-101/superpowers](https://github.com/skills-101/superpowers)
**Category:** AI Media / Automation
**First Seen:** August 12, 2026
**Quality Tier:** 🟡 Beta (fast-growing superpowers fork)

`skills-101/superpowers` is an extended edition of the classic `obra/superpowers` library, tuned for AI media and growth automation. The four headline skills — `ai-video-generation`, `ai-image-generation`, `ai-avatar-video`, and `twitter-automation` — each carry ~88K installs. Below them sits a deep bench: an ElevenLabs audio cluster (TTS, STT, dubbing, music, voice cloning), Flux and Qwen image models, agent browser tooling, and 50+ growth/content playbooks.

> **Note:** This is a different publisher from `101-skills/skills` (covered in the [AI Video Generation guide](/hermes/skills/catalog/ai-video-generation-setup/)) — same family, different repo and skill set.

---

## Installation

```bash
# Install the full repo (86 skills)
npx skills add skills-101/superpowers

# Or install the headline skills
npx skills add skills-101/superpowers --skill ai-video-generation
npx skills add skills-101/superpowers --skill ai-image-generation
npx skills add skills-101/superpowers --skill ai-avatar-video
npx skills add skills-101/superpowers --skill twitter-automation
```

---

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| `ai-video-generation` | 88.1K | Text-to-video via multiple model backends |
| `ai-image-generation` | 88.0K | Text-to-image generation |
| `ai-avatar-video` | 87.9K | Talking-head / avatar video |
| `twitter-automation` | 87.9K | X/Twitter posting and automation |
| `agent-browser` | 16.6K | Browser control from agents |
| `web-search` | 11.1K | Search integration |
| `infsh-cli` | 11.1K | Inference.sh CLI workflow |
| `agent-tools` | 11.1K | General agent toolset |
| `remotion-render` | 11.1K | Remotion video rendering |
| `python-executor` | 11.1K | Sandboxed Python execution |

**Model connectors:** `flux-image`, `qwen-image-2`, `nano-banana`, `gpt-image`, `seedance`, `happyhorse`, `google-veo`, `p-video`, `p-image` — single-skill wrappers per generation model.

**ElevenLabs cluster:** `elevenlabs-tts`, `elevenlabs-stt`, `elevenlabs-dubbing`, `elevenlabs-music`, `elevenlabs-voice-isolator`, `elevenlabs-voice-changer`, `elevenlabs-sound-effects`, `elevenlabs-dialogue`.

**Growth & content playbooks (~50):** `landing-page-design`, `storyboard-creation`, `competitor-teardown`, `product-hunt-launch`, `video-ad-specs`, `product-photography`, `youtube-thumbnail-design`, `seo-content-brief`, `press-release-writing`, `case-study-writing`, `content-repurposing`, `newsletter-curation`, `social-media-carousel`, `twitter-thread-creation`, `linkedin-content`, `email-design`, `og-image-design`, `pitch-deck-visuals`, and more.

---

## Prerequisites

| Requirement | Details |
|---|---|
| Node.js + npx | For the skills.sh CLI install path |
| API keys per backend | ElevenLabs, Flux/Qwen/Veo endpoints, or Inference.sh for media skills |
| X/Twitter credentials | For `twitter-automation` |

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **UGC video pipeline** | `ai-video-generation` + `ai-avatar-video` + `storyboard-creation` as an alternative/complement to RunComfy and HyperFrames |
| **Voiceover** | ElevenLabs cluster replaces macOS TTS (long-standing pipeline gap) |
| **Social automation** | `twitter-automation` + `content-repurposing` for the X presence |
| **Launch playbooks** | `product-hunt-launch` + `competitor-teardown` for go-to-market |

---

## Limitations / Verification

- Fork of `obra/superpowers` — verify upstream differences before relying on behavior parity
- ~50 playbook skills have 17-19 installs each; treat the install counts as community votes on the headline four
- Verify install: `npx skills list | grep -E "ai-video|elevenlabs|twitter-automation"`

---

## Related

- [Obra Superpowers Setup](/hermes/skills/catalog/obra-superpowers-setup/)
- [RunComfy Agent Skills Setup](/hermes/skills/catalog/runcomfy-agent-skills-setup/)
- [AI Video Generation Setup](/hermes/skills/catalog/ai-video-generation-setup/)

*Powered by CorpusIQ*
