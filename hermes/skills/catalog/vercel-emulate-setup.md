---
title: "Vercel Emulate - API Emulators Setup Guide"
description: "vercel-labs/emulate: 3.6K combined installs. Production-fidelity API emulators for local dev, CI and sandboxes across 17 skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/vercel-emulate-setup/"
robots: "index,follow"
last_updated: "2026-11-28"
tags: ["hermes skill", "agent skill", "skill setup", "api emulation", "local development", "ci testing"]
---

# Vercel Emulate - Setup Guide

**Source:** [vercel-labs/emulate](https://www.skills.sh/vercel-labs/emulate) via skills.sh - 3.6K combined installs across 17 indexed listings; first seen Nov 28 2026 (morning sweep)

**GitHub:** [vercel-labs/emulate](https://github.com/vercel-labs/emulate) - 2,113 stars, Apache-2.0 license, branch main, last pushed 2026-11-26; 17 skills under `skills/<name>/SKILL.md`, with each emulated service also published as a `packages/@emulators/<name>` package.

**Category:** API emulators - local, stateful replacements for third-party developer APIs in local dev, CI and no-network sandboxes

**Quality Tier:** 🟠 Orange - Snyk fails next; Warn cells land on emulate (Snyk) and slack (Snyk).

vercel-labs/emulate is a Vercel Labs project that provides local drop-in replacement services for CI and no-network sandboxes, described in the README as fully stateful, production-fidelity API emulation rather than mocks. One command starts fifteen services on loopback ports with no config file needed, spanning Vercel, GitHub, Google, Slack, Apple, Microsoft, Okta, AWS, Resend, Stripe, MongoDB Atlas, Clerk, Linear, Twilio and a deterministic AI service that answers OpenAI and Anthropic SDK calls.

The repository indexes 17 skills on skills.sh: one per emulated service, plus the core emulate skill and the next and nuxt adapters for embedding emulators inside a Next.js or Nuxt app. Each skill lives at `skills/<name>/SKILL.md` and ships alongside the matching `@emulators/*` package in the monorepo, so the same emulator can be reached through the CLI, the programmatic API, or an embedded route handler.

## Installation

The CLI starts every service with one command and no config file:

```bash
npx emulate
```

Start a subset or customize with the CLI flags:

```bash
npx emulate --service vercel,github
npx emulate --port 3000
npx emulate --seed config.yaml
npx emulate init
npx emulate init --service vercel
npx emulate list
```

Install the programmatic API for test setup, and build custom emulators from a scaffold:

```bash
npm install emulate
npm install -D emulate
npx emulate init --custom inventory
npx emulate start --watch
```

To embed emulators in a Next.js or Nuxt app on the same origin, install the adapter plus the service packages you need:

```bash
npm install @emulators/adapter-next @emulators/github @emulators/google
npm install @emulators/adapter-nuxt @emulators/github @emulators/google
```

All services listen on 127.0.0.1 by default. Use `npx emulate start --host 0.0.0.0` for container or cross-machine access, and `--base-url` for the advertised URLs used by OAuth redirects.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| emulate | 584 | Start emulated services, configure seed data, write tests against local APIs and set up CI without network access, via the emulate CLI or programmatic API. |

The remaining 16 indexed listings range from 15 to 395 installs: one listing per emulated service (google, stripe, resend, aws, github, apple, vercel, slack, microsoft, linear, twilio, custom-apis, mongoatlas and ai) plus the next and nuxt framework adapters.

## Why This Matters for Hermes Agents

Local API emulation is the fastest way to make a Hermes agent's integration code testable: instead of real credentials, rate limits and network calls, tests run against a stateful local server that reproduces the provider's wire format. The CLI starts fifteen services on loopback with no config, so an agent building against the GitHub, Slack, Stripe or Vercel APIs can script its flows in CI without keys or connectivity.

The ai service is the standout for agent builders: it answers the OpenAI Responses, Chat Completions, Anthropic Messages and Gemini surfaces with deterministic, rule-driven replies, so an agent that calls a model can be tested offline, including streaming, tool loops, refusals, retries and errors, at zero cost. The next and nuxt adapters solve the preview-deployment problem of OAuth callback URLs by embedding emulators on the same origin.

Each service ships both as a skill (`skills/<name>/SKILL.md`, which documents triggers and setup) and as an `@emulators/*` package, so the same emulator is reachable through the CLI, the programmatic API, or an embedded route handler. Custom emulators extend the pattern to any third-party HTTP API an agent depends on, defined in TypeScript with seeds, resets, persistence and request inspection.

## Usage

| You say | What happens |
|---|---|
| "Start all the emulated services locally" | `npx emulate` launches every service on loopback ports 4000 through 4014. |
| "Run just the Stripe and GitHub emulators" | `npx emulate --service stripe,github` starts only those two services. |
| "Test my Stripe checkout without hitting real Stripe" | The stripe skill seeds products, prices and customers and processes checkout and webhooks locally. |
| "Test Google sign-in and Gmail offline" | The google skill serves OIDC discovery, token exchange, Gmail, Calendar and Drive. |
| "Mock the OpenAI SDK in my tests" | The ai skill returns deterministic Responses, Chat Completions and Anthropic Messages. |
| "Embed emulators in my Next.js preview app" | The next skill wires createEmulateHandler and withEmulate for same-origin OAuth. |
| "Build an emulator for my own vendor API" | The custom-apis skill scaffolds one with `npx emulate init --custom`. |

## Verification

Before installing, fetch a skill's SKILL.md directly to read its frontmatter and instructions. The layout on branch main is `skills/<name>/SKILL.md`:

```bash
curl -sL https://raw.githubusercontent.com/vercel-labs/emulate/main/skills/emulate/SKILL.md
```

After a clone, confirm the skill directories:

```bash
git clone --depth 1 https://github.com/vercel-labs/emulate.git /tmp/emulate
ls /tmp/emulate/skills/
```

The skills listing should show 17 skill directories (ai through vercel). The core CLI lives under `packages/emulate/` and each service under `packages/@emulators/<name>/`.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| emulate | Pass | Pass | Warn |
| google | Pass | Pass | Pass |
| stripe | Pass | Pass | Pass |
| resend | Pass | Pass | Pass |
| aws | Pass | Pass | Pass |
| github | Pass | Pass | Pass |
| apple | Pass | Pass | Pass |
| vercel | Pass | Pass | Pass |
| slack | Pass | Pass | Warn |
| next | Pass | Pass | Fail |
| microsoft | Pass | Pass | Pass |
| linear | Pass | Pass | Pass |
| nuxt | Pass | Pass | Pass |
| twilio | Pass | Pass | Pass |
| custom-apis | Pass | Pass | Pass |
| mongoatlas | Pass | Pass | Pass |
| ai | Pass | Pass | Pass |

This guide is Orange because Snyk fails next. The Gen Agent Trust Hub passes all 17 sampled listings, and the Warn cells sit on emulate (Snyk) and slack (Snyk).

## Limitations

- Snapshot data, verified 2026-11-28: 3,558 combined installs across 17 indexed listings; 2,113 GitHub stars; Apache-2.0 license; last pushed 2026-11-26. Counts drift over time.
- The 17 indexed listings map one-to-one to the `skills/` directories in the current tree, so there is no index-versus-tree drift to reconcile.
- Emulation is stateful and production-fidelity but not exhaustive: several services document unimplemented areas, including Slack Connect invitation flows, Twilio carrier delivery, and Linear full schema coverage.
- The ai service is rule-driven, not a real model: replies are scripted, so it cannot stand in for the actual providers' behavior and quality.
- HTTPS with trusted certificates requires the separate portless CLI (`npm i -g portless`); otherwise services listen on HTTP loopback by default.
- Re-check the skills.sh security pages before production use, since Snyk flags next (Fail) and emulate and slack (Warn).

## Related

- [Vercel Agent Skills - Official Vercel Collection Setup](/hermes/skills/catalog/vercel-agent-skills-setup)
- [Resend Agent Skills - Setup Guide](/hermes/skills/catalog/resend-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with a bare `npx emulate` to bring up all fifteen services, then read the specific `skills/<name>/SKILL.md` before wiring a service into a test.
- Use `--service` to run only what a test needs, and `--seed config.yaml` for repeatable fixture state.
- For CI with no network, the CLI and the programmatic `createEmulator` API are the simplest path; use the next or nuxt adapters only when you need same-origin OAuth in preview deployments.
- Script the ai service's rules to return the exact replies your tests expect, rather than relying on default echo behavior.
- Check the skills.sh security pages before adopting, since the next skill carries a Snyk Fail.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
