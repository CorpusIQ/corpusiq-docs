---
title: Hermes Imports — Convert Hermes Workflows to ECC Skills
description: Sanitize and convert local Hermes operator workflows into reusable ECC skills. Strip private state, credentials, and local paths. 2.4K+ installs.
---

# Hermes Imports — Setup Guide

**Source:** [affaan-m/everything-claude-code](https://skills.sh/affaan-m/everything-claude-code/hermes-imports) (2,400+ installs)
**Category:** Agent Infrastructure / Skill Development
**Quality Tier:** 🟢 Production

Convert repeated Hermes operator workflows into safe, reusable ECC (Everything Claude Code) skills. Strips private workspace state, credentials, and local-only paths so workflows can be shared publicly without leaking sensitive data.

---

## Installation

```bash
npx skills add affaan-m/everything-claude-code --skill hermes-imports
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | Running local workflows worth converting |
| **Git** | For committing and PRing the sanitized skill |

---

## Key Capabilities

### Import Rules

- Convert local paths to repo-relative paths or placeholders
- Replace live account names with role labels (`operator`, `default profile`, `workspace owner`)
- Describe credential requirements by provider name only
- Keep examples narrow and operational
- Never ship raw workspace exports, tokens, OAuth files, health data, CRM data, or finance data

### Sanitization Checklist

Before committing an imported workflow, scan for:

- Absolute paths (`/Users/...`, `/home/...`)
- `~/.hermes` paths unless explicitly explaining local setup
- API keys, tokens, cookies, OAuth files, or bearer strings
- Phone numbers, private email addresses, and personal contact graphs
- Client names, family names, or non-public account names
- Revenue, health, or CRM details
- Raw logs including tool output from private systems

---

## Quick Start

### Conversion Pattern

1. Identify the repeatable operator loop
2. Strip private inputs and outputs
3. Rewrite local paths as repo-relative examples
4. Turn one-off instructions into a `When To Use` section and a short process
5. Add concrete output requirements
6. Run a secret and local-path scan before opening a PR

### Example: Converting a Launch Handoff

**Local Hermes prompt (unsafe to share):**
```text
Read my local workspace files and finalize launch copy.
```

**ECC-safe version:**
```text
Use the public release pack under docs/releases/<version>/.
Return one X thread, one LinkedIn post, one recording checklist, and the missing assets list.
```

### Example: Converting a Quiet-Hours Job

**Local Hermes job (unsafe to share):**
```text
Run my private inbox, finance, and content checks overnight.
```

**ECC-safe version:**
```text
Describe the scheduler policy, the quiet-hours window, the escalation rules,
and the categories of checks. Do not include private data sources or credentials.
```

---

## Output Contract

Return after each import:

- Candidate ECC skill name
- Sanitized workflow summary
- Required public inputs
- Private inputs removed
- Remaining risks
- Files that should be created or updated

---

## Verification

```bash
# Test the skill loaded correctly
npx skills use affaan-m/everything-claude-code@hermes-imports

# Run through a sample workflow
# Create a test Hermes workflow with fake private data
# Verify the sanitization checklist catches everything
```

---

## Notes

- **Ideal for teams** that want to share Hermes workflows across members without exposing individual workspace state
- **Pairs well with** `claude-handoff` for session continuity across sanitized workflows
- The skill is part of the `everything-claude-code` mono-repo which contains 40+ Claude Code / Hermes skills
