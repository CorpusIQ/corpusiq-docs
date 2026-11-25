---
title: "Flux CD Agent Skills - GitOps Engineering Setup"
description: "fluxcd/agent-skills - 3.3K combined installs: official Flux CD skills for GitOps manifests, repo audits and live cluster debugging."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/fluxcd-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-24"
tags: ["hermes skill", "agent skill", "skill setup", "flux", "gitops", "kubernetes"]
---

# Flux CD Agent Skills - Setup Guide

**Source:** [fluxcd/agent-skills](https://www.skills.sh/fluxcd/agent-skills) via skills.sh - 3.3K combined installs across 7 indexed listings; first catalogued Nov 24, 2026 (Nov 24, 2026 evening sweep)
**GitHub:** [fluxcd/agent-skills](https://github.com/fluxcd/agent-skills) - 245 stars, Apache-2.0 license, last pushed Nov 24, 2026; the three public skills live under skills/<name>/, three maintainer skills under internal/skills/, and analyze-gitops-repo has no SKILL.md in the current tree.
**Category:** GitOps and Kubernetes
**Quality Tier:** 🟠 Orange - analyze-gitops-repo fails the Gen Agent Trust Hub check; the other six sampled skills pass or carry only Warn cells.

fluxcd/agent-skills is the official AI skills suite from the Flux CD maintainers, aimed at turning AI agents into GitOps engineers. It covers three core jobs: answering Flux questions and generating schema-validated manifests (gitops-knowledge), auditing and validating GitOps repositories (gitops-repo-audit), and debugging live Kubernetes clusters (gitops-cluster-debug), plus internal release-management skills for the Flux controllers.

The skills.sh index lists 7 listings at 3.3K combined installs. Three maintainer-facing skills (commit-assisted-by, flux-controller-patch-releases, flux-controller-minor-releases) live under internal/skills/, and one indexed listing (analyze-gitops-repo) has no SKILL.md counterpart in the current tree.

## Installation

Flux CLI (verifies the cosign signature and extracts to .agents/skills):

```shell
flux plugin install operator
flux operator skills install ghcr.io/fluxcd/agent-skills --agent claude-code
```

Update later with flux operator skills update.

NPX:

```shell
npx skills add fluxcd/agent-skills
```

Claude Code:

```shell
/plugin marketplace add fluxcd/agent-skills
/plugin install gitops-skills@fluxcd
```

Codex:

```shell
codex plugin marketplace add fluxcd/agent-skills
codex plugin add gitops-skills@fluxcd
```

GitHub Copilot:

```shell
copilot plugin marketplace add fluxcd/agent-skills
copilot plugin install gitops-skills@fluxcd
```

Prerequisites: flux v2.10 or later, flux-schema (flux plugin install schema), and flux-operator-mcp for gitops-cluster-debug. A Brewfile is provided for macOS.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| gitops-knowledge | 1,343 | answering Flux questions and generating schema-validated YAML for all Flux CRDs |
| gitops-cluster-debug | 1,241 | debugging Flux on live Kubernetes clusters via the Flux MCP server |
| gitops-repo-audit | 727 | auditing GitOps repos for structure, security and deprecated APIs, with a prioritized report |
| analyze-gitops-repo | 12 | analyzing a GitOps repository (name-level: no SKILL.md counterpart in the current tree) |
| commit-assisted-by | 4 | adding an Assisted-by git trailer to AI-assisted commits |
| flux-controller-patch-releases | 3 | running the upstream Flux controller patch release procedure |
| flux-controller-minor-releases | 3 | running the upstream Flux controller minor release procedure |

All 7 indexed listings clear the 1-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

Flux CD reconciles Kubernetes clusters against Git, and its CRD surface (HelmRelease, Kustomization, GitRepository, OCIRepository, ResourceSet, FluxInstance) is large enough that a general-purpose agent produces stale or invalid manifests. These skills bundle OpenAPI schemas for every Flux resource, so a Hermes agent can generate schema-validated YAML instead of guessing at field names. The repo-audit skill turns local files into a prioritized GitOps report (deprecated APIs, RBAC, secrets), which is the kind of deterministic, offline check a builder wants wired into a review loop. The cluster-debug skill reaches a live cluster through the Flux MCP server and can preview what a local manifest change would do before commit. Installation is signature-verified through the Flux CLI, a stronger supply-chain posture than most skill installs. The maintainer-facing skills under internal/ are less useful to end users but show the Flux team's own release automation.

## Usage

| You say | What happens |
|---|---|
| Generate a HelmRelease for my frontend | Uses gitops-knowledge to produce schema-validated YAML |
| Audit the current repo | Uses gitops-repo-audit to scan and produce a prioritized GitOps report |
| Debug the failing HelmRelease | Uses gitops-cluster-debug to inspect Flux resources, events and logs |
| What will this manifest change do? | Uses gitops-cluster-debug to preview the change against the cluster |
| Validate my repo without a full audit | Uses gitops-repo-audit to run only the manifest validation phase |
| Tag my commits with the agent that made them | Uses commit-assisted-by to add an Assisted-by trailer |

## Verification

Confirm the README resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/fluxcd/agent-skills/main/README.md | head -60
```

Confirm a representative skill body before installing:

```bash
curl -sL https://raw.githubusercontent.com/fluxcd/agent-skills/main/skills/gitops-knowledge/SKILL.md | head -30
```

The Flux CLI install extracts skills to .agents/skills in the repo root; confirm that directory exists after install.

## Security

skills.sh verdicts for sampled skills (verified Nov 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| gitops-knowledge | Pass | Pass | Pass |
| gitops-cluster-debug | Pass | Pass | Pass |
| gitops-repo-audit | Pass | Pass | Pass |
| analyze-gitops-repo | Fail | Pass | Warn |
| commit-assisted-by | Pass | Pass | Pass |
| flux-controller-patch-releases | Pass | Pass | Warn |
| flux-controller-minor-releases | Pass | Pass | Warn |

## Limitations

- Snapshot data, verified Nov 24, 2026: 3,333 combined installs across 7 indexed listings; 245 GitHub stars; Apache-2.0 license; last pushed Nov 24, 2026. Counts drift over time.
- The install index and the tree drift: analyze-gitops-repo carries 12 installs and a Fail verdict on Gen Agent Trust Hub but has no SKILL.md in the current tree.
- Three of the seven listings are maintainer-facing and live under internal/skills/, so they are less relevant to end users than the three public skills.
- gitops-cluster-debug requires the flux-operator-mcp server and cluster access, and its read-only posture depends on the --read-only flag you pass at setup.
- One sampled skill (analyze-gitops-repo) fails Gen Agent Trust Hub; treat that listing with caution.

## Related

- [Darkmatter Skills - Team Skill Catalog Setup](/hermes/skills/catalog/darkmatter-skills-setup)
- [khasky - Awesome Agent Skills Setup](/hermes/skills/catalog/khasky-awesome-agent-skills-setup)
- [AWS Agent Plugins - Official AWS Plugin Suite Setup](/hermes/skills/catalog/aws-agent-plugins-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Prefer the Flux CLI install; it verifies the cosign signature so you know the OCI artifact is published by the Flux team.
- Omit the --agent flag if your agent reads the conventional .agents/skills path; otherwise pass --agent claude-code or the matching agent name.
- Add --read-only to the flux-operator-mcp server so the agent can inspect but not mutate the cluster.
- Start a new Codex thread after installation so the skills are discovered.
- Keep flux, flux-schema and flux-operator-mcp current; several skills depend on their presence.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
