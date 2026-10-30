---
title: "Auth0 Agent Skills - Identity and OAuth Setup"
description: "auth0/agent-skills: 28.1K combined installs. Official Auth0 skill for login, MFA, SSO, Organizations and migrating off other auth providers."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/auth0-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "auth0", "oauth", "mfa", "identity"]
---

# Auth0 Agent Skills - Setup Guide

**Source:** [auth0/agent-skills](https://www.skills.sh/auth0/agent-skills) via skills.sh - 28.1K combined installs across 47 indexed listings; first seen 2026-10-30 (morning sweep)

**GitHub:** [auth0/agent-skills](https://github.com/auth0/agent-skills) - 55 stars, Apache-2.0 License, branch main, last pushed 2026-10-30 (commit 7ab52d2); one skill in the tree at `plugins/auth0/skills/auth0/SKILL.md`, carrying 70 reference directories (144 files) under `references/`, 12 asset files under `assets/`, `scripts/render_pdf.sh`, `scripts/validate-skill.sh`, `agents/openai.yaml`, per-host plugin manifests for Claude Code, Codex, Cursor and Antigravity, and `plugins/auth0/plugin.json` at version 2.8.0

**Category:** Identity, authentication, OAuth and authorization for agent-built applications

**Quality Tier:** 🟡 Yellow - 4 sampled Warn verdict(s) in the five sampled skills, every one of them in the Snyk column; Apache-2.0, official Auth0 guidance that also reaches a live tenant through the Auth0 CLI

Auth0 is an authentication and authorization platform, and this repository is its own official agent skill rather than a community wrapper. The README states the intent plainly: AI agent skills that help coding assistants implement Auth0 authentication correctly, shipped under Apache-2.0 at version 2.8.0, for Claude Code, Cursor, Codex, Antigravity, Gemini CLI, GitHub Copilot and the 40+ other agents that support the Agent Skills format. The suite is one skill named `auth0`, not a bundle of per-framework skills, and the plugin README lists 37+ frameworks in its coverage line.

What makes it more than a cheat sheet is the routing contract inside `SKILL.md`. It runs four steps: detect intent from a table of plain-language developer goals (integrate, MFA, passkeys, Organizations, enterprise SSO, Universal Portals, custom domains, ACUL, branding, DPoP, token exchange, token vault, audit, health check, guidance, debug, rate limits, migrate, SDK upgrade, tooling), detect the framework in three tiers (an installed Auth0 SDK first, then ordinary framework dependencies in `package.json`, `requirements.txt`, `build.gradle`, `*.csproj`, `composer.json`, `go.mod`, `Package.swift` or `pubspec.yaml`, then the prompt itself), detect the tooling (Auth0 CLI, Terraform, an active Auth0 MCP server, or the Vercel integration), and only then load 2 to 3 reference files. The reference tree is large enough that this selectivity is the point: 144 files across 70 directories, including a per-framework index for each supported stack and per-feature guides that branch again by SDK.

The collection is also wider than framework integration. The same skill audits a tenant for security and configuration problems (CheckMate), scores tenant health and plan fit, debugs 401, 403, CORS, callback-mismatch and redirect-loop failures, walks a migration off Firebase, Cognito, Supabase, Clerk, Okta, NextAuth.js or Passport.js, and upgrades an SDK across a major version. The README is explicit that earlier releases shipped one skill per SDK or framework and that those have been consolidated into `auth0`, a detail that matters when you compare the install index against the current tree.

## Installation

The README's broadest route is the Skills CLI, which works with Claude Code, Cursor, Copilot, Codex and the other Agent Skills clients:

```bash
npx skills add auth0/agent-skills
```

Target specific agents when you do not want the skill offered to everything on the machine:

```bash
npx skills add auth0/agent-skills --agent claude-code cursor
```

The plugin-level README also documents an install scoped to just the plugin directory:

```bash
npx skills add auth0/agent-skills/plugins/auth0
```

Claude Code users get the marketplace route, and the README notes the skill is on the official Claude Code plugins marketplace:

```text
/plugin install auth0@claude-plugins-official
```

```bash
claude plugin install auth0@claude-plugins-official
```

ClawHub is the third distribution channel named in the README:

```bash
npx clawhub install auth0
```

Antigravity and Gemini CLI both install from a local clone. Gemini's `extensions install` expects a manifest at the root of the repository it is given, and this manifest lives at `plugins/auth0/`, so the GitHub URL does not work for that client:

```bash
git clone https://github.com/auth0/agent-skills.git
cd agent-skills

agy plugin install plugins/auth0
```

```bash
git clone https://github.com/auth0/agent-skills.git
cd agent-skills

gemini extensions install ./plugins/auth0
```

Hermes is not one of the hosts this repository generates a manifest for, so the durable route for this profile is a directory copy. Copy the whole skill directory rather than `SKILL.md` alone, because the router's whole mechanism is loading files out of `references/`:

```bash
git clone https://github.com/auth0/agent-skills.git
mkdir -p ~/.hermes/profiles/corpusiq/skills
cp -r agent-skills/plugins/auth0/skills/auth0 ~/.hermes/profiles/corpusiq/skills/auth0
```

That copy lands `SKILL.md`, `references/`, `assets/`, `scripts/` and `agents/` as one unit under `~/.hermes/profiles/corpusiq/skills/auth0/`. Drop `assets/` or `references/` and the skill still activates, but its routing instructions will point at files that are not there.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| auth0 | 5,580 | The consolidated skill and its router: picks an intent from plain-language goals, detects the framework from project manifests, detects tooling, then loads 2 to 3 reference files instead of the whole tree. |
| auth0-quickstart | 2,657 | Quickstart routing when the request does not name a framework: detect the stack, then install the right SDK, create the auth routes, set the environment variables and wire login and logout. |
| auth0-nextjs | 1,630 | Next.js 13+ on the App Router or Pages Router with `@auth0/nextjs-auth0`: protected routes, server-side sessions and the Next.js reference file. |
| auth0-react | 1,457 | React single-page apps on Vite or CRA with `@auth0/auth0-react`, including provider setup and route guarding. |
| auth0-react-native | 963 | React Native CLI apps on the bare workflow with `react-native-auth0`, including the native callback configuration. |
| auth0-express | 816 | Express.js web applications with `express-openid-connect`, including sessions and protected routes. |
| auth0-mfa | 811 | A second factor after the password: TOTP, SMS, email, push and WebAuthn, plus step-up authentication before a sensitive action. |
| auth0-angular | 762 | Angular 13+ applications with `@auth0/auth0-angular`. |
| auth0-vue | 727 | Vue 3 applications with `@auth0/auth0-vue`. |
| auth0-migration | 687 | Moving an existing app off Clerk, NextAuth.js, Firebase, Cognito, Okta, Supabase, Passport.js or custom auth, with the provider-specific migration reference. |
| auth0-nuxt | 594 | Nuxt 3 and Nuxt 4 applications with `@auth0/auth0-nuxt`. |
| auth0-fastify-api | 562 | Fastify APIs used as resource servers: JWT validation and the `fastify-api` variant, with no login UI in play. |
| auth0-fastify | 555 | Fastify web applications with `@auth0/auth0-fastify`, as opposed to the API variant. |
| auth0-expo | 555 | Expo managed-workflow apps with `react-native-auth0`, detected by the presence of `app.json` or `app.config.js`. |

The remaining 33 indexed listings range from 3 to 490 installs.

Those listings are real install counts over retired skill names. The README's migration section records that `auth0-react`, `auth0-nextjs`, `express-oauth2-jwt-bearer` and the rest were folded into the single `auth0` skill, so an install of any name in the table above resolves to the same router today, and a reference to one of the old names in a `CLAUDE.md` or another skill's `requires.skills` now dangles.

## Why This Matters for Hermes Agents

Authentication is the part of an application where a confident wrong answer is expensive: a plausible-looking callback URL, a token audience read from the wrong place, or a session cookie set without the right flags all pass review and fail in production. This skill is built around preventing invention, which is why it queries 144 reference files rather than answering from a summary.

The framework detection is the piece that pays off in unattended runs. A subagent or cron job that wakes up in a repository with no conversational context can still be routed correctly, because the skill reads `package.json`, `requirements.txt`, `build.gradle`, `*.csproj`, `composer.json`, `go.mod`, `Package.swift` and `pubspec.yaml` before it decides anything, and it checks the more specific signals first, so an Ionic project with Capacitor is not mistaken for a plain React app and a Fastify API is not treated as a Fastify web app.

The skill's own instruction for an ambiguous request is worth copying into any prompt you write around it: pick the closest goal, and if the goal is genuinely unclear, ask the developer what they are trying to accomplish rather than guessing an intent. That is the behaviour you want from an agent touching login code.

Two intents reach outside the codebase without mutating anything. `audit` runs a tenant security and configuration review and can then propose fixes, and `healthcheck` returns two scores plus a plan recommendation, which makes both of them reasonable read-first steps before an agent is allowed to change a tenant. The tooling step then decides whether those calls go through the Auth0 CLI, Terraform, an active Auth0 MCP server or the Vercel integration, instead of assuming one.

Because the reference files branch by feature as well as by framework, a request like passkeys in an Expo app and a request like Organizations in a Spring Boot API load different pairs of files from the same skill. For a Hermes profile that installs many skills, that selectivity keeps one identity skill from crowding out the rest of the routing context.

## Usage

| You say | What happens |
|---|---|
| "Add Auth0 login to my Next.js app" | The router matches the integrate intent, reads `package.json` and finds `@auth0/nextjs-auth0`, then loads the framework-nextjs reference with the App Router or Pages Router guidance, SDK install, environment variables and login and logout routes. |
| "Add multi-factor authentication with TOTP" | Intent `feature:mfa`, framework detected from the manifest, and the MFA reference loads for that SDK, covering TOTP enrolment, step-up authentication and the recovery path. |
| "Secure my Express API with Auth0 JWT validation" | The variant step distinguishes a web app from a resource server, so the API branch is chosen for `express-oauth2-jwt-bearer` and the `express-jwt` reference rather than the session-based Express guide. |
| "Migrate from Firebase Auth to Auth0" | Intent `migrate`, which carries the provider-specific migration guidance for Firebase, Cognito, Supabase, Clerk, Okta, NextAuth.js or Passport.js plus the mapping of users, tokens and sessions. |
| "Let business customers log in through their own identity provider" | Intent `feature:enterprise-connect` for B2B SSO, or `feature:organizations` when separate tenants each need their own users, roles and login, loaded per framework. |
| "Audit my tenant and tell me what is misconfigured" | Intent `audit` runs the CheckMate review through the Auth0 CLI, reports findings with a rendered report template, and offers remediation from the audit-remediation reference. |
| "Why does my login redirect loop in Safari?" | Intent `debug` loads the common-errors pattern file alongside the framework reference, which is where callback URL mismatch, cookie and third-party storage problems are covered. |

## Verification

Both raw paths below returned 200 on branch main when this guide was written on 2026-10-30:

```bash
curl -sL -o /dev/null -w "%{http_code} skill\n" \
  https://raw.githubusercontent.com/auth0/agent-skills/main/plugins/auth0/skills/auth0/SKILL.md
curl -sL -o /dev/null -w "%{http_code} nextjs\n" \
  https://raw.githubusercontent.com/auth0/agent-skills/main/plugins/auth0/skills/auth0/references/framework-nextjs/index.md
```

Expect `200` twice, and the second one tells you the reference tree is present at the layout the skill expects. Read the `SKILL.md` before installing: its `description` field is the whole routing contract, and the intent table near the top is what decides whether your request reaches the right reference files.

After the copy lands in the profile, confirm the frontmatter and that the references came with it:

```bash
head -6 ~/.hermes/profiles/corpusiq/skills/auth0/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/auth0/references | wc -l
```

A good copy shows `name: auth0` and a long `description:` in the frontmatter, and the directory count comes back at 70. A count far below that means the copy was partial and the router will point at missing files.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-30) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| auth0 | Pass | Pass | Pass |
| auth0-quickstart | Pass | Pass | Warn |
| auth0-nextjs | Pass | Pass | Warn |
| auth0-react | Pass | Pass | Warn |
| stripe-projects-auth0 | Pass | Pass | Warn |

No FAIL verdict appears in the sampled five, and the one listing that passes all three scanners is the consolidated `auth0` skill you would actually install. The four Warns are all Snyk, and the pack records the verdict rather than the finding behind it, so read those Snyk entries on skills.sh before installing the older per-framework names; three of the four belong to listings that are retired in the tree anyway.

The surface to review here is execution and credentials, not markup. The skill instructs an agent to run the Auth0 CLI, and its frontmatter declares the `auth0` binary as a requirement with a brew install hint, so a session that is told to audit or health-check a tenant is a session with tenant credentials in its environment. Keep management credentials in the shell environment or a credential helper rather than in a prompt, scope the machine-to-machine application to the tenant you are actually working on, and treat `audit` as read-first: the skill's own flow reports before it offers remediation.

## Limitations

- Snapshot data, verified 2026-10-30: 28,077 combined installs across 47 indexed listings; 55 GitHub stars; Apache-2.0; last pushed 2026-10-30. Counts drift over time.
- The install index outruns the tree by a wide margin. skills.sh indexes 47 listings, while the checkout holds exactly one `SKILL.md`, at `plugins/auth0/skills/auth0/SKILL.md`. The README explains it: earlier versions shipped one skill per SDK or framework and those are now consolidated into the single `auth0` skill, which routes to the same guidance by detecting the framework. The per-framework names in the table are historical installs, not separate packages to fetch.
- Old skill names dangle. If a `CLAUDE.md`, another skill's `requires.skills` field or any instruction file references `auth0-react`, `auth0-nextjs`, `express-oauth2-jwt-bearer` or a sibling name, that reference now points at nothing and has to be replaced with `auth0`.
- The entry points disagree in places. The repository README documents `/plugin install auth0@claude-plugins-official`, while `plugins/auth0/README.md` says to add the `auth0/agent-skills` marketplace and then run `/plugin install auth0@auth0-agent-skills`, and the two READMEs give different Skills CLI invocations (`auth0/agent-skills` versus `auth0/agent-skills/plugins/auth0`). Gemini CLI cannot install from the GitHub URL at all, because its manifest lives at `plugins/auth0/` rather than the repository root.
- Several intents need a live service. `audit`, `healthcheck`, `tooling`, tenant setup and anything that creates an application or API run against a real Auth0 tenant through the `auth0` CLI or an MCP server. Without one, the skill still plans the work and explains the failures, but it cannot read or change a tenant.
- Install counts do not rank these skills. Thirteen listings sit between 555 and 1,630 installs, which is publication history rather than adoption signal, and the consolidated `auth0` skill that all of them resolve to ranks at the top on merit as well as count.

## Related

- [Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)
- [Vercel Chat SDK Skills - Chat Bot Development Setup](/hermes/skills/catalog/vercel-chat-sdk-skills-setup)
- [Better Icons - Icon Search Skill Setup](/hermes/skills/catalog/better-auth-better-icons-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Copy the directory, not the markdown. The router's instructions are all of the form "load these 2 to 3 files from `references/`", so a lone `SKILL.md` gives you a skill that describes 144 files it cannot open.
- Install the one `auth0` skill and stop there. Adding the historical per-framework names buys nothing, because they resolve to the same router, and each extra skill description competes for routing attention.
- Force it with `/auth0` when the model is small or the session is crowded. The README records that auto-detection is reliable on capable models but that open-ended questions on smaller models can miss the trigger, and naming the skill removes the selection step entirely.
- Let it read the manifest before you describe the stack. Saying "add login" in a Next.js repository usually lands better than a long prompt, because the tier-1 detection is driven by `package.json`, `requirements.txt`, `build.gradle` and friends, and a wrong framework named in the prompt can beat a correct dependency.
- Start live-tenant work with `audit` or `healthcheck` and read the report before letting the agent change anything. Both are read paths that produce a report template, which gives you a reviewable baseline and a diff after the fix.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
