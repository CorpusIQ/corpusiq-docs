---
title: "Home Assistant Skills - Automation Setup Guide"
description: "homeassistant-ai/skills: 9.3K combined installs from one listing, a Home Assistant best-practice skill for automations, dashboards and safe refactors."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/home-assistant-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-15"
tags: ["hermes skill", "agent skill", "skill setup", "home assistant", "smart home", "automation"]
---

# Home Assistant Skills - Setup Guide

**Source:** [homeassistant-ai/skills](https://www.skills.sh/homeassistant-ai/skills) via skills.sh - 9.3K combined installs across 1 indexed listing; first seen Nov 14, 2026 (Nov 14 evening sweep)
**GitHub:** 978 stars, MIT license, `main` branch, last pushed 2026-10-29, one `SKILL.md` at `skills/home-assistant-best-practices/SKILL.md` with fifteen reference files behind it and 31 eval cases under `evals/`
**Category:** Home automation authoring and operations
**Quality Tier:** 🟢 Green - the single sampled skill passes all three auditors.

The Home Assistant skills repository ships one skill, `home-assistant-best-practices`, built around a decision workflow and an anti-pattern table rather than around documentation. The premise is that agents already know Home Assistant exists and make the same predictable mistakes with it: Jinja template conditions where a native condition belongs, `device_id` where `entity_id` is required, `mode: single` on a motion light, renames that silently break dashboards and scripts downstream.

Each anti-pattern in the table comes with its fix, and the reference files carry the depth: triggers and conditions, helper selection, dashboards and cards, blueprints, scenes, device control, YAML-only integrations, backups, and AppDaemon. The repository also ships an eval suite, which is unusual for a Markdown skill and is the clearest signal of how seriously the authors treat correctness.

## Installation

Install with the Agent Skills installer, which requires Node.js 22.20 or later:

```bash
npx skills add homeassistant-ai/skills
```

Add `-g` to install for every project instead of the current one, and run `npx skills update` to move to a newer version. This works with Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI and the other clients that follow the Agent Skills standard.

For Claude Code's own plugin cache, run these inside Claude Code instead:

```text
/plugin marketplace add homeassistant-ai/skills
/plugin install home-assistant-skills@home-assistant-skills
```

Claude Desktop and claude.ai take the same repository as a marketplace from Customize, Plugins, Add marketplace, with cloud code execution enabled first. Auto-update is off by default for third-party marketplaces, so turn it on in the marketplace entry or update by hand.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| home-assistant-best-practices | 9,310 | Authoring and reviewing Home Assistant automations, scripts, scenes, helpers, dashboards, blueprints, backups and AppDaemon apps. |

The single indexed listing appears in the table above.

## Why This Matters for Hermes Agents

Home Assistant configuration fails in ways that look correct until the system loads it. A template condition is checked for Jinja syntax alone, so a typo in an entity name survives until the automation runs; a native condition is validated key by key when the automation loads. The skill encodes that difference as a rule and shows the before-and-after YAML, which is exactly the shape an agent can apply without being told twice.

The reference split matters for context cost. `SKILL.md` is a router with an anti-pattern table and pointers, and the agent loads only the reference that matches the task: `helper-selection.md` for choosing a helper, `safe-refactoring.md` before a rename, `dashboard-cards.md` for a card question. A question about a single automation does not pull in the AppDaemon documentation.

The rename path is the one that saves real damage. Renaming an entity in Home Assistant silently breaks every dashboard, script and automation that referenced the old identifier, and the repository ships `references/safe-refactoring.md` plus eval cases named for exactly this migration. For an agent editing a live smart-home configuration, that is the difference between a change and an outage.

## Usage

| You say | What happens |
|---|---|
| "Turn on the hallway light when motion is detected and off five minutes after it stops" | Writes the automation with native triggers and conditions, and picks the right mode instead of leaving it at single. |
| "Why did my automation never fire?" | Walks the trigger and condition rules, including template-versus-native validation, and names the likely cause. |
| "Rename sensor.living_room to sensor.lounge" | Loads the safe refactoring workflow and lists the dashboards, scripts and automations that reference the old identifier first. |
| "Should this be a helper or a template?" | Uses the helper selection reference and recommends the helper type that fits the device behaviour. |
| "Build a dashboard for the upstairs rooms" | Uses the dashboard guide and card references, with the layout and card patterns the repository documents. |
| "Back up before I change the configuration" | Loads the backups reference and walks the backup and recovery path. |
| "This automation needs real Python logic" | Checks the AppDaemon reference for when AppDaemon beats native Home Assistant, and how to structure the app. |

## Verification

Read the skill router before installing, and confirm the reference set resolves:

```bash
curl -fsSL https://raw.githubusercontent.com/homeassistant-ai/skills/main/skills/home-assistant-best-practices/SKILL.md | head -30
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/homeassistant-ai/skills/main/skills/home-assistant-best-practices/references/safe-refactoring.md
```

Both live under `skills/home-assistant-best-practices/`, so install and document paths that stop at the repository root will miss the real files.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-14) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| home-assistant-best-practices | Pass | Pass | Pass |

The repository holds Markdown, YAML examples and eval fixtures with no executable install script, and the client-side installers copy files into the agent's skills directory.

## Limitations

- Snapshot data, verified 2026-11-14: 9,310 combined installs across 1 indexed listing; 978 GitHub stars; MIT; last pushed 2026-10-29. Counts drift over time.
- One skill only. The suite does not include separate skills for companion projects such as ESPHome, Zigbee or Node-RED, and those are outside its coverage.
- The installer path needs Node.js 22.20 or later, which is newer than the Node floor of many other skills.
- Auto-update is off by default when installed as a Claude Code marketplace plugin, so an agent can run a stale copy without warning.
- The eval cases under `evals/` are the authors' test fixtures, not a live test harness you can run against your own configuration.
- Advice targets current Home Assistant releases; a long-unmaintained installation may disagree with the recommended patterns.

## Related

- [AAHL Skills - Smart Home & TTS Setup](/hermes/skills/catalog/aahl-skills-setup)
- [Docker Agent Skills - Container Workflow Suite](/hermes/skills/catalog/docker-agent-skills-setup)
- [Make Platform Skills - Make.com Automation Setup](/hermes/skills/catalog/make-platform-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Ask for the rename impact list before any entity rename, even when the change looks cosmetic: display names and storage dashboards are the documented blind spots.
- Keep `references/examples.yaml` open when the agent writes YAML; it is the repository's own worked example set.
- Prefer the native condition over a template whenever both would work, so Home Assistant validates the entity and threshold at load time.
- Enable marketplace auto-update, or run `npx skills update` on a schedule, so the anti-pattern table stays current with Home Assistant releases.
- Point the agent at one reference file per question. Loading the whole reference set costs context and rarely improves the answer.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
