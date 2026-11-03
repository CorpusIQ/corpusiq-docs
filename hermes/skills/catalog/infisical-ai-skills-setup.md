---
title: "Infisical AI Skills - Secrets Management Setup"
description: "Infisical/ai-skills: 7.5K combined installs. 17 skills for secrets management: CLI and SDK setup, API, syncs, dynamic secrets, PKI, KMS and PAM."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/infisical-ai-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-02"
tags: ["hermes skill", "agent skill", "skill setup", "infisical", "secrets management", "security", "devops"]
---

# Infisical AI Skills - Setup Guide

**Source:** [Infisical/ai-skills](https://www.skills.sh/Infisical/ai-skills) via skills.sh - 7.5K combined installs across 18 indexed listings; first documented 2026-11-02 (evening sweep)

**GitHub:** [Infisical/ai-skills](https://github.com/Infisical/ai-skills) - 37 stars, MIT license, branch main, last pushed 2026-10-19; 17 skills under `skills/`, each mirrored as a Claude Code plugin under `plugins/` for 34 skill directories in the tree, plus an `AGENTS.md` router, `evals/` result sets, `docs/`, `tools/` reference generators and a `.claude-plugin/marketplace.json` manifest

**Category:** Secret management for agents: CLI and SDK integration, REST API, secret syncs, dynamic secrets and rotation, PKI, KMS, PAM, Kubernetes operator, SSO and self-hosting

**Quality Tier:** 🟡 Yellow - two of the three sampled listings pass all three auditors and the license is MIT, but the third carries a Socket Warn and one indexed listing does not map to any skill in the repository

This is Infisical's official suite, and the pitch in the repository description is defensive rather than promotional: stop your AI from hallucinating about Infisical secrets management. The README goes further and recommends connecting the docs MCP server at `https://infisical.com/docs/mcp` as the primary route, offering the skills as the offline and local alternative for tools that do not speak MCP. Seventeen skills cover the platform from both ends, from getting a secret into a container to brokering a recorded database session for an AI agent.

The design is built around a failure mode that shows up as soon as a suite has more than a handful of skills: mis-routing. `AGENTS.md` opens with an instruction to read the router before loading anything, then a 17-row intent table and a disambiguation table for the pairs that get confused. Dynamic secrets create a new credential per lease while rotation changes an existing one on a timer; PAM brokers a session and never reveals the credential while dynamic secrets hand one to a workload; an App Connection is Infisical authenticating outward while a machine identity is a workload authenticating inward. Each skill repeats its own boundary in the description frontmatter and again in a "Not this skill" table, because the description is what decides whether the skill loads.

## Installation

The README documents three install paths. The universal one is the CLI:

```bash
npx skills add Infisical/ai-skills
```

Claude Code users can add the repository as a plugin marketplace instead, which is the path that picks up the `plugins/` wrappers:

```bash
/plugin marketplace add Infisical/ai-skills
```

The manual route is a folder copy, and the only decision worth making is which of the two mirrored trees to take. `skills/` is the plain set; `plugins/` is the same 17 skills wrapped in plugin manifests:

```bash
git clone --depth 1 https://github.com/Infisical/ai-skills.git /tmp/infisical-ai-skills
mkdir -p ~/.hermes/profiles/corpusiq/skills/infisical
cp -R /tmp/infisical-ai-skills/skills/. ~/.hermes/profiles/corpusiq/skills/infisical/
```

The README also gives a per-agent table for the manual case: `.claude/skills/` for Claude Code, `~/.codex/skills/` for Codex, `.cursor/skills/` or `.agents/skills/` for Cursor, and `.github/skills/` for GitHub Copilot. If you would rather use the hosted route, the MCP server needs no install at all:

```bash
claude mcp add --transport http infisical-docs https://infisical.com/docs/mcp
```

Nothing in the repository installs Infisical itself. The skills assume you have either a cloud project or a self-hosted instance, and `infisical-self-host` is the skill that deploys one.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| infisical-api | 1,023 | Calling the Infisical REST API directly: secret create, read, update and delete including batch operations, project and environment and machine identity management, Universal Auth bearer tokens, which endpoints paginate and which return everything at a path, and the cloud rate limits. |
| infisical-secret-syncs | 941 | Pushing secrets from Infisical out to third party services across all 48 sync destinations: AWS Secrets Manager, GCP Secret Manager, Azure Key Vault, GitHub, Vercel, HashiCorp Vault, Cloudflare, Snowflake, Databricks and Railway among them, plus key schemas and the initial sync enums. |
| infisical-user-setup-guide | 881 | The listing skills.sh indexes at this name carries the access control and governance description: org and project roles, custom roles built from subject and action permissions, granular secret permissions that separate describing a secret from reading its value, ABAC from user metadata and identity attributes, temporary access, access requests and audit streams. No folder of this name exists in the repository. |
| infisical-agent | 856 | Configuring the Infisical Agent daemon, which manages token lifecycle and renders secrets to files through Go templates without touching application code: the full YAML format, all 6 auth methods (universal-auth, kubernetes, aws-iam, azure, gcp-id-token, gcp-iam), sinks, template functions such as listSecrets and getSecretByName and dynamicSecret, polling and on-change commands. |
| infisical-dynamic-secrets | 763 | On-demand short-lived credentials across all 30 providers: PostgreSQL, MySQL, MSSQL, Oracle, Redis, MongoDB, Elasticsearch, AWS IAM, GCP IAM, Azure Entra ID, SSH certificates, Kubernetes service accounts, LDAP and more, with lease handling. |
| infisical-self-host | 745 | Operating a self-hosted Infisical: Docker and Docker Compose and Kubernetes deployment, environment variables, ENCRYPTION_KEY management, PostgreSQL, Redis with the required noeviction policy, production hardening, FIPS 140-3 compliance, scaling and high availability. |
| infisical-terraform | 511 | The Infisical Terraform Provider: HCL resource configuration, ephemeral secrets, data source patterns, project role permissions and OIDC authentication for Terraform Cloud. |
| infisical-access-control | 189 | Roles and governance in depth: custom roles, the granular secret actions, ABAC, additional privileges, assume-privilege, time-bound temporary access, access requests, change approval and audit streams. |
| infisical-secret-scanning | 179 | Finding leaked credentials: the 3 cloud data sources (GitHub through a GitHub Radar connection, GitLab, Bitbucket), full scans versus automatic diff scans on push, finding lifecycle and severity, and the `infisical scan` CLI over git history, working directories, staged changes and CI, including pre-commit hooks. |
| infisical-app-connections | 179 | Creating the reusable authenticated links that everything else depends on: all 83 connection types with their exact auth methods, from AWS assume-role versus access-key to GitHub OAuth versus GitHub App versus PAT. |
| infisical-secret-rotation | 178 | Rotating credentials that already exist in a third party system on a fixed interval and writing the new values back into secrets: all 28 providers, dual-phase versus single-phase rotation, and the two-user SQL pattern where rotation alternates between two pre-existing accounts. |
| infisical-sso | 165 | Human login and provisioning: Google and GitHub SSO on the free tier, SAML 2.0 and OIDC with Okta, Entra ID, JumpCloud, Google, Auth0, Keycloak, PingOne and GitLab, LDAP login, SCIM user and group provisioning, group to role mapping, enforcement and break-glass access. |
| infisical-gateway | 165 | Reaching private network resources with no inbound firewall rules: the gateway and relay architecture over SSH reverse tunnels, the exact ports and egress allowlist (TCP 2222 to the relay, 443 to Infisical, 8443 platform to relay) and deployment. |
| infisical-pam | 164 | Privileged Access Manager: brokered human and AI agent access to 13 account types, where the connecting party never sees the credential, with session lifecycle, recording, just-in-time access requests and approvals, and the `infisical pam agentic access` path for agents. |
| infisical-kms | 164 | Managed keys and crypto operations without the key leaving the platform: key creation with the three usages (encrypt-decrypt, sign-verify, generate-verify-mac), symmetric algorithms, RSA and ECC and post-quantum ML_DSA keys, plus key rotation. |
| infisical-pki | 162 | Certificate management: all 9 CA types including internal root and intermediate, ACME with Let's Encrypt, AWS Private CA, Microsoft ADCS, DigiCert, Venafi and GoDaddy, certificate profiles, the 4 enrollment methods (API, ACME, EST, SCEP) and 12 PKI syncs. |
| infisical-kubernetes-operator | 153 | Syncing secrets into Kubernetes Secrets and ConfigMaps, pushing them back out, and managing dynamic secret leases in-cluster: the v1beta1 CRDs (InfisicalConnection, InfisicalAuth, InfisicalStaticSecret), the legacy v1alpha1 set, Helm installation and the auto-reload annotation. |
| infisical-setup | 70 | The onboarding path the repository actually ships: interactive setup for the CLI, Docker at build time and runtime, CI/CD for GitHub Actions and GitLab CI, Kubernetes through the operator, and application code across all 9 SDKs, plus choosing among the 13 machine identity auth methods. |

All 18 indexed listings clear the threshold and appear in the table above.

The suite also carries its own evidence. `evals/` holds per-skill A/B results, and the README reports 98 percent Tier 1 accuracy with a skill loaded against 46 percent without, a 52 point delta. The ten skills added in the expansion from 7 to 17 scored 56 of 56 with the skill against 27 of 56 unaided, and the README keeps the null results too: on App Connections the base model already scored 4 of 4, while the Kubernetes Operator scored 0 of 5 because unaided it reaches for the deprecated v1alpha1 CRD. A routing eval over 14 prompts sitting on the seam between similar skills reports 14 of 14 correct after the boundaries were moved into the description frontmatter.

## Why This Matters for Hermes Agents

The repository's own "why this exists" table is the argument for installing it, and it is unusually specific. Models get the Python package name wrong, the Ruby gem and require path differ, Terraform credentials nest inside an `auth` block rather than sitting at the provider root, the secrets list endpoint does not paginate while other endpoints do, paginated responses return a differently named total field, Kubernetes Secrets from the operator do not restart pods without an annotation, and SQL rotation alternates between two pre-existing users rather than rotating one password.

None of those are hard concepts. All of them are the kind of wrong that reads as right, which is the expensive kind when the topic is credentials. An agent that confidently writes `pip install infisical-python` produces a broken build, and an agent that confidently hands a workload a static service token where a machine identity belongs produces a security decision nobody reviewed.

Secrets are also the one domain where a suite that touches project state is worth more than a suite that explains. `infisical-setup` includes a `references/agent-bootstrap.md` written for the case where the agent itself is running the CLI with no interactive terminal, covering login, project creation and `.env` import without the prompts that hang a subprocess. That is a detail only a publisher who has watched an agent stall on a TTY prompt would write.

The maintenance model is the part worth copying. App Connection facts and the API endpoint list are generated from the Infisical source by `tools/generate-app-connection-refs.py`, and CI fails on drift with `--check`, so the counts in the references are derived rather than typed. The README states the consequence plainly: a drifted skill performs worse than no skill, and re-verification is regenerate plus `git diff`.

## Usage

| You say | What happens |
|---|---|
| "Get my secrets into this Docker container" | `infisical-setup` picks build-time or runtime injection, writes the `infisical run` wrapper or the build arg path, and points at `references/docker-integration.md`. |
| "Which SDK call lists secrets in Python?" | `infisical-api` returns the current package name and client class, the correct field accessors on the returned objects, and the correct endpoint version for the region. |
| "Give this app a temporary database password" | `infisical-dynamic-secrets` configures the provider so each request gets a lease on a generated credential, rather than storing a static password. |
| "Push our secrets to AWS and Vercel" | `infisical-secret-syncs` creates the sync per destination, and `infisical-app-connections` supplies the authenticated connection each sync depends on. |
| "Let a support engineer into prod for one hour" | `infisical-pam` sets up a brokered account with a time-bound access request and approval, with the session recorded and the credential never shown. |
| "Deploy an EC2 instance with Terraform using Infisical" | `infisical-terraform` writes the provider with credentials nested in the `auth` block, uses ephemeral resources so the value is never persisted in state. |
| "Rotate our Postgres password every 30 days" | `infisical-secret-rotation` configures the two-user SQL pattern, since one password cannot rotate in place without a second account to alternate into. |

## Verification

The raw path below returned 200 on branch main on 2026-11-02:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/Infisical/ai-skills/main/skills/infisical-setup/SKILL.md
```

After a clone, confirm the reference files came along, since the SKILL.md bodies are short and lean on them:

```bash
git clone --depth 1 https://github.com/Infisical/ai-skills.git /tmp/infisical-ai-skills
find /tmp/infisical-ai-skills/skills -name SKILL.md | wc -l
find /tmp/infisical-ai-skills/plugins -name SKILL.md | wc -l
head -3 /tmp/infisical-ai-skills/skills/infisical-pam/SKILL.md
```

The first two counts both print 17, because `plugins/` mirrors `skills/`, and `head` shows `name: infisical-pam` with a description that ends by naming the skill it is not. Confirm the installed copy carries the references:

```bash
ls ~/.hermes/profiles/corpusiq/skills/infisical/infisical-setup/references
ls ~/.hermes/profiles/corpusiq/skills/infisical | wc -l
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-02) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| infisical-api | Pass | Pass | Pass |
| infisical-secret-syncs | Pass | Pass | Pass |
| infisical-user-setup-guide | Pass | Warn | Pass |

No executable code ships in the skill folders. They are Markdown plus the `tools/` generator and the `evals/` fixtures, and installing a skill does not run anything. The MIT license is a real grant, which makes this one of the easier repositories in the catalog to mirror or adapt.

The risk profile is operational rather than supply chain. An agent with these skills loaded will want to authenticate, create projects, mint machine identities and fetch secret values, and several of the skills describe commands that act on live infrastructure: `infisical login`, secret CRUD, rotation against a database, broker sessions in PAM. Give it a scoped machine identity for a sandbox project, not an admin token, and keep the destructive rotations and syncs behind an explicit confirmation step.

The one Warn sits on the listing whose description is access control guidance, which is content rather than code. Read `infisical-pam/SKILL.md` and `infisical-access-control/SKILL.md` before granting an agent broad platform rights, since PAM explicitly exists to broker agent access and the skill will happily describe giving an agent a recorded session to production.

## Limitations

- Snapshot data, verified 2026-11-02: 7,488 combined installs across 18 indexed listings; 37 GitHub stars; MIT; last pushed 2026-10-19. Counts drift over time.
- The index has 18 listings but the repository has 17 skills. `infisical-user-setup-guide` has no folder, and its description duplicates the access control text, while the repository's onboarding skill is `infisical-setup` at 70 installs.
- The install distribution is long tailed: the top listing has 1,023 and the bottom has 70. Per-listing numbers measure how often one skill was pulled, not how many teams run the suite.
- The accuracy figures in the README are the publisher's own A/B evals, run against assertions the publisher wrote. They are a useful signal of intent, not an independent benchmark.
- Every skill is a vendored snapshot of a moving product. The README says a drifted skill performs worse than no skill, and the only re-verification offered is regenerating the reference files and diffing.
- 17 skills in one namespace means routing matters more than content. The suite mitigates that with descriptions that end in exclusions, but a loader that only reads folder names will still pick badly.
- Nothing works without an Infisical instance. Cloud project or self-hosted deployment first, skills second.

## Related

- [Bagelhole DevOps Security Skills Setup](/hermes/skills/catalog/bagelhole-devops-security-skills-setup)
- [ClawHub Skill Vetting - Security Scanner Setup](/hermes/skills/catalog/clawhub-skill-vetting-setup)
- [Metamask Openclaw Security Analysis Setup](/hermes/skills/catalog/metamask-openclaw-security-analysis-setup)
- [Pulumi Agent Skills - Infrastructure as Code Setup](/hermes/skills/catalog/pulumi-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Put the router in front of the suite. `AGENTS.md` is the disambiguation table, and asking the agent to read it first is cheaper than debugging an answer built from the wrong skill, which is the failure mode the repository itself calls dominant.
- Prefer the docs MCP when you have a choice. The README recommends `https://infisical.com/docs/mcp` as the auto-updating route and positions the skills as the offline fallback, so running both is reasonable but the MCP is the fresher one.
- Use `infisical-setup/references/agent-bootstrap.md` when the agent drives the CLI. It exists because interactive prompts hang a subprocess, and that is exactly what happens on the first `infisical login` without it.
- Scope the identity before the task. A sandbox project plus a narrow machine identity turns a wrong guess into a permission error instead of a production incident.
- Read the generated references as data. The App Connection and API endpoint lists are regenerated from source with a drift check, so when a count disagrees with a docs page, the generated file is the one to trust.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
