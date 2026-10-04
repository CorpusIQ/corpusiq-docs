---
title: "Callicrate Skills - AGENTS.md & Documentation Authoring"
description: "Two focused skills for repository instruction files and project documentation: agents-md and make-documentation, with analyzer/validator scripts and tests. 2.9K installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/callicrate-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-02"
tags: ["hermes skill", "agent skill", "skill setup", "agents.md", "documentation", "developer tools"]
---

# Callicrate Skills - Setup Guide

**Source:** [callicrate/skills](https://github.com/callicrate/skills) (1⭐, no LICENSE file)
**Skill family:** `callicrate/skills` (2 SKILL.md files in-repo; 2 indexed listings)
**Combined Installs:** ~2,921 across indexed listings (Oct 2, 2026 snapshot)
**Category:** Developer Tooling / Documentation
**Quality Tier:** 🔵 Community (high installs on a brand-new low-star repo; no LICENSE file in-repo - verify provenance before production reliance)

Callicrate publishes two tightly-scoped developer skills. `agents-md` creates, updates, reviews, and validates repository `AGENTS.md` files; `make-documentation` writes READMEs, architecture notes, changelogs, runbooks, and install docs. Both ship analyzer/validator scripts and pytest fixtures, and both are explicit about when NOT to trigger - a sign of deliberate scope discipline rather than a grab-bag.

---

## Installation

```bash
npx skills add callicrate/skills
```

Individual skill directories can be worked on locally:

```bash
cd agents-md # or make-documentation
python -m pytest
```

## Roster - Indexed Skills

| Skill | Installs | What It Does |
|---|---|---|
| make-documentation | 1,482 | Write READMEs, architecture docs, changelogs, release notes, runbooks, install docs, notebook docs |
| agents-md | 1,439 | Create/update/review/split/validate scoped repository `AGENTS.md` files |

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| Repo onboarding docs | `agents-md` to generate evidence-backed, scoped `AGENTS.md` guidance for a repository |
| Docs quality pass | `make-documentation` for README/architecture/changelog coherence; run its `audit_documentation.py` first |
| Agent-instruction hygiene | Use the `agents-md` validator (`validate_agentsmd.py` + `semantic_check_agentsmd.py`) to check instruction files pre-commit |

## Limitations / Verification

- skills.sh indexing verified Oct 2, 2026: 2 indexed listings; 2 SKILL.md files verified via the GitHub trees API on branch `main`.
- **Repo has 1 star and no LICENSE file.** Install counts (1,482 / 1,439) are high relative to the repo's community traction - treat as unverified provenance. Check the repository's terms before commercial use.
- Skills invoke bundled Python scripts (`analyze_project.py`, `validate_agentsmd.py`, `audit_documentation.py`) - review these before running against internal repos.
- No live install test performed; install counts are from the Oct 2, 2026 sweep snapshot.
