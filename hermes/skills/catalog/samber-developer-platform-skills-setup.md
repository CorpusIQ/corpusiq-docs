---
title: "Samber Developer Platform Skills - API & DX Setup"
description: "Setup guide for samber/developer-platform-skills - 95.1K combined installs. 32 skills for public APIs, webhooks, SDKs, and the developer portal."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/samber-developer-platform-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "developer platform", "api design", "sdk engineering"]
---

# Samber Developer Platform Skills - Setup Guide

**Source:** [samber/developer-platform-skills](https://www.skills.sh/samber/developer-platform-skills) via skills.sh - 95.1K combined installs across 32 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [samber/developer-platform-skills](https://github.com/samber/developer-platform-skills) (3 stars, MIT; pushed Sep 28, 2026; skills live under skills/)
**Category:** Developer Platform / API & SDK Engineering
**Quality Tier:** 🟡 Beta - samber authority series (developer-platform extension); MIT; new repo, low stars (3); all sampled verdicts Pass

Developer Platform Skills is a 32-skill collection from samber covering the developer-facing surface of a SaaS product: public APIs and their lifecycle, webhooks, SDKs, the developer portal, and the connector marketplace around it. It is written for platform PMs, API and DX engineers, SDK authors, and partner engineering - design and policy work, not code generation - and every skill is tool-agnostic: it teaches the decision, not one vendor's console.

Start with developer-platform-kickoff, which routes any developer-platform task to the right skill in the collection and returns a ranked short-list, an ordered chain, and an honest gap list. The skills are atomic by design and reference each other freely, so the README recommends installing the whole collection rather than picking single skills.

---

## Installation

Install every skill in the repo, not just one: the skills reference each other freely, and a single-skill install leaves sibling references and routed handoffs dangling.

```bash
# skills.sh - universal, works with any Agent Skills-compatible tool
npx skills add samber/developer-platform-skills
```

Alternative channels from the README: Claude Code (`/plugin marketplace add samber/developer-platform-skills` then `/plugin install developer-platform-skills@developer-platform-skills`), Codex (`codex plugin add github:samber/developer-platform-skills`), or Gemini CLI (`gemini extensions install https://github.com/samber/developer-platform-skills`).

Then start with the collection's kickoff skill:

```
/developer-platform-kickoff We're about to publish our first public REST API and I'm not sure the design is ready to commit to.
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| api-reference-quality | 3,047 | Audit a published API reference endpoint by endpoint; drive fixes with CI gates |
| app-marketplace-review | 3,037 | Operator-side review and approval process for third-party marketplace apps |
| api-test-mode-design | 3,036 | Test/sandbox mode: isolation, test keys, deterministic events, path to live |
| connector-marketplace-strategy | 3,034 | Build a connector marketplace, join others', or buy embedded iPaaS |
| api-auth-key-management | 3,034 | API-key surface: format, hashed storage, scoping, zero-downtime rotation |
| developer-platform-kickoff | 3,032 | Start here: routes a platform task with a ranked short-list and gap list |
| app-marketplace-launch-marketing | 3,028 | Marketplace launch and app co-marketing: cohort, reveal, featuring, budget |
| integration-partnership-strategy | 3,024 | Which partners to integrate, how deep, with a demand-data scorecard |
| api-idempotency-retry | 3,024 | Idempotency keys and client retry guidance: scoping, backoff, retry budgets |
| developer-portal-design | 3,018 | External developer portal: IA, signup-to-first-call path, search, RBAC |
| api-rate-limit-policy | 3,016 | Published rate-limit policy: quotas, burst numbers, headers, 429 contract |
| developer-platform-hiring | 3,015 | Hiring side: scorecard, interview loop, sourcing channels, comp stance |
| developer-platform-career | 3,015 | Candidate side: role track, portfolio signals, interview prep, offers |
| api-status-communication | 3,013 | Status pages, incident cadence, public postmortems, and SLA reporting |
| partner-app-onboarding | 3,008 | Partner journey from signup to first submitted app: sandbox to support |

The remaining 17 indexed listings range from 2,860 to 2,986 installs.

## Why This Matters for Hermes Agents

Most agent skill collections generate code; this one sharpens decisions. For builders working on a product's public surface - API design reviews, rate-limit policy, webhook envelopes, OAuth2 provider design, marketplace listing standards - the collection encodes the policy questions that are expensive to get wrong and easy to postpone, and every skill teaches the decision instead of one vendor's console. Hermes agents get a clean fit because the skills are tool-agnostic prose procedures with no runtime dependencies, and the kickoff skill's routing returns a ranked short-list plus an ordered chain, which gives an agent a deterministic path through a fuzzy platform task. The collection is organized along a real build sequence: kickoff, API design, authentication, documentation, lifecycle, integration surfaces, testing, SDKs, the portal, status communication, partnerships, and the connector marketplace. Install it as a whole set - the skills reference each other freely, and single-skill installs leave sibling handoffs dangling.

## Usage

| You say | What happens |
|---|---|
| "/developer-platform-kickoff We're about to publish our first public REST API" | Routes the task to a ranked short-list, an ordered chain, and an honest gap list. |
| "Should we expose a public gRPC API?" | public-grpc-api-design runs the expose-or-not gate, then proto conventions and breaking-change gates. |
| "Define our idempotency and retry story for POST endpoints." | api-idempotency-retry scopes keys, replay windows, backoff, and SDK defaults. |
| "Set the rate limits and 429 contract we publish." | api-rate-limit-policy sets quotas, burst numbers, response headers, and override paths. |
| "We want to launch an app marketplace." | connector-marketplace-strategy plus the app-marketplace-* skills cover build-vs-join, review, monetization, and launch. |
| "Audit our API reference for quality and drift." | api-reference-quality audits endpoint by endpoint, then drives a source-of-truth rollout with CI gates. |
| "Design our outbound webhook platform." | webhook-platform-design covers event taxonomy, signed payloads, retry and dead-letter policy, and debugging. |

## Verification

Confirm the collection is visible to your agent, then fetch a skill's full source before running it:

```bash
# List installed skills
npx skills list | grep developer-platform

# Review a skill's full source before install
curl -sL https://raw.githubusercontent.com/samber/developer-platform-skills/main/skills/api-reference-quality/SKILL.md
```

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| api-reference-quality | Pass | Pass | Pass |
| app-marketplace-review | Pass | Pass | Pass |
| api-test-mode-design | Pass | Pass | Pass |

## Limitations

- New repo with very low traction: 3 GitHub stars and a collection pushed Sep 28, 2026, so independent validation is thin.
- All 32 listings cluster tightly between 2,860 and 3,047 installs, consistent with a single recent promotion wave rather than long organic adoption.
- Decision and policy skills, not code generation: teams expecting implementation output must pair them with build-oriented skills.
- Single-skill installs break cross-references; install the whole collection.
- The collection is an extension of the samber authority series and shares its conventions; check overlap with the DevRel and Go collections before duplicating internal standards.

- Snapshot data, verified Oct 10, 2026: 95,144 combined installs across 32 indexed listings; 3 GitHub stars; MIT; last pushed Sep 28, 2026. Counts drift over time.

## Related

- [Samber DevRel Skills - Open Source Growth Suite Setup](/hermes/skills/catalog/samber-devrel-skills-setup) - sibling samber collection: DevRel strategy and execution
- [Samber Go Skills - Golang Engineering Standards](/hermes/skills/catalog/samber-golang-skills-setup) - sibling samber collection: Golang engineering standards
- [LaunchDarkly Agent Skills - Feature Flags & AgentControl Setup](/hermes/skills/catalog/launchdarkly-agent-skills-setup) - staged rollouts for platform surfaces behind flags
- [Build Mcp Server Setup](/hermes/skills/catalog/build-mcp-server-setup) - pairs with mcp-server-offering when you ship an MCP surface
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Read developer-platform-kickoff first; it routes the task and names the gaps you did not know you had.
- Install the full collection; cross-references resolve only when the sibling skills are present.
- Pair the decision skills with a build-side collection - these skills decide, they do not generate code.
- Version the output: policy decisions (rate limits, error envelopes, deprecation windows) belong in files your platform team can review, not in chat scrollback.
- Fetch per-skill sources under skills/ to review any skill before install; each is a short standalone SKILL.md.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
