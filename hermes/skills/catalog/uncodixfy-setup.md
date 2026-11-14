---
title: "Uncodixfy - Anti AI UI Pattern Skill"
description: "cyxzdev/uncodixfy: 5.7K combined installs across 1 listing, a rule set that stops agents generating the generic gradient and card AI interface."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/uncodixfy-setup/"
robots: "index,follow"
last_updated: "2026-11-14"
tags: ["hermes skill", "agent skill", "skill setup", "ui design", "frontend", "code quality"]
---

# Uncodixfy - Setup Guide

**Source:** [cyxzdev/uncodixfy](https://www.skills.sh/cyxzdev/uncodixfy) via skills.sh - 5.7K combined installs across 1 indexed listing; first seen Nov 14, 2026 (standing window)
**GitHub:** 2,683 stars, MIT license, `main` branch, last pushed 2026-03-18, one `SKILL.md` at the repo root
**Category:** Frontend UI quality: a negative rule set that blocks generic AI interface patterns
**Quality Tier:** 🟠 Orange - one sampled verdict fails Snyk while the other two auditors pass, and the repository has been unchanged since March 2026.

Uncodixfy is one skill with an unusual shape: it does not teach an agent how to design. It lists the patterns the agent falls back to by default and tells it not to use them. Floating cards, oversized rounded corners, gradient-heavy dashboards, decorative eyebrow labels, glass panels and hero sections inside dashboards are named as banned, and each is paired with the normal implementation that should replace it.

The framing is deliberate. The README states the problem as a recognisable house style rather than a model defect: ask for interfaces long enough and the same defaults reappear. The skill names Linear, Raycast, Stripe and GitHub as the reference aesthetic, and it works by subtraction, so it changes the output without adding a design system or a component library to the context.

The trade-off is that it is a prompt-level control, not a linter. Nothing enforces the rules at build time, so the effect depends on the agent reading the skill before it writes UI code. The repository has also not changed since March 2026, which is worth knowing before adopting it as a standing rule.

## Installation

The README documents one install path and one invocation:

```bash
npx skills add cyxzdev/Uncodixfy
```

Once installed, invoke it in a session as `/uncodixfy`. The skill works in agents that support the skill format, including Codex and Claude Code.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| uncodixfy | 5,677 | Blocking generic AI UI patterns when generating HTML, CSS, React, Vue or Svelte, and replacing them with plain, human-designed layouts. |

No indexed listings fall below the threshold; the single listing appears above.

## Why This Matters for Hermes Agents

Output quality is the whole argument. An agent that ships UI code reproduces the same tells every time unless something names them, and a reviewer then spends the review round removing gradients, shrinking corner radii and deleting decorative labels. A negative rule set moves that work before generation.

It also composes with the design skills already in this catalog. A design-system skill describes what good looks like; Uncodixfy describes what to stop doing, so the two answer different questions and can load together without fighting over the same tokens.

The honest limit is enforcement. Because the rules live in prose, the agent can still drift on a long session, so treat the skill as one strong constraint among several rather than as a guarantee, and keep a visual review step in the loop.

## Usage

| You say | What happens |
|---|---|
| "Build a settings page" | Loads the banned-pattern list before generating, so the layout uses a plain shell instead of a floating card stack. |
| "Make this dashboard look good" | Pushes the agent toward normal spacing, solid surfaces and real hierarchy instead of gradients and glass panels. |
| "Review this UI" | Names the AI tells in the existing markup and gives the normal implementation for each. |
| "Style these components" | Applies the size, radius and border conventions the skill documents rather than inventing them per component. |
| "Why does this look AI-generated?" | Maps the visible symptoms back to the specific banned patterns. |

## Verification

Probe the skill before installing. The file sits at the repo root and returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/cyxzdev/uncodixfy/main/SKILL.md | head -20
```

The frontmatter description is the trigger text, so an agent that loads the skill sees the instruction to apply it whenever it writes frontend code.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-14) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| uncodixfy | Pass | Pass | Fail |

Two auditors pass and Snyk fails, on the only listing there is, so the Fail is not diluted by a larger sample. Read the Snyk report before installing rather than treating the skill as pre-cleared. The content itself is markdown instruction with no scripts, but the Fail is a published verdict and this guide does not explain it away.

## Limitations

- Snapshot data, verified 2026-11-14: 5,677 combined installs across 1 indexed listing; 2,683 GitHub stars; MIT; last pushed 2026-03-18. Counts drift over time.
- Snyk fails the only sampled skill. One Fail out of one sample is the whole security signal available here.
- The repository has not been pushed since 2026-03-18, so it does not track newer model behaviour or newer frontend frameworks.
- The rules are prose, not a linter: nothing fails a build when a banned pattern reappears, so the effect depends on the agent loading the skill before it writes UI code.
- The reference aesthetic is opinionated toward Linear, Raycast, Stripe and GitHub. Projects with a different design language should read the banned list as a starting point rather than a house style.

## Related

- [Anti-Slop - AI Copywriting Quality Skill](/hermes/skills/catalog/anti-slop-setup)
- [Designlang Skill - Extract Any Site's Design System](/hermes/skills/catalog/design-extract-skill-setup)
- [Interface Skills - Animation and UI Craft for Agents](/hermes/skills/catalog/raphaelsalaja-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Load the skill at the start of a UI task, not after the first draft; the point is to prevent the patterns rather than to remove them.
- Pair it with a design-system skill so one supplies what to build and the other supplies what to avoid.
- Run `/uncodixfy` before a review pass to catch the tells you would otherwise spend a round removing.
- Keep the before-and-after images in the README handy when arguing for a layout change; they show the difference faster than prose.
- Re-check the Snyk verdict yourself before adding the skill to a standing workflow.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
