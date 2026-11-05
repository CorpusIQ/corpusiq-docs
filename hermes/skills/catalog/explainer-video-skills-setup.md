---
title: "Explainer Video Skills - Script to Render Setup"
description: "iart-ai/explainer-video-skills on skills.sh: 9.6K combined installs across 5 listings; narrated explainers, wrapped recaps and animated diagrams."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/explainer-video-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "video", "animation", "motion graphics"]
---

# Explainer Video Skills - Setup Guide

**Source:** [iart-ai/explainer-video-skills](https://www.skills.sh/iart-ai/explainer-video-skills) via skills.sh - 9.6K combined installs across 5 indexed listings; first seen 2026-11-05 (Nov 5, 2026 morning sweep)
**GitHub:** 81 stars, MIT licence, last pushed 2026-06-22, five SKILL.md directories under skills/ plus a scripts/ verify-loop toolkit
**Category:** Motion graphics for agents: narrated explainers, animated diagrams, whiteboard and isometric scenes, and wrapped-style recaps
**Quality Tier:** 🟡 Beta - Snyk Warn on diagram-animation; MIT; 81 stars.

iart-ai publishes a family of open-source motion packs, 14 in the collection according to the README, and this repository is the explainer and video one. Five skills turn an idea, a data table or a written script into a paced short: `explainer-video` runs the full pipeline from script to storyboard to scene build to narration and caption sync, while the other four each own a single visual treatment.

The split is by output rather than by tool. `wrapped-video` takes one template plus a data table and produces many personalized 9:16 videos, `diagram-animation` reveals diagrams and charts over time, `whiteboard-animation` draws a hand sketching an illustration onto a board, and `isometric-animation` builds 2.5D scenes with stacked layers and extruded blocks. The README says the skills run in Claude Code, Cursor, Codex and 40+ agents, and the same repo ships a small `scripts/` toolkit so an agent can screenshot a frame and assert the encoded file's resolution, codec, fps and duration instead of eyeballing the result.

## Installation

The README installs cross-agent through skills.sh:

```bash
npx skills add iart-ai/explainer-video-skills
```

Claude Code users can add the repo as a plugin marketplace instead, since it ships a `.claude-plugin/marketplace.json`:

```bash
/plugin marketplace add iart-ai/explainer-video-skills
```

Then install the pack itself:

```bash
/plugin install explainer-video-skills
```

The README installs sibling packs from the same collection individually, for example `npx skills add iart-ai/motion-design-skills` or `npx skills add iart-ai/tiktok-video-skills`, so a project can take only the treatment it needs.

## What It Provides

Five listings, all above the threshold.

| Skill | Installs | Use For |
|---|---|---|
| explainer-video | 2,028 | Turning one message into a paced, narrated 30 to 90 second short through script, storyboard, scene build, narration and caption sync, edit and polish |
| diagram-animation | 1,973 | Revealing diagrams, flowcharts, architecture and sequence diagrams and animated charts over time, with growing bars, drawn lines and count-ups |
| whiteboard-animation | 1,912 | Draw-on VideoScribe style explainers where a hand sketches illustrations and handwriting onto a board stroke by stroke, paced to narration |
| isometric-animation | 1,910 | Isometric and 2.5D scenes: stacked layers, extruded blocks, exploded diagrams and isometric grids with staggered reveals and camera drift |
| wrapped-video | 1,792 | Spotify Wrapped style recaps: one template times a data table, producing many personalized 9:16 videos |

No indexed listings fall below the threshold; all 5 appear above.

## Why This Matters for Hermes Agents

An agent asked for a product video will usually produce a slide deck with a voiceover bolted on, because nothing in a general prompt says what an explainer actually is. `explainer-video` opens with that decision: its SKILL.md states the narrative has to be locked before any pipeline step, on the grounds that an explainer is an argument and not a feature tour, and only then does storyboarding start.

The animation skills solve a different failure. Left alone, an agent animates everything at once and the viewer retains nothing. `diagram-animation` encodes a progressive disclosure order, nodes then edges then labels, with a hold of roughly half a second to a second and a half per step, and keeps a colour-to-meaning mapping fixed for the whole piece. That is a reviewable standard rather than a taste preference.

The `scripts/` toolkit matters more than it looks. Video work fails quietly: the file exists, it plays, and it is the wrong resolution or the wrong frame rate. `probe-mp4.sh` asserts the real spec, `seek-shot.sh` freezes a moment through a page's seek harness, and `contact-sheet.sh` tiles start, mid and end into one image for a glance review. An agent that runs those three checks catches clipped text and off-canvas framing before a human has to.

Finally, the packs compose. A launch can take the narrated pipeline from `explainer-video`, a per-customer variant from `wrapped-video`, and a technical cutaway from `diagram-animation` without installing three unrelated suites.

## Usage

| You say | What happens |
|---|---|
| "Make a 60s explainer for our release tool, script and build it" | explainer-video locks a narrative, writes the script and storyboard, builds scenes and syncs narration with captions |
| "Turn this feature into a short narrated how-it-works video" | explainer-video runs the how-it-works pipeline and keeps the runtime short |
| "Build a Spotify Wrapped style year in review from this CSV" | wrapped-video maps the data table onto its template and renders one video per row |
| "Animate this architecture diagram so it reveals node by node" | diagram-animation builds a progressive reveal with flowing connectors |
| "Grow these bars and count up the numbers" | diagram-animation animates the chart with staggered entrance and count-up values |
| "Make a whiteboard video of this onboarding flow" | whiteboard-animation paces hand-drawn strokes and handwriting to the narration |
| "Build an isometric scene of our stack, layer by layer" | isometric-animation assembles extruded blocks with staggered reveals and camera drift |

## Verification

Confirm the raw skill file before installing anything, because the description is what the agent matches against:

```bash
curl -fsSL https://raw.githubusercontent.com/iart-ai/explainer-video-skills/main/skills/explainer-video/SKILL.md | head -4
```

It should open with `name: explainer-video` and a description naming explainer, storyboard and narration. After installing, check that one directory landed per skill:

```bash
ls ~/.claude/skills | grep -E 'explainer-video|wrapped-video|diagram-animation|whiteboard-animation|isometric-animation'
```

Five directories should appear. If you plan to use the verify-loop scripts, confirm the two runtime dependencies first, since `seek-shot.sh` needs Playwright Chromium and the other two need ffmpeg:

```bash
ffprobe -version | head -1
npx playwright install chromium
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| explainer-video | Pass | Pass | Pass |
| diagram-animation | Pass | Pass | Warn |
| whiteboard-animation | Pass | Pass | Pass |

The repo also carries three executable POSIX shell scripts under `scripts/`, which drive a browser through the page's seek harness and shell out to ffmpeg. Read them before running an agent unattended, and keep renders in a project directory rather than a home directory.

## Limitations

- Snapshot data, verified 2026-11-05: 9,615 combined installs across 5 indexed listings; 81 GitHub stars; MIT; last pushed 2026-06-22. Counts drift over time.
- `diagram-animation` carries a Snyk Warn. It is the skill most likely to pull in a charting or animation dependency, so review what it proposes to install.
- The skills are instruction sets, not a renderer. A finished MP4 needs a render tier in the project: standalone HTML for the light path, Remotion or Manim for the heavy one.
- The verify-loop scripts add external dependencies: Playwright Chromium for `seek-shot.sh`, and ffmpeg plus ffprobe for `contact-sheet.sh` and `probe-mp4.sh`.
- The README's iart.ai links are vendor funnel links, and the hosted agent is a separate product. The repository is MIT licensed, but the hosted service is not the same thing.
- Narration and caption sync are part of the pipeline, so a headless run needs a working text-to-speech and caption path before the explainer skill can finish a file.

## Related

- [remotion-best-practices - Video Production Setup](/hermes/skills/catalog/remotion-best-practices-setup)
- [Motion Design Skills - After Effects and Remotion Setup](/hermes/skills/catalog/motion-design-skills-setup)
- [Claude Code Video Toolkit - Video Pipeline Skills Setup](/hermes/skills/catalog/claude-code-video-toolkit-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Lock the narrative before touching a timeline. `explainer-video` does this first, and every later choice, from scene count to caption length, follows from it.
- Render one still before rendering the whole short. A contact sheet of start, mid and end catches clipped text and off-canvas elements in seconds.
- Ask for `probe-mp4.sh` to assert the spec, not just to report it. The script takes the expected resolution and fps, so a 1080x1920 vertical contract fails loudly instead of shipping sideways.
- Use `wrapped-video` only when the data actually varies per viewer. For a single recap, the same template is cheaper to run through `explainer-video`.
- Keep the animation skills apart. Asking for an isometric whiteboard diagram mixes two visual grammars, and the output reads as neither.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
