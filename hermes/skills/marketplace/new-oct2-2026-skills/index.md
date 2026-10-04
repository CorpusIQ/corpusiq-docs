---
title: "New Skills - October 2, 2026"
description: "Skills.sh sweep for October 2, 2026: 732 unique skills collected, 20 NEW, 3 new publisher guides (01coder Agent Skills, Steipete Agent Scripts, Callicrate Skills)."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct2-2026-skills/"
robots: "index,follow"
last_updated: "2026-10-02"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace"]
---

# New Skills - October 2, 2026

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected | 732 (15 queries, 0 failed) |
| NEW (not in catalog) | 20 |
| NEW >= 100 installs | 7 |
| PARTIAL (source known, skill not cataloged) | 223 |
| New publisher guides | 3 |
| Roster reconciles | 0 |

## New Publisher Guides

### 1. 01coder Agent Skills - Content, Publishing & Security Toolkit

**Source:** [sugarforever/01coder-agent-skills](https://github.com/sugarforever/01coder-agent-skills) (136⭐, MIT) · **~21,505 installs** across 27 indexed listings · 23 SKILL.md files in-repo

VerySmallWoods' creator-focused marketplace: Chinese content creation, multi-platform publishing (X Articles, Substack, Zsxq), subtitle correction, video planning, and a security-scanning cluster. Install base is concentrated in `china-stock-analysis` (12.6K of the 21.5K total).

→ [Setup guide](/hermes/skills/catalog/01coder-agent-skills-setup)

### 2. Steipete Agent Scripts - Portable Agent Skills & Helpers

**Source:** [steipete/agent-scripts](https://github.com/steipete/agent-scripts) (7,198⭐, MIT) · **~9,472 installs** across 61 indexed listings · 54 SKILL.md files in-repo

Peter Steinberger's canonical shared agent repo. Ships the sync/validation infrastructure (`scripts/sync-skills`, `scripts/validate-skills`) plus macOS/Swift tooling, media conversion, and GitHub workflow skills.

→ [Setup guide](/hermes/skills/catalog/steipete-agent-scripts-setup)

### 3. Callicrate Skills - AGENTS.md & Documentation Authoring

**Source:** [callicrate/skills](https://github.com/callicrate/skills) (1⭐, no LICENSE file) · **~2,921 installs** across 2 indexed listings · 2 SKILL.md files in-repo

Two tightly-scoped developer skills with bundled analyzer/validator scripts: `agents-md` (repository instruction files) and `make-documentation` (READMEs, architecture docs, changelogs, runbooks).

→ [Setup guide](/hermes/skills/catalog/callicrate-skills-setup)

## NEW Candidates Below the Guide Floor (<100 installs)

| Source | Skill | Installs |
|---|---|---|
| fanthus/agent-skills | openclaw-expert | 137 → cluster combined 241 |
| jontsai/openclaw-command-center | command-center | 118 (single-listing repo) |
| oakencore/skillvet | skillvet | 113 → cluster combined 143 |
| purpleliu/siyuan-mcp | siyuan-skill | 104 → cluster combined 108 |

Publisher follow-ups confirmed all four clusters sit below the 100-install combined floor (fanthus 241, oakencore 143, jontsai 118, purpleliu 108) - none qualify for a guide. `oakencore/skillvet` is a security-testing harness (trigger/false-positive fixtures); `fanthus/agent-skills` and `jontsai/openclaw-command-center` are OpenClaw-adjacent.

## Notes

- All three guide candidates verified via GitHub trees API + repo meta API on their default branch (`main`) - none were previously documented.
- No roster reconciles this run; the PARTIAL >=100 backlog (223 rows) remains deferred.
- Sweep tooling note: `rg -o` with many `-e` alternatives reports the leftmost match, so a short pattern (`hermes`) masks longer ones (`hermes-agent`). The sweep script now re-probes any collected name that is a substring of another - see the catalog maintenance skill.
