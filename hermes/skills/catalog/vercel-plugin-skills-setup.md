---
title: "Vercel Plugin Skills - Full Vercel Ecosystem Agent Setup"
description: "Comprehensive Vercel ecosystem plugin: 50 skills across AI Gateway, AI SDK, Functions, flags, auth, CDN, and agent-building guidance. 4.8K installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/vercel-plugin-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-01"
tags: ["hermes skill", "agent skill", "skill setup", "vercel", "nextjs", "ai sdk", "deployment"]
---

# Vercel Plugin Skills - Setup Guide

**Source:** [vercel/vercel-plugin](https://github.com/vercel/vercel-plugin) (295⭐, NOASSERTION)
**Skill family:** `vercel/vercel-plugin` (11 indexed skills; 43 in-repo under `skills/`)
**Combined Installs:** ~4,768 across indexed listings (Oct 1, 2026 snapshot)
**Category:** Platform / Deployment
**Quality Tier:** 🟡 Trusted (official Vercel org, active same-day cadence; license is NOASSERTION - no recognized SPDX file)

Vercel's comprehensive ecosystem plugin packs a relational knowledge graph plus skills for every major Vercel product, specialized agents, and Vercel conventions. Unlike the narrower [vercel-labs/agent-skills](/docs/hermes/skills/catalog/vercel-agent-skills-setup) collection, this repo is the broad "one plugin to teach an agent the whole platform" package: AI Gateway, AI SDK, backend architecture, deployment protection, flags, queues, and a set of Vercel's own engineering-hygiene skills.

---

## Installation

```bash
npx skills add vercel/vercel-plugin
```

## Roster - Indexed Skills

| Skill | Installs | What It Does |
|---|---|---|
| access-protected-vercel-deployment | 2,433 | Access/test Vercel deployments behind Vercel Auth, SSO, or Deployment Protection |
| build-agents | 1,399 | Default guidance for building AI agents (eve is the default choice) |
| create-a-backend | 568 | Backend architecture: Functions, Services, containers, Workflows |
| flags-sdk | 249 | Feature flags and A/B tests with the Flags SDK + Vercel Flags |
| queues | 54 | Queue/background-processing guidance |
| custom-metrics | 35 | Custom metrics instrumentation |
| domains | 22 | Domain configuration |
| styled-jsx | 3 | styled-jsx CSS-in-JS guidance |
| ncc | 2 | ncc bundler guidance |
| edge-runtime | 2 | Edge Runtime guidance |
| streamdown | 1 | Streamdown streaming-markdown guidance |

*In-repo skills not yet indexed on skills.sh (from the 43 under `skills/`) include: `ai-gateway` (setup/model discovery/routing/fallbacks/BYOK/budgets/spend), `ai-sdk` (AI SDK expert guidance), `auth`, `bootstrap`, `cdn-caching`, and more.*

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| Deploy + verify our sites | access-protected-vercel-deployment to test protected previews by agent |
| Build internal agents | build-agents for scaffolding a durable backend agent on Vercel |
| Frontend AI features | ai-sdk + ai-gateway for model routing with spend controls |
| Backend selection | create-a-backend to match workload to Functions/Services/Workflows |

## Limitations / Verification

- skills.sh indexing verified Oct 1, 2026: 11 skills indexed; 6 SKILL.md files verified via raw.githubusercontent on branch `main` (50 SKILL.md files total in-repo: 43 under `skills/`, 7 internal under `.claude/skills/`).
- License is `NOASSERTION` - the repo has a LICENSE file but GitHub does not recognize its SPDX identifier. Review the license text before commercial redistribution.
- Distinct from the three already-documented Vercel guides ([vercel-labs/agent-skills](/docs/hermes/skills/catalog/vercel-agent-skills-setup), [vercel/ai](/docs/hermes/skills/catalog/vercel-ai-skills-setup), [vercel/eve](/docs/hermes/skills/catalog/vercel-eve-agent-skills-setup)) - this is the broad platform-ecosystem plugin repo.
- No live install test performed; install counts and the 295-star count are from the Oct 1, 2026 sweep snapshot.

## Security

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Vercel Agent Skills](/docs/hermes/skills/catalog/vercel-agent-skills-setup)
- [Vercel AI SDK Skills](/docs/hermes/skills/catalog/vercel-ai-skills-setup)
- [Vercel Eve Agent Skills](/docs/hermes/skills/catalog/vercel-eve-agent-skills-setup)
- [Skills Marketplace](/docs/hermes/skills/marketplace)

---

*← [Skills Catalog](/docs/hermes/skills/catalog) | [Marketplace](/docs/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
