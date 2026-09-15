---
title: "Owl Listener Designer Skills - 107-Skill Design Suite Setup"
description: "owl-listener/designer-skills - 107 skills, 124.7K combined installs. Agentic design skills from research to systems: presentation decks, design tokens, typography and color systems, accessibility audits, UX writing, and Gestalt-law-driven layout judgment."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/owl-listener-designer-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-31"
tags: ["hermes skill", "agent skill", "skill setup", "design"]
---

# Owl Listener Designer Skills - Setup Guide

**Source:** [skills.sh](https://www.skills.sh/owl-listener/designer-skills) (124.7K combined installs)
**GitHub:** [owl-listener/designer-skills](https://github.com/owl-listener/designer-skills) (2,437⭐, MIT)
**Category:** UI/UX & Visual Design
**First Seen:** March 9, 2026 (skills.sh)
**Quality Tier:** 🟢 Production (Gen Agent Trust Hub Pass / Socket Pass / Snyk Pass)

The largest design-focused skill collection on skills.sh: 107 agentic skills, commands, and plugins covering the full design lifecycle - research (user-persona, journey-map, competitive-analysis), systems (design tokens, color/typography/spacing systems, theming), specification (wireframe-spec, component-spec, micro-interaction-spec), evaluation (heuristic-evaluation, accessibility-audit, design-qa-checklist), and presentation (presentation-deck with stakeholder-update, design-review, and showcase structures). Includes a psychology layer (Gestalt laws, Jakob's Law, Tesler's Law, peak-end rule) for judgment calls.

---

## Installation

```bash
npx skills add owl-listener/designer-skills --skill presentation-deck
npx skills add owl-listener/designer-skills --skill design-token
npx skills add owl-listener/designer-skills --skill accessibility-audit
# Or install the full collection from the publisher page
```

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| presentation-deck | 2.1K | Structured design presentations (stakeholder update, review, showcase, case study) |
| typography-scale / color-system / spacing-system / layout-grid | 1.5-1.7K | Foundational design systems |
| visual-hierarchy / design-principles | 1.6K / 1.4K | Layout and hierarchy judgment |
| design-token / design-token-audit / theming-system | 1.4K | Token architecture and governance |
| wireframe-spec / component-spec / prototype-strategy | 1.4-1.5K | Specification and prototyping |
| accessibility-audit / design-qa-checklist | 1.4K | Quality gates before ship |
| ux-writing / error-handling-ux / loading-states | 1.4K | Interface copy and states |
| user-flow-diagram / journey-map / experience-map | 1.4-1.5K | Flow and experience mapping |
| heuristic-evaluation / design-critique / usability-test-plan | 1.4-1.5K | Evaluation methods |
| law-of-* (Gestalt laws), jakobs-law, teslers-law, zeigarnik-effect, peak-end-rule | 317-338 | Psychology-driven design judgment |
| interfaces-that-feel / conversational-ux / business-design | 318-740 | Interaction quality and business framing |
| (≈57 more) | <1.5K each | critique-* family, personas, naming, case studies, platform conventions |

## Prerequisites

- None - prompt-skill collection; no API keys or design-tool licenses
- Pairs with any frontend stack; token skills output framework-agnostic JSON/YAML

## CorpusIQ Use Cases

- **Brand visual systems** - token/color/typography skills supply the systematic layer for CorpusIQ's branded assets (ad images, dashboards, docs)
- **Product UX evaluation** - heuristic-evaluation and accessibility-audit skills are ready-made QA passes for CorpusIQ's product surface
- **Operator-facing decks** - presentation-deck's stakeholder-update structure is directly reusable for weekly operator/investor updates

## Limitations / Verification

- 107 skills is a lot of surface; install flagship skills (presentation-deck, design-token, accessibility-audit) rather than the full set
- Design judgment skills don't generate pixels - they structure agent reasoning; pair with image/UI tooling
- Verify install: `npx skills list | grep -E "presentation-deck|design-token"`

## Security

[Gen Agent Trust Hub: Pass](https://www.skills.sh/owl-listener/designer-skills/presentation-deck/security/agent-trust-hub) · [Socket: Pass](https://www.skills.sh/owl-listener/designer-skills/presentation-deck/security/socket) · [Snyk: Pass](https://www.skills.sh/owl-listener/designer-skills/presentation-deck/security/snyk)

## Related

- [Emil Kowalski Design Skills](/docs/hermes/skills/catalog/emilkowalski-skills-setup)
- [Superdesign Setup](/docs/hermes/skills/catalog/superdesign-skill-setup)
- [Meng To Skills - Frontend & Motion Design Suite](/docs/hermes/skills/catalog/mengto-skills-setup)
