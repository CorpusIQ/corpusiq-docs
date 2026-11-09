---
title: "OpenMontage Video Production Skills - Setup Guide"
description: "openmontageinc/openmontage on skills.sh: 28.9K combined installs; 20 indexed video production skills for scripting, TTS, editing and rendering."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/openmontage-video-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-09"
tags: ["hermes skill", "agent skill", "skill setup", "video production", "remotion", "ffmpeg", "text to speech"]
---

# OpenMontage - Setup Guide

**Source:** [openmontageinc/openmontage](https://www.skills.sh/openmontageinc/openmontage) via skills.sh - 28.9K combined installs across 20 indexed listings; first seen 2026-11-09 (Nov 9, 2026 sweep)
**GitHub:** 78,868 stars, AGPL-3.0 via LICENSE, `main` branch, last pushed 2026-11-09, 141 SKILL.md files in the tree (92 under `.agents/skills`, 49 under `.claude/skills`), README.md at the repository root
**Category:** Video production: agentic pipelines for research, scripting, asset generation, editing and rendering
**Quality Tier:** 🟡 Solid with caveats - no Fail verdicts and a large install base, but four Warns across the twenty sampled skills, AGPL-3.0 copyleft on the repository, and a media toolchain that has to be installed before anything renders.

OpenMontage is an agentic video production system rather than a single video tool. The repository description claims 12 production pipelines, 100+ tools and 700+ agent skill and production-knowledge files. The tree carries 141 SKILL.md files: 92 under `.agents/skills` and a parallel copy of 49 under `.claude/skills`. The `skills/` directory holds 158 markdown files but no SKILL.md of its own, and there is no root-level SKILL.md either, so there is no single entry point for the skills CLI to install here. The assistant instruction files at the root (`CLAUDE.md`, `CURSOR.md`, `CODEX.md`, `COPILOT.md`, `.windsurfrules`) all point at `AGENT_GUIDE.md` and `PROJECT_CONTEXT.md`, and those two files carry the operating contract.

The twenty listings skills.sh indexes are the external technology packs from layer 3 of the repository's own model. The README describes three layers: `tools/` plus `pipeline_defs/` as what exists, `skills/` as how OpenMontage wants a capability used (pipeline directors, creative techniques, core tool skills and meta review skills), and `.agents/skills/` as how the underlying technology works. The indexed listings lean on ffmpeg, Remotion, ElevenLabs, HeyGen and Seedance. The tree also carries HyperFrames, GSAP, ComfyUI and other packs that skills.sh does not index, so the twenty rows are the smallest slice of layer 3 by count and the one with the most portable value outside OpenMontage itself.

## Installation

The documented route is a clone plus one make target. Prerequisites from the README are Python 3.10 or newer, FFmpeg, Node.js on a patched 22.x (22.23.4 or newer), 24.x (24.22.1 or newer) or 26.x (26.12.1 or newer) release, and an AI coding assistant that can read files and run Python.

```bash
git clone https://github.com/calesthio/OpenMontage.git
cd OpenMontage
make setup
```

The clone URL in the README still names the old `calesthio` organization. GitHub answers with a 301 redirect to `OpenMontageInc/OpenMontage`, which is the same repository skills.sh indexes as `openmontageinc/openmontage`, so the command works and the checkout directory is named `OpenMontage` either way.

Where `make` is not available, the README gives a single line that does the same work:

```bash
python3 -m venv .venv && source .venv/bin/activate && python -m pip install 'pip>=26.2.2' && python -m pip install -r requirements.txt && cd remotion-composer && npm install && cd .. && python -m pip install piper-tts && cp .env.example .env
```

A single skill can be installed without the clone:

```bash
npx skills add https://github.com/openmontageinc/openmontage --skill svg-character-animation
```

The documented command names one skill explicitly, so substitute the skill you want from the table below. Be clear about what that buys: the skill text describes how to use a tool, while the tool itself lives in `tools/`, the orchestration lives in `pipeline_defs/`, and the state and checkpoint code lives in `lib/`. A standalone skill install teaches an agent the conventions and leaves it without the production machinery, which is why the clone route is the one that ends in a rendered file.

To take the whole instruction layer without the application, copy the skill folders into a Hermes profile. The tree carries 92 of them under `.agents/skills/`, and this loop skips any folder that already exists:

```bash
git clone --depth 1 https://github.com/openmontageinc/openmontage.git /tmp/openmontage
mkdir -p ~/.hermes/profiles/corpusiq/skills
for skill in /tmp/openmontage/.agents/skills/*; do
  [ -f "$skill/SKILL.md" ] || continue
  destination="$HOME/.hermes/profiles/corpusiq/skills/$(basename "$skill")"
  [ -e "$destination" ] || cp -R "$skill" "$destination"
done
```

That route carries the instructions and not the engine: `tools/`, `pipeline_defs/`, `lib/` and `schemas/` stay in the clone, so a skill copied this way tells an agent how the step should be done without giving it the code that does it.

API keys are optional and go in `.env`. The README states that every key is optional and that `make setup` produces a working zero-key path: Piper for offline narration, Archive.org, NASA and Wikimedia Commons for open footage, Pexels, Unsplash and Pixabay for free stock, Remotion and HyperFrames for composition, and FFmpeg for post-production. Keys such as `FAL_KEY`, `ELEVENLABS_API_KEY`, `HEYGEN_API_KEY`, `RUNWAY_API_KEY` and `PEXELS_API_KEY` widen the provider pool rather than unlocking the system.

## What It Provides

The threshold for this guide is zero installs, so all 20 indexed listings appear below with the install integers exactly as skills.sh reports them:

| Skill | Installs | Use For |
|---|---|---|
| svg-character-animation | 1,800 | Animating SVG character rigs with GSAP, CSS transforms, Remotion frame control and HyperFrames-compatible browser previews |
| video-edit | 1,795 | Local ffmpeg editing: trim, concat, resize, speed, overlay, audio extraction, compression and format conversion |
| video-understand | 1,680 | Reading a video locally through ffmpeg frame extraction and Whisper transcription, with no API keys |
| ai-video-gen | 1,495 | Text-to-video and image-to-video across provider gateways: VEO, Kling, Sora, Runway, Seedance, MiniMax and Gemini Omni, through HeyGen, fal.ai, the Kling direct API or the Gemini API |
| character-animation-qa | 1,486 | Reviewing character animation with schema checks, Playwright browser previews, frame sampling and FFmpeg/ffprobe output checks |
| video-download | 1,485 | Downloading video, audio, subtitles and metadata from YouTube and 1000+ sites with yt-dlp, with no API keys |
| ffmpeg | 1,458 | Format conversion, resizing, compression, audio extraction and asset preparation for Remotion and HyperFrames |
| remotion | 1,453 | Toolkit-specific Remotion patterns: custom transitions, shared components and project conventions, with core framework knowledge left to the separate remotion-official skill |
| text-to-speech | 1,433 | HeyGen native Voice1 and catalog speech, voice discovery, timestamps and streaming |
| pose-library-design | 1,416 | Designing reusable 2D character pose libraries, action cycles and expression states for data-driven animation |
| visual-style | 1,396 | Creating, extracting and applying portable visual-style.md design systems, including extraction from a website URL, video or PDF brand guide |
| seedance-2-0 | 1,374 | Cinematic clips with ByteDance Seedance 2.0: synchronized audio in one pass, multi-shot cuts, director-level camera control, lip-sync from quoted dialogue and reference-conditioned generation |
| create-video | 1,374 | One-shot prompt-to-video through HeyGen Video Agent when the prompt does not name avatars, voices or scenes |
| sound-effects | 1,349 | Sound effects from text through ElevenLabs, with looping, duration control and prompt influence tuning |
| speech-to-text | 1,346 | Transcribing audio and video to text with ElevenLabs Scribe v2, including subtitles and meeting transcripts |
| playwright-recording | 1,331 | Recording browser interactions as video with Playwright for demos, app walkthroughs and Remotion footage |
| lottie-bodymovin | 1,329 | Applying Disney's 12 animation principles to Lottie animations exported from After Effects |
| elevenlabs | 1,329 | Voiceovers, sound effects, music, soundtracks, voice cloning and other audio synthesis through the ElevenLabs APIs |
| framer-motion | 1,328 | Applying Disney's 12 animation principles with Framer Motion in React applications |
| video-toolkit | 1,275 | Building a video autonomously with claude-code-video-toolkit: voiceovers, image generation, music, talking heads and Remotion rendering |

The install spread is flat. svg-character-animation sits at 1,800 and video-toolkit at 1,275, and those two have nothing in common in scope, so the ordering carries no quality signal. Pick by the job in front of you.

What the table hides is the production layer above the skills. The README names eleven pipelines in its own table, from animated explainer and talking head to documentary montage and localization, and every one of them runs the same stage sequence: research to proposal to script to scene plan to assets to edit to compose. Each stage has a director skill under `skills/pipelines/` that tells the agent how to execute it, self-review it and checkpoint state.

Three behaviours are enforced rather than suggested. Human approval gates pause at proposal, script, scene plan, generated assets and publish, and the checkpoint writer rejects a gated stage marked complete without a recorded approval. Provider selection scores every option across seven weighted dimensions and logs the winner with the alternatives considered. Budget control estimates, reserves and reconciles spend, with a per-action approval threshold that defaults to $0.50 and a total cap that defaults to $10.

The zero-key path is the part most people misread as a demo. Narration comes from Piper TTS, footage from Archive.org, NASA and Wikimedia Commons, stock from Pexels, Unsplash and Pixabay, and composition from Remotion or HyperFrames, so a real edited video is possible with no paid provider. The documentary montage pipeline is built specifically for that case: it builds a CLIP-indexed corpus from free and open archives and edits real motion clips rather than animating stills.

## Why This Matters for Hermes Agents

Most of what Hermes does with media is assembly: take a brief, gather source material, produce narration, cut it to a timeline and encode it. OpenMontage is that job written down as instructions plus Python tools, and the instruction layer is the part worth reading even if you never run the pipeline.

The reason is that the failure mode of an agent making video is not a bad frame, it is a plan that cannot produce motion. OpenMontage encodes that as a slideshow risk score across six dimensions, a pre-compose check that blocks a render when the delivery promise is violated, and a post-render self-review that runs ffprobe, samples four frames, checks audio levels for silence and clipping and verifies subtitle presence. An agent that adopts only those four checks produces visibly better output than one that renders and ships.

The second transferable piece is the scored provider selection. Seven weighted dimensions with task fit at 30 percent, output quality at 20, control features at 15, reliability at 15, cost efficiency at 10, latency at 5 and continuity at 5, plus a decision log carrying the alternatives. That is a reusable shape for any decision where several APIs can do the same job and the agent has to justify the pick.

The third is cost control expressed as tooling rather than advice. Estimate, reserve, reconcile, a per-action approval threshold and a hard cap are five small mechanisms that turn an agent that might spend $80 on generation calls into one that stops at $10 unless a human raises the limit.

The honest counterweight is that this is a full application, not a skill pack. Installing a listing gives the agent a technology reference; the pipelines, checkpoints, schemas and Backlot board only exist in the clone, and the clone wants FFmpeg, Node on a specific patched release and Python 3.10 or newer on the machine doing the work.

## Usage

| You say | What happens |
|---|---|
| "Make a 60-second animated explainer about how neural networks learn" | Selects the animated explainer pipeline, runs the research stage across web sources, drafts a script and scene plan, generates images, narrates with a configured or local TTS engine, burns in word-level subtitles and renders through Remotion |
| "Here is a YouTube Short I love. Make me something like this, but about quantum computing" | Analyses the reference for transcript, pacing, scenes, keyframes and style, then returns two or three differentiated concepts with what it keeps, what it changes and what the target duration will cost before any asset is generated |
| "Make a 75-second documentary montage about city life in the rain, real footage only, no narration" | Uses the documentary montage pipeline to build a CLIP-indexed corpus from Pexels, Archive.org, NASA, Wikimedia and Unsplash, ranks clips semantically and edits a timeline of real motion footage |
| "Cut this two-hour podcast into a dozen social clips" | Runs clip factory over the source, ranks the candidate segments and renders short-form cuts in the platform profile you pick, from 1080x1920 vertical up to 21:9 cinematic |
| "What will this cost before you spend anything?" | Returns the estimate from the budget layer, reserves it, and pauses for approval above the per-action threshold, which defaults to $0.50 against a total cap of $10 |
| "Dub this video into Spanish and keep the timing" | Runs the localization and dub pipeline: speech-to-text with word timestamps, translation, voice generation and re-timed audio mixed back onto the original picture |
| "Show me what the production is actually doing" | Opens the Backlot board with `python -m backlot open <project-id>`, which fills in stage by stage and can replay a finished run from its timestamps |

## Verification

The skill layout is `.agents/skills/<name>/SKILL.md`, so every raw path carries that segment. This one returns 200 and is the file the table lists first:

```bash
curl -fsSL https://raw.githubusercontent.com/openmontageinc/openmontage/main/.agents/skills/svg-character-animation/SKILL.md | head -6
```

It opens with YAML frontmatter holding `name: svg-character-animation`, a one-line description and `license: MIT`, then the heading `# SVG Character Animation`. The `license` key is worth noticing: it is on the skill file, not on the repository, and the repository ships AGPL-3.0.

A second skill confirms the tree is intact. The ffmpeg skill runs to 432 lines:

```bash
curl -fsSL https://raw.githubusercontent.com/openmontageinc/openmontage/main/.agents/skills/ffmpeg/SKILL.md | head -10
```

That should return frontmatter with `name: ffmpeg`, no `license` key, and the heading `# FFmpeg for Video Production`. A 404 here means the `.agents/skills/` layout moved and every path in this guide needs a new segment.

The count check is the cheapest way to see how much of the tree skills.sh is not indexing:

```bash
curl -fsSL "https://api.github.com/repos/openmontageinc/openmontage/git/trees/main?recursive=1" | grep -c '"path": ".*SKILL.md"'
```

That returns 141, against 20 indexed listings.

After a clone, confirm the runtime actually registered its tools, which is the README's own capability check:

```bash
python -c "from tools.tool_registry import registry; import json; registry.discover(); print(json.dumps(registry.support_envelope(), indent=2))"
```

It prints the tool support envelope as JSON. An empty or minimal envelope means the environment is missing a dependency rather than the install being wrong.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-09) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| svg-character-animation | Pass | Pass | Pass |
| video-edit | Warn | Pass | Pass |
| video-understand | Pass | Pass | Pass |
| ai-video-gen | Pass | Pass | Pass |
| character-animation-qa | Pass | Pass | Pass |
| video-download | Pass | Pass | Warn |
| ffmpeg | Pass | Pass | Pass |
| remotion | Pass | Pass | Pass |
| text-to-speech | Pass | Pass | Pass |
| pose-library-design | Pass | Pass | Pass |
| visual-style | Pass | Pass | Warn |
| seedance-2-0 | Pass | Pass | Pass |
| create-video | Pass | Pass | Pass |
| sound-effects | Pass | Pass | Pass |
| speech-to-text | Pass | Pass | Warn |
| playwright-recording | Pass | Pass | Pass |
| lottie-bodymovin | Pass | Pass | Pass |
| elevenlabs | Pass | Pass | Pass |
| framer-motion | Pass | Pass | Pass |
| video-toolkit | Pass | Pass | Pass |

