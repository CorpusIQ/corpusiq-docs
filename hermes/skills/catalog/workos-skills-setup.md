---
title: "WorkOS Skills - AuthKit, SSO, and Reference Router"
description: "workos/skills - 4.9K combined installs across 45 indexed listings: a router skill plus references for AuthKit, SSO, Directory Sync, RBAC, and Vault."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/workos-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-16"
tags: ["hermes skill", "agent skill", "skill setup", "auth", "access management"]
---

# WorkOS Skills - Setup Guide

**Source:** [workos/skills](https://www.skills.sh/workos/skills) via skills.sh - 4.9K combined installs across 45 indexed listings; first seen Nov 16, 2026 (Nov 16 evening sweep)
**GitHub:** 46 stars, MIT license, `main` branch, last pushed 2026-11-02, two skills under `plugins/workos/skills/` with reference files per skill
**Category:** Developer platform - authentication and access management guidance
**Quality Tier:** 🟠 Orange - 4 of 24 sampled skills fail Gen Agent Trust Hub or Snyk, with Snyk warnings on most AuthKit references.

WorkOS ships a two-skill router for coding agents. The `workos` skill maps a task to the right reference file: AuthKit setup per framework, SSO/SAML, Directory Sync, RBAC, FGA, MFA, Vault, Audit Logs, Admin Portal, Pipes, Feature Flags, Radar, webhooks, Custom Domains, migrations from Auth0, Clerk, Cognito, Firebase, Supabase, Stytch, Descope, or Better Auth, and the backend SDKs. The `workos-widgets` skill handles the embedded widgets across Next.js, React, React Router, TanStack Start, Vite, and SvelteKit, with version-checked token issuance.

The 45 indexed listings come from the two registered skills plus each reference file carrying its own install count. The repo also ships as an npm package (`@workos/skills`) with `getReference` and `getSkill` helpers, and it includes an eval framework that runs the same prompt with and without a skill to score the delta.

## Installation

With the skills CLI:

```sh
npx skills add workos/skills
```

This installs two skills, `workos` and `workos-widgets`. The `workos` skill routes to the right reference automatically, so you do not install references individually.

Or by hand: copy `plugins/workos/skills/<name>/` into your agent's skills directory, for example `.claude/skills/` for Claude Code or `.agents/skills/` for agents that read that path. Copy the whole set, since the router dispatches to references by relative path.

For programmatic access from your own tooling:

```sh
npm install @workos/skills
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| workos | 3,633 | Router that maps your task to the right reference: AuthKit, SSO, Directory Sync, RBAC, FGA, MFA, Vault, migrations, and backend SDKs. |
| workos-widgets | 902 | Multi-framework WorkOS widget integration, from frontend detection to version-checked token issuance. |
| workos-authkit-nextjs | 64 | AuthKit setup reference for Next.js App Router. |
| workos-authkit-base | 42 | AuthKit architecture reference shared by the framework guides. |
| workos-authkit-react | 33 | AuthKit setup reference for React SPAs. |

The remaining 40 indexed listings range from 1 to 28 installs.

## Why This Matters for Hermes Agents

The suite solves the stale-guidance problem: WorkOS ships many frameworks and features, and an agent's training data is usually months behind. The `workos` router uses progressive disclosure, loading only the one reference the current task needs, so context stays small while the guidance stays current. AuthKit setup references are the richest, with step-by-step install, decision trees, verification checklists, and error recovery. Each reference leads with doc URLs as the source of truth, then the gotchas agents commonly get wrong from training data. The eval framework is the part worth copying: it scores the same prompt with and without a skill, giving a measurable signal that the skill actually helps. For Hermes agents, the widgets skill's frontend detection plus backend SDK token generation is a self-contained pattern for wiring embedded UI to a hosted platform.

## Usage

| You say | What happens |
|---|---|
| "Add WorkOS SSO with SAML to my app" | The router loads the workos-sso reference and walks the SSO/SAML setup. |
| "Embed the User Management widget in Next.js" | workos-widgets detects the framework, generates access tokens, and wires the component. |
| "Migrate our auth from Auth0" | Loads the workos-migrate-auth0 reference with step-by-step migration guidance. |
| "Set up directory sync from Okta" | Loads the workos-directory-sync reference for IdP directory sync. |
| "Add role-based access control" | Loads the workos-rbac reference for RBAC setup. |
| "Swap my Clerk UserButton for WorkOS" | Recommends the published React components for profile, account, security, and organization UI. |

## Verification

```bash
curl -fsSL https://raw.githubusercontent.com/workos/skills/main/plugins/workos/skills/workos/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/workos/skills/main/plugins/workos/skills/workos-widgets/SKILL.md | head -20
npx skills add workos/skills
```

Each skill is one `SKILL.md` under `plugins/workos/skills/<name>/`; confirm the path exists in the current tree before copying a specific skill.

## Security

skills.sh verdicts for sampled skills (verified Nov 16, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| workos | Pass | Pass | Pass |
| workos-widgets | Pass | Pass | Pass |
| workos-authkit-nextjs | Pass | Pass | Warn |
| workos-authkit-base | Pass | Pass | Warn |
| workos-authkit-react | Pass | Pass | Warn |
| workos-authkit-vanilla-js | Pass | Pass | Warn |
| workos-authkit-tanstack-start | Pass | Pass | Warn |
| workos-authkit-react-router | Pass | Pass | Warn |
| workos-vault | Pass | Pass | Warn |
| workos-sso | Pass | Pass | Warn |
| workos-rbac | Pass | Pass | Warn |
| workos-pipes | Fail | Pass | Fail |
| workos-mfa | Pass | Pass | Warn |
| workos-magic-link | Pass | Pass | Warn |
| workos-integrations | Pass | Pass | Warn |
| workos-fga | Pass | Pass | Warn |
| workos-feature-flags | Fail | Pass | Warn |
| workos-events | Pass | Pass | Warn |
| workos-email | Pass | Pass | Warn |
| workos-domain-verification | Fail | Pass | Warn |
| workos-directory-sync | Pass | Pass | Warn |
| workos-custom-domains | Pass | Pass | Warn |
| workos-audit-logs | Pass | Pass | Warn |
| workos-api-widgets | Pass | Pass | Fail |

Of the 24 sampled skills, 4 fail (workos-pipes, workos-feature-flags, workos-domain-verification, workos-api-widgets) and most AuthKit references carry Snyk warnings, so check the individual scanner pages before relying on them.

## Limitations

- Snapshot data, verified Nov 16, 2026: 4,882 combined installs across 45 indexed listings; 46 GitHub stars; MIT; last pushed 2026-11-02. Counts drift over time.
- 40 of the 45 indexed listings sit at 28 installs or fewer, so most of the catalog is reference files rather than widely used standalone skills.
- 4 of 24 sampled skills fail Gen Agent Trust Hub or Snyk, and most AuthKit references carry Snyk warnings.
- The `workos` router dispatches to references by relative path, so a partial install can leave references missing; copy the whole set.
- New AuthKit setups assume `npx workos@latest install`, and guidance is tuned to the current WorkOS dashboard and CLI.

## Related

- [Appwrite Skills](/hermes/skills/catalog/appwrite-skills-setup)
- [Laravel Boost](/hermes/skills/catalog/laravel-boost-setup)
- [Medusa Agent Skills](/hermes/skills/catalog/medusa-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Copy the whole set: the router loads references by relative path, so a partial install breaks dispatch.
- Start new AuthKit setups with `npx workos@latest install`; it needs no WorkOS account up front.
- Point the agent at doc URLs first; each reference treats the WorkOS docs as the source of truth.
- Run the eval suite with and without a skill to see the measured delta before trusting it in a pipeline.
- Use `getReference` and `getSkill` from `@workos/skills` for programmatic access from your own tooling.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
