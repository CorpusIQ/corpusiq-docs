---
title: NuShell Pro — Structured Shell Scripting Skill Setup Guide for Hermes Agents
description: Install hustcer/nushell-pro (1.1K installs) — NuShell scripting expertise for agents: structured data pipelines, custom commands, and typed shell automation.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/nushell-pro-setup/"
robots: "index,follow"
last_updated: "2026-08-13"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# NuShell Pro — Setup Guide

**Source:** [hustcer/nushell-pro](https://www.skills.sh/hustcer/nushell-pro) (2 skills · 1.1K combined installs)
**Repo:** [github.com/hustcer/nushell-pro](https://github.com/hustcer/nushell-pro)
**Category:** Infrastructure & DevOps / Shell
**First Seen:** August 13, 2026
**Quality Tier:** 🟡 Community (`nushell-pro` at 1.1K installs)

`nushell-pro` encodes NuShell expertise — structured data pipelines, custom command design, and typed shell automation — for agents that script system administration tasks. NuShell's data-centric model (everything is a table) maps well to agent pipelines that currently fight text-parsing in bash. `nushell-craft` is the newer, still-experimental companion.

---

## Installation

```bash
# Direct install
npx skills add hustcer/nushell-pro

# Hermes: install by identifier
hermes skills install hustcer/nushell-pro/nushell-pro
```

---

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| `nushell-pro` | 1.1K | NuShell scripting, pipelines, and custom commands |
| `nushell-craft` | 0 | Experimental companion (new) |

---

## Prerequisites

| Requirement | Details |
|---|---|
| NuShell installed | `nushell` binary on the agent host |
| Any agent runtime | Procedural knowledge — no API keys |

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Structured system tasks** | Replace fragile text-parsing shell scripts with typed pipelines |
| **Data extraction from CLI tools** | Table-native parsing of command output |
| **Hermes deployment scripting** | Cleaner setup scripts for customer installations |

---

## Limitations / Verification

- Community tier — one skill, modest install base
- `nushell-craft` at 0 installs is untested
- Verify install: `npx skills list | grep nushell`

---

## Related

- [Terminal Skills Setup](/hermes/skills/catalog/terminal-skills-setup/)
- [Infrastructure & DevOps category](/hermes/skills/catalog/)
- [Skills Catalog](/hermes/skills/catalog/)
