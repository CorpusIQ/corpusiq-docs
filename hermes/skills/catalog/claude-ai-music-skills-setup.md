---
title: "Music Production Skills - Songwriting, Lyrics and Release"
description: "Human and AI music production for Suno from bitwize-music-studio: 14.6K combined installs across 63 listings covering lyrics, mastering and release."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claude-ai-music-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-19"
tags: ["hermes skill", "agent skill", "skill setup", "music production", "suno", "audio mastering", "lyrics"]
---

# Music Production Skills - Setup Guide

**Source:** [bitwize-music-studio/claude-ai-music-skills](https://www.skills.sh/bitwize-music-studio/claude-ai-music-skills) via skills.sh - 14.6K combined installs across 63 indexed listings; first seen Nov 19, 2026 (Nov 19, 2026 evening sweep)

**GitHub:** 681 stars, CC0-1.0 licence, main branch, last pushed Nov 20, 2026. Skills live in `skills/<name>/SKILL.md` (61 skill folders), with a Python MCP server in `servers/`, audio and sheet-music tooling in `tools/`, 72 genre guides in `genres/`, and `reference/`, `templates/`, `config/` and a large `tests/` tree alongside.

**Category:** AI music production and album workflow

**Quality Tier:** 🟠 Orange - 1 Fail and 3 Warn among the 16 sampled skills.sh verdicts (release-director fails Snyk); CC0-1.0 licence.

bitwize-music-studio publishes a Claude Code plugin that turns a conversation into a full album production pipeline. You describe what you want to make, and the plugin handles concept development, lyrics, Suno style prompts, audio mastering, and release preparation, with quality gates and source verification at each stage.

The suite is notable for its depth rather than its breadth of domains: 61 skills split across a creative tier (Opus), a reasoning tier (Sonnet) and a mechanical tier (Haiku), a Python MCP server exposing 80+ tools, a 10-domain research system for documentary and true-story albums, and 72 genre directories with production guides and mastering presets. macOS, Linux, WSL2 and native Windows are all supported.

## Installation

Install the plugin inside Claude Code:

```bash
/plugin marketplace add bitwize-music-studio/claude-ai-music-skills
/plugin install bitwize-music@bitwize-music
```

Then run `/bitwize-music:setup` to detect your environment and install dependencies, and `/bitwize-music:configure` to set your artist name and workspace paths.

OpenAI Codex can install the same plugin (experimental support):

```bash
codex plugin marketplace add bitwize-music-studio/claude-ai-music-skills
codex plugin add bitwize-music@bitwize-music
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| lyric-writer | 565 | Writes or reviews lyrics with prosody and rhyme craft |
| suno-engineer | 515 | Builds Suno style prompts, model selection and generation settings |
| mastering-engineer | 407 | Guides audio mastering for streaming platforms |
| mix-engineer | 403 | Polishes per-stem WAVs and remixes into a master-ready stereo file |
| plagiarism-checker | 391 | Scans lyrics for phrases that may match existing songs |
| lyric-reviewer | 360 | Reviews lyrics against a quality checklist before generation |
| album-art-director | 286 | Creates album artwork concepts and AI art prompts |
| pronunciation-specialist | 286 | Scans lyrics for pronunciation risks to avoid Suno mispronunciations |
| lyric-refiner | 274 | Multi-pass lyric refinement for cohesion and album unity |
| sheet-music-publisher | 270 | Converts mastered audio to sheet music and printable songbooks |
| researchers-historical | 266 | Researches archives and reconstructs timelines from primary sources |
| release-director | 265 | Coordinates album QA, distribution prep and platform uploads |
| pre-generation-check | 264 | Validates pre-generation gates before sending tracks to Suno |
| album-conceptualizer | 262 | Designs album concepts, tracklists and thematic planning |
| researchers-legal | 261 | Researches court documents, indictments and sentencing records |
| clipboard | 261 | Copies track lyrics and style prompts to the system clipboard |
| tutorial | 259 | Interactive guided album creation for new users |
| promo-writer | 259 | Generates platform-specific social media copy |
| promo-director | 259 | Generates short vertical promo videos from mastered audio |

The remaining 44 indexed listings range from 3 to 257 installs.

## Why This Matters for Hermes Agents

This suite demonstrates how far a skill collection can push a coding agent into a real creative production domain. The interesting pattern for builders is the tiered model routing: skills declare which model tier they need, so creative work that defines the music runs on the strongest model while mechanical imports and validation run on the cheapest, without a per-skill edit every time a new model ships.

The research system is the second transferable idea. For true-story and documentary albums it coordinates ten domain-specific sub-agents, then requires a verification agent to cross-check every claim against a captured source before lyrics generation is allowed. That source-verification handoff, with human sign-off as a hard gate, is a concrete template for any agent workflow where claims must trace to evidence.

The MCP server keeps skills calling tools instead of reading files directly, which keeps responses fast and state consistent. The quality-gate pattern, a 13-point lyrics checklist, pre-generation gates, and a 7-point audio QC, is worth borrowing for any pipeline where output ships to a public platform.

## Usage

| You say | What happens |
|---|---|
| "Let's make an album about the 2016 Bangladesh Bank heist" | The plugin creates album structure and runs 7-phase concept planning |
| "Start the research" | Legal, financial and security researchers gather and cross-verify sources in parallel |
| "Sources look good, let's write track 1" | Lyrics are drafted, prosody-checked and turned into a Suno style prompt |
| "Track sounds great, here are the stems" | Per-stem audio is polished and mastered to a streaming loudness target |
| "Pre-gen check" | All pre-generation gates are validated before anything is sent to Suno |
| "Master this album" | Approved tracks are mastered per platform with genre-specific presets |

## Verification

After installing, run `/bitwize-music:setup` in Claude Code and confirm the skill folders are present under `skills/` in the repository checkout (61 folders, one `SKILL.md` each). To review a skill before first use, fetch its definition directly:

```bash
curl -sL https://raw.githubusercontent.com/bitwize-music-studio/claude-ai-music-skills/main/skills/lyric-writer/SKILL.md
```

## Security

skills.sh verdicts for sampled skills (verified Nov 19, 2026) - re-check the security pages on skills.sh before production use:

One Fail sits in the sample: release-director fails Snyk. Three Warn cells sit in Snyk: plagiarism-checker, researchers-historical and researchers-legal. Every sampled skill passes the Gen Agent Trust Hub and Socket.

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| lyric-writer | Pass | Pass | Pass |
| suno-engineer | Pass | Pass | Pass |
| mastering-engineer | Pass | Pass | Pass |
| mix-engineer | Pass | Pass | Pass |
| plagiarism-checker | Pass | Pass | Warn |
| lyric-reviewer | Pass | Pass | Pass |
| album-art-director | Pass | Pass | Pass |
| pronunciation-specialist | Pass | Pass | Pass |
| lyric-refiner | Pass | Pass | Pass |
| sheet-music-publisher | Pass | Pass | Pass |
| researchers-historical | Pass | Pass | Warn |
| release-director | Pass | Pass | Fail |
| pre-generation-check | Pass | Pass | Pass |
| album-conceptualizer | Pass | Pass | Pass |
| researchers-legal | Pass | Pass | Warn |
| clipboard | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 19, 2026: 14,649 combined installs across 63 indexed listings; 681 GitHub stars; CC0-1.0 licence; last pushed Nov 20, 2026. Counts drift over time.
- The install index outruns the README: the skills.sh index carries 63 listings while the repository documents 61 skills, so a couple of listings have no direct counterpart in the skill tree.
- Suno's own MCP server is an invite-only beta, so the skills that depend on it (generate, listen, check-take, edit-take, extend-take, sound-effects, suno-voice, import-audio) may break without warning until Suno releases it officially.
- Several workflow skills depend on licensed or external tools: MuseScore PDF export, AnthemScore transcription (licensed install), and ffmpeg for the audio pipeline.
- The CC0-1.0 licence is public domain; the repository still asks users to respect applicable law and platform terms for generated content.

## Related

- [Songwriting & AI Music - Creative Music Generation Setup](/hermes/skills/catalog/songwriting-and-ai-music-setup)
- [Recoup Skills - Music Label Agent Suite Setup](/hermes/skills/catalog/recoupable-skills-setup)
- [Sonilo Skills - Music, SFX and Dubbing for Video](/hermes/skills/catalog/sonilo-skills-setup)
- [HeartMuLa - Open-Source AI Music Generation Setup](/hermes/skills/catalog/heartmula-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `/bitwize-music:configure` before anything else; artist name and workspace paths drive most downstream skills.
- Use the pre-generation-check skill as a final gate before any Suno generation so you never burn a generation on unreviewed lyrics.
- The 72 genre directories are the fastest way to ground a prompt: each has production guides, mastering presets and reference artists.
- If you are on Windows and want sheet music, AnthemScore transcription needs a licensed install because its free trial exposes no CLI.
- On a standard Pro subscription, multi-track sessions can hit rate limits; the Max tier is where multi-agent research and parallel generation run comfortably.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
