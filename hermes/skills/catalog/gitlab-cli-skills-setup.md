---
title: "GitLab CLI Skills - glab Command Reference"
description: "vince-winkintel/gitlab-cli-skills - 7.7K combined installs across 53 indexed listings: glab command reference for GitLab CI, MRs, issues and auth."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/gitlab-cli-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-15"
tags: ["hermes skill", "agent skill", "skill setup", "gitlab", "cli", "devops"]
---

# GitLab CLI Skills - Setup Guide

**Source:** [vince-winkintel/gitlab-cli-skills](https://www.skills.sh/vince-winkintel/gitlab-cli-skills) via skills.sh - 7.7K combined installs across 53 indexed listings; first seen Nov 15, 2026 (Nov 15 evening sweep)
**GitHub:** 51 stars, MIT license, `main` branch, last pushed 2026-11-10, a top-level `gitlab-cli-skills/` index skill plus one directory per `glab-*` skill at the repo root
**Category:** GitLab CLI command reference and automation
**Quality Tier:** 🟡 Yellow - the top-level skill carries a Snyk warn.

This is a collection of skills for AI coding agents following the Agent Skills format, built so an agent can use the GitLab CLI (`glab`) effectively. It ships a top-level `gitlab-cli-skills` overview that handles routing and shared workflows, plus 40+ standalone `glab-*` sub-skills, each in its own directory with its own `SKILL.md`.

`npx skills add` discovers all of them and lets you pick which to install. Skills activate automatically when a relevant task is detected, and the index skill routes to the specialized sub-skills for auth, CI, MRs, issues, releases and repos.

## Installation

```bash
# List every skill in the repo (no install)
npx skills add vince-winkintel/gitlab-cli-skills --list

# Interactive picker (default)
npx skills add vince-winkintel/gitlab-cli-skills

# Install everything
npx skills add vince-winkintel/gitlab-cli-skills --all

# Install specific skills only
npx skills add vince-winkintel/gitlab-cli-skills --skill gitlab-cli-skills --skill glab-mr
```

Claude.ai organization skills need a zip with exactly one `SKILL.md`: download the pre-built `claude-skill.zip` from the latest release, or build it with `bash scripts/build-claude-skill.sh`. The skills also need the GitLab CLI installed:

```bash
brew install glab
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| gitlab-cli-skills | 1,939 | Top-level overview and routing to the glab-* sub-skills. |
| glab-mr | 192 | Create, review, approve and merge merge requests. |
| glab-api | 168 | Direct GitLab REST API calls and JSON queries. |
| glab-ci | 166 | CI/CD pipelines, jobs, artifacts and .gitlab-ci.yml. |
| glab-auth | 151 | Login, auth status, account switching and Docker registry access. |
| glab-issue | 145 | Create, view and update issues and boards. |
| glab-repo | 143 | Clone, create, fork, archive and manage projects. |
| glab-job | 133 | View, retry, cancel and trace individual CI jobs. |
| glab-runner | 127 | List, assign and manage CI/CD runners. |
| glab-release | 127 | Create, list and download releases and assets. |
| glab-config | 127 | Configure glab defaults and per-host settings. |
| glab-skills | 126 | Inspect, install and update bundled agent skills. |
| glab-variable | 124 | Manage project and group CI/CD variables. |
| glab-changelog | 123 | Generate changelogs from releases, tags and commits. |
| glab-mcp | 122 | Legacy glab MCP server guidance and migration. |
| glab-stack | 121 | Manage stacked merge requests. |
| glab-packages | 121 | List, upload and delete package registry packages. |
| glab-check-update | 121 | Check for glab and Duo CLI updates. |
| glab-help | 120 | Display command and subcommand help. |
| glab-user | 119 | View user profiles, events and SSH keys. |
| glab-container-registry | 119 | Manage container registry repositories and tags. |
| glab-workitems | 118 | Create and update work items, tasks and OKRs. |
| glab-version | 118 | Display glab version and build details. |
| glab-token | 118 | Manage personal, project and group access tokens. |
| glab-opentofu | 117 | OpenTofu and Terraform state management. |
| glab-quick-actions | 116 | Slash-command quick actions in comments and bodies. |
| glab-label | 116 | Create, list and update project and group labels. |
| glab-gpg-key | 116 | Manage GPG keys for commit signing. |
| glab-alias | 116 | Create and list glab command aliases. |
| glab-schedule | 115 | Manage scheduled CI/CD pipelines. |
| glab-orbit | 115 | Run the Orbit CLI for code-graph queries. |
| glab-incident | 115 | Create and manage incidents. |
| glab-completion | 115 | Generate shell completion scripts. |
| glab-duo | 114 | Install and run GitLab Duo CLI. |
| glab-deploy-key | 114 | Manage SSH deploy keys for projects. |
| glab-todo | 113 | List and clear your to-do list. |
| glab-ssh-key | 113 | Manage account SSH keys. |
| glab-snippet | 113 | Create project or personal code snippets. |
| glab-milestone | 112 | Manage project milestones. |
| glab-iteration | 112 | Manage iterations for sprint planning. |
| glab-runner-controller | 111 | Manage runner controllers and tokens (experimental). |
| glab-cluster | 111 | Manage Kubernetes clusters and agents. |
| glab-attestation | 111 | Verify artifacts and provenance. |
| glab-whatsnew | 110 | View release notes and what changed. |
| glab-securefile | 110 | Manage secure files for CI/CD. |

The remaining 8 indexed listings range from 2 to 96 installs.

## Why This Matters for Hermes Agents

Most agents know GitLab through a web UI or a generic REST client, but `glab` is the command-line surface, and its subcommands and flags are specific. These skills encode that surface so an agent reaches for the right command instead of shelling out to `curl` for everything.

The split is the design worth noting: one index skill routes to 40+ standalone sub-skills, so an agent loads only the slice it needs for the task at hand. A pipeline investigation loads `glab-ci` and `glab-job`, not the whole reference.

A few sub-skills handle the risky parts of automation explicitly: `glab-token` and `glab-deploy-token` keep creation and rotation behind explicit approval, and `glab-artifact-registry` exchanges credentials for short-lived tokens rather than long-lived ones.

## Usage

| You say | What happens |
|---|---|
| "Log into GitLab CLI" | glab-auth handles login, auth status and Docker registry access. |
| "Check the status of my pipeline" | glab-ci reads pipeline status, job logs and artifacts. |
| "Review this merge request" | glab-mr opens, approves, comments and merges the MR. |
| "File a bug for this traceback" | glab-issue creates the issue with the right labels. |
| "Create a release for this tag" | glab-release publishes the version and uploads assets. |
| "Get a short-lived registry token" | glab-artifact-registry exchanges credentials for an ephemeral token. |
| "What's new in glab" | glab-whatsnew shows release notes since the last version. |

## Verification

Check the skill files before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/vince-winkintel/gitlab-cli-skills/main/gitlab-cli-skills/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/vince-winkintel/gitlab-cli-skills/main/glab-mr/SKILL.md | head -20
npx skills add vince-winkintel/gitlab-cli-skills --list
brew install glab
```

The skills assume `glab` is installed and authenticated; run `glab auth status` after install to confirm before relying on any sub-skill.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-15) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| gitlab-cli-skills | Pass | Pass | Warn |

