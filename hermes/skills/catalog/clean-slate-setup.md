---
title: Clean Slate — Session-End Verification Skill Setup Guide
description: Install and configure clean-slate, the session-end verification skill that turns "looks done" into "is actually done." Works with Hermes, Claude Code, Codex, and OpenClaw.
---

# Clean Slate — Setup Guide

**Source:** [sidhartha1s/clean-slate](https://github.com/sidhartha1s/clean-slate)
**Category:** Agent Infrastructure / Quality Assurance
**License:** MIT · **Published:** June 28, 2026

Every coding agent eventually says "this should work" when it doesn't. Clean Slate is a session-end verification skill that audits every claim — merged PRs, passing tests, fixed bugs — against the real artifact (git history, CI status, test output). It reconciles unmerged work, flags half-finished changes, and produces a verifiable status report.

---

## The Problem It Solves

| Agent Claims | Clean Slate Verifies |
|-------------|---------------------|
| "PR merged" | Checks `git log` and remote for the actual merge commit |
| "Tests pass" | Runs the test suite and captures exit codes |
| "Bug fixed" | Searches for the fix commit, verifies it addresses the report |
| "Branch cleaned up" | Lists stale branches, flags unpushed work |
| "Documentation updated" | Diffs docs/ against last tag |

---

## Installation

```bash
npx skills add sidhartha1s/clean-slate
```

Direct clone:

```bash
git clone https://github.com/sidhartha1s/clean-slate.git
cp clean-slate/SKILL.md ~/.hermes/profiles/corpusiq/skills/clean-slate.md
```

---

## Usage with Hermes Agent

Invoke at the end of any coding session:

```
"Run clean-slate verification on this session"
```

Or trigger automatically by adding to your session-end workflow:

```yaml
# ~/.hermes/config.yaml
hooks:
  session_end:
    - skill: clean-slate
      args: --strict
```

### Output Example

```
Clean Slate Report — Session #8472
===================================
✅ PR #342 merged — commit a3f2b1c on main
✅ Tests pass — 142/142, 0 failures
⚠️  Branch fix/login-timeout not deleted
❌ Bug #591 claim "fixed" — no related commit found
⚠️  2 files modified but not committed:
    - src/auth/session.ts
    - docs/CHANGELOG.md

Verdict: SESSION NOT CLEAN — 1 unverified fix, 2 uncommitted files
```

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| Agent session hygiene | Run at end of every coding session to catch loose ends |
| CI/CD gate | Add as pre-merge check — block PRs from unclean sessions |
| Multi-agent coordination | Verify one agent's claims before another agent builds on them |
| Onboarding QA | New contributors run clean-slate to build verification habits |

---

*This guide is part of the [Hermes Skills Catalog](/hermes/skills/catalog/). Discovered June 29, 2026. Powered by CorpusIQ.*
