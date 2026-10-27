---
title: "Ant Design Skills - Official antd Agent Suite Setup"
description: "ant-design official skills: 11.8K combined installs. Offline antd CLI metadata for props, demos, lint and migration, plus a v6 and Pro decision guide."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ant-design-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-24"
tags: ["hermes skill", "agent skill", "skill setup", "ant design", "react", "frontend"]
---

# Ant Design Skills - Setup Guide

**Source:** [ant-design/ant-design-cli](https://www.skills.sh/ant-design/ant-design-cli) and [ant-design/antd-skill](https://www.skills.sh/ant-design/antd-skill) via skills.sh - 11.8K combined installs across 12 indexed listings; first seen Feb 1, 2026 (ant-design) and Mar 24, 2026 (antd)
**GitHub:** [ant-design/ant-design-cli](https://github.com/ant-design/ant-design-cli) (260 stars; MIT; pushed 2026-10-21; layout `skills/antd/SKILL.md` beside the CLI source and 71 bundled data files) and [ant-design/antd-skill](https://github.com/ant-design/antd-skill) (136 stars; MIT; pushed 2026-03-27; layout `skills/ant-design/SKILL.md`, `skills/ant-design/references/antd-cli.md`, `skills/antd/SKILL.md`)
**Category:** Frontend / React Design System
**Quality Tier:** 🟢 Production - official Ant Design org, MIT on both repos, a vitest suite covering every CLI command in the CLI repo, sampled verdicts Pass on all three scanners, and a CLI push on the day of this sweep

Ant Design is the React design system behind Ant Group's enterprise products and one of the most installed component libraries in the ecosystem. This is the official publisher's own agent layer: a CLI that carries every antd prop, token, demo and changelog offline, shipped with a skill that teaches an agent when to call it, plus a sibling repo holding a decision guide for antd 6, Ant Design Pro 5 and Ant Design X v2.

The pair solves the most common failure in agent-written frontend code: the model writes an API from memory and gets a prop name, a default or a version boundary slightly wrong. Here the lookup is local and version-pinned. The CLI bundles 67 per-version snapshots (v3 2, v4 26, v5 31, v6 8) plus `design-v6.md`, so `antd info Button --version 5.12.0 --format json` answers for that exact release instead of the latest one.

## Installation

```bash
# The CLI skill, from the repo that ships the CLI
npx skills add ant-design/ant-design-cli

# The decision-guide skills, from the sibling repo
npx skills add ant-design/antd-skill

# The CLI itself, which both skills call on every task
npm install -g @ant-design/cli
```

```bash
# Other package managers for the CLI
pnpm add -g @ant-design/cli
bun add -g @ant-design/cli
```

`antd setup --client claude` (also `cursor`, `vscode`, `codex`, `github-actions`) writes the client's MCP config or installs the bundled skill, and `--dry-run` previews the write.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| antd | 5,979 | Offline antd workflows: query props, tokens, demos and docs, lint a file, run doctor checks, analyze usage, and migrate v3 to v6 |
| ant-design | 4,098 | Decision guide for antd 6, Pro 5 and Ant Design X v2: component choice, theming and tokens, SSR, accessibility, performance, Pro routing and CRUD |

The remaining 10 indexed listings range from 3 to 1,329 installs: antd 1,329 (an older copy of the same CLI skill, indexed from antd-skill), antd 121 and pro-upgrade 118 from the ant-design-pro repo, five maintainer workflow skills from the main ant-design/ant-design repo (antd-commit-msg 31, antd-create-pr 23, antd-issue-reply 20, antd-version-release 16, antd-test-review 15), and ant-design-pro 7 plus ant-design-x 3 from antd-skill.

## Why This Matters for Hermes Agents

Frontend work is where a Hermes session burns the most retries: write a component, run the build, watch it fail on a prop that changed two minor versions ago, fix, repeat. An offline lookup that answers per version removes that loop at the source. The agent checks the API before writing the first line, which is the same discipline the skill's own mandatory rules encode.

The second gain is verification. `antd lint` reports deprecated APIs, accessibility gaps and performance issues in files the agent just touched, and `antd doctor` runs ten project-level checks covering React compatibility, duplicate packages, peer dependencies, SSR and babel plugin conflicts. Those are cheap, deterministic gates an agent can run before claiming work is done, and they speak JSON.

The third is migration. `antd migrate 4 5` returns a checklist split into auto-fixable and manual items, and `--apply ./src` generates an agent-ready prompt without touching files, so a version upgrade becomes a reviewed plan rather than a blind rewrite. The same command set covers v3 to v4, v4 to v5 and v5 to v6.

Finally it runs as an MCP server. `antd mcp` exposes eight lookup tools and two prompts over stdio, which means a Hermes agent can consume antd knowledge as tools instead of shelling out, and Cursor, Claude Code or VS Code can share the same source of truth.

## Usage

| You say | What happens |
|---|---|
| "Add a filterable table with server-side pagination" | Runs `antd info Table --format json` and `antd demo Table basic`, then writes the component against the real prop surface |
| "This Select does not behave right on 5.12.0" | Pins the lookup with `antd info Select --version 5.12.0` and checks the prop against that release rather than latest |
| "Upgrade this project from antd 4 to 5" | `antd changelog 4.24.0 5.0.0` for the breaking list, `antd migrate 4 5` for the checklist, then `antd lint` on the changed files |
| "Theme the Form to match our brand" | `antd token Form --format json` and `antd semantic Form --format json` return component tokens and the classNames structure, tokens first instead of global overrides |
| "Which component should I use for a multi-step form?" | The ant-design decision guide maps the need to Steps plus Form, and names the provider and validation baseline |
| "Something in this repo is misconfigured" | `antd doctor` runs the ten diagnostic checks and `antd env` collects the full environment snapshot |
| "Report this antd bug" | `antd bug` previews the issue with the collected environment, waits for confirmation, then submits with `--submit` |

## Verification

Confirm what the skills CLI installed:

```bash
npx skills list | grep -i antd
```

Read both skills before installing. All four URLs below returned 200 when checked on Oct 21, 2026:

```bash
curl -sL https://raw.githubusercontent.com/ant-design/ant-design-cli/main/skills/antd/SKILL.md
curl -sL https://raw.githubusercontent.com/ant-design/antd-skill/main/skills/ant-design/SKILL.md
curl -sL https://raw.githubusercontent.com/ant-design/antd-skill/main/skills/antd/SKILL.md
curl -sL https://raw.githubusercontent.com/ant-design/antd-skill/main/skills/ant-design/references/antd-cli.md
```

Prove the offline lookup works before trusting it in a task:

```bash
which antd || npm install -g @ant-design/cli
antd info Button --format json | head -20
```

## Security

skills.sh verdicts for sampled skills (verified Oct 21, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| antd | Pass | Pass | Pass |
| ant-design | Pass | Pass | Pass |

No sampled verdict reports malware, injection or data exfiltration, and the CLI ships its knowledge inside the npm package, so ordinary lookups make no network calls.

Read the permission block before installing, because three behaviours are writes. The skill grants `Bash(antd *)`, `Bash(antd bug*)`, `Bash(antd bug-cli*)`, `Bash(npm install -g @ant-design/cli*)` and `Bash(which antd)`, and the CLI copy also grants `Bash(antd upgrade*)`. `antd bug --submit` and `antd bug-cli --submit` open a public GitHub issue, which publishes whatever the report contains. `antd setup --client ...` writes MCP config files into the project. `antd upgrade` invokes the detected package manager, which can reach the network. Set `ANTD_NO_AUTO_REPORT=1` to stop the agent from suggesting bug reports at all, and always review a `antd bug` preview before `--submit`.

## Limitations

- The CLI is the load-bearing half and it needs Node plus a global npm install. The two skills still work without it, but every workflow they describe assumes `antd` is on PATH.
- The `antd` skill ships twice and the two copies differ: the ant-design-cli copy allows `antd upgrade` and claims v3 to v6 migration coverage, while the antd-skill copy allows neither and stops at v4 to v6 metadata. Install the CLI repo copy if you want the newer instructions.
- ant-design-pro (7 installs) and ant-design-x (3 installs) are indexed from antd-skill, but that repo's tree holds only `skills/ant-design/` and `skills/antd/`, so those two listings have no SKILL.md today.
- The five maintainer skills are indexed from the main ant-design/ant-design repo. Probes for `skills/<name>/SKILL.md`, `.claude/skills/<name>/SKILL.md`, `.agents/skills/<name>/SKILL.md` and `agent/skills/<name>/SKILL.md` on both `master` and `main` all returned 404, so their path in that repo is unconfirmed at this snapshot.
- Component knowledge stops where the bundled snapshots stop. A brand new release can lag until `antd upgrade` refreshes the data, and v3 projects are handled through `antd migrate 3 4` rather than direct v3 lookups.
- Snapshot data, verified Oct 21, 2026: 11,760 combined installs across 12 indexed listings; 260 GitHub stars on ant-design-cli and 136 on antd-skill; MIT on both; last pushed 2026-10-21 and 2026-03-27. Counts drift over time.

## Related

- [HeroUI Skills - React & React Native UI Component Setup](/hermes/skills/catalog/heroui-skills-setup) - the same CLI-backed lookup pattern for a different React component system.
- [Stitch Skills - Google Design-to-Code Pipeline Setup](/hermes/skills/catalog/stitch-skills-setup) - design-to-code generation that pairs with antd component lookups.
- [Emil Kowalski Skills - Design Engineering Suite Setup](/hermes/skills/catalog/emilkowalski-skills-setup) - interaction and motion quality checks for the components built with antd.
- [Better UI Skills - Interface Polish Suite Setup](/hermes/skills/catalog/better-ui-skills-setup) - a polish pass over generated interfaces.
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Let the agent query first. The skill's own rule is `antd info <Component>` before writing code, and it is the single change that removes most broken component output.
- Always pass `--format json`. Text output is for humans, and a parser against it breaks on the next release.
- Pin `--version` to the project's installed antd when the answer matters. Without it the CLI answers for its newest snapshot.
- Use `antd migrate 4 5 --apply ./src` to get a plan, not an edit. It emits a prompt and leaves files untouched, so the upgrade stays reviewable.
- Wire `antd mcp` into the agent config when the session does a lot of component work. Eight tools over stdio beat shelling out per question, and they return the same offline data.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
