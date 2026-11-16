---
title: "Text-to-Lottie - Animation Generation Setup"
description: "diffusionstudio/lottie: 11.5K combined installs from one listing, a skill that writes production-ready Lottie JSON animations for a local Skia player."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/text-to-lottie-setup/"
robots: "index,follow"
last_updated: "2026-11-15"
tags: ["hermes skill", "agent skill", "skill setup", "lottie", "animation", "motion design"]
---

# Text-to-Lottie - Setup Guide

**Source:** [diffusionstudio/lottie](https://www.skills.sh/diffusionstudio/lottie) via skills.sh - 11.5K combined installs across 1 indexed listing; first seen Nov 14, 2026 (Nov 14 evening sweep)
**GitHub:** 5,752 stars, MIT license, `main` branch, last pushed 2026-07-25, one `SKILL.md` at `skills/text-to-lottie/SKILL.md` with eighteen reference files, four eval fixtures and a local Skia Skottie player in `src/`
**Category:** Motion design and animation generation
**Quality Tier:** 🟡 Yellow - the single sampled skill carries a Snyk Warn while the other two auditors pass.

Text-to-Lottie turns a prompt into a Lottie animation: an agent writes the JSON, and a bundled player renders it so the result can be scrubbed, inspected and corrected in the same loop. The repository comes from Diffusion Studio, the team behind a browser video editor, and the 5,752 stars put it among the larger single-skill repositories in the catalog.

The design decision worth noticing is that the skill treats the renderable scene as the deliverable, not the JSON file. The agent is told to use the official player and verify in Skia Skottie rather than hand-rolling a viewer, which removes the most common failure mode in animation work: a file that parses but does not look like what was asked for.

## Installation

Install the skill with the skills CLI:

```bash
npx skills add diffusionstudio/lottie
```

Then ask the agent to generate a Lottie animation using `text-to-lottie`. The repository sets up the workspace and the included player on first use, with each animation living as a scene inside a project directory that the player loads automatically.

There is no separate CLI install and no global service. Everything the skill needs comes from the repository it clones into the agent workspace.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| text-to-lottie | 11,490 | Authoring Lottie JSON animations: logos, typography, loaders, UI microinteractions, lower thirds, diagrams, data and stat charts, product promos, camera and scene motion. |

The single indexed listing appears in the table above.

## Why This Matters for Hermes Agents

Animation is a domain where a model can produce syntactically valid output with no taste. The reference library is how this skill handles that: `motion-taste.md` and `design-taste.md` carry the judgement that the spec alone does not, while `lottie-spec-map.md` covers the JSON structure, keyframes, slots, shapes and assets. The router table in `SKILL.md` maps an intent such as "logo animation" to the exact references to load, so a small task stays small.

The recipe set is broad and specific at the same time. There are separate references for logo, typography, lower thirds, loaders and icons, success and error states, UI microinteractions, diagrams, data and stat cards, product promos, scene and camera motion, and SVG animation. An agent asked for a spinner gets the loader recipe and the motion taste file, not the whole library.

The evaluation fixtures are the other unusual part. Four files under `skills/text-to-lottie/evals/` define trigger prompts, routing prompts, reference-loading prompts and an output rubric, which means the repository tests not only whether the skill fires but whether it loads the right references when it does. For anyone maintaining a skill library, that is a pattern worth copying.

## Usage

| You say | What happens |
|---|---|
| "Animate this SVG logo with a premium gradient" | Loads the logo recipe, design taste and motion taste, then builds the scene in the player. |
| "Make a loader for a checkout button" | Uses the loaders and icons recipe with the microinteraction guidance. |
| "Animate these quarterly numbers" | Uses the data and stats recipe to build the chart animation with readable timing. |
| "Add a lower third with the speaker name" | Uses the lower thirds recipe with typography references and taste files. |
| "The reveal feels too fast, slow it down" | Edits the existing scene in place, with the player showing the change on save. |
| "Expose the background colour as a control" | Adds slot controls, which the skill notes are not exposed by default. |
| "Why does this render black in the player?" | Walks the Skottie debugging path against `references/player-contract.md`. |

## Verification

Read the router and the player contract before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/diffusionstudio/lottie/main/skills/text-to-lottie/SKILL.md | head -40
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/diffusionstudio/lottie/main/skills/text-to-lottie/references/player-contract.md
```

The skill requires `references/player-contract.md` before any create, edit or fix operation, so a missing file is the first thing to check when a scene will not render.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-14) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| text-to-lottie | Pass | Pass | Warn |

The repository runs a local Vite player and a set of scripts inside the agent workspace. Review the scripts before pointing an agent at it in an unattended loop.

## Limitations

- Snapshot data, verified 2026-11-14: 11,490 combined installs across 1 indexed listing; 5,752 GitHub stars; MIT; last pushed 2026-07-25. Counts drift over time.
- The last push is four months before this snapshot, so the recipes track the Lottie spec as of that date rather than current Skia releases.
- One skill only: there is no separate skill for After Effects export, video encoding or 3D motion.
- Output is Lottie JSON and a local player scene. Delivery formats such as MP4 or GIF are outside the skill and need your own encoder.
- Snyk warns on the sampled skill; the other two auditors pass. Review the scripts if your policy requires a clean Snyk result.
- The player is the intended verification surface. Judging an animation from the JSON alone is the failure mode the repository explicitly argues against.

## Related

- [remotion-best-practices - Video Production Setup](/hermes/skills/catalog/remotion-best-practices-setup)
- [GSAP Skills - GreenSock Animation Platform Setup](/hermes/skills/catalog/greensock-gsap-skills-setup)
- [Animation Principles Skills - Motion Setup](/hermes/skills/catalog/dylantarre-animation-principles-setup)
- [Petdex - Animated Mascots for Hermes Agent](/hermes/skills/catalog/petdex-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Ground the prompt in real assets. The repository's own prompt guide says results improve sharply when the animation is based on a supplied SVG, screenshot or dataset.
- Use motion design vocabulary in the request, such as ease-in and ease-in-out, rather than "make it smooth".
- Ask for specific controls. Only a background colour control is exposed by default, so other properties need to be requested explicitly.
- State the frame rate and total frame count when the animation has to fit a fixed duration.
- Camera language works: pushes, pans and zooms are documented prompt patterns that change the output noticeably.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
