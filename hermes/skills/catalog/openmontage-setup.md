---
title: "OpenMontage - Video Production Studio for Agents"
description: "calesthio/openmontage: 101.8K combined installs across 90 listings; an open-source agentic video studio that cuts real footage and renders clips."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/openmontage-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup", "video production", "ffmpeg", "remotion"]
---

# OpenMontage - Setup Guide

**Source:** [calesthio/openmontage](https://www.skills.sh/calesthio/openmontage) via skills.sh - 101.8K combined installs across 90 indexed listings; first documented November 3, 2026 (evening sweep)
**GitHub:** 76,073 stars, AGPL-3.0, last pushed 2026-11-03, 140 SKILL.md directories
**Category:** Video production for agents: cutting, captions, avatars, motion and rendered social clips through one studio suite
**Quality Tier:** 🟡 Two of the five sampled listings carry a Socket or Snyk warning, and the licence is AGPL-3.0 rather than permissive

OpenMontage is an open-source agentic video production system: 12 production pipelines, 100+ tools and 700+ skill and production-knowledge files, shipped as 140 SKILL.md directories under `.agents/skills/`. The premise in the README is that a coding assistant becomes a video production studio, and one plain-language request should carry research, scripting, asset generation, editing and final composition without the user learning the pipeline order.

The distinction the README draws is the one worth keeping. The pack can animate stills, but it also builds a corpus from free stock footage and open archives, retrieves real motion clips, edits them into a timeline and renders the result, which is a different job from turning a handful of images into a slideshow. The worked example is a cinematic science-fiction trailer, SIGNAL FROM TOMORROW, taken from concept and script through Veo-generated motion clips and a soundtrack into a Remotion composition.

## Installation

skills.sh lists this source at https://www.skills.sh/calesthio/openmontage. The standard CLI form for a listed repository is:

```bash
npx skills add calesthio/openmontage
```

The README excerpt in this pack stops before its Quick Start anchor, so the CLI is the skills.sh route and the loop below is the route that the tree itself guarantees. Every skill is a folder with a `SKILL.md` at `.agents/skills/<name>/SKILL.md`, which is the same shape a Hermes profile reads:

```bash
git clone --depth 1 https://github.com/calesthio/openmontage.git /tmp/openmontage
mkdir -p ~/.hermes/profiles/corpusiq/skills
for skill in /tmp/openmontage/.agents/skills/*; do
  [ -f "$skill/SKILL.md" ] || continue
  destination="$HOME/.hermes/profiles/corpusiq/skills/$(basename "$skill")"
  [ -e "$destination" ] || cp -R "$skill" "$destination"
done
```

That loop installs all 140 directories, not the 90 the index carries, and it never overwrites a skill folder that already exists. Generation and voice work call hosted providers, and the README keeps the provider list in `docs/PROVIDERS.md` rather than inline, so read that file before a run that needs keys.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| video-edit | 1,657 | The editing step of the README flow: retrieved clips and generated assets cut into a timeline after asset generation and before composition. |
| svg-character-animation | 1,562 | Animated SVG characters; the tree also carries character-rigging and canvas-procedural-animation as neighbours. |
| video-understand | 1,555 | Reading a video that already exists, which is the README's "paste a video" starting point. |
| ai-video-gen | 1,384 | Hosted video-model generation for shot clips, the route the SIGNAL FROM TOMORROW trailer used for its motion. |
| video-download | 1,374 | Pulling source footage in, part of the free stock-footage and open-archive corpus route in the README. |
| ffmpeg | 1,336 | Command-line encode, trim and inspect work, present in the tree at `.agents/skills/ffmpeg/`. |
| remotion | 1,334 | Composition and render as React code; the trailer example finishes as a Remotion composition. |
| character-animation-qa | 1,325 | A check pass over character animation before a piece is delivered. |
| text-to-speech | 1,316 | Speaking a finished script, with elevenlabs, doubao-tts, fish-audio-tts and azure-text-to-speech sitting beside it in the tree. |
| visual-style | 1,283 | Fixing the look a piece is generated against so separate shots read as one film. |
| pose-library-design | 1,281 | Pose sets that the character animation skills build their motion from. |
| video-toolkit | 1,270 | Shared video helpers that the other video skills sit on top of. |
| create-video | 1,263 | The end-to-end entry that follows the README order: research, script, assets, edit, compose. |
| seedance-2-0 | 1,261 | Seedance 2.0 motion generation, alongside seedance-2-5 and minimax-h3 for other models. |
| sound-effects | 1,231 | Sound design and effects for a cut, which the trailer example names as part of the build. |
| speech-to-text | 1,230 | Transcribing audio so edits and captions can be driven by the words actually spoken. |
| playwright-recording | 1,220 | Screen recording driven by Playwright, with synthetic-screen-recording and website-to-video as the other capture routes. |
| elevenlabs | 1,219 | Hosted voice generation for narration. |
| framer-motion | 1,218 | Motion inside React interfaces, for pieces that include an animated product screen. |
| lottie-bodymovin | 1,214 | Lottie files and their export path for vector motion. |
| avatar-video | 1,214 | Talking-avatar video with a generated presenter; heygen sits next to it in the tree. |

The remaining 69 indexed listings range from 113 to 1,212 installs.

The tree runs wider than the index: 140 `SKILL.md` directories against 90 indexed listings. Two names visible in the layout excerpt, character-rigging and canvas-procedural-animation, carry no indexed listing in this pack's rows, so the table is a sample of the pack rather than its full inventory.

## Why This Matters for Hermes Agents

Video is the format where an agent most often produces something that looks finished and is not: invented b-roll, a caption track written from a guess, a timeline assembled from stills and called a film. This pack pushes those decisions into skills that name the step, so a run has an order to follow instead of one large prompt. The README's claim is narrow and testable: the agent retrieves actual motion clips and edits them rather than animating images and hoping the result passes.

The skill set is also unusually broad for one repository, with editing, generation, voice, transcription, character animation, motion graphics, 3D, diagrams and screen capture in the same tree, so one request can move from script to voice to cut to render without a second toolchain. For an agent that has to finish a piece unattended, that continuity matters more than any single skill in the list.

The cost model is mixed, and it is the part worth designing around: pipeline scaffolding, ffmpeg work, Remotion composition and the motion-graphics skills are local, while generation, voice and avatar steps call hosted providers listed in `docs/PROVIDERS.md`. Composition in named tools such as Remotion, ffmpeg and HyperFrames also makes output reviewable, because a frame can be pulled and inspected and the same spec rendered again. And the AGPL-3.0 licence is fine for internal production but awkward if a modified version is offered to others over a network, so a team that forks the pack should read the licence before shipping it inside a product.

## Usage

| You say | What happens |
|---|---|
| "Take this video I like and make me something in that style" | video-understand reads the reference, visual-style fixes the look, and the build runs from there instead of guessing at the style. |
| "Cut these five clips into a 40 second piece with music" | video-edit assembles the timeline, sound-effects or music supplies the bed, and ffmpeg finishes the encode. |
| "Write a 60 second script about our launch and voice it" | The scripting step produces the text, text-to-speech or elevenlabs records the narration, and the audio lands as a track for the edit. |
| "Generate a shot of a city at night, slow push in" | ai-video-gen or seedance-2-0 returns a motion clip rather than a still, which is what the README insists on. |
| "Turn my website into a 30 second promo" | website-to-video or playwright-recording captures the pages, then the edit and composition skills build the cut. |
| "Animate this character I drew for the intro" | svg-character-animation with character-rigging builds the motion, and character-animation-qa checks it before delivery. |
| "Add captions to this interview" | speech-to-text transcribes the audio and the caption track is laid over the existing cut. |

## Verification

The raw paths below were built from the repository tree on branch main. Probe them before installing, and expect an HTTP 200:

```bash
for p in ffmpeg create-video; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/calesthio/openmontage/main/.agents/skills/$p/SKILL.md"
done
```

After the clone, count directories rather than trusting the index, and read one skill's frontmatter, which is what the agent routes on:

```bash
git clone --depth 1 https://github.com/calesthio/openmontage.git /tmp/openmontage
find /tmp/openmontage/.agents/skills -name SKILL.md | wc -l
head -4 /tmp/openmontage/.agents/skills/create-video/SKILL.md
```

The count should be 140. If it is smaller, the clone is shallow or interrupted, and the copy loop will install a partial studio. Confirm the installed side separately with `ls ~/.hermes/profiles/corpusiq/skills | wc -l` and check that the folders you expect, such as `ffmpeg` and `create-video`, are present.

## Security

skills.sh verdicts for sampled skills (verified November 3, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| video-edit | Pass | Pass | Pass |
| grok-media | Pass | Pass | Pass |
| threejs-materials | Pass | Pass | Pass |
| hyperframes-media | Pass | Warn | Warn |
| website-to-hyperframes | Pass | Pass | Warn |

The sample is broad (editing, media generation, three.js materials and two HyperFrames listings) and every verdict is Pass on Gen Agent Trust Hub, but three of the five carry at least one warning, so read the individual security pages for the skills you actually intend to run. A warning on a media skill is usually about network calls to a provider rather than about code that runs on your machine, and the security page is the place to confirm which.

Nothing in the repository is a compiled daemon: the installable content is Markdown skill folders plus whatever the individual pipelines call. The real surface is therefore the provider credentials that generation, voice and avatar steps need, and those belong in the environment rather than in a skill folder.

## Limitations

- Snapshot data, verified November 3, 2026: 101,840 combined installs across 90 indexed listings; 76,073 GitHub stars; AGPL-3.0; last pushed 2026-11-03. Counts drift over time.
- The licence is AGPL-3.0, so a modified version offered to others over a network carries source-sharing obligations; internal production use is unaffected.
- The tree carries 140 `SKILL.md` directories while skills.sh indexes 90 listings, so installing the repository and installing from the index are not the same set.
- Several overlapping motion stacks ship together (Remotion, HyperFrames, GSAP, three.js, manim, Lottie), which is more than one project needs and more context than one run should load.
- Generation, voice and avatar steps depend on hosted providers whose keys and terms live in `docs/PROVIDERS.md`; the free route is stock footage plus local encoding.
- The README excerpt here does not include the Quick Start commands, so the CLI route comes from skills.sh and the copy loop from the repository layout rather than from documented instructions.

## Related

- [ai-video-generation - AI Video Production (196K installs)](/hermes/skills/catalog/ai-video-generation-setup)
- [Claude Code Video Toolkit - Video Pipeline Skills Setup](/hermes/skills/catalog/claude-code-video-toolkit-setup)
- [Motion Graphics Skills - Launch Video Suite](/hermes/skills/catalog/motion-graphics-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start from the edit and work backwards. Decide the runtime and shot count, then generate only the clips that plan needs, because a generated clip you never cut is pure cost.
- Use the free corpus route for anything that does not need a specific shot. The README's differentiator is real footage from open archives, and it is also the cheapest path through the pipeline.
- Keep one motion stack per project. Loading Remotion, HyperFrames and GSAP into the same run produces three ways to do the same thing and a render you cannot explain.
- Pull a frame from the middle of every shot before the final encode. Composition happens in tools you can inspect, so the check is cheap and it catches the invented detail that a preview hides.
- Put provider keys in the environment, never in a skill folder, and check `docs/PROVIDERS.md` before a run that needs generation or voice so the run fails at the planning step rather than halfway through.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
