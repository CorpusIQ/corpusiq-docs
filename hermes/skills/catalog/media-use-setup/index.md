---
title: Media Use — Setup Guide for Hermes Agents
description: Install and use the media-use skill from heygen-com/hyperframes. Agent Media OS — resolve, generate, and operate on BGM, SFX, images, icons, voice, and color grades. 182.7K+ installs on skills.sh.
---

# Media Use — Setup Guide

**Source:** [heygen-com/hyperframes](https://skills.sh/heygen-com/hyperframes/media-use) (HeyGen)
**Skill:** `media-use` · **Installs:** 182.7K+ · **Category:** Media & Video
**Platform:** Linux, macOS, Windows

The single skill for every media need in a HyperFrames project. Resolve background music, sound effects, images, icons, brand logos, voiceover, and color grades into frozen local files. Generate via TTS, music, and image models when the catalog misses. Operate on media (cut, reframe, transform). Reuse assets across projects.

Think of it as the "media OS" — one verb (`resolve`), one skill, zero context noise.

---

## Installation

```bash
npx skills add heygen-com/hyperframes --skill media-use
```

The skill installs to your Hermes skills directory. It includes a `resolve.mjs` script, reference docs for each media type, and provider configuration.

---

## Prerequisites

| Requirement | Details |
|-------------|---------|
| **Node.js** | v18+ (required by resolve.mjs) |
| **HeyGen CLI** | Free-usage path available. Install via `npm i -g @heygen/cli` or use bundled setup |
| **API Keys (optional)** | TTS providers (HeyGen free tier, ElevenLabs, Kokoro local), music generation, image models |
| **HyperFrames ecosystem** | Not required standalone; `media-use` works independently |

---

## Quick Start

### 1. Verify Installation

```bash
node <SKILL_DIR>/scripts/resolve.mjs --doctor
```

Confirms all providers are accessible and the skill is ready.

### 2. Resolve Your First Asset

The `resolve` verb is the single entry point for all media types:

```bash
node <SKILL_DIR>/scripts/resolve.mjs --type <type> --intent "<description>" --project <dir>
```

Returns one line: `resolved <id> → <path> (<type>, <metadata>)`.

### 3. Supported Media Types

| Type | Description | Intent Example |
|------|-------------|----------------|
| `bgm` | Background music (10K+ tracks) | "upbeat corporate intro with synth pad" |
| `sfx` | Sound effects (bundled 19-file library + catalog) | "notification ping, soft and modern" |
| `image` | Photos, backgrounds (75K+ vectors) | "city skyline at sunset, warm tones" |
| `icon` | Icons, symbols (transparent) | "download arrow, minimal, 24px" |
| `logo` | Official brand marks (never redrawn) | "stripe" → auto-resolves from svgl/simple-icons |
| `voice` | TTS voiceover (HeyGen free / ElevenLabs / Kokoro) | "professional narrator, medium pace" |
| `grade` | Color correction / grading measurement | "warm cinematic, kodak portra 400 feel" |
| `lut` | User-provided .cube LUT file | "path/to/film-look.cube" |

### 4. Check Candidates Before Resolving Fresh

Always check for reusable candidates first:

```bash
node <SKILL_DIR>/scripts/resolve.mjs --type bgm --candidates
```

The skill maintains an internal ledger — assets resolved in one project are reusable in others.

---

## Key Workflows

### Voiceover from Script

```bash
# Generate TTS voiceover from a script
node <SKILL_DIR>/scripts/resolve.mjs --type voice \
  --intent "narrate: 'Welcome to CorpusIQ. Let me show you how...'" \
  --project ./my-video
```

### Background Music for Video

```bash
# Search the 10K+ track HeyGen music catalog
node <SKILL_DIR>/scripts/resolve.mjs --type bgm \
  --intent "cinematic ambient, 120bpm, strings and piano" \
  --project ./my-video
```

### Color Grade for Footage

```bash
# Measure and propose a corrective grade
node <SKILL_DIR>/scripts/resolve.mjs --type grade \
  --for "the hero shot feels underexposed and flat" \
  --project ./my-video
```

The skill inspects the actual footage, proposes one correction, and persists it. It never silently mutates — you approve before application.

### Icon Resolution

```bash
# Resolve an icon (transparent PNG)
node <SKILL_DIR>/scripts/resolve.mjs --type icon \
  --intent "chart line graph, minimal, blue" \
  --project ./dashboard
```

---

## Proactive Media Scanning

When building or reviewing HyperFrames compositions, run a media opportunity pass:

| Signal Detected | Action |
|----------------|--------|
| Text/script with no voiceover | Offer TTS voiceover |
| Emoji or CSS-styled icon | Resolve a real icon |
| Placeholder/tiny/upscaled image | Resolve a better image |
| Hard cuts with no sound | Add transition SFX |
| Piece >10s with no music bed | Resolve BGM |
| Under/over-exposed footage | Propose corrective grade |
| Flat-feeling photographic media | Suggest source-appropriate preset |

**Rules:** One consolidated ask per project. Respect "leave it." Never silently mutate.

---

## Reference Files

The skill includes detailed reference docs for each domain:

| Task | Reference File |
|------|---------------|
| Asset resolution, reuse, adoption, flags | `references/resolve.md` |
| Color grading, LUTs, smart grade | `references/grading.md` |
| Voiceover, TTS, music, SFX, captions | `references/audio.md` |
| Cut, reframe, transform, HEVC | `references/operations.md` |
| Creative treatments, effects, reveals | `references/media-treatments.md` |
| Install, auth, providers, RAM ladders | `references/setup-providers.md` |
| Remembered preferences, recipes | `references/memory.md` |

---

## Provider Setup

The skill supports multiple providers for generation. Configure in `references/setup-providers.md`:

- **TTS:** HeyGen (free tier), ElevenLabs, Kokoro (local)
- **Music:** HeyGen catalog (10K+ tracks), Suno, Udio
- **Images:** DALL·E, Midjourney, Stable Diffusion
- **Icons:** Simple Icons, svgl, bundled library
- **Color:** Built-in measurement engine (no API key required)

---

## Related Skills

- [HyperFrames Setup Guide](/hermes/skills/catalog/hyperframes-setup/) — Core video composition skill
- [AI Video Generation Setup](/hermes/skills/catalog/ai-video-generation-setup/) — General AI video creation
- [SamuraiGPT Generative Media](/hermes/skills/catalog/samuraigpt-generative-media-setup/) — Alternative media generation

---

*Part of the HyperFrames ecosystem by HeyGen. 182.7K+ installs on skills.sh. Hermes setup guide maintained by CorpusIQ.*
