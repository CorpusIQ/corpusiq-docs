---
title: "Auto-Editor Skills - Video & Audio Editing Setup"
description: "wyattblue/auto-editor: 5 skills for silence- and motion-based video and audio editing with the auto-editor CLI - 6.0K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/auto-editor-setup/"
robots: "index,follow"
last_updated: "2026-11-21"
tags: ["hermes skill", "agent skill", "skill setup", "video editing", "audio editing", "transcription"]
---

# Auto-Editor Skills - Video & Audio Editing Setup

**Source:** [wyattblue/auto-editor](https://www.skills.sh/wyattblue/auto-editor) via skills.sh - 6.0K combined installs across 5 indexed listings; first seen Nov 21, 2026 (Nov 21, 2026 morning sweep)
**GitHub:** [WyattBlue/auto-editor](https://github.com/WyattBlue/auto-editor) - 6,038 stars, Unlicense license, master branch, last pushed Nov 21, 2026; the Nim editor source lives under `src/` with five agent skills at `skills/<name>/SKILL.md`.
**Category:** Video and Audio Editing
**Quality Tier:** 🟡 Yellow - 5 of 5 sampled skills pass Gen Agent Trust Hub and Socket; 1 Snyk Warn, 0 Fails.

Auto-Editor is a command line application that automatically edits video and audio by analysing loudness, motion and black frames, published by WyattBlue. The repository ships the editor itself plus a five-skill package where each skill documents one part of the auto-editor CLI: the base cut-and-pace workflow, exports to professional editors, transcription-driven editing, per-section effects and animations, and transitions.

The split matters because the CLI is the real dependency. The skills carry no executable code; they teach an agent the flags, thresholds and export targets so it can drive the installed binary correctly. First seen in the Nov 21, 2026 morning sweep.

## Installation

Install the auto-editor CLI first. It ships as an official binary and via Homebrew, and it is no longer published on pip:

```bash
brew install auto-editor
```

or download the platform binary from the GitHub Releases page. Then install the skills:

```bash
npx skills add WyattBlue/auto-editor
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| auto-editor | 1,595 | record a microphone or cut dead space (silence, motionlessness, black frames), set the pace, and render |
| auto-editor-export | 1,357 | export edits and microphone recordings to Premiere, DaVinci Resolve, Final Cut Pro, ShotCut or Kdenlive |
| auto-editor-transcribe | 1,347 | transcribe media or a live microphone to text or subtitles, then cut by spoken content |
| auto-editor-effects | 1,242 | apply per-section speed, volume, zoom, boxes, logos and picture-in-picture with ramps and easing |
| auto-editor-transitions | 462 | add cross-dissolves, Premiere Pro transitions and audio crossfades at cuts |

All 5 indexed listings clear the 400-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

Video and audio cleanup is exactly the work that is tedious to do by hand and easy to get subtly wrong in an editor: an hour of footage with dead air, a podcast with long pauses, a screen recording with black frames. Auto-Editor turns that first pass into a deterministic command, and the skills give an agent the exact flags to express what to cut and what to keep. Because the cut is computed from loudness, motion or subtitles rather than by eyeball, the result is repeatable across takes and clients.

The transcription skill is the operationally interesting one: an agent can cut a video to its spoken content by matching words or regexes, so a recording can be trimmed to only the sections that mention a topic. The export skill routes the same edit into Premiere, DaVinci Resolve, Final Cut Pro, ShotCut or Kdenlive, which means an agent can hand a human editor a project file instead of a flattened video. Everything runs through the local binary and ffmpeg, so no media leaves the machine.

## Usage

| You say | What happens |
|---|---|
| Remove the dead air from this recording | Cuts silent, motionless or black sections and renders a tightened video |
| Keep only the parts where someone is talking | Transcribes and cuts to spoken content, dropping the rest |
| Hand me a Premiere project for this edit | Exports the timeline as an editor-ready XML instead of a flattened video |
| Add cross-dissolves at every cut and fade the ends | Applies transitions at the cuts and carries them into an editor export |
| Slow the loud parts and zoom in on the second section | Applies per-section speed and Ken Burns effects from the CLI |
| Turn this podcast into subtitle files | Runs the whisper subcommand and emits text or subtitle files |

## Verification

Confirm the CLI is installed, then review the base skill before installing, since it documents the flags the other skills build on:

```bash
auto-editor --help
```

```bash
curl -sL https://raw.githubusercontent.com/WyattBlue/auto-editor/master/skills/auto-editor/SKILL.md | head -40
```

Run a first pass on a short known file before touching client media.

## Security

skills.sh verdicts for sampled skills (verified Nov 21, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| auto-editor | Pass | Pass | Pass |
| auto-editor-export | Pass | Pass | Pass |
| auto-editor-transcribe | Pass | Pass | Warn |
| auto-editor-effects | Pass | Pass | Pass |
| auto-editor-transitions | Pass | Pass | Pass |

The skills carry no executable code; the work happens in the local auto-editor binary, which shells out to ffmpeg on local media. Scope the input and output directories before running a write command.

## Limitations

- Snapshot data, verified Nov 21, 2026: 6,003 combined installs across 5 indexed listings; 6,038 GitHub stars; Unlicense license; last pushed Nov 21, 2026. Counts drift over time.
- The skills document the auto-editor CLI and are not standalone tools; you must install the binary separately, and it is no longer published on pip.
- Transcription depends on the whisper subcommand and its model files, which are fetched at task time rather than bundled with the skill.
- Export fidelity is editor-specific: what survives into Premiere versus DaVinci Resolve, Final Cut Pro, ShotCut or Kdenlive depends on each editor's XML/EDL import support.
- The README install command spells the owner "WyattBlue" while skills.sh indexes it as "wyattblue"; both resolve to the same repository.
- No index-versus-tree drift: all 5 indexed listings have a matching `skills/<name>/SKILL.md` directory.

## Related

- [Claude Code Video Toolkit - Video Pipeline Skills Setup](/hermes/skills/catalog/claude-code-video-toolkit-setup)
- [Video Agent Skills - Video Production for Agents](/hermes/skills/catalog/video-agent-skills-setup)
- [Pexo Video Skills - AI Video Generation Suite Setup](/hermes/skills/catalog/pexo-video-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the CLI first and confirm `auto-editor --help` returns before adding the skills, so the agent has a working binary to drive.
- Start with the base auto-editor skill on a short known file; it is the cut-and-pace engine the other four skills build on.
- Use `--margin` to keep a little breathing room around kept sections so cuts do not feel abrupt.
- Prefer the export skills when a human editor will finish the job; hand them a project file rather than a flattened video.
- Pin a known-good auto-editor version, since flag and default behaviour changes between releases.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
