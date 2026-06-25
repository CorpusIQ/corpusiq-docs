---
title: Skill Repo Manager — Hermes Skill Repository Management Setup Guide
description: Install and configure Victor-F-M-A-R/skywork-skill-skill-repo-manager — manage the complete lifecycle of Hermes skill GitHub repositories with sync, audit, and update detection
---

# Skill Repo Manager — Setup Guide

**Source:** [Victor-F-M-A-R/skywork-skill-skill-repo-manager](https://github.com/Victor-F-M-A-R/skywork-skill-skill-repo-manager)
**Stars:** 0 ⭐ | **License:** None
**Created:** June 24, 2026
**Category:** DevOps / Skill Management / GitHub Automation

---

## 1. What It Is

A Hermes agent skill that manages the complete lifecycle of GitHub repositories for all Hermes skills — sync, audit, update detection, topic/description management, and new repo creation. Built for managing the 18-skill Skywork ecosystem, but portable to any Hermes skill collection.

### Included Scripts

| Script | Purpose |
|--------|---------|
| `sync_all_skills.py` | Sync all skill repos from local → GitHub (create, update, push) |
| `audit_hermes.py` | Audit skill compatibility with Hermes Agent; auto-fix option |
| `check_updates.sh` | Detect changed skills via SHA comparison |

---

## 2. Prerequisites

- GitHub token with `repo` scope
- Python 3.8+
- Git

---

## 3. Installation

```bash
git clone https://github.com/Victor-F-M-A-R/skywork-skill-skill-repo-manager.git
cd skywork-skill-skill-repo-manager
```

### Verify

```bash
ls scripts/
# Should show: sync_all_skills.py  audit_hermes.py  check_updates.sh
```

---

## 4. Usage

### Check Which Skills Are Outdated

```bash
bash scripts/check_updates.sh $GITHUB_TOKEN
```

### Sync All Skills to GitHub

```bash
python3 scripts/sync_all_skills.py --token $GITHUB_TOKEN
```

### Sync a Specific Skill

```bash
python3 scripts/sync_all_skills.py --token $GITHUB_TOKEN --skill web-design-engineer
```

### Audit Hermes Compatibility

```bash
# Read-only audit
python3 scripts/audit_hermes.py --all

# Audit and auto-fix
python3 scripts/audit_hermes.py --all --fix
```

---

## 5. Skill Lifecycle

```
Local Skill Dev → check_updates.sh (detect changes)
    ↓
sync_all_skills.py → GitHub (push/update repo)
    ↓
audit_hermes.py → Verify Hermes compatibility
    ↓
skywork-skills-hub → Git submodule updated
```

---

## 6. Companion: Skywork Skills Hub

This skill is paired with the [Skywork Skills Hub](https://github.com/Victor-F-M-A-R/skywork-skills-hub) — a monorepo that bundles 18 Hermes skills as Git submodules:

| # | Skill | Category |
|---|-------|----------|
| 1 | `animations` | Frontend |
| 2 | `architecture-designer` | Backend/Arch |
| 3 | `artifacts-builder` | Frontend |
| 4 | `content_marketing` | Marketing |
| 5 | `create-prd` | Product |
| 6 | `ds` | Data Science |
| 7 | `extract-design` | Design |
| 8 | `frontend-design` | Frontend |
| 9 | `marketing-psychology` | Marketing |
| 10 | `short-drama-writer` | Writing |
| 11 | `stock-market-industry-analyst` | Finance |
| 12 | `template-based-apa-professional-paper` | Documents |
| 13 | `template-based-business-analysis-report` | Documents |
| 14 | `template-based-competitive-analysis` | Documents |
| 15 | `template-based-general-service-agreement` | Documents |
| 16 | `web-design-engineer` | Frontend |
| 17 | `youtube-watcher` | Utilities |
| 18 | `skill-repo-manager` | Management |

All available as individual repos under `Victor-F-M-A-R/skywork-skill-*`.

---

## 7. CorpusIQ Use Cases

| Use Case | Application |
|----------|-------------|
| **CorpusIQ skill fleet management** | Sync, audit, and version-control all CorpusIQ agent skills |
| **Multi-agent skill consistency** | Ensure all agent profiles use the same skill versions |
| **Skill compatibility checks** | Audit custom skills against Hermes API changes |
| **CI/CD for skills** | Integrate `check_updates.sh` into deployment pipeline |

---

## 8. Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `sync_all_skills.py` fails | Missing GitHub token | Export `GITHUB_TOKEN` or pass `--token` |
| Audit reports false failures | Hermes API version mismatch | Update `references/hermes-compatibility.md` |
| `check_updates.sh` silent | No changes detected | Normal — only reports when SHAs differ |
| Submodule not updating | Hub not synced after skill push | Run `sync_all_skills.py` then update hub submodules |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [June 24 Evening Discovery](/hermes/skills/marketplace/new-june24-2026-evening/) →*
