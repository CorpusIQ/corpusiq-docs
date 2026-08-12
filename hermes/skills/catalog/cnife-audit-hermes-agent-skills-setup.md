---
title: Audit Hermes Agent Skills — Skill Usage Audit & Cleanup Setup Guide
description: Install and use audit-hermes-agent-skills from cnife/skills — audits installed Hermes skills by usage frequency via the Hermes internal API and generates an XLSX cleanup report. 13 installs.
---

# Audit Hermes Agent Skills — Setup Guide

**Source:** [cnife/skills](https://skills.sh/cnife/skills/audit-hermes-agent-skills)
**GitHub:** [github.com/cnife/skills](https://github.com/cnife/skills) (repo: 25 skills, 354 installs)
**Category:** Skill Management / Hygiene
**First Seen:** April 22, 2026
**Security:** Gen Agent Trust Hub Pass · Socket Pass · Snyk Pass

A skill-usage auditor for Hermes Agent. It measures how often each installed skill is actually used, identifies long-dormant skills, and produces a cleanup decision report. The skill queries Hermes' internal API (`_find_all_skills`, `_read_manifest`, `HubLockFile`) for authoritative skill source classification (hub/builtin/local/external) and combines it with filesystem scanning to locate real directory paths.

Note: the skill's UI and report are in Chinese (技能审计报告).

---

## Installation

```bash
npx skills add https://github.com/cnife/skills --skill audit-hermes-agent-skills
```

The skill requires `uv` for dependency management — all commands run through `uv run`.

---

## Usage

### Step 1 — Generate the audit report

```bash
uv run ~/.hermes/skills/audit-hermes-agent-skills/scripts/audit.py
```

Prints a console overview and writes `技能审计报告.xlsx` (skill audit report) to the current directory.

### Step 2 — Review in Excel

The XLSX lists every installed skill with source classification and usage data. Mark keep/remove decisions per row.

### Step 3 — Clean up

Remove skills marked for deletion, guided by the source classification:

| Source | Meaning | Cleanup Path |
|---|---|---|
| hub | Installed from a registry | `npx skills remove <repo>` |
| builtin | Shipped with Hermes | Do not remove — exclude from reports |
| local | User-created | `rm -rf` the skill directory |
| external | Manual/other installs | Remove via the original install path |

---

## Prerequisites

| Requirement | Details |
|---|---|
| Hermes Agent | Installed and accessible from the shell |
| uv | Python package manager (`curl -LsSf https://astral.sh/uv/install.sh | sh`) |
| Excel-compatible viewer | For the XLSX report |

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Quarterly skill audits** | Automate the skill-pruning cycles CorpusIQ runs manually today |
| **Usage evidence** | Decide skill deletions on real usage frequency instead of memory |
| **Source hygiene** | Identify external/hub skills that drifted from their install source |
| **Bloat detection** | Catch skill sprawl before context and startup costs degrade |

---

## Limitations / Verification

- Report UI is in Chinese — decisions are still readable as skill names, sources, and counts
- Requires Hermes' internal APIs to be accessible; if Hermes relocates them, the script may need updates
- Verify: `uv run ~/.hermes/skills/audit-hermes-agent-skills/scripts/audit.py` exits 0 and produces 技能审计报告.xlsx

---

## Related

- [Discovery Page — Aug 12 OpenClaw Ecosystem Sweep](/hermes/skills/marketplace/new-aug12-2026-openclaw-ecosystem/)
- [Skills Catalog](/hermes/skills/catalog/)

*Powered by CorpusIQ*
