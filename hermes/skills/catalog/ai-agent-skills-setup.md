---
title: "AI Agent Skills - Skill Package Manager and Library"
description: "moizibnyousaf/ai-agent-skills on skills.sh: 8.0K combined installs across 20 listings; a universal skill installer and library manager for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ai-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-09"
tags: ["hermes skill", "agent skill", "skill setup", "package manager", "skill library", "cli", "workspace"]
---

# AI Agent Skills - Setup Guide

**Source:** [moizibnyousaf/ai-agent-skills](https://www.skills.sh/moizibnyousaf/ai-agent-skills) via skills.sh - 8,012 installs across 20 indexed listings (8.0K combined); first seen 2026-11-09 (Nov 9, 2026 sweep)
**GitHub:** 1,156 stars, MIT via LICENSE, `main` branch, last pushed 2026-09-21, 94 files in the tree with 19 SKILL.md files in a `skills/<name>/SKILL.md` layout
**Category:** Skill packaging and library management: a universal installer, CLI and TUI for building a curated skills library across 12 or more agent runtimes
**Quality Tier:** 🟡 Watch - MIT license and Pass on the Trust Hub and Socket columns for all 20 sampled skills, but three listings carry a Snyk Warn and the install index outruns the current tree by eight listings.

The package is not a set of domain skills. It is an installer and a package manager for skills, with a curated library bundled on top: `npx ai-agent-skills` opens a terminal browser, `install` writes a skill into an agent's skills directory, and `init-library` creates a managed workspace with shelves, provenance metadata and generated docs. The 20 indexed listings on skills.sh are library entries that the manager installs, not a suite you receive by adding the repository.

The repository predates the current installer default. The README says it launched on December 17, 2025, "before `skills.sh` existed and before the ecosystem had a clear default universal installer", and that the project has since become a place to build and manage your own library. That history explains the shape: two kinds of entry, house copies that live as folders under `skills/<name>/` and ship inside the npm package, and cataloged upstream picks that exist only as metadata in `skills.json` and are fetched from their source repository at install time.

The drift between the index and the tree is the first thing to know. Twenty listings are indexed, and only 12 of them have a `SKILL.md` in the current tree. The eight without one are code-review, code-refactoring, expo-app-design, python-development, canvas-design, job-application, javascript-typescript and xlsx, which is also why every "(none found)" description in the upstream scans belongs to that group.

## Installation

The skills.sh route installs a single listing through the generic skills CLI:

```bash
npx skills add https://github.com/moizibnyousaf/ai-agent-skills --skill code-review
```

The README route installs the manager itself, which is the part that gives you shelves, sync and a library:

```bash
# Open the terminal browser
npx ai-agent-skills

# List the shelves
npx ai-agent-skills list

# Install a skill from the library
npx ai-agent-skills install frontend-design

# Install to the project shelf instead of the global one
npx ai-agent-skills install pdf -p

# Browse a repository before installing from it
npx ai-agent-skills install openai/skills --list
```

Default targets are global `~/.claude/skills/` and project `.agents/skills/`. Legacy agent-specific targets still work through `--agent <name>`.

To create a library rather than install one skill:

```bash
npx ai-agent-skills init-library my-library
cd my-library
npx ai-agent-skills add frontend-design --area frontend --branch Implementation --why "I want this on my shelf."
npx ai-agent-skills install frontend-design -p
npx ai-agent-skills sync frontend-design -p
npx ai-agent-skills build-docs
```

An existing flat repository of skills can be bootstrapped in place with `npx ai-agent-skills init-library . --areas "mobile,workflow,agent-engineering" --import --auto-classify`. The README warns that invalid private-only names are skipped and reported, and that low-confidence imports fall back to the `workflow` shelf with a needs-curation label.

## What It Provides

The threshold for this guide is zero installs, so all 20 indexed listings appear below with their exact counts:

| Skill | Installs | Use For |
|---|---|---|
| code-review | 961 | Reviewing code changes; name-level scope only, because this listing has no SKILL.md in the current tree |
| backend-development | 874 | Backend API design, database architecture, microservices patterns and test-driven development |
| database-design | 615 | Schema design, optimization and migration patterns for PostgreSQL, MySQL and NoSQL |
| code-refactoring | 585 | Restructuring existing code; name-level scope only, because this listing has no SKILL.md in the current tree |
| code-documentation | 569 | API docs, README files, inline comments and technical developer guides |
| best-practices | 531 | Rewriting a vague prompt into a phased Claude Code prompt with verification, context and constraints |
| llm-application-dev | 466 | Prompt engineering, RAG patterns and LLM integration for AI features, chatbots and automation |
| content-research-writer | 412 | Research-backed writing with citations, iterated outlines and per-section feedback |
| changelog-generator | 397 | Turning git commit history into user-facing release notes grouped by change type |
| ask-questions-if-underspecified | 380 | Clarifying requirements before implementation; its own description restricts it to explicit invocation |
| expo-app-design | 360 | Designing Expo applications; name-level scope only, because this listing has no SKILL.md in the current tree |
| python-development | 318 | Python application work; name-level scope only, because this listing has no SKILL.md in the current tree |
| canvas-design | 230 | Canvas-based visual design; name-level scope only, because this listing has no SKILL.md in the current tree |
| job-application | 222 | Job application drafting; name-level scope only, because this listing has no SKILL.md in the current tree |
| javascript-typescript | 216 | JavaScript and TypeScript work; name-level scope only, because this listing has no SKILL.md in the current tree |
| xlsx | 180 | Spreadsheet work; name-level scope only, because this listing has no SKILL.md in the current tree |
| review-a-skill | 177 | Previewing a candidate skill, checking frontmatter and structure, then keeping, curating or removing it |
| browse-and-evaluate | 177 | Comparing catalog entries before installing, with `--fields` to bound output and `--dry-run` first |
| build-workspace-docs | 172 | Regenerating README.md and WORK_AREAS.md in a managed workspace, dry run before the write |
| audit-library-health | 170 | Running doctor, validate, stale-skill and docs-in-sync checks across a library |

Threshold zero means no listing falls below it, so the table is the whole index. The counts are small and evenly spread, which fits a repository whose value is the manager rather than any single skill: the top row is 961 installs and the bottom is 170, a spread of less than six times.

The library splits its entries two ways. House copies are local folders under `skills/<name>/` that ship with the npm package, which the README says makes them install fast and work offline. Cataloged upstream picks are metadata rows in `skills.json` with no local folder, so they stay upstream and install from the source repository on request. The README's own numbers for the library size disagree with each other: the badge row reads "141 skills, 6 shelves" with "18 house copies, 123 cataloged upstream", while the 4.3.1 release note reads "115 cataloged skills (17 house copies, 98 cataloged upstream)".

Nine companion workflow skills ship with the library and are installed automatically when it is used: install-from-remote-library, curate-a-team-library, share-a-library, browse-and-evaluate, update-installed-skills, build-workspace-docs, review-a-skill, audit-library-health and migrate-skills-between-libraries. They are the operational half of the package, and every one of them is a command protocol rather than a body of knowledge about a language.

## Why This Matters for Hermes Agents

Hermes already keeps a skills directory per profile, and the recurring failure is not a missing skill but an unmanaged one: a directory of folders with no record of where each came from, which version it is, or why it is there. This package answers that with `skills.json`, a shelf taxonomy, a `--why` note per entry and generated workspace docs.

The second fit is provenance. A cataloged upstream entry keeps its source repository in metadata and installs from there, so an agent can report where a skill came from instead of inferring it from a folder name. For a team that runs several agents against the same library, that is the difference between a shared shelf and four divergent copies.

The third is that the workflow is command-shaped. `list --area`, `search`, `collections`, `add --area --branch --why`, `sync`, `build-docs` are all steps a script or an agent can run in order, and the README ships a paste-in protocol in `FOR_YOUR_AGENT.md` that tells an agent to ask at most three questions, map the stack to shelves and add three to eight skills with explicit metadata.

The honest counterweight: this is another package manager in a space that already has one. The README says so directly, "Use `skills.sh` for the broad ecosystem. Use `ai-agent-skills` when you want a smaller library with shelves, provenance, and notes." If the requirement is one skill installed once, the two-line `npx skills add` is less machinery. The manager earns its place when the library has to stay curated over time.

## Usage

| You say | What happens |
|---|---|
| "Install the backend development skill for this project" | Runs `npx ai-agent-skills install backend-development -p`, which writes into `.agents/skills/` rather than the global target |
| "What is on the workflow shelf" | Runs `npx ai-agent-skills list --area workflow` and reads back the shelf rather than the full catalog |
| "Where did this skill come from" | Runs `npx ai-agent-skills info <name>` for the provenance view: publisher, source repository, shelf and branch |
| "Start a shared skills library for the team" | Runs `init-library <name>`, asks at most three questions, maps the stack to shelves, adds three to eight skills with `--area`, `--branch` and `--why`, then builds docs |
| "Refresh the skills we already installed" | Runs `sync <name> -p` per entry, or `update-installed-skills` from the companion set for the whole set |
| "Is this library healthy" | Runs doctor and validate through the `audit-library-health` skill, plus the stale-skill and docs-in-sync checks |
| "Show me a skill before I install it" | Runs `install <owner>/<repo> --list`, or the `review-a-skill` skill, which previews content and frontmatter first |

## Verification

Two raw fetches cover the two kinds of entry. A house copy is on disk in the repository:

```bash
curl -fsSL https://raw.githubusercontent.com/moizibnyousaf/ai-agent-skills/main/skills/backend-development/SKILL.md | head -8
```

This returns 200 and opens with YAML frontmatter whose `description` matches the row in the table above. The operational half of the library is the same shape:

```bash
curl -fsSL https://raw.githubusercontent.com/moizibnyousaf/ai-agent-skills/main/skills/audit-library-health/SKILL.md | head -8
```

That also returns 200, and its body names the commands the skill runs: doctor, validate, stale-skill checks and a docs-in-sync comparison.

The drift check is the third fetch, and a 404 is the expected result:

```bash
curl -s -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/moizibnyousaf/ai-agent-skills/main/skills/code-review/SKILL.md
```

On 2026-11-09 this printed `404`. If it starts printing `200`, the listing has acquired a tree counterpart and the drift note in Limitations is stale.

After an install, confirm the file landed where the client reads it rather than one directory above:

```bash
test -f .agents/skills/backend-development/SKILL.md && echo ok
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-09) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| backend-development | Pass | Pass | Pass |
| database-design | Pass | Pass | Pass |
| code-documentation | Pass | Pass | Pass |
| best-practices | Pass | Pass | Pass |
| job-application | Pass | Pass | Warn |
| review-a-skill | Pass | Pass | Warn |
| browse-and-evaluate | Pass | Pass | Warn |
| audit-library-health | Pass | Pass | Pass |

Seventeen of the 20 listings are Pass on all three scanners. The three Snyk Warns fall on job-application, review-a-skill and browse-and-evaluate, and they are content-level warnings about prompt text rather than reports of malicious code. Read those three bodies before deploying them in a pipeline that handles resumes or that decides what enters a shared library.

The verdicts do not cover the part that executes. The skills are Markdown, but `ai-agent-skills` is an npm package that writes into agent skill directories, shells out to git and npm for upstream sources, and pulls content chosen by `skills.json` metadata at install time. Nothing in the README describes signature verification or a pinned digest for cataloged upstream entries, so an install is a trust decision about the upstream repository at the moment it runs.

That matters more here because of the index and tree drift. Eight indexed listings have no `SKILL.md` in the repository, so an install of one of those resolves to something the tree does not show you. Confirm the source before installing a drifted listing, and prefer a house copy for anything that will run unattended.

Operationally, two habits are worth keeping. Do not run `init-library` inside a project directory that ships, because the workspace writes `README.md`, `WORK_AREAS.md` and `skills.json` into the tree. And keep the global target on a path you audit, since the default `~/.claude/skills/` is shared with every other Claude Code session on the machine.

## Limitations

- Snapshot data, verified 2026-11-09: 8,012 combined installs across 20 indexed listings; 1,156 GitHub stars; MIT license; last pushed 2026-09-21. Counts drift over time.
- The install index outruns the tree: 20 listings are indexed and only 12 have a `SKILL.md` in the current tree. The eight without one are code-review (961), code-refactoring (585), expo-app-design (360), python-development (318), canvas-design (230), job-application (222), javascript-typescript (216) and xlsx (180). A raw fetch of `skills/code-review/SKILL.md` returned 404 on 2026-11-09.
- Exactly 20 listings are visible, which is the skills.sh source page cap rather than a measured ceiling. A repository with more listings would still show 20.
- The README contradicts itself on library size: the badge row says 141 skills across 6 shelves with 18 house copies and 123 cataloged upstream, while the 4.3.1 release note says 115 cataloged skills with 17 house copies and 98 cataloged upstream. Treat either number as approximate.
- Cataloged upstream entries carry no local copy, so their content is whatever the source repository holds at install time. The README documents `sync` for refreshing installed skills but no way to pin an upstream entry to a commit.
- The default targets are Claude Code paths (`~/.claude/skills/`) and a project `.agents/skills/`. Hermes reads its own profile skills directory, so a Hermes install needs `--agent` or a copy step, and the README's per-agent target list is not enumerated.

## Related

- [skill-creator - Anthropic's Skill Creation Framework Setup](/hermes/skills/catalog/skill-creator-setup)
- [Agent Skill Creator - Skill Generation and Templating Setup](/hermes/skills/catalog/agent-skill-creator-setup)
- [somasays Skill Creator - Claude Skills Setup](/hermes/skills/catalog/somasays-skill-creator-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Learn the two views before the flags. `list` is the shelf view and `info` is the provenance view, and almost every curation mistake starts with browsing the catalog when the question was about one entry's source.
- Use `--dry-run` and `--fields` on every browse that feeds a decision. The `browse-and-evaluate` skill says so explicitly, and it keeps a catalog sweep from flooding the context window.
- Give every `add` a `--why`. The note is the only record of intent in the library, and it is what makes a shelf review possible six months later.
- Check the tree before installing a drifted listing. Eight of the 20 indexed names have no `SKILL.md` in the repository, so the install target for those is upstream, not the copy you can read.
- Run `build-docs` after the last mutation, not before. The generated `README.md` and `WORK_AREAS.md` reflect the library at the moment of the command, and an agent that skips it leaves the docs describing an older shelf.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
