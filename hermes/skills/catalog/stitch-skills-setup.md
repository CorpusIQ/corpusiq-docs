---
title: Stitch Skills — Google Design-to-Code Pipeline for Hermes Agents
description: Transform designs into production React/Shadcn code with Google's Stitch. 285K+ combined installs across 6 skills. Design MD, React generation, prompt enhancement, and Remotion video — official Google Labs project.
---

# Stitch Skills — Setup Guide

**Source:** [google-labs-code/stitch-skills](https://skills.sh/google-labs-code/stitch-skills) (285K+ combined installs)
**Category:** Development / AI-Assisted Design
**Quality Tier:** 🟡 Beta

Google Labs' Stitch — a design-to-code pipeline that transforms Figma designs, screenshots, or design markdown into production-ready React components with Shadcn UI. Includes prompt enhancement, iteration loops, and Remotion video generation. Five new skills for Hermes development agents (Remotion already catalogued separately).

---

## Installation

```bash
npx skills add google-labs-code/stitch-skills --skill design-md
npx skills add google-labs-code/stitch-skills --skill react
npx skills add google-labs-code/stitch-skills --skill enhance-prompt
npx skills add google-labs-code/stitch-skills --skill stitch-loop
npx skills add google-labs-code/stitch-skills --skill shadcn-ui
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **design-md** | 55.5K | Convert visual designs (Figma, screenshots) to structured Design Markdown |
| **react** | 50.4K | Generate React components from Design MD or descriptions |
| **enhance-prompt** | 50.3K | Improve design prompts for better code generation output |
| **stitch-loop** | 48.8K | Iterative refinement cycle — generate, review, fix, repeat |
| **shadcn-ui** | 45.7K | Generate Shadcn UI components with proper theming and accessibility |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **React project** | Next.js, Vite, or any React framework |
| **Shadcn UI** | Optional — `shadcn-ui` skill expects Shadcn initialized |
| **Figma access** | Optional — for `design-md` with Figma URLs |

---

## Key Capabilities

### Design Markdown (design-md)
Convert any visual design source into structured Design Markdown — a machine-readable design spec format. Accepts Figma URLs, screenshots, sketches, or text descriptions. Outputs layout hierarchy, component tree, spacing tokens, color palette, and typography scale.

### React Generation (react)
Generate production React components from Design MD or natural language descriptions. Produces functional components with proper TypeScript types, responsive layouts, and accessibility attributes. Supports Tailwind CSS and CSS Modules.

### Prompt Enhancement (enhance-prompt)
Improve design-to-code prompts by adding missing context: responsive breakpoints, dark mode, loading states, error boundaries, and accessibility requirements. Reduces iteration cycles by frontloading edge cases.

### Iteration Loop (stitch-loop)
Automated refinement cycle: generate code → visual diff → identify issues → fix → re-generate. Converges on production-quality output in 3-5 cycles typically.

### Shadcn UI (shadcn-ui)
Generate Shadcn UI components (buttons, dialogs, tables, forms, navigation) with proper theming via CSS variables. Ensures consistency with the Shadcn design system and Radix UI accessibility patterns.

---

## Quick Start

```bash
# Convert a design to structured spec
npx skills use google-labs-code/stitch-skills@design-md

# Generate React components
npx skills use google-labs-code/stitch-skills@react

# Iterate until production-ready
npx skills use google-labs-code/stitch-skills@stitch-loop

# Add Shadcn UI components
npx skills use google-labs-code/stitch-skills@shadcn-ui
```

---

## Verification

```bash
npx skills list | grep stitch
```

---

## Notes

- Google Labs project — experimental but production-quality output
- `remotion` skill (34.5K installs) from the same publisher is catalogued separately at [remotion-best-practices-setup](/hermes/skills/catalog/remotion-best-practices-setup/)
- Design MD format is becoming a standard; compatible with other design-to-code tools
- Best results with `enhance-prompt` before `react` generation
- Quality tier 🟡 Beta: 285K+ combined installs, actively developed by Google Labs
