---
title: design-review — Setup Guide
description: Designer Who Codes skill for Hermes Agent from the nexu-io/open-design repo (90K⭐). Visual UI audit with fixes, atomic commits, and before/after screenshots.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/design-review-setup/"
robots: "index,follow"
last_updated: "2026-08-21"
tags: ["hermes skill", "agent skill", "skill setup", "design review", "ui audit"]

---

# design-review — Setup Guide

**Source:** [nexu-io/open-design](https://github.com/nexu-io/open-design) (90,117 ⭐)
**Skill:** `design-review`
**Installs:** 2,369

A "Designer Who Codes" skill: runs a visual audit on shipped UI, then fixes issues with atomic commits and before/after screenshots. Useful for tightening interfaces before launch. Curated from Garry Tan's [gstack](https://github.com/garrytan/gstack) workflow, part of the open-design ecosystem (the open-source Claude Design alternative) that runs on Hermes Agent plus 26 other CLI agents via ACP.

## Installation

```bash
npx skills add https://github.com/nexu-io/open-design --skill design-review
```

After install, reload skills:
- Hermes CLI: `/reload-skills` or restart session
- Hermes gateway: `/restart` or `hermes gateway restart`

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Hermes Agent | v2.0+ (ACP-compatible) |
| Node.js | v18+ (for npx) |
| Git repo | Target UI must live in a git repository (atomic commits) |
| Screenshot tooling | Browser or local renderer for before/after captures |

## Capabilities

| Capability | Trigger | Output |
|-----------|---------|--------|
| Visual UI audit | "design review" / "visual audit" | Structured findings list |
| Pre-launch design check | "pre launch design check" | Prioritized fix list |
| Auto-fix with commits | "before after" | Atomic commits + screenshots |
| Tighten shipped UI | "design review" on existing app | Cleaned-up interface |

## CLI/Command Reference

The skill is invoked through Hermes Agent prompts, not a standalone CLI. Once installed, Hermes agents call it natively:

```
"Run a design review on the checkout flow and fix the issues found."
"Visual audit on our landing page before launch."
```

The skill follows the OpenDesign agent-native loop: discover the brief, lock the direction, stream the artifact, critique, deliver. Fixes land as atomic commits with before/after screenshots for verification.

## CorpusIQ Use Cases

| Use Case | How to Apply |
|----------|-------------|
| Docs UI polish | Run design-review on docs.corpusiq.io pages before public release |
| Landing page QA | Pre-launch design check on marketing pages |
| Connector dashboards | Visual audit on new connector UIs before announcement |
| Recurring quality gate | Schedule periodic design reviews of shipped pages |

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| Skill not found after install | Skills not reloaded | `/reload-skills` or restart session |
| Screenshots missing | No browser/renderer configured | Install a headless browser or use local renderer |
| Atomic commits fail | Target not a git repo | `git init` the target directory first |
| ACP connection errors | Agent not ACP-enabled | Verify Hermes Agent is running with ACP support |

## Verification

```bash
# Confirm the skill is installed
npx skills list | grep design-review

# Quick smoke test
"Run a design review on the current project's index page."
```

Expect a findings list with before/after screenshots and atomic commits when fixes are applied.
