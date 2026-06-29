---
title: Coding Posture — Task-Aware Working Modes Setup Guide
description: Install and configure coding-posture, a single SKILL.md that gives Hermes agents task-aware working modes (debug, fix, review, migrate). 9★, works across Claude Code, Codex, Cursor, and Pi.
---

# Coding Posture — Setup Guide

**Source:** [alexei-led/coding-posture](https://github.com/alexei-led/coding-posture) · 9★
**Category:** Agent Infrastructure / Development Workflows
**License:** MIT · **Language:** Shell · **Published:** June 24, 2026

A single `SKILL.md` that switches coding agents between task-aware working modes. Instead of the agent guessing whether you want a quick fix or a full migration, coding-posture gives it explicit posture instructions. One file, zero dependencies, 9 stars of community validation.

---

## What It Does

| Mode | What It Optimizes For | When To Use |
|------|----------------------|-------------|
| **debug** | Root cause analysis, log diving | Bug reports, error traces |
| **fix** | Minimal change, no side effects | Quick patches, hotfixes |
| **review** | Standards enforcement, anti-pattern detection | PR reviews, code audits |
| **migrate** | Safe refactoring, backward compatibility | Framework upgrades, API changes |
| **explain** | Clarity, diagrams, mental models | Onboarding, documentation |
| **test** | Coverage, edge cases, regression prevention | TDD, test suite gaps |

The agent reads the mode from the skill and adjusts its reasoning depth, tool selection, and output format accordingly.

---

## Installation

### Via skills.sh (Recommended)

```bash
npx skills add alexei-led/coding-posture
```

### Direct GitHub Clone

```bash
git clone https://github.com/alexei-led/coding-posture.git
cp coding-posture/SKILL.md ~/.hermes/profiles/corpusiq/skills/coding-posture.md
```

### Manual (Single File)

Download `SKILL.md` and place it in your Hermes skills directory:

```bash
curl -o ~/.hermes/profiles/corpusiq/skills/coding-posture.md \
  https://raw.githubusercontent.com/alexei-led/coding-posture/main/SKILL.md
```

---

## Usage with Hermes Agent

After installation, invoke by mentioning the mode:

```
"Review this PR in review posture"
"Debug the connection timeout in debug posture"
"Migrate this Express app to Fastify in migrate posture"
```

Or explicitly:

```
"Switch to fix posture and patch the null pointer"
```

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| Code review automation | Switch to `review` posture for PR analysis |
| On-call debugging | `debug` posture for error trace triage |
| Dependency upgrades | `migrate` posture for safe refactoring |
| Test coverage gaps | `test` posture for TDD workflows |

---

*This guide is part of the [Hermes Skills Catalog](/hermes/skills/catalog/). Discovered June 29, 2026. Powered by CorpusIQ.*
