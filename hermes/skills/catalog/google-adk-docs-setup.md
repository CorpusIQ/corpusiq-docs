---
title: "Google ADK Docs - Agent Development Kit Setup"
description: "google/adk-docs: 16.4K combined installs. Agent Development Kit documentation skills for agent design, evaluation, deployment and observability."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/google-adk-docs-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "google adk", "multi-agent", "documentation", "observability"]
---

# Google ADK Docs - Setup Guide

**Source:** [google/adk-docs](https://www.skills.sh/google/adk-docs) via skills.sh - 16.4K combined installs across 11 indexed listings; first seen 2026-10-30 (morning sweep)

**GitHub:** [google/adk-docs](https://github.com/google/adk-docs) - 1,530 stars, Apache-2.0 License, branch main, last pushed 2026-10-30; 5 `SKILL.md` files in the tree, four side by side under `.agents/skills/<name>/SKILL.md` (integration-review, integration-create, api-reference-audit, adk-bot-review) and one documentation example at `examples/typescript/snippets/skills/skills/weather_skill/SKILL.md`, beside `docs/`, `scripts/`, `llms.txt`, `llms-full.txt` and `mkdocs.yml`

**Category:** Google Agent Development Kit: agents, tools, sessions and deployment

**Quality Tier:** 🟡 Beta - 1 sampled Warn verdict(s); Apache-2.0, a small set of documentation and contributor-workflow skills covering agent design, evaluation, deployment and observability

Google's Agent Development Kit (ADK) is an open-source, code-first toolkit for building, evaluating and deploying AI agents, optimized for Gemini and the Google ecosystem while staying model-agnostic, deployment-agnostic and compatible with other frameworks. This repository is not the SDK: it is the documentation project behind adk.dev, an MkDocs site that also carries the handful of agent skills its maintainers use to keep that documentation accurate. The README frames the same pillars the docs sell, a rich tool ecosystem, code-first development, modular multi-agent systems, built-in tracing and monitoring, and deployment to Cloud Run, GKE or Agent Runtime, and points AI coding tools at `llms.txt` and `llms-full.txt` for context instead of scraping pages.

What skills.sh indexes here is broader than what the checkout ships. The index counts 11 listings and 16.4K combined installs, while the tree holds five `SKILL.md` files: four contributor-workflow skills under `.agents/skills/` and one documentation example buried at `examples/typescript/snippets/skills/skills/weather_skill/`. The six highest-install listings (`adk-dev-guide` through `adk-observability-guide`) have no matching directory on branch main, so read the shipped four as the real package and treat the rest as index-only until a tree confirms them.

## Installation

The README documents no skills-install path. There is no `npx skills add` line, no plugin marketplace command and no plugin manifest anywhere in the checkout; the install material it does carry points at the per-language get-started pages on adk.dev and at the `llms.txt` / `llms-full.txt` context files. The skills themselves ship no install instructions either, so the route for a Hermes profile is a directory copy.

Clone once, then copy whole skill directories, because each in-tree skill ships a human-facing `README.md` beside its `SKILL.md`:

```bash
git clone --depth 1 https://github.com/google/adk-docs.git
cp -R adk-docs/.agents/skills/integration-review ~/.hermes/profiles/corpusiq/skills/integration-review
cp -R adk-docs/.agents/skills/integration-create ~/.hermes/profiles/corpusiq/skills/integration-create
cp -R adk-docs/.agents/skills/api-reference-audit ~/.hermes/profiles/corpusiq/skills/api-reference-audit
cp -R adk-docs/.agents/skills/adk-bot-review ~/.hermes/profiles/corpusiq/skills/adk-bot-review
```

If you only want one skill, fetch the file over the network without keeping a clone:

```bash
mkdir -p ~/.hermes/profiles/corpusiq/skills/adk-bot-review
curl -sL -o ~/.hermes/profiles/corpusiq/skills/adk-bot-review/SKILL.md \
  https://raw.githubusercontent.com/google/adk-docs/main/.agents/skills/adk-bot-review/SKILL.md
```

The directory name matters more than usual here. `.agents` is dot-prefixed, so a plain `skills/*` glob misses it, and `weather_skill` sits five levels deep under an examples tree rather than in a top-level skills folder; copy it only as a shape reference, not as a general-purpose skill. Nothing in the repository installs an ADK runtime, so any Hermes profile that will actually build agents still needs the SDK for its language of choice from the adk.dev get-started pages.

## What It Provides

The six rows below are the indexed listings at or above 500 installs. None of the six has a matching directory in the current tree, so their scope is read from the ADK feature set the README documents rather than from a shipped `SKILL.md`:

| Skill | Installs | Use For |
|---|---|---|
| adk-dev-guide | 2,742 | Core ADK development guidance: code-first agent logic, tool wiring and orchestration, framed around the Python, TypeScript, Go, Java and Kotlin start paths the README links. |
| adk-cheatsheet | 2,681 | Quick reference for ADK primitives and command shapes while an agent is being built, for the moments when a full documentation pass is too slow. |
| adk-scaffold | 2,645 | Project scaffolding: the directory and package skeleton for a new agent, its tools and its run entry point, before any agent logic is written. |
| adk-eval-guide | 2,623 | Evaluation work: test cases, scoring and repeatable runs for an agent, matching the evaluation stage the README names next to building and deploying. |
| adk-deploy-guide | 2,620 | Deployment of a finished agent: containerising onto Cloud Run or GKE, or scaling through Agent Runtime. |
| adk-observability-guide | 2,606 | Tracing and monitoring: reading the built-in agent observability data to debug and optimise a workflow instead of guessing at behaviour. |

The remaining 5 indexed listings range from 1 to 126 installs.

## Why This Matters for Hermes Agents

ADK is one of the few agent frameworks with published SDKs in five languages, so a Hermes profile asked to build, review or ship an agent on Google's stack needs ADK conventions rather than generic prompting advice. What this repository offers is narrower and more specific than a tutorial series: skills written by documentation maintainers for the work of maintaining documentation. The strongest of them is `integration-review`, which encodes a full review contract, four severity tiers, `file:line` anchoring, a recommended decision and draft-only output, and that contract transfers almost unchanged to any docs or content review job a Hermes agent is asked to run. `integration-create` complements it by naming the real template as the shipping pages themselves, the `docs/integrations/github.md` and `phoenix.md` exemplars, rather than an abstract skeleton, which is the same "copy what works" discipline that makes agent output reviewable. `api-reference-audit` is the one that reads like a governance tool: it detects drift between in-repo version strings and upstream package registries, recommends the per-surface release process, and refuses to emit an executable plan unless asked, which is the behaviour a cron job wants from a report-only step. For an agent working with ADK itself, the README's `llms.txt` and `llms-full.txt` are the cheaper context route, and the skills here are best treated as workflow partners to that context rather than as a substitute for it.

## Usage

| You say | What happens |
|---|---|
| "Review docs/integrations/bigquery.md before I open the PR" | `integration-review` compares the page against shipping peers in the same category, checks structure, links, working code and catalog conventions, and returns a prioritised report with `file:line` findings, a recommended decision and draft comments; nothing is posted to GitHub. |
| "Create an integration page for this observability tool" | `integration-create` picks the right category template, opens the exemplar pages for that category, drafts the Markdown under `docs/integrations/` with the required catalog tags, then hands the result to `integration-review` and `mkdocs serve`. |
| "Are our API reference pages current?" | `api-reference-audit` compares the generated pages under `docs/api-reference/` and the hardcoded version strings against upstream releases and package registries per SDK, then reports what needs bumping and which process to follow. |
| "Review this adk-bot PR" | `adk-bot-review` traces the PR back to its issue, confirms the change is technical and correctly sized, checks mergeability and CI, searches closed issues for rejected prior art, and lists what it could not verify. |
| "Are the version pins in these samples stale?" | `api-reference-audit` flags samples pinned to superseded releases as a light check and states plainly that deep sample verification is out of scope, rather than implying a full audit. |
| "Should I install adk-deploy-guide?" | Answer from the checkout, not the install count: the listing carries 2,620 installs but no directory exists on branch main, so re-check the tree and the skills.sh security page before depending on it. |
| "Add a weather tool to my ADK agent" | `weather_skill` is the shipped example: it declares `metadata.adk_additional_tools` with `get_weather` and instructs the agent to call it with a location, which is worth copying as a shape and not worth installing as a package. |

## Verification

Both raw paths below returned 200 on branch main when this guide was written on 2026-10-30:

```bash
curl -sL -o /dev/null -w "%{http_code} review\n" \
  https://raw.githubusercontent.com/google/adk-docs/main/.agents/skills/integration-review/SKILL.md
curl -sL -o /dev/null -w "%{http_code} api-audit\n" \
  https://raw.githubusercontent.com/google/adk-docs/main/.agents/skills/api-reference-audit/SKILL.md
```

Expect `200` twice. Read one before installing: the frontmatter is the routing contract, and both files state their trigger phrases in the `description` field, which is what decides whether your agent picks the skill up at all.

After a copy lands in the profile, confirm the file and the directory shape:

```bash
head -4 ~/.hermes/profiles/corpusiq/skills/integration-review/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/integration-review/
```

A good copy shows `name:` and `description:` in the frontmatter and lists both `SKILL.md` and `README.md` in the directory. The `README.md` is the usage guide the maintainers wrote, with the invocation phrasings and the shape of the report you should expect back.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-30) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| adk-dev-guide | Pass | Pass | Pass |
| adk-cheatsheet | Pass | Pass | Warn |
| adk-scaffold | Pass | Pass | Pass |
| adk-eval-guide | Pass | Pass | Pass |
| weather_skill | n/a | n/a | n/a |

No FAIL verdict appears in the sampled five. The single Warn sits on `adk-cheatsheet`, and the pack records the verdict rather than the finding behind it, so read that Snyk entry on skills.sh before you install it; a quick-reference skill is also the kind of file most likely to accumulate shell snippets, which is a plausible reason for a scanner to flag it. `weather_skill` is scored n/a by all three scanners, which is consistent with it being a three-paragraph documentation example rather than a maintained skill.

The shipped four carry no bundled `scripts/` directory and no executable helpers, so their attack surface is instruction text plus whatever the agent then does. That second half is the part worth reviewing: `integration-create` writes Markdown files into `docs/integrations/`, `api-reference-audit` reads package registries over the network, and the two review skills read repository history, pull request state and CI results. All four are written to report rather than act, and `api-reference-audit` explicitly does not edit files, run generators or open PRs by default, but a Hermes profile that grants write access will not inherit those scruples from the file alone.

## Limitations

- Snapshot data, verified 2026-10-30: 16,398 combined installs across 11 indexed listings; 1,530 GitHub stars; Apache-2.0; last pushed 2026-10-30. Counts drift over time.
- The index outruns the tree. skills.sh counts 11 listings while the checkout holds 5 `SKILL.md` files, and the six highest-install listings, `adk-dev-guide`, `adk-cheatsheet`, `adk-scaffold`, `adk-eval-guide`, `adk-deploy-guide` and `adk-observability-guide`, have no matching directory on branch main. Their install counts are real; what those skills contain cannot be read from this repository.
- There is no install mechanism to inherit. No `npx skills add` line, no plugin manifest, no marketplace metadata and no install instructions inside any `SKILL.md`, so every install is a manual copy that will not receive updates.
- The layout works against casual copying. `.agents/skills/` is dot-prefixed and skipped by ordinary globbing, and `weather_skill` lives at `examples/typescript/snippets/skills/skills/weather_skill/`, a path an agent will not find by listing a top-level skills directory.
- The skills are repository-specific, not framework-generic. Their steps name paths that only exist in an adk-docs checkout, `docs/integrations/`, `docs/api-reference/`, `scripts/integrations.py` and `CONTRIBUTING.md`, so pointed at your own project they will either fail a lookup or quietly review the wrong thing.
- Two of them need a live environment to be useful. `api-reference-audit` compares against PyPI, npm, pkg.go.dev and Maven Central, so it needs network access and a current checkout, and integration work wants `mkdocs` installed locally to preview a page before review.

## Related

- [OpenAI Agents Python Skills - Multi-Agent Setup](/hermes/skills/catalog/openai-agents-python-skills-setup)
- [Oh My Hermes (OMH) Suite - Multi-Agent Orchestration Skills Setup](/hermes/skills/catalog/oh-my-hermes-omh-suite-setup)
- [Claw Multi-Agent Skill Setup](/hermes/skills/catalog/claw-multi-agent-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Copy the directory, not the markdown file. Each in-tree skill ships a `README.md` that states the invocation phrasings and the expected report shape, and that file is half the value at install time.
- Install `integration-review` first even if your work is not ADK documentation. Its four-tier, `file:line` review contract is the most reusable thing in the repository and ports to any content review queue.
- Treat the six index-only listings as unverified. Before relying on any of them, confirm a directory exists on the branch and read the `SKILL.md`; the 16.4K combined figure is not evidence that a file will be there.
- For ADK facts rather than workflow, use the README's `llms.txt` and `llms-full.txt` pointers. A full documentation bundle in context beats a partial skill when the question is about sessions, tools or deployment targets.
- Rewrite the path tables at the top of whichever skill you adopt. `api-reference-audit` itself warns that its maps are hints rather than ground truth, and re-deriving a path when a lookup fails is the habit the file asks for.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
