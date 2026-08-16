---
title: "OXC Project Skills — Linter & Formatter Migration Setup"
description: "oxc-project/oxc — 4 skills, 9.9K installs: ESLint-to-Oxlint and formatter migration playbooks from the OXC team."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/oxc-project-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-16"
tags: ["hermes skill", "agent skill", "skill setup", "linting", "tooling", "oxc"]
---

# OXC Project Skills — Setup Guide

**Source:** [oxc-project/oxc](https://skills.sh/oxc-project/oxc)
**GitHub:** [oxc-project/oxc](https://github.com/oxc-project/oxc)
**Skills:** 4 skills · 9.9K total installs
**Category:** Tooling Migration
**First Seen:** catalogued August 16, 2026 sweep (migrate-oxlint on skills.sh since March 5, 2026)
**Quality Tier:** 🟡 Trusted — official OXC org; top skill carries a Snyk Warn (see Limitations)

OXC's skills guide agents through the highest-leverage tooling migration in JavaScript: replacing ESLint with the Rust-based Oxlint. Rust-native linting cuts CI lint times by an order of magnitude, and these skills run the official `@oxlint/migrate` tool rather than hand-translating configs.

---

## Installation

```bash
npx skills add oxc-project/oxc
```

Individual skills install with the explicit repo form:

```bash
npx skills add https://github.com/oxc-project/oxc --skill migrate-oxlint
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **JavaScript/TypeScript project** | With an existing ESLint flat config |
| **Migration tool** | `npx @oxlint/migrate` — invoked by the skill |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| migrate-oxlint | 6.3K | ESLint → Oxlint migration: runs `@oxlint/migrate`, generates `.oxlintrc.json`, handles unsupported rules |
| migrate-oxfmt | 3.4K | Formatter migration to Oxfmt |
| performance-lint-rules | 158 | Performance-specific rule guidance |
| insta-snapshots | 142 | Snapshot testing with Insta |

## Quick Start

1. Install: `npx skills add oxc-project/oxc`
2. In the project root, ask: "migrate this project from ESLint to Oxlint"
3. The skill runs the automated migration and walks the unsupported-rule cleanup

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **CI speed** | Rust-native linting cuts minutes off our lint jobs — a direct cost and cycle-time win |
| **Migration template** | The automated-migrate-then-cleanup pattern is reusable for other tooling migrations |
| **Dependency reduction** | Replacing ESLint drops a deep plugin dependency tree |

## Limitations / Verification

- Security audits on migrate-oxlint: Gen Agent Trust Hub Pass, Socket Pass, **Snyk Warn** — trusted with the audit named
- Publisher-page install counts verified (6.3K + 3.4K); GitHub 22.3K stars on the repo
- Oxlint does not implement every ESLint plugin rule — migrations may leave a small ESLint shim for rare plugins
- performance-lint-rules and insta-snapshots are sub-200 installs — early content

```bash
npx skills add oxc-project/oxc   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
