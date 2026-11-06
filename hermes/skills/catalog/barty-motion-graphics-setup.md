---
title: "Motion Graphics Skills - B-roll and Explainer Video"
description: "barty-bart/motion-graphics on skills.sh: 12.2K combined installs across 6 listings; motion B-roll, SAM 2 object separation, sound and explainer cuts."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/barty-motion-graphics-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "video", "motion graphics", "ffmpeg"]
---

# Motion Graphics Skills - Setup Guide

**Source:** [barty-bart/motion-graphics](https://www.skills.sh/barty-bart/motion-graphics) via skills.sh - 12.2K combined installs across 6 indexed listings; first seen 2026-11-06 (Nov 6, 2026 morning sweep)
**GitHub:** 1,086 stars, MIT licence (LICENSE in the repo root), last pushed 2026-10-13, 6 SKILL.md directories under skills/, each with its own README and a demo GIF under docs/
**Category:** Video editing for agents: motion B-roll timed to a transcript, object separation, sound effects and three explainer cuts
**Quality Tier:** 🟡 Review - MIT licence, but the five sampled skills carry seven scanner warnings between them and every skill renders or rewrites video on your machine.

Motion Graphics is a set of six video-editing skills published under Barty-Bart for Claude Code and other agents that read skills, under the tagline "each skill does one job". Two of them work on footage you already shot: `motion-broll` reads a talking-head video and its transcript and builds motion-graphic B-roll timed to the speaker's words, and `object-separation` pulls a person, product or hand off its background with SAM 2 on your own machine. The other four make video from a brief: three explainer cuts of different lengths and a sound pass that lands on the beat.

The interesting detail is that the outputs are rendered rather than prompted. The explainer skills render from code to MP4 with music, the three cuts differ deliberately (a 12 to 20 second hype promo, a 10 to 30 second continuous shot, a 45 to 90 second product demo), and `sound-effects` mixes to -16 LUFS with true peaks below -4 dBFS measured on the exported file. Each skill ships its own README with the full guide, so the agent can read the method for one job without loading the other five.

## Installation

The README installs through the Agent Skills CLI:

```bash
npx skills add Barty-Bart/motion-graphics
```

It prompts you to pick the skills you want. It works in Claude Code and other agents that read skills, and the manual alternative is to copy a skill's folder out of `skills/` into `.claude/skills/`.

Read the per-skill README before the first render. `skills/motion-broll/README.md`, `skills/object-separation/README.md` and the three `explainer-*` READMEs carry the working method, and the README links a demo GIF for each skill under `docs/` so you can see the output before spending a render on it.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| motion-broll | 2,691 | Turns a talking-head video and its transcript into motion-graphic B-roll timed to the words, in a continuous one-shape style driven by a cursor and spring motion |
| sound-effects | 2,160 | Builds a cue list, checks the music's beat grid against the kick drums, lands cuts on the beat and places one real CC0 sound effect per cue |
| object-separation | 2,056 | Separates a person, product or hand from the background on your own computer with SAM 2, and outputs the video with the subject highlighted plus frame-by-frame masks |
| explainer-high-energy | 1,811 | A 12 to 20 second beat-locked promo: kinetic typography, a shape that carries across every transition and a HUD frame, rendered from code to MP4 |
| explainer-engaging | 1,776 | A 10 to 30 second continuous shot: one hero element travels through the product workflow laid out as stations on one canvas and the camera follows it |
| explainer-default | 1,754 | A clean 45 to 90 second product demo: the product's own UI rebuilt and shown up close as it is used, on an airy light canvas |

All 6 indexed listings clear the 500-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

Video is where text-only agents produce the most confident nonsense. An agent can describe a cut, a beat and a transition, and none of that survives contact with a render. These skills close that gap by writing code that emits an MP4, so the output is a file you can watch rather than a treatment you have to interpret.

The transcript-timed B-roll skill is the strongest case for the suite. Timing overlays to a speaker's actual words requires word-level timings from a transcript, and doing it by hand across a ten minute video is an hour of scrubbing. Handing the video and transcript to one skill that returns a timed overlay track is a real reduction in work, and the one-shape constraint keeps the result coherent.

Local separation matters for anyone working with client footage or footage of themselves. `object-separation` runs SAM 2 on the machine, scans the hardware first to pick a model size, and returns masks rather than uploading the clip to a service. The privacy property is the point, not a feature bullet.

The sound pass is the least glamorous and the most measurable. Beat grids, cue lists, one effect per cue and a loudness target on the exported file are checkable claims, and they separate a finished piece from a clip with music behind it.

## Usage

| You say | What happens |
|---|---|
| "Turn this interview into B-roll" | motion-broll reads the video and transcript and builds a one-shape motion overlay timed to the words |
| "Cut the speaker out of this clip" | object-separation scans the machine, picks a SAM 2 model size and writes the video with the subject separated plus masks |
| "Make a hype promo for the launch" | explainer-high-energy renders a 12 to 20 second beat-locked promo from code to MP4 |
| "I need a one-take explainer of the workflow" | explainer-engaging builds a single canvas of stations with one hero element travelling through it |
| "Make a 60 second product demo" | explainer-default rebuilds the product UI and films it up close while it is used |
| "The audio sounds cheap" | sound-effects builds a cue list, checks the beat grid, lands cuts on the beat and mixes to -16 LUFS |

## Verification

Read the skill you plan to run before installing it:

```bash
curl -fsSL https://raw.githubusercontent.com/barty-bart/motion-graphics/main/skills/motion-broll/SKILL.md | head -5
curl -fsSL https://raw.githubusercontent.com/barty-bart/motion-graphics/main/skills/sound-effects/SKILL.md | head -5
```

Both return 200 on the `main` branch. The first should open with `name: motion-broll` and a description naming the continuous one-shape style, the cursor and spring motion. The second should name the cue list, the beat grid check and the bundled CC0 library.

Then install and confirm the skill landed with its README, which is where the working method lives:

```bash
npx skills add Barty-Bart/motion-graphics
ls ~/.claude/skills/motion-broll
```

The listing should show SKILL.md next to README.md and whatever scripts the skill needs. If only SKILL.md is there, you copied a single file rather than installing the skill.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| motion-broll | Warn | Warn | Pass |
| sound-effects | Pass | Pass | Warn |
| explainer-high-energy | Pass | Pass | Warn |
| explainer-engaging | Warn | Pass | Warn |
| explainer-default | Pass | Pass | Warn |

This is the warning-heaviest sample in the batch: four Snyk Warns out of five, plus Trust Hub and Socket Warns on motion-broll. Read the flagged SKILL.md and its scripts before running them; the skills execute local rendering and, in the case of object-separation, download and run a segmentation model.

The footage stays on your machine, which is the good part. The download is still a download: check what model size the machine scan selects and where the weights land before you point this at client material. The bundled sound effects are CC0, but the wider asset terms are split, with MIT for the code, the SIL Open Font License for the Geist fonts and ISC for the Lucide icon paths.

## Limitations

- Snapshot data, verified 2026-11-06: 12,248 combined installs across 6 indexed listings; 1,086 GitHub stars; MIT; last pushed 2026-10-13. Counts drift over time.
- These skills render. A brief in, an MP4 out means the machine needs the rendering toolchain and codecs each skill's README pins, plus enough CPU or GPU to finish the job. The skill file alone is not enough.
- Object separation is hardware-bound. SAM 2 model choice comes from a scan of your machine, so the same skill behaves differently on a laptop and a workstation, and long clips take time.
- The sound pass assumes music with a detectable beat grid. A spoken-word bed or an ambient track gives the beat check nothing to align to.
- Asset terms are split by type: MIT for the code, SIL Open Font License for the Geist fonts, ISC for the Lucide icon paths, and CC0 1.0 for the sound effects in `skills/sound-effects/sfx/`. Check `LICENSES.md` in that skill before redistributing.
- The README also promotes the author's paid Skool community. Nothing in the six skills requires it, and the install command above is the whole dependency.

## Related

- [Motion Graphics Skills - Launch Video Suite](/hermes/skills/catalog/motion-graphics-skills-setup)
- [Explainer Video Skills - Script to Render Setup](/hermes/skills/catalog/explainer-video-skills-setup)
- [Hyperframes Setup](/hermes/skills/catalog/hyperframes-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `motion-broll` and a transcript that has word-level timings. The skill's whole value is timing to the words, and a paragraph-level transcript gives it nothing to align to.
- Pick the explainer by duration before you pick it by style. Twelve to twenty seconds, ten to thirty and forty-five to ninety are different products, not three settings of one.
- Run `object-separation` on a short clip first. It tells you which model the machine scan chose and how long a frame takes before you commit a long video.
- Do the sound pass last. `sound-effects` needs the final cut so its cue list matches the picture, and re-cutting after the mix wastes the pass.
- Keep one shape across a B-roll run. The one-element-morphs-never-cuts rule is what makes generated overlays look designed rather than assembled.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
