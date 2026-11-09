---
title: "Brag - Launch Video Skill for Agents"
description: "latent-spaces/brag on skills.sh: 36.3K combined installs. Turns a finished project into a short, shareable launch video with music and share copy."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/brag-launch-video-setup/"
robots: "index,follow"
last_updated: "2026-11-08"
tags: ["hermes skill", "agent skill", "skill setup", "launch video", "hyperframes", "brag"]
---

# Brag - Setup Guide

**Source:** [latent-spaces/brag](https://www.skills.sh/latent-spaces/brag) via skills.sh - 36,286 combined installs across 2 indexed listings; first seen 2026-11-08 (Nov 8, 2026 evening sweep)
**GitHub:** 20,778 stars, MIT via LICENSE, `main` branch, last pushed 2026-10-23, 2 SKILL.md directories at `skills/brag/` and `skills/brag-slim/`
**Category:** Launch video: turn a finished project into a short shareable video with music, motion and share copy
**Quality Tier:** 🟡 Beta - 20,778 stars and a Pass verdict on all three scanners for brag, but brag-slim returned a Snyk Warn and the full workflow depends on an external render toolchain.

Brag is a narrow skill with an unusually clear job. You point an agent at a project directory, say three words, and get a 15 to 25 second launch video with a soundtrack, on-screen motion and a caption written to be pasted into a post. The repository ships two skills that do this: `brag`, which hands a composition brief to Hyperframes and renders through it, and `brag-slim`, a single-file rewrite for newer models that builds the whole video with the tools already on the machine. The pack holds 36.3K combined installs, and the repository carries 20,778 stars, a plausible ratio for a project that grew out of a demo rather than a library.

The design decision worth understanding is that the skill owns the story and the renderer owns the pixels. Brag decides the angle, the tone, the three beats to show and the copy, then writes `brag-plan.md` and a composition brief before any code is generated. That split is why the output feels specific to the project instead of generic: the plan is derived from reading the actual source, including the real colours, fonts and component structure, and the creative laws in both SKILL.md files forbid the fallback language that makes most generated promo videos interchangeable.

## Installation

The README's generic path is the skills CLI, which covers Cursor, Codex CLI, Copilot, Gemini CLI and opencode:

```bash
npx skills add https://github.com/latent-spaces/brag --skill brag
```

Add `-g` to install globally so the skill is available in every project, or leave it off to scope the install to the current directory. The slim variant installs the same way:

```bash
npx skills add https://github.com/latent-spaces/brag --skill brag-slim
```

Codex takes the plugin route:

```bash
codex plugin marketplace add latent-spaces/brag
codex plugin add brag@brag
```

Claude Code uses its own marketplace commands, and the plugin carries both skills:

```bash
/plugin marketplace add latent-spaces/brag
/plugin install brag@brag
```

If there is no installer at hand, the README's fallback is a copy into the agent's skill directory:

```bash
rsync -a --exclude '.DS_Store' skills/brag/ ~/.claude/skills/brag/
```

The requirements are listed plainly and they are not optional: Node.js 22 or newer, FFmpeg on `PATH`, and the Hyperframes CLI reachable through `npx hyperframes`. Check the last one before blaming the skill for a failed render:

```bash
npx hyperframes doctor
```

## What It Provides

The threshold for this guide is zero installs, so both indexed listings appear below:

| Skill | Installs | Use For |
|---|---|---|
| brag | 23,283 | The full workflow: read the project, plan the angle, storyboard it, hand a brief to Hyperframes, then render with bundled music and sound effects |
| brag-slim | 13,003 | The lean single-file variant for newer models: same story and share copy, built by the model with on-machine tools, no Hyperframes and no bundled assets |

Both indexed listings clear the threshold, and since the threshold is zero no rows fall below it.

The full skill is a directory, not a single file. `SKILL.md` holds the invocation dispatch, the option table and the four steps, and each step delegates to a reference: `step-1-inspect.md` for extracting material from the project, `step-2-plan.md` for the planning rubric and storyboard, `step-3-compose.md` for the Hyperframes handoff, and `step-4-deliver.md` for validation, render and share copy. `tones.md` defines the seven presets (`default`, `polished`, `yc-parody`, `chaotic`, `deadpan`, `cinematic`, `app-store`) and `audio.md` covers music selection and beat sync. There is also a Python script, `scripts/analyze_music_cues.py`, with its own `pyproject.toml` and `uv.lock`, used to detect cue points in the bundled track.

The output contract is explicit. A run writes to `brag-output/`, or to a timestamped `brag-output-YYYY-MM-DD-HHmmss/` when a previous run exists, and leaves `brag-plan.md`, a `composition/` directory, `brag.mp4`, `brag.jpg` and `share-copy.txt`. The poster frame is not an arbitrary still: the skill requires picking the best frame and baking it as frame 0 so the video has a correct idle thumbnail wherever it is embedded.

The options are a small, honest surface. `--tone` takes a preset or freeform direction, `--format` takes `landscape`, `vertical` or `square` at 30fps, `--duration` overrides the automatic 15 to 25 second window, `--no-music` and `--no-sfx` strip audio, `--title` overrides the inferred name, and `--voice` turns on narration. Voice is off by default and runs on a single provider, Kokoro through Hyperframes, with no provider-selection logic in the skill.

## Why This Matters for Hermes Agents

Hermes finishes things constantly and then has nothing to show for it. The last mile of any build is a shareable artefact, and a launch video is the one that travels, but it is also the one an agent is worst at producing: it requires a creative decision, a render pipeline and a caption, and most agents will happily spend an hour generating a plausible plan and never emit an mp4. Brag removes that failure mode by putting a gate at the end of every step, and the last gate is a file on disk.

The second fit is that the skill is written against the awkward parts of automation rather than the happy path. The plan has to answer nine specific questions before it can exist. Scene durations have to sum inside the window. The composition has to pass `npx hyperframes check` with zero errors before a render is attempted. Share copy has to be written. Those are checkable claims, which means a Hermes run can be verified instead of trusted, and a failed run reports a specific missing artefact rather than a vague disappointment.

The third is privacy discipline. Both skills tell the model to skip build output, lock files, `.git/`, env files, keys and service-account JSON when reading a project, and `brag-slim` adds an explicit instruction to swap real customer names, emails and internal hostnames for fictional stand-ins before anything reaches the video or the share copy. For an agent working inside a real client repository, that is the difference between a demo and an incident, and it is the reason to prefer this skill over asking an agent to "make a promo video" without constraints.

The counterweight is honest: this is a render pipeline, and render pipelines fail on fonts, codecs and GPU limits. Expect a first run to need a missing dependency or a font installed, and treat the checklist in Verification as the real acceptance test.

## Usage

| You say | What happens |
|---|---|
| "let's /brag" | Reads the project, plans an angle, writes `brag-plan.md`, then renders `brag.mp4` into `brag-output/` |
| "/brag --tone 'fake Series A launch from 2016'" | Keeps the freeform direction, maps pacing and structure to the nearest preset, and preserves the wording in the plan and brief |
| "/brag --format vertical --duration 18" | Renders 1080x1920 at 30fps with scene durations summing to about 18 seconds instead of the automatic window |
| "/brag --voice" | Enables Kokoro narration for that run only, with a script written to complement the visuals rather than read the on-screen text |
| "brag about https://example.com" | With brag-slim installed, loads the live site in a headless browser, pulls the real copy, colours and assets, and builds the video from those |
| "/brag-slim about this directory" | Single-file path: inspects, plans, builds and renders with on-machine tools, no Hyperframes and no bundled music |
| "make a launch video for the new settings page" | Narrows the plan to that one feature, with the hook built around it and the rest of the product left out |
| "/brag --no-music --no-sfx" | Renders a silent video for a platform where the soundtrack would be replaced anyway |

## Verification

Confirm the repository layout before trusting any path in the skill, because the two skills live in separate directories:

```bash
curl -fsSL https://raw.githubusercontent.com/latent-spaces/brag/main/skills/brag/SKILL.md | head -12
```

That should open with YAML frontmatter naming `brag` and a description scoped to turning the current project website into a launch video with Hyperframes, followed by the invocation dispatch section. The references are the substance of the skill, so check that they resolve:

```bash
curl -fsSL https://raw.githubusercontent.com/latent-spaces/brag/main/skills/brag/references/step-2-plan.md | head -20
```

After install, the cheapest real test is one run on a small project rather than a dry read of the file. Ask for `/brag`, then check the artefacts it claims to produce:

```bash
ls -la brag-output/ && ffprobe -v error -show_entries format=duration -of default=nw=1 brag-output/brag.mp4
```

A successful run leaves `brag-plan.md`, `composition/`, `brag.mp4`, `brag.jpg` and `share-copy.txt`. The duration reported by `ffprobe` should sit between 15 and 25 seconds, and `brag.jpg` should be a chosen frame rather than a black first frame. If the render never appears, run `npx hyperframes doctor` before changing anything in the skill, since a missing FFmpeg or an old Node version fails in exactly this shape.

For the Hyperframes path, the intermediate gate is worth running directly, because it catches composition errors faster than a full render:

```bash
cd brag-output/composition && npx hyperframes check
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-08) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| brag | Pass | Pass | Pass |
| brag-slim | Pass | Pass | Warn |

Both skills are instruction files, and the only executable code in the pack is a small Python script that reads audio for cue points, shipped with a locked dependency set in `uv.lock`. The scanner results reflect that narrow surface. The Snyk Warn on `brag-slim` is the one asymmetrical result and should be read before installing that variant in an automated pipeline rather than by hand.

The actual risk sits in what the skill is asked to read. `brag` inspects a project directory, and `brag-slim` can be pointed at a live website, where it fetches markup, text and media, then reuses them in a video that is meant to be published. Both files instruct the model to skip env files, keys, credentials and ignored paths, and `brag-slim` tells it to strip script tags and serve assets from local copies rather than live URLs, and to treat page content as data rather than instructions. Those are the right instructions, but they are instructions, not a sandbox. Run the skill against a directory you would be comfortable publishing, and read the generated `brag-plan.md` before the render, because that file is where leaked names or internal URLs would surface first.

Two smaller notes. The README offers a hosted path through letsbrag.app, which sends a site URL to a third party and is outside anything the skill controls. And a brag video is a public artefact by design, so the review step is editorial as much as technical: check the claims in the share copy against what the product actually does.

## Limitations

- Snapshot data, verified 2026-11-08: 36,286 combined installs across 2 indexed listings; 20,778 GitHub stars; MIT license; last pushed 2026-10-23. Counts drift over time.
- `brag-slim` returned a Snyk Warn verdict while the other two scanners passed. The variant is a single instruction file with no bundled assets, so the warning most likely concerns how it fetches and reuses remote material, but that is an inference and the verdict should be read directly.
- The full workflow is not self-contained. It needs Node 22 or newer, FFmpeg, and the Hyperframes CLI, and it delegates timing, animation mechanics and render behaviour to that external toolkit, so failures can originate outside this repository.
- Output quality is a judgement call, not a test. The gates check that a plan exists, durations sum correctly and an mp4 was written; they cannot check whether the video is any good, so a human still has to watch it.
- `brag` on newer models silently switches to the slim workflow unless `--full` or `--voice` is passed. That is convenient and it also means two runs of the same command can produce visually different videos depending on the model in use.
- The seven tone presets are strong defaults and easy to overuse. Nothing in the skill prevents every video from landing on the same playful cadence, which is worth watching if the output is going to a serious audience.

## Related

- [HyperFrames - Full Setup Guide for Hermes Agents](/hermes/skills/catalog/hyperframes-setup)
- [Explainer Video Skills - Script to Render Setup](/hermes/skills/catalog/explainer-video-skills-setup)
- [Motion Design Skills - After Effects and Remotion Setup](/hermes/skills/catalog/motion-design-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Read `brag-plan.md` before letting the render finish. It is short, it states the angle and the claim, and it is far cheaper to correct than a rendered video with the wrong hook.
- Write the tone as a sentence rather than a preset name. `/brag --tone "museum exhibit for a database tool"` produces a more specific edit than `/brag --tone cinematic`, and the skill is built to keep freeform direction.
- Keep `brag-output/` out of the repository. The folder holds intermediate frames and downloads, it is timestamps apart from the previous run, and nothing in the pack suggests it is meant to be committed.
- Check the poster frame. `brag.jpg` becomes frame 0, so a bad pick follows the video into every embed and preview, and it is a one-line fix at that stage.
- Install only `brag-slim` on a machine where the Hyperframes toolchain is not available. It needs no bundled assets and no render service, which makes it the more portable of the two skills.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
