---
title: "Understand Anything - Code to Knowledge Graph Setup"
description: "egonex-ai/understand-anything: 35.0K combined installs. MIT skills that turn a codebase into a knowledge graph, dashboard and onboarding tour."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/understand-anything-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup", "codebase analysis", "knowledge graph", "onboarding", "code review"]
---

# Understand Anything - Setup Guide

**Source:** [egonex-ai/understand-anything](https://www.skills.sh/egonex-ai/understand-anything) via skills.sh - 35.0K combined installs across 9 indexed listings; first documented 2026-11-03 (nightly sweep)

**GitHub:** [egonex-ai/understand-anything](https://github.com/egonex-ai/understand-anything) - 90,113 stars, MIT, branch main, last pushed 2026-10-26; nine skill directories under `understand-anything-plugin/skills/`, five of them a bare `SKILL.md` and four shipping Node or Python helpers (18 helper scripts in total), plus a TypeScript plugin package with a `hooks/` directory and a `packages/` workspace

**Category:** Codebase understanding for agents: structural knowledge graphs, an interactive dashboard, diffs, domain flows, onboarding and Figma design graphs

**Quality Tier:** 🟡 Yellow - Snyk fails the sampled `understand-dashboard` listing while Gen Agent Trust Hub and Socket pass all three sampled skills, and the repository does ship a LICENSE file (MIT)

Understand Anything is published by Egonex AI and built around a blunt premise from its README: the value of a graph is not that it impresses you with complexity, it is that it teaches you how the code fits together. The plugin analyses a project with a multi agent pipeline, writes a knowledge graph of every file, function, class and dependency, and serves an interactive dashboard for exploring it.

The pipeline splits work between a deterministic parser and a model. Tree-sitter extracts the structural facts (imports, exports, definitions, call sites, inheritance), pre-resolved into an `importMap`, so the same code always yields the same edges. LLM agents add what parsers cannot see: plain English summaries, architectural layer assignments, business domain mapping, guided tours and language concept callouts. `/understand` orchestrates five agents (project scanner, file analyser, architecture analyser, tour builder, graph reviewer), `/understand-domain` adds a sixth and `/understand-knowledge` a seventh. File analysers run in parallel, up to five concurrent workers and 20 to 30 files per batch.

## Installation

There are three documented routes, and they install different things. Claude Code gets the native plugin:

```bash
/plugin marketplace add Egonex-AI/Understand-Anything
/plugin install understand-anything
```

Every other platform uses the one-line installer, which accepts a platform argument to skip the prompt. The README lists `hermes` among the supported values:

```bash
curl -fsSL https://raw.githubusercontent.com/Egonex-AI/Understand-Anything/main/install.sh | bash -s hermes
```

That installer clones the repository to `~/.understand-anything/repo` and creates the right link for the chosen platform, so it needs network access and a git binary. It also carries `--update` and `--uninstall <platform>` flags, and on Windows the equivalent is `install.ps1` through `iwr -useb | iex`. Cursor and VS Code with Copilot auto-discover the plugin from `.cursor-plugin/plugin.json` and `.copilot-plugin/plugin.json` once the repository is cloned, with no installer run at all.

The skills.sh listing documents the third route, which installs the skill text without the plugin wrapper:

```bash
npx skills add egonex-ai/understand-anything
```

For a Hermes profile, check where the installer puts the link before trusting it. The platform table in `install.sh` maps `hermes` to `$HOME/.hermes/skills` in folder style, and this profile reads `/home/hermes/.hermes/profiles/corpusiq/skills/`, so pass the platform, then copy or link the folder yourself:

```bash
git clone --depth 1 https://github.com/Egonex-AI/Understand-Anything.git /tmp/ua
cp -r /tmp/ua/understand-anything-plugin/skills/understand ~/.hermes/profiles/corpusiq/skills/
```

Copy individual skill directories rather than all nine at once. Each one is a command with its own argument hint, and the routing layer only needs the ones your project will actually use. Copy whole directories when you do: `understand` alone carries 15 helper files (Node scanners, batch mergers, a Python graph merger) that its instructions invoke by path.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| understand | 5,574 | Analysing a codebase into an interactive knowledge graph covering architecture, components and relationships. Accepts a path, a subdirectory, `--full`, `--auto-update`, `--review` and `--language`. |
| understand-explain | 4,058 | A deep dive explanation of one file, function or module, grounded in the graph rather than in a fresh read of the source. |
| understand-dashboard | 4,040 | Launching the interactive web dashboard that visualises the knowledge graph: pan, zoom, search, colour by architectural layer, click a node for code and relationships. |
| understand-chat | 3,977 | Asking questions about a codebase against its graph, such as how a payment flow works, instead of re-reading files per question. |
| understand-onboard | 3,971 | Generating an onboarding guide for new team members joining a project, built from the graph and its guided tours. |
| understand-diff | 3,828 | Analysing git diffs or pull requests to see what changed, which components are affected, and where the risk sits. |
| understand-domain | 3,788 | Extracting business domain knowledge (domains, flows, process steps) into an interactive flow graph, either standalone from a lightweight scan or derived from an existing graph. |
| understand-knowledge | 3,684 | Analysing a Karpathy-pattern LLM wiki knowledge base into a graph with entity extraction, implicit relationships and topic clustering. |
| understand-figma | 2,069 | Analysing a Figma file through the Figma REST API into a design graph of pages, screens, components, component sets, instances and design tokens, rendered with a design kind dashboard. |

No indexed listings fall below the threshold; all 9 appear above.

The graph is written to `.ua/knowledge-graph.json`, and projects that already carry a `.understand-anything/` directory keep using it, so an upgrade does not require a migration. Language choice is persisted: `/understand --language zh` switches node summaries and dashboard labels, and the first run detects the conversation language and asks before generating anything other than English. The README is candid that the initial `/understand` on a large project can consume a significant number of tokens, recommends a subscription or a local model for that first pass, and notes that later runs are incremental because fingerprint based change detection only re-analyses changed files.

## Why This Matters for Hermes Agents

The first question an agent asks in an unfamiliar repository is which files matter, and the usual answer is a grep followed by hope. A graph replaces that with a structural index: an agent can look up a symbol's relationships, walk from a route to its handler to its data layer, and skip the files that only look relevant. That is the difference between a review that reads the change and a review that reads the change in context.

The deterministic and semantic split is what makes the output trustworthy. Structural edges come from tree-sitter and are reproducible, so a wrong edge is a bug rather than a hallucination, while the semantic layer carries summaries and layer assignments that are clearly model output. When an agent reports "this change touches the payment domain", the claim has a provenance you can inspect.

The diff and domain skills are the ones with day to day leverage in a Hermes workflow. `understand-diff` maps a pull request onto affected components and risk before review starts, and `understand-domain` turns the same code into a business flow graph, which is the artefact a non engineer stakeholder can actually read. For onboarding, `understand-onboard` plus the guided tours answers the "where do I start" question from the graph rather than from a README that may be stale.

## Usage

| You say | What happens |
|---|---|
| "Analyse this repo and tell me how it is structured" | `/understand` runs the scanner, file analysers and architecture analyser, then writes `.ua/knowledge-graph.json` and a summary of layers and components. |
| "Show me a picture of this codebase" | `/understand-dashboard` starts the local dashboard on the existing graph, colour coded by layer and searchable by symbol. |
| "How does the checkout flow work here?" | `/understand-chat` answers from the graph, tracing the flow across files instead of reading them one at a time. |
| "What does this pull request actually touch?" | `/understand-diff` maps the diff onto affected components and names the risk areas. |
| "Explain src/auth/login.ts to me" | `/understand-explain` gives a deep dive on that file grounded in its graph node, callers and dependencies. |
| "Write an onboarding guide for the new hire" | `/understand-onboard` generates a tour driven guide from the graph, covering entry points, layers and key flows. |
| "Turn this Figma file into a component map" | `/understand-figma` reads the file through the Figma REST API and produces a design graph with pages, screens, components and tokens. |

## Verification

The raw paths below returned 200 on branch main on 2026-11-03:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/Egonex-AI/Understand-Anything/main/understand-anything-plugin/skills/understand/SKILL.md
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/Egonex-AI/Understand-Anything/main/install.sh
```

After a clone, confirm the nine skills and read the frontmatter the runtime routes on:

```bash
git clone --depth 1 https://github.com/Egonex-AI/Understand-Anything.git /tmp/ua
ls -d /tmp/ua/understand-anything-plugin/skills/*/ | wc -l
head -4 /tmp/ua/understand-anything-plugin/skills/understand/SKILL.md
grep -n 'understand-dashboard\|\.ua/knowledge-graph' /tmp/ua/README.md | head -5
```

The count should print 9, and `head` should show `name: understand` with an `argument-hint` listing the path and flag options. Once installed, the real check is the artefact:

```bash
ls .ua/knowledge-graph.json
python3 -c "import json;d=json.load(open('.ua/knowledge-graph.json'));print(list(d)[:6])"
```

A graph file that parses and carries nodes and edges is the proof the pipeline ran. If `/understand` reports success and no file appears, check the data directory name, because a pre-existing `.understand-anything/` directory takes precedence over `.ua/`.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-03) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| understand | Pass | Pass | Pass |
| understand-explain | Pass | Pass | Pass |
| understand-dashboard | Pass | Pass | Fail |

This is not a Markdown only install, and the fail on `understand-dashboard` is worth understanding before you wire it up. The plugin ships a `hooks/hooks.json` that registers a `PostToolUse` hook matched to `Bash`, which runs `node ${CLAUDE_PLUGIN_ROOT}/hooks/post-tool-use-auto-update.mjs` after shell commands, plus a `SessionStart` hook that inspects `.ua/meta.json` and instructs the agent to refresh a stale graph. That second hook is written to tell the model to update the graph without asking for confirmation. Read both files in `understand-anything-plugin/hooks/` before installing, and keep `autoUpdate` off in `.ua/config.json` unless you want graph rebuilds triggered by normal shell use.

The installer is a curl-pipe-to-bash script. It clones a repository and creates symlinks under your home directory, which is a broad set of powers for a one-liner; read `install.sh` first, as it is 321 lines of plain bash with an explicit platform table.

The skills are not inert either. `understand` runs a tree-sitter scan through `scan-project.mjs` and `extract-structure.mjs`, then merges batches with `merge-batch-graphs.py`; `understand-domain`, `understand-knowledge` and `understand-figma` ship their own Python and Node helpers. All of it executes locally against your repository, and none of it asks for credentials except the Figma token. On a codebase with secrets in the tree, remember that any scanned content can end up inside the graph and in whatever the model provider receives.

Data leaves the machine in two places. `/understand-figma` makes outbound calls to `api.figma.com` with a `FIGMA_TOKEN` read from the environment and sent only in the `X-Figma-Token` header, while the README states the rest of the pipeline is local to the model provider you already configured. If you point it at a local model, the code does not leave the host.

## Limitations

- Snapshot data, verified 2026-11-03: 34,989 combined installs across 9 indexed listings; 90,113 GitHub stars; MIT; last pushed 2026-10-26. Counts drift over time.
- The one-line installer's `hermes` row targets `$HOME/.hermes/skills` in folder style. A profile based Hermes install, including this catalogue's own profile, reads its own skills directory, so the link has to be placed or copied by hand.
- The first `/understand` run on a large codebase is expensive in tokens. The README says so directly and recommends a subscription or a local model for initialisation; only later runs are incremental.
- The graph pipeline runs on Node helpers, and the dashboard and Figma skill add a pnpm 10 build with a Vite app. A host without a modern JS toolchain gets no graph at all rather than a partial one, so check `node --version` before the first run.
- `understand-figma` is the one skill that is not offline: it needs a Figma personal access token and reaches `api.figma.com` on every run.
- The plugin registers hooks that execute on shell commands and at session start. That behaviour is part of the install, not an opt-in, and it is the most likely reason the dashboard listing failed the Snyk audit.

## Related

- [codebase-design - Deep Module Design Vocabulary Setup](/hermes/skills/catalog/codebase-design-setup)
- [shadcn Improve - Codebase Audit to Plan Setup](/hermes/skills/catalog/shadcn-improve-setup)
- [Qodo Skills - Code Review and Standards Suite](/hermes/skills/catalog/qodo-skills-setup)
- [Fallow Skills - Codebase Intelligence for TS and JS Setup](/hermes/skills/catalog/fallow-rs-fallow-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `/understand` on a subdirectory first on a monorepo. The command accepts a path, and a scoped graph is both cheaper and more useful than a whole tree with shallow summaries.
- Check `.ua/config.json` for `autoUpdate` before leaving an agent unattended. The hook will otherwise rebuild the graph after shell commands, which is surprising in a long session.
- Use `/understand-diff` as the first step of a review, not the last. It names affected components before you read the patch, which changes what you look for.
- Try the hosted live demo on understand-anything.com before installing if you only want to see the dashboard shape. It runs the same interface without spending tokens on your repository.
- Re-run `/understand` after a large merge rather than trusting a stale graph. Incremental runs are cheap, and a graph that disagrees with the working tree is worse than no graph.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
