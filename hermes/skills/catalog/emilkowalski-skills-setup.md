---
title: Emil Kowalski Skills — Design Engineering Suite Setup Guide for Hermes Agents
description: "10 design-engineering skills from Emil Kowalski (Sonner, vaul) — 694.4K combined installs. Interface polish, animation review, Apple-design vocabulary, UI library selection, and prototyping for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/emilkowalski-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-13"
tags: ["hermes skill", "agent skill", "skill setup", "design"]
---

# Emil Kowalski Skills — Setup Guide

**Source:** [skills.sh](https://www.skills.sh/emilkowalski/skills) (694.4K combined installs)
**GitHub:** [emilkowalski/skills](https://github.com/emilkowalski/skills)
**Category:** Design Engineering
**First Seen:** August 13, 2026 sweep
**Quality Tier:** 🟢 Production

Emil Kowalski is the creator of [Sonner](https://sonner.emilkowalski.com) (the toast library) and vaul, and one of the most-copied voices in agent UI quality. His skill pack is the highest-signal design-quality layer on skills.sh: it teaches agents to recognize bad AI-generated UI, audit motion instead of sprinkling it, and pick the right library before writing a component. `emil-design-eng` is the flagship at 204.4K installs.

---

## Installation

```bash
npx skills add emilkowalski/skills
```

Installs all 10 skills. Hermes: place the SKILL.md files under your agent's skills directory, or run inside any skills.sh-compatible agent (Claude Code, Codex, Cursor, Hermes, OpenClaw, Nous Research).

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| emil-design-eng | 204.4K | Fluid, tactile interface design — the core design-engineering doctrine |
| review-animations | 97.6K | Adversarial review of animation/motion code against craft bars |
| animation-vocabulary | 85.1K | Reverse-lookup glossary: vague descriptions → named motion primitives |
| apple-design | 77.0K | Apple's HIG-informed approach to fluid, physical interfaces |
| improve-animations | 70.1K | Senior-engineer pass over a codebase's animation and motion code |
| find-animation-opportunities | 58.7K | Scan a UI for places that should animate but don't |
| pick-ui-library | 44.8K | Choose the right frontend library for the task before building |
| prototype | 34.0K | Build multiple genuinely different UI versions of a piece |
| animate | 16.8K | Build an animation from scratch, making the decisions |
| ask-sonner | 5.9K | Sonner-specific component guidance |

## Prerequisites

- A frontend project (React-based for most skills; ask-sonner requires Sonner)
- Access to motion libraries (Framer Motion / Motion One) for animation skills

## CorpusIQ Use Cases

- **UI quality gate for agent-built dashboards** — run `review-animations` + `improve-animations` before shipping any agent-generated frontend, the same way `anti-ui-slop` gates visual design
- **Docs site polish** — `find-animation-opportunities` on docs.corpusiq.io surfaces motion gaps in landing and onboarding flows
- **Design-vocabulary alignment** — `animation-vocabulary` gives team prompts shared language when briefing video/graphics work (pairs with the HyperFrames pipeline)

## Limitations / Verification

- Quality-tier judgement is subjective — the skills encode opinions, not measurements; treat verdicts as review feedback, not tests
- Verify installation with `ls ~/.claude/skills/ | grep -i emil` or your agent's equivalent skills directory listing

## Related

- [Uizze UI Skills — Anti-UI-Slop Design Quality Setup](/hermes/skills/catalog/uizze-ui-skills-setup/)
- [Extract Design System — UI Token & Component Extraction Setup](/hermes/skills/catalog/extract-design-system-setup/)
- [Apple Design](https://developer.apple.com/design/human-interface-guidelines)
