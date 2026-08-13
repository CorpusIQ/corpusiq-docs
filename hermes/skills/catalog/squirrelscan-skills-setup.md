---
title: SquirrelScan Skills — Website Audit Tool Setup Guide for Hermes Agents
description: "squirrelscan/skills — 2 skills, 71.4K combined installs. Agent-driven website audits (SEO, performance, accessibility) via the SquirrelScan audit tool."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/squirrelscan-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-13"
tags: ["hermes skill", "agent skill", "skill setup", "seo"]
---

# SquirrelScan Skills — Setup Guide

**Source:** [skills.sh](https://www.skills.sh/squirrelscan/skills) (71.4K combined installs)
**GitHub:** [squirrelscan/skills](https://github.com/squirrelscan/skills)
**Category:** Website Auditing / SEO
**First Seen:** August 13, 2026 sweep
**Quality Tier:** 🔵 Community

Agent skills for the SquirrelScan website audit tool. The flagship `audit-website` (68.4K installs) walks an agent through a structured site audit — performance, SEO, accessibility, and content — using SquirrelScan's crawler output. Small cluster, high signal: website audits are one of the most common operator asks for agents.

---

## Installation

```bash
npx skills add squirrelscan/skills
```

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| audit-website | 68.4K | Structured website audit workflow |
| squirrelscan | 3.0K | Core SquirrelScan tool usage |

## Prerequisites

- A website to audit (any public URL works)
- Optional SquirrelScan account for full crawler reports

## CorpusIQ Use Cases

- **Docs site health** — periodic `audit-website` runs on docs.corpusiq.io complement the existing SEO/AEO/GEO pass
- **Competitor site teardowns** — quick structured audits of competitor landing pages for the competitive-intelligence brief
- **Client-facing value** — audit workflow reusable as a CorpusIQ onboarding artifact for business operators

## Limitations / Verification

- Community-maintained (86⭐); tool features may shift faster than the skill documents
- Verify by running the audit workflow against a small site and confirming the report sections populate

## Related

- [OSINT Skills — Open-Source Intelligence Investigation Setup](/hermes/skills/catalog/osint-skills-setup/)
- [CorpusIQ SEO Audit Skill](https://www.corpusiq.io/docs/hermes/skills/catalog/featured-seo-audit/)
