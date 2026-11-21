---
title: "Namespace Agent Skills - Remote Devboxes Setup"
description: "namespacelabs/agent-skills: a devboxes skill for isolated remote Namespace development environments, builds and tests - 3.2K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/namespacelabs-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-21"
tags: ["hermes skill", "agent skill", "skill setup", "devboxes", "remote development", "ci"]
---

# Namespace Agent Skills - Remote Devboxes Setup

**Source:** [namespacelabs/agent-skills](https://www.skills.sh/namespacelabs/agent-skills) via skills.sh - 3.2K combined installs across 1 indexed listing; first seen Nov 21, 2026 (Nov 21, 2026 morning sweep)
**GitHub:** [namespacelabs/agent-skills](https://github.com/namespacelabs/agent-skills) - 2 stars, Apache-2.0 license, main branch, last pushed Nov 19, 2026; one `namespace` plugin at the repo root whose per-agent manifests (Claude, Codex, Cursor, Antigravity, Gemini) all share `skills/` and a hosted MCP server.
**Category:** Remote Development Environments and CI
**Quality Tier:** 🟢 Green - the single sampled skill passes Gen Agent Trust Hub, Socket and Snyk.

Namespace publishes this plugin plus skills set for agents that investigate CI and builds, adopt Namespace runners and caching, optimize CI speed and cost, debug failed jobs, and manage devboxes. The plugin connects to the hosted MCP server at `https://mcp.namespace.so/mcp`, and on first use your agent opens Namespace in the browser to authorize one workspace. A read-only MCP endpoint is available for agents that only need to inspect.

The repo ships four skills (devboxes, adopting-namespace-runners, debugging-github-actions-jobs, optimizing-namespace-ci), but skills.sh indexes only one of them, devboxes, so the install count belongs to that single listing. A devbox is an isolated Linux or macOS environment for remote builds, tests and workloads that exceed local capacity. First seen in the Nov 21, 2026 morning sweep.

## Installation

Claude Code and Claude Cowork:

```sh
claude plugin marketplace add namespacelabs/agent-skills
claude plugin install namespace@namespace
```

Then run `/mcp`, select `plugin:namespace:namespace`, and choose Authenticate.

Codex:

```sh
codex plugin marketplace add namespacelabs/agent-skills
```

Then run `/plugins`, select Namespace, and install it.

Gemini CLI:

```sh
gemini extensions install https://github.com/namespacelabs/agent-skills
```

Antigravity:

```sh
agy plugin install https://github.com/namespacelabs/agent-skills
```

Skills only, for any agent that supports Agent Skills and skips the MCP server:

```sh
npx skills add namespacelabs/agent-skills
npx skills add namespacelabs/agent-skills --skill devboxes
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| devboxes | 3,239 | creating, running, sharing and tearing down Namespace devboxes for isolated remote builds, tests and workloads |

No indexed listings fall below the threshold; the single indexed listing appears above.

## Why This Matters for Hermes Agents

The devboxes skill gives an agent a disposable remote environment, so builds and test runs do not compete with the local machine and workloads beyond local capacity can still execute. Task markers keep unattended work alive inside a devbox, which matters for long jobs an agent starts and then steps away from. The devbox can be shared or torn down, so an operator gets a clean, reproducible environment per job instead of a snowflake laptop state.

The other three in-tree skills cover runner adoption, caching, CI debugging and cost optimization, but they are not indexed by skills.sh, so they carry no tracked install count even though they ship in the same repository. The plugin gates on browser authorization of one workspace, and a read-only MCP endpoint exists for agents that only need to inspect CI state. For operators, this moves CI investigation and compute-heavy work off the laptop with a single natural-language request.

## Usage

| You say | What happens |
|---|---|
| Spin up a devbox and run this test suite inside it | devboxes creates an isolated environment and runs the tests, with sharding support |
| Why did this GitHub Actions job time out | debugging-github-actions-jobs finds why a Namespace-run job failed, timed out or waited to start |
| Move our workflows onto Namespace runners and turn on caching | adopting-namespace-runners converts GitHub-hosted labels and enables runners and caches |
| Make our CI faster and cheaper | optimizing-namespace-ci sizes runners and shards from measured evidence |
| Give me a disposable Linux host for this build | devboxes creates a throwaway Docker host for the workload |
| Keep this long job alive while I step away | devboxes task markers keep unattended work running inside the devbox |

## Verification

Confirm the plugin landed and review the devboxes skill's instructions before first use:

```bash
ls skills 2>/dev/null || ls ~/.claude/plugins 2>/dev/null
```

```bash
curl -sL https://raw.githubusercontent.com/namespacelabs/agent-skills/main/skills/devboxes/SKILL.md | head -40
```

On first use the agent opens Namespace in the browser to authorize one workspace; confirm the workspace is the one you intend before allowing compute or CI changes.

## Security

skills.sh verdicts for sampled skills (verified Nov 21, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| devboxes | Pass | Pass | Pass |

Devboxes are real remote compute, so scope the authorized workspace and prefer the read-only MCP endpoint (`https://mcp.namespace.so/mcp/readonly`) when the agent only needs to inspect.

## Limitations

- Snapshot data, verified Nov 21, 2026: 3,239 combined installs across 1 indexed listing; 2 GitHub stars; Apache-2.0 license; last pushed Nov 19, 2026. Counts drift over time.
- The family is one skill in the install index: only devboxes is indexed, while the repo also ships adopting-namespace-runners, debugging-github-actions-jobs and optimizing-namespace-ci with no skills.sh listing.
- Devboxes spin up remote compute, so usage is metered and depends on your Namespace account rather than local hardware.
- The MCP server is hosted, so skill behaviour depends on the Namespace MCP tool surface, which changes independently of these skill files.
- Authorize one workspace on first use; the skills operate inside whatever workspace the agent is connected to.

## Related

- [Replicas Agent Skill - Cloud Workspace Coding Agent Setup](/hermes/skills/catalog/replicas-agent-skill-setup)
- [Openwork Skills - Agent Workspace Setup](/hermes/skills/catalog/openwork-skills-setup)
- [Railway Agent Skills - Infrastructure Deployment Setup](/hermes/skills/catalog/railway-agent-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Use the read-only MCP endpoint first so the agent can inspect CI and devboxes without write access.
- Prefer a devbox for one-off jobs over the local machine, and use task markers to keep unattended work alive inside it.
- Install with `--skill devboxes` when you only need the indexed skill and want to skip the MCP server.
- Keep the workspace authorization to one known workspace, and re-check it after browser auth before compute-heavy runs.
- Pin the plugin version you tested rather than tracking the marketplace head, since manifests and the MCP URL change across releases.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
