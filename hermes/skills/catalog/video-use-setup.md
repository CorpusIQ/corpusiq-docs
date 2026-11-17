---
title: "Video Use - Edit Videos With Coding Agents"
description: "browser-use/video-use: 6.2K combined installs across 2 listings; skills for editing raw footage and rendering Manim animations with coding agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/video-use-setup/"
robots: "index,follow"
last_updated: "2026-11-17"
tags: ["hermes skill", "agent skill", "skill setup", "video editing", "manim", "animation"]
---

# Video Use - Setup Guide

**Source:** [browser-use/video-use](https://www.skills.sh/browser-use/video-use) via skills.sh - 6.2K combined installs across 2 indexed listings; first seen Nov 17, 2026 (this sweep)
**GitHub:** 31,176 stars, MIT license, `main` branch, last pushed 2026-10-08, two skills: a root `SKILL.md` for video editing plus `skills/manim-video/` for Manim animation
**Category:** Video editing / agent media production
**Quality Tier:** 🟢 Green - all sampled skills pass Gen Agent Trust Hub, Socket, and Snyk.

video-use edits raw footage through conversation: drop footage in a folder, chat with the agent, and get `final.mp4` back, with no presets or menus. The agent never watches the video frame by frame. Instead it reads two layers: an audio transcript with word-level timestamps, speaker diarization, and audio events, plus on-demand visual composites produced only at decision points. A second skill, manim-video, produces 3Blue1Brown-style mathematical and technical animations with Manim Community Edition.

The suite covers talking heads, montages, tutorials, travel, and interviews. Editing runs through a pipeline of transcribe, pack, reason, edit, render, and self-evaluate, so the rendered output is checked at every cut boundary before anything is shown.

## Installation

The README's setup prompt hands the whole install to an agent with shell access:

```text
Set up https://github.com/browser-use/video-use for me.
```

The agent reads `install.md`, installs dependencies and ffmpeg, registers the skill, and prompts once for an ElevenLabs API key. Manual install is also documented:

```bash
git clone https://github.com/browser-use/video-use ~/Developer/video-use
ln -sfn ~/Developer/video-use ~/.claude/skills/video-use
cd ~/Developer/video-use
uv sync
brew install ffmpeg
cp .env.example .env
```

Then point the agent at a folder of raw takes and ask it to edit them into a video.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| video-use | 6,019 | Edit raw footage by chatting: cut filler, color grade, subtitles, animation overlays, and self-evaluated renders. |
| manim-video | 220 | Create 3Blue1Brown-style math and technical animations with Manim Community Edition. |

No indexed listings fall below the threshold; both listings appear above.

## Why This Matters for Hermes Agents

The video-use skill gives an agent word-boundary cutting precision without ever watching the video. The transcript is the surface: one ElevenLabs Scribe call per source packs into a roughly 12KB file with timestamps, diarization, and audio events, and a visual composite is rendered only at decision points such as ambiguous pauses or cut-point checks.

That is the browser-use pattern applied to video: give the LLM a structured representation instead of a stream of frames. The README contrasts a naive approach of 30,000 frames against the packed transcript plus a handful of images, so an agent reasons about edits on text and small visuals rather than millions of tokens of noise.

For Hermes agents the workflow is a full editing loop: ask, confirm, execute, self-evaluate, and persist session memory in `project.md` so a later session picks up where the last one left off. manim-video extends the suite to programmatic animation for explainers, equation derivations, and algorithm walkthroughs.

## Usage

| You say | What happens |
|---|---|
| "Set up https://github.com/browser-use/video-use for me" | Reads install.md, installs deps and ffmpeg, registers the skill, and prompts for the ElevenLabs API key. |
| "Edit these into a launch video" | Inventories the sources, proposes a strategy, waits for approval, then renders `edit/final.mp4`. |
| "Cut the filler words and dead air" | Trims umms, false starts, and silence gaps, adding 30ms audio fades at each cut. |
| "Make a 3Blue1Brown-style explainer" | Runs manim-video to script and render a Manim animation. |
| "Burn subtitles in 2-word uppercase chunks" | Renders burned-in captions in the configured subtitle style. |

## Verification

Probe both skills on the `main` branch before installing. Both return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/browser-use/video-use/main/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/browser-use/video-use/main/skills/manim-video/SKILL.md
```

The main skill lives at the repository root as `SKILL.md`, manim-video lives at `skills/manim-video/SKILL.md`, and the editing helpers live in `helpers/`.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-17) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| video-use | Pass | Pass | Pass |
| manim-video | Pass | Pass | Pass |

The sample covers both indexed listings, so this is a full census; both skills pass all three auditors.

## Limitations

- Snapshot data, verified 2026-11-17: 6,239 combined installs across 2 indexed listings; 31,176 GitHub stars; MIT; last pushed 2026-10-08. Counts drift over time.
- Transcription requires an ElevenLabs API key; the agent prompts for it at setup, and transcriptions are not free.
- manim-video trails the main skill at 220 installs, so it is the less-proven half of the suite.
- The pipeline shells out to ffmpeg (required) and optionally yt-dlp for online sources; both must be present on the host.
- The cloud-hosted version is waitlist-only at the time of writing, so this guide covers the open-source local workflow.

## Related

- [Video Agent Skills - Video Production for Agents](/hermes/skills/catalog/video-agent-skills-setup)
- [Claude Code Video Toolkit - Video Pipeline Skills Setup](/hermes/skills/catalog/claude-code-video-toolkit-setup)
- [Remotion Framework Skills - Programmatic Video Setup](/hermes/skills/catalog/remotion-framework-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Drop raw takes into a dedicated folder and let the agent propose a strategy before it touches a cut; the workflow never edits without approval.
- Read the packed transcript (`takes_packed.md`) rather than the raw files; it is the agent's primary reading view.
- The self-eval loop re-renders up to three times on issues, so a slow render is normal rather than a failure.
- Keep outputs in `<videos_dir>/edit/` so the skill directory stays clean across sessions.
- For math or technical content, reach for manim-video instead of the footage pipeline.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
