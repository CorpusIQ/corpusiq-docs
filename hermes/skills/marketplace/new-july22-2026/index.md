---
title: "New Skills — July 22, 2026 Marketplace Sweep"
description: "2 new Hermes-bundled skills discovered on skills.sh not yet documented. 844+ combined installs. Official Hermes skills from nousresearch/hermes-agent."
---

# New Skills — July 22, 2026

Skills discovered during the July 22 early-morning marketplace sweep. 2 new setup guides created for Hermes agents. These are official bundled skills from nousresearch/hermes-agent that were missing from our documentation catalog.

## Summary

| Metric | Count |
|---|---|
| New skills found | 2 |
| Setup guides created | 2 |
| Combined installs | ~844+ |
| Quality: 🟢 Production | 2 |

## New Skills

### Creative & Design

| Skill | Publisher | Installs | Tier | Guide |
|---|---|---|---|---|
| **popular-web-designs** | nousresearch/hermes-agent | 451 | 🟢 | [Setup Guide](/hermes/skills/catalog/popular-web-designs-setup/) |

### Productivity

| Skill | Publisher | Installs | Tier | Guide |
|---|---|---|---|---|
| **powerpoint** | nousresearch/hermes-agent | 393 | 🟢 | [Setup Guide](/hermes/skills/catalog/powerpoint-setup/) |

## Skill Details

### popular-web-designs (451 installs)

54 real-world design systems (Stripe, Linear, Vercel, Apple, Airbnb, Notion, Supabase, and 48 more) as HTML/CSS templates. Each template captures a site's complete visual language: color palette, typography hierarchy, component styles, spacing system, shadows, and responsive behavior. Includes Hermes-specific implementation notes with CDN font substitutes and Google Fonts `<link>` tags.

Pairs with `claude-design` for design process and `generative-widgets` for live preview via cloudflared tunnel.

### powerpoint (393 installs)

Complete PowerPoint creation, reading, and editing. Supports from-scratch generation via pptxgenjs, template-based XML manipulation, speaker notes, native charts, and design QA via LibreOffice. Includes 20+ documented gotchas (hex color format, shadow offsets, chart data labels), 10 curated color palettes, and comprehensive validation scripts.

Part of the Hermes office suite alongside `docx`, `xlsx`, and `pdf`.

## Notes

- Both skills are official Hermes bundled skills from the nousresearch/hermes-agent repository
- These were missing from our documentation catalog despite being available on skills.sh
- Discovered by cross-referencing the 183 SKILL.md files in nousresearch/hermes-agent against our existing catalog of 248+ setup guides
- All setup guides follow the standard format with installation, usage, related skills, and verification sections
- Total catalog now covers 349+ Hermes-relevant skills from skills.sh and community sources
