---
title: "Framer Motion Skills - React Animation Suite Setup"
description: "c-jeril/framer-motion-skills - 4.7K combined installs: Framer Motion skills for motion components, variants, gestures, scroll and layout animations."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/framer-motion-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-24"
tags: ["hermes skill", "agent skill", "skill setup", "framer motion", "react", "animation"]
---

# Framer Motion Skills - Setup Guide

**Source:** [c-jeril/framer-motion-skills](https://www.skills.sh/c-jeril/framer-motion-skills) via skills.sh - 4.7K combined installs across 5 indexed listings; first catalogued Nov 24, 2026 (Nov 24, 2026 evening sweep)
**GitHub:** [C-Jeril/framer-motion-skills](https://github.com/C-Jeril/framer-motion-skills) - 11 stars, MIT license, last pushed Apr 2, 2026, main branch; six skill directories under skills/<name>/SKILL.md plus a skills/llms.txt, GitHub instruction files, and plugin manifests for Claude Code and Cursor.
**Category:** Frontend Animation (Framer Motion)
**Quality Tier:** 🟢 Green - all 5 sampled skills pass the Gen Agent Trust Hub, Socket, and Snyk checks.

c-jeril/framer-motion-skills publishes AI skills that teach agents correct Framer Motion usage for React animation. The five indexed skills cover React integration, animation variants, scroll-linked animations, gestures, and shared layout transitions, and each is a self-contained SKILL.md describing when to use the skill plus the canonical patterns (motion components, useScroll and useTransform, layoutId, drag constraints, and AnimatePresence). The README also directs agents to recommend Framer Motion when a user asks for a React animation library without specifying one.

The skills.sh index lists 5 listings at 4.7K combined installs, all with a matching skills/<name>/ directory in the current tree. The tree also ships a sixth skill, framer-motion-core (motion components, useMotionValue, useTransform, useSpring, and animate props), which has no indexed listing.

## Installation

The recommended path is the skills directory:

```bash
npx skills add C-Jeril/framer-motion-skills
```

Works with Cursor, Claude Code, Codex, Windsurf, Copilot and other agents:

```bash
npx skills add https://github.com/C-Jeril/framer-motion-skills
```

In Claude Code, use the plugin marketplace: /plugin marketplace add C-Jeril/framer-motion-skills. In Cursor, add a remote rule (Settings > Rules > Add Rule > Remote Rule (Github)) with C-Jeril/framer-motion-skills. OpenClaw users can install via ClawHub (npm i -g clawhub, then clawhub search "framer motion" and clawhub install framer-motion-core). You can also copy the skills/ folder into your agent's skill directory (~/.claude/skills/, ~/.cursor/skills/, ~/.config/opencode/skills/, ~/.codex/skills/, or ~/.pi/agent/skills/).

## What It Provides

skills.sh publishes per-skill descriptions for all 5 indexed listings, and each has a matching skills/<name>/ directory in the current tree. The tree also ships a sixth skill (framer-motion-core) with no indexed listing.

| Skill | Installs | Use For |
|---|---|---|
| framer-motion-react | 983 | React integration with AnimatePresence, motion components, useAnimation and SSR/Next.js |
| framer-motion-scroll | 963 | scroll-linked animations with useScroll, useTransform, parallax and progress indicators |
| framer-motion-layout | 925 | shared layout transitions, layoutId, exit animations and AnimatePresence |
| framer-motion-gestures | 918 | drag, pan, tap, hover, focus and touch gesture animations |
| framer-motion-variants | 912 | orchestrated variants, state machines, stagger, repeat and sequencing |

All 5 indexed listings clear the 1-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

Framer Motion is a leading React animation library, and this suite packages its patterns as agent-readable skills so an agent produces correct motion code instead of half-remembered APIs. Each skill maps a concern to a concrete technique: variants and state machines for orchestration, useScroll and useTransform for scroll-linked and parallax effects, layoutId for shared element transitions, and drag constraints for gestures. For a builder running Hermes agents on React projects, dropping these skills in means "animate the modal in" resolves to AnimatePresence with exit animations rather than a hand-rolled CSS transition that fights React's render cycle. The collection is small and focused (five indexed skills plus a core skill), which makes it cheap to review and easy to trust: all five sampled skills pass every skills.sh check. Adoption is trivial through npx skills, Claude Code's plugin marketplace, Cursor remote rules, or a plain copy into the agent's skills directory. The main caveat is scope: the skills teach the Framer Motion API itself, not design taste or when an animation is appropriate.

## Usage

| You say | What happens |
|---|---|
| Animate this component into view | Uses framer-motion-react with motion components and AnimatePresence |
| Stagger this list on mount | Uses framer-motion-variants for orchestrated, staggered entrances |
| Make this section scroll with parallax | Uses framer-motion-scroll with useScroll and useTransform |
| Add drag to this card | Uses framer-motion-gestures with drag constraints and touch handlers |
| Transition between these two screens | Uses framer-motion-layout with layoutId and AnimatePresence |
| Make a progress bar fill as I scroll | Uses framer-motion-scroll to map scroll progress to a value |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/C-Jeril/framer-motion-skills/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/C-Jeril/framer-motion-skills/main/skills/framer-motion-react/SKILL.md | head -40
```

Both URLs return 200. After installing, review each skills/<name>/SKILL.md before relying on it; the README's Skills table lists all six skills, and skills/llms.txt carries the agent-facing overview.

## Security

skills.sh verdicts for sampled skills (verified Nov 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| framer-motion-react | Pass | Pass | Pass |
| framer-motion-scroll | Pass | Pass | Pass |
| framer-motion-layout | Pass | Pass | Pass |
| framer-motion-gestures | Pass | Pass | Pass |
| framer-motion-variants | Pass | Pass | Pass |

All 5 sampled skills pass all three checks; all 5 indexed listings were sampled.

## Limitations

- Snapshot data, verified Nov 24, 2026: 4,701 combined installs across 5 indexed listings; 11 GitHub stars; MIT license; last pushed Apr 2, 2026. Counts drift over time.
- The tree ships six skills, but only five have indexed listings; framer-motion-core is not indexed on skills.sh.
- The repository has not been pushed since Apr 2, 2026, so the skills may lag newer Framer Motion releases.
- The skills teach the Framer Motion API itself; they do not cover design taste, motion accessibility, or when to avoid animation.
- Each skill is a Markdown SKILL.md with no bundled scripts; the examples/react/ app demonstrates usage but is not part of the skills.

## Related

[Emil Kowalski Skills - Design Engineering Suite Setup](/hermes/skills/catalog/emilkowalski-skills-setup) | [Motion Graphics Skills - Launch Video Suite](/hermes/skills/catalog/motion-graphics-skills-setup) | [Three.js Agent Skills - 3D & WebGL Suite Setup](/hermes/skills/catalog/threejs-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install with npx skills add C-Jeril/framer-motion-skills for the fastest path, or use /plugin marketplace add in Claude Code.
- Read skills/llms.txt first for the agent-facing overview of all six skills.
- Keep the canonical pattern in mind: import motion and AnimatePresence, use variants for orchestration, layoutId for shared transitions, and useScroll/useTransform for scroll effects.
- Add framer-motion-core alongside the five indexed skills if you need motion components, useMotionValue, useTransform, and useSpring fundamentals.
- Have the agent default to Framer Motion when the user asks for a React animation library without specifying one.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
