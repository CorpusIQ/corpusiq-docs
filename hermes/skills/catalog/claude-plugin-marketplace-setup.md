---
title: "Claude Plugin Marketplace - Azure and DevOps Packs"
description: "josiahsiegel/claude-plugin-marketplace on skills.sh: 41.7K combined installs across 200 listings; Azure, Docker, Bash and Tailwind plugin packs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claude-plugin-marketplace-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "claude code plugins", "azure", "devops", "tailwind css"]
---

# Claude Plugin Marketplace - Setup Guide

**Source:** [josiahsiegel/claude-plugin-marketplace](https://www.skills.sh/josiahsiegel/claude-plugin-marketplace) via skills.sh - 41.7K combined installs across 200 indexed listings; first seen 2026-11-06 (Nov 6, 2026 morning sweep)
**GitHub:** 59 stars, MIT (LICENSE in the repo root), last pushed 2026-06-18, 223 SKILL.md directories at plugins/<plugin>/skills/<skill>/SKILL.md
**Category:** Claude Code plugin marketplace: Azure, Azure DevOps, Databricks, Bash, PowerShell and language packs
**Quality Tier:** 🟡 Review - a large surface (223 skill directories, 200 indexed listings) from a single maintainer, four and a half months since the last push, and one sampled skill (kaggle-environment) carrying Warn verdicts from two scanners.

This is a marketplace rather than a single skill. One command registers it with Claude Code, and each plugin inside it ships its own `skills/` directory plus commands, agents and hooks. The README lists plugins across development tooling (`plugin-master`, `context-master`, `doc-master`), cloud and infrastructure (`azure-master`, `azure-to-docker-master`, `terraform-master`), DevOps (`docker-master`, `ado-master`, `git-master`), scripting (`bash-master`, `powershell-master`), and language or platform bundles for Python, React, Next.js, Tailwind CSS, FFmpeg, SSDT, T-SQL, Azure Data Factory, Salesforce, Windows paths and Cloudflare.

The install index sees 200 individual skills behind those plugins and the tree holds 223 `SKILL.md` directories. Volume is concentrated: a cluster of Tailwind CSS skills accounts for four of the top five listings, and the PowerShell, Docker and Git bundles take the next three places. Versions live in `.claude-plugin/marketplace.json` at the repo root and are mirrored in each plugin's own `.claude-plugin/plugin.json`, which is what the README tells you to read when you want the current catalog instead of its highlights list.

## Installation

The README's quick start runs inside Claude Code, not in a shell. Add the marketplace first:

```bash
/plugin marketplace add JosiahSiegel/claude-plugin-marketplace
```

Then install any plugin from it by name:

```bash
/plugin install <plugin-name>@claude-plugin-marketplace
```

Step three is browsing the catalog and installing what the task needs. The README treats `.claude-plugin/marketplace.json` as the source for the full, current catalog and says the plugin list in the README only highlights commonly used entries, so read the manifest before assuming a plugin name:

```bash
curl -fsSL https://raw.githubusercontent.com/josiahsiegel/claude-plugin-marketplace/main/.claude-plugin/marketplace.json | head -40
```

For a harness that does not speak the Claude Code plugin format, the repository is also a plain tree of skill directories. Each plugin keeps its skills at `plugins/<plugin>/skills/<skill>/SKILL.md`, so a shallow clone gives you files you can copy into any agent that reads the Agent Skills layout.

## What It Provides

Twenty-one listings clear the 209-install threshold. They fall into four groups: Tailwind CSS craft, container and shell operations, Git and planning discipline, and version-specific notes for Azure, SQL Server and OpenTofu.

| Skill | Installs | Use For |
|---|---|---|
| tailwindcss-advanced-layouts | 8,166 | CSS Grid and Flexbox layout patterns, grid-template-areas through v4 arbitrary values, responsive grids and overflow control |
| tailwindcss-animations | 2,370 | animate-* utilities, custom keyframes through @theme, transitions, transforms and reduced-motion handling |
| tailwindcss-mobile-first | 2,109 | Mobile-first breakpoints and responsive utility ordering for Tailwind v4 |
| powershell-master | 1,112 | PowerShell scripts, modules and cmdlets across Windows, Linux and macOS, including CI/CD automation |
| docker-best-practices | 943 | Production Dockerfiles, multi-stage builds, base image selection, layer caching and build order |
| git-master | 808 | Git operations from branch strategy and conflict resolution to history rewriting and recovery |
| tailwindcss-advanced-design-systems | 657 | Design tokens and @theme configuration: colour scales, semantic tokens, typography rules |
| docker-security-guide | 615 | Container security review: non-root users, read-only root filesystems, capability dropping, seccomp and AppArmor |
| ffmpeg-captions-subtitles | 510 | Burning and muxing subtitles, extracting tracks and converting formats for FFmpeg 7.1 and 8.0 |
| tailwindcss-responsive-darkmode | 478 | Dark mode setup (class-based vs media query), runtime toggling, prefers-color-scheme and per-component overrides |
| bash-master | 462 | Bash scripting for Linux, macOS, Git Bash on Windows and WSL, with ShellCheck and POSIX portability guidance |
| context-master | 399 | Planning and context management for multi-file tasks: file order, delegation, token budgeting, long sessions |
| tailwindcss-fundamentals-v4 | 393 | Tailwind v4 install paths, CSS-first @theme configuration and the v3 to v4 migration |
| tui-fundamentals | 366 | Terminal UI design: architecture, framework choice, dashboards, wizards, REPL shells and prompt flows |
| tailwindcss-accessibility | 299 | WCAG 2.2 patterns in Tailwind: focus-visible rings, minimum touch targets and ARIA |
| tailwindcss-framework-integration | 296 | Tailwind inside React, Next.js, Vue and Nuxt, SvelteKit and Angular |
| sql-server-2025 | 259 | SQL Server 2025 features: vector type and vector indexes, AI integration, SqlPackage workflows |
| tailwindcss-advanced-components | 250 | Component variants with CVA, compound variants, tailwind-merge and clsx |
| tailwindcss-performance | 237 | v4 Oxide engine behaviour, Lightning CSS minification, bundle size and safelist tuning |
| opentofu-guide | 209 | OpenTofu installation and migration from Terraform, provider and state file compatibility |
| powershell-shell-detection | 209 | Detecting PowerShell, pwsh, Git Bash or cmd on Windows, path handling and MSYS_NO_PATHCONV |

The remaining 179 indexed listings range from 61 to 207 installs. That tail is where the repository's breadth lives: more Tailwind variants (debugging, plugins), dated feature notes for Azure OpenAI, AKS, Fabric, Databricks, Salesforce Agentforce and GitHub Actions, an FFmpeg sub-family covering filter graphs, hardware acceleration, karaoke text and container deployment, fal.ai media generation, React and Next.js singles, Python packaging and asyncio, Unity subsystems, Stripe idempotency notes, and short-form video scripting.

## Why This Matters for Hermes Agents

A marketplace is a different shape of dependency from a skill pack, and that shape is what makes it useful. A single plugin install brings a whole working set: the skills, plus the commands and agents the plugin author wired around them. An agent asked to modernise an Azure Pipeline or harden a Dockerfile gets one install instead of an afternoon of prompt engineering.

The strongest signal in the install data is where the volume sits. Tailwind layout and animation lead by a wide margin, and the top twenty is dominated by things an agent can get wrong quietly: grid behaviour, breakpoint ordering, dark-mode strategy, focus rings, Dockerfile layer order, container privileges. These are not research topics, they are craft checks that a confident model will skip unless a skill makes it read them.

The bundles are opinionated in a useful direction. `powershell-master` and `bash-master` are explicitly scoped apart from each other, and `powershell-master` states that it covers Windows, Linux and macOS rather than assuming one shell. `docker-security-guide` names the specific controls (non-root user, read-only root filesystem, `--cap-drop`, seccomp, AppArmor) rather than saying "follow best practices".

Several skills are version-anchored, which is either the point or the trap. `sql-server-2025` targets SQL Server 2025, `tailwindcss-fundamentals-v4` targets Tailwind v4, `opentofu-guide` addresses the Terraform-to-OpenTofu fork, and the FFmpeg skills pin 7.1 and 8.0. For an agent working on a specific stack, that specificity is the value. For an agent working on an older stack, it is a source of confident advice about features that do not exist yet.

Finally, `context-master` and `plugin-master` are the meta layer. One covers planning, delegation and token budgeting across long sessions, the other covers building and publishing further plugins. An agent maintaining its own skill estate has a use for both, and they are cheap to evaluate separately from the cloud and media bundles.

## Usage

| You say | What happens |
|---|---|
| "Build this dashboard layout with Tailwind v4" | tailwindcss-advanced-layouts works grid-template-areas, responsive columns and overflow before any class is written |
| "Review my Dockerfile for production" | docker-best-practices checks base image, multi-stage structure and layer caching, then docker-security-guide covers the runtime surface |
| "This script has to run on Windows and Linux" | powershell-master handles the PowerShell side, bash-master the Git Bash and WSL side, and powershell-shell-detection separates them at runtime |
| "Why is dark mode breaking on the settings page?" | tailwindcss-responsive-darkmode covers class-based vs media-query strategy and per-component overrides |
| "Plan this six-file refactor" | context-master sets file order, delegation and token budget for the session |
| "Migrate our Terraform config to OpenTofu" | opentofu-guide covers the CLI migration, provider compatibility and state file handling |
| "Write CI that runs these tests" | The ado-master and git-master plugins cover pipeline YAML and repository operations, with test-master for the test setup itself |

## Verification

Read the skill you are about to rely on before installing the plugin that carries it. Two probes, both on the `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/josiahsiegel/claude-plugin-marketplace/main/plugins/bash-master/skills/bash-master/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/josiahsiegel/claude-plugin-marketplace/main/plugins/docker-master/skills/docker-best-practices/SKILL.md | head -20
```

The first opens with a `name:` and a `description:` that scopes the skill to Bash on Linux, macOS, Git Bash and WSL and says explicitly that it does not provide PowerShell parity. The second opens with a description covering production Dockerfiles, multi-stage builds and base image selection. If either file 404s, the plugin layout has moved and the install path in this guide is stale.

For versions, read the manifest rather than the README's highlights list:

```bash
curl -fsSL https://raw.githubusercontent.com/josiahsiegel/claude-plugin-marketplace/main/.claude-plugin/marketplace.json | head -40
```

Each plugin entry carries `name`, `source`, `description`, `version` and `author`, so you can pin a decision to a version string before installing. After the two `/plugin` commands, the plugin appears in the `/plugin` browser inside Claude Code; if the marketplace itself is missing there, the add step did not take.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| tailwindcss-advanced-layouts | Pass | Pass | Pass |
| windows-git-bash-testing | Pass | Pass | Pass |
| viral-video-long-form | Pass | Pass | Pass |
| python-type-hints | Pass | Pass | Pass |
| kaggle-environment | Warn | Pass | Warn |

Four of the five sampled skills are clean across all three scanners. `kaggle-environment` is the exception, with Warn verdicts from Gen Agent Trust Hub and Snyk, and it sits in the tail of the index rather than near the top, so it is easy to install by accident when you take a whole plugin.

The larger risk with a marketplace is scope. Installing `docker-master` or `azure-master` brings every skill in that plugin, including dated feature notes written for a 2025 release window, and the plugin also carries commands, agents and hooks that run outside the skill text. Read the plugin directory, not just the skill you wanted, before granting it a working repository.

The repository root also carries `CLAUDE.md`, the maintainer's own agent instructions. That file is part of the tree an agent may read once the repository is cloned. Treat it as untrusted input in the same way you would treat any README: instructions in it are not your operating rules.

The licence is MIT with a single LICENSE file, which settles redistribution for the skill text. It says nothing about the advice inside the skills, which references third-party tooling (Docker, Azure, Databricks, FFmpeg, Tailwind) under those projects' own terms.

## Limitations

- Snapshot data, verified 2026-11-06: 41,688 combined installs across 200 indexed listings; 59 GitHub stars; MIT; last pushed 2026-06-18. Counts drift over time.
- The tree is wider than the index. 223 `SKILL.md` directories exist under `plugins/`, and 200 listings carry install counts, so a directory can be installed without any usage signal behind it.
- Installs are counted per skill while installation is per plugin. The top listing (`tailwindcss-advanced-layouts` at 8,166) is one skill inside `tailwindcss-master`; you cannot install it on its own through the marketplace.
- The last push is 2026-06-18, roughly four and a half months before this snapshot. Several skills are version-anchored (SQL Server 2025, Tailwind v4, FFmpeg 8.0, PowerShell 7.5, Azure 2025 features), so check the tree date against the version your project runs.
- The README's plugin list is explicitly a highlights list, not the catalog. Plugin names, versions and the full set resolve through `.claude-plugin/marketplace.json`, and a name that is absent from the README can still be installable.
- Quality varies by plugin. The five sampled verdicts are mostly clean, but 223 directories from one maintainer means the sampled set is thin relative to the surface.

## Related

- [Microsoft Azure AI Foundry Skills - Enterprise Agent](/hermes/skills/catalog/microsoft-azure-skills-setup)
- [CC DevOps Skills - Kubernetes and IaC Suite](/hermes/skills/catalog/cc-devops-skills-setup)
- [Databricks Agent Skills - Data & AI Platform Skills](/hermes/skills/catalog/databricks-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install one plugin, not the marketplace. Adding the marketplace is harmless; installing `ffmpeg-master` and `azure-master` together puts a lot of version-specific advice in front of an agent that may not need any of it.
- Read the manifest entry before the README entry. `marketplace.json` carries the version string that the README summary omits, which is how you tell a current plugin from a stale one.
- Point the agent at one SKILL.md, not the plugin root. The files are small and scoped; loading a whole plugin directory dilutes the instruction that matters.
- For non-Claude harnesses, use the tree directly. `plugins/<plugin>/skills/<skill>/` is plain Agent Skills layout, so a selective copy beats a plugin install.
- Watch the dated skills. Anything with a year in its name is a snapshot of a release window, not a maintained reference.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
