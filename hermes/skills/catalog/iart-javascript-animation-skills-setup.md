---
title: "iart JavaScript Animation Skills - Code-Drawn Motion"
description: "iart-ai/javascript-animation-skills: 3.6K combined installs. Two skills for films drawn frame by frame in JavaScript, music synthesized in code."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/iart-javascript-animation-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-27"
tags: ["hermes skill", "agent skill", "skill setup", "animation", "canvas", "web audio", "generative art"]
---

# iart JavaScript Animation Skills - Setup Guide

**Source:** [iart-ai/javascript-animation-skills](https://www.skills.sh/iart-ai/javascript-animation-skills) via skills.sh - 3.6K combined installs across 2 indexed listings; first documented 2026-11-27 (morning sweep)

**GitHub:** [iart-ai/javascript-animation-skills](https://github.com/iart-ai/javascript-animation-skills) - 85 stars, MIT, branch main, last pushed 2026-11-11; two skill folders under `skills/`: `javascript-animation/` (SKILL.md plus references, scripts and a starter template) and `soundtrack/` (SKILL.md plus references, a sync-check script and two music templates)

**Category:** Code-drawn animation and synthesized audio: canvas films rendered to MP4 with a self-checked soundtrack

**Quality Tier:** 🟡 Yellow - one of the two sampled listings carries a Gen Agent Trust Hub warn and the other a Snyk warn, though the repository is Markdown and JavaScript tooling with no API keys

This suite teaches an agent to make short films where every frame is drawn in JavaScript: zero image assets, zero API keys, one self-contained HTML file, and music synthesized in the same page with the Web Audio API. It is built for the kind of canvas films Claude Opus 5.5 became known for, rendered frame-accurately to MP4 and self-checked before delivery.

Two listings are indexed: javascript-animation, the film skill, and soundtrack, the music and A/V sync skill. The README documents one install route through the skills.sh CLI and a Claude Code plugin marketplace route, and notes the skills run in Claude Code, Cursor, Codex and 40+ agents.

## Installation

The skills.sh CLI route installs both skills at once:

```bash
npx skills add iart-ai/javascript-animation-skills
```

Or add it as a Claude Code plugin marketplace:

```text
/plugin marketplace add iart-ai/javascript-animation-skills
```

then `/plugin install javascript-animation-skills`.

Requirements are Node 18+, `npm i playwright-core`, ffmpeg and Chrome (or `npx playwright install chromium`). There are no API keys. A headless browser seeks the page into an MP4, and the page's Web Audio score is rendered offline to WAV and muxed in.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| javascript-animation | 1,803 | Short animated films computed on an HTML canvas: stories, explainers, loops and picture books from photos, with a drawing library, a seek-and-render harness to MP4, contact sheets and a zero-asset audit. |
| soundtrack | 1,754 | Music written in code with Web Audio for each film, rendered offline to WAV, with a tempo map that lands scene cuts on the beat and a sync check that fails the render on a missed beat or a startling loudness jump. |

All 2 indexed listings appear in the table above.

The film skill works from a beat grid, shot list and blocking written as data in the page, so the pictures, camera and soundtrack all read the same source and sound lands on every action by construction. Every frame is a pure function of time, which is what makes the render seekable and deterministic. The agent then checks its own work before you see it: a zero-asset audit, A/V sync, layout collision checks, a still per shot against the storyboard, and a director pass on a 2 fps contact sheet.

## Why This Matters for Hermes Agents

The usual way to get an agent to "make a video" is a generative model or a stock asset search, both of which are hard for an agent to control frame by frame. The technique makes the frame a pure function of time, so the agent can seek to any moment, re-render, and reason about exactly what is on screen, which is the same property that makes code preferable to a video model for anything that needs to be deterministic.

The self-check is the durable pattern. Rather than trusting the model's own judgment, the skill runs a scripted audit that fails the render on real defects: a missing asset, a cut off the beat, a text collision, a startling volume jump. Teaching an agent to gate its own output this way transfers to any deliverable, not just animation.

The two-skill split is deliberate routing. The soundtrack skill activates on "add music" and "sync the music", and holds its own sync-check script, so a film request and a music request do not blur into one skill. The README is also explicit about the model ceiling: drawing a whole film in code needs spatial reasoning, taste and a vision-capable model, and weaker models draw crudely.

## Usage

| You say | What happens |
|---|---|
| "Draw every frame of a 40-second explainer on why babies love black-and-white cards." | The film skill derives a look, writes the beat grid and shot list, then renders one HTML file to MP4. |
| "Turn these photos of my dog into a 30-second animated day-in-the-life of her." | It builds a picture-book style film from the supplied photos rather than invented frames. |
| "Add music made in code and sync it to the cuts." | The soundtrack skill writes a Web Audio score, and the tempo map lands every scene cut on a downbeat. |
| "Check the audio lines up with the picture." | The sync-check script fails the render if a cut misses the beat or the music jumps loud enough to startle. |
| "Make a wordless paper-boat story in picture-book style with a music-box soundtrack." | Both skills run together: the film skill draws, the soundtrack skill composes and syncs. |

## Verification

The raw path below returned 200 on branch main on 2026-11-27:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/iart-ai/javascript-animation-skills/main/skills/javascript-animation/SKILL.md
```

After a clone, confirm both skills and their supporting files are present:

```bash
git clone --depth 1 https://github.com/iart-ai/javascript-animation-skills.git /tmp/js-anim
ls /tmp/js-anim/skills
head -3 /tmp/js-anim/skills/javascript-animation/SKILL.md
head -3 /tmp/js-anim/skills/soundtrack/SKILL.md
```

There should be two skill directories, and each `head` should show the skill's `name` and `description` fields the runtime routes on.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-27) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| javascript-animation | Warn | Pass | Pass |
| soundtrack | Pass | Pass | Warn |

Neither listing carries a Socket fail, but the two warns across the pair are why this guide is yellow. The repository is Markdown plus a handful of JavaScript scripts: `asset-audit.mjs`, `layout-check.mjs` and `render.mjs` for the film skill and `sync-check.mjs` for the soundtrack. There is no install script, no hook and no API key; the only Node dependency the README names is playwright-core, and rendering uses a local headless browser and ffmpeg rather than any remote service.

## Limitations

- Snapshot data, verified 2026-11-27: 3,557 combined installs across 2 indexed listings; 85 GitHub stars; MIT; last pushed 2026-11-11. Counts drift over time.
- Drawing a whole film in code leans hard on the model: the README says it was built and tested with Claude Opus 5.5 and needs a vision-capable model to review its own contact sheets and stills.
- Rendering needs Node 18+, playwright-core, ffmpeg and Chrome, and the self-check needs a model that can look at images.
- The two skills are a pair, and the README positions soundtrack as a companion to javascript-animation; the film skill alone will not synthesize music.
- One listing carries a Gen Agent Trust Hub warn and the other a Snyk warn; re-check the security pages on skills.sh before production use.
- This is one pack in a 19-pack collection from iart-ai; this guide covers only javascript-animation-skills.

## Related

- [GSAP Skills - GreenSock Animation Platform Setup](/hermes/skills/catalog/greensock-gsap-skills-setup)
- [Animation Principles Skills - Motion Setup](/hermes/skills/catalog/dylantarre-animation-principles-setup)
- [Meng To Skills - Frontend & Motion Design Suite Setup](/hermes/skills/catalog/mengto-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Use the strongest vision-capable model you can; the README warns weaker models draw crudely.
- Keep both skills installed so "add music" and "sync the music" trigger the soundtrack skill instead of the film skill.
- Ask for the beat grid, shot list and blocking as data up front; the picture, camera and soundtrack all read it, so sound lands on action by construction.
- Let the self-check run before you look: the zero-asset audit and sync check fail the render on real defects rather than shipping them.
- Reuse the starter template and the two music templates (groove.js and score.js) instead of starting from a blank page.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
