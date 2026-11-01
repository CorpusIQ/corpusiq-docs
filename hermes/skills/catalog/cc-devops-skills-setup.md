---
title: "CC DevOps Skills - Kubernetes and IaC Suite"
description: "akin-ozer/cc-devops-skills: 22.2K combined installs. Thirty-one DevOps skills pairing generators with validators across Terraform, Kubernetes and CI."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/cc-devops-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-31"
tags: ["hermes skill", "agent skill", "skill setup", "devops", "kubernetes", "terraform", "ci pipelines"]
---

# CC DevOps Skills - Setup Guide

**Source:** [akin-ozer/cc-devops-skills](https://www.skills.sh/akin-ozer/cc-devops-skills) via skills.sh - 22.2K combined installs across 31 indexed listings; first seen 2026-10-31 (evening sweep)

**GitHub:** [akin-ozer/cc-devops-skills](https://github.com/akin-ozer/cc-devops-skills) - 330 stars, Apache-2.0, branch main, last pushed 2026-07-26; 31 `SKILL.md` files, one per directory under `devops-skills-plugin/skills/`, most adding `scripts/`, `assets/`, `examples/` and a `test/` or `tests/` directory, with 21 of the 31 carrying a `references/` folder

**Category:** DevOps and platform engineering for agents: Kubernetes, Terraform, CI pipelines and incident work

**Quality Tier:** 🟡 Yellow - ansible-validator carries a Warn from all three auditors and makefile-validator from two of them, while the other three sampled skills are clean Passes

The README states the shape of this pack in one sentence: 31 skills, made up of 16 generators for scaffolding configuration, 14 validators for linting and dry-run checks, and one debugger, `k8s-debug`, for cluster troubleshooting. The skill catalogue is grouped by domain and the grouping is even rather than lopsided: six infrastructure-as-code skills split across Ansible, Terraform and Terragrunt, eight CI/CD skills across Azure Pipelines, GitHub Actions, GitLab CI and Jenkins, seven container and Kubernetes skills, six observability and logging skills, and four scripting and build skills. The stated goal is to make infra and pipeline work faster without skipping correctness checks, and the README is candid that this is the whole design thesis.

The mechanism is the generator and validator pair. Most generators name their matching validator as the follow-up step: `jenkinsfile-generator` says generated files are validated with the `jenkinsfile-validator` skill, and `terraform-generator` marks `Skill(devops-skills:terraform-validator)` as REQUIRED after generation. The README's own usage section shows the loop as ask a generator, create the artifact, run the matching validator, patch and re-run until the checks pass. The exception is the two query and configuration generators in the observability group: there is no `logql-validator` or `loki-validator` listing, so those two end at generation, with `loki-config-generator` running its own validation stage before deployment. The validators in turn behave like tools rather than writing assistants. `k8s-yaml-validator` declares itself REPORT-ONLY and forbids file edits or fix offers, `helm-validator` is read-only by default and only changes files when explicitly asked, and the README documents the real command chains behind them, for example `terraform fmt` then `tflint` then `terraform validate` then Checkov for `terraform-validator`, and `helm lint` then `helm template` then `kubeconform` for `helm-validator`.

The pack is also unusually honest about degraded environments. Many skills run shell or Python checks straight out of their own `scripts/` folders, and when a tool is missing they degrade gracefully and say what was skipped instead of failing silently. `ansible-validator` makes that explicit for Molecule: it attempts role testing automatically, marks it `BLOCKED` when the runtime cannot support it, and continues the remaining checks.

## Installation

The README leads with the Claude Code plugin marketplace:

```bash
/plugin marketplace add akin-ozer/cc-devops-skills
/plugin install devops-skills@akin-ozer
```

Codex desktop has a skills-only installer that points at the packaged skills directory:

```bash
$skill-installer install https://github.com/akin-ozer/cc-devops-skills/tree/main/devops-skills-plugin/skills
```

The manual Codex route clones the repo and links the packaged plugin, then registers it in `~/.agents/plugins/marketplace.json`:

```bash
git clone https://github.com/akin-ozer/cc-devops-skills.git ~/.codex/devops-skills
mkdir -p ~/plugins ~/.agents/plugins
ln -s ~/.codex/devops-skills/devops-skills-plugin ~/plugins/devops-skills
```

The packaged Claude manifest is `devops-skills-plugin/.claude-plugin/plugin.json` and the Codex manifest sits beside it at `devops-skills-plugin/.codex-plugin/plugin.json`, both pointing at the same `skills/` directory. Team rollout is documented as an `extraKnownMarketplaces` entry in a project-level `.claude/settings.json`, with `akin-ozer/cc-devops-skills` as the GitHub source.

There is no skills.sh CLI command in this README, so `npx skills add` is not a documented route here. The durable install for a Hermes profile is a directory copy, and it has to copy whole directories rather than just each `SKILL.md`, because the validators ship their checking logic as scripts:

```bash
git clone --depth 1 https://github.com/akin-ozer/cc-devops-skills.git /tmp/cc-devops-skills
cp -r /tmp/cc-devops-skills/devops-skills-plugin/skills/. ~/.hermes/profiles/corpusiq/skills/
```

The prerequisite list is per domain rather than global. The baseline is `bash` and `python3`, with 3.8 or newer recommended and 3.9 or newer for some security tooling. Terraform work wants `terraform`, `tflint`, `terragrunt` and `checkov`, Kubernetes and Helm work wants `kubectl`, `kubeconform`, `helm` and `yamllint`, Docker wants `hadolint`, GitHub Actions wants `actionlint` and `act`, shell work wants `shellcheck`, and Prometheus work wants `promtool`. The README's macOS example installs them with brew, pipx and `helm plugin install` for `helm-diff`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| ansible-validator | 1,386 | Validating, linting, auditing and debugging Ansible playbooks, roles, inventories and FQCN usage, including automatic Molecule role tests that are marked `BLOCKED` with a reason when the runtime cannot run them. |
| terragrunt-generator | 1,215 | Scaffolding Terragrunt HCL: `root.hcl`, `terragrunt.hcl`, child modules, stacks and multi-environment layouts, with generated configuration validated in the same pass. |
| k8s-debug | 843 | Diagnosing and fixing pods in CrashLoopBackOff or Pending, DNS and networking faults, storage issues and rollout failures with kubectl, through a deterministic safety-first workflow. |
| ansible-generator | 843 | Generating Ansible playbooks, roles, tasks, handlers, inventories and vars, with trigger phrases covering deployment playbooks and TLS setup. |
| jenkinsfile-generator | 827 | Generating declarative or scripted Jenkinsfiles and shared-library pipelines, then handing the result to `jenkinsfile-validator`. |
| dockerfile-validator | 756 | Linting and security-scanning Dockerfiles with deterministic stages, severity reporting and explicit fallbacks when tools or network access are constrained. |
| dockerfile-generator | 712 | Writing multi-stage, security-hardened Dockerfiles with optimised layer structure and automatic validation with iterative fixes. |
| gitlab-ci-validator | 696 | Validating, linting and securing `.gitlab-ci.yml` pipelines, stages and jobs, with strict and test-only modes and bundled test fixtures. |
| bash-script-validator | 694 | Checking shell scripts in layers: syntax with `bash -n` or `sh -n`, then ShellCheck-oriented lint and audit passes. |
| k8s-yaml-validator | 687 | Validating Kubernetes manifests as a report-only tool: CRD detection, `kubeconform` schema checks and a `kubectl --dry-run` flow, with suggested fixes shown as before and after blocks. |
| helm-validator | 686 | Validating Helm charts: `helm lint`, `helm template`, YAML and schema validation, CRD documentation lookup and security checks, read-only by default. |
| bash-script-generator | 682 | Creating production-ready Bash scripts, automation and CLI helpers through requirements capture, deterministic generation and validation-first iteration. |
| jenkinsfile-validator | 678 | Validating Jenkinsfiles and shared-library pipeline code with local scripts first, then optional enrichment from plugin documentation. |
| terragrunt-validator | 673 | Validating Terragrunt HCL files, stacks, module wiring and compliance, with bundled test fixtures. |
| k8s-yaml-generator | 667 | Generating Kubernetes manifests including CRDs, Deployments, Services, ConfigMaps, Ingress, RBAC and StatefulSets, with bounded CRD research and mandatory validation. |
| azure-pipelines-generator | 664 | Generating `azure-pipelines.yml` with stages, jobs, steps and reusable templates through deterministic steps and explicit fallbacks. |
| gitlab-ci-generator | 659 | Generating `.gitlab-ci.yml` pipelines, stages and jobs. |
| github-actions-generator | 655 | Scaffolding GitHub Actions workflows and `action.yml` actions, then validating them with `github-actions-validator`. |
| terraform-validator | 654 | Running the full Terraform check chain: `terraform fmt`, `tflint`, `terraform validate`, Checkov, and an optional `terraform plan`. |
| github-actions-validator | 654 | Validating and runtime-testing workflows under `.github/workflows` with `actionlint` static checks plus `act`. |

The remaining 11 indexed listings range from 596 to 652 installs.

## Why This Matters for Hermes Agents

Infrastructure work is where a fluent model does the most damage, because a wrong `resources:` block or a missing `depends_on` fails at apply time rather than at review time. This pack's answer is not better prose, it is a second opinion: an agent that scaffolds a Terraform module with `terraform-generator` is expected to immediately run `terraform-validator`, which runs the real binaries and reports what actually broke instead of asking the model to reread its own output.

The validators also encode environment honesty. Skills that depend on external binaries check for them, degrade to the checks they can still run, and tell the operator what was skipped, which matters on a host where `tflint` or `act` may not be installed. That behaviour is written into the skills rather than left to the model's judgement, and it is the difference between a report that says "clean" and a report that says "clean as far as I could verify".

The read-only default is the other half. `k8s-yaml-validator` explicitly forbids editing files or offering to fix them, and `helm-validator` follows the same rule unless asked otherwise, so an agent reviewing a chart or a manifest set cannot quietly rewrite the thing it was asked to inspect. When a fix is wanted, the driver skill is the generator, and the report stays a report.

Coverage is the practical argument for a single pack over individual skills. Terraform, Terragrunt, Ansible, Helm, Kubernetes YAML, Dockerfiles, five CI systems, Makefiles, shell scripts and the Prometheus and Loki query languages are all covered by the same convention: a generator to scaffold and a validator to gate. An agent profile that carries all 31 gets consistent behaviour across the stack instead of five unrelated house styles.

## Usage

| You say | What happens |
|---|---|
| "Scaffold a reusable AWS VPC module with outputs and examples" | `terraform-generator` writes the module, then `terraform-validator` runs fmt, tflint, validate and Checkov against it. |
| "Validate ./infra/vpc and list only high-severity findings" | `terraform-validator` runs the check chain and returns the severity-filtered report. |
| "Diagnose pods stuck in Pending in the payments namespace" | `k8s-debug` walks cluster state with kubectl through its deterministic troubleshooting workflow. |
| "Generate a Jenkins deployment pipeline with approvals" | `jenkinsfile-generator` writes the declarative pipeline and hands it to `jenkinsfile-validator`. |
| "Scan this Dockerfile for security problems, do not edit it" | `dockerfile-validator` runs its scripted lint and security path and reports findings with explicit fallbacks. |
| "Check this Helm chart but leave the templates alone" | `helm-validator` lints, templates and schema-checks the chart and proposes changes without applying them. |
| "Add a GitHub Actions workflow for PR linting" | `github-actions-generator` scaffolds the workflow, and `github-actions-validator` runs `actionlint` plus `act`. |

## Verification

The raw path for the top skill returned HTTP 200 on branch main when this guide was written on 2026-10-31:

```bash
curl -sL -o /dev/null -w "%{http_code} ansible-validator\n" \
  https://raw.githubusercontent.com/akin-ozer/cc-devops-skills/main/devops-skills-plugin/skills/ansible-validator/SKILL.md
```

Expect `200`. After the copy lands, confirm the count and that the scripts came along, since the validators are useless without them:

```bash
ls /tmp/cc-devops-skills/devops-skills-plugin/skills | wc -l
ls ~/.hermes/profiles/corpusiq/skills/ansible-validator
head -4 ~/.hermes/profiles/corpusiq/skills/terraform-validator/SKILL.md
```

The count should print 31, the directory listing should show `SKILL.md` alongside `scripts`, `references`, `assets`, `test`, and the header should show `name: terraform-validator` with a one-line `description`. If a validator directory arrives with only `SKILL.md`, the copy skipped subdirectories and its checks will not run.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-31) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ansible-validator | Warn | Warn | Warn |
| gitlab-ci-validator | Pass | Pass | Pass |
| azure-pipelines-generator | Pass | Pass | Pass |
| makefile-validator | Pass | Warn | Warn |
| loki-config-generator | Pass | Pass | Pass |

The content surface is markdown plus checking scripts, with no package to install, no build step and no postinstall hook. What raises flags is behaviour rather than payload: these skills run shell and Python validation scripts and invoke real binaries such as `terraform plan`, `kubeconform`, `helm template` and `act`. `ansible-validator`, the only skill to draw a Warn from all three auditors, is also the heaviest of them, running syntax, lint, check-mode, role tests and security scanning in one flow. `makefile-validator` draws Socket and Snyk Warns without a Trust Hub Warn, which is the usual shape for a skill that shells out to a linter.

The operational risk is blast radius, not exfiltration. A validator that can run `terraform plan` or `kubectl --dry-run` against a live cluster needs read credentials with production access to be useful, so scope the kubeconfig and cloud profiles the agent session can see, and keep write access out of the environment entirely. `k8s-debug` goes further than read-only and takes fixes, which means its cluster context should be the least privileged one that can still reproduce the problem.

## Limitations

- Snapshot data, verified 2026-10-31: 22,236 combined installs across 31 indexed listings; 330 GitHub stars; Apache-2.0; last pushed 2026-07-26. Counts drift over time.
- The repository has not been pushed to since 2026-07-26, so tool behaviour it documents (Checkov, `kubeconform`, `act` flags in particular) can lag the installed releases.
- The only documented install routes are the Claude Code marketplace, the Codex skills installer and manual plugin linking. There is no `npx skills add` command in the README, so a Hermes profile install is a manual directory copy.
- Nothing works without the external toolchain. Each domain needs its own binaries, and a host missing `tflint`, `actionlint`, `hadolint` or `promtool` gets degraded validator reports that say what was skipped, not a clean bill of health.
- Several skills are explicitly read-only by default, so "fix this manifest" style requests are answered with a report and proposed diffs rather than applied edits unless the operator asks for the change.
- Install counts are not a ranking of depth. `terraform-validator` and `github-actions-validator` sit last in the table at 654 while carrying the most orchestration, and `k8s-debug` sits third at 843 as the pack's only debugging skill.

## Related

- [OrchestKit - Orchestration and DevOps Skills](/hermes/skills/catalog/orchestkit-skills-setup)
- [Lev Nikolaevich Skills - DevOps and Delivery Setup](/hermes/skills/catalog/levnikolaevich-claude-code-skills-setup)
- [Dot Skills - 96-Skill Agent Engineering Collection Setup - Setup Guide](/hermes/skills/catalog/dot-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the pairs, not single skills. Every generator is written to hand off to its validator, and a profile carrying only the generators gets scaffolding with no gate.
- Run the validator as a separate step and keep its report. The read-only skills are designed to be quoted back to a human, and the report is far more useful than a rewritten file when the change is going to a PR.
- Check the toolchain before trusting a clean result. A validator that could not find `checkov` or `act` will say so in its fallback notes, and that note is the difference between verified and unverified.
- Use `k8s-debug` against a minimally privileged kubeconfig. It is the one skill in the pack that proposes fixes to a live cluster.
- The repository also ships a drop-in wrapper around `anthropics/claude-code-action@v1` at `akin-ozer/cc-devops-skills@v1`, which injects these skills by default in CI and can be run as pure passthrough with `inject_devops_skills: "false"`.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
