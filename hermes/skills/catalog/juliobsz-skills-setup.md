---
title: "Juliobsz Skills - Award-Caliber Websites and Jury Review"
description: "juliobsz/skills: 4.9K combined installs across 2 listings; builds award-caliber websites from one line and scores any site like an Awwwards jury."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/juliobsz-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-19"
tags: ["hermes skill", "agent skill", "skill setup", "web design", "design qa", "website builder"]
---

# Juliobsz Skills - Setup Guide

**Source:** [juliobsz/skills](https://www.skills.sh/juliobsz/skills) via skills.sh - 4.9K combined installs across 2 indexed listings; first seen Nov 19, 2026 (Nov 19, 2026 morning sweep)
**GitHub:** 1,375 stars, MIT licence, `main` branch, last pushed 2026-10-26. Two skills at the repository root (`awwwards/` and `jury/`), each a `SKILL.md` with references and Node helper scripts, plus a Claude Code plugin marketplace under `.claude-plugin/`.
**Category:** Web design and design QA
**Quality Tier:** 🟡 Yellow - 1 Warn among 2 sampled skills (jury); MIT licence.

Juliobsz Skills builds award-caliber websites from a one-line prompt and scores any site the way an Awwwards jury would. `/awwwards` works as creative director, designer, and creative developer in one, treating Awwwards Site of the Day as the quality bar and finishing with a browser-checked build; `/jury` reviews an existing site from evidence alone and returns a ranked fix list.

The two skills share the same quality rubric and QA scripts, so a site built by `/awwwards` and a site you built are judged the same way.

## Installation

Install with the skills CLI (it detects your agents and lets you pick):

```bash
npx skills add juliobsz/skills -g
```

Install a single skill with `--skill`:

```bash
npx skills add juliobsz/skills -g --skill jury
```

Or install as a Claude Code plugin:

```
/plugin install awwwards --marketplace juliobsz/skills
/plugin install jury --marketplace juliobsz/skills
```

The optional `/anatomy` skill by wheresryan22 adds interactive isometric explainer figures:

```bash
npx skills add wheresryan22/anatomy -g
```

Requirements: Node 22.20+ for the skills CLI (helper scripts need Node 20+), Playwright and axe-core for screenshots and the accessibility pass, and a model that can read images.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| awwwards | 2,798 | Build award-caliber websites from a one-line prompt: concept, art direction, typography, motion, WebGL, real content, SEO, and accessibility, then visual QA in a browser. |
| jury | 2,108 | Score any website the way an Awwwards jury would: screenshots, LCP/CLS/FPS/axe measurements, SEO and metadata audit, then a blind critic scores Design, Usability, Creativity, Content, and six developer areas with a ranked fix list. |

No indexed listings fall below the threshold; all 2 appear above.

## Why This Matters for Hermes Agents

The default answer to "make me a portfolio" is a purple gradient and three cards; these skills replace that default with a process. The value for an agent is the encoded pipeline: three concepts scored on originality, a real design system written to `DESIGN.md`, motion where it earns its place, and a QA loop that builds production output, screenshots it on desktop and a throttled phone, and fixes until every category hits 8/10.

The jury rubric is the reusable part for Hermes: it scores Design, Usability, Creativity, Content, and six developer areas from measurements and screenshots alone, and every number cites evidence. The skills ship as plain `SKILL.md` files plus Node scripts, so any harness that reads skill files can run them.

## Usage

| You say | What happens |
|---|---|
| "Make me a portfolio, my name is Ana" | awwwards infers the brief, proposes three concepts, builds, and browser-checks the site. |
| "Redesign this landing page to win Site of the Day" | awwwards applies the rubric and reworks the page against the quality bar. |
| "/jury https://your-site.com" | jury screenshots every page type, measures performance and accessibility, and returns a scored, ranked fix list. |
| "Roast my site" | jury runs the blind critic and reports a score card with cited evidence. |
| "Score my site vs theirs" | jury evaluates both URLs and compares the score cards. |

## Verification

Probe both skills on the `main` branch before installing. Both return 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/juliobsz/skills/main/awwwards/SKILL.md
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/juliobsz/skills/main/jury/SKILL.md
```

After install, start a new agent session, then type `/awwwards` or ask for a website.

## Security

skills.sh verdicts for sampled skills (verified Nov 19, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| awwwards | Pass | Pass | Pass |
| jury | Pass | Pass | Warn |

The sample covers both indexed listings; jury carries a single Warn. The skills run builds and scripts on your machine, so read each `SKILL.md` before installing; nothing is deployed without your confirmation.

## Limitations

- Snapshot data, verified Nov 19, 2026: 4,906 combined installs across 2 indexed listings; 1,375 GitHub stars; MIT licence; last pushed 2026-10-26. Counts drift over time.
- A full `/awwwards` run is concept, design system, build, and several rounds of screenshots and fixes: expect a long session and heavy token use.
- The concept and visual QA are only as good as the model doing them; the skills were built and tested with Claude Code, Antigravity, and Codex.
- `/jury` is an estimate, not affiliated with Awwwards; its jury estimate rests on two winning sites, so weaker sites are not yet calibrated.
- Content is yours to finish: without real projects, photos, and copy, the site ships with clearly marked placeholders.

## Related

- [Bergside Design Skills - Design Systems Setup](/hermes/skills/catalog/bergside-awesome-design-skills-setup)
- [Popular Web Designs - 54 Design Systems as HTML/CSS Templates Setup](/hermes/skills/catalog/popular-web-designs-setup)
- [design-review - Visual UI Audit & Fix Setup](/hermes/skills/catalog/design-review-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `/jury` on a competitor before you build, so the fix list guides the brief you hand `/awwwards`.
- Give `/awwwards` your real name, what you do, where you are, and two or three real projects; the concept comes from your story instead of a placeholder.
- Use the plugin or the skills CLI, not both, or each skill shows up twice.
- Add `/anatomy` (wheresryan22/anatomy) for one "how it works" section built as an isometric figure styled to your palette and grid.
- On a local project, `/jury` builds and scores the production output, never the dev server.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
