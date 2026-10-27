---
title: "Claude Code Extensions - Agents, Skills & Hooks Setup"
description: "Setup guide for nodnarbnitram/claude-code-extensions - 9.6K combined installs. Modular plugin suite: 60+ agents, 18 skills, 8 hooks, 11 commands."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/nodnarbnitram-claude-code-extensions-setup/"
robots: "index,follow"
last_updated: "2026-10-24"
tags: ["hermes skill", "agent skill", "skill setup", "claude code", "agent plugins"]
---

# Claude Code Extensions - Setup Guide

**Source:** [nodnarbnitram/claude-code-extensions](https://www.skills.sh/nodnarbnitram/claude-code-extensions) via skills.sh - 9.6K combined installs across 23 indexed listings; first seen Oct 11, 2026 (morning sweep)
**GitHub:** [nodnarbnitram/claude-code-extensions](https://github.com/nodnarbnitram/claude-code-extensions) (16 stars, MIT license; pushed Apr 20, 2026; `.claude/skills/<name>/SKILL.md` layout; 21 self-contained plugins)
**Category:** Developer Tooling / Claude Code Plugins
**Quality Tier:** 🔵 Community - independent modular plugin collection (16 stars, MIT); broad multi-stack coverage; last push Apr 2026

Publisher nodnarbnitram ships a 21-plugin extension collection for Claude Code: 60+ specialized agents, 18 model-invoked skills, 8 lifecycle hooks, and 11 slash commands, packaged as self-contained bundles that can be installed individually from a single marketplace. Coverage spans core orchestration (code review, research coordination, planning) plus deep stacks: Kubernetes, Cloudflare Workers, ESPHome, React, Django, Vue, Temporal, Grafana, Home Assistant, and Tauri.

The install counts show where demand concentrates: tauri-v2 alone carries 7,662 of the 9,637 combined installs, and the smart-home cluster (Home Assistant, ESPHome, and Frigate skills) forms the deepest vertical in the set. Safety hooks (dangerous-command blocking, .env protection, audit logging) and auto-linting ship in the core plugin, and a standalone Python installer merges settings.json safely for projects that prefer a clone over the plugin path.

---

## Installation

Prerequisites: Claude Code for the plugin path, or Python 3.11+ and uv for the standalone installer. Install through Claude Code's plugin marketplace for multi-project setups:

```bash
# In any Claude Code session:
/plugin marketplace add github:nodnarbnitram/claude-code-extensions

# Essential foundation (contains the hooks and core agents):
/plugin install cce-core@cce-marketplace

# Add plugins for your stack:
/plugin install cce-tauri@cce-marketplace
/plugin install cce-homeassistant@cce-marketplace
```

For a single project or a custom setup, install from a clone:

```bash
git clone https://github.com/nodnarbnitram/claude-code-extensions.git
cd claude-code-extensions
./install_extensions.py install ~/my-project
```

The installer lists extensions, previews changes with `--dry-run`, and merges settings.json without conflicts.

## What It Provides

Install counts from the Oct 11, 2026 skills.sh snapshot:

| Skill | Installs | Use For |
|---|---|---|
| tauri-v2 | 7,662 | Tauri v2 cross-platform desktop and mobile apps with Rust backend, IPC patterns, and security configuration |
| code-reviewer | 291 | Read-only code review for best practices, security issues, and potential bugs |
| ha-voice | 216 | Home Assistant Assist voice control: pipelines, intents, and wake words |
| esphome-config-helper | 133 | ESPHome configuration generation, GPIO reference, compile-error troubleshooting, and validation |
| frigate-configurator | 111 | Frigate NVR YAML, object detection, zones, and hardware acceleration (Coral TPU, OpenVINO) with Home Assistant integration |
| ha-energy | 101 | Home Assistant energy monitoring: solar, grid, and device tracking dashboards |
| ha-automation | 87 | Home Assistant automations, scripts, blueprints, and Jinja2 templates |
| kubernetes-operations | 83 | Kubernetes debugging, resource management, and cluster operations with token-efficient scripts |
| kubernetes-health | 82 | Cluster health diagnostics with dynamic API discovery and operator-specific agents |
| ha-api | 81 | Home Assistant REST and WebSocket API integration |
| ha-dashboard | 74 | Home Assistant Lovelace dashboards, cards, views, and themes |
| ha-addon | 74 | Home Assistant add-on development with Docker, Supervisor API, and multi-arch builds |
| commit-helper | 74 | Conventional commit messages generated from git diffs |
| ha-integration | 70 | Custom Home Assistant integrations, config flows, entities, and platforms |
| esphome-box3-builder | 69 | ESP32-S3-BOX-3 templates: display lambdas, touch patterns, and voice assistant audio pipelines |
| grafana-plugin-scaffolding | 67 | Scaffold Grafana plugins (panel, data source, app, backend) with a Docker dev environment |
| grafana-billing | 65 | Prometheus and Loki billing metrics from Grafana Cloud for cost analysis |
| cloudflare-vpc-services | 65 | Cloudflare VPC Services and cloudflared tunnels so Workers reach private APIs |
| vitest-v4 | 59 | Vitest 4 testing: Vite-native configuration, mocks, Browser Mode, coverage, and migration |
| typescript-v6 | 58 | TypeScript 6 tsconfig migrations, deprecations, module resolution, and modern standard-library types |
| vite-v8 | 50 | Vite 8 development with Rolldown, Oxc, environment-aware plugins, SSR, and migration guidance |

The remaining 2 indexed listings range from 26 to 39 installs: linear (39) and triage-workflow (26).

## Why This Matters for Hermes Agents

Agent-skill folders are becoming the portable unit of agent capability, and this repo shows how far one publisher can push the pattern: 21 self-contained bundles of agents, skills, hooks, and commands distributed through a marketplace, a Python installer, or a manual copy. Three details matter for anyone building with agents. The hooks layer is the pattern every harness needs before running unattended: a pre-tool-use guard that blocks dangerous commands and protects .env files, plus post-tool audit logging and auto-linting. The domain depth is real operational knowledge, not prompt wrappers: Kubernetes diagnostics with dynamic operator discovery, Frigate NVR tuning with Coral TPU and OpenVINO detection, ESPHome device configuration, and Grafana plugin scaffolding. And the packaging travels: the same SKILL.md folders install under Claude Code, are noted as working in opencode, and map onto the skills.sh distribution channel that Hermes agents already use. If you maintain an internal skills library, this is a useful reference for splitting one into modular, independently installable pieces.

## Usage

| You say | What happens |
|---|---|
| "Review my recent changes before I commit" | code-reviewer analyzes the diff read-only and commit-helper drafts the message |
| "My Home Assistant automation keeps misfiring" | ha-automation debugs automations, scripts, blueprints, and Jinja2 templates |
| "Scaffold a Tauri v2 desktop app" | tauri-v2 walks through the Rust backend, IPC patterns, and security configuration |
| "Set up voice control for my smart home" | ha-voice configures Assist pipelines, intents, and wake words |
| "Why is my cluster unhealthy?" | kubernetes-health runs diagnostics with dynamic API discovery across operators |
| "Migrate this project to Vite 8 and TypeScript 6" | vite-v8 and typescript-v6 guide the migration flags and config changes |
| "Scaffold a Grafana plugin" | grafana-plugin-scaffolding generates the plugin structure with a Docker dev environment |

## Verification

```bash
# Confirm the marketplace and installed plugins in a Claude Code session
/plugin marketplace add github:nodnarbnitram/claude-code-extensions
/plugin

# Review the tauri-v2 skill from GitHub before installing
curl -sL https://raw.githubusercontent.com/nodnarbnitram/claude-code-extensions/main/.claude/skills/tauri-v2/SKILL.md | head -20

# Standalone path: clone and preview an install
git clone https://github.com/nodnarbnitram/claude-code-extensions.git
cd claude-code-extensions && ./install_extensions.py install --dry-run ~/my-project
```

## Security

skills.sh verdicts for sampled skills (verified Oct 11, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| tauri-v2 | Pass | Pass | Pass |
| code-reviewer | Pass | Pass | Pass |
| ha-voice | Pass | Pass | Pass |
| kubernetes-operations | Pass | Pass | Pass |
| esphome-config-helper | Pass | Pass | Pass |
| frigate-configurator | Pass | Pass | Pass |

## Limitations

- Independent collection: 16 GitHub stars and a single maintainer; the last push was Apr 20, 2026, so review the hooks against current Claude Code releases before enabling them in production projects.
- Install concentration: tauri-v2 alone accounts for about 80% of the combined installs (7,662 of 9,637); most other listings sit in the double digits.
- The hooks intercept commands and file writes (dangerous-command blocking, .env protection, and audit logging are documented defaults); read `.claude/hooks/` before enabling them in a project that handles secrets.
- The install index runs slightly ahead of both the README table (18 skills) and the repo tree (22 folders): esphome-config-helper, esphome-box3-builder, frigate-configurator, and cloudflare-vpc-services ship inside plugin bundles, while triage-workflow (26 installs) has no counterpart folder in the current tree.
- The README notes the extensions "can typically also be used in opencode"; non-Claude agent support is community-reported rather than guaranteed.
- Snapshot data, verified Oct 11, 2026: 9,637 combined installs across 23 indexed listings; 16 GitHub stars; MIT; last pushed Apr 20, 2026. Counts drift over time.

## Related

- [Steipete Agent Scripts - Portable Agent Skills & Helpers Setup](/hermes/skills/catalog/steipete-agent-scripts-setup) - another portable multi-agent skill collection with sync and validation tooling
- [Callicrate Skills - AGENTS.md & Documentation Authoring Setup](/hermes/skills/catalog/callicrate-skills-setup) - agent-instruction and documentation authoring companion
- [Moonlight Lupin Agent Skills - Hermes Skill Suite Setup](/hermes/skills/catalog/moonlight-lupin-agent-skills-setup) - a Hermes-native multi-skill suite with skill-retrieval tooling
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install cce-core first (13 core agents, 8 hooks, and the safety layer); every other plugin layers on top.
- Preview standalone installs with `install_extensions.py install --dry-run ~/my-project` before merging settings.json.
- Use the meta-agent to generate new specialist agent configs from a description instead of hand-writing them.
- Home Assistant users get the deepest coverage in the set (7 experts, 8 skills, 3 commands in cce-homeassistant); start with ha-automation and ha-voice.
- Pin the plugin set per project rather than installing all 21 globally, so each repo loads only its stack.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
