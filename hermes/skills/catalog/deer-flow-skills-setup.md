---
title: "DeerFlow Skills - Deep Research Agent Setup"
description: "bytedance/deer-flow: 60.3K combined installs. ByteDance's open deep-research harness with 27 bundled skills for research, slides, media and docs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/deer-flow-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "deep research", "agent harness", "python"]
---

# DeerFlow Skills - Setup Guide

**Source:** [bytedance/deer-flow](https://www.skills.sh/bytedance/deer-flow) via skills.sh - 60.3K combined installs across 26 indexed listings; first seen 2026-10-30 (evening sweep)

**GitHub:** [bytedance/deer-flow](https://github.com/bytedance/deer-flow) - 84,743 stars, MIT License, branch main, last pushed 2026-10-31; 33 `SKILL.md` files across two trees, 29 under `skills/public/` and 4 under `.agent/skills/`, which resolve to 27 installable skill packages because six of the public files are eval fixtures nested inside `skill-reviewer/evals/fixtures/`

**Category:** Open-source deep-research agent harness with a bundled skill library

**Quality Tier:** 🟡 Yellow - four of the five sampled skills Pass all three auditors while find-skills carries Socket and Snyk Warn, and the licence and star count are strong but most skills only make sense inside the DeerFlow harness

DeerFlow is ByteDance's open-source super agent harness: a LangGraph application that orchestrates sub-agents, memory and sandboxes to carry out long research and build tasks, with skills as the extension layer that tells it how. The repository stands at 84,743 stars under the MIT License, and it took the number one spot on GitHub Trending after the 2.0 launch in February 2026. Version 2.0 is a ground-up rewrite that shares no code with v1, which is still maintained on the `main-1.x` branch.

The skills ship inside the framework rather than beside it, and that shapes what this guide is for. The checkout carries 27 installable skill packages and skills.sh indexes 26 of them, from ppt-generation at 5,251 installs down to three single-digit maintainer skills. Most exist to work on or with the DeerFlow harness: claude-to-deerflow drives a running instance over its HTTP API, deerflow-maintainer-orchestrator drafts and posts issue and PR comments for maintainers, blocking-io-guard keeps async backend code from blocking the event loop, engineer-system-change scrutinises system-level changes before they are built, and skill-reviewer grades skill packages against DeerFlow's own packaging rules. A smaller group reads as general-purpose and portable to any harness that loads standard Agent Skills: find-skills, frontend-design, data-analysis, chart-visualization, academic-paper-review, systematic-literature-review, code-documentation, vercel-deploy and web-design-guidelines. Read the `SKILL.md` before assuming a row is a standalone utility.

## Installation

The harness installs from the repository. The README's path is a clone plus an interactive wizard that takes about two minutes and writes a `config.yaml` and `.env` for you:

```bash
git clone https://github.com/bytedance/deer-flow.git
cd deer-flow
make setup
```

The wizard asks for an LLM provider, an optional web search provider, and execution preferences such as sandbox mode, bash access and file-write tools. Verify the result before starting anything:

```bash
make doctor
```

The container route is three make targets and needs Docker Compose v2.24 or newer:

```bash
make docker-init    # pull the sandbox image, once
make docker-start   # start services, sandbox mode read from config.yaml
make docker-logs    # tail the logs
```

Skills load from `skills/` under the project root by default. `DEER_FLOW_SKILLS_PATH` moves that root, which is the setting to use when the checkout sits outside the project or several deployments share one skill library.

One skill has a standalone install, and it is the only skills-CLI command the README documents, under Claude Code integration:

```bash
npx skills add https://github.com/bytedance/deer-flow --skill claude-to-deerflow
```

`--skill` takes any package name from the table below, so the same call installs deep-research, frontend-design or web-design-guidelines into a harness that is not DeerFlow at all. That is the route that matters for a Hermes profile, which can load the markdown without running the harness. The checkout holds 33 `SKILL.md` files and 27 packages; the fixture files are supporting data, not extra skills.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| ppt-generation | 5,251 | Planning a deck, generating one image per slide with the previous slide as a style reference, and assembling them into a PPTX file. |
| claude-to-deerflow | 3,853 | Talking to a running DeerFlow instance over its HTTP API: sending research questions, starting threads, checking health, listing models and skills, uploading files. |
| find-skills | 3,831 | Discovering and installing agent skills from the open ecosystem when a request needs a capability the agent does not already have. |
| frontend-design | 3,721 | Building distinctive, production-grade web UI such as components, pages, dashboards and posters, with explicit rules against generic AI aesthetics. |
| data-analysis | 3,637 | Querying uploaded Excel and CSV files through DuckDB, covering schema inspection, aggregation, joins, pivot tables and export to CSV, JSON or Markdown. |
| consulting-analysis | 3,062 | Two-phase report work: an analysis framework with chapter skeleton and data requirements first, then a finished report with charts and strategic insight once data exists. |
| video-generation | 3,041 | Generating video from a structured prompt plus an optional reference image, driven by a bundled Python script. |
| image-generation | 2,924 | Generating images from structured JSON prompts, optionally with reference images to guide the result. |
| github-deep-research | 2,916 | Multi-round investigation of a repository through the GitHub API plus web search and fetch, ending in a report with timeline, metrics and Mermaid diagrams. |
| deep-research | 2,785 | A multi-angle web research methodology to load before content work, instead of one superficial search. |
| academic-paper-review | 2,714 | A structured, peer-review-grade critique of a single paper: summary, methodology, contribution, literature positioning, recommendations. |
| chart-visualization | 2,643 | Choosing one of 26 chart types from the data, extracting parameters and rendering the chart image with a JavaScript script. |
| systematic-literature-review | 2,469 | Breadth-first synthesis across many arXiv papers on a topic, with annotations and citations in APA, IEEE or BibTeX style. |
| podcast-generation | 2,433 | Turning written content into a two-host conversational podcast script and synthesising the audio. |
| skill-creator | 2,348 | Writing new skills, editing existing ones, running evals and benchmarks, and tuning a description for trigger accuracy. |
| web-design-guidelines | 2,337 | Reviewing UI code against the Web Interface Guidelines for accessibility and design conformance. |
| surprise-me | 2,283 | Discovering enabled skills and combining them creatively for an unexpected showcase when the user asks to be surprised. |
| vercel-deploy | 2,226 | Deploying a project to Vercel with no authentication and returning a preview URL plus a claimable link. |
| code-documentation | 1,930 | Generating READMEs, API references, inline comments, architecture docs, changelogs and developer guides for a codebase. |
| newsletter-generation | 1,832 | Researching a topic, curating sources and drafting a publishable newsletter or digest in Markdown. |

The remaining 6 indexed listings range from 6 to 1,539 installs.

The tail is mostly tooling rather than product surface: bootstrap at 1,539, music-generation at 298 and skill-reviewer at 199, then the three DeerFlow maintainer skills at 7, 7 and 6 installs. One package in the tree carries no listing at all, `.agent/skills/smoke-test`, which walks a deployment through pull, install, availability check and health check in one run. Treat the single-digit rows as internal maintainer tooling and judge the suite by the research, analysis and presentation skills at the top.

## Why This Matters for Hermes Agents

DeerFlow is the most complete public example of a harness that treats skills as the primary extension mechanism rather than an add-on, and the 27 packages here are worth reading even if you never start the harness. Each one is a single `SKILL.md` with frontmatter, inline scripts and a workflow of numbered steps, which makes the suite a free reference for how a research-oriented skill should be scoped: deep-research is a routing rule that fires before any content task, academic-paper-review defines its output sections up front, and systematic-literature-review explicitly tells the agent when to hand off to the single-paper skill instead of doing both badly.

Several of the packages transfer to a Hermes profile with a one-line install and no dependencies on the harness. find-skills turns skill discovery into a step the agent can take on its own, frontend-design and web-design-guidelines cover the write and review halves of front-end work, and data-analysis plus chart-visualization chain into a short path from a spreadsheet to a rendered figure.

The rest are worth having for the opposite reason: they are specs. blocking-io-guard, engineer-system-change and skill-reviewer encode how a large agent project keeps its own quality bar, and that is the part most skill libraries skip.

For profiles that do run research at volume, claude-to-deerflow reframes the harness as a service. Hermes can hand a long investigation to a running DeerFlow gateway over HTTP, poll the thread, and read back the report, which keeps a heavy multi-round crawl off the local machine without giving up the skill layer.

## Usage

| You say | What happens |
|---|---|
| "Review this paper and tell me whether the method holds up" | academic-paper-review loads and produces a sectioned critique: summary, strengths, weaknesses, methodology assessment, contribution, literature positioning, recommendations. |
| "Map the competitive landscape for this category and write the report" | deep-research gathers from multiple angles, then consulting-analysis generates the chapter skeleton and data requirements before the report is assembled with charts. |
| "Turn this research into a deck for Thursday" | ppt-generation plans the structure, generates one image per slide using the previous slide as a style reference, and composes a PPTX. |
| "Here is a CSV, find the outliers and chart them" | data-analysis queries the file through DuckDB, then chart-visualization picks one of 26 chart types and renders the image. |
| "Is DeerFlow healthy, and what models does it have?" | claude-to-deerflow calls the gateway API for health, model, skill and agent listings, then reports back in the conversation. |
| "Find me a skill that does X" | find-skills searches the open skills ecosystem and walks through installing the match. |
| "Check my UI against the design guidelines" | web-design-guidelines fetches the current guidelines, reads the named files or pattern, and returns findings in a terse `file:line` format. |

## Verification

Both raw paths below returned 200 on branch main when this guide was written on 2026-10-30:

```bash
curl -sL -o /dev/null -w "%{http_code} ppt\n" \
  https://raw.githubusercontent.com/bytedance/deer-flow/main/skills/public/ppt-generation/SKILL.md
curl -sL -o /dev/null -w "%{http_code} deep-research\n" \
  https://raw.githubusercontent.com/bytedance/deer-flow/main/skills/public/deep-research/SKILL.md
```

Expect `200` twice. Read the ppt-generation file before installing anything: its frontmatter `description` is the sentence that decides whether the skill triggers on your request, and the body names the two composition rules (EXIF orientation, transparent PNG preservation) that later changes to the repository keep touching.

After a clone, confirm the package count and that the loader will see what you expect:

```bash
cd deer-flow
find . -name SKILL.md | wc -l
ls -d skills/public/*/ | wc -l
head -8 skills/public/deep-research/SKILL.md
```

A good checkout reports 33 and 23, and the head shows `name:` and `description:` frontmatter. Then `make doctor`, which prints the configuration it resolved and actionable hints for anything it refuses.

For a Hermes profile, the install is a directory copy and the check is one file:

```bash
cp -r skills/public/deep-research ~/.hermes/profiles/corpusiq/skills/deep-research
head -6 ~/.hermes/profiles/corpusiq/skills/deep-research/SKILL.md
```

## Security

Two of the five sampled skills carry a Warn, find-skills on both Socket and Snyk, which means those two scanners flagged the package and it should not be treated as cleared for production use until you read the findings yourself.

skills.sh verdicts for sampled skills (verified 2026-10-30) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ppt-generation | Pass | Pass | Pass |
| claude-to-deerflow | Pass | Pass | Pass |
| find-skills | Pass | Warn | Warn |
| frontend-design | Pass | Pass | Pass |
| engineer-system-change | Pass | Pass | Pass |

The find-skills warnings are the interesting case: the skill's job is to search an external registry and install what it finds, so the scanner surface is the install action itself rather than the markdown. Installing it gives an agent the ability to add arbitrary third-party code to a profile, and the skill that ends up installed has not been audited by anyone. Keep it behind a review step or leave it out of an unattended profile.

Two more things sit outside the verdict table. Several skills execute local scripts and call external APIs: video-generation, music-generation, podcast-generation, image-generation and chart-visualization all shell out to bundled Python, and each needs its own provider key, which lands next to the code in the checkout. And the harness itself is the larger surface: `make setup` writes model and search credentials into `.env`, bash access and file-write tools are configurable, sandbox mode decides whether generated code runs on the host, and self-hosted fetch backends are refused by default unless you confirm outbound isolation. Read `config.example.yaml` before turning those on.

## Limitations

- Snapshot data, verified 2026-10-30: 60,292 combined installs across 26 indexed listings; 84,743 GitHub stars; MIT License; last pushed 2026-10-31. Counts drift over time.
- The last-pushed date, 2026-10-31, sits one day after the snapshot date. It is carried verbatim from the repository metadata rather than adjusted, and it is the reason this suite moves: re-read the `SKILL.md` you copied, because the one on main may be newer than the guide.
- The index and the tree do not line up one to one. There are 26 listings against 27 packages, and the extra one is `.agent/skills/smoke-test`, which ships with the repository but has no skills.sh entry. The six extra `SKILL.md` files under `skill-reviewer/evals/fixtures/` are test fixtures, not skills.
- Most of the suite is not portable. claude-to-deerflow needs a DeerFlow gateway listening on port 2026, blocking-io-guard scans DeerFlow's own backend paths, deerflow-maintainer-orchestrator assumes maintainer rights on the repository, and skill-reviewer grades against DeerFlow packaging conventions. Copying those into another profile gives you instructions for a system you do not have.
- Running the harness is not a small install. Local development is quoted at 4 vCPU, 8 GB RAM and 20 GB of disk to be comfortable, Docker builds want more headroom, and a production `make up` stack is quoted at 8 vCPU and 16 GB. Multi-round deep research also spends real model tokens per run.
- The install counts are not a quality ranking. One skill holds 5,251 of the 60,292 combined installs, three rows sit in single digits, and the lowest of them are internal maintainer tooling that no external user was ever meant to install.

## Related

- [Deep Agents - Batteries-Included Agent Harness Setup](/hermes/skills/catalog/deepagents-setup)
- [Deep Research Skill - Citation-Tracked Research Setup](/hermes/skills/catalog/claude-deep-research-skill-setup)
- [AI Research Skills - 100-Skill ML Research Library Setup](/hermes/skills/catalog/ai-research-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install from the skills CLI for a single skill and from the clone for the whole suite. `npx skills add https://github.com/bytedance/deer-flow --skill find-skills` puts one markdown file in place with no harness, while `make setup` is only worth it when you actually want the DeerFlow gateway.
- Start with deep-research, academic-paper-review and systematic-literature-review. They are the three that read as methodology rather than plumbing, they need no provider keys, and they show how the suite separates a routing rule from an execution skill.
- Skip vetting by install count. The 5,251-install leader is a slide composer, and the two most interesting packages for an agent builder, engineer-system-change and blocking-io-guard, have 6 and 7 installs. Read `description` and the numbered steps, not the number in the table.
- Keep the copied skill out of the checkout. Copy `skills/public/<name>` into the profile instead of symlinking, because DeerFlow follows operator-managed symlinks on its own discovery pass and a link shared by both loaders will drift when the repository moves.
- Run `make doctor` after any configuration change rather than reading the failure out of a startup log. It reports refused backends, missing keys and unwritable runtime paths in one pass, with the fix in the same message.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
