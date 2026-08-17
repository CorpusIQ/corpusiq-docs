---
title: "UI/UX Pro Max — 19-Skill Design System Pack Setup"
description: "nextlevelbuilder/ui-ux-pro-max-skill — 19 skills, 611.4K combined installs. Design systems, brand, banner design, and slides for agents building production interfaces."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ui-ux-pro-max-setup/"
robots: "index,follow"
last_updated: "2026-08-13"
tags: ["hermes skill", "agent skill", "skill setup", "design"]
---

# UI/UX Pro Max — Setup Guide

**Source:** [skills.sh](https://www.skills.sh/nextlevelbuilder/ui-ux-pro-max-skill) (611.4K combined installs)
**GitHub:** [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
**Category:** Design & UI
**First Seen:** August 13, 2026 sweep
**Quality Tier:** 🟢 Production

The largest general-purpose UI/UX skill pack for agents outside the framework-official ones. The flagship `ui-ux-pro-max` (314K installs) is a full interface-design workflow; the `ckm:*` variants are Claude-Knowledge-Module ported copies of the same core skills. Covers design systems, styling, brand application, banner/ad design, and slide decks — the complete surface area of an agent doing marketing and product visuals.

---

## Installation

```bash
npx skills add nextlevelbuilder/ui-ux-pro-max-skill
```

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| ui-ux-pro-max | 314.0K | Full UI/UX design workflow — discovery to polished screens |
| ckm:design-system | 32.8K | Design-system construction (tokens, components, scales) |
| ckm:design | 32.5K | Interface design principles and process |
| ckm:ui-styling | 32.5K | Styling craft — spacing, typography, color |
| ckm:brand | 32.0K | Brand identity application across surfaces |
| ckm:banner-design | 32.0K | Ad and banner creative |
| ckm:slides | 31.9K | Presentation slide design |
| design-system / design / ui-styling / brand / banner-design / slides | 16–18K each | Plain (non-ckm) versions of the above |

## Prerequisites

- Figma or a component library target (React/Vue/HTML) for the design-system skills
- No API keys required — pure procedural knowledge

## CorpusIQ Use Cases

- **Social creative pipeline** — `banner-design` + `brand` feed the daily X/LinkedIn post images (Postiz pipeline) with consistent brand application
- **Slides for operator-facing content** — `slides` for the McKinsey-format daily report decks
- **Design-system governance** — `ckm:design-system` aligns agent-built marketing pages with the CorpusIQ brand tokens

## Limitations / Verification

- Two parallel naming tracks (plain vs `ckm:` prefixed) duplicate content — install the `ckm:` set only if your agent runs the Claude Knowledge Module system; otherwise use the plain set
- Verify: `ls` the skills directory for `ui-ux-pro-max` and confirm the 314K-install flagship is present

## Related

- [Emil Kowalski Skills — Design Engineering Suite Setup](/hermes/skills/catalog/emilkowalski-skills-setup/)
- [Uizze UI Skills — Anti-UI-Slop Design Quality Setup](/hermes/skills/catalog/uizze-ui-skills-setup/)