The sample covers only the top-level skill; the 40+ `glab-*` sub-skills are not individually listed in this sample, so re-check each skill's security page on skills.sh before production use.

## Limitations

- Snapshot data, verified 2026-11-15: 7,673 combined installs across 53 indexed listings; 51 GitHub stars; MIT; last pushed 2026-11-10. Counts drift over time.
- The security sample covers the top-level skill only; the 52 `glab-*` sub-skills carry no per-skill verdicts here.
- The reference tracks the installed `glab` version, so keep the CLI updated alongside the skills; guidance can lag a fresh glab release.
- Several skills are experimental or deprecated: glab-autoflow (experimental Relay), glab-runner-controller (experimental, admin-only) and glab-mcp (deprecated in favor of the GitLab MCP Server).
- The Claude.ai path needs a separate merged `claude-skill.zip` built from the latest release, not the per-skill directories.

## Related

- [gh-issue-sync - Local Markdown GitHub Issues Skill Setup](/hermes/skills/catalog/gh-issue-sync-setup)
- [gh-stack - GitHub Stacked PRs Skill Setup](/hermes/skills/catalog/gh-stack-setup)
- [Fandhe Agent CLI Skills - Commit and PR Workflows](/hermes/skills/catalog/fandhe-agent-cli-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install only the sub-skills you use; each `glab-*` skill is standalone and `npx skills add` lets you pick.
- Keep `glab` current, since the skills describe the current CLI surface.
- For Claude.ai, use the pre-built `claude-skill.zip` from the latest release instead of hand-merging.
- Route through the index skill for shared workflows, then let it dispatch to the `glab-*` sub-skill.
- Use glab-api for anything no dedicated sub-skill covers.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
