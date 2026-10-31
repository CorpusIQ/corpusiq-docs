---
title: "Patricio Skills - Full Stack Engineering Suite Setup"
description: "patricio0312rev/skills: 56.7K combined installs. 155 MIT markdown skills for frontend animation, API tooling, CI/CD, testing and AI engineering."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/patricio-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "engineering suite", "frontend", "ai engineering"]
---

# Patricio Skills - Setup Guide

**Source:** [patricio0312rev/skills](https://www.skills.sh/patricio0312rev/skills) via skills.sh - 56.7K combined installs across 153 indexed listings; first seen 2026-10-30 (evening sweep)

**GitHub:** [patricio0312rev/skills](https://github.com/patricio0312rev/skills) - 63 stars, MIT License, branch main, last pushed 2026-01-11; 155 `SKILL.md` files, one per skill directory, grouped into ten discipline folders (`foundation`, `frontend`, `backend`, `ai-engineering`, `architecture`, `ci-cd`, `db-management`, `testing`, `security`, `performance`) with no `scripts/` or `assets/` beside them and only two `references/` files across the whole tree

**Category:** Full stack software engineering skill collection

**Quality Tier:** 🟢 Green - all five sampled skills Pass on all three auditors and the collection is MIT licensed, though the repository has been idle since January 2026

Patricio Marroquin publishes this collection as `patricio0312rev/skills`, and it is a very large single-owner suite: 155 skills in ten groups, from project scaffolding and lint setup through React animation, API design, CI/CD, database work, testing, security and AI engineering. The README frames it as full SDLC coverage for modern software engineering, and each skill is a self-contained `SKILL.md` with a core workflow, configuration samples and an output checklist.

The install counts do not follow the DevOps framing. The busiest skill is `framer-motion-animator` at 11,211 installs, then `eslint-prettier-config`, `postman-collection-generator` and `changelog-writer`; `dockerfile-optimizer` is eighth. Read the suite as general engineering coverage whose centre of gravity is frontend and developer tooling, with the deployment shelf (`dockerfile-optimizer`, `nginx-config-optimizer`, `kubernetes-manifest-generator`, `github-actions-pipeline-creator`, `terraform-module-builder`) as one of ten, not as the theme.

## Installation

The README documents a copy-based install only: there is no CLI, marketplace command or install script in the repository. Skills are picked one at a time and dropped into a `.claude/skills/` folder in the project:

```bash
mkdir -p .claude/skills
cp -r path/to/skills/frontend/framer-motion-animator .claude/skills/
```

For a Hermes profile the same move works with the profile skills directory as the target. Clone once, then copy the directories you want:

```bash
git clone https://github.com/patricio0312rev/skills.git patricio-skills
cp -r patricio-skills/frontend/framer-motion-animator ~/.hermes/profiles/corpusiq/skills/framer-motion-animator
```

The tree holds exactly 155 `SKILL.md` files, one per skill directory: no scripts, no assets and no plugin manifest, and only two skills ship a `references/` file (`foundation/project-scaffolder` and `foundation/repo-structure-linter`). The group folder is organisation only, so `frontend/framer-motion-animator` lands as `skills/framer-motion-animator`. Copying a whole shelf is a loop over directories:

```bash
for d in patricio-skills/foundation/*/; do cp -r "$d" ~/.hermes/profiles/corpusiq/skills/; done
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| framer-motion-animator | 11,211 | Page transitions, gesture and scroll driven animation in Framer Motion, plus orchestrated sequences across a React interface. |
| eslint-prettier-config | 1,084 | ESLint and Prettier setup for TypeScript and React, with rule choices, plugin wiring and formatting config. |
| postman-collection-generator | 689 | Scanning Express, Next.js, Fastify or Hono routes and writing an importable Postman collection from them. |
| changelog-writer | 617 | Release notes and changelogs from git history, grouped into breaking, feature, fix and improvement, in Keep a Changelog form. |
| bruno-collection-generator | 605 | The same route scan for the open source Bruno client, producing .bru files with environments, auth and folder structure. |
| jsdoc-typescript-docs | 551 | JSDoc and TypeDoc inline documentation for a TypeScript codebase, including an exported API reference. |
| websocket-realtime-builder | 533 | Socket.io real time features: rooms, handshake auth, reconnection handling and push updates. |
| dockerfile-optimizer | 532 | Multi stage Dockerfiles with smaller images, better cache reuse and hardened build steps. |
| animation-micro-interaction-pack | 501 | Hover, entrance and gesture presets that make a UI feel finished, with reduced motion support. |
| explaining-code | 475 | Walking a reader through unfamiliar code with an analogy, a diagram and a plain walkthrough. |
| conventional-commits | 475 | Semantic commit messages with type, scope, breaking change note and footer per the Conventional Commits spec. |
| nginx-config-optimizer | 436 | Nginx reverse proxy and load balancer configs tuned for caching, TLS and throughput. |
| multi-tenant-safety-checker | 427 | Tenant isolation review at query and policy level, using row level security and cross tenant leak tests. |
| api-docs-generator | 398 | OpenAPI or Swagger specifications turned into interactive API reference pages with code examples. |
| codebase-summarizer | 397 | An ARCHITECTURE.md tour of a repository: entry points, module map, data flow and edit here pointers. |
| dark-mode-implementer | 375 | Dark and light theming with CSS variables, Tailwind dark mode and system preference detection. |
| unit-test-generator | 365 | Unit suites in Arrange Act Assert shape, with edge cases, error paths and coverage gaps named. |
| redis-patterns | 363 | Redis for caching, sessions, rate limiting, pub/sub and distributed locks. |
| i18n-frontend-implementer | 361 | Translation plumbing and key strategy, plural rules, and date, number and currency formatters. |
| accessibility-auditor | 357 | A WCAG 2.1 audit pass over ARIA patterns, keyboard paths, screen reader output and contrast. |

The remaining 133 indexed listings range from 213 to 355 installs.

## Why This Matters for Hermes Agents

A profile that carries only hand written skills keeps rebuilding the same scaffolding: a lint config, a Dockerfile, a component test file, a changelog format. This collection answers that at breadth, one directory per problem, and each file arrives with a workflow, configuration samples and a checklist, so the agent starts from a shaped plan rather than a blank page.

The stronger argument is for copying selectively. With 155 descriptions competing for the same triggers, several overlap plainly: `framer-motion-animator` and `animation-micro-interaction-pack` both fire on animation requests, `redis-patterns` and `caching-strategist` both fire on cache questions, and `api-docs-generator` ships twice under different groups. A profile that swallows the whole tree spends context on near duplicate descriptions and then picks between them unreliably, which is worse than carrying eight skills it routes cleanly.

The files earn their place as reference even when they are never installed. Each runs several hundred lines of concrete instruction, enough to lift a checklist or a config shape into a project specific skill of your own, and the suite covers the corners teams skip: tenant isolation under row level security, PII redaction in logs, artifact SBOM publishing, dependency vulnerability triage, prompt regression testing.

The deployment shelf is real, and it is what makes a DevOps label tempting: `dockerfile-optimizer`, `nginx-config-optimizer`, `github-actions-pipeline-creator`, `preview-environments-builder`, `rollback-workflow-builder`, `kubernetes-manifest-generator` and `terraform-module-builder` cover most of a release path, one layer per file.

The caveat is age. Nothing in the repository has changed since 2026-01-11, so the fast moving surfaces date fastest: React Server Components, TanStack Query, Next.js App Router, and the whole AI engineering shelf, from `rag-pipeline-builder` to `mcp-server-builder`. Treat a January file as a starting point to verify against current docs, not as current best practice.

## Usage

| You say | What happens |
|---|---|
| "Add a page transition to the dashboard" | framer-motion-animator picks the animation primitive, writes the variant and transition config, and covers gesture and reduced motion cases. |
| "Scan our API routes and give me a Postman collection" | postman-collection-generator walks the route definitions, extracts endpoints, methods and params, and writes importable collection JSON. |
| "Our image is 1.4GB, fix the Dockerfile" | dockerfile-optimizer rewrites the build as multi stage, reorders layers for cache reuse and trims what reaches the runtime stage. |
| "Write the release notes for v2.3" | changelog-writer parses commits and PR titles since the last tag, groups them by impact and suggests the next semantic version. |
| "Is our tenant data actually isolated?" | multi-tenant-safety-checker reviews queries and policies for row level security coverage and writes cross tenant leak tests. |
| "Explain how the payment module works" | explaining-code leads with an analogy, then a diagram, then a code walk aimed at someone new to the file. |
| "Audit this page for accessibility" | accessibility-auditor runs a WCAG 2.1 pass over ARIA roles, keyboard order, focus handling and contrast, then lists fixes. |

## Verification

Both raw paths below returned 200 on branch main when this guide was written on 2026-10-30:

```bash
curl -sL -o /dev/null -w "%{http_code} framer\n" \
  https://raw.githubusercontent.com/patricio0312rev/skills/main/frontend/framer-motion-animator/SKILL.md
curl -sL -o /dev/null -w "%{http_code} eslint\n" \
  https://raw.githubusercontent.com/patricio0312rev/skills/main/foundation/eslint-prettier-config/SKILL.md
```

Expect `200` twice. After a copy lands in the profile, confirm what arrived and that the count matches your intent:

```bash
ls ~/.hermes/profiles/corpusiq/skills/framer-motion-animator
sed -n '1,3p' ~/.hermes/profiles/corpusiq/skills/framer-motion-animator/SKILL.md
find ~/.hermes/profiles/corpusiq/skills -name SKILL.md | wc -l
```

A good copy is a directory holding one `SKILL.md` and nothing else, with `name:` and `description:` on lines 2 and 3, which is the whole routing surface. A count of 155 means every skill in the suite is present.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-30) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| framer-motion-animator | Pass | Pass | Pass |
| eslint-prettier-config | Pass | Pass | Pass |
| postman-collection-generator | Pass | Pass | Pass |
| changelog-writer | Pass | Pass | Pass |
| security-incident-playbook-generator | Pass | Pass | Pass |

No Fail and no Warn appears in the sample, so there is no verdict to flag here. The table covers five listings out of 153, though, so it reads as a clean pattern across the busiest skills and one security skill, not as an audit of all 155 files. The executing surface is genuinely small: each skill is a markdown file with no scripts, hooks, install steps or network calls, so copying one runs nothing. The surface that matters is behavioural, because a skill is followed rather than executed. A file that says to add a dependency, relax a lint rule, paste a Dockerfile or open a port changes the target repository the moment the agent acts on it, and that change inherits whatever the file assumed about versions and trust. Read the `SKILL.md` before it steers a real PR, and read the resulting diff before merging.

## Limitations

- Snapshot data, verified 2026-10-30: 56,693 combined installs across 153 indexed listings; 63 GitHub stars; MIT License; last pushed 2026-01-11. Counts drift over time.
- The repository is idle. The last commit is 2026-01-11, roughly nine and a half months before this sweep, so framework specific skills predate a lot of movement in React, Next.js and the AI tooling libraries they name.
- The counts are not a ranking of quality. `framer-motion-animator` alone holds 11,211 of the 56,693 combined installs, and `dockerfile-optimizer`, the obvious namesake for a Docker title, sits eighth at 532.
- Install is a manual copy. There is no CLI and no marketplace command in the repository, the README documents `.claude/skills/`, and a Hermes profile needs its own target directory plus a rename to flatten the group folder.
- The skills are markdown only. The 155 directories hold one `SKILL.md` each plus two `references/` files in total, with no scripts, tests or evaluations, so quality can only be judged by reading the instructions, not by running them.
- Index and tree disagree slightly. skills.sh indexes 153 listings while the checkout holds 155 directories, and `api-docs-generator` exists in both `backend/` and `testing/`, so installing by name can land two different files.

## Related

- [Dockerize and Deploy](/hermes/skills/catalog/dockerize-and-deploy-setup)
- [Developer Kit - Java and TypeScript Skill Suite Setup](/hermes/skills/catalog/developer-kit-setup)
- [Capgo Skills - Capacitor Mobile Release Suite Setup](/hermes/skills/catalog/capgo-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Copy by shelf, not by count. `foundation/` holds 23 skills that earn their place in almost any profile (scaffolding, lint, git hygiene, changelog, docs, onboarding); the AI engineering shelf ages fastest of the ten.
- Read the `description:` field before copying, because it is the entire routing surface. Generic ones such as "use when building APIs" fight each other in a profile, so edit your copy to name your actual stack.
- Keep the install path flat. The group folder is for browsing the repository, not for the skill directory; Hermes wants `skills/<name>/SKILL.md`.
- Check for the duplicate first. `api-docs-generator` ships in both `backend/` and `testing/` with different content, and the `backend/` copy is the OpenAPI reference generator.
- Pair the deployment files deliberately: `dockerfile-optimizer`, `nginx-config-optimizer`, `github-actions-pipeline-creator` and `rollback-workflow-builder` each cover one layer, and none of them orchestrates the others, so the sequencing stays your call.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
