---
title: impeccable-design-polish - Post-Generation Design Polish Skill for Hermes Agents
description: "Install and use nexu-io/open-design@impeccable-design-polish (2K+ installs) - follow-up design polish inspired by Impeccable: audit, critique, polish, animate, harden and prep HTML artifacts for live/share."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/impeccable-design-polish-setup/"
robots: "index,follow"
last_updated: "2026-09-09"
tags: ["hermes skill", "agent skill", "skill setup", "design polish", "anti-ai-slop"]
---

# impeccable-design-polish - Setup Guide

**Source:** [nexu-io/open-design](https://skills.sh/nexu-io/open-design/impeccable-design-polish) (2,072 installs)
**Skill:** `nexu-io/open-design@impeccable-design-polish`
**Installs:** 2,072
**Category:** Design / Frontend Quality
**First Seen:** Sep 9, 2026

`impeccable-design-polish` is the post-generation pass for an existing design. It does not restart a project from scratch - it makes the current HTML artifact sharper, more usable, and closer to something a designer would ship. Inspired by [pbakaus/impeccable](/docs/hermes/skills/catalog/impeccable-design-setup) but a distinct skill from the Open Design project (the "Claude Design alternative" - local-first desktop app for design via coding agents, HTML/PDF/PPTX/MP4 export).

---

## Installation

```bash
npx skills add nexu-io/open-design --skill impeccable-design-polish
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | Any recent version with skill support |
| **Node.js 18+** | For the `npx skills` CLI |
| **An existing web/HTML artifact** | The skill is a follow-up pass, not a greenfield generator |

---

## What It Provides

| Mode | Trigger | What It Does |
|---|---|---|
| **Audit** | "audit this page" | Identify highest-impact issues in hierarchy, spacing, color, type, interaction states, responsiveness, accessibility |
| **Critique** | "critique design" | Explain what feels generic, overdesigned, underdesigned, or inconsistent |
| **Polish** | "polish page" | Directly edit the artifact to fix the top issues while preserving user intent |
| **Animate** | "animate page" | Add restrained, useful motion only where it improves feedback or storytelling |
| **Harden** | "harden ui" | Repair mobile overflow, text clipping, contrast problems, missing states, broken links, fragile layout |
| **Live** | "live review" | Prepare the artifact for presentation/sharing: final visual QA and clear next actions |

**Anti-AI-slop rules** (built in): remove purple-blue glow gradients with no product reason, generic 3-card feature rows, oversized rounded cards, empty marketing adjectives, inconsistent spacing/type scale, and decorative effects that don't support comprehension. Preserve accessibility: focus states, contrast, semantic controls, reduced-motion fallbacks.

**Best pairings:** `design-taste-frontend` or `gpt-taste` for stronger anti-slop redesign; `emilkowalski-motion` or GSAP skills for motion-specific polish; image/video skills when the artifact needs real assets instead of CSS-only decoration.

## Quick Start

1. Install: `npx skills add nexu-io/open-design --skill impeccable-design-polish`
2. Generate a page with any agent flow, then invoke: "Use impeccable-design-polish on the current HTML artifact: audit visual hierarchy, remove AI tells, tighten copy, add restrained motion, harden responsive/accessibility issues"
3. Operating rules: inspect the current page before editing; keep existing content/brand/scenario; prefer a few decisive fixes over broad cosmetic churn; finish with the artifact in a better runnable state, not just a critique list

## Limitations / Verification

```bash
# Verify skill installed
hermes skills list | grep impeccable-design-polish

# Functional test
# Generate any HTML page, then ask for the polish pass and confirm the artifact was edited, not just critiqued
```

- Distinct from pbakaus/impeccable (setup guide [here](/docs/hermes/skills/catalog/impeccable-design-setup)) - same inspiration, different publisher and scope: this one is a follow-up polish pass, not a full design brain
- Triggers include Chinese "反 AI 味" (anti-AI taste) - useful for CN-market artifacts

## Security

- [skills.sh listing](https://skills.sh/nexu-io/open-design/impeccable-design-polish) - Pass
- [GitHub repo](https://github.com/nexu-io/open-design) - Pass (not a fork; original project)
- Upstream inspiration: [pbakaus/impeccable](https://github.com/pbakaus/impeccable) - Pass

## Related

- [impeccable - Design Quality Skills Setup](/docs/hermes/skills/catalog/impeccable-design-setup)
- [Design Review Setup](/docs/hermes/skills/catalog/design-review-setup)
- [Matt Pocock Agent Workflow Suite - 20-Skill Setup](/docs/hermes/skills/catalog/mattpocock-agent-workflow-suite-setup)
