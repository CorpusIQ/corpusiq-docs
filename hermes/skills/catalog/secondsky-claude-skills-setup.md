---
title: "SecondSky Claude Skills - Backend and API Suite Setup"
description: "secondsky/claude-skills: 85.1K combined installs. A 145-plugin Claude Code suite for Tailwind, React, Bun, Cloudflare and API backend work."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/secondsky-claude-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "api backend", "cloudflare workers", "claude code"]
---

# SecondSky Claude Skills - Setup Guide

**Source:** [secondsky/claude-skills](https://www.skills.sh/secondsky/claude-skills) via skills.sh - 85.1K combined installs across 200 indexed listings; first seen 2026-10-30 (evening sweep)

**GitHub:** [secondsky/claude-skills](https://github.com/secondsky/claude-skills) - 240 stars, MIT, branch main, last pushed 2026-09-26; 187 `SKILL.md` files, each nested one plugin deep at `plugins/<plugin>/skills/<skill>/SKILL.md` across 145 plugin directories, beside `docs/`, `schemas/`, `scripts/`, `templates/`, `MARKETPLACE.md` and both a `.claude-plugin/` and a `.codex-plugin/` manifest tree

**Category:** Backend, API and frontend skill suite for Claude Code and Codex CLI

**Quality Tier:** 🟢 Green - all five sampled skills Pass on all three scanners, and the whole collection ships under a single MIT licence at 240 stars

SecondSky Claude Skills is published by the Claude Skills Maintainers collective as `secondsky/claude-skills`, a curated collection aimed at people building modern web applications: Tailwind CSS v4 with shadcn/ui, React and Vue component libraries, Vitest and Playwright testing, the Bun runtime, Cloudflare Workers and D1, plus an explicit API track that walks from resource naming and contract testing through authentication, rate limiting, pagination, idempotency and versioning. The README describes it as 145 production-ready skills in 18 categories, at version 3.9.0 and last updated 2026-09-09, with 400 or more documented errors prevented across the set.

The packaging is the interesting part. Each skill sits in its own plugin directory with a plugin manifest, so Claude Code installs from a marketplace command and Codex CLI installs from the same repository natively, while harnesses without a marketplace reach the identical `SKILL.md` files through skills.sh and the `npx skills` CLI. That makes this suite one of the few large collections that is genuinely portable: the same file that Claude Code loads is the file a Hermes profile can vendor, with no build step and no server.

## Installation

The README's recommended route is the Claude Code marketplace, one command to add the repository and one per skill:

```bash
# Add the marketplace
/plugin marketplace add https://github.com/secondsky/claude-skills

# Install individual skills as needed
/plugin install cloudflare-d1@claude-skills
/plugin install tailwind-v4-shadcn@claude-skills
/plugin install gemini-cli@claude-skills
```

Codex CLI has a native path from the generated manifests:

```bash
codex plugin marketplace add secondsky/claude-skills
# then /plugins in the Codex TUI to browse and Space to enable
```

For Hermes and every other harness without a marketplace, the README's cross-harness route is skills.sh, which auto-detects the agent and installs into its own directory:

```bash
npx skills add secondsky/claude-skills --skill api-authentication

# Several at once
npx skills add secondsky/claude-skills --skill rest-api-design --skill api-testing

# List, search, update, remove
npx skills ls -g
npx skills find cloudflare
npx skills update api-authentication
npx skills remove api-authentication
```

Install by name, not with `--all`. The README warns that bulk discovery walks the standard container directories such as `skills/` and `.claude/skills/`, while this repo nests everything under `plugins/<plugin>/skills/<skill>/`, so a single `--all` pass may not pick up the whole collection; `npx skills add secondsky/claude-skills -l` lists what it actually finds. The checkout used for this guide holds 187 `SKILL.md` files, so that is the verified size of the tree, not the README's 145 figure.

A direct vendor copy is the other option, one skill directory at a time:

```bash
cp -r plugins/api-authentication/skills/api-authentication \
  ~/.hermes/profiles/corpusiq/skills/api-authentication
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| tailwind-v4-shadcn | 8,128 | Production setup for Tailwind CSS v4 with shadcn/ui and Vite in React, covering the @theme inline pattern, CSS variable architecture, dark mode and Tailwind v3 migration gotchas. |
| aceternity-ui | 1,534 | Over 100 animated React components for Next.js and Tailwind, for hero sections, parallax, 3D effects and shadcn CLI integration errors. |
| vitest-testing | 1,253 | Vitest unit and integration testing for TypeScript projects, with native ESM support, Vite HMR and mocking patterns. |
| motion | 1,087 | Motion, the Framer Motion library: drag and drop, scroll animations, gestures, SVG morphing, spring physics and bundle size problems. |
| playwright | 1,039 | Playwright browser automation and end to end testing: auto-detecting dev servers, writing test scripts, filling forms, screenshots, responsive checks and login flows. |
| api-testing | 897 | HTTP API testing with Supertest for TypeScript and httpx plus pytest for Python, covering request and response validation, authentication and error handling. |
| responsive-web-design | 695 | Adaptive layouts with Flexbox, CSS Grid and media queries on a mobile first basis, including cross-browser compatibility. |
| zod | 655 | TypeScript schema validation and type inference for API payloads, form data, environment variables and configs, with JSON Schema output for OpenAPI. |
| nano-banana-prompts | 611 | Prompt craft for Gemini 2.5 Flash Image, also called Nano Banana: photo prompts, art styles and multi turn editing workflows. |
| image-optimization | 594 | Image delivery for the web through modern formats, responsive sources and lazy loading to cut page weight. |
| rest-api-design | 593 | RESTful API conventions: resource naming, HTTP methods, status codes and response formats. |
| mobile-first-design | 582 | Responsive interfaces designed from the mobile screen up, with progressive enhancement for larger breakpoints. |
| web-performance-optimization | 565 | Performance work through code splitting, lazy loading, caching strategies and Core Web Vitals monitoring. |
| inspira-ui | 563 | Over 120 animated Vue and Nuxt components with TailwindCSS v4, motion-v, GSAP and Three.js, plus motion-v integration errors. |
| api-authentication | 539 | JWT, OAuth 2.0 and API key authentication for service to service calls and third party integrations, including token management and security headers. |
| code-review | 538 | Review discipline with verification gates: receiving feedback, requesting reviewer subagent passes and avoiding false completion claims. |
| web-performance-audit | 532 | Core Web Vitals audits, bottleneck identification and optimisation recommendations for LCP, FID and CLS regressions. |
| vulnerability-scanning | 522 | Dependency, code and container scanning with Trivy, Snyk and npm audit, for CI security gates, CVE detection and SBOM generation. |
| kpi-dashboard-design | 516 | Metric selection, visual hierarchy and data visualisation for executive dashboards and analytics views. |
| progressive-web-app | 511 | Installable web apps with service workers, web manifest, offline support, install prompts and cache strategies. |

The remaining 180 indexed listings range from 128 to 506 installs.

## Why This Matters for Hermes Agents

The API skills here cover the part of backend work that agents get subtly wrong rather than loudly wrong. A generated endpoint usually compiles and usually returns something; the failures are a 200 on a validation error, a list endpoint with no pagination contract, a retry that duplicates a payment because nothing made the POST idempotent, or an auth check that lives in the handler instead of the route. `rest-api-design`, `api-pagination`, `idempotency-handling`, `api-rate-limiting`, `api-error-handling` and `api-contract-testing` each exist to state those rules before the code is written, which is the cheapest possible point to fix them.

The testing and security skills pair with that nicely. `vitest-testing`, `api-testing`, `playwright` and `mutation-testing` give an agent a concrete way to prove an endpoint works instead of asserting it does, and `vulnerability-scanning`, `csrf-protection`, `xss-prevention`, `security-headers-configuration` and `defense-in-depth-validation` give the review pass something to check against. For a Hermes profile that writes backend code on request, the value is that verification becomes a documented step rather than a habit the model may skip.

Loading them is cheap and predictable. Each is a plain `SKILL.md` with YAML frontmatter, a one-line `description` and often an `allowed-tools` list, with optional `templates/`, `scripts/` and `references/` directories beside it. There is no MCP server, no daemon and no install-time hook, so a copied directory works in a Hermes profile exactly as it works in Claude Code.

The naming is also agent friendly: one topic per skill, named after the technology, so routing on the skill name plus description is reliable without a router model. That is the opposite of the monolithic mega-skills, where a single description has to cover a dozen unrelated triggers.

## Usage

| You say | What happens |
|---|---|
| "Design the REST surface for a returns API" | The agent loads `rest-api-design` and answers with resource names, HTTP methods, status codes and error shapes before writing any handler. |
| "Add pagination and filtering to the orders list" | `api-pagination` and `api-filtering-sorting` supply cursor versus offset conventions, parameter names and the response envelope, so the endpoint ships with a stable contract. |
| "This charge ran twice when the client retried" | `idempotency-handling` walks the idempotency key pattern, the storage choice and the replay behaviour, and the agent patches the handler accordingly. |
| "Write tests for the new endpoints" | `api-testing` produces Supertest or httpx plus pytest cases covering auth, validation and error paths, and `api-contract-testing` pins the response schema. |
| "Lock down the auth layer" | `api-authentication`, `oauth-implementation` and `session-management` cover token issuance, refresh and storage, with `csrf-protection` and `security-headers-configuration` for the browser surface. |
| "Scan this before we deploy" | `vulnerability-scanning` runs the Trivy, Snyk and npm audit passes and reports CVEs, outdated packages and SBOM gaps as a CI gate. |
| "Build a dark mode theme switcher that actually works" | `tailwind-v4-shadcn` applies the documented `@theme inline` pattern and CSS variable architecture, avoiding the v4 theming failures the skill exists to prevent. |

## Verification

The raw path below returned 200 on branch main when this guide was written on 2026-10-30:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/secondsky/claude-skills/main/plugins/tailwind-v4-shadcn/skills/tailwind-v4-shadcn/SKILL.md
```

Expect `200`. That file is also the best sample of house style: read the `description` field, because it carries the trigger phrases the agent routes on, and check whether an `allowed-tools` line is present before you plan to run the skill unattended.

After installing, confirm what landed. The profile count should rise by exactly the number of skills you asked for, since each plugin holds one or more skill directories:

```bash
find ~/.hermes/profiles/corpusiq/skills -name SKILL.md | wc -l
head -6 ~/.hermes/profiles/corpusiq/skills/api-authentication/SKILL.md
grep -c "" ~/.hermes/profiles/corpusiq/skills/api-authentication/SKILL.md
```

A good copy shows `name: api-authentication`, a description naming JWT, OAuth 2.0 and API keys, and a body that opens with the authentication methods section rather than a redirect to another file. Skills are large, so the line count matters: anything over a few hundred lines with `references/` beside it is meant to be read progressively, not pasted whole into a prompt.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-30) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| tailwind-v4-shadcn | Pass | Pass | Pass |
| aceternity-ui | Pass | Pass | Pass |
| vitest-testing | Pass | Pass | Pass |
| motion | Pass | Pass | Pass |
| better-chatbot-patterns | Pass | Pass | Pass |

No Fail and no Warn appears in the sample, and the repository is MIT throughout, but the sample is five listings out of 200, so the table describes five skills rather than the suite. The remaining 195 listings carry no verdict in this pack and were not audited for this guide.

The repo does a fair amount of security work on its own account, which is a better signal than a scanner pass. The README states that 31 skills carry tailored "Secure Installation" guidance across the high-risk categories: Bun, Nuxt, Cloudflare, AI and agent SDKs, Docker and CI/CD, and that `dependency-upgrade` gained Socket CLI integration for typosquatting and malicious package detection plus GitHub Actions templates for supply chain gates.

Two caveats worth carrying into review. The README itself says skills.sh warnings are advisory rather than authoritative, citing a Trail of Bits analysis from June 2026 that found the LLM meta-analyzer both missing malicious skills and flagging unfamiliar but legitimate version pins, so a Pass here is not a proof of safety. And several skills instruct the agent to run scaffolding and package installers, which is where real risk lives: review the commands a skill proposes before letting it run them against a machine holding credentials.

## Limitations

- Snapshot data, verified 2026-10-30: 85,061 combined installs across 200 indexed listings; 240 GitHub stars; MIT; last pushed 2026-09-26. Counts drift over time.
- The index outruns the tree. skills.sh carries 200 listings while the checkout holds 187 `SKILL.md` files across 145 plugin directories, and the README advertises 145 skills, so three different counts describe the same repository; the 13 extra listings have no skill directory to copy today.
- The counts are heavily skewed. `tailwind-v4-shadcn` alone holds 8,128 installs and the 180 listings below the 511 threshold run from 506 down to 128, so an install number says more about search traffic than about quality.
- Only five skills were audited for this guide. The other 195 listings have no verdict here, and a Pass on a Tailwind theming skill says nothing about the package installers some infrastructure skills invoke.
- The skills are written for Claude Code's discovery model, which caps total skill description size at 15,000 characters in the system prompt; the README offers `SLASH_COMMAND_TOOL_CHAR_BUDGET=30000` as a workaround for that client, but Hermes does not share the cap and does not read the same manifest, so vendor by directory or use `npx skills` rather than copying a `.claude-plugin/` tree.
- Bulk install is unreliable by the maintainer's own note. `npx skills add ... --all` walks standard container directories and this repo nests skills one level deeper, so unnamed bulk passes can silently install a subset.

## Related

- [Anthropic Claude API Skills - Official Claude API](/hermes/skills/catalog/anthropics-claude-api-skills-setup)
- [Developer Kit - Java and TypeScript Skill Suite Setup](/hermes/skills/catalog/developer-kit-setup)
- [Superpowers - Agentic Skills Framework Setup](/hermes/skills/catalog/superpowers-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the API track, not the frontend one. `rest-api-design`, `api-error-handling`, `api-pagination`, `idempotency-handling` and `api-contract-testing` are the five that most change generated backend code, and together they are smaller than the Tailwind skill alone.
- Install by name with `--skill`, one repo per call. `--all` is documented as unreliable against this layout, and a silent partial install looks exactly like a successful one in the count.
- Read the `allowed-tools` line before installing. Several skills declare Bash, Write and Edit, which means the skill expects to run commands rather than only advise; decide per skill whether that is acceptable in the profile you are installing into.
- Pair `web-performance-audit` with `web-performance-optimization`. The audit names the LCP, FID and CLS bottleneck and the optimization skill carries the code splitting and caching changes that address it, so they are more useful as a pair than either alone.
- Keep the plugin directory as the unit of upgrade. The manifests and `MARKETPLACE.md` are generated by scripts in the repo, so pulling a fresh copy of the directory gets you the current skill text without re-deriving anything by hand.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
