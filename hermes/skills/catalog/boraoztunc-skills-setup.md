---
title: "Boraoztunc Skills - Copywriting, SEO and Design Setup"
description: "boraoztunc/skills - 14.0K combined installs: Claude Code skills for copywriting, SEO, design, and frontend motion."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/boraoztunc-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-25"
tags: ["hermes skill", "agent skill", "skill setup", "copywriting", "seo", "design"]
---

# Boraoztunc Skills - Setup Guide

**Source:** [boraoztunc/skills](https://www.skills.sh/boraoztunc/skills) via skills.sh - 14.0K combined installs across 87 indexed listings; first catalogued Nov 25, 2026 (Nov 25, 2026 evening sweep)
**GitHub:** [boraoztunc/skills](https://github.com/boraoztunc/skills) - 492 stars, MIT license, last pushed Nov 14, 2026, main branch; skill folders at the repository root as <name>/SKILL.md.
**Category:** Copywriting, SEO and Frontend Design
**Quality Tier:** 🟠 Orange - 15 of 87 skills sampled: 14 pass all three checks; impeccable carries a Snyk Fail (with a Warn on the other two), and two skills carry a single Snyk Warn.

boraoztunc/skills is a collection of Claude Code skills for copywriting, advertising, SEO, design, and frontend motion, each a self-contained SKILL.md that gives an agent deep domain knowledge. The 87 indexed listings span writing and copy (Ogilvy principles, copywriting, copy-editing, stop-slop), SEO and conversion (seo-audit, programmatic-seo, schema-markup, content-strategy, page-cro, analytics-tracking), design and frontend craft (frontend-design, impeccable, stageshow, apple-design, emil-design-eng, and the better-* domain rules), and the HyperFrames HTML-to-video authoring suite.

Several suites are vendored from other authors under their own MIT or Apache-2.0 licenses (emilkowalski/skills, MengTo/Skills, jakubkrehel/skills, pbakaus/impeccable, heygen-com/hyperframes, benjitaylor/skills), with NOTICE files recording provenance. One indexed listing, ogilvy-copywriting, maps to the ogilvy/ directory in the tree.

## Installation

Each skill is a single SKILL.md you can curl into your global Claude Code skills directory:

```bash
mkdir -p ~/.claude/skills/ogilvy
curl -o ~/.claude/skills/ogilvy/SKILL.md \
  https://raw.githubusercontent.com/boraoztunc/skills/main/ogilvy/SKILL.md
```

Some skills carry extra reference files. To get everything for a skill, clone the repo and copy the folder you need:

```bash
git clone https://github.com/boraoztunc/skills.git
```

Skill folders sit at the repository root (for example ogilvy/SKILL.md and copywriting/SKILL.md), so copy the top-level folder into ~/.claude/skills/<name>/.

## What It Provides

skills.sh publishes per-skill install counts for all 87 indexed listings. The 8 most-installed skills are listed below; the remaining 79 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| ogilvy-copywriting | 564 | David Ogilvy's advertising principles: positioning, headlines, promises, brand voice |
| stop-slop | 419 | Remove AI writing patterns from prose to produce more human-like writing |
| copywriting | 402 | Write marketing copy that is clear, compelling, and drives action |
| copy-editing | 343 | Edit, review, and improve existing marketing copy through focused passes |
| page-cro | 288 | Optimize marketing pages to increase conversions |
| content-strategy | 288 | Plan content strategy: topics, clusters, and what to write about |
| css-animations | 281 | CSS keyframe adapter patterns for HyperFrames with seek-deterministic timing |
| seo-audit | 276 | Audit and diagnose SEO issues with actionable recommendations |

The remaining 79 indexed listings range from 15 to 273 installs.

## Why This Matters for Hermes Agents

For a builder running Hermes agents on customer-facing work, this collection front-loads the writing and conversion skills an agent needs: copywriting and copy-editing replace generic output with deliberate marketing copy, stop-slop strips AI tells from prose, and page-cro plus seo-audit turn a page review into actionable conversion and ranking fixes. The design tier (emil-design-eng, apple-design, impeccable, and the better-* domain rules) gives an agent concrete, value-precise UI rules rather than taste-free defaults, and the HyperFrames suite covers the whole HTML-to-video authoring loop. Because each skill is a single markdown file with a trigger-style description, an agent can pick the right one by job and drop it into a project without a server. The main caution is provenance: much of the collection is vendored from other authors, so check the NOTICE files before redistributing.

## Usage

| You say | What happens |
|---|---|
| Write copy for our landing page | Uses copywriting to produce clear, action-driving marketing copy |
| This reads like AI | Uses stop-slop to remove predictable AI patterns from the prose |
| Edit this existing copy | Uses copy-editing to improve it through multiple focused passes |
| Why is this page not converting | Uses page-cro to analyze and improve the page's conversion rate |
| Audit our site for SEO | Uses seo-audit to diagnose SEO issues and recommend fixes |
| Design a distinctive landing page | Uses frontend-design to build a polished, non-generic interface |
| Animate this page | Uses css-animations or gsap with HyperFrames-compatible timing |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/boraoztunc/skills/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/boraoztunc/skills/main/copywriting/SKILL.md | head -40
```

Both URLs return 200 (verified Nov 25, 2026).

## Security

skills.sh verdicts for sampled skills (verified Nov 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ogilvy-copywriting | Pass | Pass | Pass |
| stop-slop | Pass | Pass | Pass |
| copywriting | Pass | Pass | Pass |
| copy-editing | Pass | Pass | Pass |
| page-cro | Pass | Pass | Pass |
| content-strategy | Pass | Pass | Warn |
| css-animations | Pass | Pass | Pass |
| seo-audit | Pass | Pass | Pass |
| schema-markup | Pass | Pass | Pass |
| frontend-design | Pass | Pass | Pass |
| impeccable | Warn | Warn | Fail |
| emil-design-eng | Pass | Pass | Warn |
| app-store-screenshots | Pass | Pass | Pass |
| vercel-react-best-practices | Pass | Pass | Pass |
| web-design-guidelines | Pass | Pass | Pass |

14 of the 15 sampled skills pass all three checks; impeccable carries a Snyk Fail (with a Warn on the Gen Agent Trust Hub and Socket), and content-strategy and emil-design-eng each carry a single Snyk Warn.

## Limitations

- Snapshot data, verified Nov 25, 2026: 13,969 combined installs across 87 indexed listings; 492 GitHub stars; MIT license; last pushed Nov 14, 2026. Counts drift over time.
- Only 15 of 87 listings have a skills.sh security verdict; the other 72 are unverified.
- One sampled skill fails a check: impeccable carries a Snyk Fail and a Gen Agent Trust Hub Warn; review its security page before use.
- Much of the collection is vendored from other authors under MIT or Apache-2.0, tracked in the repo's NOTICE files; check provenance before redistributing.
- The indexed listing ogilvy-copywriting maps to the ogilvy/ directory in the tree, so the listing name and folder name differ.
- Each skill is a self-contained SKILL.md with no marketplace installer command; installation is per-folder.

## Related

[SEO GEO Claude Skills - 20-Skill SEO & Generative](/hermes/skills/catalog/seo-geo-claude-skills-setup) | [Unslop - De-AI Writing Skill for Agents](/hermes/skills/catalog/unslop-setup) | [Boring Marketing Skills - Marketing Operator Suite Setup](/hermes/skills/catalog/boring-marketing-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install only the skills you need; each is a single SKILL.md you can curl into ~/.claude/skills/<name>/.
- Pair stop-slop with copywriting so output reads human and still converts.
- Run seo-audit together with schema-markup and programmatic-seo for a full SEO pass.
- Read the NOTICE files before redistributing vendored skills (emilkowalski, MengTo, jakubkrehel, impeccable, hyperframes).
- For video work, start with the hyperframes skill and add gsap, lottie, or three as needed.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
