---
title: "Loom Agent Orchestrator - Rust Swarm of Claude Code Agents"
description: "cosmix/loom: 2.5K combined installs. A Rust-based agent orchestrator running a swarm of Claude Code sessions to build software."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/loom-agent-orchestrator-setup/"
robots: "index,follow"
last_updated: "2026-11-28"
tags: ["hermes skill", "agent skill", "skill setup", "agent orchestration", "claude code", "rust"]
---

# Loom Agent Orchestrator - Setup Guide

**Source:** [cosmix/loom](https://www.skills.sh/cosmix/loom) via skills.sh - 2.5K combined installs across 90 indexed listings; first seen Nov 28 2026 (morning sweep)

**GitHub:** [cosmix/loom](https://github.com/cosmix/loom) - 66 stars, MIT license, branch main, last pushed 2026-11-26, not archived; skills live under `skills/<name>/SKILL.md` (75 `loom-` prefixed skills), with agents under `agents/` and Codex assets under `codex/skills/`.

**Category:** Agent orchestration - a Rust orchestrator that runs a swarm of Claude Code (and optionally Codex) sessions across isolated git worktrees, with planning, verification, knowledge capture and sandboxing skills

**Quality Tier:** 🟠 Orange - 2 Gen Agent Trust Hub Fails (logging-observability, background-jobs) and 3 Snyk Warns (prometheus, grafana, feature-flags) across 20 sampled verdicts.

cosmix/loom is a Rust-based agent orchestrator that runs a swarm of Claude Code (and optionally Codex) sessions across isolated git worktrees to build software. You design the system and write a plan; loom implements it, verifies each stage's work independently, merges stages progressively, and distills what it learned into a tiered knowledge base in your repo. A terminal or browser dashboard lets you watch and steer any session live.

The skills.sh index lists 90 listings under cosmix/loom for a combined 2.5K installs, with every listing well under 500 installs. The repo ships 75 `loom-` prefixed skills (10 core, always loaded, plus 65 more loaded on demand), while 15 generic names in the index (prometheus, ci-cd, grafana and similar) have no counterpart in the current tree. The skills are domain knowledge modules covering observability, testing, security, language and infrastructure guidance that loom's agents load while building software.

## Installation

Loom installs through a signed release binary for Linux x86_64 and macOS Apple Silicon; every other platform builds from source. Prerequisites are `git` (2.40 or newer), the `claude` CLI, `jq`, `minisign` and `tmux`; `rg` and `fd` are recommended, and the `codex` CLI is optional.

```bash
curl -fsSL https://raw.githubusercontent.com/cosmix/loom/main/install.sh | bash
```

The installer downloads the signed binary to `~/.local/bin/loom` and installs loom's agents, skills, commands, hooks and orchestration rules into `~/.claude/` and `~/.codex/`, verifying the release against a pinned public key before executing it. Build from source instead with:

```bash
git clone https://github.com/cosmix/loom.git
cd loom
bash ./dev-install.sh
```

`install.sh` takes an optional `--skills core|all` flag (default `core`): `core` installs a small set of always-loaded core skills to `~/.claude/skills/` and catalogs the rest under `~/.claude/loom-skill-catalog/` for on-demand loading; `all` installs every loom skill directly to `~/.claude/skills/`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| prometheus | 64 | Prometheus monitoring and alerting for cloud-native observability. |
| event-driven | 60 | Event-driven architecture: message queues, pub/sub, event sourcing, CQRS, sagas. |
| ci-cd | 60 | CI/CD pipeline design: testing, builds, deployment, security scanning. |
| grafana | 56 | Observability visualization with Grafana and the LGTM stack. |
| refactoring | 55 | Restructures existing code without changing behavior. |
| logging-observability | 55 | Logging and observability patterns: logs, traces, metrics. |
| background-jobs | 52 | Background job patterns. |
| data-validation | 50 | Schema validation, input sanitization, output encoding, type coercion. |
| testing | 46 | Unit, integration, e2e, security, infrastructure, data pipeline, and ML testing. |
| loom-ci-cd | 44 | Designs and implements CI/CD pipelines: testing, builds, deployment, security scanning. Not for: a loom stage/job. |
| karpenter | 44 | Karpenter Kubernetes node autoscaling. |
| feature-flags | 43 | Feature flag patterns. |
| auth | 42 | Authentication and authorization patterns. |
| loom-logging-observability | 39 | Logging and observability patterns for production systems: logs, traces, metrics. |
| loom-data-validation | 37 | Data validation: schema validation, input sanitization, output encoding, type coercion. |
| loom-prometheus | 36 | Prometheus monitoring and alerting for cloud-native observability. Not for: a loom orchestration job. |
| loom-refactoring | 35 | Restructures code for readability, maintainability, and performance without changing behavior. |
| loom-testing | 34 | Test implementation across unit, integration, e2e, security, infrastructure, data pipeline, and ML domains. |
| loom-grafana | 34 | Observability visualization with Grafana and the LGTM stack. |
| loom-event-driven | 31 | Event-driven architecture: message queues, pub/sub, event sourcing, CQRS, sagas. Not for: webhooks. |
| loom-feature-flags | 30 | Feature flag patterns for loom stages. |
| loom-docker | 30 | Docker patterns for loom stages. |
| loom-python | 28 | Python guidance for loom stages. |
| loom-karpenter | 28 | Karpenter Kubernetes node autoscaling guidance. |
| loom-background-jobs | 28 | Background job patterns for loom stages. |
| loom-test-strategy | 27 | Test strategy planning for loom stages. |
| loom-performance-testing | 27 | Performance testing guidance. |
| loom-kubernetes | 26 | Kubernetes patterns for loom stages. |
| loom-error-handling | 26 | Error handling patterns. |
| loom-e2e-testing | 26 | End-to-end testing guidance. |
| loom-dead-code-check | 26 | Detects dead code that nothing calls. |
| loom-data-visualization | 26 | Data visualization guidance. |
| loom-code-review | 26 | Code review guidance for loom stages. |
| loom-auth | 26 | Authentication and authorization patterns. |
| dead-code-check | 26 | Detects dead code that nothing calls. |
| before-after | 26 | Before/after change verification for code edits. |
| loom-webhooks | 25 | Webhook patterns for loom stages. |
| loom-typescript | 25 | TypeScript guidance for loom stages. |
| loom-technical-writing | 25 | Technical writing guidance. |
| loom-sql-optimization | 25 | SQL query optimization guidance. |
| loom-security-scan | 25 | Security scanning guidance. |
| loom-security-audit | 25 | Security audit guidance. |
| loom-rate-limiting | 25 | Rate limiting patterns. |
| loom-prompt-engineering | 25 | Prompt engineering guidance. |
| loom-git-workflow | 25 | Git workflow guidance. |
| loom-debugging | 25 | Debugging guidance. |
| loom-caching | 25 | Caching patterns. |
| loom-api-design | 25 | API design guidance. |
| loom-accessibility | 25 | Accessibility guidance. |
| loom-wiring-test | 24 | Checks that new code is wired in and reachable. |
| loom-usage | 24 | Usage and token accounting guidance. |
| loom-threat-model | 24 | Threat modeling guidance. |
| loom-terraform | 24 | Terraform patterns for loom stages. |
| loom-serialization | 24 | Serialization guidance. |
| loom-react | 24 | React guidance for loom stages. |
| loom-model-evaluation | 24 | Model evaluation guidance. |
| loom-documentation | 24 | Documentation writing guidance. |
| loom-diagramming | 24 | Diagramming guidance. |
| loom-dependency-scan | 24 | Dependency scanning guidance. |
| loom-database-design | 24 | Database design guidance. |
| loom-crossplane | 24 | Crossplane patterns for loom stages. |
| loom-code-migration | 24 | Code migration guidance. |
| loom-before-after | 24 | Before/after change verification for code edits. |
| loom-api-documentation | 24 | API documentation guidance. |
| wiring-test | 24 | Checks that new code is wired in and reachable. |
| loom-search | 23 | Search guidance for loom stages. |
| loom-rust | 23 | Rust guidance for loom stages. |
| loom-plan-writer | 23 | Writes loom plan files from a feature description. |
| loom-md-tables | 23 | Markdown table generation guidance. |
| loom-kustomize | 23 | Kustomize patterns for loom stages. |
| loom-istio | 23 | Istio service mesh patterns. |
| loom-i18n | 23 | Internationalization guidance. |
| loom-golang | 23 | Go guidance for loom stages. |
| loom-fluxcd | 23 | FluxCD GitOps patterns. |
| loom-concurrency | 23 | Concurrency guidance. |
| loom-argocd | 23 | Argo CD GitOps patterns. |
| loom-java | 17 | Java guidance for loom stages. |
| loom-ruby | 16 | Ruby guidance for loom stages. |
| loom-kotlin | 16 | Kotlin guidance for loom stages. |
| loom-javascript | 16 | JavaScript guidance for loom stages. |
| loom-swift | 15 | Swift guidance for loom stages. |
| loom-skills | 15 | Guidance for authoring loom skills. |
| loom-scala | 15 | Scala guidance for loom stages. |
| loom-php | 15 | PHP guidance for loom stages. |
| loom-orchestration | 15 | Orchestration patterns for loom stages. |
| loom-elixir | 15 | Elixir guidance for loom stages. |
| loom-dart | 15 | Dart guidance for loom stages. |
| loom-csharp | 15 | C# guidance for loom stages. |
| loom-cpp | 15 | C++ guidance for loom stages. |
| loom-c | 15 | C guidance for loom stages. |

The full 90-listing index is shown above because no listing reaches 500 installs (prometheus leads at 64). The index mixes 15 generic names (24 to 64 installs) with 75 `loom-` prefixed skills; only the prefixed skills live in the repo's `skills/` tree, as 10 always-loaded core skills plus 65 on-demand catalog entries.

## Why This Matters for Hermes Agents

Loom is a production-scale reference for orchestrating many coding agents against one plan, and its skill layer is the part most relevant to Hermes builders. It splits skills into a small always-loaded core and a larger on-demand catalog, loading only what a stage needs, which is a clean pattern for a skill router that must keep per-session context small.

The verification model is instructive: implementer sessions do not self-report success; loom runs each stage's acceptance criteria itself and inspects the tree for stubs, unwired code, and dead code. That separation of writing from checking is worth copying into any agent harness.

The deterministic guardrails are equally notable: commit discipline, worktree boundaries, and subagent limits fire from shell hooks, so they hold whatever the model intends. The same principle applies to Hermes skill and hook design.

Finally, the knowledge system (per-session memory distilled into a tiered, versioned markdown base) shows how an agent team can accumulate durable context across runs without re-reading everything each time.

## Usage

| You say | What happens |
|---|---|
| "Install loom on this machine" | Runs the install.sh curl command, installing the CLI plus agents, skills, hooks and orchestration rules. |
| "Plan a new feature" | `loom plan` opens the Feature Planner; a planning session writes a vision, product spec, metaplan and plans. |
| "Write the plan in Claude Code" | The `/loom-plan-writer` skill drafts `doc/plans/PLAN-<name>.md`. |
| "Validate this plan before running it" | `loom plan verify doc/plans/PLAN-<name>.md` checks schema, fields, duplicate IDs and path safety. |
| "Run the plan" | `loom init` parses the plan and wires hooks, then `loom run` starts the daemon and orchestrator. |
| "Watch the run" | `loom status --live` shows the terminal dashboard; `loom status --web` serves the browser dashboard. |
| "Pressure-test the plan first" | `loom pressure` has Claude and Codex review the plan adversarially and harden it. |

## Verification

The cleanest pre-install check is to fetch a skill's SKILL.md directly and read its frontmatter. Skills live at `skills/<name>/SKILL.md` on branch main:

```bash
curl -sL https://raw.githubusercontent.com/cosmix/loom/main/skills/loom-ci-cd/SKILL.md
```

After installing, confirm the CLI and the skill layout:

```bash
ls ~/.local/bin/loom
ls ~/.claude/skills/loom-*/
ls ~/.claude/loom-skill-catalog/loom-*/
```

The default install puts 10 core skills in `~/.claude/skills/` and catalogs the other 65 under `~/.claude/loom-skill-catalog/`; the `--skills all` flag installs every loom skill directly to `~/.claude/skills/`.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| prometheus | Pass | Pass | Warn |
| event-driven | Pass | Pass | Pass |
| ci-cd | Pass | Pass | Pass |
| grafana | Pass | Pass | Warn |
| refactoring | Pass | Pass | Pass |
| logging-observability | Fail | Pass | Pass |
| background-jobs | Fail | Pass | Pass |
| data-validation | Pass | Pass | Pass |
| testing | Pass | Pass | Pass |
| loom-ci-cd | Pass | Pass | Pass |
| karpenter | Pass | Pass | Pass |
| feature-flags | Pass | Pass | Warn |
| auth | Pass | Pass | Pass |
| loom-logging-observability | Pass | Pass | Pass |
| loom-data-validation | Pass | Pass | Pass |
| loom-prometheus | Pass | Pass | Pass |
| loom-refactoring | Pass | Pass | Pass |
| loom-testing | Pass | Pass | Pass |
| loom-grafana | Pass | Pass | Pass |
| loom-event-driven | Pass | Pass | Pass |

This guide is Orange because the Gen Agent Trust Hub fails logging-observability and background-jobs, with Snyk Warns on prometheus, grafana and feature-flags. 20 of the 90 indexed listings were sampled; the remaining 70 carry no skills.sh verdict.

## Limitations

- Snapshot data, verified 2026-11-28: 2,526 combined installs across 90 indexed listings; 66 GitHub stars; MIT license; last pushed 2026-11-26. Counts drift over time.
- The install index outruns the tree: 15 generic names (prometheus, event-driven, ci-cd, grafana, refactoring, logging-observability, background-jobs, data-validation, testing, karpenter, feature-flags, auth, dead-code-check, before-after, wiring-test) carry install counts but have no counterpart in the repo's `skills/` tree, which ships only the 75 `loom-` prefixed skills.
- No listing reaches 500 installs (prometheus leads at 64), so this is an early-adoption index; treat the counts accordingly.
- The security verdicts cover only 20 of the 90 listings, and two of those (logging-observability, background-jobs) fail the Gen Agent Trust Hub.
- Loom is under active development: signed release binaries cover only Linux x86_64 and macOS Apple Silicon, and every other platform builds from source.

## Related

- [Paseo Skills - A Fleet of Coding Agents](/hermes/skills/catalog/paseo-orchestration-skills-setup)
- [OrchestKit - Orchestration and DevOps Skills](/hermes/skills/catalog/orchestkit-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Fetch a skill's SKILL.md before installing the whole suite; the frontmatter description is what triggers the skill, so read it first.
- Prefer the default `--skills core` install so only 10 skills stay always-loaded and the other 65 load on demand, keeping session context small.
- Treat the non-prefixed names (prometheus, ci-cd, grafana and similar) as the upstream skills.sh listings; loom's own behavior lives in the `loom-` prefixed skills.
- Loom's verification model (implementers do not self-report; an independent check runs each acceptance criterion) is worth studying even if you never run loom itself.
- Re-check the two failing skills (logging-observability, background-jobs) on skills.sh before pulling them into a production profile.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
