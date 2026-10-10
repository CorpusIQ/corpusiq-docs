---
title: "Designer Skills - Design Process Suite Setup"
description: "Setup guide for julianoczkowski/designer-skills: 8 design-process skills from brief to reviewed frontend - 43.0K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/designer-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-09"
tags: ["hermes skill", "agent skill", "skill setup", "design process", "frontend", "design tokens", "product design"]
---

# Designer Skills - Setup Guide

**Source:** [julianoczkowski/designer-skills](https://www.skills.sh/julianoczkowski/designer-skills) via skills.sh - 43,011 combined installs across 8 indexed listings (design-tokens 5,698; information-architecture 5,673; design-review 5,609; frontend-design 5,336; grill-me 5,307; design-brief 5,192; design-flow 5,133; brief-to-tasks 5,063); first seen Oct 9, 2026 (evening sweep)
**GitHub:** [julianoczkowski/designer-skills](https://github.com/julianoczkowski/designer-skills) (578 stars, Apache-2.0 license; active - pushed Jul 6, 2026; eight skills at the repo root, each a folder with a `SKILL.md`, plus a Claude Code plugin manifest)
**Category:** Design Process / Product Design / Frontend
**Quality Tier:** 🟡 Beta - 578-star Apache-2.0 repo, active; 43.0K combined installs across 8 indexed listings; design-process skills for designers who prototype with AI; all sampled verdicts Pass/Pass/Pass

Designer Skills is Julian Oczkowski's collection of eight agent skills for designers who prototype and build with AI coding tools. The premise, stated in the repo: these skills encode design process so AI follows a structured path instead of producing random output. The suite walks a feature through a deliberate sequence - grill-me interrogation, design brief, information architecture, design tokens, task breakdown, frontend build, and design review - with /design-flow orchestrating the whole run and letting you skip phases.

Julian Oczkowski builds AI tools for knowledge work and publishes walkthroughs on YouTube (@aiforwork_app), Medium, and LinkedIn. The skills work individually or as an orchestrated flow, run across Claude Code, Cursor, Codex, Windsurf, and 40+ other agents, and save every artifact - briefs, architecture, task lists, reviews - to a `.design/` folder inside your project, organized by feature, so nothing gets overwritten and a later session can resume where the last one stopped. The suite carries 43.0K combined installs across eight indexed skills.sh listings.

---

## Installation

```bash
# Skills CLI (interactive: pick skills, agents, and project or global scope)
npx skills add julianoczkowski/designer-skills
```

Claude Code plugin (all 8 skills as one plugin):

```text
/plugin marketplace add julianoczkowski/designer-skills
/plugin install designer-skills@designer-skills
```

Claude invokes the skills automatically from their descriptions, or you can call one explicitly (for example `/designer-skills:design-brief`); update later with `/plugin update designer-skills@designer-skills`. To try the plugin from a local checkout first, run `claude --plugin-dir /path/to/designer-skills`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| design-tokens | 5,698 | Generate a complete token system (colors, spacing, typography, motion) with light and dark palettes from the chosen aesthetic philosophy |
| information-architecture | 5,673 | Define the structural skeleton: navigation, content hierarchy, page structure, URL patterns, user flows |
| design-review | 5,609 | Structured critique against the brief; code review and screenshot-based review, run on request |
| frontend-design | 5,336 | Build mobile-first with a named aesthetic philosophy; 8 philosophies with concrete implementation parameters |
| grill-me | 5,307 | Interrogate a plan until every design decision is resolved |
| design-brief | 5,192 | Turn the grilling session into a structured design brief, including codebase exploration |
| design-flow | 5,133 | Orchestrate the full workflow as a guided sequence; confirms between steps and lets you skip phases |
| brief-to-tasks | 5,063 | Break the brief into an ordered checklist of independently buildable vertical slices |

Every skill that touches the codebase ships a detection checklist - CSS variables, Tailwind config, UI framework themes, component directories, Storybook stories, token files, font loading, and package dependencies - so the agent respects what already exists instead of inventing new components or clashing colors.

## Why This Matters for Hermes Agents

Most agent design problems are process problems: the model starts building before the brief exists, invents a new button instead of reusing one, or picks colors that clash with the established palette. Designer Skills attacks that directly - it makes the agent interrogate the plan first, explore the existing codebase before proposing anything, define tokens before components, and review against the brief at the end. The suite is portable across the major coding agents, and the installed skills behave like any other skill in a Hermes agent's skills directory: plain instruction files with no runtime service. Two defaults change output immediately: /frontend-design builds mobile-first (375px layout first, scaling up with min-width media queries) with a named aesthetic philosophy, and /design-tokens always emits light and dark palettes. The persistence model is agent-friendly: every artifact lands in a `.design/<feature>/` folder, so a later session can pick the work back up from the brief and task list instead of restarting. For agents producing UI for products or clients, this is the process layer that keeps generation aligned with a written design record.

## Usage

| You say | What happens |
|---|---|
| "Start a design flow for the new onboarding feature" | /design-flow orchestrates the sequence from grilling to review, confirming between each step |
| "Grill me on this plan" | /grill-me interrogates you until every design decision is resolved |
| "Write up the design brief" | /design-brief explores the codebase and turns the session into a structured brief |
| "Define the design tokens" | /design-tokens generates color, spacing, typography, and motion tokens with light and dark palettes |
| "Build the frontend in a Swiss International style" | /frontend-design builds mobile-first with that philosophy's typography, color, layout, spacing, motion, and detail parameters |
| "Break this into tasks" | /brief-to-tasks produces an ordered checklist of independently buildable vertical slices |
| "Review what we built" | /design-review critiques the result against the brief, from code or screenshots, on request |

## Verification

```bash
# Confirm the skills are installed
npx skills list | grep -E "design-flow|grill-me|design-brief|information-architecture|design-tokens|brief-to-tasks|frontend-design|design-review"

# Claude Code / skills-directory agents - confirm the skills landed
ls ~/.claude/skills/ | grep -E "design-|grill-me|brief-to-tasks"

# Review a SKILL.md directly before installing
curl -fsSL https://raw.githubusercontent.com/julianoczkowski/designer-skills/main/design-brief/SKILL.md | head -40
```

Installs track the latest commit on `main`, so the raw fetch above matches what the installer delivers. Plugin users can confirm the plugin loaded by invoking a skill explicitly, for example `/designer-skills:design-brief`.

## Security

skills.sh verdicts for sampled skills (verified Oct 9, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| design-brief | Pass | Pass | Pass |
| design-tokens | Pass | Pass | Pass |
| frontend-design | Pass | Pass | Pass |

All three sampled skills return Pass across Gen Agent Trust Hub, Socket, and Snyk. The repository ships a SECURITY.md with a responsible-disclosure process and states plainly that its files are instructions for local AI tools: review skills before using them in sensitive or production contexts, and treat them like any other project dependency.

## Limitations

- The flow is interactive, not hands-off: /design-flow confirms between steps, and /design-review runs only on request, after you have something built.
- /frontend-design is mobile-first by mandate (375px layout first, then scaling up); desktop-first teams should expect that build order.
- The skills write design documents into your repository under `.design/`, named per feature, so plan for version-control hygiene.
- Aesthetic output is opinionated, not measured: the 8 philosophies are a menu with concrete parameters, and naming one (or describing a vibe) is what anchors the result.
- Snapshot data, verified Oct 9, 2026: 43,011 combined skills.sh installs across 8 indexed listings; 578 GitHub stars; Apache-2.0; last pushed Jul 6, 2026. Counts drift over time.

## Related

- [Emil Kowalski Skills - Design Engineering Suite Setup](/hermes/skills/catalog/emilkowalski-skills-setup) - interaction and motion craft once the process reaches the UI layer
- [Uizze UI Skills - Anti-UI-Slop Design Quality Setup](/hermes/skills/catalog/uizze-ui-skills-setup) - screenshot-based slop detection to gate the frontend build step
- [Better UI Skills - Interface Polish Suite Setup](/hermes/skills/catalog/better-ui-skills-setup) - the polish layer for agent-built interfaces
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start greenfield features with /design-flow, then switch to individual skills when resuming later - the flow detects which features exist and where you left off.
- Name the philosophy when you have a brand direction ("build this in a Dieter Rams style"); if you leave it open, the skill picks one based on context and tells you which.
- Answer /grill-me honestly and completely - it is where unresolved decisions get caught before they turn into rework.
- Keep the `.design/` folder in version control: every later skill reads from the same feature subfolder, so the brief and tokens stay the single source of truth.
- Run /design-review after you have something built, and use screenshot-based review when you want the critique to reflect what users actually see.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
