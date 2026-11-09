---
title: "EmDash CMS Skills - Astro CMS Agent Suite"
description: "emdash-cms/skills on skills.sh: 6.8K combined installs across 6 listings; Astro-native EmDash CMS build, plugin and migration skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/emdash-cms-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-09"
tags: ["hermes skill", "agent skill", "skill setup", "emdash", "astro", "cms", "wordpress migration"]
---

# EmDash CMS Skills - Setup Guide

**Source:** [emdash-cms/skills](https://www.skills.sh/emdash-cms/skills) via skills.sh - 6.8K combined installs across 6 indexed listings; snapshot 2026-11-09 (Nov 9, 2026 sweep)
**GitHub:** 13 stars, MIT via the README License section, `main` branch, last pushed 2026-10-29, 34 files with 6 `SKILL.md` files under `skills/<name>/`, one directory per skill
**Category:** CMS and content: EmDash on Astro, schema and seeds, plugin authoring, CLI operations, upgrades and WordPress migrations
**Quality Tier:** 🟡 Yellow - MIT and all six listings indexed, but three of the six carry a Warn on one scanner, and the repository has 13 stars behind 6,804 installs.

EmDash is an Astro-native CMS: content and schema live in the database, the site reads it through live content collections, and the admin UI ships at `/_emdash/admin`. These six skills are the publisher's own instructions for building on it, written for coding agents rather than humans, and split by task: site work, plugin authoring, CLI operations, upgrades, and two porting paths from WordPress.

The repository is generated. Its README states that the skills live in the `skills/` directory of the EmDash monorepo at `emdash-cms/emdash` and sync here with each EmDash release, replacing anything edited directly. That is the most important operational fact about this install: you get a mirror, and the place to file an issue or a patch is the monorepo, not this repository.

The install profile is the other notable thing. All six listings sit between 1,083 and 1,188 installs, a spread of about a hundred, which is what a suite looks like when it is adopted as a set rather than skill by skill.

## Installation

The skills CLI covers every major agent from one command:

```bash
npx skills add emdash-cms/skills
```

Pass `--skill <name>` to install one skill, or `-g` to install for the user rather than the current project. With the GitHub CLI:

```bash
gh skill install emdash-cms/skills --all
```

Claude Code installs the repository as a plugin from its marketplace:

```text
/plugin marketplace add emdash-cms/skills
/plugin install emdash@emdash
```

Skills then appear namespaced, as `emdash:building-emdash-site` and so on. Third-party marketplaces do not auto-update by default, so run `/plugin marketplace update emdash` after a release or enable auto-update in `/plugin`.

Codex takes the marketplace route as well:

```bash
codex plugin marketplace add emdash-cms/skills
```

Then install the `emdash` plugin from the Plugins directory. GitHub Copilot CLI has a direct command:

```bash
copilot plugin install emdash-cms/skills
```

In VS Code, run `Chat: Install Plugin From Source` and enter `https://github.com/emdash-cms/skills`. In Cursor, open Customize, then Plugins, then From GitHub Repository, and enter the same URL. Factory Droid uses two commands:

```bash
droid plugin marketplace add emdash-cms/skills
droid plugin install emdash@emdash
```

For a manual install, copy the directories under `skills/` into your agent's skills directory. The README notes that `.agents/skills/` in a project works for most agents.

## What It Provides

The threshold for this guide is zero installs, so all six indexed listings appear below:

| Skill | Installs | Use For |
|---|---|---|
| building-emdash-site | 1,188 | Site-facing EmDash work on Astro: schema and seeds, content queries, Portable Text rendering, menus, taxonomies, widgets and deployment configuration |
| emdash-cli | 1,172 | Managing an EmDash instance from the command line: content, schema, media, taxonomies, menus, search, authentication, seeds, migrations, generated types, site export and import |
| creating-plugins | 1,158 | Authoring EmDash plugins with sandboxed hooks, routes, storage, content and media APIs, MCP tools and declarative admin UI, or native React and Astro extensions |
| wordpress-theme-to-emdash | 1,105 | Porting a WordPress theme's design and template behavior to an EmDash site: design matching, PHP template conversion and CMS wiring |
| wordpress-plugin-to-emdash | 1,098 | Porting WordPress plugin behavior, custom post types, shortcodes, admin workflows and stored data to EmDash extension points |
| upgrading-emdash | 1,083 | Upgrading an existing EmDash project with upgrade-emdash: reading `.emdash/UPGRADE.md`, applying required project changes and verifying the result |

All 6 indexed listings clear the zero-install threshold; none fall below it.

The suite is close to flat on installs, so the differentiator is the file, not the number. `building-emdash-site` is the entry point at 151 lines, and it is the skill the porting pair defers to for anything site-shaped. `emdash-cli` is the longest at 267 lines because it covers a broad command surface: content, schema, media, taxonomies, menus, search, auth, seeds, migrations, generated types, and whole-site export and import.

`upgrading-emdash` is the shortest at 33 lines, and that is deliberate. It does not restate an upgrade procedure; it tells the agent to run `upgrade-emdash`, read `.emdash/UPGRADE.md` for the release, apply the project changes that file names, and then verify the package, the skill and the migration result.

The two WordPress skills are scoped against each other and against the rest of the suite. The theme skill is for design and template behavior, the plugin skill is for behavior, custom post types, shortcodes and stored data, and both say what they are not for. The README adds the dependency in one line: the porting skills link to `building-emdash-site` and `creating-plugins`, so install those alongside them.

## Why This Matters for Hermes Agents

WordPress to Astro is a migration an agent is often asked to do badly: copy the templates, keep the PHP mental model, and hand back a site that looks right and stores content wrong. These skills exist to prevent that, and they do it by naming where behavior belongs in EmDash rather than by producing boilerplate.

The split into theme and plugin is the useful part. A migration task almost always mixes both, and the two skills force the agent to decide per feature whether it is design, plugin behavior, schema, seed data or Astro code before it writes anything. That decision is the work, and it is the step a model skips when given one generic migration instruction.

The CLI skill covers the operational half, which is where a Hermes agent adds value beyond code generation: reading schema, moving media, running seeds, checking search configuration, exporting a site before a risky change. Import and export in particular make a migration reversible in a way that editing files is not.

The plugin skill is the one that requires the most caution. It authorises the agent to write sandboxed hooks, routes, storage access, admin UI and MCP tools, which is application code with a security surface, and the publisher provides the extension points rather than the review.

The honest counterweight: EmDash is young, the repository is small at 13 stars, and the skills track releases of a product whose API is still moving. Treat the guidance as current for the version you run, not as durable knowledge.

## Usage

| You say | What happens |
|---|---|
| "Build the marketing site on EmDash" | Uses building-emdash-site: defines schema and seeds, writes content queries, renders Portable Text, wires menus, taxonomies and widgets, and sets deployment configuration |
| "Port this WordPress theme to EmDash" | Runs wordpress-theme-to-emdash: maps the design and template behavior onto an Astro site, converts the PHP templates, and hands content and plugin behavior to the other two skills |
| "This plugin's shortcode needs to keep working" | Applies wordpress-plugin-to-emdash to decide where the behavior belongs: an EmDash plugin, site schema, a seed, or Astro code |
| "Write a plugin that adds a reviews field and an admin screen" | Uses creating-plugins: sandboxed hooks, routes and storage, a declarative admin UI, and an MCP tool if the field should be agent-readable |
| "Export the site before I change the schema" | Follows emdash-cli: whole-site export, then the schema change, with generated types refreshed afterwards |
| "Upgrade this project to the current EmDash release" | Runs upgrading-emdash: `upgrade-emdash`, read `.emdash/UPGRADE.md`, apply the named project changes, verify package, skill and migration |
| "Why does this page show stale content" | Checks the content query path in building-emdash-site and the seed and schema state through the CLI before touching templates |

## Verification

Read the site skill before installing, because the rest of the suite defers to it:

```bash
curl -fsSL https://raw.githubusercontent.com/emdash-cms/skills/main/skills/building-emdash-site/SKILL.md | head -8
```

The frontmatter holds `name: building-emdash-site` and the same description the index shows, ending with the boundary that plugin authoring belongs to `creating-plugins`. The body opens with a paragraph stating that EmDash stores schema in the database rather than in code, serves content through live content collections, and exposes the admin UI at `/_emdash/admin`, then moves into a gotchas section.

Confirm the file count and the layout in one call, since the paths here are `skills/<name>/SKILL.md` and not the `.agents/skills/` layout some publishers use:

```bash
curl -fsSL https://raw.githubusercontent.com/emdash-cms/skills/main/skills/emdash-cli/SKILL.md | wc -l
```

That returns 267. A 404 on either path means the mirror layout changed and the `--skill` names in this guide no longer resolve.

After an install, check the directory the client indexes:

```bash
test -f ~/.claude/skills/building-emdash-site/SKILL.md && echo ok
```

Through the Claude Code plugin route the name is namespaced instead, so confirm with `/plugin` that `emdash` is listed and enabled rather than looking for the directory.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-09) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| building-emdash-site | Pass | Pass | Pass |
| emdash-cli | Pass | Pass | Warn |
| creating-plugins | Pass | Pass | Pass |
| wordpress-theme-to-emdash | Pass | Pass | Warn |
| wordpress-plugin-to-emdash | Pass | Pass | Pass |
| upgrading-emdash | Pass | Warn | Pass |

