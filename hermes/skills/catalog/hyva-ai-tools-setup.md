---
title: "Hyva AI Tools - Magento Front-End for Agents"
description: "hyva-themes/hyva-ai-tools on skills.sh: 14.0K combined installs across 13 listings; Hyva child themes, Alpine components and Magento modules."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/hyva-ai-tools-setup/"
robots: "index,follow"
last_updated: "2026-11-04"
tags: ["hermes skill", "agent skill", "skill setup", "magento", "hyva"]
---

# Hyva AI Tools - Setup Guide

**Source:** [hyva-themes/hyva-ai-tools](https://www.skills.sh/hyva-themes/hyva-ai-tools) via skills.sh - 14.0K combined installs across 13 indexed listings; first documented November 4, 2026 (morning sweep)
**GitHub:** 85 stars, OSL-3.0 licence, last pushed 2026-07-31, 13 SKILL.md directories under skills/
**Category:** Magento storefronts for agents: Hyva child themes, Alpine components, CMS components and Tailwind compilation
**Quality Tier:** 🟢 Green: all five sampled skills pass Gen Agent Trust Hub, Socket and Snyk, and the publisher ships a security policy

Hyva replaces the standard Magento front end (Knockout, RequireJS, Less) with Alpine.js and Tailwind, which means most generic Magento advice an agent has absorbed is wrong for a Hyva storefront. This pack is the corrective: thirteen skills written by the theme vendor that cover child theme scaffolding, CSP-compatible Alpine components, CMS component authoring, Tailwind compilation and Magento module creation.

The pack is small and internally consistent. Nine of the thirteen skills sit above 1,200 installs, and the set is designed to be installed piecemeal: each SKILL.md declares a requires: line, and the installer walks that graph, so asking for hyva-child-theme also brings in hyva-exec-shell-cmd, hyva-theme-list and hyva-compile-tailwind-css.

The emphasis on Alpine CSP is the detail worth noting. The vendor's Alpine guidance targets the CSP build that runs without unsafe-eval, which is the variant needed for PCI-DSS 4.0 compliance on payment pages, so the skills are aimed at checkout-adjacent storefront work rather than marketing pages alone.

## Installation

The README recommends per-skill installs from a clone, with dependencies resolved automatically:

```bash
git clone https://github.com/hyva-themes/hyva-ai-tools.git
```

```bash
./hyva-ai-tools/install-hyva-skill.sh hyva-child-theme claude
```

```bash
./hyva-ai-tools/install-hyva-skill.sh hyva-cms-component
```

```bash
./hyva-ai-tools/install-hyva-skill.sh --list
```

Skills are symlinked into the target agent's skills directory by default, so a git pull inside the clone updates every installed skill at once. Use --copy when the agent runs somewhere the symlink cannot reach, such as a container:

```bash
./hyva-ai-tools/install-hyva-skill.sh --copy hyva-child-theme claude
```

Copied skills do not follow git pull; re-run the install command to refresh them. When no agent argument is given the installer checks the HYVA_SKILLS_AGENT environment variable, then auto-detects an existing agent directory in the working directory, then prompts. Supported agents are claude, codex, copilot, cursor, gemini, junie and opencode.

There is also a legacy install-all route, which copies rather than symlinks:

```bash
curl -fsSL https://raw.githubusercontent.com/hyva-themes/hyva-ai-tools/refs/heads/main/install.sh | sh -s claude
```

None of the supported agent names is Hermes, so the practical path is to clone, run the installer with --copy, and move the resulting skill directories into your Hermes agent skills directory.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| hyva-exec-shell-cmd | 1,328 | Detect Warden, DDEV, docker-magento or local and pick the right command wrapper |
| hyva-alpine-component | 1,321 | CSP-compatible Alpine.js components for Hyva templates |
| hyva-child-theme | 1,307 | Scaffold a child theme with structure, Tailwind and inheritance |
| hyva-compile-tailwind-css | 1,292 | Build development and production Tailwind CSS for a theme |
| hyva-render-media-image | 1,287 | Responsive image markup through the Hyva Media view model |
| hyva-ui-component | 1,286 | Install Hyva UI templates such as header, footer, gallery and minicart |
| hyva-playwright-test | 1,283 | Playwright E2E tests and page objects for Hyva and Alpine |
| hyva-theme-list | 1,281 | List Hyva theme paths in a Magento 2 project |
| hyva-create-module | 1,280 | Scaffold a Magento 2 module in app/code |
| hyva-cms-component | 768 | Custom Hyva CMS components with presets, variants and PHTML templates |
| hyva-cms-custom-field | 757 | Custom field types and field handlers for Hyva CMS |
| hyva-cms-components-dump | 749 | Dump the merged components JSON from active modules |
| hyva-tailwind-include-exclude | 25 | Add a module path to the include or exclude list in hyva.config.json |

No indexed listings fall below the threshold; all 13 appear above.

## Why This Matters for Hermes Agents

Magento is one of the stacks where an agent's training data is actively misleading: most public examples target Luma, Knockout and Less, and pasting those into a Hyva theme produces broken markup. A vendor-written skill set removes that failure mode at the source.

The dependency graph is the part worth copying into your own skill libraries. Each skill declares requires: in its frontmatter (hyva-ui-component pulls in four others), and the installer resolves the chain. An agent can ask for one capability and still get a coherent environment, which is the difference between a skill library and a folder of prompts.

The utility skills also show a clean separation of concerns. hyva-exec-shell-cmd exists only to detect whether the project runs under Warden, DDEV, docker-magento or bare metal and to return the right command prefix; every other skill delegates to it instead of guessing at docker exec syntax.

The scope is narrow on purpose. If you do not run Magento 2 with Hyva, there is nothing here for you, and the 85-star footprint reflects a vendor utility rather than a general-purpose pack.

## Usage

| You say | What happens |
|---|---|
| "Create a Hyva child theme called Storefront" | hyva-child-theme scaffolds the directory tree and theme inheritance, then installs the Tailwind skills it requires |
| "Build an Alpine dropdown that passes CSP" | hyva-alpine-component writes CSP-safe Alpine with no unsafe-eval patterns |
| "Add a hero banner CMS component" | hyva-cms-component generates components.json entries and PHTML templates |
| "My Tailwind classes stopped applying" | hyva-compile-tailwind-css rebuilds the stylesheet and checks the include and exclude lists |
| "Add a custom field to this CMS component" | hyva-cms-custom-field creates the field type and its handler |
| "Write a Playwright test for the product page" | hyva-playwright-test produces page objects and selectors that work with Alpine |
| "Which themes exist in this project?" | hyva-theme-list returns every Hyva theme path, locally or in the container |

## Verification

List what the installer can see before installing anything:

```bash
./hyva-ai-tools/install-hyva-skill.sh --list
```

Then fetch one raw skill file to confirm the tree matches what skills.sh indexed. This URL is the skills/hyva-child-theme/SKILL.md path on branch main:

```bash
curl -fsSL https://raw.githubusercontent.com/hyva-themes/hyva-ai-tools/main/skills/hyva-child-theme/SKILL.md | head -30
```

A response with YAML frontmatter, a name field and a requires: line confirms the content is live and that dependency resolution will work. After installing, confirm the skill landed where the agent looks:

```bash
ls .claude/skills
```

## Security

skills.sh verdicts for sampled skills (verified November 4, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| hyva-exec-shell-cmd | Pass | Pass | Pass |
| hyva-compile-tailwind-css | Pass | Pass | Pass |
| hyva-playwright-test | Pass | Pass | Pass |
| hyva-cms-component | Pass | Pass | Pass |
| hyva-tailwind-include-exclude | Pass | Pass | Pass |

The repository ships a SECURITY.md with a reporting address (security@hyva.io) and states there is no paid bug bounty. The one skill to read before unattended use is hyva-exec-shell-cmd: its job is to execute shell commands in the project environment, and it decides the wrapper by detecting the local setup.

## Limitations

- Snapshot data, verified November 4, 2026: 13,964 combined installs across 13 indexed listings; 85 GitHub stars; OSL-3.0 licence; last pushed 2026-07-31. Counts drift over time.
- Magento 2 with the Hyva theme only. The skills assume app/code, hyva.config.json and a Hyva theme structure, and offer nothing for Luma or headless storefronts.
- The installer supports claude, codex, copilot, cursor, gemini, junie and opencode; Hermes is not on that list, so a manual copy step is required.
- OSL-3.0 is a reciprocal licence rather than a permissive one. Check your obligations before bundling these skills into a distributed product.
- The last listing sits at 25 installs and the repository was last pushed 2026-07-31, so treat the pack as stable rather than actively developed.
- hyva-exec-shell-cmd runs commands in your environment; review its detection logic and keep it out of unattended runs against production.

## Related

- [Webflow Skills - Site Building for Agents Setup](/hermes/skills/catalog/webflow-skills-setup)
- [Interface Design Skill - Non-Templated Product UI Setup](/hermes/skills/catalog/interface-design-skill-setup)
- [Frontend God Mode - Design Skills Bundle Setup](/hermes/skills/catalog/frontend-god-mode-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install hyva-child-theme first. It pulls the utility chain in for you, and every other skill then has what it needs.
- Prefer symlinks over --copy unless you run the agent in a container; git pull then updates all thirteen skills at once.
- Set HYVA_SKILLS_AGENT in your shell profile to skip the interactive agent prompt on every install.
- Ask the agent to run hyva-theme-list before any theme work. Most bad output starts with the agent guessing at a theme path.
- If Tailwind classes silently stop applying, run hyva-compile-tailwind-css before editing templates; the include and exclude lists are the usual cause.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