No Fail verdict appears, and the four Warns land on the skills whose job is to touch the network or the filesystem: video-edit shells out to ffmpeg, video-download drives yt-dlp against arbitrary URLs, visual-style fetches a website, video or PDF to extract a style, and speech-to-text uploads audio to a hosted API. Those are expected surfaces for what these skills do, and the verdicts are a reason to read the skill body before install rather than a reason to skip it.

The licence is the bigger operational question. AGPL-3.0 is a copyleft licence with a network clause. Running OpenMontage locally to make videos for yourself triggers nothing beyond the usual obligations of keeping the licence and the source notices with any copy you distribute. But if you modify it and let other people use the modified version over a network, you have to offer those users the corresponding source, including your changes. Embedding a modified copy inside a product, or putting it behind a hosted endpoint that other people call, reaches the same clause. The practical pattern for a commercial product is to run OpenMontage as a separate process you invoke over an API boundary rather than copying its code into your own tree, and to get legal advice before shipping anything that links to it. This is a plain reading of the licence, not legal advice.

One inconsistency belongs in the open: `svg-character-animation` declares `license: MIT` in its own frontmatter while the repository root ships AGPL-3.0. Treat the repository licence as governing unless the publisher states otherwise in writing. Do not take a per-skill `license` key as a grant.

