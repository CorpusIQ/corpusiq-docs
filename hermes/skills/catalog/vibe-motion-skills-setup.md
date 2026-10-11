---
title: "Vibe Motion Skills - SVG & Motion Renders Setup"
description: "Setup guide for vibe-motion/skills - 8.3K combined installs. 16 motion and animation skills: SVG, Remotion renders, brand launch videos."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/vibe-motion-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "motion", "animation", "remotion"]
---

# Vibe Motion Skills - Setup Guide

**Source:** [vibe-motion/skills](https://www.skills.sh/vibe-motion/skills) via skills.sh - 8.3K combined installs across 16 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [vibe-motion/skills](https://github.com/vibe-motion/skills) (1,339 stars, NO LICENSE FILE; pushed 2026-10-05; `<name>/SKILL.md` at the repo root, 16 skill dirs)
**Category:** Motion / Animation / Video Renders
**Quality Tier:** 🔵 Community - 1,339-star repo; README marks it no longer maintained (points to motionface.cc); NO LICENSE file; mixed sampled verdicts

This collection packages 16 motion and animation skills behind one install: SVG animators, Remotion renders (photo tickers, financial candlesticks, chat motion), procedural and 3D effects, and a brand launch video pipeline. Each skill lives in its own directory as `<name>/SKILL.md` at the repo root, and the installer is interactive: pick skills with the space bar, choose your agent (for example Claude Code), and the CLI drops them into the right path.

Two facts change the calculus before you install. First, the README (in Chinese) marks the project as no longer maintained and points readers to motionface.cc, so treat this as a frozen artifact rather than an evolving library. Second, the top indexed listing, svg-assembly-animator at 1,124 installs, was removed from the repository on Sep 4, 2026 (commit "delete svg-assembly-animator") and has no counterpart in the current tree, so its install count is historical and does not resolve to a skill you can install today.

---

## Installation

Prerequisites: Node.js for the `npx` skills CLI, and an agent such as Claude Code that loads skills.

```bash
npx skills add vibe-motion/skills
```

The installer is interactive: select skills with the space bar (the README suggests installing all of them) and remember to pick your target agent, because different agents use different skill directories.

## What It Provides

Install counts from the Oct 10, 2026 skills.sh snapshot:

| Skill | Installs | Use For |
|---|---|---|
| svg-assembly-animator | 1,124 | SVG assembly build-up animation render; removed from the repository on Sep 4, 2026, with no counterpart in the current tree |
| claude-typer | 1,051 | Turns prompt text into a Claude Code CLI style typing animation demo |
| procedural-fish-render | 978 | Looping procedurally animated fish render |
| ruler-progress-render | 901 | Ruler-style progress animation with configurable text and progress |
| light-spotlight-render | 789 | Swinging spotlight reveal animation over text (HTML) with configurable text, swing width, lamp scale, glow, and background color |
| remotion-3d-ticker | 788 | Remotion-based infinite-loop 3D photo ticker wall; configurable image columns, scroll direction, and speed |
| wechat-2d-render | 769 | WeChat-style 2D chat motion video: chat animation, message bubbles, transparent-background Remotion export |
| threejs-earth-render | 603 | Three.js 3D earth with flight-route animation rendered via Puppeteer; 16:9 GIF/MP4 export |
| disney-animation-rule-skill | 531 | Applies Disney's 12 principles of animation to code-driven motion (Web, SVG, Canvas, React, Remotion, UI, 3D scenes) |

The remaining 7 indexed listings range from 1 to 224 installs.

## Why This Matters for Hermes Agents

Motion work used to mean a designer in After Effects; these skills hand the same jobs to a coding agent, which matters most for deliverables whose inputs an agent can already see: an SVG animation for a landing page, a Remotion ticker or candlestick chart for a dashboard demo, a chat render for a product video. Each skill is self-contained, so a Hermes agent can pull one in for a single render without adopting a framework. The disney-animation-rule-skill is the useful odd one out: it is a review lens for any code-driven animation, including ones an agent just wrote, which turns it into a quality gate rather than a generator. The maintenance reality cuts the other way though: the README says the project is no longer maintained, and several skills clone or update companion repositories at run time (threejs-earth-render, wechat-2d-render, 3d-chladni-render), so reproducible renders mean pinning and testing rather than trusting a floating clone. There is also no license file, so clear terms with the publisher before commercial use.

## Usage

| You say | What happens |
|---|---|
| "Make a typing animation of this prompt for the launch post" | claude-typer converts the text into a Claude Code CLI style typing demo |
| "Generate a looping fish animation for the loading screen" | procedural-fish-render produces the looping procedural fish motion |
| "I need a ruler-style progress animation with custom labels" | ruler-progress-render builds it with configurable text and progress |
| "Spin up a 3D photo ticker wall for the demo video" | remotion-3d-ticker renders the infinite-loop wall with configurable columns, direction, and speed |
| "Render a chat animation with message bubbles" | wechat-2d-render renders the WeChat-style 2D chat motion with a transparent-background export |
| "Give me a rotating earth with flight routes for the deck" | threejs-earth-render clones the companion project and renders the 16:9 earth flyover |
| "This animation feels stiff; what is wrong with it?" | disney-animation-rule-skill reviews the code-driven motion against Disney's 12 principles |

## Verification

```bash
# Confirm the install through the skills CLI
npx skills list | grep -iE 'claude-typer|disney'

# Or check the skills directory your agent scans
ls ~/.claude/skills/ | grep -E 'claude-typer|procedural-fish-render|threejs-earth-render'

# Review a current skill straight from GitHub before installing
curl -sL https://raw.githubusercontent.com/vibe-motion/skills/main/disney-animation-rule-skill/SKILL.md | head -20
```

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| svg-assembly-animator | Pass | Pass | Warn |
| disney-animation-rule-skill | Pass | Pass | Pass |
| motion | - | - | - |

The scored sample is mixed: disney-animation-rule-skill passes all three engines, while svg-assembly-animator carries a Snyk Warn (and is no longer in the repo). Most of the catalog was not sampled, so re-check the security pages on skills.sh before production use.

## Limitations

- No LICENSE file, so default all-rights-reserved terms apply; clear usage terms with the publisher before commercial use.
- The README (in Chinese) marks the project as no longer maintained and points readers to motionface.cc.
- The top listing, svg-assembly-animator (1,124 installs), was deleted from the repository on Sep 4, 2026 and has no counterpart in the current tree; its count is historical.
- Mixed verdicts: a Snyk Warn on the svg-assembly-animator sample; most listings are unscored.
- Several skills clone or update companion repositories at run time; pin and test before relying on reproducibility.
- Snapshot data, verified Oct 10, 2026: 8,311 combined installs across 16 indexed listings; 1,339 GitHub stars; NO LICENSE FILE; last pushed 2026-10-05. Counts drift over time.

## Related

- [remotion-best-practices - Video Production Setup](/hermes/skills/catalog/remotion-best-practices-setup) - deeper Remotion engineering patterns for the render skills
- [Design Motion Principles Skill - Motion & Interaction Setup](/hermes/skills/catalog/design-motion-principles-skill-setup) - motion principles for interaction design
- [Motion Design Skill - LottieFiles Animation Setup](/hermes/skills/catalog/lottiefiles-motion-design-skill-setup) - a Lottie-based alternative for UI motion
- [GSAP Skills - GreenSock Animation Platform Setup](/hermes/skills/catalog/greensock-gsap-skills-setup) - web animation with GSAP
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Treat the repo as frozen: since it is no longer maintained, pin the commit you test instead of expecting upstream updates.
- The installer is interactive; select your agent explicitly or the skills land in the wrong directory for your terminal.
- Do not script an install around the top listing before checking it; svg-assembly-animator no longer exists in the current tree.
- Pair generation with review: render first, then run disney-animation-rule-skill over the result as a quality gate.
- Companion-repo skills clone or update their source projects at run time; install them once and cache the clones for repeatable offline renders.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
