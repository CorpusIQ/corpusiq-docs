---
title: "DaVinci Resolve Skills - Video Editing Skill Suite"
description: "chaiwithjai/davinci-resolve-claude-skills: 1.5K combined installs. Claude Code skills for editing, audio, color and export in DaVinci Resolve 20."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/davinci-resolve-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-28"
tags: ["hermes skill", "agent skill", "skill setup", "davinci resolve", "video editing", "post-production"]
---

# DaVinci Resolve Skills - Setup Guide

**Source:** [chaiwithjai/davinci-resolve-claude-skills](https://skills.sh/chaiwithjai/davinci-resolve-claude-skills) via skills.sh - 1.5K combined installs across 11 indexed listings; first seen Nov 28 2026 (morning sweep)

**GitHub:** [ChaiWithJai/davinci-resolve-claude-skills](https://github.com/ChaiWithJai/davinci-resolve-claude-skills) - 38 stars, MIT license, branch main, last pushed 2026-05-17; 11 skills under skills/<name>/SKILL.md plus a docs/wiki/ reference layer and per-skill Python scripts.

**Category:** Agent skills - DaVinci Resolve 20 post-production: editing, audio, color grading, titles, export and troubleshooting

**Quality Tier:** 🟢 Green - all 11 sampled listings pass Gen Agent Trust Hub, Socket and Snyk.

chaiwithjai/davinci-resolve-claude-skills is a Claude Code skills library for DaVinci Resolve 20, built by Jai Bhagat and indexed on skills.sh. Eleven skills each solve one post-production job to be done: install and setup, a reusable DevRel project template, screen-recording cuts, webcam color grading, podcast audio cleanup, branded titles and lower thirds, multi-platform export, troubleshooting, Computer Use training, speaker-led social editing, and hard-drive folder autocutting.

The repo's core design idea is a two-layer reference model. Fast working summaries live under docs/wiki/, one per official Blackmagic DaVinci Resolve 20 training PDF, and each skill cites specific PDF page ranges (about 1,800 pages across six free Blackmagic PDFs) as a ground-truth reset layer. Several skills also ship Python scripts that drive Resolve through its external scripting API, so an agent can perform real edits, exports and audits rather than only describe them.

## Installation

The README installs skills by copying them into ~/.claude/skills/, which Claude Code picks up automatically:

```bash
git clone https://github.com/ChaiWithJai/davinci-resolve-claude-skills.git
cp -R davinci-resolve-claude-skills/skills/* ~/.claude/skills/
```

To keep the install pullable via git, symlink each skill directory instead:

```bash
git clone https://github.com/ChaiWithJai/davinci-resolve-claude-skills.git
cd davinci-resolve-claude-skills
for skill in skills/*/; do
  name=$(basename "$skill")
  ln -s "$(pwd)/$skill" "$HOME/.claude/skills/$name"
done
```

For a single project, copy the skills into <repo>/.claude/skills/ instead. Several skills ship Python scripts that drive Resolve through its external scripting API; to run them, enable DaVinci Resolve > Preferences > System > General > External scripting using (Local or Network), then run from the Workspace > Console > Py3 console or from your shell after exporting the RESOLVE_SCRIPT_API, RESOLVE_SCRIPT_LIB and PYTHONPATH variables the README lists.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| davinci-resolve-social-editor | 203 | Plan and build speaker-led social edits with semantic cuts, B-roll, burned-in captions and Resolve handoff. |
| davinci-resolve-titles-and-lower-thirds | 183 | Branded titles, animated lower thirds and logo intros from Resolve's Text+ node and Fusion animation modifiers. |
| davinci-resolve-export-multi-platform | 163 | Export one edit for YouTube (16:9), LinkedIn (square 1:1) and Reels/Shorts/TikTok (9:16) with correct dimensions and loudness. |
| davinci-resolve-color-grade-webcam | 147 | Make webcam or talking-head footage broadcast-quality: exposure, white balance, skin tones and overall color. |
| davinci-resolve-audio-cleanup-podcast | 145 | Denoise, de-hum and level podcast or interview audio, and duck music under voice in Fairlight. |
| davinci-resolve-troubleshooting | 130 | Diagnose common breakage: red playback indicator, missing media, offline clips, audio drift and render crashes. |
| davinci-resolve-setup | 123 | Install Resolve correctly, configure media drives and backups before the first edit. |
| davinci-resolve-cut-screen-recording | 114 | Cut a long screen recording or demo into a tight watchable version, removing dead air, mistakes and silences. |
| davinci-resolve-devrel-project-template | 100 | A reusable project with bins, timeline, render presets and a color preset for repeat DevRel videos. |
| social-video-folder-autocutter | 95 | Turn a hard-drive folder into repeatable Instagram and YouTube cut briefs, B-roll plans and eval artifacts. |
| davinci-resolve-computer-use-training | 94 | Work through Blackmagic lesson homework with Computer Use and turn UI lessons into production skills. |

All 11 indexed listings appear in the table above.

## Why This Matters for Hermes Agents

This suite is a compact reference for wiring an agent to a desktop application through its scripting API. Each skill bundles instructions plus Python scripts that attach to a running Resolve instance via DaVinciResolveScript, so a Hermes agent that can shell out can drive real exports, silence cuts and timeline checks rather than only producing advice.

The two-layer reference model is the part worth copying. Fast wiki summaries live in docs/wiki/ as working context, and every skill cites specific page ranges in the six official Blackmagic Resolve 20 PDFs as a reset layer. When the user pushes back, the agent re-reads the cited PDF range instead of improvising. That is a clean grounding pattern for any agent that summarizes a large, versioned body of documentation.

The skills are written around jobs to be done rather than tool features: cut the story, repair the audio, keep the speaker in frame, add readable captions, source B-roll. Each description enumerates the triggering phrases, so a router can match user intent to the right skill without a separate classification pass. The README's production-standard checklist is also a ready acceptance gate for generated video: a coherent story, clean dialogue on phone speakers, proofread burned-in captions, and a Resolve timeline a human editor can take over.

## Usage

| You say | What happens |
|---|---|
| "My screen recording is too long, help me cut it down" | davinci-resolve-cut-screen-recording removes dead air, mistakes and silences. |
| "How do I make my webcam look better" | davinci-resolve-color-grade-webcam corrects exposure, white balance and skin tones. |
| "The music in my podcast is drowning out the host" | davinci-resolve-audio-cleanup-podcast denoises, de-hums and ducks music under voice. |
| "Export my edit for LinkedIn and YouTube" | davinci-resolve-export-multi-platform renders the same edit at 16:9 and square 1:1. |
| "Make this folder into an Instagram Reel and YouTube cut" | social-video-folder-autocutter plans folder-to-video cut briefs and B-roll plans. |
| "Add a name lower third and an animated logo intro" | davinci-resolve-titles-and-lower-thirds builds reusable title templates with Text+ and Fusion. |
| "Resolve is dropping frames when I render" | davinci-resolve-troubleshooting walks the common failure modes and fixes. |

## Verification

The layout on branch main is skills/<name>/SKILL.md. Fetch a skill directly to review its frontmatter and instructions before installing:

```bash
curl -sL https://raw.githubusercontent.com/ChaiWithJai/davinci-resolve-claude-skills/main/skills/davinci-resolve-social-editor/SKILL.md
```

After a clone, confirm the skill directories:

```bash
git clone --depth 1 https://github.com/ChaiWithJai/davinci-resolve-claude-skills.git /tmp/davinci-resolve-skills
ls /tmp/davinci-resolve-skills/skills/
head -3 /tmp/davinci-resolve-skills/skills/davinci-resolve-setup/SKILL.md
```

The skills listing should show 11 skill directories. The repo root also holds docs/wiki/ (the reference summaries) and docs/jtbd-map.md (the job-to-skill mapping).

## Security

skills.sh verdicts for sampled skills (verified 2026-11-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| davinci-resolve-social-editor | Pass | Pass | Pass |
| davinci-resolve-titles-and-lower-thirds | Pass | Pass | Pass |
| davinci-resolve-export-multi-platform | Pass | Pass | Pass |
| davinci-resolve-color-grade-webcam | Pass | Pass | Pass |
| davinci-resolve-audio-cleanup-podcast | Pass | Pass | Pass |
| davinci-resolve-troubleshooting | Pass | Pass | Pass |
| davinci-resolve-setup | Pass | Pass | Pass |
| davinci-resolve-cut-screen-recording | Pass | Pass | Pass |
| davinci-resolve-devrel-project-template | Pass | Pass | Pass |
| social-video-folder-autocutter | Pass | Pass | Pass |
| davinci-resolve-computer-use-training | Pass | Pass | Pass |

All 11 sampled listings clear Gen Agent Trust Hub, Socket and Snyk, which is why this guide is Green. The Python automation scripts are the main attack surface worth a second look, since they execute locally against a running Resolve instance.

## Limitations

- Snapshot data, verified 2026-11-28: 1,497 combined installs across 11 indexed listings; 38 GitHub stars; MIT license; last pushed 2026-05-17. Counts drift over time.
- The repo last pushed 2026-05-17, so the cited DaVinci Resolve 20 PDF page ranges may drift behind newer Blackmagic releases.
- Every skill sits under 203 installs (davinci-resolve-social-editor leads at 203), so this is an early-stage suite with a small install base.
- The Python automation scripts attach to a running Resolve instance via DaVinciResolveScript, so they need Resolve open with a project loaded and external scripting enabled, with Network mode for remote use.
- The docs/wiki/ files are working summaries, not ground truth; the README directs the agent back to the cited PDF page ranges when context drifts.

## Related

- [OpenMontage Video Production Skills - Setup Guide](/hermes/skills/catalog/openmontage-video-skills-setup)
- [Auto-Editor Skills - Video & Audio Editing Setup](/hermes/skills/catalog/auto-editor-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Read a skill's SKILL.md before installing the whole suite: the description frontmatter is the trigger, and each skill cites the PDF page ranges that anchor its technique.
- Prefer the symlink install if you will pull updates, since the repo can change without re-copying.
- To run the Python automation, enable external scripting in Resolve and keep a project open; the scripts attach to the running instance via DaVinciResolveScript.
- Treat docs/wiki/ as fast context, not truth: when a cut looks wrong, read the cited PDF page range to reset the model.
- All 11 sampled listings pass all three scanners, but re-check the skills.sh security pages before pulling the suite into a production profile.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
