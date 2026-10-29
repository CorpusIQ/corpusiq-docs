---
title: "Elestio Skill - Managed DevOps Deployment Setup"
description: "Elestio: 7.5K combined installs. An agent skill for deploying and managing VMs, databases, clusters and CI/CD pipelines via the Elestio CLI or MCP."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/elestio-skill-setup/"
robots: "index,follow"
last_updated: "2026-10-29"
tags: ["hermes skill", "agent skill", "skill setup", "elestio", "managed hosting", "infrastructure"]
---

# Elestio - Setup Guide

**Source:** [elestio/elestio-skill](https://www.skills.sh/elestio/elestio-skill) via skills.sh - 7.5K combined installs across 1 indexed listing; snapshot 2026-10-29 (Oct 29 morning sweep)

**GitHub:** [elestio/elestio-skill](https://github.com/elestio/elestio-skill) - 1 star, no LICENSE file at the repository root (the README's own License section says MIT), branch main, last pushed 2026-10-20; the tree is a single root `SKILL.md` (46 KB, version 2.4), a `README.md`, a `.gitignore` and `scripts/install.sh`, with no per-skill directory

**Category:** Managed hosting and PaaS provisioning, database clustering and CI/CD pipeline operations

**Quality Tier:** 🟡 Beta - a genuine vendor skill from the company running the platform, with a detailed procedure and no test suite, held back by 1 GitHub star against 7,467 installs, no LICENSE file at the root, and a Gen Agent Trust Hub FAIL on the listing

Elestio is a fully managed DevOps platform, and its own skill file describes the product precisely enough to judge the skill: dedicated VMs rather than shared Kubernetes, 400+ open-source templates, 10 cloud providers and 100+ regions, with deployment, security updates, backups, monitoring and support handled by the platform. The skill is version 2.4, author `getateam`, last updated 2026-09-22, and it is meant to be read by an agent that has either the official `elestio` CLI installed (`npm install -g elestio`) or the Elestio MCP connector available. It maps every CLI command to its MCP equivalent in a 24-row table, so the same rules apply on either route.

What makes this file worth reading is that it is not a command catalogue bolted onto a marketing page. It opens with a decision tree for the three deployment shapes (managed service on its own VM, cluster with replication, or catalog software running as a pipeline on a shared CI/CD target), then spends a section on the single most common failure in the platform: using `elestio cicd create` for catalog software, which builds an empty pipeline because it knows nothing about the software's ports, environment variables or install scripts, and only produces a running service through `elestio cicd deploy-template`. Around that sit a mandatory interactive procedure that makes the agent ask for provider, region, size, name and admin email one at a time, a `--dry-run` rule for anything that multiplies billed VMs, a rate-limit warning about the API restricting whole accounts after a parallel sweep, and reference tables for provider feature gaps, error handling and the `vmID` versus `serverID` confusion.

## Installation

The README's documented route pipes a remote script into bash. Read it first, because it does three things: it installs the CLI globally, it clones the repository to a temp directory, and it copies `SKILL.md` into whichever of `~/.claude/skills`, `~/.codex/skills`, `~/.config/opencode/skill` or `~/.cursor/skills` exist, deleting an existing `elestio` directory at each destination with `rm -rf` before copying. It exits with an error when none of those four parent directories is present, which is what happens on a machine that only runs Hermes.

```bash
curl -fsSL https://raw.githubusercontent.com/elestio/elestio-skill/main/scripts/install.sh | bash
```

The README also documents the skills.sh CLI form:

```bash
npx skills add elestio/elestio-skill
```

Neither route targets Hermes, so the predictable install is the manual one. The repository has a root `SKILL.md` and no skill directory, so create the directory yourself and fetch the file:

```bash
mkdir -p ~/.hermes/profiles/corpusiq/skills/elestio
curl -sL -o ~/.hermes/profiles/corpusiq/skills/elestio/SKILL.md \
  https://raw.githubusercontent.com/elestio/elestio-skill/main/SKILL.md
```

The skill is useless without the CLI, which the installer would have added for you:

```bash
npm install -g elestio
elestio login --email "you@example.com" --token "your_api_token"
elestio auth test
```

The API token comes from the Elestio dashboard security page, and the SKILL.md is explicit that signup, payment and account approval are human steps: a new account needs a credit card and approval before anything deploys. Nothing is billed by installing or authenticating; billing starts when a service is created.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| elestio | 7467 | Deploying catalog software as an isolated VM (`elestio deploy postgresql --project 112 --name my-db`), as a replicated cluster with `--cluster --nodes N`, or as a pipeline on a shared CI/CD target via `elestio cicd deploy-template`; plus project, firewall, SSL, SSH key, volume, backup, billing, audit-log and cluster operations (promote, failover, resync, add-node, remove-node, lock). |

No indexed listings fall below the threshold.

## Why This Matters for Hermes Agents

Provisioning is where an agent stops being a text generator and starts spending money, and this file is unusually honest about that boundary. The three-shape decision tree removes the guess that normally produces a useless deployment: an agent that picks the pipeline route for Vaultwarden without reading the template's `elestio.yml` gets a pipeline that deploys cleanly and runs nothing, and the skill says so in bold rather than leaving it to error messages.

The dry-run rules are the part worth copying into any infrastructure skill. Cluster billing is per VM, so `--nodes 3` bills three VMs, not one with three replicas; the file requires a `--dry-run` before any cluster deploy and requires the agent to tell the user the VM count and monthly cost. The same pattern appears for `cicd deploy-template` and `clusters add-node`.

The interactive procedure is also a deliberate brake. Instead of accepting defaults, the agent must ask for provider, region, size, service name and admin email in that order, with the size question carrying prices so the human sees the monthly cost before the deploy call. On a host where an agent can be woken by a cron or a chat message and asked to "spin up a database", that is the difference between a confirmed purchase and a surprise invoice.

Two operational details travel outside Elestio. The first is the rate-limit rule: the API throttles bursts and then answers `Access temporarily restricted` on every endpoint including authentication, so it looks like a credentials failure, and a parallel sweep got one account restricted for over half an hour. The second is that the skill refuses to treat an automation as done on a successful API response, requiring `elestio cicd pipelines <vmID>` to show a `success` build before the deployment counts.

The honest caveat is size and coupling. This is a 46 KB single file that describes one vendor's CLI and API in detail, so it competes for context with whatever else your agent loads, and the destructive commands it documents (`delete-service --force`, `clusters delete --force`, firewall opens) are real actions on real servers that a human would otherwise have taken ten minutes to think about.

## Usage

| You say | What happens |
|---|---|
| "Deploy PostgreSQL for the analytics project" | The mandatory procedure asks provider, region, size (with price), service name and admin email one at a time, then runs `elestio deploy postgresql --project <id> --name <name>` and waits for `deploymentStatus = "Deployed"` before handing over credentials. |
| "I need a Redis cache, cheap" | Redis is in the catalog, so the deploy route applies rather than a pipeline, and the agent proposes the smallest size for the chosen provider after checking `elestio sizes --provider <p>`. |
| "Give me a Postgres cluster with two replicas" | The agent runs `elestio deploy postgresql --cluster --nodes 3 --dry-run` first, reports that `--nodes` is the total including the primary and that 3 VMs will be billed, then deploys without the dry-run flag once you confirm. |
| "Run Vaultwarden on the existing CI/CD target" | It uses `elestio cicd templates vaultwarden` to confirm pipeline support, then `elestio cicd deploy-template vaultwarden --target <vmID> --dry-run`, and explicitly does not use `cicd create`, which would build an empty pipeline. |
| "Deploy my app from GitHub" | Only the user's own repository takes this route: a CI/CD target is deployed, then `elestio cicd create --auto --target <vmID> --name my-app --repo owner/repo --mode github`, followed by a build check in `cicd pipelines`. |
| "What is this costing me?" | `elestio billing` reports the total and `elestio billing project <id>` gives the per-service breakdown, while `--dry-run` on any planned deploy shows the price before it is committed. |
| "Delete the staging server and open port 5432" | Both are refused until confirmed: deletions require `--force` plus explicit approval, and firewall changes are funnelled through `elestio firewall` / `firewall-open` with the same confirmation rule the MCP enforces with `"confirm": true`. |

## Verification

The raw paths below returned 200 on the `main` branch when this guide was written, SKILL.md and the installer both:

```bash
curl -sL -o /dev/null -w "%{http_code} SKILL.md\n" \
  https://raw.githubusercontent.com/elestio/elestio-skill/main/SKILL.md
curl -sL -o /dev/null -w "%{http_code} install.sh\n" \
  https://raw.githubusercontent.com/elestio/elestio-skill/main/scripts/install.sh
```

Before installing, read the file and check three things against your own setup: that the frontmatter `name` is `elestio` and `version` is `2.4`, that the CLI version the file requires (`>= 1.4.0` in the compatibility line) is what `elestio --version` reports, and that the MCP mapping table exists, since that is what the file uses instead of CLI calls when a connector is present:

```bash
ls -l ~/.hermes/profiles/corpusiq/skills/elestio/SKILL.md
head -12 ~/.hermes/profiles/corpusiq/skills/elestio/SKILL.md
elestio --version
elestio auth test
```

A `[SUCCESS] Authenticated as user@domain.com` from `auth test` and at least one row from `elestio projects` is the setup being genuinely finished. `elestio templates` needs no credentials at all, so it is the way to confirm the CLI works before the token is in place.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-29) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| elestio | Fail | Warn | Warn W011 |

The single indexed listing, `elestio`, fails Gen Agent Trust Hub and warns on Socket and on Snyk's W011 check. Read the FAIL as a statement about an infrastructure skill rather than a document: this file instructs an agent to create and delete real servers, clusters, firewall rules, volumes and DNS records through an authenticated API, and to read back generated credentials (`elestio credentials`), live logs and the account audit trail. A trust-hub failure on that combination is the verdict that matters most here, because the blast radius of a wrong instruction is a deleted production database or an open port, not a bad paragraph of prose. W011 on Snyk is the same class of finding seen elsewhere in this catalogue (weak or missing security metadata and review signals), and it reinforces rather than overrides the FAIL.

Two concrete behaviours deserve a review before you point this at anything real. The README's installer is a `curl ... | bash` pipe that installs a global npm package, clones a repository, and runs `rm -rf` on an existing `elestio` skills directory before copying into it, so read `scripts/install.sh` and prefer the manual copy route above. And the skill's destructive surface is broad by design: `delete-service --force`, `clusters delete --force`, `remove-node`, `firewall-open`, `backups local-delete` and `volumes delete` all exist, and the file's own protection is the requirement that a human confirm and pass `--force` (or send `"confirm": true` through the MCP). Scope the API token to a dedicated Elestio account or project, keep the token out of agent-readable files, and start on a throwaway project rather than the one holding production data. The licensing position adds a smaller but real concern: no `LICENSE` file exists at the repo root while the README says MIT, so the repository is effectively unlicensed for redistribution until a file appears.

## Limitations

- Snapshot data, verified 2026-10-29: 7467 combined installs across 1 indexed listing; 1 GitHub star; no license file at the repo root; last pushed 2026-10-20. Counts drift over time.
- No `LICENSE` file exists at the repository root and GitHub reports no license, yet the README's own License section says MIT. Treat the repository as unlicensed until the file is added, especially before vendoring `SKILL.md` into an internal skills repo.
- 1 star against 7,467 installs is the widest install-to-community gap in this catalogue sweep. The install count reflects agents pulling a vendor skill, not a reviewed or battle-tested one, and there is no test suite, no eval and no CI in the tree to compensate.
- The pack and the repo disagree on the CLI version floor, and the repo disagrees with itself: the SKILL.md `compatibility` frontmatter requires CLI `>= 1.4.0`, the README's Requirements section says `>= 1.2.0`, the catalog-pipeline section says the full-catalogue route works from `1.3.0`, and rate-limit reporting is attributed to `1.2.3`. Install the latest (`npm install -g elestio@latest`) rather than reasoning about the minimum.
- The bundled installer only targets Claude Code, OpenAI Codex, OpenCode and Cursor, and it exits with an error when none of those parent directories exists. On a Hermes-only host it installs nothing, which is why the manual directory route is the one shown above.
- The whole skill is one 46 KB, roughly 1,096 line `SKILL.md` at the root with no skill directory, so every session that loads it pays that context cost, and the indexed listing name `elestio` matches the directory name you create rather than anything in the upstream tree.
- Version drift is visible inside the file: the header says last updated 2026-09-22 and version 2.4, while the most recent commit (2026-10-20) is a merge that removes snapshot support, and the Snapshots section now says VM snapshots were dropped by Elestio on 2026-08-06 and directs users to backups instead.

## Related

- [Railway Agent Skills - Infrastructure Deployment Setup](/hermes/skills/catalog/railway-agent-skills-setup)
- [Netlify Agent Skills - Serverless Deployment for Hermes Setup](/hermes/skills/catalog/netlify-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Treat the `cicd deploy-template` versus `cicd create` rule as the first thing to memorise. Catalog software in a pipeline goes through `deploy-template` (MCP `deploy_catalog_pipeline`), and `cicd create` on the same template produces a pipeline that deploys and runs nothing, which is the failure the file calls most frequently reported.
- Always take the dry-run, then read it. `--dry-run` on a cluster or on `deploy-template` prints the VM count, cost, ports, environment variables and lifecycle hooks and creates nothing, which makes it the cheapest review step in the whole workflow.
- Keep the interactive parameter procedure even when you are in a hurry. Provider, region, size, name, admin email, in that order, with prices attached to the size question, is what stops a cron-driven agent from buying a `XL-8C-16G` because a default looked reasonable.
- Serialise every loop and stop on `Access temporarily restricted` rather than retrying. The API throttles per account, authentication included, so a fan-out over the 400+ template catalogue can lock you out of every endpoint for half an hour.
- Remember `vmID` and `serverID` are different numbers for the same service. Backup and notes endpoints take `serverID` while actions, firewall and SSL take `vmID`, and passing the wrong one is the mistake the file calls out as the common one.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
