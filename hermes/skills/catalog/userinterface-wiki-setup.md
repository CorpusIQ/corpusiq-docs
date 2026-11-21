---
title: "User Interface Wiki - UI/UX Review Skills Setup"
description: "raphaelsalaja/userinterface-wiki: 152 UI/UX rules across 12 categories for reviewing and generating interfaces - 6.1K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/userinterface-wiki-setup/"
robots: "index,follow"
last_updated: "2026-11-21"
tags: ["hermes skill", "agent skill", "skill setup", "ui design", "ux", "motion"]
---

# User Interface Wiki - UI/UX Review Skills Setup

**Source:** [raphaelsalaja/userinterface-wiki](https://www.skills.sh/raphaelsalaja/userinterface-wiki) via skills.sh - 6.1K combined installs across 16 indexed listings; first seen Nov 21, 2026 (Nov 21, 2026 morning sweep)
**GitHub:** [raphaelsalaja/userinterface-wiki](https://github.com/raphaelsalaja/userinterface-wiki) - 958 stars, MIT license, main branch, last pushed Jul 29, 2026; a Fumadocs wiki whose installable skill is a single `skills/SKILL.md` (152 rules) with per-rule notes under `skills/rules/` and article source under `content/`.
**Category:** UI/UX Design and Motion
**Quality Tier:** 🟠 Orange - next-upgrade carries a Fail cell on Gen Agent Trust Hub; 2 of 16 sampled skills carry Warn cells and 2 carry 'not parsed' cells.

Raphael Salaja's "A Living Manual for Better Interfaces" is a free, evolving wiki of articles, patterns and best practices for designing and building user interfaces. The repository distills that site into one agent skill: a 152-rule guide across 12 categories, from animation principles and timing functions through exit animations, CSS pseudo-elements, audio feedback, morphing icons, UX laws, predictive prefetching, typography and visual design. Skills.sh indexes the repo as 16 listings, but the installable agent skill is a single `skills/SKILL.md`; the remaining listings are the wiki's content articles and a set of Vercel, Next.js and skill-creator related names that have no counterpart in the current tree.

The dominant listing, `userinterface-wiki` at 4,874 installs, is the agent skill itself. It is a review-oriented rulebook that outputs `file:line - [rule-id]` findings, which makes it a read-only first step an agent can run against existing code before it changes anything. First seen in the Nov 21, 2026 morning sweep.

## Installation

Install the agent skill with the Vercel-labs skills CLI:

```bash
npx skills add raphaelsalaja/userinterface-wiki
```

The repo describes the skill as an Agent Skill that installs into Claude Code, Codex, Cursor and other coding agents. It ships as one `SKILL.md` at the repo root; the per-rule files under `skills/rules/` are the rule reference the skill reads, not separate installable skills.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| userinterface-wiki | 4,874 | 152 prioritized UI/UX rules across 12 categories, from animation and timing to typography, output as file:line findings |
| 12-principles-of-animation | 275 | the 12 foundations of animation from squash and stretch to timing and exaggeration, applied to web motion |
| generating-sounds-with-ai | 177 | building a custom library of UI sounds with Cursor and the Web Audio API |
| sounds-on-the-web | 153 | adding feedback, personality and presence through interface sound with action and button sound patterns |
| to-spring-or-not-to-spring | 152 | choosing between easing curves and springs for interface motion |
| mastering-animate-presence | 147 | advanced Motion AnimatePresence: presence state, manual exit control, directional and nested exits |
| pseudo-elements | 139 | modern CSS pseudo-elements beyond ::before and ::after, including view transitions and ::backdrop |
| morphing-icons | 120 | icons that morph through real shape transformation using three SVG lines, not crossfades |

The remaining 8 indexed listings range from 1 to 9 installs: web-design-guidelines (9) and seven Vercel, Next.js and skill-creator related names at 1 or 2 installs each, none of which has a counterpart in the current tree.

## Why This Matters for Hermes Agents

Interface review is where agents fail quietly: they generate something that looks plausible, ship it, and nobody notices the motion timing, the missing active state or the misaligned numbers until a user feels it. This skill replaces that guesswork with a deterministic rule set. An agent can review a component and return findings with rule IDs such as `timing-under-300ms` or `physics-active-state`, so every observation traces to a documented rule and a code example of the wrong and right version.

The rules are prioritized by impact, with animation principles and timing functions marked critical and typography marked incremental, so an agent knows where to spend its attention first. The decision frameworks are the operational value: springs for gesture-driven and interruptible motion, easing for system state changes, linear only for progress, and no animation for high-frequency interaction. Accessibility is folded into the rules rather than bolted on, with reduced-motion checks for audio and icons, a visual equivalent for every sound, and a disable toggle requirement. Because the skill is a read-only reference, an agent can audit a teammate's UI work and hand back findings without touching the code.

## Usage

| You say | What happens |
|---|---|
| Review this component for animation problems | Returns file:line findings with rule IDs for timing, easing and physics violations |
| Should this drag use a spring or an easing curve | Applies the spring-versus-easing decision framework and tells you which to use |
| Check our modal exit animation | Verifies the AnimatePresence wrapper, exit prop, keys and parent-child timing |
| Add a hover sound to this button | Applies the audio feedback rules, including visual equivalent and a disable toggle |
| Make this icon morph into that one | Applies the three-SVG-line morphing rules for shape transformation |
| Audit the typography on this page | Checks tabular numbers, optical sizing, text-wrap balance and font synthesis |
| Why does this transition feel slow | Flags durations over 300ms and prefers shortening duration over changing the curve |

## Verification

Review the skill file before installing it, then confirm it landed in your agent's skills directory:

```bash
curl -sL https://raw.githubusercontent.com/raphaelsalaja/userinterface-wiki/main/skills/SKILL.md | head -40
```

The raw SKILL.md resolves (HTTP 200) and opens with the frontmatter name `userinterface-wiki`, the MIT license field and the 152-rule, 12-category summary. After install, confirm the single skill file is present and that your agent can read it, then run a read-only review of one component as a first test.

## Security

skills.sh verdicts for sampled skills (verified Nov 21, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| userinterface-wiki | Pass | Pass | Pass |
| 12-principles-of-animation | Pass | Pass | Pass |
| generating-sounds-with-ai | Pass | Pass | Pass |
| sounds-on-the-web | Pass | Pass | Pass |
| to-spring-or-not-to-spring | Pass | Pass | Pass |
| mastering-animate-presence | Pass | Pass | Pass |
| pseudo-elements | Pass | Pass | Pass |
| morphing-icons | Pass | Pass | Pass |
| web-design-guidelines | Pass | Pass | Warn |
| vercel-react-best-practices | Pass | Pass | Pass |
| vercel-react-native-skills | None | Pass | None |
| vercel-composition-patterns | Pass | None | Pass |
| skill-creator | not parsed | not parsed | not parsed |
| next-upgrade | Fail | None | Warn |
| next-cache-components | not parsed | not parsed | not parsed |
| next-best-practices | Pass | None | Pass |

The main skill passes all three scanners. The listings that carry Fail, Warn, None or not-parsed cells are the long-tail entries with no counterpart in the current tree; treat them as unverified before use.

## Limitations

- Snapshot data, verified Nov 21, 2026: 6,054 combined installs across 16 indexed listings; 958 GitHub stars; MIT license; last pushed Jul 29, 2026. Counts drift over time.
- Index-versus-tree drift: 15 of the 16 indexed listings have no matching SKILL.md in the tree. Seven map to content articles under `content/<slug>/index.mdx`; the other eight (web-design-guidelines and the vercel, next and skill-creator names) have no counterpart in the current tree.
- The skill is a reference rulebook, not an executor: it outputs findings and guidance, so the agent still writes the actual fix.
- The wiki README documents the website build (Fumadocs), not the agent skill; install and usage details come from the skill files and the content/skill article.
- Two of the 16 sampled listings carry not-parsed security cells and one carries a Fail, so rely on the main `userinterface-wiki` skill and review anything else before use.

## Related

- [Animation Principles Skills - Motion Setup](/hermes/skills/catalog/dylantarre-animation-principles-setup)
- [Design Motion Principles Skill - Motion & Interaction Setup](/hermes/skills/catalog/design-motion-principles-skill-setup)
- [GSAP Skills - GreenSock Animation Platform Setup](/hermes/skills/catalog/greensock-gsap-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Review one component at a time and ask for file:line findings; the output format is built to paste straight into a review thread.
- Run the animation principles and timing function rules first; they are marked critical and catch the most visible quality issues.
- Cite the rule ID (for example timing-under-300ms) in every finding so a human can trace it to the rule and its code example.
- When reviewing audio, check for a visual equivalent and a disable toggle first; those two accessibility rules fail most often.
- The per-rule notes live under skills/rules/, so you can read a specific rule's rationale without loading the whole 152-rule file.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
