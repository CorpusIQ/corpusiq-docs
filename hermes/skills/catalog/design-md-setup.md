---
title: DESIGN.md — Full Setup Guide for Hermes Agents
description: Google's open spec for describing visual identity to coding agents. YAML design tokens + Markdown rationale. Lint, diff, and export to Tailwind/W3C DTCG.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/design-md-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# DESIGN.md — Setup Guide

**Source:** [nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent) (227.9K⭐)
**Skill:** `nousresearch/hermes-agent@design-md`
**Installs:** 330
**Category:** Design / Frontend
**First Seen:** Apr 27, 2026

DESIGN.md is Google's open spec (Apache-2.0, [`google-labs-code/design.md`](https://github.com/google-labs-code/design.md)) for describing a visual identity to coding agents. One file combines YAML front matter (machine-readable design tokens) with Markdown prose (human-readable rationale). The CLI lints structure + WCAG contrast, diffs versions for regressions, and exports to Tailwind or W3C DTCG JSON.

---

## Installation

```bash
npx skills add nousresearch/hermes-agent@design-md
```

Also install the DESIGN.md CLI:

```bash
npm install -g @google/design.md
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js** | For `@google/design.md` CLI |
| **Hermes Agent** | Any version |
| **A visual identity** | Colors, typography, spacing, and branding decisions documented |

---

## What It Provides

### DESIGN.md File Structure

```yaml
---
# Machine-readable tokens (YAML front matter)
colors:
  primary: '#0a2540'
  accent: '#635bff'
  background: '#ffffff'
  text: '#1a1a2e'
typography:
  heading: 'Inter'
  body: 'Inter'
  mono: 'JetBrains Mono'
spacing:
  unit: 4
  scale: [0, 4, 8, 16, 24, 32, 48, 64]
borderRadius:
  default: 8
  pill: 9999
---

# Human-readable rationale (Markdown body)
## Brand Identity
...
```

### CLI Commands

| Command | Description |
|---|---|
| `npx @google/design.md lint` | Validate structure and WCAG AA contrast ratios |
| `npx @google/design.md diff` | Compare two DESIGN.md versions for regressions |
| `npx @google/design.md export --format tailwind` | Export tokens as Tailwind config |
| `npx @google/design.md export --format dtcg` | Export as W3C Design Tokens Community Group JSON |

---

## Quick Start

```bash
# 1. Install skill + CLI
npx skills add nousresearch/hermes-agent@design-md
npm install -g @google/design.md

# 2. Generate a DESIGN.md scaffold
npx @google/design.md init

# 3. Fill in your brand tokens
# Edit DESIGN.md with your colors, fonts, spacing

# 4. Validate
npx @google/design.md lint

# 5. Export to Tailwind
npx @google/design.md export --format tailwind > tailwind.config.design.js
```

---

## When to Use

Use this skill when:
- User asks for a DESIGN.md file, design tokens, or a design system spec
- User wants consistent UI/brand across multiple projects or tools
- User pastes an existing DESIGN.md and asks to lint, diff, export, or extend it
- User asks to port a style guide into a format agents can consume
- User wants contrast / WCAG accessibility validation on their color palette

---

## Verification

After creating a DESIGN.md:

```bash
# Check structure validity
npx @google/design.md lint

# Verify exports work
npx @google/design.md export --format tailwind | head -20
```

---

## Security

- [Gen Agent Trust Hub: Pass](https://www.skills.sh/nousresearch/hermes-agent/design-md/security/agent-trust-hub)
- [Socket: Pass](https://www.skills.sh/nousresearch/hermes-agent/design-md/security/socket)
- [Snyk: Warn](https://www.skills.sh/nousresearch/hermes-agent/design-md/security/snyk)

---

**Related:** [popular-web-designs-setup.md](popular-web-designs-setup.md)
