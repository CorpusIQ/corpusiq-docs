---
title: "Bitbucket CLI (bkt) - Bitbucket Workflows Agent Skill Setup"
description: "avivsinai/bitbucket-cli - 2.1K combined installs: a Bitbucket Cloud and Data Center CLI skill teaching agents PRs, pipelines, repos, and webhooks."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/avivsinai-bitbucket-cli-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "bitbucket", "cli", "devops"]
---

# Bitbucket CLI (bkt) - Setup Guide

**Source:** [avivsinai/bitbucket-cli](https://www.skills.sh/avivsinai/bitbucket-cli) via skills.sh - 2.1K combined installs across 1 indexed listing; first catalogued Nov 26, 2026 (Nov 26, 2026 evening sweep)
**GitHub:** [avivsinai/bitbucket-cli](https://github.com/avivsinai/bitbucket-cli) - 268 stars, MIT license, last pushed Nov 26, 2026, master branch; the bkt skill ships at skills/bkt/SKILL.md with mirrors at .agents/skills/bkt/ and .claude/skills/bkt/.
**Category:** Bitbucket DevOps CLI
**Quality Tier:** 🟡 Yellow - the single sampled skill passes the Gen Agent Trust Hub and Socket, but Snyk marks it Warn.

bkt is a Bitbucket Cloud and Data Center command-line interface with gh-like ergonomics, and skills.sh indexes it as a single listing. All 2,113 combined installs attach to that one listing. The skill lives at skills/bkt/SKILL.md alongside 19 rules reference files covering pull requests, pipelines, repositories, branches, commits, auth, webhooks, variables, permissions, and more, and the repository also mirrors the same SKILL.md into .agents/skills/bkt/ and .claude/skills/bkt/.

The skill teaches an agent to drive bkt for Bitbucket Cloud and Bitbucket Data Center (the server product) work: creating and reviewing pull requests, listing and triggering pipelines, managing repositories, branches, permissions, and webhooks, and calling the REST API with bkt api. Authentication is the CLI's own credential path: bkt auth login stores a token in the OS keychain, and CI or container jobs use BKT_TOKEN and BKT_HOST instead. The same skill is published for Claude Code, Codex, and the universal .agents directory.

## Installation

Install the CLI from the README's install table, then add the agent skill:

```bash
brew install bitbucket-cli                                  # macOS / Linux (Homebrew)
winget install AvivSinai.Bitbucket-CLI                      # Windows (WinGet)
go install github.com/avivsinai/bitbucket-cli/cmd/bkt@latest  # Go 1.26+
nix profile install github:avivsinai/bitbucket-cli          # Nix flakes
```

The agent skill installs with the skills CLI:

```bash
npx skills add avivsinai/bitbucket-cli -g -y
```

Alternatives from the README: `npx skild install @avivsinai/bkt -t claude -y`, the Claude Code marketplace (`/plugin marketplace add avivsinai/skills-marketplace` then `/plugin install bkt@avivsinai-marketplace`), or copying skills/bkt into ~/.claude/skills/. The CLI also ships an MCP server (`bkt mcp serve`) that exposes read-only Bitbucket tools over stdio.

After installing, authenticate with `bkt auth login https://bitbucket.org --kind cloud --web` (Cloud browser OAuth) or `bkt auth login https://bitbucket.example.com --web-token` (Data Center PAT), then create a context so bkt knows the default host and workspace or project.

## What It Provides

skills.sh indexes one listing.

| Skill | Installs | Use For |
|---|---|---|
| bkt | 2,113 | Operate Bitbucket Cloud or Data Center repositories, pull requests, branches, pipelines, permissions, and webhooks with bkt |

No indexed listings fall below the 1,000-install threshold.

## Why This Matters for Hermes Agents

The bkt skill gives a Hermes agent a single, stable command set for Bitbucket work instead of re-deriving REST calls by hand. Every bkt command returns a JSON or YAML output contract, so an agent can script PR creation, pipeline triggering, and repo management and parse the result reliably. The skill covers the whole surface: pull requests, pipelines, repositories, branches, commits, permissions, variables, and webhooks, plus a bkt api escape hatch for anything else. Because the skill ships in the same repository as the CLI and is mirrored for Claude Code, Codex, and the universal .agents directory, it tracks the CLI's own releases. Authentication stays inside the CLI: tokens live in the OS keychain, and CI or container jobs switch to BKT_TOKEN and BKT_HOST with no config file. The main caveat is that bkt is a third-party CLI unrelated to other tools named bitbucket-cli, so the agent should confirm the platform (Cloud versus Data Center) before issuing platform-specific commands.

## Usage

| You say | What happens |
|---|---|
| List my open pull requests | Runs `bkt pr list --state OPEN` and returns the list, parsed as JSON |
| Create a PR from this branch | Runs `bkt pr create` with a title, source, and target branch |
| Wait for the PR build to finish | Runs `bkt pr checks <id> --wait --timeout 5m` with backoff |
| Trigger the staging pipeline | Runs `bkt pipeline run --ref main --var ENV=staging` |
| Show me this repo's permissions | Runs `bkt perms repo list --project DATA --repo platform-api` |
| Create a webhook for CI | Runs `bkt webhook create` with a name, URL, and event |
| Call an arbitrary Bitbucket endpoint | Runs `bkt api` using the stored credentials |

## Verification

Confirm the README and the skill body resolve on the master branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/avivsinai/bitbucket-cli/master/README.md | head -40
curl -sL https://raw.githubusercontent.com/avivsinai/bitbucket-cli/master/skills/bkt/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/avivsinai/bitbucket-cli/master/skills/bkt/rules/pr.md | head -40
```

All three URLs return 200. After installing, review the SKILL.md and its rules files before relying on it, and confirm which platform (Cloud or Data Center) your Bitbucket host is.

## Security

skills.sh verdicts for the sampled skill (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| bkt | Pass | Pass | Warn |

Across the 1 sampled skill there are 2 Pass, 1 Warn, and 0 Fail cells; the single listing carries a Snyk Warn. Read the Snyk advisory before relying on this skill in a pipeline that gates on security results.

## Limitations

- Snapshot data, verified Nov 26, 2026: 2,113 combined installs across 1 indexed listing; 268 GitHub stars; MIT license; last pushed Nov 26, 2026. Counts drift over time.
- The default branch is master, not main; every raw URL in this guide uses master, and scripts that assume main will 404.
- This is a single-listing CLI skill, not a skill collection; the 2,113 installs attach to the one bkt listing.
- bkt is one of several unrelated tools named bitbucket-cli (the README also disambiguates it from a Rust subprocess-caching tool and a Swisscom enterprise CLI), so confirm the binary before scripting around it.
- Authentication is the CLI's own credential path (OS keychain or BKT_TOKEN/BKT_HOST); the skill does not carry or manage credentials itself, so the agent inherits whatever the CLI has authenticated.
- The repository is mostly Go source for the CLI itself (381 files); the agent skill is a small part of it.

## Related

[gh-axi - Token-Efficient GitHub CLI for Agents](/hermes/skills/catalog/gh-axi-setup) | [Jess Agent Skills - GitHub Workflow Suite Setup](/hermes/skills/catalog/jssblck-agents-setup) | [GitNexus - Code Intelligence Engine Skills Setup](/hermes/skills/catalog/abhigyanpatwari-gitnexus-setup) | [Build Mcp Server Setup](/hermes/skills/catalog/build-mcp-server-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Use the master branch in every raw URL; the repo has no main branch.
- Confirm the platform before platform-specific commands: Cloud uses workspaces (api.bitbucket.org), Data Center uses projects and a self-hosted host.
- Prefer --json and --jq for scripted output so the agent parses a stable contract instead of human-readable tables.
- Point the agent at bkt api for anything the dedicated subcommands do not cover; it reuses the stored credentials.
- In CI or containers, set BKT_TOKEN and BKT_HOST so bkt needs no login and no config file.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
