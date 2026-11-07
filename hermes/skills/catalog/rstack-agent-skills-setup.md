---
title: "Rstack Skills - Rspack Ecosystem Maintenance"
description: "rstackjs/agent-skills on skills.sh: 11.7K combined installs across 24 listings; Rspack, Rsbuild, Rslib, Rspress and Rstest skills for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/rstack-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "rspack", "rsbuild", "frontend tooling"]
---

# Rstack Skills - Setup Guide

**Source:** [rstackjs/agent-skills](https://www.skills.sh/rstackjs/agent-skills) via skills.sh - 11.7K combined installs across 24 indexed listings; first seen 2026-11-06 (Nov 6, 2026 evening sweep)
**GitHub:** 98 stars, MIT, last pushed 2026-10-22, 31 SKILL.md directories, 23 under `skills/` and 8 maintainer-workflow skills under `.agents/skills`
**Category:** Rspack ecosystem work for agents: docs writing, release notes, PR creation, CI debugging and repo maintenance passes
**Quality Tier:** 🟡 Review - four of five sampled skills pass all three scanners, but one carries a Snyk warning and one sampled listing returned no verdict at all.

This repository is the Rstack team's own skill collection for its toolchain: Rspack, Rsbuild, Rslib, Rspress, Rsdoctor, Rstest and Rslint. The README describes it as "A collection of Agent Skills for Rstack" and summarises the purpose as "AI-powered skills for debugging, tracing, upgrading, and analyzing Rstack projects".

The set splits into two halves, and the difference matters for installation. The 23 packaging and migration skills under `skills/` are what a user of the ecosystem installs: best practices for each tool, v1 to v2 upgrade paths, Rspress documentation generators, Rsdoctor bundle analysis. The 8 skills under `.agents/skills/` are the maintainers' own workflow: drafting release notes, writing release blog posts, creating pull requests, triaging ecosystem CI, reviewing PRs. Both halves ship in the same plugin.

## Installation

The README recommends installing the repository as an Agent Plugin, which follows the vendor-neutral Agent Plugins 1.0 standard. Its own commands, per harness:

```bash
codex plugin marketplace add rstackjs/agent-skills
codex plugin add rstack@rstack
```

```bash
claude plugin marketplace add rstackjs/agent-skills
claude plugin install rstack@rstack
```

```bash
copilot plugin marketplace add rstackjs/agent-skills
copilot plugin install rstack@rstack
```

Cursor takes a clone into its local plugin directory instead:

```bash
git clone https://github.com/rstackjs/agent-skills.git ~/.cursor/plugins/local/rstack
```

For VS Code the README says to run **Chat: Install Plugin From Source** and enter the repository URL.

Individual skills install with the skills CLI, one command per skill, and the README gives one under each heading. The shape is:

```bash
npx skills add rstackjs/agent-skills --skill rsbuild-best-practices
```

## What It Provides

Seven listings clear the threshold, and they map onto the tools a build engineer touches in order of how often the problem appears:

| Skill | Installs | Use For |
|---|---|---|
| rsbuild-best-practices | 2,819 | Configuring, reviewing or troubleshooting Rsbuild apps: build and dev commands, assets, type checking, bundle optimisation |
| rstest-best-practices | 1,448 | Setting up or reviewing Rstest tests and configuration: environments, mocks, snapshots, coverage and CI |
| rslib-best-practices | 1,064 | Rslib library builds: output formats, declaration files, dependency handling and integrations |
| rspack-best-practices | 685 | Rspack builds: loaders, CSS, assets, type checking, bundle optimisation and profiling |
| rspress-best-practices | 552 | Rspress v2 sites: content conventions, navigation, MDX, assets, search and deployment |
| rspack-v2-upgrade | 526 | Upgrading a Rspack 1.x project to v2, including dependency and configuration changes |
| rspress-description-generator | 510 | Generating missing `description` frontmatter for Rspress Markdown and MDX pages, including site-wide metadata passes |

The remaining 17 indexed listings range from 1 to 490 installs.

The tail is where the migrations live: `migrate-to-rsbuild`, `migrate-to-rstest`, `migrate-to-rslib`, `migrate-to-rslint`, `rsbuild-v2-upgrade`, `rspress-v2-upgrade`, `rsdoctor-v2-upgrade`. There are also narrower craft skills such as `rspack-tracing` and `rspack-debugging` for performance work, `rspack-split-chunks` for bundle shaping, `rsdoctor-analysis` for reading local build data, `rspress-custom-theme`, `storybook-rsbuild` and `rslib-modern-package`. The maintainer half adds `create-draft-release-notes`, `release-blog-writer`, `rstack-docs-writer`, `mdx-to-markdown`, `pr-creator`, `rstack-eco-ci-debug`, `rstack-repo-maintain` and `rstack-skill-evaluator`.

## Why This Matters for Hermes Agents

Build tooling is where an agent's training data goes stale fastest. Rspack 2, Rsbuild 2, Rslib and Rstest all changed configuration surfaces, and an agent answering from memory produces options that were renamed or removed. These skills carry the current option set for each tool, which turns a plausible-looking config into one that runs.

The migration skills are the highest-value part for a Hermes agent doing maintenance work. A v1 to v2 upgrade touches dependencies, config files, plugin APIs and output assumptions in a fixed order, and each migration skill encodes that order with the specific replacements. Left alone, an agent improvises a partial upgrade that builds but silently drops features.

The Rspress pair covers documentation work rather than code. `rspress-docs-generator` creates or maintains a docs site, `rspress-description-generator` fills in missing `description` frontmatter across pages, and `mdx-to-markdown` converts MDX to portable Markdown. For a team that documents in the same repository it ships, these turn a chore into a single request.

The CI skill is the one worth knowing about even if you never install the maintainer half. `rstack-eco-ci-debug` triages ecosystem CI across repositories, follows green-to-red pivots, runs Rspack canary bisects, and attributes a failure to an upstream or downstream change while checking for flaky runs. That is agent-shaped work: repetitive, evidence-driven, and easy to get wrong by guessing.

## Usage

| You say | What happens |
|---|---|
| "Review this Rsbuild config for problems" | The Rsbuild skill checks build and dev settings, asset handling and type checking against current practice, then names the offending options |
| "Upgrade this project from Rspack 1 to 2" | `rspack-v2-upgrade` walks dependencies, config replacements and plugin changes in order, then validates the build |
| "Migrate our tests from Jest to Rstest" | `migrate-to-rstest` moves discovery, assertions, mocks, snapshots and coverage while keeping the suite runnable |
| "Build a docs site for this package" | `rspress-docs-generator` scaffolds or extends an Rspress v2 site with navigation and MDX conventions intact |
| "Our bundle has duplicate packages, analyse it" | `rsdoctor-analysis` reads local Rsdoctor build data and reports chunk, module and package findings with recommendations |
| "Ecosystem CI went red overnight, find the cause" | `rstack-eco-ci-debug` attributes the failure to an upstream or downstream change and checks for flaky runs before blaming a commit |
| "Write the release notes for this version" | `create-draft-release-notes` drafts organised notes, or outputs Markdown when draft creation is unavailable |

## Verification

Read a skill before installing the plugin. This path returned HTTP 200 on the repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/rstackjs/agent-skills/main/skills/rsbuild-best-practices/SKILL.md | head -20
```

It should open with `name: rsbuild-best-practices` and the description about configuring, reviewing or troubleshooting Rsbuild applications, then the rule list that follows.

After install, check that the CLI picked up the set, since a plugin install and a skills CLI install land in different places:

```bash
npx skills list
```

It should list the skills by name, starting with the best-practices entries. If you used the plugin route instead, the harness's own plugin list is the check, for example `claude plugin list` or `codex plugin list`.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| rsbuild-best-practices | Pass | Pass | Pass |
| rspress-description-generator | Pass | Pass | Pass |
| rspress-docs-generator | Pass | Pass | Warn |
| rspress-v2-upgrade | Pass | Pass | Pass |
| rsdoctor-analytics | ? | ? | ? |

The one warning is on `rspress-docs-generator`, which is the skill that writes documentation files into your repository. Read its `SKILL.md` before letting it run unattended on a docs tree you care about, because a generator that writes pages is a file-writing permission by another name.

The `?` row is worse than a warning in one respect: it means no verdict was returned, so there is nothing to check. Treat `rsdoctor-analytics` as unreviewed rather than cleared.

The maintainer half deserves separate thought. `pr-creator` opens pull requests using repository branch rules and templates, `create-draft-release-notes` writes GitHub releases, and `rstack-eco-ci-debug` reads CI state across repositories. All three need GitHub credentials with write access, so install that half only where a token already exists for the purpose, and not on a machine where a broad personal token is ambient.

## Limitations

- Snapshot data, verified 2026-11-06: 11,707 combined installs across 24 indexed listings; 98 GitHub stars; MIT; last pushed 2026-10-22. Counts drift over time.
- The tier is Yellow. One sampled skill carries a Snyk warning and one returned no verdict from any of the three scanners, so the security picture is incomplete rather than clean.
- Usage is top-heavy. The two best-practices entries account for over a third of the combined installs, and 17 of 24 listings sit under 500, including every migration skill except `rspack-v2-upgrade`.
- The content is version-pinned by nature. Rspack 2 and Rsbuild 2 guidance is correct for those majors and wrong for 1.x projects, which is why the upgrade skills exist as separate entries.
- Half the repository is maintainer tooling. `pr-creator`, `rstack-repo-maintain` and the release skills assume the Rstack monorepo conventions and a pnpm workspace, so they add noise in an unrelated project.
- Small project, 98 stars. The skills are maintained by the ecosystem team rather than exercised by a wide user base, so an error would surface slowly.

## Related

- [Frontend God Mode - Design Skills Bundle Setup](/hermes/skills/catalog/frontend-god-mode-setup)
- [Next.js Agent Skills - Official Vercel Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)
- [CLI-Anything GUI Harnesses - Setup Guide](/hermes/skills/catalog/cli-anything-harnesses-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install single skills with `--skill` rather than the plugin when you only need one. The migration skills are self-contained, and the plugin drags the maintainer tooling along.
- Name the major version in the request. "Upgrade to Rspack 2" routes to `rspack-v2-upgrade`, while "fix my Rspack config" routes to best practices and may leave the version unexamined.
- Run the migration skill before the best-practices skill after a major bump. The config surface changes first, and the best-practices advice assumes the new one.
- Point `rsdoctor-analysis` at real build output. It reads local Rsdoctor data, so a run without that data produces generic advice.
- Keep `pr-creator` and the release skills on a machine with scoped credentials. They are the only part of the set that writes to GitHub on your behalf.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
