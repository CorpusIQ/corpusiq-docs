---
title: "LJG Skills Setup Guide for Hermes Agents"
description: "lijigang/ljg-skills - 124.5K installs across 30 skills, 7.2K stars: veteran Chinese tech blogger Li Jigang's personal knowledge-work suite - content cards, paper reading, writing, learning, and thinking workflows."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ljg-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-31"
tags: ["hermes skill", "agent skill", "skill setup", "productivity", "knowledge management", "writing", "reading"]
---

# LJG Skills - Setup Guide

**Source:** [lijigang/ljg-skills](https://skills.sh/lijigang/ljg-skills) (124.5K installs across 30 skills)
**GitHub:** [lijigang/ljg-skills](https://github.com/lijigang/ljg-skills) (7.2K stars)
**Skills:** 30 skills; top skills: `ljg-card` (6.7K), `ljg-paper` (6.6K), `ljg-roundtable` (6.5K)
**Category:** Productivity / Personal Knowledge Management
**First Seen:** skills.sh Mar 9, 2026; catalogued in the Aug 31, 2026 sweep
**Quality Tier:** 🟡 Trusted - publisher authority (Li Jigang, veteran Chinese tech blogger) with Gen Agent Trust Hub and Socket Pass, but Snyk carries a warning on the top skill (see Security Audit Status)

Li Jigang - a long-time Chinese tech blogger and community moderator - publishes a 30-skill personal knowledge-work suite. The skills encode his own working methods: `ljg-card` turns content into PNG share cards (long-form narrative, full-text layout, comic panels, and whiteboard argument modes via `-l`, `-f`, `-c`, `-w` flags), `ljg-paper` and `ljg-paper-flow` structure academic paper reading, `ljg-writes` and `ljg-word-flow` cover writing workflows, `ljg-learn` handles deliberate learning, `ljg-think` structures thinking, and `ljg-invest` supports investment research.

The suite is distinctive for its tightly parameterized interfaces: `ljg-card` declares its four modes as a parameter table with dimensions, image roles, and required read order - an unusually precise skill design. The skills are consistent bestsellers on skills.sh (top skills all 6-7K installs).

---

## Installation

```bash
npx skills add lijigang/ljg-skills
```

Or per-skill:

```bash
npx skills add https://github.com/lijigang/ljg-skills --skill ljg-card
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js** | Recent LTS for the `npx skills` installer |
| **Language handling** | SKILL.md content is Chinese; agents must process the original-language instruction text (see Limitations) |

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| ljg-card | 6.7K | Content-to-PNG share cards: `-l` long narrative, `-f` full text, `-c` comic panels, `-w` whiteboard argument |
| ljg-paper | 6.6K | Academic paper reading and note-taking |
| ljg-roundtable | 6.5K | Multi-perspective discussion and debate structure |
| ljg-writes | 6.3K | Writing workflows |
| ljg-plain | 6.2K | Plain-text and minimal-format discipline |
| ljg-learn | 6.2K | Deliberate learning workflows |
| ljg-invest | 6.1K | Investment research structure |
| ljg-rank | 6.1K | Ranking and prioritization methods |
| ljg-travel | 6.1K | Travel planning workflows |
| ljg-word | 6.0K | Vocabulary and word-level craft |

Plus `ljg-relationship`, `ljg-think`, `ljg-read`, `ljg-paper-flow`, `ljg-skill-map`, `ljg-paper-river`, `ljg-word-flow`, `ljg-present`, `ljg-qa`, `ljg-push`, `ljg-book`, `ljg-library`, `ljg-map`, `ljg-constraint`, `ljg-blind`, `ljg-x-download`, `ljg-structure`, `ljg-is`, `ljg-classic`, `ljg-teach`.

## Security Audit Status (skills.sh, verified Aug 31, 2026)

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ljg-card | Pass | Pass | Warn |

Gen Agent Trust Hub and Socket Pass; Snyk carries a warning - the reason this suite ships 🟡 Trusted rather than 🟢 Production.

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Share-card generation** | `ljg-card`'s parameterized card modes are a reference pattern for visual content produced from text |
| **Research synthesis** | `ljg-paper` + `ljg-paper-flow` structure reading pipelines for research sweeps |
| **Skill design reference** | The `ljg-card` parameter table (modes, dimensions, image roles, read order) is a model for writing precise, parameterized skills |
| **Writing workflows** | `ljg-writes` and `ljg-word-flow` complement CorpusIQ content production |

## Limitations / Verification

- **Source language is Chinese.** The SKILL.md files ship in the original Chinese and are not translated; agents must handle the original-language instruction text, and downstream English output requires translation discipline. Named per the non-English-suite precedent (wecomteam, genshijin).
- The suite is one author's personal method collection; it is opinionated by design.
- Snyk warning is named in the tier above.

Verification after install:

```bash
npx skills add lijigang/ljg-skills --list    # 30 skills discovered
```

## Related

- [Skills Catalog](/hermes/skills/catalog) - full quality-tiered directory
- [Skills Marketplace](/hermes/skills/marketplace) - more discovery batches

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
