---
title: "UI Skills - Design Engineer Skill Registry Setup"
description: "Setup guide for ibelick/ui-skills: 99.1K combined installs. Design-engineer skills for UI review, motion, and accessibility, with CLI and MCP access."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ibelick-ui-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-09"
tags: ["hermes skill", "agent skill", "skill setup", "design engineering", "ui quality", "motion", "accessibility"]
---

# UI Skills - Setup Guide

**Source:** [ibelick/ui-skills](https://www.skills.sh/ibelick/ui-skills) via skills.sh - 99.1K combined installs across 8 indexed listings; first seen Oct 9, 2026 (evening sweep)
**GitHub:** [ibelick/ui-skills](https://github.com/ibelick/ui-skills) (9,564 stars, MIT license; active - pushed Oct 9, 2026; seven skills under `skills/`: baseline-ui, create-design-md, fixing-accessibility, fixing-metadata, fixing-motion-performance, improve-ui, and ui-skills-root)
**Category:** Design Engineering / UI Quality / Skill Registry
**Quality Tier:** 🟢 Production - 9,564-star MIT repo (ibelick), active (pushed Oct 9, 2026); 99.1K combined installs across 8 indexed listings; all sampled verdicts Pass/Pass/Pass

UI Skills is a skill registry for design engineers: seven skills that direct an agent's interface work, a CLI for browsing and fetching them from the terminal, and an MCP endpoint that lets compatible agents list and pull skills directly. The repository bills itself as "Skills for Design Engineers," and the skill set covers interface fundamentals: baseline rules (baseline-ui), an improvement pass (improve-ui), design documentation (create-design-md), and three focused repair skills for accessibility, metadata, and motion performance. A companion playbook collects distilled UI lessons from the best design-engineering skills.

The distribution is deliberately agent-neutral. The CLI (`npx ui-skills`) browses categories and fetches any skill by id, and the MCP endpoint at ui-skills.com/mcp exposes `list_skills` and `get_skill` tools. Top installs tell a clear story: fixing-motion-performance (24.5K), baseline-ui (21.9K), fixing-accessibility (19.9K), and fixing-metadata (16.5K) lead the registry.

---

## Installation

```bash
# Browse and fetch skills from the terminal (README commands)
npx ui-skills start
npx ui-skills categories
npx ui-skills list --category motion
npx ui-skills get baseline-ui
```

Skills fetch by id, so the terminal is the natural place to inspect one before it reaches an agent. MCP-capable agents can skip the CLI and connect to the hosted registry at `https://www.ui-skills.com/mcp` (tools: `list_skills`, `get_skill`).

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| fixing-motion-performance | 24,528 | Motion performance repair for interface code |
| baseline-ui | 21,940 | The baseline UI rule layer for design-engineer work |
| fixing-accessibility | 19,878 | Accessibility repair for UI code |
| fixing-metadata | 16,487 | Metadata repair for pages and interfaces |
| improve-ui | 6,469 | An improvement pass over existing UI |
| ui-skills-root | 6,103 | The registry's root skill - suite orientation |
| create-design-md | 3,639 | Creating a design.md document for a project |

One additional 22-install listing (`ui-skills`) completes the eight indexed entries. The registry organizes its skills into categories - motion, metadata, and accessibility among them - browsable with `npx ui-skills categories`.

## Why This Matters for Hermes Agents

Agents that generate UI tend to converge on the same generic output, and the details that separate production-quality interfaces - motion performance, accessibility, metadata - are usually the first things lost. This registry is the design-engineering counterweight: baseline rules to start from, an improvement pass for existing screens, and dedicated repair skills for the defect classes above. The most-adopted entries are the three repair skills - fixing-motion-performance, fixing-accessibility, and fixing-metadata. Because every skill is plain Markdown fetched by id, a Hermes agent adopts the suite the same way it adopts any other skill, with no runtime service beyond the fetch. For teams that gate UI work before ship, these slot naturally into a review step. The CLI and MCP endpoint make the registry reachable both from a terminal session and from inside an agent loop, and the MIT license keeps vendoring simple.

## Usage

| You say | What happens |
|---|---|
| "This animation stutters on slower machines" | fixing-motion-performance drives a motion performance repair pass |
| "Audit the signup page for accessibility issues" | fixing-accessibility runs an accessibility fix pass |
| "Our page metadata is inconsistent - clean it up" | fixing-metadata normalizes page and interface metadata |
| "This dashboard looks generic - make it feel designed" | improve-ui applies an interface improvement pass |
| "We need design documentation for this project" | create-design-md produces a design.md |
| "Set ground rules before we start building UI" | baseline-ui supplies the baseline layer |
| "What motion skills are available?" | `npx ui-skills list --category motion` (or `list_skills` over MCP) lists the registry's options |

## Verification

```bash
# Browse the registry from the terminal (README commands)
npx ui-skills categories
npx ui-skills list --category motion

# Confirm fetched skills landed in your agent's skills directory
ls ~/.claude/skills/ | grep -iE "baseline-ui|improve-ui|create-design-md|fixing-|ui-skills-root"

# Review any skill's SKILL.md directly before installing (no rate limits)
curl -s https://raw.githubusercontent.com/ibelick/ui-skills/main/skills/fixing-accessibility/SKILL.md | head -20
```

## Security

skills.sh verdicts for sampled skills (verified Oct 9, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| improve-ui | Pass | Pass | Pass |
| create-design-md | Pass | Pass | Pass |
| fixing-accessibility | Pass | Pass | Pass |

All three sampled skills pass all three scanners, and the repository is MIT-licensed. Terminal use runs through `npx ui-skills`, so normal supply-chain hygiene applies to the fetcher; the fetched skill content is plain Markdown and reviewable before use.

## Limitations

- Skill descriptions on this page are name-level - open each SKILL.md before wiring it into a pipeline (see Verification).
- The repair skills (fixing-accessibility, fixing-metadata, fixing-motion-performance) and improve-ui assume existing interface code to review rather than greenfield generation.
- Terminal use runs through `npx ui-skills`; environments that need reproducible installs should vendor fetched skills rather than rely on live fetches.
- MCP access depends on the hosted registry endpoint (ui-skills.com/mcp) staying available.
- Snapshot data, verified Oct 9, 2026: 99,066 combined installs across 8 indexed listings; 9,564 GitHub stars; MIT; last pushed Oct 9, 2026. Counts drift over time.

## Related

- [Better UI Skills - Interface Polish Suite Setup](/hermes/skills/catalog/better-ui-skills-setup) - the closest overlap: interface-polish review and repair for existing UI
- [Emil Kowalski Skills - Design Engineering Suite Setup](/hermes/skills/catalog/emilkowalski-skills-setup) - motion and interaction craft behind the fixing-motion-performance workflow
- [shadcn Skill - shadcn/ui Component Workflows Setup](/hermes/skills/catalog/shadcn-ui-setup) - the component layer for React projects this suite reviews
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Pull the repair skills into a pre-ship review: fixing-motion-performance, fixing-accessibility, and fixing-metadata are the registry's three most-adopted skills.
- Browse before fetching: `npx ui-skills categories` and `npx ui-skills list --category motion` show the catalog, and `get <id>` fetches a single skill.
- Register the MCP endpoint (`https://www.ui-skills.com/mcp`) once so an agent can list and fetch skills in-loop instead of pasting content by hand.
- Check ui-skills.com/playbook for the distilled UI lessons that explain the rules behind the skills.
- If a project lacks written design rules, run create-design-md early so future sessions have a reference.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
