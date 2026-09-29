---
title: "Meng To Skills Setup Guide for Hermes Agents"
description: "mengto/skills - 76.2K installs across 155 skills, 5.6K stars: Design+Code founder Meng To's frontend, motion, and visual design suite - landing pages, GSAP, Three.js, anti-slop auditing, and design taste."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/mengto-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-29"
tags: ["hermes skill", "agent skill", "skill setup", "design", "frontend", "motion", "gsap", "threejs", "anti-ai-slop"]
---

# Meng To Skills - Setup Guide

**Source:** [mengto/skills](https://skills.sh/mengto/skills) (76.2K installs across 155 skills)
**GitHub:** [mengto/skills](https://github.com/mengto/skills) (5.6K stars)
**Skills:** 155 skills; top skills: `landing-page` (857), `animation-on-scroll` (848), `animation-systems` (823)
**Category:** Design / Frontend & Motion
**First Seen:** skills.sh Feb 7, 2026; catalogued in the Aug 31, 2026 sweep
**Quality Tier:** 🟢 Production - publisher authority (Meng To, founder of Design+Code) and all three skills.sh security audits Pass (see Security Audit Status)

Meng To - founder of Design+Code and one of the most followed design educators in the developer community - publishes a 155-skill visual design suite. It spans the full agent-design surface: high-conversion landing pages and pricing pages, motion systems (GSAP, Lenis, scroll-triggered storytelling), 3D and WebGL (Three.js, globe particles, laser effects), layout systems (brutalist, editorial, glass-dark), and asset generation (Unsplash images, company logos).

The suite is notable for its **self-auditing layer**: `no-ai-design-slop` and `audit-ai-design-slop` teach agents to detect and remove exactly the visual patterns that flag machine-generated design, and `design-taste-frontend` plus `gpt-taste` encode taste as a procedural skill. The `landing-page` skill is a worked example of the suite's discipline: a landing page wins one intent (one offer, one audience, one primary action), with purpose, offer, and conversion defined before any design work starts.

---

## Installation

```bash
npx skills add mengto/skills
```

Or per-skill:

```bash
npx skills add https://github.com/mengto/skills --skill landing-page
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js** | Recent LTS for the `npx skills` installer |
| **Web context** | Most skills target HTML/CSS/JS output; no build toolchain required |

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| landing-page | 857 | High-conversion landing pages: one offer, one audience, one primary action |
| web-technique-to-skill | 839 | Converts web techniques into installable skills (added Sep 29, 2026 sweep) |
| animation-on-scroll | 848 | Scroll-triggered reveals and entrance animations |
| animation-systems | 823 | Designing cohesive motion systems rather than one-off effects |
| threejs | 810 | 3D scenes and objects with Three.js |
| cinematic-gsap-lenis-motion-system | 807 | Cinema-grade scroll motion with GSAP + Lenis |
| cinematic-scroll-storytelling | 781 | Narrative scroll sequences |
| design-first-ui-prompting | 762 | Prompting models for design-first UI output |
| gsap | 757 | Core GSAP animation patterns |
| beautiful-shadows | 742 | Depth and shadow systems that read as designed |
| progressive-blur | 737 | Layered blur treatments |
| tailwindcss | 736 | Tailwind-driven layout and styling |

Plus `build-awwwards-quality-sites`, `pricing-page`, `masked-reveal`, `no-ai-design-slop`, `audit-ai-design-slop`, `elevenlabs-tts`, `copywriting`, `seo-audit`, `playwright`, and 130+ more layout, motion, and asset skills.

New in the Sep 27, 2026 sweep: `operational-enterprise-ai` (986 installs - enterprise AI operations workflow) and `add-mouse-driven-orbit` (800 installs - mouse-driven 3D orbit interaction), bringing the suite to 155+ indexed skills.

## Security Audit Status (skills.sh, verified Aug 31, 2026)

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| landing-page | Pass | Pass | Pass |

All three audits Pass - the basis for the 🟢 Production tier.

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Public pages that convert** | `landing-page` and `pricing-page` encode conversion discipline for the pages CorpusIQ agents generate |
| **Visual answers** | Motion and layout skills (masked reveal, staggered word reveal, scroll sequences) elevate agent-generated report and answer pages |
| **Anti-slop enforcement** | `audit-ai-design-slop` and `no-ai-design-slop` are runnable counterparts to CorpusIQ's own content-voice rules |
| **Video and motion assets** | GSAP, Lenis, and Three.js skills feed the HyperFrames and UGC pipeline's frontend layers |

## Limitations / Verification

- 155 skills means heavy install weight; install per-skill (`--skill <name>`) when only a few are needed.
- Skills are design-direction knowledge, not libraries: they guide code generation but ship no bundled components.
- Individual install counts are modest (top skill 857); the 76.2K total reflects long-tail breadth across the suite.

Verification after install:

```bash
npx skills add mengto/skills --list    # 155 skills discovered
```

## Related

- [Hallmark Design Skill Setup](/docs/hermes/skills/catalog/hallmark-setup)
- [Skills Catalog](/docs/hermes/skills/catalog) - full quality-tiered directory

---

*← [Skills Catalog](/docs/hermes/skills/catalog) | [Skills Marketplace](/docs/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
