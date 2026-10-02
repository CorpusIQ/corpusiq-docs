---
title: Generative Media Skills - 153-Skill Media Suite
description: "calesthio/generative-media-skills - 153 research-backed media production skills (45 skills.sh-indexed, 2.1K combined installs): provider intelligence for image/video/audio/voice models, production craft direction, and deterministic QA scripts. Explicit Hermes support via HERMES.md."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/generative-media-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-26"
tags: ["hermes skill", "agent skill", "skill setup", "media production", "video generation", "image generation", "text to speech", "elevenlabs", "hyperframes", "heygen", "ugc video"]
---

# Generative Media Skills - Setup Guide

**Source:** [calesthio/generative-media-skills](https://skills.sh/calesthio/generative-media-skills)
**GitHub:** [calesthio/generative-media-skills](https://github.com/calesthio/generative-media-skills) (137⭐, MIT, published July 11, 2026)
**Skills:** 153 packages across 25 categories (45 indexed on skills.sh at 43-77 installs each, 2,143 combined indexed installs)
**Category:** Media Production / Generative AI Operations
**First Seen:** August 26, 2026 sweep
**Quality Tier:** 🔵 Community - high craft quality (per-skill `EVAL.md`, dated fact verification, progressive disclosure) but low install counts and no extracted marketplace audit verdicts; inspect SKILL.md packages before production use

The Generative Media Skills suite is a complete media production brain for AI agents: 153 hand-researched skill packages spanning provider intelligence (image, video, TTS, voice, music, avatar, 3D), production craft (cinematography, editing, sound design, post-production), content formats (ads, shorts, podcasts, demos, trailers), and deterministic QA tooling. It is one of the few skills.sh suites that names Hermes explicitly - the repo ships a `HERMES.md` entrypoint and the README lists "OpenClaw/Hermes-style agents" as a first-class target.

This maps directly onto CorpusIQ's daily media pipeline: UGC video generation, GPT-Image-2 image production, HyperFrames and Remotion composition, and the pending ElevenLabs voiceover migration.

---

## Installation

The maintained-checkout pattern (recommended - keeps all 153 skills updateable with `git pull`):

```bash
git clone https://github.com/calesthio/generative-media-skills.git
```

```yaml
# ~/.hermes/config.yaml
skills:
  external_dirs:
    - /absolute/path/to/generative-media-skills/skills
```

Or via the skills.sh marketplace CLI (verified working Aug 26, 2026 - discovers 151 of 153 packages):

```bash
# Install the whole suite
npx skills add calesthio/generative-media-skills

# Install a single skill
npx skills add calesthio/generative-media-skills -s openai-gpt-image

# List available skills without installing
npx skills add calesthio/generative-media-skills --list
```

Skills live under `skills/providers/<category>/<skill>/` and `skills/production/<category>/<skill>/`. Each package is plain Markdown (`SKILL.md`) plus optional `scripts/`, `references/`, and `assets/` - copy any individual package into `~/.hermes/profiles/<profile>/skills/` and Hermes loads it natively.

**Known issue:** the CLI skips 2 packages with a YAML parse error (`amazon-rekognition`, `google-cloud-vision` - multi-line frontmatter descriptions that trip the strict parser). Install those two by copying their directories manually.

## Prerequisites

| Requirement | Details |
|---|---|
| **Provider API keys (per skill)** | Provider skills cite APIs but never bundle keys. Image skills need OpenAI/Stability/Flux keys; TTS skills need ElevenLabs/Cartesia/OpenAI keys; video skills need Runway/Kling/Veo keys - only for the providers you actually use |
| **Runtime tooling (skill-dependent)** | `ffmpeg-media-finishing` needs ffmpeg; `comfyui-media-workflows` needs a ComfyUI instance; `hyperframes-video-composition` needs the HyperFrames runtime; `remotion-video-composition` needs Node + Remotion |
| **Hermes Agent** | Any version that loads SKILL.md packages; no minimum version constraint |

No account registration is required for the suite itself - it is MIT-licensed Markdown + scripts.

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| generative-media-skills (meta) | 77 | Suite entrypoint - routes a brief to the right provider and production skills |
| editing-montage | 63 | Montage/editing craft: rhythm, match cuts, structure |
| cinematic-shot-direction | 62 | Shot plans, camera language, lighting intent for video generation prompts |
| audio-mixing-mastering | 59 | Loudness, balance, and delivery mastering for voiceover and music tracks |
| color-grading-finishing | 58 | Look consistency and finishing passes across a shot series |
| generated-media-qa | 57 | Deterministic QA checks on generated media output |
| character-design-continuity | 54 | Keeping a character/avatar visually consistent across shots |
| storyboard-previsualization | 54 | Previsualization boards before committing to renders |
| ecommerce-product-imagery | 53 | Product image production for commerce pages |
| ffmpeg-media-finishing | 52 | FFmpeg-driven finishing: containers, codecs, captions, checksums |
| media-qc-delivery | 51 | Delivery-time QC: specs, manifests, platform requirements |
| social-short-production | 49 | Vertical social short format: hooks, pacing, platform specs |
| hyperframes-video-composition | - | HyperFrames timeline composition (matches CorpusIQ's HyperFrames stack) |
| heygen-avatar-video | - | HeyGen avatar video production |
| openai-gpt-image | - | GPT Image 2/1.5 workflows - matches CorpusIQ's gpt-image-2-medium backend |
| elevenlabs-tts | - | ElevenLabs voiceover production - the pending fix for the rejected macOS `say` voice |
| ugc-ad-production | - | UGC-style ad production playbook |
| remotion-video-composition | - | Remotion React video composition |
| media-provenance-rights | 47 | Provenance, consent, and rights records for published media |

Full catalog: `SKILL_INDEX.md` in the repo (153 packages: 25 categories split into Providers and Production families).

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Daily UGC video pipeline** | `ugc-ad-production` + `social-short-production` replace ad-hoc scripting with researched format specs; `media-qc-delivery` adds a deterministic QA pass before Postiz posting |
| **Image production consistency** | `openai-gpt-image` encodes the current GPT Image 2 lifecycle (aliases, deprecations, cost limits) - exactly the backend `image_generate` uses; pairs with the GPT-Image-2 Style Library already catalogued |
| **Voiceover migration** | `elevenlabs-tts` + `elevenlabs-dubbing-voice-conversion` provide the researched playbook for moving off macOS `say -v Samantha` (rejected for robotic quality) to ElevenLabs voices |
| **HyperFrames compositions** | `hyperframes-video-composition` and `comfyui-media-workflows` (which validates HyperFrames timelines) harden the existing HyperFrames UGC pipeline |
| **Social QA + rights** | `generated-media-qa` + `media-provenance-rights` gate every outgoing asset - scriptable checks instead of eyeballing, plus provenance records for platform disputes |

## Limitations / Verification

- Install counts are modest (43-77 per indexed skill). The value is the research craft: every SKILL.md carries dated fact verification and per-package `EVAL.md` scoring.
- Marketplace security audit verdicts (Gen Agent Trust Hub / Socket / Snyk) were not extracted this sweep - inspect `scripts/` folders before running anything in production; most packages are Markdown-only.
- Provider facts (prices, limits, deprecations) are marked volatile and dated (e.g., gpt-image-1 deprecation verified 2026-07-09) - re-verify against the linked official docs before quoting to users.
- The repo was last pushed July 14, 2026 - treat provider sections as snapshots of that date.

## Related

- [GPT-Image-2 Style Library Setup](/hermes/skills/catalog/gpt-image-2-style-library-setup) - style templates for the same image backend
- [Skills Marketplace](/hermes/skills/marketplace) - marketplace index for more discovery batches
- [New Skills - August 26, 2026](/hermes/skills/marketplace/new-aug26-2026) - discovery page for this sweep

*Powered by CorpusIQ*
