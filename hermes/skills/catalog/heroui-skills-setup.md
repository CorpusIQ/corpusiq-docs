---
title: "HeroUI Skills - React & React Native UI Component Setup"
description: "Official HeroUI agent skills: v3 React (Tailwind v4 + React Aria) and Native component libraries plus a v2-to-v3 migration guide. 25.7K installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/heroui-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-01"
tags: ["hermes skill", "agent skill", "skill setup", "react", "ui", "heroui", "tailwind"]
---

# HeroUI Skills - Setup Guide

**Source:** [heroui-inc/heroui](https://github.com/heroui-inc/heroui) (30,850⭐, previously NextUI)
**Skill family:** `heroui-inc/heroui` (3 indexed skills)
**Combined Installs:** ~25,747 across indexed listings (Oct 1, 2026 snapshot)
**Category:** Frontend / UI
**Quality Tier:** 🟢 Verified (Apache-2.0 LICENSE in-repo, official `heroui` org, same-day commits)

HeroUI (formerly NextUI) is a React UI component library. The project ships three agent skills that let a coding agent build interfaces with version-matched component APIs instead of guessing at props from memory. The v3 line is built on Tailwind CSS v4 + React Aria, with a parallel React Native track (Tailwind via Uniwind).

---

## Installation

```bash
npx skills add heroui-inc/heroui
```

## Roster - Indexed Skills

| Skill | Installs | What It Does |
|---|---|---|
| heroui-react | 11,508 | HeroUI v3 React components (Tailwind v4 + React Aria) - Buttons, Modals, Forms, Cards |
| heroui-native | 10,339 | HeroUI Native (React Native, Tailwind v4 via Uniwind) - mobile UI components |
| heroui-migration | 3,900 | v2 → v3 migration guide: upgrading components and accessing migration docs (preview) |

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| Internal dashboard builds | Use heroui-react to scaffold operator-facing admin UI with current v3 APIs |
| Docs/demo scaffolds | Pair heroui-react with Vercel/Next.js skills for a full-stack UI prototype |
| Mobile ops app | heroui-native for a React Native companion view |
| Legacy upgrade | heroui-migration to move a v2 codebase to v3 safely |

## Limitations / Verification

- skills.sh indexing verified Oct 1, 2026: 3 skills indexed; all 3 SKILL.md files verified via raw.githubusercontent on branch `v3`.
- No live install test performed; install counts and the 30,850-star count are from the Oct 1, 2026 sweep snapshot.
- `heroui-migration` carries `status: preview` in its SKILL.md metadata - treat migration output as advisory.
- Default branch is `v3` (not `main`), which is unusual; `npx skills add` handles this automatically.

## Security

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Vercel Agent Skills](/docs/hermes/skills/catalog/vercel-agent-skills-setup)
- [Skills Marketplace](/docs/hermes/skills/marketplace)

---

*← [Skills Catalog](/docs/hermes/skills/catalog) | [Marketplace](/docs/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