The credential surface is broad by design. A configured `.env` can hold keys for fal.ai, HeyGen, ElevenLabs, Kling, Runway, Atlas Cloud, Suno, Pexels, Pixabay, Unsplash, OpenAI, Google and xAI, each with its own spend authority. Keep `.env` out of version control (the repository ships `.env.example`), issue keys with the smallest scope each provider offers, and leave the budget cap in `cap` mode rather than `observe` once anyone other than you can trigger a run.

The last surface is the media toolchain itself. The pipeline shells out to ffmpeg and ffprobe, runs a Node renderer inside `remotion-composer/`, and drives Playwright for browser recording and character animation previews. Those are three separate executable dependencies in the trust path, and a pinned Node release is part of the install instructions for a reason.

## Limitations

- Snapshot data, verified 2026-11-09: 28,932 combined installs across 20 indexed listings; 78,868 GitHub stars; AGPL-3.0; last pushed 2026-11-09. Counts drift over time.
- The twenty listings are a page cap, not the whole library. skills.sh shows at most 20 listings on a source page and the tree carries 141 SKILL.md files, 92 of them under `.agents/skills`, so the install index covers a small minority of the skill text and the rest has no install count published at all. Assume the 20 rows understate the suite rather than describing it.
- AGPL-3.0 is a copyleft network licence. Anything that modifies OpenMontage and serves it to other people over a network carries a source-offer obligation, and that constraint is inherited by whatever product it is embedded in.
- This is an application install, not a skill install. The README expects Python 3.10 or newer, FFmpeg on the PATH, Node on a patched 22.23.4, 24.22.1 or 26.12.1 release, and `make`. A standalone `npx skills add` install gives you the instructions without the `tools/`, `pipeline_defs/`, `lib/` or `schemas/` half of the system.
- The README clone command still names the `calesthio` organization and relies on a GitHub redirect to `OpenMontageInc/OpenMontage`. If the redirect is ever dropped, the documented `git clone` line stops working while the skills.sh source path keeps working.
- Install counts cluster between 1,275 and 1,800 with no functional grouping behind them, so the ordering cannot be used to judge which skill matters. The pipeline documentation also disagrees with itself on scale: eleven named pipelines in the README table, twelve in the repository description, thirteen files under `pipeline_defs/`.

## Related

- [remotion-best-practices - Video Production Setup](/hermes/skills/catalog/remotion-best-practices-setup)
- [Higgsfield Skills - AI Video & Image Generation Cluster Setup](/hermes/skills/catalog/higgsfield-skills-setup)
- [Tesseract Video Skills - Agent Creative Suite Setup](/hermes/skills/catalog/tesseract-video-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Read `AGENT_GUIDE.md` before any skill. The repository is explicit that real work goes through `pipeline_defs/`, the stage director skills in `skills/pipelines/` and the tool registry, and an agent that improvises a workflow fights the checkpoints.
- Treat the pipeline as a selection problem. Pick the pipeline first, read its YAML manifest, then the stage skill, then the tools. Starting from a tool is how an agent ends up encoding a video that was never planned.
- Leave the approval gates on. They pause at proposal, script, scene plan, assets and publish, and the cost of a wrong scene plan discovered after generation is the whole asset budget.
- Run the slideshow risk check on anything described as motion-led. A render that is 80 percent stills fails the delivery promise and gets blocked before it burns GPU time, which is cheaper than a re-render.
- Keep the budget in `cap` mode with the default $0.50 per-action threshold on a first project, then raise it once the estimate and reconcile numbers match what you actually spend.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
