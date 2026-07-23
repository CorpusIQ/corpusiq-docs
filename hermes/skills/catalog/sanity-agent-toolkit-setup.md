---
title: Sanity Agent Toolkit — Headless CMS Operations for Hermes Agents
description: Sanity CMS best practices, migration, SEO/AEO, content modeling, experimentation, and Portable Text from Sanity.io. 34K+ combined installs across 6 skills.
---

# Sanity Agent Toolkit — Setup Guide

**Source:** [sanity-io/agent-toolkit](https://skills.sh/sanity-io/agent-toolkit) (34K+ combined installs)
**Category:** Development / Content Infrastructure
**Quality Tier:** 🟡 Beta

Sanity.io's official agent toolkit — structured content operations for the leading headless CMS. Covers content modeling, migrations, SEO/AEO best practices, content experimentation, and Portable Text serialization. Essential for Hermes agents managing content-driven applications.

---

## Installation

```bash
npx skills add sanity-io/agent-toolkit --skill sanity-best-practices
npx skills add sanity-io/agent-toolkit --skill sanity-migration
npx skills add sanity-io/agent-toolkit --skill seo-aeo-best-practices
npx skills add sanity-io/agent-toolkit --skill content-modeling-best-practices
npx skills add sanity-io/agent-toolkit --skill content-experimentation-best-practices
npx skills add sanity-io/agent-toolkit --skill portable-text-serialization
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **sanity-best-practices** | 14.4K | Core Sanity patterns — schema design, GROQ queries, studio customization |
| **sanity-migration** | 8.1K | Content migration scripts — import/export, schema evolution, data transforms |
| **seo-aeo-best-practices** | 4.6K | SEO and Answer Engine Optimization for structured content |
| **content-modeling-best-practices** | 3.1K | Content type design — reusable blocks, references, localization |
| **content-experimentation-best-practices** | 2.4K | A/B testing content structures, personalization, dynamic pages |
| **portable-text-serialization** | 1.4K | Portable Text spec — rich text serialization, custom annotations, embeds |

---

## Quick Start

```bash
npx skills use sanity-io/agent-toolkit@sanity-best-practices
npx skills use sanity-io/agent-toolkit@content-modeling-best-practices
```

---

## Verification

```bash
npx skills list | grep sanity
```

---

## Notes

- Official Sanity.io skills — actively maintained
- `seo-aeo-best-practices` covers AEO (Answer Engine Optimization) for AI search visibility
- `content-modeling` skill is critical for scalable content architectures
- Quality tier 🟡 Beta: 34K+ combined installs
