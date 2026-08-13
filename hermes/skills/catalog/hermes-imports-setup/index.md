---
title: Hermes Imports — Setup Guide for Hermes Agents
description: Convert local Hermes workflows into sanitized ECC skills and release-pack artifacts. Strip private state, paths, and credentials for safe public reuse. 2.7K+ installs.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/hermes-imports-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Hermes Imports — Setup Guide

**Source:** [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) (Community)
**Skill:** `hermes-imports` · **Installs:** 2.7K+ · **Category:** Workflow / DevOps
**Platform:** Linux, macOS, Windows

Hermes Imports converts repeated Hermes operator workflows into safe, shareable ECC (Everything Claude Code) skills. It strips private workspace state — local paths, credentials, account names, personal data — and produces release-pack artifacts ready for public distribution.

## Installation

```bash
npx skills add affaan-m/everything-claude-code@hermes-imports
```

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Hermes Agent | Working local workflow to export |
| Git | For version control of exported skills |
| ECC environment | Target for the exported skill |

## When to Use

- A Hermes workflow has been repeated enough to become reusable
- A local operator prompt should become a public ECC skill
- A launch, content, research, or engineering workflow needs sanitized handoff docs
- A workflow mentions local paths, credentials, personal datasets, or private account names

## Import Rules

- Convert local paths → repo-relative paths or placeholders
- Replace live account names → role labels (`operator`, `default profile`, `workspace owner`)
- Describe credential requirements by provider name only
- Keep examples narrow and operational
- Never ship: raw workspace exports, tokens, OAuth files, health data, CRM data, finance data
- If the workflow requires private state to make sense, keep it local

## Sanitization Checklist

Before committing an imported workflow, scan for:

- [ ] Absolute paths (`/Users/...`, `/home/...`)
- [ ] `~/.hermes` paths (unless documenting local setup)
- [ ] API keys, tokens, cookies, OAuth files, bearer strings
- [ ] Phone numbers, private email addresses, personal contact graphs
- [ ] Client names, family names, non-public account names
- [ ] Revenue, health, or CRM details
- [ ] Raw logs with tool output from private systems

## Conversion Pattern

1. Identify the repeatable operator loop
2. Strip private inputs and outputs
3. Rewrite local paths as repo-relative examples
4. Turn one-off instructions into `When To Use` + process steps
5. Add concrete output requirements
6. Run a secret and local-path scan before committing

## Verification

After export:
- Grep for absolute paths: `grep -r "/Users\|/home/" ./exported-skill/`
- Grep for credentials: `grep -ri "token\|api.key\|secret\|password" ./exported-skill/`
- Verify the skill works in a clean ECC environment
- Open a PR with the sanitized skill

## Related Skills

- [Claude Handoff Setup](/hermes/skills/catalog/claude-handoff-setup/)
- [Awesome Hermes Agent Ecosystem](/hermes/skills/catalog/awesome-hermes-agent-ecosystem-setup/)
