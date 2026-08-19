---
title: "Genshijin Skills — Japanese Concise-Reply Framework Setup"
description: "interfacex-co-jp/genshijin — 7 skills, 19.2K installs: a Japanese concise-reply framework for agents with commit, review, compress, stats, help, and crew workflow commands."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/genshijin-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-18"
tags: ["hermes skill", "agent skill", "skill setup", "japanese", "concise replies", "git workflow", "genshijin"]
---

# Genshijin Skills — Setup Guide

**Source:** [interfacex-co-jp/genshijin](https://skills.sh/interfacex-co-jp/genshijin)
**GitHub:** [interfacex-co-jp/genshijin](https://github.com/interfacex-co-jp/genshijin)
**Skills:** 7 skills · 19.2K total installs
**Category:** Agent Communication
**First Seen:** April 7, 2026 (catalogued August 18, 2026 sweep)
**Quality Tier:** 🟢 Production — Gen Agent Trust Hub Pass, Socket Pass, and Snyk Pass on the genshijin flagship; 310 GitHub stars; #2 on the hot page at sweep time

Genshijin (原始人, "primitive man") is a Japanese concise-reply framework for coding agents. The core skill enforces brutal brevity — all technical content kept, all filler removed — with three persistent modes (通常 normal, 丁寧 polite, 極限 extreme) switched via a slash command, and it stays active across turns, resisting politeness regression and filler drift. Six companion skills extend it into a full workflow: genshijin-commit (concise conventional commits), genshijin-review (terse code review), genshijin-compress (context compression), genshijin-help, genshijin-stats, and genshijin-crew (multi-agent crew coordination). The cluster sits at #2 on the skills.sh hot page with genshijin-commit at +13 installs in one hour.

---

## Installation

```bash
npx skills add interfacex-co-jp/genshijin
```

Individual skills install with the explicit repo form:

```bash
npx skills add https://github.com/interfacex-co-jp/genshijin --skill genshijin
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **Japanese-capable agent** | The SKILL.md content ships in Japanese; the framework works for any language output but the instruction text is Japanese |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| genshijin | 3.0K | Core concise-reply framework with persistent mode switching (通常/丁寧/極限) |
| genshijin-commit | 2.7K | Concise conventional commit messages |
| genshijin-compress | 2.7K | Context compression for long sessions |
| genshijin-review | 2.7K | Terse code review feedback |
| genshijin-help | 2.7K | Usage help for the framework |
| genshijin-stats | 2.7K | Reply-length and mode statistics |
| genshijin-crew | 2.7K | Crew coordination across multiple agents |

## Quick Start

1. Install: `npx skills add interfacex-co-jp/genshijin`
2. The core skill activates automatically; switch modes with `/genshijin 丁寧|通常|極限`
3. Disable with 「原始人やめて」or 「通常モード」

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Token discipline** | genshijin and genshijin-compress align with our field-filtering and memory-compaction token strategy |
| **Consistent commit style** | genshijin-commit enforces concise conventional commits across agent-built repos |
| **Multi-agent coordination** | genshijin-crew maps to multi-agent orchestration workflows |
| **Reply hygiene** | Mode persistence prevents filler drift on long-running agent sessions |

## Limitations / Verification

- Security audits on the genshijin flagship: Gen Agent Trust Hub Pass, Socket Pass, Snyk Pass
- Publisher-page total verified (19.2K across 7 skills); 310 GitHub stars as of the sweep
- Below the 20K install guide bar — drafted on #2 hot-page position, +13 one-hour momentum on genshijin-commit, and Japanese corporate publisher (interfacex-co-jp)
- SKILL.md instruction text is Japanese — the skills.sh excerpt and install content carry over untranslated and agents must handle the original-language instructions (same handling as the wecomteam suites)

```bash
npx skills add interfacex-co-jp/genshijin   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
