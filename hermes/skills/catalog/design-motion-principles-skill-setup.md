---
title: Design Motion Principles Skill — Motion & Interaction Setup
description: "kylezantos/design-motion-principles — design-motion-principles (7.8K installs): create and audit purposeful UI motion across HTML/CSS, React, Framer Motion, and native transitions. All three security audits pass."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/design-motion-principles-skill-setup/"
robots: "index,follow"
last_updated: "2026-08-15"
tags: ["hermes skill", "agent skill", "skill setup", "motion design", "animation", "interaction design"]
---

# Design Motion Principles Skill — Setup Guide

**Source:** [kylezantos/design-motion-principles](https://skills.sh/kylezantos/design-motion-principles)
**GitHub:** [kylezantos/design-motion-principles](https://github.com/kylezantos/design-motion-principles) (908 stars)
**Skills:** 1 skill (`design-motion-principles`) · 7.8K installs
**Category:** Motion & Interaction Design
**First Seen:** Jan 19, 2026 (catalogued August 15, 2026 midday sweep)
**Quality Tier:** 🟢 Production (all three security audits pass — Gen Agent Trust Hub, Socket, Snyk)

This skill makes the agent a senior design engineer for motion and interaction design, with two modes: Create (build interactive components with purposeful motion via workflows/create.md) and Audit (review existing motion and report findings via workflows/audit.md). It covers HTML/CSS, React, Framer Motion / Motion, iOS/Android transitions, and design-system animations.

---

## Installation

```bash
npx skills add kylezantos/design-motion-principles --skill design-motion-principles
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **Frontend project** | For Create mode; any UI with motion for Audit mode |

## What It Provides

| Capability | Notes |
|---|---|
| Create mode | Build interactive components with purposeful motion |
| Audit mode | Review existing motion design and report findings |
| Frequency framework | Applies beyond the web (game engines, Lottie, Rive, video) |
| Mode detection | Explicit routing table for create/audit/ambiguous requests |

## Quick Start

1. Install: `npx skills add kylezantos/design-motion-principles --skill design-motion-principles`
2. Ask: "audit the motion in this UI and report what is purposeless" or "animate this modal with purposeful motion"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **UI polish** | Purposeful-motion doctrine for product and client interfaces |
| **Motion audits** | Pre-ship audit pass for animation quality |
| **HyperFrames complement** | The frequency framework informs our video motion work |
| **Design-system animation** | Guidance for animation tokens in design systems |

## Limitations / Verification

- Designer-specific techniques may not translate to game engines, Lottie, Rive, or video — only the frequency framework does
- Single-skill cluster; all three audits pass (verified on skill page)

```bash
npx skills add kylezantos/design-motion-principles   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
