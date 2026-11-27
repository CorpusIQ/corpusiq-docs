---
title: "Lemo OpusCar - Film Style Toolbox for Coding Agents"
description: "lemomo-ai/lemo-opuscar: 5.9K combined installs. A 99-style film toolbox that turns a prompt into a short film made entirely in code, no video model."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/lemo-opuscar-setup/"
robots: "index,follow"
last_updated: "2026-11-27"
tags: ["hermes skill", "agent skill", "skill setup", "video", "film styles", "code art", "animation"]
---

# Lemo OpusCar - Setup Guide

**Source:** [lemomo-ai/lemo-opuscar](https://www.skills.sh/lemomo-ai/lemo-opuscar) via skills.sh - 5.9K combined installs across 1 indexed listing; first documented 2026-11-27 (morning sweep)

**GitHub:** [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) - 21,810 stars, NOASSERTION (per-file licensing; the README splits code under MIT, docs under CC BY-NC 4.0 and demo films under CC BY 4.0), branch main, last pushed 2026-11-26; the skill lives at `plugin/skills/lemo-opuscar/` (a `SKILL.md` plus `scripts/setup.sh`), alongside a `styles/` tree of 99 style prompts, a `core/` render toolkit and a `styleboard/` gallery site

**Category:** Film-style video generation in code: canvas and WebGL renders, code-made scores and text-to-speech narration

**Quality Tier:** 🟡 Yellow - the single sampled listing passes Gen Agent Trust Hub and Socket but carries a Snyk warn, and the repository is a large multi-license tree rather than a small Markdown-only skill

Lemo-Opuscar is a toolbox from Lemomo (LemoLab) of 99 film styles for coding agents, each a style prompt plus a demo film made entirely in code by Claude Opus 5.5, with no video model anywhere in the pipeline. Install the skill once, name a style in one sentence, and the agent directs, draws, scores and mixes a short film in that style.

The skill is a Claude Code plugin, and the README also documents a git-clone route and a copy of `plugin/skills/lemo-opuscar/` into another agent's skills folder. One listing is indexed on skills.sh, so the single table row below is the whole set.

## Installation

The README documents two install routes. The plugin marketplace route is recommended:

```bash
claude plugin marketplace add lemomo-ai/lemo-opuscar
claude plugin install lemo-opuscar@lemolab
```

Or clone the repository and run Claude Code from inside it:

```bash
git clone https://github.com/lemomo-ai/lemo-opuscar.git
cd lemo-opuscar
claude
```

Update and uninstall are a single command each:

```bash
claude plugin marketplace update lemolab && claude plugin update lemo-opuscar@lemolab
claude plugin uninstall lemo-opuscar@lemolab
```

On first use the skill downloads its guides, tools and style prompts to `~/lemo-opuscar`, shared by all your films, and each film's project lands in the folder you start from. You need Node 20+, ffmpeg 7+ and Python 3.11+ (or uv); the agent installs the rest. For other agents, copy `plugin/skills/lemo-opuscar/` into their skills folder.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| lemo-opuscar | 5,901 | Directing and producing a short film made entirely in code, in one of the 99 library styles or a style you make your own: explainers, launches, news, music videos and films built from real material such as satellite imagery, laser scans, CAD files or archive scans. |

All 1 indexed listing appears in the table above.

The substance sits in the skill plus the three guides it reads: `DIRECTOR.md` for story, sound, rhythm, camera, performance and self-checks; `TECHNIQUE.md` for frame-by-frame rendering, voice, music and mixing; and `styles/<style>/STYLE.md` for what each style looks and sounds like. The 99 styles are grouped into 15 categories, from Edit and Documentary through Painting, Printmaking, Cartoons, 3D and Data and Maps. Default output is 1920x1080 at 24 fps, and a film takes an agent roughly 30-60 minutes.

## Why This Matters for Hermes Agents

A "make a film" request usually lands as a dead end for an agent: the tooling is a video model call, a stock library, or a render farm, none of which the agent can drive, debug or cost-account on its own. Lemo-Opuscar turns the whole task into code the agent writes and can fix, so a failed frame is a bug in a JavaScript file rather than a bad prompt or a re-roll.

The style library is the reusable asset. Each of the 99 styles is a tested style prompt plus a working demo film, so an agent does not have to invent a visual system from nothing; it picks a proven one and spends its effort on the story. The evidence styles (Satellite Briefing, LiDAR Survey, Exploded Teardown) are a rare pattern where real data, not a hallucinated scene, drives the picture.

The make-your-own flow matters for builders. An agent can change a library style into a brand-specific one, or build from a blank page, and the kept style lives in `~/lemo-my-styles/` and survives updates. The licensing is deliberately split: films you make are yours, commercial films included, while the style docs are CC BY-NC 4.0, which means redistributing the library itself is the thing that needs care, not using it.

## Usage

| You say | What happens |
|---|---|
| "Make a film in the Neon Tubes style about the coffee farm my family runs." | The skill names the style, reads its STYLE.md, then directs, draws, scores and mixes the film in code. |
| "Make a 40-second LiDAR Survey film about the old quarry from public laser-scan data." | It picks the LiDAR Survey style and builds the explainer from real scan data instead of invented imagery. |
| "Change the Ukiyo-e style into my own version." | It walks the make-your-own flow one question at a time, shows a side-by-side frame, then keeps the result in `~/lemo-my-styles/`. |
| "Start from a blank page: a chalk-on-blackboard style, warm and slow." | It picks the closest library style as a technique base, says why, and builds the new style in five steps. |
| "/lemo-opuscar:lemo-opuscar" (with nothing else) | It asks which language to use, then whether you want a library-style film, a style made your own, or a film in a saved style. |

## Verification

The raw path below returned 200 on branch main on 2026-11-27:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/lemomo-ai/lemo-opuscar/main/plugin/skills/lemo-opuscar/SKILL.md
```

After a clone, confirm the skill and its setup script are present, and that the style tree really does hold 99 styles:

```bash
git clone --depth 1 https://github.com/lemomo-ai/lemo-opuscar.git /tmp/lemo-opuscar
ls /tmp/lemo-opuscar/plugin/skills/lemo-opuscar
ls -d /tmp/lemo-opuscar/styles/*/ | wc -l
head -3 /tmp/lemo-opuscar/plugin/skills/lemo-opuscar/SKILL.md
```

The listing should show `SKILL.md` and a `scripts/` folder, the count should print 100 (99 library styles plus the `_template/` starter directory), and `head` should show the skill's `name` and `description` fields.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-27) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| lemo-opuscar | Pass | Pass | Warn |

The single Snyk warn is why this guide is yellow rather than green. This is not a Markdown-only skill: the repository ships a `core/` render toolkit, Python and Node scripts, and a `plugin/skills/lemo-opuscar/scripts/setup.sh` that installs core packages, so code does run locally when you build a film. Nothing is downloaded at skill-load time; the heavy dependencies are fetched on first film use.

The license field needs attention because GitHub reports NOASSERTION. Licensing is per-file and recorded in `REUSE.toml`: code is MIT, the Markdown docs and style prompts are CC BY-NC 4.0, and demo films, posters and stills are CC BY 4.0, with third-party assets (fonts, Poly Haven models, sample libraries, footage) keeping their own terms. Six narration tracks are excluded from the CC BY grant. Films you make with the library are yours; redistributing or repackaging the library commercially is what requires a commercial license, so read the LICENSE file before shipping the style prompts anywhere.

## Limitations

- Snapshot data, verified 2026-11-27: 5,901 combined installs across 1 indexed listing; 21,810 GitHub stars; NOASSERTION (per-file); last pushed 2026-11-26. Counts drift over time.
- The repository is roughly 3,950 files, most of them per-style demo source, assets and gallery images rather than skill logic; the skill itself is one SKILL.md plus a setup script.
- Licensing is split per file: code MIT, docs and style prompts CC BY-NC 4.0, demo films CC BY 4.0, and six voice tracks excluded from the CC BY grant. Films you make are yours, but redistributing the library itself needs care.
- Three styles (Manga Panels, Text Flash Cuts, Comic History Cartoon) draw characters with an image generator you supply; every other style works without one.
- A film takes an agent about 30-60 minutes and a fair amount of tokens, and needs Node 20+, ffmpeg 7+ and Python 3.11+.
- The single indexed listing carries a Snyk warn; re-check the skills.sh security page before production use.

## Related

- [OpenMotion - Open-Source Motion Graphics Studio Setup](/hermes/skills/catalog/nexu-io-openmotion-setup)
- [Remotion Motion Graphics Skill - Agent Video Setup](/hermes/skills/catalog/remotion-motion-graphics-skill-setup)
- [Herk Edit Kit - AI Video Editing Setup](/hermes/skills/catalog/herk-edit-kit-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install via the plugin marketplace, not a clone, so the `~/lemo-opuscar` library updates itself on the next film.
- Set effort to high in Claude Code (`/effort high`); the README says the styles are tuned for the stronger models and weaker ones may not reproduce them.
- Ask for a storyboard first on anything long; the skill stops once to show key shots before rendering the whole film.
- Say "make this style my own" early rather than tweaking per film; kept styles live in `~/lemo-my-styles/` and survive updates and uninstalls.
- Feed the evidence and data styles real material (laser scans, CAD, archive footage) instead of letting the agent invent it.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
