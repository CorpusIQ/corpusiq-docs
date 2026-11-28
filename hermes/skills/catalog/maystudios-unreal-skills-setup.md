---
title: "MayStudios Claude Skills - UE5, llama.cpp and OpenCode"
description: "maystudios/claude-skills: 2.0K combined installs. Production Claude Code skills for Unreal Engine 5, llama.cpp, and OpenCode CLI integration."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/maystudios-unreal-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-28"
tags: ["hermes skill", "agent skill", "skill setup", "unreal engine", "llama.cpp", "opencode"]
---

# MayStudios Claude Skills - Setup Guide

**Source:** [maystudios/claude-skills](https://www.skills.sh/maystudios/claude-skills) via skills.sh - 2.0K combined installs across 22 indexed listings; first seen Nov 28 2026 (morning sweep)

**GitHub:** [maystudios/claude-skills](https://github.com/maystudios/claude-skills) - 32 stars, MIT license, branch main, last pushed 2026-08-15; each skill is a top-level folder holding a SKILL.md plus optional scripts, references and assets.

**Category:** Claude Code skills - Unreal Engine 5, AI and LLM tooling, video and media processing, audio and music, and web development

**Quality Tier:** 🟠 Orange - Gen Agent Trust Hub fails opencode and gemini-image-gen, and Snyk fails hermes-tweet; Warn cells land on audio-to-midi, video-fetch-and-summarize, 2d-pixel-asset, video-download, auto-research, anthropic-skilljar-extractor and tech-product-landing.

maystudios/claude-skills is a curated collection of production-ready Claude Code skills for game development, AI tooling, media processing, audio/MIDI workflows and C++ programming, built from shipping an Unreal Engine 5.7 horror game. Each skill is a folder with a SKILL.md that Claude Code loads on demand, and many bundle scripts, reference docs and assets.

The 22 indexed listings range from unreal-best-practices at 175 installs down to gemini-web-media-analysis at 43. The skills cluster into Unreal Engine 5 development, AI and LLM integration, image and asset generation, video generation and media processing, audio and music, web development and research. The README also documents link-download, a yt-dlp video and audio downloader that appears in the repo tree but carries no skills.sh listing.

## Installation

The README installs skills with `npx skills add`, either all at once or one at a time:

```bash
# Install all skills at once
npx skills add maystudios/claude-skills

# Or pick individual skills
npx skills add maystudios/claude-skills/unreal-gas
npx skills add maystudios/claude-skills/opencode
npx skills add maystudios/claude-skills/gemini-image-gen
npx skills add maystudios/claude-skills/audio-to-midi
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| unreal-best-practices | 175 | Modern UE5.x best practices: choosing current systems over legacy ones, C++ vs Blueprint, data-driven design, naming, performance and Unreal Insights debugging. |
| unreal-gas | 155 | UE5.x Gameplay Ability System C++ development: abilities, effects, attributes, tags, cues, tasks, prediction and replication. |
| audio-to-midi | 151 | Transcribe MP3/WAV/FLAC to MIDI and MusicXML with music analysis, using Basic Pitch or a high-accuracy piano model with optional stem separation. |
| unreal-blueprint-codegen | 135 | Generate UE5.x Blueprint and Widget Blueprint .uasset files programmatically from C++, including event graphs and UMG animations. |
| unreal-pcg-python | 134 | UE5.x Procedural Content Generation Python integration via PCGPythonInterop: the Execute Python Script node, the PCG Python API and editor automation. |
| unreal-thirdparty | 123 | Integrate third-party C/C++ libraries into UE5.x: linking, Build.cs configuration, runtime staging and cross-platform pitfalls. |
| midi-synth | 90 | Render MIDI/MusicXML to WAV/MP3 and convert MIDI to Strudel live-coding patterns, with ghost-note cleaning and tempo and transpose control. |
| llama-cpp | 90 | llama.cpp C/C++ inference reference: the C API, GGUF format, quantization, GPU backends, HTTP server and UE5 integration. |
| video-fetch-and-summarize | 77 | Download videos from URLs and generate a Gemini Markdown summary per video, with custom prompt support. |
| video-summarizer | 76 | Analyze local MP4 files with the Gemini API and produce structured Markdown summaries in bulk. |
| opencode | 76 | Invoke the OpenCode CLI as a sub-agent to delegate coding tasks to GPT-5.x, Codex or local models for a second opinion. |
| 2d-pixel-asset | 76 | Generate 2D pixel art assets with Google Gemini via Chrome, with style consistency, background removal and exact-dimension rasterization. |
| video-download | 75 | Download videos from YouTube, Instagram, TikTok, Twitter/X and other platforms as MP4 via yt-dlp, with bot-detection recovery. |
| gemini-image-gen | 75 | Generate images with Google Gemini via Chrome: resolution control, reference images, style transfer, editing and inpainting. |
| auto-research | 74 | Improve any SKILL.md, CLAUDE.md, subagent or slash-command with web-researched rewrites plus autonomous binary eval loops. |
| anthropic-skilljar-extractor | 73 | Extract an Anthropic Academy (Skilljar) course into a structured Markdown folder, one file per lesson. |
| tech-product-landing | 72 | Build production-grade landing pages for software and CLI tools with Vite, React, TypeScript and Tailwind. |
| google-ai-studio-tts | 70 | Generate speech, podcasts and multi-speaker dialogue with Google AI Studio TTS driven through Chrome. |
| seedance | 57 | Prompt ByteDance's Seedance 2.0 video model: text and image to video, first and last frames, multi-shot generation and synchronized audio. |
| hermes-tweet | 53 | Use Hermes Tweet with Hermes Agent for X/Twitter endpoint discovery, reads, audience analysis and guarded publishing. |

The remaining 2 indexed listings range from 43 to 46 installs: meta-muse-video-analysis (46) analyzes local videos with Meta's Muse Spark 1.2 Contributor model, and gemini-web-media-analysis (43) attaches a local image or video to gemini.google.com through Chrome for analysis.

## Why This Matters for Hermes Agents

The Unreal Engine 5 skills form a coherent reference set for C++ game development: unreal-gas, unreal-best-practices, unreal-thirdparty, unreal-pcg-python and unreal-blueprint-codegen each pair a SKILL.md with a references folder that holds the deeper material, so a builder can copy the layered reference pattern for any domain. llama-cpp is a complete C/C++ inference reference that extends all the way to UE5 integration, which is useful for wiring local models into an agent that runs inside a game engine. The browser-driven skills (gemini-image-gen, 2d-pixel-asset, google-ai-studio-tts and gemini-web-media-analysis) show how to automate a live web app through Chrome instead of relying on an API. opencode demonstrates cross-model delegation by invoking a second CLI as a sub-agent for a second opinion, and auto-research shows a self-improvement workflow built on cited rewrites and binary eval loops with git bookkeeping. The security verdicts are a useful calibration: a mostly-Markdown repository can still carry Gen Agent Trust Hub and Snyk failures, so scan any suite before it enters a production profile.

## Usage

| You say | What happens |
|---|---|
| "Add gameplay abilities to my UE5 character" | Uses unreal-gas for Gameplay Ability System C++ patterns. |
| "Which UE system should I use for this feature?" | Uses unreal-best-practices to choose a modern system over a legacy one. |
| "Convert this MP3 to MIDI and render it back" | Uses audio-to-midi for transcription and midi-synth for audio rendering. |
| "Get a second opinion from Codex on this function" | Uses opencode to delegate the task to the OpenCode CLI. |
| "Download these videos and summarize them" | Uses video-fetch-and-summarize to save each video and write a Gemini summary. |
| "Generate a 32x32 pixel sprite for my game" | Uses 2d-pixel-asset to generate pixel art with Gemini in Chrome. |
| "Build a landing page for my CLI tool" | Uses tech-product-landing to scaffold a Vite and React site. |

## Verification

The README installs through `npx skills add`, so the cleanest pre-install check is to fetch a SKILL.md directly and read its frontmatter. The layout on branch main is `<name>/SKILL.md`:

```bash
curl -sL https://raw.githubusercontent.com/maystudios/claude-skills/main/unreal-best-practices/SKILL.md
```

After a checkout, confirm the skill folders at the repo root:

```bash
git clone --depth 1 https://github.com/maystudios/claude-skills.git /tmp/maystudios-skills
ls /tmp/maystudios-skills/
head -3 /tmp/maystudios-skills/unreal-best-practices/SKILL.md
```

The repo root holds one folder per skill: 22 indexed listings plus link-download, which the README documents but skills.sh does not index, alongside README.md and LICENSE.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| unreal-best-practices | Pass | Pass | Pass |
| unreal-gas | Pass | Pass | Pass |
| audio-to-midi | Pass | Pass | Warn |
| unreal-blueprint-codegen | Pass | Pass | Pass |
| unreal-pcg-python | Pass | Pass | Pass |
| unreal-thirdparty | Pass | Pass | Pass |
| midi-synth | Pass | Pass | Pass |
| llama-cpp | Pass | Pass | Pass |
| video-fetch-and-summarize | Pass | Pass | Warn |
| video-summarizer | Pass | Pass | Pass |
| opencode | Fail | Warn | Pass |
| 2d-pixel-asset | Warn | Pass | Warn |
| video-download | Pass | Warn | Pass |
| gemini-image-gen | Fail | Pass | Pass |
| auto-research | Pass | Pass | Warn |
| anthropic-skilljar-extractor | Pass | Pass | Warn |
| tech-product-landing | Pass | Pass | Warn |
| google-ai-studio-tts | Pass | Pass | Pass |
| seedance | Pass | Pass | Pass |
| hermes-tweet | Warn | Warn | Fail |

This guide is Orange because Gen Agent Trust Hub fails opencode and gemini-image-gen, and Snyk fails hermes-tweet. Warn cells land on audio-to-midi (Snyk), video-fetch-and-summarize (Snyk), opencode (Socket), 2d-pixel-asset (Gen Agent Trust Hub and Snyk), video-download (Socket), auto-research (Snyk), anthropic-skilljar-extractor (Snyk) and tech-product-landing (Snyk). Only 20 of the 22 indexed listings were sampled; meta-muse-video-analysis and gemini-web-media-analysis are not covered.

## Limitations

- Snapshot data, verified 2026-11-28: 1,996 combined installs across 22 indexed listings; 32 GitHub stars; MIT license; last pushed 2026-08-15. Counts drift over time.
- This is a young suite: no listing exceeds 175 installs, and the combined total is 1,996.
- link-download is documented in the README and present in the repo tree but carries no skills.sh listing, so the install index and the repo tree do not line up exactly.
- The security verdicts cover 20 of the 22 indexed listings; meta-muse-video-analysis and gemini-web-media-analysis were not sampled.
- The README describes the skills as built from shipping an Unreal Engine 5.7 horror game, so the UE5 skills reflect that project's conventions and may lag newer UE5.x APIs.
- The browser-driven skills (gemini-image-gen, 2d-pixel-asset, google-ai-studio-tts and gemini-web-media-analysis) depend on Chrome automation and live web apps that can change without notice.

## Related

- [Unreal Engine Skills - Game Dev Suite for Agents](/hermes/skills/catalog/unreal-engine-skills-setup)
- [OpenCode Skills - Interface Design and Review Suite Setup](/hermes/skills/catalog/opencode-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install individual skills with `npx skills add maystudios/claude-skills/<name>` to pull only what you need, since the suite spans game development, media, audio and web.
- Read a SKILL.md before installing: the frontmatter and body define what Claude loads on demand.
- Treat the UE5 skills as a layered set: the SKILL.md is the trigger, and the references folders carry the deeper guidance.
- Confirm your Chrome automation setup before using the browser-driven skills, since they drive live web apps through the claude-in-chrome MCP server.
- Re-check the skills.sh security pages before pulling opencode, gemini-image-gen or hermes-tweet into a production profile.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
