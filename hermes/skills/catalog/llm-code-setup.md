---
title: "LLM Code Skills - Cross-Tool Documentation Pack"
description: "itechmeat/llm-code: 6.0K combined installs. Versioned documentation skills for Vite, FastAPI, Bun, Mantine, Vitest and other stacks, for any coding agent."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/llm-code-setup/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skill setup", "documentation", "developer tools", "framework reference"]
---

# LLM Code - Setup Guide

**Source:** [itechmeat/llm-code](https://www.skills.sh/itechmeat/llm-code) via skills.sh - 6.0K combined installs across 49 indexed listings; first seen 2026-11-01 (evening sweep)

**GitHub:** [itechmeat/llm-code](https://github.com/itechmeat/llm-code) - 24 stars, MIT, branch master, last pushed 2026-10-24; 38 `SKILL.md` directories under `skills/`, one per skill, each with a `references/` set beside it

**Category:** Documentation-based skills for any coding agent: framework references for Vite, FastAPI, Bun, Mantine and more

**Quality Tier:** 🟡 Yellow - docs-only pack with an MIT LICENSE in the repo root, 24 stars, 38 skill directories; Gen Agent Trust Hub and Socket pass on all five sampled listings, three of which carry a Snyk warning

LLM Code is an independently maintained collection from itechmeat that packages library and tool documentation as agent skills rather than as prompts or MCP servers. It targets Copilot, Claude, Cursor and every other assistant that reads the agentskills.io layout, so one folder works across tools. Each skill holds a `SKILL.md` plus reference files for a single stack, and the frontmatter carries a version and a release date per skill, which makes staleness visible instead of silent.

The spread is wider than frontend docs. Alongside Vite 8.3.5, Mantine 9.7.3, Vitest 5.0.5 and React Testing Library 16.3.3 sit process skills (Conventional Commits, Keep a Changelog, OpenSpec artifacts, a GNU Make guide), infrastructure references (Kubernetes Cluster API, Qdrant, pgvector, SeaweedFS, Turso, and nine Cloudflare services in the index), and API notes for Open-Meteo, Tavily, Perplexity, Telegram and Inworld. One skill, `skill-master`, is about writing skills: folder structure, reference and script layout, trigger evaluations and blind A/B comparisons against the agentskills.io specification, and the README points contributors at it.

The counts in the repo and in the index do not agree. skills.sh indexes 49 listings, the README heading says 46 above a table of 38, and the clone holds 38 `SKILL.md` directories. Eleven indexed names, the nine `cloudflare-*` entries plus `agent-browser` and `livekit-agents`, have no directory on branch master, so read the table below as a description of what is indexed rather than of what installs by path.

## Installation

With no arguments the CLI installs every skill in the repository into the current project, choosing directories for the AI coding agent it detects:

```bash
npx add-skill itechmeat/llm-code
```

The README lists four narrower forms: list the catalogue, install named skills, target specific agents, and run non-interactively for CI:

```bash
npx add-skill itechmeat/llm-code --list
npx add-skill itechmeat/llm-code --skill vite --skill fastapi
npx add-skill itechmeat/llm-code -a claude-code -a github-copilot
npx add-skill itechmeat/llm-code -y
```

Hermes is not one of the agents that CLI targets, so copy the directories you want instead. Each skill is self-contained, which makes a two-skill install normal:

```bash
git clone https://github.com/itechmeat/llm-code.git
cp -R llm-code/skills/vite llm-code/skills/react-testing-library \
  ~/.hermes/profiles/corpusiq/skills/
```

The clone root holds no `package.json`, so nothing in the repository executes at install time. The only code that runs is the `add-skill` CLI that `npx` fetches.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| react-testing-library | 1,385 | Writing React component tests the user-centric way: queries by role, label and text, `user-event` simulation, async utilities and an accessibility-first API instead of implementation detail. |
| openspec | 844 | Working in the OpenSpec artifact-driven workflow (OPSX): artifact graphs, dependency order for planning a change, schema and template resolution, and the change lifecycle. |
| mantine-dev | 287 | Building React interfaces with Mantine: 100+ components and hooks, forms, theming, dark mode and CSS modules, including the v9.7 additions such as Tour, Toolbar, Toggle and JsonViewer. |
| social-writer | 266 | Drafting posts and threads for X, LinkedIn, Threads, Instagram and Facebook with a hooks catalogue and explicit AI-writing avoidance patterns. |
| base-ui | 232 | Assembling unstyled React components from `@base-ui/react`: multi-part composition with the `render` prop, forms, menus and overlays, with accessibility from the library and styling from you. |
| refine-dev | 207 | Building admin panels and internal CRUD tools on Refine: data providers for REST, GraphQL, Supabase and Strapi, plus resources, routing, authentication and access control. |
| vitest | 200 | Writing and configuring Vitest tests: the Jest-compatible API, mocking, snapshots, coverage, browser mode and TypeScript setup. |
| changelog | 190 | Maintaining `CHANGELOG.md` in Keep a Changelog 1.1.0 format: structure, change types and semver conventions, with a mandatory English-language rule. |
| commits | 176 | Writing Conventional Commits messages: header structure, the type vocabulary, `BREAKING CHANGE` markers and the link to automated changelog generation. |
| makefile | 175 | Writing and maintaining GNU Make targets, recipes and build automation, including the variable and include patterns that keep a Makefile readable. |
| skill-master | 159 | Authoring skills themselves: `SKILL.md` design, folder layout for references and scripts, trigger evaluations, quality benchmarks and blind A/B comparisons against the agentskills.io spec. |
| openapi | 123 | Writing, reading and validating OpenAPI 3.x documents: paths, operations, schemas, parameters and security schemes, with the current spec version noted as 3.2.0. |
| project-creator | 111 | Scaffolding a `.project/` folder: about, specs, architecture, project context and user stories, with templates in `assets/` and guides in `references/`. |
| vite | 109 | Setting up and running Vite: dev server, HMR, build configuration, plugin authoring, environment variables and modes, plus the Environment API and Rolldown. |

The remaining 35 indexed listings range from 1 to 97 installs.

## Why This Matters for Hermes Agents

An agent asked about Vite 8 or Mantine 9 answers from whatever it last absorbed during training, and the answer is confidently wrong at the edges: a renamed option, a removed component, a config key that moved. This pack attacks that by shipping the documentation as files inside the skill, so the agent reads a reference tree captured at a stated version instead of recalling one. Each `SKILL.md` carries a frontmatter version and release date, so you can tell before reading whether the skill is current for your project.

The trigger surface is narrow and explicit. Every description names its package and the situations it applies to, sometimes down to the API terms, which matters where several skills cover neighbouring ground: `base-ui` and `mantine-dev` are both React component libraries, `vitest` and `react-testing-library` are both testing tools, and `commits` and `changelog` both sit in the release flow. An agent asked to write a changelog should land on `changelog`, and the descriptions are written to make that separation hold.

Three of the higher-install skills are process rather than library: `commits`, `changelog` and `openspec`. They need no external service, and they change behaviour on ordinary repository work, which makes them the cheapest first installs. `skill-master` is the reason the pack is worth reading at all: it is the authoring guide for the format every other directory is written in, covering folder structure, trigger evals and benchmarking, so it doubles as documentation for the pack itself.

Everything here is static text. No MCP server, no API key, and no network call from the skills themselves; the only runtime dependency is the assistant reading the markdown. That is the trade as well. The pack cannot fetch a newer framework, so the version in the frontmatter is the version you get until you reinstall.

## Usage

| You say | What happens |
|---|---|
| "Write component tests for the settings form" | react-testing-library drives queries by role and label, `user-event` for interaction and the async helpers for loading states, instead of reaching for test ids. |
| "Why is our Vite build slow and what changed in v8" | vite walks the config, plugin and build references, including the Environment API and Rolldown notes, and answers against 8.3.5 rather than an older major. |
| "Turn these commits into a changelog entry" | commits checks the messages against the Conventional Commits structure, then changelog formats the entry under the Keep a Changelog headings. |
| "Plan the artifact graph for this change before we write code" | openspec lays out the artifact dependencies and schema resolution for OPSX, so the plan names the artifacts and their order instead of jumping to files. |
| "Scaffold the project docs for this service" | project-creator writes about, specs, architecture, project context and user stories into `.project/`, using its own templates and reference guides. |
| "Add a component library to this React app" | mantine-dev or base-ui is chosen by description: Mantine for a styled component set and theming, Base UI for unstyled parts that keep your own styling. |
| "Document this endpoint in OpenAPI" | openapi drafts the path, operation, request and response schemas and the security scheme against OpenAPI 3.x structure. |

## Verification

Probe the paths before installing, on branch `master`. The four below returned 200 when this guide was written, and every row in the table above resolves at `skills/<name>/SKILL.md` on the same branch:

```bash
for p in skills/react-testing-library/SKILL.md skills/skill-master/SKILL.md \
         skills/vite/SKILL.md skills/openspec/SKILL.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/itechmeat/llm-code/master/$p"
done
```

The two to read first are `skill-master`, because it defines the format everything else follows, and `react-testing-library`, the most installed skill and a fair sample of how much reference depth a directory carries:

- https://raw.githubusercontent.com/itechmeat/llm-code/master/skills/skill-master/SKILL.md
- https://raw.githubusercontent.com/itechmeat/llm-code/master/skills/react-testing-library/SKILL.md

After install, confirm what landed and that the folder name matches the frontmatter name:

```bash
ls ~/.hermes/profiles/corpusiq/skills/vite
head -4 ~/.hermes/profiles/corpusiq/skills/vite/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/vite/references | head -5
```

A skill directory that holds only `SKILL.md` and no references installed incompletely, which is the failure mode to look for when an agent quotes a framework confidently and vaguely.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-01) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| react-testing-library | Pass | Pass | Pass |
| project-creator | Pass | Pass | Pass |
| pydantic-ai | Pass | Pass | Warn |
| github-stars-organizer | Pass | Pass | Warn |
| livekit-agents | Pass | Pass | Warn |

The three warnings sit on three of the lowest-install entries in the index, at 55, 27 and 1 installs, and none of the five carries a Fail. The two that pass all three auditors include the most installed skill. Read those three `SKILL.md` files before installing them, and treat the warning as a property of the sample rather than of the repository, which is not audited as a whole.

What executes at install is small. The clone root has no `package.json`, no build script and no lifecycle hook, and the skill directories are markdown plus reference files, 507 files in total with a minimum of three in the smallest skill. The code that runs belongs to the `add-skill` CLI that `npx` fetches, not to this repository, so the CLI version is the thing you are trusting when you run it.

The skills themselves do not call out. None of the sampled skills requires a credential, and the install writes text into a project directory. The part to watch is the API documentation: `open-meteo`, `tavily`, `perplexity`, `telegram` and `inworld` describe services that need a key and a network call, so an agent following one will need a key you supply. Keep such keys in the environment, not in a skill directory that gets copied between projects or committed.

## Limitations

- Snapshot data, verified 2026-11-01: 5,960 combined installs across 49 indexed listings; 24 GitHub stars; MIT; last pushed 2026-10-24. Counts drift over time.
- The index, the README and the tree disagree on size: 49 indexed listings, a README heading that says 46 above a table of 38, and 38 `SKILL.md` directories in the clone. Eleven indexed names, the nine `cloudflare-*` entries plus `agent-browser` and `livekit-agents`, have no directory on branch master, so a listing without a directory cannot be installed by path.
- Three of the five sampled listings carry a Snyk Warn, on `pydantic-ai`, `github-stars-organizer` and `livekit-agents`. The repository as a whole is not covered by that sample.
- Documentation ages. The newest reference in the clone is stamped 2026-10-21 (`vite` 8.3.5) and the oldest 2019-02-21 (`commits`), so the pack spans seven years of conventions, and no update process is described beyond re-running the install.
- Nothing is written for Hermes. The documented paths are the `add-skill` CLI and its four flags; the copy route above is the one that works, and it leaves updates in your hands.
- Coverage is lopsided toward the React, Vite and Postgres stacks. The nine Cloudflare services are indexed at 6 to 23 installs each with no files behind them, so a plan that leans on them has nothing to install.

## Related

- [Tailwind 4 Docs Skill - Local Docs Snapshot Setup](/hermes/skills/catalog/tailwind-4-docs-skill-setup)
- [Modern Web Guidance - Google Chrome Agent Skill Setup](/hermes/skills/catalog/googlechrome-modern-web-guidance-setup)
- [Nuxt Skills - Vue, Nuxt and NuxtHub Agent Setup](/hermes/skills/catalog/onmax-nuxt-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `skill-master` first if you write skills at all. It is the format specification for the folder you are about to edit, and it is the only entry whose subject is the pack itself.
- Prefer `--skill` over the bare command. The default install places all 38 directories in the project, and neighbours such as `base-ui` and `mantine-dev` compete for the same component questions.
- Read the frontmatter version before trusting an answer. `mantine-dev` states 9.7.3 and `vite` states 8.3.5; on an older major, the API the skill quotes may not exist in your build yet.
- Keep `commits` and `changelog` in every repository workspace. They are small, need no service, and stop an agent from inventing commit types or changelog headings.
- Pin the CLI in CI. `npx add-skill` with no version fetches the latest at run time, which is the one moving part in an otherwise static install.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
