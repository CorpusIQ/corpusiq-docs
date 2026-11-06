---
title: "BMAD Labs Skills - Architecture and Delivery Toolkit"
description: "bmad-labs/skills on skills.sh: 6.6K combined installs across 74 listings; architecture, TypeScript testing and release skills for delivery."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/bmad-labs-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "architecture", "typescript", "release"]
---

# BMAD Labs Skills - Setup Guide

**Source:** [bmad-labs/skills](https://www.skills.sh/bmad-labs/skills) via skills.sh - 6.6K combined installs across 74 indexed listings; first seen 2026-11-05 (Nov 5, 2026 evening sweep)
**GitHub:** 19 stars, MIT licence, last pushed 2026-11-06, 25 SKILL.md files in the tree: 23 skill folders under skills/, a template/ starter and one nested reference skill
**Category:** BMAD delivery for agents: architecture design, trade-off analysis, root-cause reports, release and multi-repo git work
**Quality Tier:** 🟡 Caution - Snyk Warned on bmad-technical-research, one of five sampled skills; the other four passed all three audits; MIT; 19 stars.

The README describes a collection of skills that give Claude Code, Cursor, Codex, OpenCode and twenty-odd other agents specialized knowledge for delivery work: architecture design, testing, clean code, release automation, incident analysis, documents and slides. The repository ships as a Claude Code plugin and as an `npx skills` source, with a `.claude-plugin/plugin.json` manifest, a `spec/` directory for the SKILL.md format, a `template/` starter and CI workflows that run skill checks.

The strongest part of the set is not code generation. It is the layer around it. `architecture-design` produces a design package at one of three detail levels: C4 views, project structure, module design, ERD, domain events, and ingress and egress API contracts, with each protocol file proven by a real validator and built one folder at a time. `trade-off-analysis` produces scored comparison matrices for architecture decisions and build-versus-buy calls. `rca-report` runs an incident investigation and writes a layered root cause with a workaround playbook, Five Whys and binned recommendations. `manual-testing` maintains a test plan across API, frontend, pipeline, AI and infrastructure surfaces.

Around those sit the TypeScript trio (E2E, unit and clean code), a release automation skill for Google's release-please, an MCP server builder, a multi-repo git skill for submodule work, document conversion skills and a slide maker with 34 token-driven layouts. The install index counts 74 listings, which is broader than the current tree.

## Installation

The README's primary route is the `skills` CLI, which detects the agents on the machine. Install everything, or scope it down:

```bash
# all skills
npx skills add bmad-labs/skills

# only the TypeScript testing trio
npx skills add bmad-labs/skills --skill typescript-clean-code --skill typescript-e2e-testing --skill typescript-unit-testing

# target one client
npx skills add bmad-labs/skills -a claude-code

# install at user level instead of the project
npx skills add bmad-labs/skills -g
```

Claude Code users can install the plugin instead, which registers every skill in the manifest:

```text
/plugin marketplace add bmad-labs/skills
/plugin install bmad-skills@bmad-skills
```

Then restart the client. The README's troubleshooting steps for skills that do not appear are to clear `~/.claude/plugins/cache`, restart, and check the Errors tab in `/plugin`. It also documents `claude plugin validate .` for a local checkout.

Once installed, a skill loads automatically from its description or runs directly as `/skill-name`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| typescript-e2e-testing | 2,284 | End-to-end and integration tests for TypeScript and NestJS with Jest, supertest and real Kafka, PostgreSQL, MongoDB and Redis in Docker, written as Given-When-Then |
| typescript-clean-code | 643 | Reviewing and refactoring TypeScript against named code smells and type hygiene rules, plus the lint and tsconfig settings that enforce them |
| typescript-unit-testing | 503 | Unit tests with Jest and DeepMocked, in-memory databases and Arrange-Act-Assert structure, including open handle and flake debugging |
| slides-generator | 199 | Slide deck generation on the Vite-based slide stack that the repo's own slide-maker template mirrors |
| skill-from-book | 177 | Turning book markdown into a skill package with granular reference files and progressive disclosure |
| ai-multimodal | 176 | Multimodal workflows at name level only: the listing has no skill directory in the current tree, so its own description could not be read |
| bmad-auto | 145 | Phase 4 implementation orchestration through sub-agents, gated on a sprint status file existing before work starts |
| book-converter | 141 | EPUB to Markdown conversion with pandoc plus AI formatting, including artifact repair and table of contents generation |
| release-please | 117 | Automated versioning, changelogs and releases through release-please, including monorepos, pre-releases and Conventional Commits |
| mcp-builder | 115 | Building MCP servers in Python with FastMCP or in Node and TypeScript with the MCP SDK |
| manual-testing | 112 | Writing, reviewing and executing manual test plans across API, frontend, pipeline, LLM and infrastructure surfaces |
| ui-ux-pro-max | 110 | A design-system skill used as an input by slide-maker; declared in plugin.json as a dependency from its own marketplace |
| template-skill | 107 | The starter template for a new skill, marked internal in its frontmatter so the installer hides it |
| load-docs | 102 | Loading files, folders and URLs fully into the main context for follow-up questions and review |

The remaining 60 indexed listings range from 4 to 97 installs.

## Why This Matters for Hermes Agents

Most skill packs optimize the write-code step. This one covers the steps where an agent is most likely to be confidently wrong: choosing an architecture, comparing two technologies, and explaining an incident. Those are judgment tasks with no compiler to catch a bad answer, and the skills turn them into artifacts with structure a reviewer can check, such as a design package whose API contracts were parsed by a validator or a trade-off matrix with explicit weights.

The TypeScript testing pair carries a second kind of value. `typescript-e2e-testing` names the real infrastructure (Kafka, PostgreSQL, MongoDB, Redis in Docker) instead of mocking it, and `typescript-unit-testing` names the in-memory substitutes. An agent reading both knows which level a given test belongs at, which is the decision that produces slow suites and false confidence when it goes wrong.

The delivery skills also encode sequencing. `bmad-auto` refuses to start when the sprint status file is absent, because that file is the evidence that the earlier phases completed. Encoding a precondition as a hard gate is a pattern worth borrowing in any agent workflow: it converts a plausible-looking start into a stop with a reason.

The repository's security posture is better than its star count suggests. A pull request workflow validates SKILL.md frontmatter and runs Snyk Agent Scan on each changed skill with accepted risks recorded per skill, and a nightly job reads the published skills.sh verdicts and fails on a HIGH or CRITICAL finding. That is a maintainer treating skill content as code that ships, which is rare and worth rewarding with a read.

## Usage

| You say | What happens |
|---|---|
| "Design the architecture for a billing service" | architecture-design produces a design package with C4 views, module boundaries, ERD and API contracts, validated per protocol |
| "Should we use Kafka or SQS here?" | trade-off-analysis builds a scored comparison matrix against stated criteria |
| "Write the RCA for yesterday's outage" | rca-report collects evidence, then writes layered root causes, a workaround playbook and Five Whys |
| "Set up E2E tests for this NestJS service" | typescript-e2e-testing scaffolds Docker-backed integration tests in Given-When-Then form |
| "This file has three smells, clean it up" | typescript-clean-code names the smells and applies the refactor with type hygiene fixes |
| "What changes in this release?" | release-please reads Conventional Commits and prepares the version bump and changelog |
| "Pull these twelve docs in and summarize them" | load-docs ingests the files into context, then answers from them |

## Verification

Read the skill file before installing a batch. Raw paths are `skills/<name>/SKILL.md` on `main`:

```bash
curl -fsSL https://raw.githubusercontent.com/bmad-labs/skills/main/skills/typescript-e2e-testing/SKILL.md | head -5
```

It should open with `name: typescript-e2e-testing` and a description naming Jest, supertest and the Docker-backed infrastructure. Then confirm the folder arrived with its references, since these skills lean on them:

```bash
ls ~/.claude/skills/typescript-e2e-testing
```

The folder should hold `SKILL.md` and `references/`. For the plugin route, `/plugin` lists the installed plugin and its Errors tab reports a skill that failed to load.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| typescript-e2e-testing | Pass | Pass | Pass |
| trade-off-analysis | Pass | Pass | Pass |
| bmad-technical-research | Pass | Pass | Warn |
| bmad-review-adversarial-general | Pass | Pass | Pass |
| architecture-design | Pass | Pass | Pass |

One sampled skill carries a Snyk warning, which is why this guide is tiered Caution and not Production. The warning sits on a research skill rather than on the testing or architecture skills, so the risk is concentrated in one folder; read that finding on skills.sh before enabling it in a session with network or repository credentials.

The repository's own controls are worth knowing. Pull requests run Snyk Agent Scan over changed skills and record accepted risks with a reason in `.github/snyk-agent-scan-allow.json`, and a nightly workflow fails the build on a HIGH or CRITICAL verdict. Some skills ship code rather than prose: `book-converter` bundles Python scripts that drive pandoc and formatting, and the `slide-maker` deck template carries a Vite project with Node check scripts. Review those folders instead of assuming markdown only.

## Limitations

- Snapshot data, verified 2026-11-05: 6,558 combined installs across 74 indexed listings; 19 GitHub stars; MIT; last pushed 2026-11-06. Counts drift over time.
- The install index outruns the tree. The current checkout holds 23 skill folders plus `template/SKILL.md`, while the index carries 74 listings; the bmad-* family, atlassian-rest, slides-generator, ai-multimodal and ui-ux-pro-max have install counts without a matching directory in this clone. `plugin.json` declares ui-ux-pro-max and agent-browser as dependencies from separate marketplaces, which explains part of the gap.
- `template-skill` is a starter stub whose frontmatter sets `internal: true` so the installer hides it. Seeing 107 installs on a template is a quirk of the index, not a recommendation.
- The skill's own evaluation report for `bmad-auto` scores it 3.8 out of 5 and names critical control flow gaps around infinite loop prevention, timeout handling and state tracking, with the recommendation to address them before production use.
- The TypeScript skills assume a NestJS project with Docker available for the integration tier. In a repository without that infrastructure, the E2E skill's commands will not run as written.
- 19 stars is a thin community signal for a 74-listing index. The CI checks are real, but the installed base is small enough that edge cases are undocumented.

## Related

- [BMad Method Skills - Agile AI Development Suite Setup](/hermes/skills/catalog/bmad-method-setup)
- [Architecture Diagram - Full Setup Guide for Hermes Agents](/hermes/skills/catalog/architecture-diagram-setup)
- [Agent Toolkit - 44 Skills for Coding Agents Setup](/hermes/skills/catalog/agent-toolkit-setup)

## Pro Tips

- Install the TypeScript trio together or not at all. The unit and E2E skills divide responsibility, and installing one without the other produces tests at the wrong level.
- Run `architecture-design` before `bmad-auto`. The orchestration skill expects a sprint status file, which exists only once the earlier phases produced their artifacts.
- Ask for the design package at low detail first. The three detail levels exist so an exploration pass does not generate a folder of contracts you will discard.
- Check `/plugin` after a marketplace install. The Errors tab is where a malformed SKILL.md surfaces, and it is faster than debugging a skill that quietly never loads.
- Pair `rca-report` with the incident evidence in hand. The skill structures an investigation; it does not go and collect the logs for you.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
