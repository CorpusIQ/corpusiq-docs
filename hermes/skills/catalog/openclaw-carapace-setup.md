---
title: OpenClaw Carapace — Design System Skills Setup Guide for Hermes Agents
description: Install and use the official OpenClaw design system package (openclaw/carapace) — 6 skills covering brand identity, UI primitives, marketing pages, and design audits. 2.3K combined installs.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/openclaw-carapace-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# OpenClaw Carapace — Setup Guide

**Source:** [openclaw/carapace](https://skills.sh/openclaw/carapace) (2.3K combined installs)
**GitHub:** [github.com/openclaw/carapace](https://github.com/openclaw/carapace) (4⭐)
**Category:** Design System / UI Engineering
**First Seen:** July 21, 2026
**Security:** Gen Agent Trust Hub Pass · Socket Pass (Warn on `openclaw-design`) · Snyk Pass

Carapace is the official OpenClaw design system, packaged as six focused skills. Instead of one monolithic design rulebook, each skill owns one surface. A router skill (`openclaw-design`) dispatches to the correct branch so the agent only loads what the task needs.

---

## Installation

```bash
# Install all six skills from the repo
npx skills add https://github.com/openclaw/carapace

# Or install individually
npx skills add https://github.com/openclaw/carapace --skill openclaw-design
npx skills add https://github.com/openclaw/carapace --skill openclaw-brand
npx skills add https://github.com/openclaw/carapace --skill openclaw-carapace
npx skills add https://github.com/openclaw/carapace --skill openclaw-marketing-pages
npx skills add https://github.com/openclaw/carapace --skill openclaw-design-audit
npx skills add https://github.com/openclaw/carapace --skill openclaw-design-system
```

---

## The Six Skills

| Skill | Installs | Use For |
|---|---|---|
| `openclaw-design` | 379 | Router — chooses the focused branch before changing any interface |
| `openclaw-brand` | 379 | Identity: typography, logos, imagery, voice, non-product brand artifacts |
| `openclaw-carapace` | 369 | App UI: semantic tokens, themes, component reuse, framework adapters |
| `openclaw-marketing-pages` | 379 | Public pages: landing/content composition, navigation, SEO, responsive layout |
| `openclaw-design-audit` | 379 | Design drift, token misuse, component substitution, accessibility, recurring audits |
| `openclaw-design-system` | 378 | v0.1.x compatibility alias for projects upgrading an existing skill lock |

**Routing rule:** for a public website change start with `openclaw-marketing-pages`, adding `openclaw-brand` only when the task changes identity, logo, imagery, typography, or voice. For a product application start with `openclaw-carapace`. Load multiple branches only when the task genuinely crosses them.

---

## Working With openclaw-carapace

The core skill enforces a read-then-build workflow over five reference files:

1. `references/tokens.md` — read before choosing colors, spacing, type, radii, or shadows
2. `references/consumer-adapters.md` — current framework adapter conventions
3. `references/application-surfaces.md` — shells, panes, settings, operational screens
4. `references/terminal-ui.md` — terminal interface design and auditing
5. `references/embedded-surfaces.md` — surfaces rendered inside host frames (MCP apps)

Core rules: use semantic tokens for UI intent and palette primitives only for documented exceptions; keep application behavior, routes, and information architecture unchanged unless the task says otherwise; validate affected routes with existing tests and real browser screenshots; inspect the consumer's existing shared primitives before creating a new component.

---

## Prerequisites

| Requirement | Details |
|---|---|
| Node.js + npx | For the skills.sh CLI install path |
| OpenClaw or Clawd runtime | Skills target OpenClaw interfaces; guidelines are reusable in Hermes UI work |
| Git access | For direct clone installs |

Direct clone alternative:

```bash
git clone --depth 1 https://github.com/openclaw/carapace.git /tmp/carapace
cp -r /tmp/carapace/openclaw-* ~/.clawd/skills/
```

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **UI surface audits** | Run `openclaw-design-audit` methodology against agent-built dashboards to catch token misuse and drift |
| **Landing page composition** | `openclaw-marketing-pages` for SEO-aware, responsive public pages |
| **Terminal UI polish** | `terminal-ui.md` reference when building or auditing TUI surfaces |
| **Brand consistency** | `openclaw-brand` when identity, voice, or imagery is involved in generated copy |
| **Framework adapter decisions** | `consumer-adapters.md` before choosing React/Vue/vanilla adapters in agent projects |

---

## Limitations / Verification

- Low GitHub star count (4⭐) and first seen July 21, 2026 — young package, follow release cadence
- `openclaw-design-system` is a compatibility alias, not new functionality — install only when upgrading old locks
- Verify install: `npx skills list | grep -i carapace` should show six entries
- Security posture is clean on all three scanners (Socket flags one Warn on the router skill)

---

## Related

- [Discovery Page — Aug 12 OpenClaw Ecosystem Sweep](/hermes/skills/marketplace/new-aug12-2026-openclaw-ecosystem/)
- [OpenClaw Ecosystem June 26 Setup](/hermes/skills/catalog/openclaw-ecosystem-june26-setup/)
- [Skills Catalog](/hermes/skills/catalog/)

*Powered by CorpusIQ*
