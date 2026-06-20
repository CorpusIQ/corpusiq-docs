---
title: Hermes Ponytail Setup Guide
description: Install and configure the Ponytail lazy-senior-dev skill pack for Hermes Agent — YAGNI-first development, over-engineering audits, and tech debt tracking
---

# Hermes Ponytail — Setup Guide

**Ponytail** makes your Hermes agent think like the laziest senior developer. YAGNI-first. Stdlib-first. No unrequested abstractions. The shortest diff that works.

Packaged as 7 pure `SKILL.md` skills for Hermes Agent by [tensakulabs/hermes-ponytail](https://github.com/tensakulabs/hermes-ponytail).

---

## 1. Prerequisites

- **Hermes Agent** installed and running
- Hermes skills CLI (`hermes skills install`)

No Python dependencies, no tools, no API keys — these are pure skill files.

---

## 2. Installation

Install all 7 skills at once:

```bash
hermes skills install tensakulabs/hermes-ponytail/ponytail --yes
hermes skills install tensakulabs/hermes-ponytail/ponytail-review --yes
hermes skills install tensakulabs/hermes-ponytail/ponytail-audit --yes
hermes skills install tensakulabs/hermes-ponytail/ponytail-debt --yes
hermes skills install tensakulabs/hermes-ponytail/ponytail-gain --yes
hermes skills install tensakulabs/hermes-ponytail/ponytail-help --yes
```

Or install individual skills as needed.

Skills land in `~/.hermes/skills/` and are auto-discovered on the next restart.

---

## 3. Skill Reference

### `ponytail` — Lazy Senior Dev Mode

Core mindset skill. Activates YAGNI-first thinking:
- No unrequested abstractions (no factories, no patterns without a problem)
- Stdlib before dependencies
- Shortest diff that works
- Delete code before adding code
- Question every dependency, every abstraction layer

**Load via:** `skill_view(name='ponytail')`

### `ponytail-review` — Diff Review

Review any diff for over-engineering. Output: one line per thing to delete, one line per thing to simplify.

**Usage:** Load before reviewing PRs or when asked to review code.

### `ponytail-audit` — Whole-Repo Audit

Systematic audit of the entire repo for over-engineering. Produces a ranked list of what to cut — most impactful simplifications first.

**Usage:** Load when doing architectural health checks or before major refactors.

### `ponytail-debt` — Tech Debt Ledger

Harvests every `ponytail:` shortcut comment in the codebase into one tracked debt ledger. Comments like `# ponytail: this abstraction is premature` become tracked items.

**Usage:** Run periodically to maintain visibility of intentional shortcuts and planned simplifications.

### `ponytail-gain` — Impact Scoreboard

Measures Ponytail's impact: less code, lower costs, faster builds. Trackable metrics over time.

**Usage:** Load for monthly retrospectives or to demonstrate simplification ROI.

### `ponytail-help` — Quick Reference

One-page reference of all Ponytail modes and skills with one-liner descriptions.

---

## 4. CorpusIQ Use Cases

- **Agent skill development** — Use `ponytail-review` when reviewing new skill SKILL.md files before publishing
- **Infrastructure code** — `ponytail-audit` on the Mac Mini and DGX Spark automation scripts
- **Growth ops** — Keep automation scripts minimal; `ponytail` mindset prevents over-engineered workflows
- **Docs management** — Audit the corpusiq-docs repo structure for unnecessary complexity

---

## 5. Limitations

- **On-demand only** — Hermes skills load when triggered, unlike Claude Code/Codex hooks that run every turn. If you want Ponytail governing *every* Hermes turn, append the ruleset from `ponytail/SKILL.md` into Hermes' base system prompt or build it as a Hermes plugin (`pre_llm_call` hook).
- **No code execution** — These are pure behavioral skills. They change how the agent *thinks*, not what tools it has.
- **Not for urgent hotfixes** — Ponytail's simplification-first mindset can slow down emergency patches where speed trumps elegance. Disable or unload for critical incidents.

---

## 6. Verification

After installation, verify the skills are available:

```bash
hermes skills list | grep ponytail
```

Expected output: all 6 ponytail skills listed (ponytail, ponytail-review, ponytail-audit, ponytail-debt, ponytail-gain, ponytail-help).

---

## 7. Uninstall

```bash
hermes skills uninstall ponytail
hermes skills uninstall ponytail-review
hermes skills uninstall ponytail-audit
hermes skills uninstall ponytail-debt
hermes skills uninstall ponytail-gain
hermes skills uninstall ponytail-help
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Hermes Ponytail Repo](https://github.com/tensakulabs/hermes-ponytail) →*
