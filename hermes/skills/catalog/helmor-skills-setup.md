---
title: "Helmor Skills - Multi-Agent Workbench Setup"
description: "Helmor skills for the open-source local multi-agent software development workbench; ~1,981 indexed installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/helmor-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-29"
tags: ["hermes skill", "agent skill", "skill setup", "multi-agent", "cli"]
---

# Helmor Skills - Setup Guide

**Source:** [dohooo/helmor](https://github.com/dohooo/helmor) (1,306⭐)
**Skill family:** `dohooo/helmor` (5 installable skills)
**Combined Installs:** ~1,981 across indexed listings (Sep 29, 2026 snapshot)
**Category:** Developer Tools
**Quality Tier:** 🟡 Unverified (no skills.sh Trust Hub / Socket / Snyk verdicts published - verified Sep 29, 2026)

Helmor is an open-source, local-first workbench (Apache 2.0) for orchestrating coding agents: parallel agents in isolated git workspaces, review, and one-click PR shipping, driven by a scriptable `helmor` CLI and MCP server. The skill family is dominated by `helmor-cli`, which teaches an agent to operate the CLI (1,968 of ~1,981 indexed installs); four smaller skills cover release, debug-operate, debug-loop, and vendor bumping.

---

## Installation

```bash
npx skills add dohooo/helmor
```

## Roster - Top Skills

| Skill | Installs | What It Does |
|---|---|---|
| helmor-cli | 1,968 | Operating the Helmor CLI |
| helmor-release | 4 | Release workflows |
| helmor-debug-operate | 3 | Debugging while operating Helmor |
| helmor-debug-loop | 3 | Debug loop workflows |
| helmor-bump-vendors | 3 | Bumping vendor dependencies |

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| Driving a local multi-agent workbench | Use helmor-cli to orchestrate coding agents from the terminal |
| Shipping release candidates | Apply helmor-release for repeatable release workflows |
| Troubleshooting workbench issues | Use helmor-debug-operate and helmor-debug-loop for structured debugging |

## Limitations / Verification

- The Sep 29, 2026 snapshot records 0/5 skills with published verification entries.
- Nearly all indexed installs are concentrated in helmor-cli; the other four skills are young.
- The main-branch README was fetched for context; star and install counts come from the marketplace snapshot. No live install test has been run from Hermes yet.

## Security

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Skills Marketplace](/hermes/skills/marketplace)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
