---
title: "Better Icons - Icon Search Skill Setup"
description: "better-auth/better-icons: 6.0K combined installs. One skill plus an MCP server for searching 200,000+ icons across 150+ Iconify collections."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/better-auth-better-icons-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "icons", "iconify", "mcp", "ui"]
---

# Better Icons - Setup Guide

**Source:** [better-auth/better-icons](https://www.skills.sh/better-auth/better-icons) via skills.sh - 6.0K combined installs across 1 indexed listing; first seen 2026-10-30 (morning sweep)

**GitHub:** [better-auth/better-icons](https://github.com/better-auth/better-icons) - 1,445 stars, MIT License, branch main, last pushed 2026-04-02; one flat skill file at `skills/SKILL.md` with no per-skill directories, beside a TypeScript CLI and MCP server in `src/` (`server.ts`, `memory.ts`, `project-sync.ts`, `commands/`), package version 1.0.5, `engines.node >= 18`

**Category:** Icon library search and selection for UI work

**Quality Tier:** 🟡 Beta - 1 sampled Warn verdict(s), the Snyk row for better-icons in a three-checker sample; one small skill file over a published CLI and MCP server that queries the public Iconify API

Better Icons is published by better-auth, the organization behind the Better Auth authentication framework, and its `package.json` names bekacru as author. The tool does one job narrowly: it searches the Iconify catalogue, which the README sizes at 200,000+ icons across 150+ collections, and returns SVG or framework component code for the icon you pick. It is shipped two ways, as a CLI you can run directly and as an MCP server that exposes the same operations to an agent, and `skills/SKILL.md` is the single skill file that teaches an agent how to drive either one.

The skill is deliberately thin, 129 lines covering an install reminder, the CLI surface, the `prefix:name` icon ID format and a table of the MCP tools. That thinness is the point: the capability lives in the npm package, not in the markdown, so the skill stays cheap to keep resident in a profile. What makes it worth a page is the local state it keeps. Searches update a collection-usage file at `~/.better-icons/preferences.json`, so the tool learns which libraries a project actually uses and ranks those first next time, and `sync_icon` writes icon components straight into a project icons file instead of pasting SVG through the conversation.

## Installation

The README's agent route is the skills CLI, and it installs the instructions only:

```bash
npx skills add better-auth/better-icons
```

The CLI itself has to exist on `PATH` before any of the commands in the skill will run, so install it once at environment setup. The skill file says the same thing and recommends the global install for exactly this reason:

```bash
# Using npm
npm install -g better-icons

# Using Bun (faster)
bun add -g better-icons
```

Running without a global install is supported, but then every command needs the `npx` or `bunx` prefix, which is what the skill's examples avoid:

```bash
npx better-icons search arrow --limit 10
npx better-icons get lucide:home > icon.svg
```

To expose the tools to an agent over MCP, the README's wizard writes the client config for you:

```bash
npx better-icons setup
```

That wizard configures Cursor, Claude Code, OpenCode, Windsurf, VS Code (Copilot) and Google Antigravity interactively, and it takes `-a` for agents and `-s` for scope (`better-icons setup -a cursor,claude-code -s project`). Hermes is not one of the six, so the durable route for this profile is a copy of the skill file into the profile skills tree:

```bash
git clone https://github.com/better-auth/better-icons.git
mkdir -p ~/.hermes/profiles/corpusiq/skills/better-icons
cp better-icons/skills/SKILL.md ~/.hermes/profiles/corpusiq/skills/better-icons/SKILL.md
```

Note the layout quirk: the repository ships `skills/SKILL.md` flat, with no `skills/better-icons/` directory of its own, so the directory name in the profile has to come from you. If you would rather have the MCP server than the CLI in the loop, the manual form is a `better-icons` entry under `mcpServers` in the client config with `command: npx` and `args: ["-y", "better-icons"]`, which is the block the README repeats for Cursor, Claude Code and Antigravity.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| better-icons | 6,047 | Searching 200,000+ icons across 150+ Iconify collections by keyword, collection prefix or category, then returning SVG, React, Vue, Svelte or Solid component code, a direct icon URL, or a written component in the project icons file; the skill covers the `better-icons search`, `get`, `setup` and `config` commands plus the MCP tool set the README documents, including batch retrieval, similar-icon lookup, use-case recommendations, project scanning and learned collection preferences. |

No indexed listings fall below the threshold; all 1 appear above.

## Why This Matters for Hermes Agents

Icon choice is a quiet failure mode in generated UI. A model asked for a "settings icon" will invent an icon name that does not exist in the installed set, or inline a plausible-looking SVG path, and neither mistake shows up until the build breaks or a reviewer notices three icon families in one toolbar. Better Icons moves that decision into a lookup against a catalogue that actually exists, keyed by the `prefix:name` IDs the tool can retrieve, so a wrong name fails at search time instead of at render time.

The token argument is the second reason. Inline SVG in a chat or a diff costs tokens on every turn it stays in context and bloats the file it lands in, which is why the tool's headline feature is project sync: `sync_icon` writes the component into a `.tsx`, `.ts` or `.js` icons file and returns the import statement to use. For a Hermes profile that edits repositories, that turns "add a home icon" into a small, reviewable write to one known file rather than a block of markup pasted into a conversation.

It is also a good fit for unattended work because the deterministic path is a shell command. `better-icons search <query> --json` returns structured results a script can parse, and `better-icons get <id> > icon.svg` is a one-line fetch, so a cron job can regenerate or audit an icon set without an agent reasoning about markup at all. The skill's contribution is telling the agent which command to reach for and what the ID format looks like.

The last point is a scoping one. This is a single flat skill, not a collection, so it costs one description in routing context and does nothing until the task is actually about icons. The learned preferences file makes repeated work in one repository cheaper over time, and the recent-icons history gives the agent a way to answer "use the same one we used before" without re-searching.

## Usage

| You say | What happens |
|---|---|
| "Find me a settings icon that matches the rest of our Lucide set" | `search_icons` with the `lucide` prefix, or `better-icons search settings --prefix lucide`, returns matching IDs in the prefix:name form the `get` command needs. |
| "Add a home icon to our icons file" | `sync_icon` fetches the SVG and appends a component to the file you name, deriving the export name from the icon ID (`lucide:arrow-right` becomes `ArrowRightIcon`), then reports the import statement and a usage example. |
| "What icons does this project already have?" | `scan_project_icons` reads the icons file you point it at and lists what is already available, which is the check that stops a duplicate component being added. |
| "Give me the same check mark in Heroicons and Material" | `find_similar_icons` on `heroicons:check` returns the variants across collections and styles, and `get_icons` fetches up to twenty of them in one batch call. |
| "Download every arrow icon as SVG files" | `better-icons search arrow -d ./icons --limit 64` uses the batch download flag to write each result as a file in the target directory, with optional `-c` colour and `-s` size applied. |
| "Which icon collection does this codebase actually use?" | `get_icon_preferences` reports the collection usage counts recorded in `~/.better-icons/preferences.json`, and `clear_icon_preferences` resets them when a project changes direction. |
| "Wire the icon tools into my editor" | `better-icons setup -a cursor,claude-code -s project` writes the MCP server entry into that client's config at project scope, or `better-icons config` prints the manual block to paste. |

## Verification

Both raw paths below returned 200 on branch main when this guide was written on 2026-10-30:

```bash
curl -sL -o /dev/null -w "%{http_code} skill\n" \
  https://raw.githubusercontent.com/better-auth/better-icons/main/skills/SKILL.md
curl -sL -o /dev/null -w "%{http_code} package\n" \
  https://raw.githubusercontent.com/better-auth/better-icons/main/package.json
```

Expect `200` twice. Read the skill file before installing, because its frontmatter is the whole routing contract and it is short enough to check in a minute: it names the trigger (working with icons in any project), the two commands that do the work and the fact that an MCP server is available as an alternative surface.

After the copy lands in the profile, confirm the file arrived with its frontmatter intact and that the CLI resolves:

```bash
head -3 ~/.hermes/profiles/corpusiq/skills/better-icons/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/better-icons/
```

The header should show `name: better-icons` and a populated `description:`, and the directory listing should show `SKILL.md`. If the listing comes back empty, the copy step never landed the file. On the CLI side, `better-icons` should resolve on `PATH` and `package.json` reports version 1.0.5 as the published package at snapshot time.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-30) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| better-icons | Pass | Pass | Warn |

The Snyk Warn is the one sampling result worth reading before you install, and the pack records the verdict rather than the finding behind it, so open that entry on skills.sh rather than inferring the cause. The plausible shape of the risk is visible in the code: the skill tells an agent to run a globally installed npm binary that makes network calls to `https://api.iconify.design` and writes SVG and component code into whatever file path the agent supplies to `sync_icon`.

That write surface is the part to constrain. `sync_icon` and `scan_project_icons` both take an absolute `icons_file` path, so an agent following the skill can modify any file it is told about, and the mitigation is the ordinary one: run it in a repository you can diff, and review the change rather than trusting the confirmation message. The manual MCP configuration in the README uses `npx -y better-icons`, which fetches the latest published package at every launch, so pinning a version is the difference between a reproducible tool and one that changes under you.

Nothing in the skill handles credentials, and there is no account or API key in the flow: Iconify's API is public and unauthenticated, and the only local state is the preferences and history file at `~/.better-icons/preferences.json`. The runtime dependency chain is small and conventional (`@modelcontextprotocol/sdk`, `commander`, `chalk`, `@clack/prompts`) and requires Node 18 or newer.

## Limitations

- Snapshot data, verified 2026-10-30: 6,047 combined installs across 1 indexed listing; 1,445 GitHub stars; MIT; last pushed 2026-04-02. Counts drift over time.
- One indexed listing means there is no ranking to read. The 6.0K figure measures the tool as a whole and says nothing about which of its surfaces, CLI or MCP, anyone actually uses, so it cannot be compared with per-skill install counts.
- The layout and the index do not line up. The index names one listing, `better-icons`, while the tree holds a single flat `skills/SKILL.md` with no `skills/better-icons/` directory, so any copy route has to supply that directory name itself and there is no per-skill folder to fetch from the repository.
- The repository is inconsistent about collection size. The README claims 200,000+ icons from 150+ collections, while the `SKILL.md` frontmatter and `package.json` description both say "200+ icon libraries". Treat the larger figure as the README's marketing line and check a live search for the collection you need.
- Installing the skill gives you instructions, not the capability. Without `better-icons` on `PATH` (or a deliberate `npx` fallback) every command in the file fails, and `npx` needs network access to resolve the package before it can do anything.
- Everything icon-shaped needs the live Iconify API at `https://api.iconify.design`. Offline or air-gapped runs cannot search or fetch, and the learned preferences are local only: `~/.better-icons/preferences.json` keeps collection counts plus a recent history capped at 50 entries, so a new machine starts with no memory.

## Related

- [shadcn Skill - shadcn/ui Component Workflows Setup](/hermes/skills/catalog/shadcn-ui-setup)
- [HeroUI Skills - React & React Native UI Component Setup](/hermes/skills/catalog/heroui-skills-setup)
- [components.build - UI Component Standards Setup](/hermes/skills/catalog/vercel-components-build-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the CLI globally before you install the skill. The skill's own advice is the same, and a profile that carries the markdown without the binary will keep narrating commands it cannot run.
- Send the agent to `sync_icon` rather than `get_icon` when the destination is a real project. `get_icon` returns markup into the conversation, which is the token cost the tool exists to avoid, while `sync_icon` writes it to the icons file and returns the import.
- Name the collection prefix in the request. `--prefix lucide` cuts a 999-result search down to one family, keeps the style consistent with the rest of the app, and the learned preferences will start favouring that collection automatically.
- Use `--json` for anything scripted. `better-icons search <query> --json` and `better-icons get <id> --json` give a cron or a build step structured output, so icon auditing does not need an agent in the loop.
- Pin the package version when you configure the MCP server. The README's `npx -y better-icons` form always pulls the latest publish, which is fine for experimenting and wrong for anything you expect to behave the same next month.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
