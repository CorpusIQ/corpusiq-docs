---
title: "LobeHub Skills - Agent Platform Engineering Setup"
description: "lobehub/lobehub: 79.9K combined installs. 56 engineering skills from the LobeHub platform repo: zustand stores, Drizzle migrations, i18n and PRs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/lobehub-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup", "lobehub", "agents", "monorepo", "typescript"]
---

# LobeHub Skills - Setup Guide

**Source:** [lobehub/lobehub](https://www.skills.sh/lobehub/lobehub) via skills.sh - 79.9K combined installs across 69 indexed listings; first documented 2026-11-03 (nightly sweep)

**GitHub:** [lobehub/lobehub](https://github.com/lobehub/lobehub) - 83,762 stars, LobeHub Community License (GitHub reports NOASSERTION), branch canary, last pushed 2026-11-03; 56 skill directories under `.agents/skills/`, each a single `SKILL.md` with plain frontmatter, plus a `.claude/skills` symlink pointing back at `../.agents/skills`

**Category:** In-repository engineering skills for a large TypeScript agent platform: state, data fetching, database, desktop, i18n, testing and release work

**Quality Tier:** 🟢 Green - all three sampled listings pass Gen Agent Trust Hub, Socket and Snyk, and the repository ships a LICENSE file, though that file is a custom community licence rather than a standard OSI one

Most skill repositories in this catalog exist so an agent can operate someone else's service. This one is different. LobeHub keeps 56 skills in its own repository, and they are the instructions its own coding agents follow when working on the codebase: how to shape a Zustand store, how to roll out a Drizzle migration, where a file belongs, how to open a stacked pull request against `canary`. Publishing them to skills.sh made a private working practice readable, and that is what makes them worth studying even if you never run them.

The repository is a real product, not a skill collection. LobeHub describes itself as a chief agent operator that organizes agents into continuous operations, hiring and scheduling and reporting on a team of them. The skills reflect that scale of engineering: `project-overview` maps the code layers, `source-layout` decides where a file lives and how to split one past 1,200 lines, `alint-ruleset` maintains a model-backed lint rule set, and `skills-audit` audits the skill directory itself for duplicates and stale entries.

The frontmatter is the part worth copying. Skills carry `user-invocable: false` when the model should load them as context but a user should not trigger them directly, `disable-model-invocation: true` when a human must run them explicitly, and `argument-hint` when they take arguments. That is a skill library with a permission model, and it is a better template than the usual free-for-all directory.

## Installation

The skills install through skills.sh by repository and skill name, the same route the repository uses for its own generated `acceptance` skill:

```bash
npx skills add lobehub/lobehub --skill zustand
npx skills add lobehub/lobehub --skill project-overview
```

For a Hermes profile, clone and copy the one directory you want. Each skill is self-contained:

```bash
git clone --depth 1 --branch canary https://github.com/lobehub/lobehub.git /tmp/lobehub
cp -r /tmp/lobehub/.agents/skills/zustand ~/.hermes/profiles/corpusiq/skills/
```

Note the branch. The default branch on this repository is `canary`, and the skill content tracks it, so a clone without `--branch canary` may land on a release branch with a different skill set.

One skill has its own installer. `acceptance` is generated from the separate `lobehub/acceptance` repository, and the repository's own CLI updates the committed copy:

```bash
lh acceptance install
lh acceptance update
```

The CLI README states that this selects the same source as `npx skills add lobehub/acceptance --skill acceptance`, that changes merged into the default branch arrive on the next install or update without a version bump, and that `update` replaces the materialised files and removes stale resources. If you only want the skill text, the plain skills.sh route is enough.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| zustand | 6,898 | Zustand stores: state shapes and type sources, state-only stores with xActions classes, replica-backed list and detail data, selectors, optimistic writes. |
| react | 5,651 | TSX components, UI libraries, styling, state locality, layout, render performance and memoization. |
| drizzle | 5,468 | Drizzle schemas and queries: tables, indexes, relations, joins and inferred types. Migration rollout belongs to `db-migrations`. |
| typescript | 5,220 | TypeScript style and type safety when editing TS, TSX or MTS: imports, async code and error suppression. |
| i18n | 4,653 | User-facing strings and react-i18next keys: namespaces, interpolation, translations and the `bun run i18n` flow. |
| project-overview | 4,434 | The repository map: code-layer lookup, ownership across `apps`, `packages` and `src`, business stubs. |
| testing | 4,317 | Vitest tests, mocks, coverage and diagnosing a failing test. |
| desktop | 4,233 | Electron work: IPC handlers, controllers, preload scripts, window and menu management. |
| modal | 4,205 | Modals, dialogs and confirmations through `createModal`, `confirmModal`, `ModalHost` or the base-ui modal APIs. |
| add-setting-env | 4,175 | Server-side environment variables that set defaults for user settings. |
| linear | 4,114 | Linear issues: LOBE-xxx links, status updates, completion comments and sub-issue trees. |
| hotkey | 4,103 | Keyboard shortcuts: registration, key combinations, scope, conflicts and shortcut tooltips. |
| add-provider-doc | 3,857 | Provider documentation for an existing model provider. The integration itself is `add-model-provider`, whose text covers provider documentation updates. |
| microcopy | 2,547 | Indexed listing with no directory in the current canary tree, so no in-tree description was available. |
| version-release | 2,368 | The release workflow and GitHub Release notes. Docs and changelog pages are a separate concern. |
| store-data-structures | 2,354 | An explicit compatibility entry that routes to the Zustand data-shape guidance. |
| pr | 2,301 | Opening a PR against `canary`, including splitting one cross-layer branch into ordered stacked PRs so the lower layer merges first. |
| upstash-workflow | 2,292 | Upstash Workflow and QStash handlers, triggers, durable steps and async fan-out. |
| debug | 1,467 | Indexed listing with no directory in the current canary tree, so no in-tree description was available. |
| recent-data | 863 | Indexed listing with no directory in the current canary tree, so no in-tree description was available. |

The remaining 49 indexed listings range from 1 to 808 installs.

## Why This Matters for Hermes Agents

The useful thing here is not the individual advice, it is the shape of a working library at scale. Fifty-six skills in one repository is past the point where a flat directory stays coherent, and the answers LobeHub arrived at are the ones a growing Hermes profile will need: a repository map skill (`project-overview`) that the others can assume, a source layout skill that decides where new files go, a duplication-audit skill run on a schedule, and frontmatter flags that separate "the model should load this" from "a human should trigger this".

The second lesson is separation by concern. `drizzle` covers schemas and queries and explicitly says that rollout belongs to `db-migrations`. `store-data-structures` is a compatibility entry that forwards to `zustand` rather than repeating it. `add-model-provider` covers the integration and owns the provider documentation update; `add-provider-doc` is the narrower entry for docs alone. That kind of boundary discipline is what keeps a large library from becoming 56 variations of the same paragraph, and it is visible in the descriptions rather than in a style guide.

The third is that these skills are written for an agent that is editing code, not for one that is answering a question. Almost all of them assume a working copy, a package manager and a test runner, and several are explicitly non-invocable by the model. Copying the format is easy; copying the assumption means committing to a repository where an agent is allowed to run the tests.

## Usage

| You say | What happens |
|---|---|
| "Where does this new component belong in this repo?" | `source-layout` answers where a file lives, how it is named and where its tests go, and `project-overview` supplies the ownership map across apps and packages. |
| "Split this 1,400-line file before I add the feature" | `split-large-file` refactors it into a directory of cohesive modules test-first; `source-layout` covers the naming and the threshold. |
| "Add a provider for this model vendor" | `add-model-provider` walks the runtime integration, model cards, configuration, branding and docs, and points at `add-provider-doc` for the documentation update alone. |
| "These new strings need translations" | `i18n` handles react-i18next namespaces, interpolation and locale keys, then runs the repository's `bun run i18n` flow. |
| "Open a PR but the backend has to merge first" | `pr` targets `canary` and splits the cross-layer branch into ordered stacked PRs so the server contract lands before its callers. |
| "Are any of our skills stale or duplicated?" | `skills-audit` checks `.agents/skills` for duplicate, overlapping, stale, inconsistent or broken entries and reports merge and delete candidates. |
| "Write the release notes for this version" | `version-release` covers the release workflow and GitHub Release notes, leaving docs and changelog pages to `docs-changelog`. |

## Verification

The raw path below returned 200 on branch canary on 2026-11-03:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/lobehub/lobehub/canary/.agents/skills/zustand/SKILL.md
```

After a clone, confirm the branch, the skill count and the symlink that lets Claude Code read the same tree:

```bash
git clone --depth 1 --branch canary https://github.com/lobehub/lobehub.git /tmp/lobehub
ls /tmp/lobehub/.agents/skills | wc -l
readlink /tmp/lobehub/.claude/skills
head -3 /tmp/lobehub/.agents/skills/zustand/SKILL.md
```

The count should print 56, `readlink` should print `../.agents/skills`, and `head` should show `name: zustand` with the store guidance description. To see the frontmatter convention in one command:

```bash
grep -rl "disable-model-invocation: true" /tmp/lobehub/.agents/skills | wc -l
grep -rl "user-invocable: false" /tmp/lobehub/.agents/skills | wc -l
```

Both counts should be non-zero. Those two flags are the reason a skill can be present in the library and still not be something the model triggers on its own, and they are worth copying into any profile that has grown past a dozen skills.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-03) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| zustand | Pass | Pass | Pass |
| react | Pass | Pass | Pass |
| drizzle | Pass | Pass | Pass |

Three passes out of three, and the content backs it up: the skills are Markdown instructions with no installer and no bundled script. The `acceptance` skill is the exception worth reading, since it runs a CLI that publishes reports, and it needs `lh login` before it can publish anything; without a login it renders reports locally instead.

The licence is the item to check before reuse. GitHub reports the licence as NOASSERTION because the file is the LobeHub Community License, which is Apache 2.0 plus a condition: LobeChat may be used commercially as a frontend and backend service without modifying the source, but a commercial licence from the producer is required to develop and distribute a derivative work. Reading and learning from these skills is unaffected. Lifting the skill text into a product you distribute is a different question, and the licence is the place to answer it.

Two operational cautions. Several skills instruct an agent to run repository commands, including the CLI, the test runner and git worktree cleanup, so install them into a profile that is pointed at a checkout you are willing to have modified. And `linear` and `acceptance` talk to external services, which means account credentials and, in the acceptance case, publication of a report.

## Limitations

- Snapshot data, verified 2026-11-03: 79,938 combined installs across 69 indexed listings; 83,762 GitHub stars; LobeHub Community License; last pushed 2026-11-03. Counts drift over time.
- The index and the tree disagree. There are 69 indexed listings and 56 skill directories, and 14 indexed names have no directory in the current canary tree, including four above the table threshold: `add-provider-doc`, `microcopy`, `debug` and `recent-data`. One directory, `cli-npm-release`, is not indexed at all.
- The skills assume LobeHub's own repository. Paths, the `bun` package manager and the `lh` CLI appear throughout, and several reference worktrees and internal packages that do not exist outside this monorepo.
- Many skills are not model-invocable. `user-invocable: false` and `disable-model-invocation: true` are common, which is correct for the repository and means a copied skill may sit idle until something explicitly routes to it.
- The licence is not OSI-standard. Commercial derivative distribution needs a licence from LobeHub, so treat the text as reference material rather than a component to vendor.
- Skills track the `canary` branch, which moves daily. Installs drift from the indexed descriptions, and there is no tagged release of the skill set to pin.

## Related

- [HeroUI Skills - React & React Native UI Component Setup](/hermes/skills/catalog/heroui-skills-setup)
- [OpenAI Agents Python Skills - Multi-Agent Setup](/hermes/skills/catalog/openai-agents-python-skills-setup)
- [Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)
- [Composio - SDK Monorepo and Agent Toolkit Setup Guide](/hermes/skills/catalog/composiohq-composio-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Read `project-overview`, `source-layout` and `skills-audit` before installing anything else. They are the three skills that explain how the other 53 are organised, and together they are the closest thing to a style guide in the repository.
- Copy the frontmatter convention, not just the prose. `user-invocable: false` for context skills and `disable-model-invocation: true` for human-only ones is what keeps a large library from flooding the model's trigger surface.
- Pin the branch when you clone. `canary` is the default, and a release branch will hand you an older set with different names.
- Skip the skills whose indexed name has no directory in the tree. `add-provider-doc`, `microcopy`, `debug` and `recent-data` are index entries from an earlier revision, and installing one from skills.sh gives you text that no longer matches the repository.
- Run `skills-audit` on your own profile once you pass a few dozen skills. It is written to find duplicate, overlapping, stale and broken entries, and that problem is not specific to LobeHub.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
