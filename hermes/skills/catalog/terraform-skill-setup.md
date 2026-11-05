---
title: "Terraform Skill - IaC Testing and Modules Setup"
description: "antonbabenko/terraform-skill on skills.sh: 7.8K combined installs; Terraform and OpenTofu testing, modules, state and CI/CD for coding agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/terraform-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "terraform", "opentofu", "infrastructure as code"]
---

# Terraform Skill - Setup Guide

**Source:** [antonbabenko/terraform-skill](https://www.skills.sh/antonbabenko/terraform-skill) via skills.sh - 7.8K combined installs across 1 indexed listing; first seen 2026-11-05 (Nov 5, 2026 morning sweep)
**GitHub:** 2,443 stars, license field NOASSERTION, last pushed 2026-10-24, one SKILL.md directory at `skills/terraform-skill`
**Category:** Infrastructure as code for agents: Terraform and OpenTofu testing, modules, state management and CI/CD
**Quality Tier:** 🟡 Beta - licence field NOASSERTION; every sampled audit Pass; 2,443 stars.

Anton Babenko maintains this skill for Terraform and OpenTofu work, and it is aimed at coding agents rather than humans: Claude Code, Cursor, Copilot, Gemini CLI, OpenCode, Codex and Kiro all get an install path in the README. AWS stays the default in the examples, but the same backend, auth, security and resource guidance is written to map onto Azure and GCP on request.

The content is a decision layer, not an API reference. It covers a testing decision matrix that separates static analysis, native `terraform test`, Terratest and policy as code; module hierarchy and naming; remote state backends with locking and multi-team isolation; GitHub Actions and GitLab CI patterns; and Trivy and Checkov scanning. The skill file opens with a diagnosis step, so the agent is told to identify the failure mode before it generates code.

## Installation

The README installs cross-agent through skills.sh:

```bash
npx skills add https://github.com/antonbabenko/terraform-skill
```

Claude Code users install it as a plugin from the author's marketplace:

```text
/plugin marketplace add antonbabenko/agent-plugins
/plugin install terraform-skill@antonbabenko
```

Gemini CLI has its own extension command:

```bash
gemini extensions install https://github.com/antonbabenko/terraform-skill
```

Cursor, OpenCode and Codex take a clone into the directory each host auto-discovers:

```bash
git clone https://github.com/antonbabenko/terraform-skill.git ~/.cursor/skills/terraform-skill
git clone https://github.com/antonbabenko/terraform-skill.git ~/.agents/skills/terraform-skill
```

One warning comes straight from the README: install through `antonbabenko/agent-plugins` and do not also add `antonbabenko/terraform-skill` as a marketplace, because both use the same marketplace name and will clash. The same README recommends the companion `code-intelligence` plugin (`/plugin install code-intelligence@antonbabenko` from the same marketplace), which holds the general code navigation rules that this skill specialises for Terraform.

## What It Provides

One indexed listing, above the threshold.

| Skill | Installs | Use For |
|---|---|---|
| terraform-skill | 7,835 | Writing, reviewing and debugging Terraform or OpenTofu modules, tests, CI, scans and state operations, with version-aware guards |

No indexed listings fall below the threshold.

## Why This Matters for Hermes Agents

Terraform is a domain where a plausible-looking answer is often wrong in a way that only shows up during apply. The skill counters that by forcing diagnosis first: identity churn, secrets in state, blast radius, CI drift and state corruption are named failure modes, and the agent is told to pick one before writing HCL.

The testing matrix is the most useful part for an agent. It answers a question agents routinely guess at, namely whether to reach for `terraform test`, Terratest, or a static scan, and it does so with the version boundary attached: native tests need 1.6 or later, mock providers 1.7 or later, and Terratest is the fallback for older code or teams with Go experience.

The native test rules encode mistakes that large language models make repeatedly, such as indexing a set-type nested block with `[0]`, or asserting on a computed ARN under `command = plan`. A skill that states those constraints up front saves a debugging cycle that would otherwise burn on a failed test run.

For Hermes agents the practical effect is a narrower search space. Instead of generating a module and hoping, the agent has a documented module hierarchy, naming conventions, block ordering and state layout to conform to, which makes its output reviewable against a standard.

## Usage

| You say | What happens |
|---|---|
| "Create a Terraform module for an S3 bucket with tests" | terraform-skill picks the module type, scaffolds the layout and writes native tests with the right command mode |
| "Should this repo use terraform test or Terratest?" | terraform-skill applies the testing decision matrix and answers with the version and cost trade-offs |
| "Review this module for naming and structure" | terraform-skill checks hierarchy, naming, block ordering and variable conventions |
| "Set up a remote state backend with locking" | terraform-skill selects a backend pattern and writes the locking and isolation configuration |
| "Add a GitHub Actions plan and apply pipeline" | terraform-skill produces a CI workflow with the scan and apply stages in order |
| "Add security scanning to this module" | terraform-skill wires Trivy and Checkov into the validation path |
| "Migrate this state to a new backend without downtime" | terraform-skill walks the migration and recovery procedure before touching configuration |

## Verification

Fetch the skill file the installer pulls and read it before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/antonbabenko/terraform-skill/master/skills/terraform-skill/SKILL.md | head -8
```

It should open with `name: terraform-skill` and a description naming Terraform and OpenTofu modules, tests, CI, scans and state operations. The default branch is `master`, not `main`, so any raw URL you script must keep that branch name. Then confirm the install landed where your host looks:

```bash
ls -l ~/.claude/plugins | grep terraform
```

An entry named `terraform-skill` should appear. For the Codex and OpenCode clone path, check the file directly:

```bash
head -4 ~/.agents/skills/terraform-skill/SKILL.md
```

A final functional check from the README: ask "Create a Terraform module with testing for an S3 bucket" and confirm the answer uses the module hierarchy and the test matrix rather than a single flat `main.tf`.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| terraform-skill | Pass | Pass | Pass |

All three sampled audits pass. The skill is guidance only: it ships no executable tooling beyond the Markdown instructions, and it does not hold cloud credentials. The Kiro power variant registers an optional read-only HashiCorp `terraform-mcp-server` in `~/.kiro/settings/mcp.json`, which is a separate server with its own trust decision, and the README says the guidance works without it.

## Limitations

- Snapshot data, verified 2026-11-05: 7,835 combined installs across 1 indexed listing; 2,443 GitHub stars; license field NOASSERTION; last pushed 2026-10-24. Counts drift over time.
- The licence is unresolved by tooling: GitHub reports NOASSERTION while the README badge declares Apache 2.0. The `LICENSE` file itself carries the Apache License 2.0 text behind a copyright and project preamble, which is why GitHub's classifier does not recognise it. Read the file before redistribution.
- The default branch is `master`. Raw URLs written against `main` will 404.
- Guidance only. The agent still needs the `terraform` binary, and the scan and lint steps assume `tflint`, `trivy` and `checkov` are installed.
- Plugin identity clash: adding the repository itself as a marketplace conflicts with `antonbabenko/agent-plugins`, so use one path or the other.
- The Kiro power adds a `POWER.md` generated from the same `SKILL.md`; the content is shared, so editing one copy does not update the other in a local clone.

## Related

- [CC DevOps Skills - Kubernetes and IaC Suite](/hermes/skills/catalog/cc-devops-skills-setup)
- [Pulumi Agent Skills - Infrastructure as Code Setup](/hermes/skills/catalog/pulumi-agent-skills-setup)
- [Railway Agent Skills - Infrastructure Deployment Setup](/hermes/skills/catalog/railway-agent-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Ask for the diagnosis first. The skill is written to name the failure mode (identity churn, secrets, blast radius, CI drift, state corruption) before it writes code, and that step is where most bad modules get caught.
- Use `command = apply` only where it is required, which means computed values and set-type nested blocks. Everything else is faster under `command = plan`.
- Never index a set-type nested block with `[0]`. Use a `for` expression or materialise the block through apply.
- Keep the companion `code-intelligence` plugin installed. It holds the language-agnostic navigation rules so this skill does not repeat them, which keeps the loaded context smaller.
- Pin the module version you generate against, then let the skill's version-aware guards do their job. Advice for Terraform 1.6 or later is wrong in a 1.4 codebase.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
