---
title: "WeChat Skyline Skills - Mini Program Rendering Setup"
description: "wechat-miniprogram/skyline-skills - 7.6K combined installs: WeChat Skyline rendering engine agent skills for Mini Program development."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/wechat-skyline-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-24"
tags: ["hermes skill", "agent skill", "skill setup", "wechat", "skyline", "miniprogram"]
---

# WeChat Skyline Skills - Mini Program Rendering Setup

**Source:** [wechat-miniprogram/skyline-skills](https://www.skills.sh/wechat-miniprogram/skyline-skills) via skills.sh - 7.6K combined installs across 7 indexed listings; first catalogued Nov 24, 2026 (Nov 24, 2026 evening sweep)
**GitHub:** [wechat-miniprogram/skyline-skills](https://github.com/wechat-miniprogram/skyline-skills) - 57 stars, MIT license, master branch, last pushed Nov 18, 2026; the seven skills live under skills/ with per-topic references/ directories.
**Category:** WeChat Mini Program Development (Skyline Rendering)
**Quality Tier:** 🟢 Green - all 7 sampled skills pass the Gen Agent Trust Hub, Socket and Snyk checks.

wechat-miniprogram/skyline-skills is WeChat's official agent-skill suite for Skyline, the rendering engine behind WeChat Mini Programs. It packages the Skyline documentation into seven skills covering overview and migration, JSON configuration, components, WXSS style support, the worklet animation system, custom routing and page transitions, and the scroll control APIs. skills.sh indexes 7 listings at 7.6K combined installs.

The README and every skill body are written in Chinese; the commands below are quoted verbatim and not translated. Each skill is a thin SKILL.md that points into a references/ directory organized by topic (api, animation, base, core, tool and migration), so the reference files are the real payload.

## Installation

The README is Chinese-language and documents adding the skills with npx:

```bash
npx skills add wechat-miniprogram/skyline-skills
```

Updating to the latest version:

```bash
npx skills update wechat-miniprogram/skyline-skills
```

## What It Provides

Use For cells are condensed from the skills' own Chinese-language SKILL.md descriptions.

| Skill | Installs | Use For |
|---|---|---|
| skyline-components | 1,147 | developing scroll lists, swipers, forms, image/text and share-element components |
| skyline-overview | 1,146 | understanding Skyline architecture, performance and migration |
| skyline-worklet | 1,118 | high-performance worklet animations with SharedValue and timing/spring/decay |
| skyline-route | 1,070 | custom routes, page transitions, half-screen popups and back gestures |
| skyline-config | 1,052 | configuring app.json, page json and project.config.json for Skyline |
| skyline-wxss | 1,037 | querying CSS property support and style compatibility |
| skyline-scroll-api | 989 | programmatic scrolling and refresh via ScrollViewContext and DraggableSheetContext |

All 7 indexed listings clear the 500-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

Skyline Skills is a documentation-as-skills reference: WeChat converted its Skyline docs into seven narrowly scoped skills, each a short SKILL.md pointing at topic-organized reference files. That structure is worth copying when turning an existing docs site into agent skills, since it keeps each SKILL.md loadable and leaves the detail in the references. The worklet skill mirrors the Reanimated model of SharedValue plus timing/spring/decay with runOnUI/runOnJS thread hops, a clean example of exposing a native animation system to an agent. The route skill enumerates the seven preset wx:// route types and custom routeBuilder transitions, useful for mapping platform constraints into agent instructions. All seven sampled skills pass the skills.sh security checks, so this suite is a safe, dependency-free way to bring Skyline knowledge into a Hermes agent that works on WeChat Mini Programs.

## Usage

| You say | What happens |
|---|---|
| Migrate my mini program to Skyline | Uses skyline-overview to guide architecture and migration |
| Configure app.json for Skyline rendering | Uses skyline-config for renderer and page JSON config |
| Build a scroll list with a swiper | Uses skyline-components for scroll-view, swiper and form components |
| Animate a drag with spring physics | Uses skyline-worklet for SharedValue and timing/spring animations |
| Add a half-screen popup transition | Uses skyline-route for custom routes and page transitions |
| Check whether a CSS property is supported | Uses skyline-wxss for style compatibility |
| Programmatically trigger pull-to-refresh | Uses skyline-scroll-api for ScrollViewContext refresh |

## Verification

Confirm the README resolves on the master branch:

```bash
curl -sL https://raw.githubusercontent.com/wechat-miniprogram/skyline-skills/master/README.md | head -40
```

Review a representative skill body before installing:

```bash
curl -sL https://raw.githubusercontent.com/wechat-miniprogram/skyline-skills/master/skills/skyline-components/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| skyline-components | Pass | Pass | Pass |
| skyline-overview | Pass | Pass | Pass |
| skyline-worklet | Pass | Pass | Pass |
| skyline-route | Pass | Pass | Pass |
| skyline-config | Pass | Pass | Pass |
| skyline-wxss | Pass | Pass | Pass |
| skyline-scroll-api | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 24, 2026: 7,559 combined installs across 7 indexed listings; 57 GitHub stars; MIT license; last pushed Nov 18, 2026. Counts drift over time.
- The README and all skill bodies are written in Chinese; the install commands are quoted verbatim, but the surrounding documentation is Chinese-only.
- The skills carry no executable tooling; they are reference documentation packaged as skills, so every Use For cell describes guidance rather than scripts.
- The seven listings all have matching directories in the current tree; no index-versus-tree drift.

## Related

- [WeChat Pay Skills - Chinese Payments](/hermes/skills/catalog/wechatpay-skills-setup)
- [Vercel Agent Skills - Official Vercel Collection Setup](/hermes/skills/catalog/vercel-agent-skills-setup)
- [Three.js Agent Skills - 3D & WebGL Suite Setup](/hermes/skills/catalog/threejs-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Read the README and skill bodies with a translation tool first; they are Chinese-language.
- Run skyline-overview before committing to a migration so the agent evaluates migration cost up front.
- Use npx skills update wechat-miniprogram/skyline-skills to pull the latest reference docs.
- Treat references/ as the real payload; the SKILL.md files are thin pointers into it.
- Ask for a CSS compatibility check through skyline-wxss rather than assuming web CSS works unchanged.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
