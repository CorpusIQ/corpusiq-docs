---
title: New Skills — June 18, 2026 Update 2 (HyperFrames Video Ecosystem)
description: 6 newly catalogued skills — the official Hermes Agent hyperframes skill (nousresearch) plus 5 HyperFrames SDK skills from heygen-com/hyperframes (103K+ installs each) — enabling agentic HTML-based video creation.
---

# New Skills — June 18, 2026 Update 2 (HyperFrames Ecosystem)

**Source:** [nousresearch/hermes-agent](https://skills.sh/nousresearch/hermes-agent) and [heygen-com/hyperframes](https://skills.sh/heygen-com/hyperframes) via [skills.sh](https://skills.sh)
**Date:** June 18, 2026 (PM update)
**Total new:** 6 skills (1 official Hermes + 5 HyperFrames SDK ecosystem)

The `hyperframes` skill from nousresearch/hermes-agent enables HTML-based video creation directly from Hermes Agent prompts — animated title cards, social overlays, captioned videos, shader transitions, and audio-reactive visuals. It wraps the massive HyperFrames SDK ecosystem (heygen-com/hyperframes) which has 470K+ total installs across 5 skills — making this one of the largest video creation ecosystems on skills.sh.

---

## Official Hermes Agent Skill (1 skill)

| # | Skill | Installs | Description |
|---|-------|----------|-------------|
| 1 | `hyperframes` | 13 | Create HTML-based video compositions, animated title cards, social overlays, captioned talking-head videos, audio-reactive visuals, and shader transitions — all from Hermes Agent |

### Installation

```bash
npx skills add nousresearch/hermes-agent --skill hyperframes
```

### Quick Start

```bash
# List available templates
bash SKILL_DIR/scripts/templates.sh --list

# Render a test title card
bash SKILL_DIR/scripts/render.sh --template title-card --text "Hello World" --output /tmp/test.mp4
```

**→ Full setup guide:** [HyperFrames Setup Guide](/hermes/skills/catalog/hyperframes-setup/)

---

## HyperFrames SDK Ecosystem (5 skills)

The HyperFrames SDK (heygen-com/hyperframes) provides the underlying rendering engine. These skills are the building blocks that the official Hermes hyperframes skill wraps. All have 74K+ installs each.

| # | Skill | Installs | Description |
|---|-------|----------|-------------|
| 1 | `hyperframes` | 103,094 | Core HyperFrames SDK — HTML video composition engine, scene graph, timeline control |
| 2 | `hyperframes-cli` | 99,994 | HyperFrames CLI — render compositions from the command line, batch processing |
| 3 | `hyperframes-registry` | 96,452 | HyperFrames template registry — discover, install, and manage video templates |
| 4 | `hyperframes-media` | 74,141 | HyperFrames media pipeline — asset management, encoding, transcoding |
| 5 | `gsap` | 92,222 | GSAP animation library integration — timeline animations, easing, sequencing |

### Installation (Ecosystem)

```bash
# Core SDK
npx skills add heygen-com/hyperframes --skill hyperframes

# CLI (recommended for automation)
npx skills add heygen-com/hyperframes --skill hyperframes-cli

# Template registry
npx skills add heygen-com/hyperframes --skill hyperframes-registry
```

These are installed automatically as dependencies when using the official Hermes Agent hyperframes skill. Direct install is only needed for standalone HyperFrames usage outside Hermes.

---

## Why This Matters for CorpusIQ

The hyperframes skill fills a critical gap in the CorpusIQ video automation pipeline:

1. **Agent-native video creation** — No more external tools. Hermes agents can now generate video content directly from prompts.
2. **Daily UGC automation** — The 5-format rotating video series (tips, Q&A, case studies, demos, behind-the-scenes) can now be fully automated with hyperframes generating overlays, captions, and animations.
3. **Massive ecosystem backing** — 470K+ total installs across the HyperFrames SDK means battle-tested infrastructure.
4. **HTML-based rendering** — Compositions are HTML/CSS/JS, making them editable, version-controllable, and infinitely customizable.

---

## Catalog Updates

- **New setup guide:** [HyperFrames Setup Guide](/hermes/skills/catalog/hyperframes-setup/) — full installation, capabilities, CLI reference, and CorpusIQ use cases
- **Marketplace index:** Updated with this page

---

*← [Skills Marketplace](/hermes/skills/marketplace/) | [June 18 Ecosystem Tools](/hermes/skills/marketplace/new-june18-2026-ecosystem/) →*
*↑ [Skills Catalog Home](/hermes/skills/catalog/)*
*Powered by CorpusIQ*
