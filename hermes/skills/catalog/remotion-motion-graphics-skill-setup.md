---
title: "Remotion Motion Graphics Skill - Agent Video Setup"
description: "liamrjohnston/remotion-motion-graphics-skill - 8.2K combined installs: four Remotion motion-graphics skills for cinematic camera and terminal inserts."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/remotion-motion-graphics-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "remotion", "motion graphics", "video"]
---

# Remotion Motion Graphics Skill - Setup Guide

**Source:** [liamrjohnston/remotion-motion-graphics-skill](https://www.skills.sh/liamrjohnston/remotion-motion-graphics-skill) via skills.sh - 8.2K combined installs across 4 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 morning sweep)
**GitHub:** [liamrjohnston/remotion-motion-graphics-skill](https://github.com/liamrjohnston/remotion-motion-graphics-skill) - 182 stars, MIT license, last pushed Jul 24, 2026, main branch; four skills under skills/<name>/SKILL.md.
**Category:** Motion Graphics (Remotion)
**Quality Tier:** 🟡 Yellow - all 4 listings sampled: three pass all three checks, and motion-graphics carries a Snyk Warn.

This is a motion-graphics skill set for Remotion, distinct from the framework skill sets already catalogued under Remotion Framework Skills and Remotion Best Practices. Rather than teaching the Remotion API itself, it teaches an AI coding agent to produce broadcast-quality motion graphics: a continuous-scene cinematic camera rig, editorial article highlights, and authentic terminal inserts, all gated by a mandatory format and background intake and a repository-wide zero-neon policy.

The four skills were developed in production at Promptible, where every example clip was built entirely by an AI agent following these instructions. The motion-graphics skill is the enforced production gate: before code, scripts/promptible-gate.mjs validates research sources, hashes bundled logos and approved references, and issues a BUILD AUTHORIZED verdict; after rendering, an independent critic must score the candidate before DELIVERY AUTHORIZED. All 4 indexed listings have a matching skills/<name>/SKILL.md in the current tree on the main branch.

## Installation

The README offers two paths. The one-command installer scaffolds a fresh Remotion project and installs the skills, or skips scaffolding when run inside an existing project:

```bash
curl -fsSL https://raw.githubusercontent.com/liamrjohnston/remotion-motion-graphics-skill/main/install.sh | bash
```

To add just the skills to an existing project, use the skills CLI:

```bash
npx skills add liamrjohnston/remotion-motion-graphics-skill
```

Variants include a global install (-g), a single agent (-a claude-code), or a single skill (--skill cinematic-camera). Update with npx skills update -y. The recommended companion is the official Remotion skill for API correctness: npx skills add remotion-dev/skills.

## What It Provides

skills.sh publishes per-skill install counts for all 4 indexed listings.

| Skill | Installs | Use For |
|---|---|---|
| cinematic-camera | 2,264 | build a continuous-scene Remotion camera system with a keyframed rig, reference review, and first-pass QA |
| motion-graphics | 2,213 | run the production gate: cached official-asset research, reference selection, art direction, and build authorization |
| article-highlights | 1,898 | build editorial article inserts with layered highlighter strokes, zero neon/glow, and mobile QA |
| terminal-inserts | 1,855 | render authentic, restrained terminal demos with real CLI symbols, zero neon or glow, and 3D window motion |

All 4 indexed listings clear the 1,800-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

Most motion-graphics guidance tells an agent what looks good; this skill set encodes a fail-closed pipeline the agent must walk. The agent asks the delivery format and background surface before writing code, researches only the named products and surfaces, reuses cached work, builds one continuous scene, and submits rendered evidence to an independent critic. A failed or incomplete gate cannot be delivered, which turns taste into an executable check an agent cannot skim. The cinematic-camera skill replaces panels popping in and out of a void with a single keyframed camera rig, and terminal-inserts bans the fake terminal chrome (checkbox UI, status chips, dashboard cards) that marks AI-generated demo videos. The zero-neon policy and the never-restate-the-voiceover rule are hard constraints a Hermes agent can carry into any video task, not just Remotion work.

## Usage

| You say | What happens |
|---|---|
| Make a 6-second vertical clip for this script line | Uses motion-graphics and cinematic-camera to run intake, research assets, build the scene, and render QA evidence |
| Add a product demo terminal to my video | Uses terminal-inserts to render authentic CLI output with real symbols and 3D window motion |
| Turn this news item into a highlight card | Uses article-highlights to build a layered editorial card with highlighter strokes and blur-in |
| Build a cinematic camera move over my app | Uses cinematic-camera to keyframe one continuous scene and drive the camera through it |
| Check my render before I ship it | Uses the motion-graphics gate to hash the MP4, contact sheet, and probe evidence for critic review |

## Verification

Confirm the README and representative skill bodies resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/liamrjohnston/remotion-motion-graphics-skill/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/liamrjohnston/remotion-motion-graphics-skill/main/skills/motion-graphics/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/liamrjohnston/remotion-motion-graphics-skill/main/skills/cinematic-camera/SKILL.md | head -40
```

All three URLs return 200. After installing, review each skills/<name>/SKILL.md before relying on it, and re-check the security pages on skills.sh for the Warn verdict noted below.

## Security

skills.sh verdicts for sampled skills (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| cinematic-camera | Pass | Pass | Pass |
| motion-graphics | Pass | Pass | Warn |
| article-highlights | Pass | Pass | Pass |
| terminal-inserts | Pass | Pass | Pass |

Across the 4 sampled skills there are 11 Pass, 1 Warn, and 0 Fail cells. Three skills pass all three checks; motion-graphics carries the single Warn (Snyk).

## Limitations

- Snapshot data, verified Nov 26, 2026: 8,230 combined installs across 4 indexed listings; 182 GitHub stars; MIT license; last pushed Jul 24, 2026. Counts drift over time.
- skills.sh sampled all 4 indexed listings, so every row has a published verdict, but four skills is a small sample for a production pipeline; re-check before relying on it.
- The example MP4s and GIFs in examples/ and previews/ are demonstration assets, and the product names and logos they show belong to their respective owners.
- These skills assume a Remotion project and pair with the official Remotion skill (remotion-dev/skills) for API correctness; this repo supplies taste and choreography, not the framework itself.

## Related

[Remotion Best Practices - Video Production Setup](/hermes/skills/catalog/remotion-best-practices-setup) | [Remotion Framework Skills - Programmatic Video Setup](/hermes/skills/catalog/remotion-framework-skills-setup) | [Hyperframes Setup](/hermes/skills/catalog/hyperframes-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run the one-command installer inside an existing Remotion project to skip scaffolding and only add the skills.
- Always pair with the official Remotion skill (npx skills add remotion-dev/skills) for API correctness; this skill set adds taste and choreography on top.
- The gate script (scripts/promptible-gate.mjs) hashes bundled logos and approved references by SHA-256, so rely on it for reproducible review rather than eyeballing.
- Study docs/prompt-threads.md for real request-to-revision threads before prompting your own agent.
- Never restate the voiceover on screen: the skills treat real data (counters, dollars, UI text, code) as the only text worth rendering.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
