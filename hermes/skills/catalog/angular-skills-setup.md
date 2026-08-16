---
title: "Angular Skills — Framework Development Setup"
description: "angular/skills — 2 skills, 40.1K installs: version-aware Angular code generation and new-project scaffolding from the Angular team."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/angular-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-16"
tags: ["hermes skill", "agent skill", "skill setup", "angular", "frontend"]
---

# Angular Skills — Setup Guide

**Source:** [angular/skills](https://skills.sh/angular/skills)
**GitHub:** [angular/skills](https://github.com/angular/skills)
**Skills:** 2 skills · 40.1K total installs
**Category:** Frontend Development
**First Seen:** catalogued August 16, 2026 sweep (angular-developer on skills.sh since March 23, 2026)
**Quality Tier:** 🟢 Production — official Angular org; angular-developer passes all three security audits

The Angular team's official skills teach agents version-aware framework development: analyze the project's Angular version before advising, scaffold with the CLI for consistency, and validate every generated change with `ng build`. A compact, high-signal suite with a build-verification discipline worth copying.

---

## Installation

```bash
npx skills add angular/skills
```

Individual skills install with the explicit repo form:

```bash
npx skills add https://github.com/angular/skills --skill angular-developer
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **Angular CLI** | For scaffolding and `ng build` verification |
| **Existing or new Angular project** | The skills adapt to the detected version |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| angular-developer | 28.7K | Full-stack framework guidance: components, signals, forms, DI, routing, SSR, accessibility, animations, testing |
| angular-new-app | 11.4K | New-project scaffolding with strict `ng new` execution rules |

Key behaviors: version detection before guidance (signal forms recommended for Angular v21+), Angular CLI for all scaffolding, and a hard rule to run `ng build` and fix errors before delivering generated code.

## Quick Start

1. Install: `npx skills add angular/skills`
2. New project: "scaffold a new Angular app with the angular-new-app skill"
3. Existing project: "review this component against current Angular best practices"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Client frontend work** | Version-aware generation prevents obsolete-pattern code in client Angular apps |
| **Build-verify discipline** | The `ng build`-before-delivery rule is a template for our own delivery gates |
| **Migration guidance** | Signals and SSR guidance for modernizing legacy Angular projects |

## Limitations / Verification

- Security audits on angular-developer: Gen Agent Trust Hub Pass, Socket Pass, Snyk Pass — 3/3
- Publisher-page install counts verified (28.7K + 11.4K); GitHub 613 stars
- Only two skills — the suite is deliberately narrow
- Guidance is Angular-specific; no cross-framework value

```bash
npx skills add angular/skills   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
