---
title: "cmux Skills - Ghostty-Based macOS Terminal Setup"
description: "manaflow-ai/cmux-skills - 6.6K combined installs: public skills for working with cmux, a Ghostty-based macOS terminal for AI coding agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/manaflow-cmux-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-24"
tags: ["hermes skill", "agent skill", "skill setup", "cmux", "terminal", "macos"]
---

# cmux Skills - Setup Guide

**Source:** [manaflow-ai/cmux-skills](https://www.skills.sh/manaflow-ai/cmux-skills) via skills.sh - 6.6K combined installs across 12 indexed listings; first catalogued Nov 24, 2026 (Nov 24, 2026 evening sweep)
**GitHub:** [manaflow-ai/cmux-skills](https://github.com/manaflow-ai/cmux-skills) - 40 stars, MIT license, main branch, last pushed Sep 8, 2026; nine self-contained skill directories under skills/<name>/SKILL.md, several with a references/ folder, helper scripts, or agent configs.
**Category:** Terminal Skills (cmux)
**Quality Tier:** 🟠 Orange - cmux-freestyle fails Snyk and carries a Warn on Socket; cmux-browser carries Warn cells on Gen Agent Trust Hub and Snyk; the other 10 sampled skills pass.

manaflow-ai/cmux-skills publishes the public skills for working with cmux, a Ghostty-based macOS terminal with vertical tabs and notifications built for AI coding agents. The skills follow the Agent Skills format and work with any agent that supports the .agents/skills/ or .claude/skills/ conventions, including Claude Code, Codex, Cursor, Amp, OpenCode, and Goose.

Installation goes through the skills CLI (npx skills add manaflow-ai/cmux-skills) or by cloning the repository and symlinking individual skill directories into an agent skills directory. Each skill is a self-contained directory with a SKILL.md plus helper references, scripts, or agent configs.

## Installation

```bash
# Add all cmux skills globally (available to every agent on this machine)
npx skills add manaflow-ai/cmux-skills -g --all

# Or pick specific ones, for specific agents
npx skills add manaflow-ai/cmux-skills --skill cmux-cli cmux-config --agent claude-code

# List what's in the repo without installing
npx skills add manaflow-ai/cmux-skills --list
```

You can also clone the repository and symlink the skills you want into an agent skills directory, such as ~/.claude/skills/ or .agents/skills/.

## What It Provides

skills.sh publishes per-skill descriptions for 9 of the 12 indexed listings; cmux-settings, cmux-customize, and cmux-groups have no skill directory in the current tree and no indexed description, so their Use For cells are name-level.

| Skill | Installs | Use For |
|---|---|---|
| cmux-cli | 928 | reference for the cmux CLI: socket commands, workspaces, panes, surfaces, browser, hooks, feed, settings, and automation |
| cmux-browser | 835 | automating the browser inside cmux: snapshot refs, DOM actions, waits, screenshots, cookies, storage, tabs, downloads, and console |
| cmux-workspace | 829 | working inside the current cmux workspace and terminal: caller surface, panes, surfaces, tagged reloads, and socket targeting |
| cmux-config | 786 | configuring cmux through ~/.config/cmux/cmux.json: settings, tab bar customization, custom actions, and sidebar workspace groups |
| cmux-ref | 775 | interpreting pasted cmux workspace, pane, surface, and window refs or IDs as explicit target context |
| cmux-artifact | 721 | building durable HTML walkthrough artifacts for dogfooding, verification, demos, and evidence pages |
| cmux-sidebar-builder | 698 | building left-sidebar custom views with cmux's runtime SwiftUI-style interpreter |
| cmux-freestyle | 667 | bringing up cmux Cloud VMs on your own Freestyle account by minting a FREESTYLE_SANDBOX_SNAPSHOT |
| cmux-cloud | 203 | using cmux Cloud machines through the cmux vm CLI: create, attach, exec, snapshot, fork, restore, and port access |
| cmux-settings | 64 | cmux settings (name-level; no counterpart in the current skills/ tree) |
| cmux-customize | 63 | cmux customization (name-level; no counterpart in the current skills/ tree) |
| cmux-groups | 55 | sidebar workspace groups (name-level; no counterpart in the current skills/ tree) |

All 12 indexed listings clear the 55-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

cmux-skills packages a complex native tool, a Ghostty-based terminal, into small single-purpose skills with references and helper scripts. Each skill maps one surface of the terminal: CLI automation, browser surfaces, workspace targeting, config editing, and even a runtime SwiftUI-style sidebar interpreter. For a builder, the interesting pattern is cmux-ref, which teaches an agent to treat opaque workspace, pane, and surface identifiers as first-class context instead of guessing. The config skill shows how to wrap a JSON config file with a validation-aware helper script that strips JSONC comments and writes atomically. Read it as a reference for structuring agent-facing tooling around a desktop application, noting it is macOS-only and aimed at cmux users rather than a cross-platform drop-in.

## Usage

| You say | What happens |
|---|---|
| Configure cmux settings | Uses cmux-config to edit ~/.config/cmux/cmux.json through the typed settings helper |
| Drive the browser surface | Uses cmux-browser to take snapshots, run DOM actions, and manage tabs |
| Interpret this cmux ref | Uses cmux-ref to resolve pasted workspace, pane, and surface IDs |
| Build a sidebar view | Uses cmux-sidebar-builder to write a SwiftUI-style sidebar and preview it |
| Create a walkthrough artifact | Uses cmux-artifact to emit an HTML evidence page and open it in the workspace |
| Bring up cmux Cloud VMs on Freestyle | Uses cmux-freestyle to mint a FREESTYLE_SANDBOX_SNAPSHOT |
| Use a cmux Cloud machine | Uses cmux-cloud to create, attach, and exec on cloud VMs |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/manaflow-ai/cmux-skills/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/manaflow-ai/cmux-skills/main/skills/cmux-cli/SKILL.md | head -30
```

Both URLs return 200. After installing, run npx skills add manaflow-ai/cmux-skills --list to confirm the skills registered.

## Security

skills.sh verdicts for sampled skills (verified Nov 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| cmux-cli | Pass | Pass | Pass |
| cmux-browser | Warn | Pass | Warn |
| cmux-workspace | Pass | Pass | Pass |
| cmux-config | Pass | Pass | Pass |
| cmux-ref | Pass | Pass | Pass |
| cmux-artifact | Pass | Pass | Pass |
| cmux-sidebar-builder | Pass | Pass | Pass |
| cmux-freestyle | Pass | Warn | Fail |
| cmux-cloud | Pass | Pass | Pass |
| cmux-settings | Pass | Pass | Pass |
| cmux-customize | Pass | Pass | Pass |
| cmux-groups | Pass | Pass | Pass |

Two sampled skills carry non-Pass cells: cmux-freestyle fails Snyk and carries a Warn on Socket, and cmux-browser carries Warn cells on Gen Agent Trust Hub and Snyk. All 12 indexed listings were sampled.

## Limitations

- Snapshot data, verified Nov 24, 2026: 6,624 combined installs across 12 indexed listings; 40 GitHub stars; MIT license; last pushed Sep 8, 2026. Counts drift over time.
- The install index outruns the tree: cmux-settings, cmux-customize, and cmux-groups carry install counts but have no skill directory in the current tree, so their Use For cells are name-level.
- cmux-freestyle carries a Fail on Snyk and a Warn on Socket; cmux-browser carries Warn cells on Gen Agent Trust Hub and Snyk.
- cmux is macOS-only, so the skills target cmux users on that platform rather than general cross-platform agents.
- The repository is not archived, but the last push was Sep 8, 2026; the cmux terminal itself lives in a separate manaflow-ai/cmux repository.

## Related

[FuDesign2008 Open Skills - Jira, Git and Workflow Setup](/hermes/skills/catalog/fudesign-open-skills-setup) | [khasky - Awesome Agent Skills Setup](/hermes/skills/catalog/khasky-awesome-agent-skills-setup) | [Letta Skills - Shared Agent Knowledge Base Setup](/hermes/skills/catalog/letta-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run npx skills add manaflow-ai/cmux-skills --list before installing to see the full inventory without committing.
- Install per agent with --skill cmux-cli cmux-config --agent claude-code to keep each agent's surface small.
- Symlink individual skill directories into ~/.claude/skills/ or .agents/skills/ for version-controlled copies without the CLI.
- Edit cmux config through cmux-config rather than by hand; its helper script strips JSONC comments, writes atomically, and validates keys.
- Review cmux-freestyle's SKILL.md before use, since it carries the only Fail verdict in the sampled set.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
