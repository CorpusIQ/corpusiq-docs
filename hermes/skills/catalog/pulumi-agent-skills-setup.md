---
title: "Pulumi Agent Skills - Infrastructure as Code Setup"
description: "pulumi/agent-skills: 16.4K combined installs. Official Pulumi agent skills for IaC authoring, cloud migration, ESC secrets and provider maintenance."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/pulumi-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "pulumi", "infrastructure as code", "cloud migration", "secrets"]
---

# Pulumi Agent Skills - Setup Guide

**Source:** [pulumi/agent-skills](https://www.skills.sh/pulumi/agent-skills) via skills.sh - 16.4K combined installs across 17 indexed listings; first seen 2026-10-30 (morning sweep)

**GitHub:** [pulumi/agent-skills](https://github.com/pulumi/agent-skills) - 78 stars, Apache-2.0 License, branch main, last pushed 2026-10-09; 17 `SKILL.md` files in four plugin groups, `pulumi/skills/<name>/SKILL.md` (9 skills), `migration/skills/<name>/SKILL.md` (5), `package-maintenance/skills/<name>/SKILL.md` (2) and `delegation/skills/<name>/SKILL.md` (1), each group shipping its own `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json` beside a root `.claude-plugin/marketplace.json`, a root `.codex-plugin/plugin.json`, a Gemini extension manifest in `gemini/`, `evals/` and an `AGENTS.md` that documents the skill conventions

**Category:** Infrastructure as code, cloud provisioning and migration for agents

**Quality Tier:** 🟡 1 sampled Warn verdict(s) - official Pulumi collection covering IaC authoring, cloud migration, provider maintenance and Neo handoff across 17 skills

Pulumi is the infrastructure as code vendor behind the Pulumi CLI and Pulumi Cloud, and `pulumi/agent-skills` is its official skill collection for coding agents. It publishes 17 skills in four groups: `pulumi` for authoring and operating Pulumi itself, `migration` for converting other tools, `package-maintenance` for people who maintain Pulumi provider repositories, and `delegation` for handing work to Pulumi Neo. The repository is Apache-2.0, was pushed on 2026-10-09, and is packaged both as a Claude Code and Codex plugin marketplace and as plain Agent Skills directories that any agentskills.io client can read. The install index carries 17 listings, one per skill, so the skills.sh names and the checked-out tree agree name for name.

The internal split is worth understanding before you install anything. `pulumi-overview` is the router, and its description is written to fire even when the user never says "Pulumi": a request to deploy an app, provision a database, stand up a VPC or configure Auth0 is meant to land there and be routed to a level or a specialist skill. `pulumi-best-practices` carries the program-level rules that break real deployments, `pulumi-esc` covers environments, secrets and short-term credentials, and the five migration skills convert Terraform, AWS CDK, CloudFormation, Azure ARM and Bicep, each with its own importer and conversion notes checked in next to `SKILL.md`.

## Installation

The README's universal route is the skills CLI. It reads the group paths separately and does not read the combined plugin manifest at the repository root, so install group by group:

```bash
npx skills add pulumi/agent-skills/pulumi --skill '*'       # 9 Pulumi skills
npx skills add pulumi/agent-skills/migration --skill '*'    # 5 migration skills
npx skills add pulumi/agent-skills/delegation --skill '*'   # 1 Neo handoff skill
```

Provider authors add the separate maintenance group:

```bash
npx skills add pulumi/agent-skills/package-maintenance --skill '*'
```

Claude Code and Codex use the plugin marketplace instead, where `pulumi` is the combined end-user plugin and `pulumi-migration` or `pulumi-delegation` are subsets that must not be installed alongside it:

```text
/plugin marketplace add pulumi/agent-skills
/plugin install pulumi
```

```bash
codex plugin marketplace add pulumi/agent-skills
gemini extensions install https://github.com/pulumi/agent-skills
```

Hermes is not one of the adapters this repository generates, so the durable route for this profile is a directory copy. Take `pulumi/skills/<name>/` (or the matching directory under `migration/`, `package-maintenance/` or `delegation/`) from a clone and copy it into `~/.hermes/profiles/corpusiq/skills/<name>/`. Copy the whole directory rather than the markdown alone: all 17 skills ship a `use_cases.yaml`, 15 ship an `agents/` directory, `provider-upgrade` and `pulumi-upgrade-provider` ship `references/`, `pulumi-migrate-from-discovered-stack` ships `scripts/`, and the migration skills ship importer notes such as `cdk-convert.md` and `arm-import.md`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| pulumi-best-practices | 2,564 | Writing, reviewing or debugging Pulumi TypeScript and Python programs: Output and apply() rules, avoiding resources created inside apply(), aliases for refactors that must not destroy resources, secrets and config, and preview or CI workflow setup. |
| pulumi-arm-to-pulumi | 2,120 | Converting Azure ARM templates, Bicep templates or ARM code to Pulumi and importing existing Azure resources; ships arm-conversion-patterns.md and arm-import.md beside SKILL.md. |
| pulumi-component | 1,466 | Authoring ComponentResource classes for reusable abstractions, including parent and child resource relationships and the composition rules that keep a component reusable across stacks. |
| pulumi-esc | 1,432 | Pulumi ESC environments, secrets and configuration: short-term credentials, OIDC for AWS, Azure and GCP, integrations with AWS Secrets Manager, Azure Key Vault, HashiCorp Vault and 1Password, and ESC use from Pulumi stacks. |
| pulumi-automation-api | 1,226 | Driving Pulumi from application code through the Automation API instead of the CLI, for programmatic stack creation, previews and updates inside a service. |
| pulumi-terraform-to-pulumi | 965 | Migrating Terraform projects to Pulumi and producing idiomatic Pulumi code in the target language. |
| pulumi-cdk-to-pulumi | 903 | Migrating AWS CDK applications to Pulumi; ships cdk-convert.md, cdk-importer.md and cloudformation-id-lookup.md. |
| cloudformation-to-pulumi | 894 | Migrating AWS CloudFormation stacks and templates to Pulumi, including logical ID lookup for imported resources. |
| provider-upgrade | 862 | Upgrading Pulumi providers without unintended infrastructure changes, with supporting material in references/. |
| package-usage | 839 | Finding which stacks across an organization use a package and at which versions, an organization-wide query rather than a per-project one. |
| pulumi-upgrade-provider | 697 | Automating upgrades in Pulumi provider repositories for provider authors and bridge maintainers, with references/ shipped alongside. |
| upstream-patches | 638 | Creating, amending, removing and rebasing Terraform provider submodule patches through ./scripts/upstream.sh, used by upgrade-provider and by manual patch work. |
| pulumi-overview | 585 | Entry point across pulumi do, IaC projects and Pulumi Cloud that picks the working level first and routes to the specialist skills, including migration requests. |

The remaining 4 indexed listings range from 176 to 441 installs.

## Why This Matters for Hermes Agents

Infrastructure skills usually fail at the same place: the model knows the provider API but not which of six valid workflows the user is in. This collection puts that decision in `pulumi-overview`, which asks the agent to choose between three levels (a stateless `pulumi do` call for one resource, a real Pulumi project with a language and a state file for anything multi-resource, and Pulumi Cloud services for credentials, policy, drift and schedules) before it runs a command. The routing description is unusually explicit about triggers, including requests that never mention Pulumi by name, which is what makes the skill fire from a plain "provision a database" instruction in a Hermes job.

The migration group is the part a builder can measure. Each converter ships its own importer notes and ID-lookup references in the repository (`cdk-convert.md`, `cfn-importer.md`, `arm-conversion-patterns.md`, `cloudformation-id-lookup.md`), so the agent is reading import mechanics rather than improvising a translation, and `pulumi-migrate-from-discovered-stack` handles the narrower case of a stack Pulumi Cloud Discovery has already found.

The safety instructions are the reason to prefer this pack over generic IaC advice. `pulumi-overview` tells the agent not to run a Pulumi command to discover whether a project already exists, because a login-dependent command can silently provision an ephemeral agent account and print a claim banner; the credential-free preflight is `npx pulumi version`. It also states that `pulumi do` writes no state, needs CLI v3.243.0 or newer, and must not mutate resources a project already manages. Those three rules remove the most common way an agent quietly breaks someone's cloud account.

The rest of the suite covers the work around the code: `pulumi-esc` for secrets and OIDC, `provider-upgrade`, `pulumi-upgrade-provider` and `upstream-patches` for maintainers of provider repositories, and `pulumi-neo-handoff`, whose description includes an explicit anti-trigger list so a mention of Neo does not drag a cron into a one-way handoff.

## Usage

| You say | What happens |
|---|---|
| "Use pulumi do to create an S3 bucket and a Cloudflare DNS record" | `pulumi-overview` treats it as a Level 1 task, keeps the two commands stateless, and passes the bucket output into the DNS record as a literal value instead of wiring a resource graph. |
| "Convert this Terraform configuration to Pulumi TypeScript" | The router hands off to `pulumi-terraform-to-pulumi`, which walks the conversion and produces idiomatic Pulumi TypeScript rather than a literal translation. |
| "Help me migrate my CDK application to Pulumi" | `pulumi-cdk-to-pulumi` sequences the migration and pulls CloudFormation logical IDs through `cloudformation-id-lookup.md` so imported resources land in the right place. |
| "Set up AWS OIDC credentials using Pulumi ESC" | `pulumi-esc` configures an environment with dynamic credentials, checks the OIDC trust relationship and shows how the stack consumes the environment. |
| "Help me create a reusable Pulumi component for a web service" | `pulumi-component` guides ComponentResource authoring, including the parent and child relationships and the arguments that keep the component reusable. |
| "Upgrade the Pulumi AWS provider safely without changing real infrastructure" | `provider-upgrade` runs the low-risk upgrade sequence and checks the preview for unexpected replacements before anything is applied. |
| "Hand this off to Neo to apply the staging migration in production" | `pulumi-neo-handoff` packages the goal, repository pointers and a compacted conversation summary into a Pulumi Neo task and returns the task URL. |

## Verification

All three raw paths below returned 200 on branch main when this guide was written on 2026-10-30:

```bash
curl -sL -o /dev/null -w "%{http_code} best-practices\n" \
  https://raw.githubusercontent.com/pulumi/agent-skills/main/pulumi/skills/pulumi-best-practices/SKILL.md
curl -sL -o /dev/null -w "%{http_code} arm-migration\n" \
  https://raw.githubusercontent.com/pulumi/agent-skills/main/migration/skills/pulumi-arm-to-pulumi/SKILL.md
curl -sL -o /dev/null -w "%{http_code} neo-handoff\n" \
  https://raw.githubusercontent.com/pulumi/agent-skills/main/delegation/skills/pulumi-neo-handoff/SKILL.md
```

Expect `200` three times. Read at least the `pulumi-overview` and `pulumi-esc` files before installing, because the whole routing contract for this collection lives in those descriptions, and `pulumi-overview` is the skill that decides whether your agent runs a one-off command or scaffolds a project.

After a copy lands in the profile, confirm the frontmatter and that the supporting directories came across:

```bash
head -4 ~/.hermes/profiles/corpusiq/skills/pulumi-overview/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/pulumi-esc/
```

A good copy shows `name:` and `description:` in the frontmatter and a directory listing that includes `use_cases.yaml` and the `agents/` folder. Only `pulumi-automation-api`, `pulumi-best-practices`, `pulumi-component` and `pulumi-debug-failed-operation` carry a `version` field in frontmatter; the other 13 files carry `name` and `description` only, so a missing version is not a broken copy.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-30) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| pulumi-best-practices | Pass | Pass | Pass |
| pulumi-arm-to-pulumi | Pass | Pass | Pass |
| pulumi-component | Pass | Pass | Pass |
| pulumi-esc | Pass | Pass | Warn |
| pulumi-context-api | Pass | Pass | Pass |

Four of the five sampled skills are clean on all three scanners; the single Warn sits on `pulumi-esc` at Snyk, and the pack records the verdict rather than the finding, so read that Snyk entry on skills.sh before you install the secrets skill. The Warn is plausible on content grounds: `pulumi-esc` is the skill that reasons about OIDC trust policies, environment composition and where credentials come from, which is the highest-consequence material in the collection.

The review that matters is behavioural, not the markdown. Every skill in this repository instructs an agent to run commands in a real cloud account, `pulumi do` included, and `pulumi-overview` documents that an unauthenticated first run can create an ephemeral agent account and print a claim banner. There is no credential handling inside the skills, no token is stored in the repository, and no skill asks for a secret in the transcript, but the skills do assume a Pulumi CLI and a logged-in context. Run them against a scratch stack or a personal organization before letting a scheduled job touch shared infrastructure, and keep provider-repository skills away from anything that is not a checkout of a provider repo, because `upstream-patches` shells out to `./scripts/upstream.sh`.

## Limitations

- Snapshot data, verified 2026-10-30: 16,370 combined installs across 17 indexed listings; 78 GitHub stars; Apache-2.0; last pushed 2026-10-09. Counts drift over time.
- The collection is young and small. Four frontmatter files carry a `version` field, no skill is versioned independently of the repository, and the install counts span 176 to 2,564, so adoption ordering here says more about which skills were published with the launch than about which ones are most useful.
- An unauthenticated first Pulumi command can silently provision an ephemeral agent account with a claim banner, as `pulumi-overview` itself warns. Use `npx pulumi version` as the credential-free preflight, and never run a command just to discover whether a project already exists in the directory.
- `pulumi do` resource verbs need CLI v3.243.0 or newer, write no state at all, and cannot wire outputs between commands, so multi-resource work genuinely belongs in a project rather than a chain of `pulumi do` calls.
- Several skills are inert without a live service or a specific checkout: `package-usage`, `pulumi-context-api` and `pulumi-debug-failed-operation` read records Pulumi Cloud already holds, while `provider-upgrade`, `pulumi-upgrade-provider` and `upstream-patches` assume a Pulumi provider repository with its own build scripts.
- The skills CLI reads the group directories, not the combined plugin manifest at the repository root, so a bare `npx skills add pulumi/agent-skills` is not a documented install route and silently installs only what the CLI discovers at that path.

## Related

- [Agent Toolkit - 44 Skills for Coding Agents Setup](/hermes/skills/catalog/agent-toolkit-setup)
- [Vercel Agent Skills - Official Vercel Collection Setup](/hermes/skills/catalog/vercel-agent-skills-setup)
- [Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the `pulumi` group first and the migration skills on demand. Nine skills already put a routing description, a program-level rule set and a secrets skill in context; the five converters are only load-bearing when a migration is actually in progress.
- Put `npx pulumi version` in the preflight of any job that touches infrastructure. It verifies the CLI without touching Pulumi Cloud, which is the one check that prevents an ephemeral agent account from being created by accident.
- Keep `pulumi-overview` installed in every profile, including ones that only run migration work. Its description is the trigger surface for requests phrased without the word Pulumi, and the migration skills are reachable through it.
- Copy the whole skill directory. `use_cases.yaml`, `agents/`, `references/` and the migration importer notes are what the markdown points at; a markdown-only copy leaves the agent citing files that are not there.
- Treat `pulumi-neo-handoff` as a deliberate tool, not a default. It is a one-way transfer to a hosted service, so keep it out of autonomous jobs that might decide a task looks like a handoff on their own.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
