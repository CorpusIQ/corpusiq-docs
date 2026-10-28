---
title: "Melodic Software Claude Code Plugins - Marketplace Setup"
description: "Melodic Software's Claude Code plugin marketplace: 5.3K combined installs across 200 listings. Architecture, review and harness skills with hooks."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/melodic-claude-code-plugins-setup/"
robots: "index,follow"
last_updated: "2026-10-27"
tags: ["hermes skill", "agent skill", "skill setup", "claude code plugins", "architecture documentation", "developer harness"]
---

# Melodic Software Claude Code Plugins - Setup Guide

**Source:** [melodic-software/claude-code-plugins](https://www.skills.sh/melodic-software/claude-code-plugins) via skills.sh - 5.3K combined installs across 200 indexed listings; snapshot 2026-10-27 (Oct 27 evening sweep)

**GitHub:** [melodic-software/claude-code-plugins](https://github.com/melodic-software/claude-code-plugins) - 28 stars, MIT, branch main, 387 `SKILL.md` files in a plugin marketplace layout, `plugins/<plugin>/skills/<skill>/SKILL.md`, with 91 plugins declared in `.claude-plugin/marketplace.json`

**Category:** Agent harness engineering, architecture documentation and engineering practice

**Quality Tier:** 🟡 Beta - 28 stars and a top listing at 259 installs, on a large tree: 91 plugins, 387 skill files, and an install index that does not line up with the directories

This is Melodic Software's public Claude Code plugin marketplace: skills, hooks and agents written to work in any repository and to be customized by the consumer without editing the plugin itself. `.claude-plugin/marketplace.json` declares 91 plugins across 18 categories (development 14, claude-code 14, quality 10, maintenance 9, design 8, discovery 6, testing 6, presentation 4, personal 4, and nine smaller groups). Each plugin is a bundle rather than a single skill: 377 skill directories sit under `plugins/*/skills/*`, a median of 3 per plugin and 19 in `harness-ops`, 29 plugins also ship a `hooks/hooks.json`, and 1,858 shell scripts live under `plugins/`. The shared shell helpers have one source of truth in `lib/`, and the README states that the vendored copies under `plugins/` are synced by `scripts/sync-<helper>.sh` with CI rejecting drift, so a copy is never edited in place.

The install index and the tree describe different shapes of the same project, and that gap is the first thing to understand. skills.sh lists 200 flat skill names, `design-thinking` at the top with 259 installs. The current tree has no directory named `design-thinking`, `plantuml-syntax`, `architecture-documentation` or `resume-optimization`, and 59 of the 60 names in the install dump match neither a plugin directory nor a skill directory in the clone; `event-storming` is the only one that matches a plugin. What the tree does ship is verb-named skills inside plugin bundles: `/architecture:map-context`, `/testing:audit`, `/verification:confirm`, `/source-control:commit`. Read the install counts as a signal about which subjects people search for, and the tree as what can actually be installed.

## Installation

The README documents a marketplace install inside Claude Code. Add the marketplace once, then install the plugins you want by name:

```text
/plugin marketplace add melodic-software/claude-code-plugins
/plugin install architecture@melodic-software
/plugin marketplace update melodic-software
```

Two behaviours in the README matter before you rely on an installed copy. An install from GitHub is a copy keyed on the plugin's semver `version`, not the commit, so a change reaches it only when a release raises that version, and until then `plugin update` reports "already at the latest version". A marketplace added from a local clone loads each plugin in place, so edits apply at the next session or after `/reload-plugins`. The README also notes that 38 of the 91 plugins set `defaultEnabled: false` and install disabled until the user opts in with `/plugin enable`; most domain, personal, harness-maintenance and external-service plugins carry the flag.

Hermes has no plugin marketplace, so the install path is the skill directory. The pack's install note is a shallow clone plus a copy of the directory you need:

```bash
git clone --depth 1 https://github.com/melodic-software/claude-code-plugins.git
cp -R claude-code-plugins/plugins/architecture/skills/map-context ~/.hermes/skills/
```

That copy carries the `SKILL.md` and the `context/`, `reference/` and `templates/` files beside it, which is what the skill reads at run time. It does not carry the plugin's hooks, its namespaced slash commands or its `userConfig` options, because those are Claude Code plugin-runtime features.

## What It Provides

The table is the install snapshot: the 22 highest indexed listings, with the pack's exact counts.

| Skill | Installs | Use For |
|---|---|---|
| design-thinking | 259 | Structured design-thinking exercises for framing a problem, its users and its constraints before a solution is chosen. |
| plantuml-syntax | 204 | PlantUML diagram syntax: sequence, class, component and activity diagrams written as text instead of drawn. |
| architecture-documentation | 180 | Architecture documentation that stays readable and current, describing a system rather than restating it. |
| system-prompt-engineering | 170 | Authoring and revising system prompts: structure, constraints, instruction ordering and the tone a model inherits. |
| system-diagnostics | 163 | Diagnosing a running system from its symptoms: logs, process state and configuration read in a deliberate order. |
| data-modeling | 137 | Data modelling: entities, relationships, keys and normalisation decisions, expressed as a schema or an ERD. |
| resume-optimization | 127 | Rewriting a resume against a target role: evidence, ordering, and the phrasing that survives an automated screen. |
| state-machine-design | 101 | Designing state machines: states, transitions, guards and the events that drive them. |
| modular-architecture | 96 | Cutting a codebase into modules with explicit boundaries, published contracts and no shared internals. |
| swot-pestle-analysis | 94 | SWOT and PESTLE analysis: internal strengths and weaknesses against external political, economic, social, technological, legal and environmental factors. |
| cryptography | 88 | Applied cryptography choices: which primitive for which job, key handling, and the failure modes that quietly void an implementation. |
| uml-modeling | 87 | UML modelling: which diagram answers which question, and how to keep a model small enough to stay true. |
| gemini-token-optimization | 83 | Reducing token spend on Gemini: prompt structure, caching and context trimming that keep the answer intact. |
| career-strategy | 82 | Career planning: target roles, skill gaps, and the sequence of moves that closes them. |
| process-modeling | 62 | Process modelling: current-state and target-state flows, handoffs, and where a process actually loses time. |
| business-rules-analysis | 58 | Extracting business rules from prose and code into explicit, testable conditions. |
| technical-presentations | 54 | Building a technical presentation: the argument first, the slides second, and depth control for a mixed audience. |
| estimation | 54 | Estimation: decomposition, ranges instead of single numbers, and the assumptions that make an estimate falsifiable. |
| event-storming | 53 | EventStorming: domain events, commands, policies and hotspots, from big-picture discovery down to design level. |
| arc42-documentation | 51 | arc42 as the section skeleton for architecture documentation, with the content each section owes its reader. |
| document-extraction | 45 | Extracting structured content from documents: layout, tables, and the parts a naive parser loses. |
| resilience-patterns | 44 | Resilience patterns: timeouts, retries with backoff, circuit breakers and bulkheads, and the failure each one trades away. |

The dump itemises 38 further listings from 42 down to 22 installs. Read as subjects rather than as a ranking, that tail is architecture and design documentation (`c4-documentation` 31, `taxonomy-architecture` 29, `domain-storytelling` 26, `swimlane-visualization` 22, plus the PlantUML, UML and arc42 rows above); systems engineering (`rate-limiting-patterns` 30, `ml-inference-optimization` 30, `test-case-design` 29, `rag-architecture` 28, `latency-optimization` 24, `asyncapi-design` 23, plus `resilience-patterns` and `state-machine-design` above); career and business analysis (`interview-skills` 37, `mentoring-developers` 33, `value-stream-mapping` 27, `journey-mapping` 27, `promotion-preparation` 26, `gap-analysis` 26, `risk-analysis` 25, `decision-analysis` 25, `business-model-canvas` 23, `benchmarking` 23, plus the resume, career, SWOT and estimation rows above); and security and compliance (`gdpr-compliance` 34, `container-security` 33, `api-security` 32, `secure-coding` 24, `hipaa-compliance` 24). The 24 to 22 install band holds 14 listings, among them `developer-visibility`, `context-audit`, `ai-writing-assistant`, `ai-tools`, `acceptance-criteria-authoring`, `user-story-mapping` and `capability-mapping`. The other 140 of the 200 indexed listings carry no count in this snapshot at all.

## Why This Matters for Hermes Agents

Hermes reads skills as instruction, so the marketplace's stated design goal, repo-agnostic skills that the consumer customizes rather than edits, is close to what a shared skills folder needs; the `architecture` skill resolves the project root and reads tracked configuration instead of assuming the author's setup. The hooks are the part a skill-only collection cannot match: 29 plugins ship `hooks/hooks.json`, and the events they bind are the ones that decide whether a rule holds, with `SessionStart` in 28 manifests, `Stop` in 11, `PreToolUse` in 8 and `PostToolBatch` in 6, plus input, compaction and permission events. A rule in a hook is run by the harness; a rule in prose is a suggestion the model may skip.

The verification and audit families are written to fail closed, which suits unattended work. `/verification:confirm` runs a mechanical build, test and lint gate before it will state a verdict, `/testing:audit` looks for tests that cannot fail and can gate on the result, `/code-metrics` reports measures only from collectors already installed and issues no verdict, and `/mcp-tools:audit-posture` inventories configured MCP servers without starting any of them. For a loop that runs without a person watching, that posture is worth more than breadth.

The cost is volume. Ninety-one plugins with a median of three skills each, and description fields long enough to act as routing tables, are exactly the kind of surface that eats a context window if you install a category because it exists. Install the bundle that matches the task and let the plugin's own `setup` skill record the project conventions.

Finally, the index-to-tree gap is an operational trap worth naming. An agent that installs by listing name writes a copy step or a raw URL for a directory that does not exist, and the failure looks like a broken repository rather than a stale index. Resolve the plugin first, then the skill inside it.

## Usage

| You say | What happens |
|---|---|
| "Chart how this service talks to everything else" | /architecture:map-context reads tracked configuration for actors and external systems, redacts credentials, and writes a C4 system context with a LikeC4 or C4-PlantUML dialect option. |
| "Why was this built this way" | /discovery:trace-intent reconstructs the decision from evidence outside the code and persists INTENT.md for the next session. |
| "Are these tests actually able to fail" | /testing:audit looks for tests that cannot fail and reports, gates or persists the findings. |
| "Prove this change did what it was supposed to" | /verification:confirm clears the build, test and lint prerequisite gate, then matches intent, evidence and verdict, detecting the criterion from the change type. |
| "Which MCP servers does this project run, and are they pinned" | /mcp-tools:audit-posture inventories the servers your configuration runs and flags floating package versions, without starting a server. |
| "Commit this following our convention" | /source-control:commit resolves the repo's convention from its own config, stages surgically and adds the Co-authored-by trailer. |
| "Is node and jq even available for the context guard" | /context-guard:check reports whether node and jq resolve and whether the mod can load, and never installs anything. |

## Verification

Probe the path you plan to copy before you copy it. These five returned 200 on 2026-10-27:

```bash
for p in plugins/architecture/skills/map-context/SKILL.md \
         plugins/docs-hygiene/skills/write-for-agents/SKILL.md \
         plugins/harness-config/skills/audit-permission-grants/SKILL.md \
         plugins/context-guard/hooks/hooks.json \
         plugins/miro/.mcp.json; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/melodic-software/claude-code-plugins/main/$p"
done
```

Read the two that run code before installing anything that uses them: the context-guard hook manifest and the miro MCP server definition.

- https://raw.githubusercontent.com/melodic-software/claude-code-plugins/main/plugins/context-guard/hooks/hooks.json
- https://raw.githubusercontent.com/melodic-software/claude-code-plugins/main/plugins/miro/.mcp.json

The same probe against a listing name is the fastest way to see the index gap for yourself. `plugins/design-thinking/skills/setup/SKILL.md` returned 404 on 2026-10-27, while `plugins/architecture/skills/map-context/SKILL.md` returned 200.

After a copy, each skill appears as one folder in `~/.hermes/skills/`, and the folder name is what the agent matches on. In Claude Code, `/plugin` lists installed plugins and their enabled state, and `/plugin marketplace update melodic-software` refreshes the catalogue.

## Security

skills.sh verdicts were not sampled for this fire, so every cell below reads Not checked. Open each skill's security page on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| design-thinking | Not checked | Not checked | Not checked |
| plantuml-syntax | Not checked | Not checked | Not checked |
| architecture-documentation | Not checked | Not checked | Not checked |
| system-prompt-engineering | Not checked | Not checked | Not checked |
| system-diagnostics | Not checked | Not checked | Not checked |
| data-modeling | Not checked | Not checked | Not checked |
| resume-optimization | Not checked | Not checked | Not checked |
| state-machine-design | Not checked | Not checked | Not checked |

The rows below 100 installs are omitted from that table; check any you intend to use.

The real risk profile here is executable surface, not markdown. A hook is a command the harness runs, and this repository ships 29 hook manifests over 1,858 shell scripts: `SessionStart` in 28 of them fires on every session start, `PreToolUse` in 8 intercepts tool calls, and `PostToolBatch` in 6 runs after a batch of edits. Install one plugin, read its `hooks/hooks.json`, and know what each command does before enabling it.

Six formatter plugins rewrite tracked files at the batch boundary (`markdown-format`, `bash-format`, `biome-format`, `ruff-format`, `go-format`, `eol-normalizer`), with `powershell-format`, `typos-format` and `actionlint` running at `Stop` and `SessionStart`. Each is gated on a config file the consuming repo owns, such as `.markdownlint-cli2.jsonc`, `biome.json`, a Ruff config, `.editorconfig` or a `PSScriptAnalyzerSettings.psd1`, so an unconfigured repo is left alone. Configured repos get edits the agent did not ask for, which is fine when work is committed and confusing when it is not.

One plugin ships a server. `plugins/miro/.mcp.json` launches a local stdio server with `node ${CLAUDE_PLUGIN_ROOT}/server/src/launch.ts` and passes `MIRO_API_TOKEN` from `user_config`; the catalog states it installs its pinned npm dependencies on first launch, needs Node 24 or newer, installs disabled, and starts without a token until you set one. `context7`, `firecrawl` and `dometrain` reach external services through a CLI or a server you configure yourself, and `dometrain` ships no server at all.

Two posture notes. Freshness is version-keyed, so an installed copy is only as current as its last semver release while a local-clone marketplace runs whatever is checked out; pin releases for anything unattended. And the repository's own eval fixtures include a case named `ob-hooks-label-is-data`, which tests that hook output is treated as data. Keep that boundary in Hermes: hook output and skill prose inform a decision, they do not authorise one.

## Limitations

- Snapshot data, verified 2026-10-27: 5,328 combined installs across 200 indexed listings; 28 GitHub stars; MIT; branch main. Counts drift over time.
- Counts and directories do not reconcile: 387 `SKILL.md` files in the clone (377 outside eval fixtures) against 200 indexed listings, about 1.9 skill files per listing, and 59 of the 60 names in the install dump match neither a plugin directory nor a skill directory. Only `event-storming` matches.
- The distribution is one long low tail. The top listing is 259 installs, and 192 of the 200 listings sit below 100, so an install count here is a signal about a subject people search for, not evidence that a skill is good.
- The clone is a single-commit shallow checkout, so the index-to-tree drift cannot be dated from history. This guide reports the drift as it stands on 2026-10-27 rather than guessing which names were retired.
- Host assumptions are real: node and jq for the context and guard plugins, Node 24 or newer plus npm for the miro server, PowerShell for the Windows paths. The README states that Windows Git Bash is not a supported host for the full `scripts/affected-tests.sh --run` gate.
- The plugin path is a Claude Code feature. Hermes gets the skill directories and their reference files, not the namespaced slash commands, the hooks or the `userConfig` options.

## Related

- [Knowledge Work Plugins - Anthropic Productivity Setup](/hermes/skills/catalog/knowledge-work-plugins-setup)
- [Luxor Claude Marketplace Skills Setup](/hermes/skills/catalog/luxor-claude-marketplace-setup)
- [Compound Engineering Plugin - Every Inc Workflow Suite Setup](/hermes/skills/catalog/compound-engineering-plugin-setup)
- [Bencium Marketplace - Design & Product Skills Suite Setup](/hermes/skills/catalog/bencium-marketplace-setup)

## Pro Tips

- Install by plugin, not by listing name. Resolve `plugins/<plugin>/skills/<skill>/SKILL.md` with a curl probe first, because most of the top listing names have no directory in the tree.
- Start with the three plugins that gate rather than generate: `verification`, `testing` and `source-control`. They produce evidence about work you were going to do anyway, so they pay for their context immediately.
- Leave `defaultEnabled: false` plugins disabled and enable one per session until you have read its `hooks/hooks.json`. The install is cheap, the hook is not.
- Use a local clone marketplace while you are still deciding. Edits and fixes apply at the next session or after `/reload-plugins`, instead of waiting for a semver bump that may never come.
- Run the formatter plugins on a clean working tree the first time. They rewrite files on the batch boundary, and a dirty tree turns that into an unreadable diff.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
