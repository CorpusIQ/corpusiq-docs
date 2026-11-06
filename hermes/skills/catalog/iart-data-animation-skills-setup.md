---
title: "Data Animation Skills - Charts That Move"
description: "iart-ai/data-animation-skills on skills.sh: 5.1K combined installs, 3 listings; Remotion skills for bar chart races, infographics and deck videos."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/iart-data-animation-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "data visualization", "remotion", "video"]
---

# Data Animation Skills - Setup Guide

**Source:** [iart-ai/data-animation-skills](https://www.skills.sh/iart-ai/data-animation-skills) via skills.sh - 5.1K combined installs across 3 indexed listings; first seen 2026-11-06 (Nov 6, 2026 morning sweep)
**GitHub:** 17 stars, MIT licence filed at the repository root, last pushed 2026-06-22, three SKILL.md directories under skills/ (one per indexed listing), plus a .claude-plugin manifest at the root
**Category:** Data video for agents: animated charts, bar chart races, count-up tickers and presentation cuts from a CSV
**Quality Tier:** 🟢 Green - MIT licence, every sampled skill passes Gen Agent Trust Hub, Socket and Snyk, and all three indexed listings have a matching SKILL.md directory in the current tree.

Data Animation Skills is iart.ai's open-source pack for turning a dataset into a video instead of a static chart. Three skills share one pipeline: a Remotion composition is written per scene, every displayed value is computed from the current frame, individual frames are rendered as stills and inspected, and only then is the MP4 encoded. The README states the goal plainly, a chart that moves "with exact, accurate numbers on every frame". The README also says the skills run in Claude Code, Cursor, Codex and 40+ agents, and this pack is one of a 14-pack collection from the same publisher that includes tiktok-video-skills, map-animation-skills and manim-skills.

The three skills split by output shape rather than by chart type. `chart-animation` covers charts that are the content: bar chart races, line and area reveals, count-up tickers, and one template rendered across many CSVs. `animated-infographic` covers a designed scene, icons plus a few key numbers plus connectors, revealed in a staggered cascade. `presentation-video` rebuilds a deck as narrated, auto-advancing slides. They cross-reference each other, and the infographic skill tells the agent to compose a chart from `chart-animation` as one block rather than rebuilding it.

## Installation

The README installs all three skills with the Agent Skills CLI:

```bash
npx skills add iart-ai/data-animation-skills
```

Or as a Claude Code plugin marketplace entry:

```bash
/plugin marketplace add iart-ai/data-animation-skills
/plugin install data-animation-skills
```

Installation only delivers the instructions. Rendering needs a Remotion project, and the skills drive it from the shell. `chart-animation` documents the render-and-inspect loop it expects the agent to follow:

```bash
npx remotion compositions
npx remotion still Race out/f-mid.png --frame=90 --props='{"data":[...]}'
npx remotion render Race out/race.mp4 --props='{"data":[...]}'
```

The repository also ships a verification toolkit in its root `scripts/` folder, and each SKILL.md points at it: `contact-sheet.sh` tiles frames into one sheet for review, and `probe-mp4.sh` asserts the encoded file's resolution, codec, frame rate and duration. Both sit outside the skill directories, so clone the repository if you want them alongside the skills.

## What It Provides

The three counts sit close together, which suggests the pack is usually installed as a set rather than skill by skill.

| Skill | Installs | Use For |
|---|---|---|
| chart-animation | 1,735 | Bar chart races, line and area reveals, count-up tickers, rank transitions, pacing and one template rendered across many CSVs |
| animated-infographic | 1,728 | Designed infographics: layout and hierarchy, staggered icon and stat reveals, key-number counters, connectors and section pacing |
| presentation-video | 1,662 | Rebuilding a deck or outline as narrated slides with staggered builds, transitions and timing locked to per-slide audio |

All three indexed listings clear the 500-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

Animated data video is a task where a competent agent produces something that renders and is still wrong. Bar heights that come from a CSS transition or a D3 transition desync from the renderer's clock, so the encoded video flickers or lands on values that were never in the data. The first rule in `chart-animation` addresses exactly that: every value must be a pure function of the current frame, never of wall-clock time or a library's animation loop.

The second failure mode is the number itself. A count-up that formats `1287.4013` or a label that shifts width as digits change looks broken on screen, and the skill is specific about the fix: round before formatting, format with `Intl.NumberFormat`, and set `tabular-nums` so the digit box stays fixed.

The third is pacing. The skills budget time per data event rather than per second of polish, and they insist on visible value labels, a time indicator and axis units rendered once. That is the difference between a chart that moves and a chart a viewer can read.

The verification loop is the most useful part for an agent operating without a human watching the screen. Because Remotion is frame-deterministic, the agent can render three stills, inspect the values and layout, and only then pay for the encode. One bad dataset caught at the still stage beats fifty broken MP4s found later.

Finally, the pack is small and legible. Three skills, each a single SKILL.md plus references and scripts, is a surface a Hermes agent can load in full, and the batch case (one template, many datasets) is written as a first-class workflow rather than an afterthought.

## Usage

| You say | What happens |
|---|---|
| "Turn this CSV of market share into a bar chart race" | `chart-animation` interpolates between sparse rows, ranks items per frame and animates bars to their new positions |
| "Animate a count-up from 0 to 1,287" | `chart-animation` interpolates the number, rounds and formats it with a thousands separator, and fixes the digit box |
| "Make a how-it-works infographic with 3 steps" | `animated-infographic` designs the static layout first, then staggers icons, labels and connectors |
| "Convert this pitch deck into a narrated video" | `presentation-video` rebuilds each slide as motion graphics, sets durations from the audio length and auto-advances |
| "Render this template for every file in /data" | `chart-animation` treats the dataset as a prop and loops the render over each file, checking one representative first |
| "The numbers look wrong at the end" | The agent renders the last frame as a still, compares it against the source data, then re-encodes |
| "Give me a GIF for the README" | `animated-infographic` renders the composition with `--codec=gif` after the MP4 checks pass |

## Verification

Fetch the skill index before installing. Both probes read the repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/iart-ai/data-animation-skills/main/skills/chart-animation/SKILL.md | head -5
curl -fsSL https://raw.githubusercontent.com/iart-ai/data-animation-skills/main/skills/presentation-video/SKILL.md | head -5
```

The first should open with `name: chart-animation` and a description naming bar chart races, CSV to video and batch template output. The second should open with `name: presentation-video` and a description naming narrated, auto-advancing slides.

Then confirm the three skills landed with their reference files:

```bash
ls ~/.claude/skills/chart-animation ~/.claude/skills/animated-infographic ~/.claude/skills/presentation-video
ls ~/.claude/skills/chart-animation/references
```

Each skill directory should hold `SKILL.md`, and `chart-animation` should carry `references/bar-chart-race.md`. The helper scripts are not in the skill directories; they live in the repository root `scripts/` folder, which a skill-only install does not include.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| chart-animation | Pass | Pass | Pass |
| animated-infographic | Pass | Pass | Pass |
| presentation-video | Pass | Pass | Pass |

A clean sample is not a clean supply chain. These skills instruct the agent to run `npx remotion` commands, which pull the Remotion toolchain and its dependencies into the project, the render step executes project code, and the bundled shell helpers execute whatever the shell passes them. Read `scripts/contact-sheet.sh` and `scripts/probe-mp4.sh` from the repository before the first run, and pin the Remotion version in the project rather than letting `npx` resolve the latest on every call.

## Limitations

- Snapshot data, verified 2026-11-06: 5,125 combined installs across 3 indexed listings; 17 GitHub stars; MIT; last pushed 2026-06-22. Counts drift over time.
- This is a video pipeline, not a chart library. Output is an MP4 plus the Remotion project; single frames are exported only to check the work, not as a delivery format.
- Remotion is the only renderer the skills describe. They assume a TypeScript Remotion project with compositions, a zod schema and default props, so a team on After Effects, Manim or plain ffmpeg gets guidance it cannot use without translation.
- The skills name Remotion APIs (`useCurrentFrame`, `spring`, `TransitionSeries`) without stating a version, and the repository was last pushed in June 2026, so a later Remotion release can break an example without warning.
- Narration in `presentation-video` is timing, not synthesis. The skill sets slide durations from audio length; it does not generate the voiceover, so you bring the audio.
- The helper scripts are outside the skills. `contact-sheet.sh` and `probe-mp4.sh` live in the repository root `scripts/` directory, so an install that copies only the skill directories leaves them behind; clone the repository to use the documented verification loop as written.

## Related

- [AntV Chart Visualization Skills - Data to Charts](/hermes/skills/catalog/antvis-chart-visualization-setup)
- [IART Web Animation Skills - GSAP and SVG Suite](/hermes/skills/catalog/iart-web-animation-skills-setup)
- [Motion Design Skills - After Effects and Remotion Setup](/hermes/skills/catalog/motion-design-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Ask for the stills before the video. "Render frames 0, 90 and 149 as PNGs and check the values against the CSV" is the cheapest way to catch a wrong digit.
- Say "bar chart race from this CSV" rather than "animated chart". The activation phrasing in the README is specific, and the skill routes on it.
- Keep the dataset as a prop from the start. Hardcoding values into the composition is what makes the batch case collapse on the second file.
- Use `animated-infographic` for the wrapper and `chart-animation` for the chart inside it. Rebuilding a race inside the infographic skill duplicates work the other skill already does correctly.
- Read `references/bar-chart-race.md` before editing a race. It is a complete component, and the rank interpolation is the part most hand edits break.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