All six are Markdown instruction files, so the verdicts describe instruction sets rather than an executable payload. The three Warns sit on `emdash-cli` (Snyk), `wordpress-theme-to-emdash` (Snyk) and `upgrading-emdash` (Socket), and those are also the three most write-capable skills in the suite: one drives a CLI against a live instance, one rewrites a theme's templates, one runs an upgrade that changes project files and migrations. That correlation is a reason to read them, not proof of a defect.

The blast radius is the CMS, not the laptop. The CLI skill covers content, schema, media, taxonomies, menus, search, authentication, seeds, migrations and whole-site import and export, which means one wrong command against a production instance can delete or overwrite content, and an import can replace a site wholesale. Point the agent at a development instance or a branch site, take an export first, and keep production credentials out of the project directory the agent reads.

The generated-repository arrangement is a supply chain fact worth knowing. Content in this repository is replaced on every EmDash release, so a pinned commit buys you reproducibility but not a review trail, since the publisher's review happens in the monorepo. If you need auditable provenance, track `emdash-cms/emdash` and diff the `skills/` directory between releases.

Plugin authoring is the last surface. The creating-plugins skill authorises sandboxed hooks, routes, storage and media API use, MCP tools and native React or Astro extensions, all of which run inside your site. Review what an agent writes there the way you would review any extension: what it can read, what it can write, and whether the MCP tool it exposes should be reachable by an agent at all.

