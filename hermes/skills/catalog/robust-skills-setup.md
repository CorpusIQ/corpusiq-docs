---
title: "Robust Skills - Architecture and Platform Suite"
description: "ccheney/robust-skills: 7.8K combined installs. Eleven engineering skills for DDD, PostgreSQL, Mermaid, Slack, Teams, CSS and Bazel."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/robust-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skill setup", "architecture", "postgresql", "slack"]
---

# Robust Skills - Setup Guide

**Source:** [ccheney/robust-skills](https://www.skills.sh/ccheney/robust-skills) via skills.sh - 7.8K combined installs across 12 indexed listings; first seen 2026-11-01 (morning sweep)

**GitHub:** [ccheney/robust-skills](https://github.com/ccheney/robust-skills) - 61 stars, MIT, branch main, last pushed 2026-09-30; 11 `SKILL.md` files under `skills/<name>/`, each with a `references/` folder of topic-split markdown (four to eleven files per skill), plus a `scripts/check-teams-card.mjs` linter inside `teams-adaptive-cards` and a repository-level `docs/`, `evals/` and `scripts/` tree

**Category:** Backend architecture, database, diagramming and workplace messaging skills for engineering agents

**Quality Tier:** 🟢 Green - all three sampled skills pass Gen Agent Trust Hub, Socket and Snyk, and the repository is MIT

The README describes the project as task-specific engineering skills for Bazel, backend and frontend architecture, JavaScript, CSS, PostgreSQL and Drizzle, Mermaid, Slack and Microsoft Teams, with a concise entrypoint per skill that links to technical references only when a task needs them. That structure is the point of the pack. A `SKILL.md` here is a routing and contract document of roughly fifty to eighty lines, and the depth sits in the reference files beside it: seven for the architecture skill, eleven for modern JavaScript, one per decision rather than one per topic.

The authoring convention is consistent enough to be a feature. Every description ends by excluding what the skill is not for, in the same grammatical slot: not routine CRUD changes, not unrelated databases or generic backend work, not every visualization, not every new component or page. Every body opens by stating that the user's explicit instructions take precedence over the skill's guidelines. The result is a pack an agent can load without turning every request into an architecture review, which is the usual failure mode of opinionated engineering skills.

The rules inside the bodies are also the kind that only get written after being burned. Do not infer the installed Drizzle relation API from an npm dist-tag, because 0.x `relations()` and v1 `defineRelations()` are different surfaces. Do not run `clean --expunge` or disable the sandbox to make a missing Bazel input go away, because both hide the cause. Treat `EXPLAIN ANALYZE` as query execution, writes included. Establish the target before applying a migration, since authoring SQL does not require running it. That tone carries through the pack and is the reason it reads as review-grade rather than tutorial-grade.

The repository also ships its own evaluation set: 112 artifact tasks, 226 routing requests, deterministic graders and a bounded free-tier runner, plus a metadata validator. No evaluation workflow runs in GitHub Actions, so the numbers are a claim you can reproduce locally rather than a badge.

## Installation

The README documents the CLI install with a full repository URL and the `--skill` flag, which differs from the shorter `-s` form some other packs use:

```bash
npx skills add https://github.com/ccheney/robust-skills
npx skills add https://github.com/ccheney/robust-skills --skill bazel
```

Both lines are quoted from the README, which repeats the single-skill form for each of the eleven directories. For a Hermes profile that wants a subset without the CLI, clone and copy the directories you need. The skills live under `skills/`, so the copy is a directory move and the `references/` folder travels with its skill:

```bash
git clone --depth 1 https://github.com/ccheney/robust-skills.git /tmp/robust-skills
cp -r /tmp/robust-skills/skills/clean-ddd-hexagonal ~/.hermes/profiles/corpusiq/skills/
```

That clone and copy is our route, not the project's; the README only documents the CLI. If you want to run the repository's own checks after cloning, the README asks for Python 3.10 or newer and one dependency:

```bash
python3 -m pip install 'PyYAML>=6,<7'
python3 scripts/validate_skills.py
```

The validator checks metadata, local resource links and evaluation coverage. It does not measure whether a skill activates on the right request or whether its technical advice is correct, which is what the evaluation cases are for.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| clean-ddd-hexagonal | 4,695 | Choosing and defending backend boundaries: bounded contexts, aggregates, dependency direction, ports and adapters, with CQRS, outbox and event sourcing treated as decisions justified by the task rather than defaults. |
| postgres-drizzle | 1,521 | Writing or reviewing PostgreSQL schemas, queries and migrations alongside Drizzle ORM code, including the 0.x `relations()` versus v1 `defineRelations()` split and index diagnosis from query plans. |
| mermaid-diagrams | 468 | Picking the diagram type that answers the question and emitting renderable Mermaid with stable node IDs, quoted labels and one declaration per block. |
| modern-javascript | 260 | Debugging ECMAScript semantics: promise completion, async iteration, lazy iterator helpers, `forEach` with async callbacks, and syntax transform versus runtime polyfill choices. |
| feature-slicing | 239 | Placing code in Feature-Sliced Design layers from app down to shared, and keeping the import contract from collapsing into sideways slices. |
| modern-css | 207 | Choosing native CSS for layout, theming and motion, from grid and container queries to cascade layers and custom properties, with a fallback where support is missing. |
| slack-block-kit | 158 | Building Block Kit payloads for messages, modals and App Home, including streaming responses and Work Object unfurls, with per-surface limits checked rather than assumed. |
| slack-mrkdwn | 121 | Formatting Slack text for the receiving field, mrkdwn versus markdown blocks versus `rich_text`, with mention IDs preserved and ampersands escaped in the right order. |
| teams-adaptive-cards | 49 | Building and validating Adaptive Cards across bot, webhook and Graph transports, with the bundled `check-teams-card.mjs` linter returning 0, 1 or 2. |
| teams-message-formatting | 42 | Formatting Teams bot text, Adaptive Card TextBlocks and Graph `chatMessage` bodies while keeping mention metadata synchronised with the visible text. |
| bazel | 18 | Configuring and troubleshooting Bazel 9 builds: choosing between `query`, `cquery` and `aquery`, Bzlmod modules, visibility, and diagnosing cache misses without resorting to `clean --expunge`. |
| slack-rich-output | 2 | No directory in the current tree; an index-only listing with no `SKILL.md` to install. |

Eleven of the twelve listings map to a directory. The remaining row, `slack-rich-output` at 2 installs, has no counterpart in the tree, so the installable surface is the eleven skills listed above it.

## Why This Matters for Hermes Agents

The expensive failures in an agent's engineering work are rarely syntax. They are boundary calls: where the domain stops and the transport starts, whether a relation belongs in the ORM or the foreign key, whether a new component deserves a shared slot. Those calls are cheap to make badly and expensive to reverse, and they are exactly what a general-purpose model improvises when it has no reference to check against. This pack supplies the reference, one decision at a time.

The reference-per-decision layout is the part that pays off inside a context window. A forty-line entrypoint plus one loaded reference is a different budget from a single long document that has to be read whole, and the entrypoint itself says which reference to load for which question, so an agent can arrive, take the table row it needs and leave. That is the opposite of dumping a framework into the prompt and hoping the relevant paragraph survives.

The pack also encodes restraint, which is harder to buy. Each skill states that an ordinary edit is not permission to migrate an architecture, and several name the shortcut that hides a real problem: expunging a cache to dodge a missing input, inferring a library API from a dist-tag, changing a transport to fix punctuation. An agent that follows those instructions declines more work, which is usually the correct behaviour and rarely the default one.

For platform-facing work, the Slack and Teams skills cover the surface that most agent integrations get subtly wrong. Markdown is not mrkdwn, Adaptive Card Markdown has no tables or code fences, a webhook is not a bot, and a payload that validates locally can still fail to render on mobile. Both skills refuse to fabricate channel or user IDs and separate creating a payload from posting it, which is the boundary you want in a profile that can write to a workspace.

## Usage

| You say | What happens |
|---|---|
| "The domain logic is leaking into our HTTP handlers, review the layers" | `clean-ddd-hexagonal` returns the boundary that is wrong, the dependency direction it should follow, and the tradeoff the fix introduces, instead of a folder restructure. |
| "This report query takes nine seconds on 400k rows" | `postgres-drizzle` reads the plan and workload evidence, checks for indexes on referencing columns, and proposes the change with the version assumptions named. |
| "Draw how an order moves from cart to fulfilment" | `mermaid-diagrams` picks a sequence or state diagram from the question, emits one fenced block, and warns if the destination renders an older Mermaid. |
| "This async map only awaits the first item" | `modern-javascript` identifies the `forEach` with an async callback, explains that rejections do not cancel work, and offers a sequential or concurrent replacement. |
| "Where should this checkout button component live?" | `feature-slicing` places it page-local first, extracts only when shared use justifies it, and prints the resulting import path. |
| "Our Slack alert shows literal asterisks in one channel and bold in another" | `slack-mrkdwn` identifies which field each message actually uses and returns the correct syntax plus the escaped fallback text. |
| "This Teams webhook card renders blank on mobile" | `teams-adaptive-cards` selects the transport, checks element support against the card version, and runs the bundled linter over the payload. |

## Verification

The raw path for the architecture skill returned HTTP 200 on branch main when this guide was written on 2026-11-01:

```bash
curl -sL -o /dev/null -w "%{http_code} clean-ddd-hexagonal\n" \
  https://raw.githubusercontent.com/ccheney/robust-skills/main/skills/clean-ddd-hexagonal/SKILL.md
```

Expect `200`. After the clone, confirm that the tree holds eleven skills and that each one carries the references its entrypoint promises:

```bash
find /tmp/robust-skills/skills -name SKILL.md | wc -l
ls /tmp/robust-skills/skills/clean-ddd-hexagonal/references
head -6 /tmp/robust-skills/skills/bazel/SKILL.md
```

The count should print 11. The reference listing should match the seven filenames the entrypoint names (LAYERS, DDD-STRATEGIC, DDD-TACTICAL, HEXAGONAL, CQRS-EVENTS, TESTING, CHEATSHEET, all `.md`), and the Bazel header should show `name: bazel` with a `metadata:` block carrying the version. A skill whose references are missing will still load and will silently lose its depth, so check this before relying on it.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-01) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| clean-ddd-hexagonal | Pass | Pass | Pass |
| postgres-drizzle | Pass | Pass | Pass |
| mermaid-diagrams | Pass | Pass | Pass |

There is very little here to exploit. The eleven skills are markdown instructions plus markdown references, with no credentials, no package manifest at the skill level and no network calls during a task. The only executable in the pack is `check-teams-card.mjs`, a local JSON validator that takes a file path and an optional transport and returns 0, 1 or 2; it reads the payload you hand it and posts nothing. The repository validator is Python and runs at authoring time, not when a skill activates.

The residual risk is behavioural rather than malicious, and it is worth being precise about it. A skill that says establish the target before applying a migration is protecting you from an agent that runs DDL against production because the SQL looked correct; a skill that says payload creation does not authorize posting is protecting you from an integration that notifies a whole workspace to demonstrate a card. Both instructions only work if the operator honours them, since nothing in the pack can enforce a target or a send. Keep the database and messaging skills scoped in the prompt, name the environment explicitly, and let the agent produce artifacts without granting it the follow-up action it did not ask for.

## Limitations

- Snapshot data, verified 2026-11-01: 7,780 combined installs across 12 indexed listings; 61 GitHub stars; MIT; last pushed 2026-09-30. Counts drift over time.
- The index lists 12 skills but the tree holds 11 directories. `slack-rich-output` at 2 installs has no directory, so it cannot be installed and its 2 installs are not part of anything you can run.
- Install counts are steeply skewed: the architecture skill carries 4,695 of the 7,780 total, six of the skills sit under 500 and the Bazel skill has 18. Popularity here tracks how broadly the topic applies, not skill quality.
- Version-specific guidance is a research snapshot. The Bazel skill is pinned to 9.2.0, the Mermaid examples were checked against 11.16, the Postgres references cover 17 and 18, and Drizzle changed its relation API between 0.x and v1. Match each to what is installed rather than assuming the newest.
- The evaluation suite is not run in CI. Reproducing the 112 artifact tasks and 226 routing requests needs a Google CLI account or an environment key and runs on your own quota.
- Some references are long enough to be a real context cost if loaded wholesale. The entrypoints tell you to load one, and that discipline is on the operator.

## Related

- [codebase-design - Deep Module Design Vocabulary Setup](/hermes/skills/catalog/codebase-design-setup)
- [Simplify Code - Parallel Review & Cleanup Setup](/hermes/skills/catalog/simplify-code-setup)
- [Developer Kit - Java and TypeScript Skill Suite Setup](/hermes/skills/catalog/developer-kit-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the two or three skills that match your stack and leave the rest. The pack covers Bazel, FSD, Drizzle, Slack and Teams, and no single project needs all five; every loaded skill competes for the same routing decision.
- Load the entrypoint, then ask for one reference by name. "Use postgres-drizzle, read PERFORMANCE.md, diagnose this plan" gets a focused answer, while "use postgres-drizzle" invites the agent to pull the whole reference set into context.
- Keep the exclusion clauses in your prompt. Every description ends with what the skill is not for, and a request that says "this is a local fix, do not migrate the architecture" lands far better than relying on the skill to infer it.
- Pair `clean-ddd-hexagonal` with a code-review pass rather than a rewrite. The skill's output is a boundary judgement and a tradeoff; asking for the patch at the same time muddles the two artifacts.
- Run `scripts/validate_skills.py` after any edit to a copied skill. It catches broken reference links, which is the failure mode that turns a two-hundred-line reference set into an entrypoint making promises it cannot keep.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
