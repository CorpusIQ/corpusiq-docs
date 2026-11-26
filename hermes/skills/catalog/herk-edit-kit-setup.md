---
title: "Herk Edit Kit - AI Video Editing Setup"
description: "nateherkai/herk-edit-kit - 4.0K combined installs: 15 video-editing skills for transcript-driven cuts, storytelling, and HyperFrames motion graphics."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/herk-edit-kit-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "video editing", "hyperframes", "motion graphics"]
---

# Herk Edit Kit - Setup Guide

**Source:** [nateherkai/herk-edit-kit](https://www.skills.sh/nateherkai/herk-edit-kit) via skills.sh - 4.0K combined installs across 14 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 morning sweep)
**GitHub:** [nateherkai/herk-edit-kit](https://github.com/nateherkai/herk-edit-kit) - 3,176 stars, NOASSERTION license, last pushed Oct 14, 2026, main branch; 15 skills mirrored into .agents/skills/ and .claude/skills/.
**Category:** Video Editing (HyperFrames)
**Quality Tier:** 🟡 Yellow - 5 of 14 listings sampled: four pass all three checks, and make-a-video carries a Snyk Warn.

Nate Herk's video-editing kit for Codex and Claude Code, built on HyperFrames and formerly known as the HyperFrames Student Kit. It brings your own footage and turns a transcript into a finished cut: cut-silences and cut-mistakes strip dead air and spoken mistakes review-gated, video-storytelling designs the visual layer as one persistent world, short-form-edit turns a talking-head recording into a reel or Short, and make-a-video interviews a beginner and builds a finished MP4. Around that core sit the 406-card motion-graphics style library, the HyperFrames and GSAP skills, and the website-to-hyperframes converter.

The 15 skills are mirrored into both .agents/skills/ and .claude/skills/, so the tree holds two copies of each. Fourteen of them are indexed on skills.sh; the 15th (motion-showreel) ships in the repo but carries no indexed listing, so it does not appear in the install table below.

## Installation

The README's install path clones the repo and runs the setup script. Prerequisites are Node.js 22 or newer, Git, FFmpeg (including ffprobe), and Chrome or Chromium, with node, ffmpeg, and ffprobe on the PATH:

```sh
git clone https://github.com/nateherkai/herk-edit-kit.git
cd herk-edit-kit
npm ci
npm run setup
npm test
```

Setup checks the tools and creates .env only if it is absent; add only the keys for the services you use. The optional transcription helper uses ElevenLabs Scribe, with OpenAI or local Whisper and Kie.ai as alternatives.

## What It Provides

skills.sh publishes per-skill install counts for 14 of the kit's 15 skills (motion-showreel is not indexed). The 9 most-installed skills are listed below; the remaining 5 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| short-form-edit | 499 | turn talking-head footage into a finished reel, YouTube Short, or short ad with curiosity-led openings, transcript-synced motion graphics, captions, music, and sound effects |
| cut-silences | 473 | remove silences and dead air, producing an edit list (EDL), a re-timed transcript, and optionally the cut video via ffmpeg |
| video-storytelling | 471 | design and build the visual layer of a long-form video as one persistent world the camera moves through |
| cut-mistakes | 469 | find and remove stutters, repeats, false starts, and retakes review-gated, rendering only the approved cuts |
| make-a-video | 434 | interview a beginner and build a finished HyperFrames video with mandatory preview and visual-verification gates |
| hyperframes-video-beats | 411 | plan, write, time, style, and validate motion-graphic beats for long-form HyperFrames videos |
| edit-video | 410 | complete edit of a raw talking-head video through transcription, silence trimming, mistake review, storytelling, and verified rendering |
| style-library | 391 | select, customize, or extend the reusable motion-graphics card library and style templates |
| short-form-video | 373 | maintain the legacy May Shorts teaching compositions; use short-form-edit for new reels |

The remaining 5 indexed listings range from 22 to 25 installs (gsap at 25; website-to-hyperframes at 24; hyperframes, hyperframes-registry, and hyperframes-cli at 22 each).

## Why This Matters for Hermes Agents

The kit encodes a full editing pipeline an agent otherwise improvises: strip silences, review mistakes, plan the story, build the motion layer, and validate. cut-silences and cut-mistakes are transcript-driven and review-gated, so an agent proposes every cut with a reason and renders only the approved edits, which keeps a destructive operation reversible. video-storytelling's persistent-world model replaces a wall of disconnected graphics with one continuous scene, and short-form-edit carries planning references and validators for caption timing, source mapping, and footage reuse. The style library gives an agent 406 draft cards to assemble from instead of hand-drawing every graphic, and the HyperFrames and GSAP skills supply the animation substrate. The trade-off is a heavier setup (Node 22+, FFmpeg, Chrome) and optional paid services for transcription and asset generation, so it suits agents that already have a media toolchain.

## Usage

| You say | What happens |
|---|---|
| Edit my recording at this path | Uses edit-video to tighten dead air, propose mistake cuts, and produce a reviewed draft |
| Cut the silences from this talking-head video | Uses cut-silences to emit an EDL, a re-timed transcript, and optionally the cut video |
| Remove my stutters and retakes | Uses cut-mistakes to propose each cut with context and render only the approved edits |
| Turn this recording into a 9:16 reel | Uses short-form-edit to plan a hook and payoff, add captions, B-roll, and sound design |
| Design the visuals for my long video | Uses video-storytelling to build one persistent world the camera moves through |
| Make a video from my rough idea | Uses make-a-video to interview you and build a finished MP4 with preview gates |

## Verification

Confirm the README and representative skill bodies resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/nateherkai/herk-edit-kit/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/nateherkai/herk-edit-kit/main/.agents/skills/short-form-edit/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/nateherkai/herk-edit-kit/main/.agents/skills/edit-video/SKILL.md | head -40
```

All three URLs return 200. After installing, review each .agents/skills/<name>/SKILL.md before relying on it, and re-check the security pages on skills.sh for the Warn verdict noted below.

## Security

skills.sh verdicts for sampled skills (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| short-form-edit | Pass | Pass | Pass |
| cut-silences | Pass | Pass | Pass |
| video-storytelling | Pass | Pass | Pass |
| cut-mistakes | Pass | Pass | Pass |
| make-a-video | Pass | Pass | Warn |

Across the 5 sampled skills there are 14 Pass, 1 Warn, and 0 Fail cells. Four skills pass all three checks; make-a-video carries the single Warn (Snyk). The other 9 indexed listings carry no published verdict.

## Limitations

- Snapshot data, verified Nov 26, 2026: 4,046 combined installs across 14 indexed listings; 3,176 GitHub stars; NOASSERTION license; last pushed Oct 14, 2026. Counts drift over time.
- GitHub reports NOASSERTION for the license field; the repo ships LICENSE, THIRD_PARTY_NOTICES.md, and a separate licenses/HYPERFRAMES-LICENSE, so treat each component's terms individually.
- skills.sh sampled only 5 of the 14 indexed listings; the remaining 9 carry no published verdict.
- The 15 skills are mirrored into both .agents/skills/ and .claude/skills/, so the tree holds two copies of each; motion-showreel ships in the repo but is not indexed.
- The style library's cards may load GSAP and Google Fonts from public CDNs; localize those dependencies before assembling a final project.

## Related

[Motion Graphics Skills - Launch Video Suite](/hermes/skills/catalog/motion-graphics-skills-setup) | [Motion Graphics Skills - B-roll and Explainer Video](/hermes/skills/catalog/barty-motion-graphics-setup) | [Kinetic Typography Skills - Animated Text for Agents](/hermes/skills/catalog/kinetic-typography-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run npm test after setup; it exercises the synthetic transcript fixture (examples/editing/source.json) with no footage or API keys required.
- Keep your footage in a new project folder; files already tracked by Git stay tracked, and raw-media/ plus new video-projects/ folders are ignored automatically.
- Use short-form-edit for new reels; short-form-video documents the older May Shorts compositions and is kept for compatibility.
- The three showcase videos are the only private recordings explicitly cleared for public sharing; do not import other private transcripts or credentials.
- Review the actual motion and audio before publishing: the kit is an agent-guided workflow, not an automated publish button.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
