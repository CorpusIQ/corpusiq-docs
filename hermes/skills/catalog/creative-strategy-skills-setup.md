---
title: "Creative Strategy Skills - Paid Social Ads Suite Setup"
description: "motion-team/creative-strategy-skills: 4.4K combined installs across 8 indexed listings; paid social creative strategy skills for hooks and ad copy."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/creative-strategy-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-18"
tags: ["hermes skill", "agent skill", "skill setup", "creative strategy", "paid social", "ad copywriting"]
---

# Creative Strategy Skills - Setup Guide

**Source:** [motion-team/creative-strategy-skills](https://www.skills.sh/motion-team/creative-strategy-skills) via skills.sh - 4.4K combined installs across 8 indexed listings; first seen Nov 18, 2026 (this sweep)
**GitHub:** 200 stars, MIT license, `main` branch, last pushed 2026-06-11. The eight skills each live in a top-level directory with its own SKILL.md, alongside brand logos and inspiration assets.
**Category:** Paid social creative strategy / ad copywriting
**Quality Tier:** 🟡 Yellow - 23 Pass and 1 Warn across the 24 sampled verdict cells; MIT licence.

Creative Strategy Skills is the paid social creative strategy suite built by Alysha, Creative Strategy Lead at Motion. The eight skills encode her workflow from brand context through review mining, messaging angles, ad concepts, visual formats, and hook writing. Install once and talk to your agent normally; the skills activate when a request matches what they do.

## Installation

Open a terminal wherever you use skills and run:

```bash
npx skills add alyshafrommotion/creative-strategy-skills
```

That is it; the skills are available in every conversation with no configuration. The README's install command uses the alyshafrommotion handle, while the repository and its skills.sh page live under motion-team; both refer to the same skill set. If you are unsure it worked, ask the agent: "What creative-strategy skills do I have installed?"

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| hook-writing | 675 | Writes high-converting, psychologically driven hooks and opening lines for paid ads and social content. |
| creative-strategy-engine | 579 | Maps pain/persona intersections and messaging angles across awareness stages to structure creative strategy. |
| creative-mechanics | 578 | Provides structural patterns that define how an ad constructs meaning between its hook, visuals, and narrative. |
| hook-tactics | 535 | Reference library of 35+ hook and headline tactic types with guidance on when to deploy each. |
| visual-formats | 534 | Reference library of 45+ visual ad formats for Meta and paid social with funnel stage and medium guidance. |
| review-audit | 512 | Analyzes positive customer reviews to surface pain points, triggers, objections, transformations, and standout language. |
| brand-intake | 506 | Runs a structured brand intake interview plus web research to build a brand context document before downstream work. |

The remaining 1 indexed listing is hook-voice-patterns (497 installs).

## Why This Matters for Hermes Agents

The suite encodes a complete creative workflow, not a grab bag of prompts. brand-intake builds a brand context document before anything else runs, review-audit mines real customer language, creative-strategy-engine maps pain and persona intersections into messaging angles, and the execution skills turn those angles into ad concepts, visual formats, and hooks. For a Hermes agent this means ad copy is grounded in a brand's actual customer voice and a documented funnel structure rather than generic, ad-libbed phrasing. The skills are guidance-only: they produce copy and concepts, not finished assets or ad account changes.

## Usage

| You say | What happens |
|---|---|
| "Run brand intake for a new client" | brand-intake runs a structured intake interview, then web research, and builds a brand context document. |
| "Analyze these customer reviews" | review-audit surfaces pain points, triggers, objections, transformations, and standout language from the reviews. |
| "Map my creative strategy for a supplement brand" | creative-strategy-engine maps pain/persona intersections and messaging angles across awareness stages. |
| "Write 10 hooks for my fitness app aimed at women 25 to 35" | hook-writing produces psychologically driven hooks tailored to product, persona, and awareness stage. |
| "Give me hooks organized by tactic" | hook-tactics returns hooks classified into its 35+ tactic types. |
| "Turn this hook into a full ad concept" | creative-mechanics pairs the hook with a structural pattern that defines the ad's meaning. |
| "What format should this ad be?" | visual-formats recommends a visual format with funnel stage and medium. |

## Verification

Install once, then confirm the repository is reachable and the skills are present:

```bash
npx skills add alyshafrommotion/creative-strategy-skills
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/motion-team/creative-strategy-skills/main/hook-writing/SKILL.md
```

To confirm the install worked, ask the agent: "What creative-strategy skills do I have installed?"

## Security

skills.sh verdicts for sampled skills (verified Nov 18, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| hook-writing | Pass | Pass | Pass |
| creative-strategy-engine | Pass | Pass | Pass |
| creative-mechanics | Pass | Pass | Pass |
| hook-tactics | Pass | Pass | Pass |
| visual-formats | Pass | Pass | Pass |
| review-audit | Pass | Pass | Pass |
| brand-intake | Pass | Pass | Warn |
| hook-voice-patterns | Pass | Pass | Pass |

The sample covers all 8 indexed listings; the single Warn is a Snyk flag on brand-intake, and every other cell is a Pass.

## Limitations

- Snapshot data, verified Nov 18, 2026: 4,416 combined installs across 8 indexed listings; 200 GitHub stars; MIT license; last pushed 2026-06-11. Counts drift over time.
- The README's install command uses the alyshafrommotion handle, while the repository and its skills.sh page live under motion-team; the two spellings are worth checking before scripting an install.
- hook-voice-patterns sits just below the 500-install cut at 497 installs, so it is not shown in the table above but installs normally with the rest.
- The suite is the work of a single author (Alysha, Creative Strategy Lead at Motion) and provides creative guidance only; it produces no finished ad assets and connects to no ad platform.
- brand-intake conducts web research to build the brand context document, so it reaches the network; the other skills work on the text you supply.

## Related

- [Marketing Skills - Content Ops Setup](/hermes/skills/catalog/zc277584121-marketing-skills-setup)
- [Kostja94 Marketing Skills - Copywriting, SEO, Ads Setup](/hermes/skills/catalog/kostja94-marketing-skills-setup)
- [ClawFu Skills - 175 Marketing Methodologies for AI Agents Setup](/hermes/skills/catalog/clawfu-skills-setup)
- [Eachlabs Skills - Creative Generation Setup](/hermes/skills/catalog/eachlabs-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Always run brand-intake first for a new brand; every other skill assumes the context document it produces.
- Pair hook-writing with hook-tactics for tactic coverage and hook-voice-patterns for a native feed voice.
- Feed review-audit real customer reviews; its five insight buckets are what make downstream hooks sound like your customers.
- Use creative-mechanics and visual-formats together; format is the vessel, mechanic is the cognitive move inside it.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
