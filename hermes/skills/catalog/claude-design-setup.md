---
title: claude-design — Setup Guide
description: Apply Claude/Apple design philosophy to any project — interface design, fluid physics, and animation principles for Hermes agents.
---

# claude-design — Setup Guide

**Source:** [nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent)
**Skill:** `claude-design`
**Installs:** 383

The `claude-design` skill encodes Apple and Anthropic's approach to interface design and animation. It enables Hermes agents to apply principles of fluid motion, physics-based interaction, and minimal visual language to any project — from web apps to terminal interfaces.

## Installation

```bash
npx skills add https://github.com/nousresearch/hermes-agent --skill claude-design
```

After install, reload skills:
- Hermes CLI: `/reload-skills` or restart session
- Hermes gateway: `/restart` or `hermes gateway restart`

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Hermes Agent | v0.16.0+ |
| Design project | Codebase, UI framework, or terminal app |

## Capabilities

| Capability | Trigger | Output |
|-----------|---------|--------|
| Design critique | "Review this UI for design quality" | Design audit with Apple/Claude principles |
| Animation guidance | "How should this element animate?" | Fluid animation specification |
| Component design | "Design a settings panel" | Component spec with interaction states |
| Design system audit | "Audit our design system" | Gap analysis against Apple HIG |
| Typography | "Pick fonts for a dashboard" | Typography recommendations |

## Key Principles Applied

- **Fluid motion**: Spring physics, no linear easing
- **Direct manipulation**: Touch/click response mirrors physical world
- **Progressive disclosure**: Show complexity on demand
- **Minimalism**: Remove before adding
- **Visual hierarchy**: Typography and spacing as primary tools

## CLI/Command Reference

The skill integrates with Hermes' design capabilities:
- `skill_view(name='claude-design')` — Load design principles
- Use `browser_vision()` to inspect UI screenshots against design principles
- Combine with `apple-design` and `emil-design-eng` skills for full design coverage

## CorpusIQ Use Cases

1. **Product UI audit** — Review CorpusIQ dashboard against Apple HIG
2. **Marketing pages** — Design landing pages with fluid animation guidance
3. **Agent UI components** — Design terminal and web interfaces for Hermes agents
4. **Component library** — Establish design tokens and interaction patterns
5. **Animation specification** — Define fluid transitions for CorpusIQ interfaces

## Troubleshooting

| Issue | Likely Cause | Resolution |
|-------|-------------|------------|
| Design feedback too generic | Missing project context | Provide code/URL/screenshots |
| Animation specs unclear | No example provided | Include a reference animation URL |
| Principles conflict | Multiple design traditions | Specify which tradition to use (Apple vs Material) |

## Verification

After installation, verify the skill is loaded:
```bash
hermes skills list | grep claude-design
```

Test with a design critique:
```
"Review the dashboard @ https://app.corpusiq.io and apply Apple design principles"
```
