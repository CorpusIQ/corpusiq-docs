---
title: Hermes Engineering Curation Setup Guide
description: Install and use Fahrnetic's professionally-curated Hermes Agent engineering workflow — 104 selected skills, 10 operator profiles, gate matrix, and engineering spine
---

# Hermes Engineering Curation

**Source:** [Fahrnetic/hermes-engineering-skill-curation](https://github.com/Fahrnetic/hermes-engineering-skill-curation)
**Stars:** 1 ⭐ | **License:** MIT
**Created:** June 23, 2026

## Overview

A professionally-curated operating system for AI-assisted engineering. Distills a 336-skill ecosystem scan into 104 selected skills, 10 operator profiles, SVG gate matrices, and a full engineering spine (Route → Specify → Test → Build → Audit → Ship → Learn).

The core thesis: **AI coding without workflow is autocomplete with a costume budget.** This catalog shows the stronger pattern — agents operating inside explicit gates, evidence loops, and role-separated review.

## Prerequisites

- Hermes Agent (any version)
- ~50MB disk space (profiles + bundles + reports)
- Git

## Installation

### Full Install (recommended)

```bash
git clone https://github.com/Fahrnetic/hermes-engineering-skill-curation.git
cd hermes-engineering-skill-curation

# Install operator profiles
cp -r profiles ~/.hermes/profiles/

# Install skill bundles
cp -r bundles ~/.hermes/bundles/

# Review the curation report
cat CURATION.md
```

### Profile-Only Install

```bash
git clone https://github.com/Fahrnetic/hermes-engineering-skill-curation.git
cp -r hermes-engineering-skill-curation/profiles ~/.hermes/profiles/
```

## Capabilities

### 10 Operator Profiles

Each profile is a role-specific skill loadout:

| Profile | Role | Key Skills |
|---------|------|------------|
| `architect` | System design | Architecture diagrams, domain modeling, contract design |
| `developer` | Implementation | Code editing, testing, debugging, git workflow |
| `tester` | Quality assurance | Test generation, coverage analysis, edge-case discovery |
| `reviewer` | Code review | PR review, security audit, dependency analysis |
| `devops` | Infrastructure | CI/CD, deployment, monitoring, cron management |
| `security` | Security audit | Vulnerability scanning, secret detection, dependency audit |
| `release` | Release management | Versioning, changelog, publishing, artifact hygiene |
| `docs` | Documentation | API docs, README generation, wiki maintenance |
| `pm` | Project management | Issue triage, milestone tracking, sprint planning |
| `data` | Data engineering | Pipeline design, schema migration, ETL workflows |

### Engineering Spine

```
Route → Specify → Test → Build → Audit → Ship → Learn
```

Each phase has:
- **Explicit gates** — conditions that must be met before advancing
- **Evidence loops** — verifiable proof of completion
- **Role-separated review** — different agents/profiles for different phases

### Gate Matrix

```
                | Route | Specify | Test | Build | Audit | Ship | Learn
----------------|-------|---------|------|-------|-------|------|-------
Contract Check  |   ✓   |    ✓    |      |       |       |      |
Test Coverage   |       |    ✓    |  ✓   |   ✓   |       |      |
Security Scan   |       |         |      |   ✓   |   ✓   |  ✓   |
Build Pass      |       |         |      |   ✓   |       |  ✓   |
Diff Review     |       |         |      |       |   ✓   |  ✓   |
Artifact Clean  |       |         |      |       |       |  ✓   |
Retrospective   |       |         |      |       |       |      |  ✓
```

## CLI Reference

```bash
# Load a profile
hermes --profile fahrnetic-architect

# Load a bundle
hermes --bundle fahrnetic-full-stack

# Review curation decisions
cat ~/.hermes/profiles/fahrnetic-*/CURATION.md
```

## CorpusIQ Use Cases

| Use Case | Profile/Bundle | Why |
|----------|---------------|-----|
| **PR Review Pipeline** | `reviewer` + `security` | Role-separated review with security audit gates |
| **Feature Development** | `architect` → `developer` → `tester` | Full spine: specify → build → verify |
| **Release Shipping** | `release` + `devops` | Artifact hygiene, changelog, deployment |
| **Agent Onboarding** | Full profiles set | Pre-built operator loadouts for new team members |

## Troubleshooting

### Profile not found

```bash
# Verify installation path
ls ~/.hermes/profiles/
# Should show fahrnetic-* directories

# Re-clone if missing
git clone https://github.com/Fahrnetic/hermes-engineering-skill-curation.git /tmp/fahrnetic
cp -r /tmp/fahrnetic/profiles/* ~/.hermes/profiles/
```

### Bundle conflicts with existing skills

The bundles reference skill names that may conflict with pre-existing installations. Review `bundles/*.yaml` before loading and comment out duplicates.

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace Home](/hermes/skills/marketplace/) →*
