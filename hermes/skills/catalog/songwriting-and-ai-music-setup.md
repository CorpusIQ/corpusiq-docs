---
title: Songwriting & AI Music Generation — Hermes Skill Setup Guide
description: Install and configure songwriting-and-ai-music, the official Hermes Agent skill for AI-assisted songwriting, music generation, and audio production — 324 installs.
---

# Songwriting & AI Music Generation — Setup Guide

**Source:** [nousresearch/hermes-agent](https://skills.sh/nousresearch/hermes-agent/songwriting-and-ai-music) (324 installs)
**Category:** Creative / Music
**License:** MIT · **Platforms:** Linux, macOS, Windows
**Dependencies:** None (guideline-based skill)

A creative guideline skill for AI-assisted songwriting and music generation. Covers song structure patterns (ABABCB, AABA, ABAB, AAA), lyrical composition, and integration with AI music generation tools. Art-forward: everything is a guideline, not a rule.

---

## What It Does

| Capability | How |
|-----------|-----|
| **Song structure** | Common skeletons — pop/rock, jazz, folk, storytelling |
| **Lyrical composition** | Verse, chorus, bridge, refrain patterns |
| **Genre awareness** | Structure conventions for different musical styles |
| **AI music integration** | Hooks for AI music generation tools (Suno, Udio, etc.) |
| **Creative workflow** | End-to-end songcraft from concept to arrangement |

---

## Installation

### Via skills.sh (Recommended)

```bash
npx skills add https://github.com/nousresearch/hermes-agent --skill songwriting-and-ai-music
```

### Direct from Hermes Agent Repo

```bash
git clone --depth 1 https://github.com/nousresearch/hermes-agent.git /tmp/hermes-agent
cp -r /tmp/hermes-agent/skills/creative/songwriting-and-ai-music ~/.hermes/skills/
```

---

## Usage

The skill activates when Hermes encounters songwriting, music composition, or lyrical requests. It provides structural templates and creative guidance rather than hard rules.

### Song Structure Templates

| Structure | Pattern | Best For |
|-----------|---------|----------|
| ABABCB | Verse/Chorus/Verse/Chorus/Bridge/Chorus | Pop, rock |
| AABA | Verse/Verse/Bridge/Verse | Jazz standards, ballads |
| ABAB | Verse/Chorus alternating | Simple, direct songs |
| AAA | Verse/Verse/Verse (strophic) | Folk, storytelling |

### Example Prompts

```
"Write a pop song about AI agents helping small businesses"
"Compose a folk ballad with an AABA structure about remote work"
"Generate lyrics for a rock anthem with ABABCB structure"
```

---

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Hermes Agent | v0.14.0+ |
| Optional: AI music tool | Suno, Udio, or similar for audio generation |

---

## Verification

After install, test with:

```
Hermes, write a short song using the ABABCB structure about debugging code at midnight.
```

The agent should respond with a structured song following the pattern.

---

## Pitfalls

- **Not an audio generator:** This skill provides lyrical/structure guidance. For actual audio generation, pair with an AI music tool (Suno, Udio, Audiocraft).
- **Guidelines, not rules:** The skill explicitly states "Art breaks rules on purpose." Don't expect rigid enforcement of structures.
- **Genre appropriateness:** Some structures work better for certain genres — the skill will guide but the user should confirm fit.

---

**Installed via:** `npx skills add nousresearch/hermes-agent --skill songwriting-and-ai-music`
