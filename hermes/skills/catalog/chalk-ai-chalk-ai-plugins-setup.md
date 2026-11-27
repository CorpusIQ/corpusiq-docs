---
title: "Chalk AI Plugins - Claude Code & Codex Marketplace Setup"
description: "chalk-ai/chalk-ai-plugins: 11.2K combined installs. Private Chalk marketplace for Claude Code and Codex: acceleration, benchmarking and deployment."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/chalk-ai-chalk-ai-plugins-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "claude code", "codex", "mlops"]
---

# Chalk AI Plugins - Setup Guide

**Source:** [chalk-ai/chalk-ai-plugins](https://www.skills.sh/chalk-ai/chalk-ai-plugins) via skills.sh - 11.2K combined installs across 5 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 evening sweep)

**GitHub:** [chalk-ai/chalk-ai-plugins](https://github.com/chalk-ai/chalk-ai-plugins) - 0 stars, no license file (the GitHub API also reports no license), branch main, last pushed 2026-09-15; five `SKILL.md` files at `plugins/<plugin>/skills/<name>/SKILL.md` across five plugin directories (chalk-accelerate, chalk-benchmark-model, chalk-deploy-function, chalk-hello and chalk-plan-cache), a sixth `chalk-lsp` plugin that ships only a language server, and root marketplace catalogs at `.claude-plugin/marketplace.json` and `.agents/plugins/marketplace.json`

**Category:** Chalk developer tooling: resolver acceleration, model benchmarking and function deployment

**Quality Tier:** 🟢 Green - all 5 sampled skills Pass on Gen Agent Trust Hub, Socket and Snyk. Described in the README as a private Chalk-internal marketplace and carrying no license file; its five install counts sit in a flat band, so one install signal carries the whole set.

The repository is Chalk's plugin marketplace, described in its own README and repo description as a private plugin marketplace for the `chalk-ai` GitHub org that distributes plugins to Claude Code and Codex from a single repository. It ships five skills across five plugin directories, all aimed at people building on Chalk's own platform: making Python resolvers statically accelerable, benchmarking a vLLM-served model's cost and throughput, deploying a chalkcompute function, debugging query plan cache misses, and a `chalk-hello` greeting used to confirm a plugin installed. A sixth plugin, `chalk-lsp`, ships a language server for Claude Code and carries no skill listing.

Access is the thing to pin down before installing. The README's Notes say "This repo is private; pushes are visible only to chalk-ai org members", and the repo description still reads "Private plugin marketplace for Claude Code and Codex". The live state disagrees: on 2026-11-26 the GitHub API reports the repository as public (private: false) and every raw file path returns HTTP 200, so the private label appears to be stale. The commands below are the README's own, including its private-repo auth steps, and the README documents no public route, so do not treat the access situation as settled without checking it yourself.

The install counts are the tell that this is not five independently popular skills. The five listings sit at 2,248, 2,244, 2,241, 2,239 and 2,237, a flat band spanning eleven installs. That shape means one install unit, the all-skills route of `gh skill install chalk-ai/chalk-ai-plugins` or a single marketplace add, appears to carry the whole plugin set rather than each skill earning its own audience.

## Installation

The README documents three install routes, all of which it frames as private-repo flows:

Skills CLI:

```text
gh skill install chalk-ai/chalk-ai-plugins
```

Choose all skills, then your coding agents, then a Global install scope in the home directory.

Claude Code:

```text
/plugin marketplace add chalk-ai/chalk-ai-plugins
/plugin install chalk-hello@chalk-ai
```

Claude Code uses your local git credentials for a private repo; for background auto-updates the README says to export a token with `repo` scope:

```text
export GITHUB_TOKEN=ghp_...
```

Codex:

```text
codex plugin marketplace add chalk-ai/chalk-ai-plugins
codex plugin add chalk-hello@chalk-ai
```

Codex reads `.agents/plugins/marketplace.json` from the repo root. The marketplace name `chalk-ai` is the identifier that appears in `/plugin install <plugin>@chalk-ai`.

There is no Hermes adapter and no `npx skills add` target here, so the durable route for this profile is a directory copy out of a clone:

```bash
cp -R plugins/chalk-benchmark-model/skills/benchmark-vllm-model ~/.hermes/profiles/corpusiq/skills/benchmark-vllm-model
cp -R plugins/chalk-plan-cache/skills/debug-plan-cache-misses ~/.hermes/profiles/corpusiq/skills/debug-plan-cache-misses
```

Copy the whole directory rather than the markdown. `benchmark-vllm-model` ships `scripts/bench.py` beside its `SKILL.md`, and `chalk-accelerate` ships `bin/accelerator-diagnostics.py` at the plugin level, so a lone `SKILL.md` leaves the skill pointing at a script that is not there.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| accelerate-python-resolvers | 2,248 | Making Chalk Python resolvers statically accelerable: run the static-acceleration diagnostics, find why a resolver cannot be accelerated, and speed up Python feature pipelines in a Chalk project (a repo with chalk.yaml or chalk.yml). |
| benchmark-vllm-model | 2,244 | Benchmarking the throughput and cost-per-token of a model served on vLLM in Chalk's container infrastructure: dollar per token, dollar per request, tokens per second, GPU sizing for an LLM, and a self-hosted model's economics against a hosted API. |
| chalk-hello | 2,241 | Verifying a plugin installed correctly by printing a friendly greeting from the Chalk plugin marketplace. |
| debug-plan-cache-misses | 2,239 | Finding and debugging Chalk query plan cache misses from engine logs: queries that replan on every request, the "ad-hoc query request missed the plan cache" warning, latency spikes from repeated planning, and queries that should share a cached plan but do not. |
| deploy-chalk-function | 2,237 | Deploying a chalkcompute function: run a standalone Python function remotely on Chalk, deploy a chalkcompute function, or use the chalkcompute SDK. |

No indexed listings fall below the 1,000-install threshold.

## Why This Matters for Hermes Agents

The value here is narrow but real: if you build on Chalk, these five skills encode the platform's own operational knowledge, and they are packaged for agents rather than for a human to read through. `accelerate-python-resolvers` turns the "why can't this resolver be accelerated" question into a diagnostic run instead of a guessing session, and `debug-plan-cache-misses` knows to drive the `chalk logs` CLI search from an engine warning, which is the kind of routing a general model gets wrong.

For everyone else the suite is mostly a template worth copying. It is a worked example of a dual-runtime marketplace: one directory of plugins, two manifest formats (`.claude-plugin/plugin.json` and `.codex-plugin/plugin.json`), two marketplace catalogs, and a CI pipeline that validates, lints, shellchecks and actually installs every plugin before it can merge. An org that maintains its own internal skill set can lift that structure directly.

Read the access line before you invest. The install counts look like a small but healthy public suite, but the README describes the repo as private and Chalk-internal, so those numbers are internal adoption rather than a public market signal. The flat band across all five listings confirms it: one install action appears to carry the whole set.

## Usage

| You say | What happens |
|---|---|
| "Why can't this resolver be accelerated?" | `accelerate-python-resolvers` walks the static-acceleration diagnostics for the Chalk project (chalk.yaml or chalk.yml) and reports the reason the resolver is not statically accelerable instead of guessing. |
| "Speed up this Chalk feature pipeline" | `accelerate-python-resolvers` finds the resolvers in the pipeline that are not statically accelerable and flags the changes that would let the accelerator take them. |
| "What would it cost to self-host this model?" | `benchmark-vllm-model` runs the vLLM benchmark against the model in Chalk's container infrastructure and reports dollars per token, dollars per request and tokens per second, plus a comparison against a hosted API. |
| "Deploy this Python function to Chalk" | `deploy-chalk-function` walks through deploying a chalkcompute function so the function runs remotely in Chalk's container infrastructure via the chalkcompute SDK. |
| "Is the marketplace installed correctly?" | `chalk-hello` prints a greeting from the Chalk plugin marketplace, confirming the plugin loaded and the install took. |
| "Why is this query replanning on every request?" | `debug-plan-cache-misses` searches the engine logs via `chalk logs` for the plan cache miss warning and explains why two seemingly identical queries do not share a cached plan. |

## Verification

The five raw paths below all returned 200 on branch main when this guide was written on 2026-11-26:

```bash
curl -sL -o /dev/null -w "%{http_code} accelerate\n" \
  https://raw.githubusercontent.com/chalk-ai/chalk-ai-plugins/main/plugins/chalk-accelerate/skills/accelerate-python-resolvers/SKILL.md
curl -sL -o /dev/null -w "%{http_code} benchmark\n" \
  https://raw.githubusercontent.com/chalk-ai/chalk-ai-plugins/main/plugins/chalk-benchmark-model/skills/benchmark-vllm-model/SKILL.md
```

Expect `200` twice. Read one before installing: the frontmatter description is the routing contract, listing the trigger phrases (for example, `benchmark-vllm-model` fires on dollar-per-token, tokens-per-second and GPU-sizing requests), and a copy with a trimmed description stops being selected for the requests it was written for.

After a copy lands in the profile, confirm the frontmatter and the directory shape:

```bash
head -3 ~/.hermes/profiles/corpusiq/skills/benchmark-vllm-model/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/benchmark-vllm-model/
```

A good copy shows `name:` and `description:` in the first three lines, and the listing shows `SKILL.md` and `scripts/` (with `bench.py` inside). For `accelerate-python-resolvers`, copy the plugin-level `bin/accelerator-diagnostics.py` alongside it or the skill's diagnostics reference will not resolve.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-26) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| accelerate-python-resolvers | Pass | Pass | Pass |
| benchmark-vllm-model | Pass | Pass | Pass |
| chalk-hello | Pass | Pass | Pass |
| debug-plan-cache-misses | Pass | Pass | Pass |
| deploy-chalk-function | Pass | Pass | Pass |

All five sampled skills Pass across all three scanners, with no FAIL or Warn in the sample. The bigger caveat is licensing: there is no license file in the repository and the GitHub API returns none, so no redistribution permission is granted by default, and any reuse or vendoring needs the owner's permission first.

## Limitations

- Snapshot data, verified 2026-11-26: 11,209 combined installs across 5 indexed listings; 0 GitHub stars; no license file (the GitHub API reports None); last pushed 2026-09-15. Counts drift over time.
- The README and repo description call this a private marketplace ("This repo is private; pushes are visible only to chalk-ai org members"), but the live GitHub API reports the repository as public (private: false) and raw files fetch with HTTP 200 on 2026-11-26. The private label appears stale; treat access as unresolved and re-check before relying on it.
- There is no license file and the GitHub API returns no license, so no permission is granted by default. Redistributing a copy, vendoring it or publishing a modified version needs the owner's permission first.
- The five install counts are a flat band (2,248 down to 2,237), so they do not rank the skills: one install unit appears to carry the whole plugin set, not five independently earned audiences.
- The README's repository-layout tree lists only four of the six plugin directories (chalk-accelerate, chalk-hello, chalk-lsp and chalk-plan-cache) and omits chalk-benchmark-model and chalk-deploy-function, which exist in the tree and carry indexed skills, so the documentation undercounts the suite.
- There is no Hermes adapter and no `npx skills add` target. Outside Claude Code and Codex the only route is a directory copy, which also means updates are a re-copy rather than an upgrade command.

## Related

- [wshobson/agents - Agent Plugin Marketplace Setup](/hermes/skills/catalog/wshobson-agents-setup)
- [Dotneet Claude Code Marketplace - Plugin Collection Setup](/hermes/skills/catalog/dotneet-claude-code-marketplace-setup)
- [Melodic Software Claude Code Plugins - Marketplace Setup](/hermes/skills/catalog/melodic-claude-code-plugins-setup)
- [Bencium Marketplace - Design & Product Skills Suite Setup](/hermes/skills/catalog/bencium-marketplace-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Copy whole directories. `benchmark-vllm-model` ships `scripts/bench.py` and `chalk-accelerate` ships `bin/accelerator-diagnostics.py`, so a lone `SKILL.md` leaves the skill pointing at a script that is not there.
- Install `chalk-hello` first. It is the README's own smoke test for the marketplace, and a greeting in the agent's output tells you the plugin pipeline works before you trust the heavier skills.
- Treat this as a Chalk-platform suite. Every skill except the greeting assumes you run a Chalk project (chalk.yaml or chalk.yml) or Chalk's container infrastructure, so the value collapses outside that environment.
- Re-check the private/public status before installing. The README says private and the GitHub API says public, and that disagreement is exactly the kind of thing that changes between snapshots.
- Read the frontmatter before trimming. Each description carries the trigger phrases that route requests to the skill, and an edited description silently unroutes the requests it was written for.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
