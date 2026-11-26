---
title: "StyleSeed Skills - Design Method Engine Setup"
description: "bitjaru/styleseed - 19.1K combined installs: a design-method engine with one skill and 22 workflows for evidence-verified UI."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/bitjaru-styleseed-setup/"
robots: "index,follow"
last_updated: "2026-11-25"
tags: ["hermes skill", "agent skill", "skill setup", "design system", "ui craft", "claude code"]
---

# StyleSeed Skills - Setup Guide

**Source:** [bitjaru/styleseed](https://www.skills.sh/bitjaru/styleseed) via skills.sh - 19.1K combined installs across 30 indexed listings; first catalogued Nov 25, 2026 (Nov 25, 2026 evening sweep)
**GitHub:** [bitjaru/styleseed](https://github.com/bitjaru/styleseed) - 1,056 stars, MIT license, last pushed Nov 26, 2026, main branch; one registered skill at skills/styleseed/SKILL.md with 22 internal workflows under skills/styleseed/workflows/<name>/WORKFLOW.md.
**Category:** Design Engineering (Agent Skills)
**Quality Tier:** 🟡 Yellow - 15 of 30 listings sampled: three carry a Warning and twelve pass all three checks; no Fails.

bitjaru/styleseed is an open-source design-method engine for Claude Code, Codex and Cursor. One registered agent skill routes a request to 22 internal workflows covering setup, build, design review, scoring, accessibility, motion, tokens, and UX copy, backed by 74 craft rules, eight output grammars, five surface adapters, and a render-then-score gate that tells an installed agent to revise screens below 80 before presenting them.

The engine compiles the selected rules into a small hash-verifiable bundle and writes a STYLESEED.md lock so design decisions survive across screens and sessions. The 30 indexed listings mix the current single-skill layout with legacy per-workflow names; the tree ships one registered skill with 22 workflows, plus an optional learning extension that is not part of the public install path.

## Installation

```bash
npx -y skills add bitjaru/styleseed -a codex claude-code -y --copy
```

Installs the core skill for Codex and Claude Code together, with no agent, skill, or install-mode menus. It copies the skills into the current project and does not install globally. For a single agent, pass only -a codex or -a claude-code; for Cursor or other agents, run the interactive npx skills add bitjaru/styleseed and choose Project then Copy.

Claude Code can also manage StyleSeed as a versioned plugin via its marketplace:

```bash
claude plugin marketplace add bitjaru/styleseed
claude plugin install styleseed@styleseed
```

Both paths install the same public skill with 22 internal workflows; the optional ss-learn learning extension is in neither.

## What It Provides

skills.sh publishes per-skill install counts for all 30 indexed listings. The 8 most-installed listings are listed below; the remaining 22 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| ss-review | 864 | design code review that cites the selected contract for each violation |
| ss-audit | 864 | Nielsen's 10 usability heuristics evaluation of a screen |
| ss-setup | 863 | interactive wizard to select output grammar, adapter, and brand recipe |
| ss-a11y | 862 | accessibility audit against WCAG 2.2 AA |
| ss-lint | 855 | quick automated lint that catches common violations in seconds |
| ss-feedback | 852 | add loading, success, error, and empty states to any component |
| ss-update | 849 | pull latest engine updates and update the project safely |
| ss-component | 836 | generate components following design conventions |

The remaining 22 indexed listings range from 1 to 835 installs.

## Why This Matters for Hermes Agents

These skills solve the specific failure that makes AI-built UI look generic: an agent that improvises a new look on every screen. StyleSeed records design decisions once and compiles them into a per-screen rule bundle, so a Hermes agent building frontend work follows a fixed design system instead of re-deciding colors, type, and spacing each task. The render-then-score gate is the piece most general coding skills lack - the agent scores what it actually rendered and revises screens below 80 before showing them, catching dead whitespace, unloaded fonts, and blank empty states that a code-only review misses. The STYLESEED.md lock means those decisions persist across screens and sessions, and the context compiler keeps the working bundle small and hash-verifiable so the agent does not re-read a 220KB handbook per task. The honest caveat: a score of 80 is not expert approval, and the gate only runs when the workflow is actually invoked - a markdown file alone cannot block delivery.

## Usage

| You say | What happens |
|---|---|
| Set up a design system for this product | Uses ss-setup to run the interactive wizard and pick grammar, adapter, and brand recipe |
| Build me a billing settings page | Uses ss-build to lock the look, build, score, and fix to 80+ before showing |
| Review this screen for design violations | Uses ss-review to audit code against the selected contract |
| Run a quick lint on this component | Uses ss-lint to catch common violations in seconds |
| Check this screen for accessibility issues | Uses ss-a11y against WCAG 2.2 AA criteria |
| Add loading and error states to this page | Uses ss-feedback to add loading, success, error, and empty states |
| Pull the latest StyleSeed engine updates | Uses ss-update to analyze the project and update safely |

## Verification

Confirm the README and the registered skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/bitjaru/styleseed/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/bitjaru/styleseed/main/skills/styleseed/SKILL.md | head -40
```

Both URLs return 200. After installing, review skills/styleseed/SKILL.md and the workflow files before relying on them, and re-check the security pages on skills.sh for the Warnings noted below.

## Security

skills.sh verdicts for sampled skills (verified Nov 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ss-review | Pass | Pass | Pass |
| ss-audit | Pass | Pass | Pass |
| ss-setup | Warn | Pass | Pass |
| ss-a11y | Pass | Pass | Pass |
| ss-lint | Pass | Pass | Pass |
| ss-feedback | Pass | Pass | Pass |
| ss-update | Pass | Pass | Warn |
| ss-component | Warn | Pass | Pass |
| ss-page | Pass | Pass | Pass |
| ss-motion | Pass | Pass | Pass |
| ss-tokens | Pass | Pass | Pass |
| ss-score | Pass | Pass | Pass |
| ss-pattern | Pass | Pass | Pass |
| ss-flow | Pass | Pass | Pass |
| ss-copy | Pass | Pass | Pass |

15 of 30 listings were sampled; three carry a single Warning (ss-setup and ss-component on Gen Agent Trust Hub, ss-update on Snyk) and twelve pass all three checks, with no Fails.

## Limitations

- Snapshot data, verified Nov 25, 2026: 19,082 combined installs across 30 indexed listings; 1,056 GitHub stars; MIT license; last pushed Nov 26, 2026. Counts drift over time.
- Only 15 of 30 listings carry skills.sh security verdicts; the remaining 15 have no sampled verdicts.
- The 30 indexed listings mix the current single-skill layout with legacy per-workflow names; the tree ships one registered skill (styleseed) with 22 ss-* workflows, while listings such as styleseed-design-review, ux-feedback, and ui-review reflect older install entries.
- The default npx skills command follows mutable main; pin a release archive (v5.0.0) for a fixed, checksummed evaluation version.
- The pushed timestamp (Nov 26, 2026) is one day after the Nov 25 snapshot date, a timezone artifact; treat the snapshot as the verification date.

## Related

[UI Craft - Design Engineering System Setup](/hermes/skills/catalog/ui-craft-setup) | [Podo Design Agent Skills - 151-Skill Design Catalog Setup](/hermes/skills/catalog/podo-design-agent-skills-setup) | [Uizze UI Skills - Anti-UI-Slop Design Quality Setup](/hermes/skills/catalog/uizze-ui-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the single skill and use /styleseed build instead of building UI free-hand, so the gate scores and fixes before you see the screen.
- Run /styleseed resolve so the agent reads the small .styleseed/effective-rules.md bundle instead of the full handbook.
- Lock decisions early with /styleseed setup; a written STYLESEED.md is the single strongest fix for inconsistency.
- Retrofit an existing generic build with /styleseed score then /styleseed review, and re-score to 80+.
- Pin a release archive for reproducible installs; the default command follows mutable main.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