## Limitations

- Snapshot data, verified 2026-11-09: 6,804 combined installs across 6 indexed listings; 13 GitHub stars; MIT license; last pushed 2026-10-29. Counts drift over time.
- The repository is generated from `emdash-cms/emdash` and replaced with each EmDash release, so direct edits here do not survive. Issues and pull requests belong in the monorepo.
- The README table documents five of the six skills. `upgrading-emdash` is indexed and present in the tree but absent from that table, so its purpose here is taken from its own `SKILL.md`, not the README.
- 6,804 installs against 13 GitHub stars means adoption runs through the skills CLI and the plugin marketplaces rather than through GitHub discovery. The install count is a distribution signal, not an evaluation of the guidance.
- The two WordPress porting skills depend on the other two. The README says to install `building-emdash-site` and `creating-plugins` alongside them, so a porting-only install leaves the agent with migration rules and no target-side reference.
- Distribution is uneven per agent: the skills CLI, the Claude Code marketplace, the Codex and Droid marketplaces and Copilot each track releases separately, and the Claude Code marketplace does not auto-update by default. Two agents in the same project can hold different skill versions.

## Related

- [WordPress Agent Skills - Official WP Development Setup](/hermes/skills/catalog/wordpress-agent-skills-setup)
- [Sanity Agent Toolkit - Headless CMS Setup](/hermes/skills/catalog/sanity-agent-toolkit-setup)
- [Payload CMS Skills - Schema and Migration Setup](/hermes/skills/catalog/payloadcms-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `building-emdash-site` and `creating-plugins` even if your task is a WordPress port. Both porting skills route to them for anything site-shaped or plugin-shaped, and without them the agent improvises Astro code.
- Take a whole-site export through `emdash-cli` before an upgrade or a schema change. The CLI skill covers import as well, which is what makes the export worth having.
- Read `.emdash/UPGRADE.md` before letting an agent touch an upgrade. `upgrading-emdash` is 33 lines precisely because the release-specific instructions live in that file, not in the skill.
- Decide where behavior belongs before writing anything in a migration. The theme skill is for design and templates, the plugin skill is for behavior and stored data, and mixing them is how a port ends up with logic in templates.
- Pin the EmDash version you are building against. The skills move with releases of a young product, and a skill that matches today's API will not match the next minor.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
