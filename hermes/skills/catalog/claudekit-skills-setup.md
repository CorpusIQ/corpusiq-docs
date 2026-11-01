---
title: "ClaudeKit Skills - Full Stack Agent Toolkit"
description: "mrgoonie/claudekit-skills: 18.0K combined installs. A 45-skill full-stack toolkit for backend, debugging, MCP building and documents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claudekit-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-31"
tags: ["hermes skill", "agent skill", "skill setup", "claude code", "full stack", "mcp"]
---

# ClaudeKit Skills - Setup Guide

**Source:** [mrgoonie/claudekit-skills](https://www.skills.sh/mrgoonie/claudekit-skills) via skills.sh - 18.0K combined installs across 33 indexed listings; first seen 2026-10-31 (evening sweep)

**GitHub:** [mrgoonie/claudekit-skills](https://github.com/mrgoonie/claudekit-skills) - 2,230 stars, no LICENSE file, branch main, last pushed 2026-04-03; 45 `SKILL.md` files under `.claude/skills/`, 31 of them at the top level and 14 nested inside three grouped packs (`debugging/` with four sub-skills, `problem-solving/` with six, `document-skills/` with docx, pdf, pptx and xlsx), plus a shared `common/` directory and 12 plugin manifests under `plugins/`

**Category:** Full-stack delivery toolkit for agents: document skills, UI styling, MCP building and code review

**Quality Tier:** 🟡 Yellow - a Gen Agent Trust Hub Warn on `debugging`, a Snyk Fail on `pdf`, and no LICENSE file in the repository

ClaudeKit is one person's working notes on Claude Code turned into a skills collection, and the README says as much: six months of digging into the tool, published as a free tier with a paid bundle at ClaudeKit.cc behind it. What ships here is broad rather than deep in any one place. Backend, frontend, databases, DevOps, testing, document processing, media processing, 3D, Shopify, payments, MCP building and a set of Anthropic-authored meta skills all sit in the same tree, and the marketplace groups them into 12 installable plugin categories.

The structure is a `.claude/skills/` directory with 45 `SKILL.md` files, three of the groups being containers rather than single skills: `debugging` pairs a router skill with root cause tracing, defense in depth, systematic debugging and verification before completion; `problem-solving` pairs a router with six named techniques plus a `when-stuck` dispatcher; `document-skills` holds docx, pdf, pptx and xlsx as four separate skills. That fan-out matters when you install, because a copy of a parent directory has to travel with its children or the router skills break.

## Installation

The README's recommended route is the Claude Code plugin marketplace, which installs a named category rather than the whole tree:

```
/plugin marketplace add mrgoonie/claudekit-skills
/plugin install ai-ml-tools@claudekit-skills
/plugin install web-dev-tools@claudekit-skills
/plugin install devops-tools@claudekit-skills
```

The available categories are `ai-ml-tools`, `web-dev-tools`, `devops-tools`, `backend-tools`, `document-processing`, `debugging-tools`, `problem-solving-tools`, `platform-tools`, `meta-tools`, `media-tools`, `research-tools` and `specialized-tools`, each backed by a directory under `plugins/` and described in `.claude-plugin/marketplace.json`. The plugin route is Claude Code only, and the repository documents no skills CLI command, so `npx skills add` is not an option here and anything that claims otherwise for this repo is guesswork.

The README's manual route is marked deprecated but still works, and it is the one Hermes needs, adjusted to copy the skills tree rather than the whole `.claude` directory:

```bash
git clone --depth 1 https://github.com/mrgoonie/claudekit-skills.git /tmp/claudekit-skills
cp -r /tmp/claudekit-skills/.claude/skills/. ~/.hermes/profiles/corpusiq/skills/
```

`INSTALLATION.md` is worth reading before the first run, because most skills assume tools that are not in the repo. `ai-multimodal` is the only skill with Python packages, listed in `scripts/requirements.txt` (`google-genai`, `pypdf`, `python-docx`, `markdown`, `Pillow`, `python-dotenv`). `media-processing` needs FFmpeg and ImageMagick, `devops` wants Wrangler, Docker and the Google Cloud CLI, `better-auth` and `shopify` want Node.js 18 or newer with the Better Auth and Shopify CLIs, and `databases` wants a PostgreSQL client and the MongoDB shell.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| backend-development | 2,307 | APIs, auth, data access, CI/CD and microservice patterns in Node.js, Python, Go or Rust, with OWASP Top 10 coverage and scalability guidance. |
| sequential-thinking | 1,798 | Step-by-step reasoning that can revise and branch for multi-stage analysis, design planning and problem decomposition. |
| threejs | 1,255 | 3D web work in Three.js on WebGL or WebGPU: scenes, shaders, PBR materials, VR and XR experiences, and product configurators. |
| devops | 990 | Deploys to Cloudflare Workers, R2 and D1, Docker, Cloud Run and GKE, Kubernetes with kubectl and Helm, plus CI/CD and security audits. |
| chrome-devtools | 740 | Browser automation and performance work through Puppeteer CLI scripts: screenshots, network traces, form automation and JavaScript debugging. |
| aesthetic | 718 | Visual design principles for interfaces, including inspiration capture through `chrome-devtools`, iterative design images through `ai-multimodal` and design documentation. |
| ui-styling | 639 | shadcn/ui and Tailwind component work: design systems, responsive layouts, accessible dialogs and tables, theming and dark mode. |
| problem-solving | 576 | A router across creative techniques (collision-zone thinking, inversion, pattern recognition, simplification cascades) with a `when-stuck` dispatcher for the right one. |
| debugging | 573 | Systematic debugging with four sub-skills: root cause tracing, defense in depth, systematic debugging and verification before completion. |
| media-processing | 562 | FFmpeg and ImageMagick pipelines: format conversion, codec choices, HLS and DASH manifests, thumbnails, filters and batch image work. |
| ai-multimodal | 535 | Google Gemini API work: audio transcription with timestamps, image understanding and generation, video analysis and PDF or document extraction. |
| code-review | 518 | Receiving review feedback with technical rigour, requesting reviews from a subagent, and gating completion claims on evidence. |
| context-engineering | 499 | Designing agent context: degradation patterns, compaction, masking and caching, memory architectures, multi-agent patterns and LLM-as-judge evaluation. |
| shopify | 452 | Shopify apps, extensions and themes: GraphQL and REST admin APIs, the Shopify CLI, Polaris components, Liquid, webhooks and billing. |
| web-testing | 444 | Playwright, Vitest and k6 across E2E, unit, integration, load, visual and accessibility testing, including flake and Core Web Vitals work. |
| databases | 438 | MongoDB and PostgreSQL schema design, queries, aggregation, indexing, migrations, replication, backup and administration. |
| frontend-design | 419 | Distinctive, production-grade frontend code that avoids the generic look of generated interfaces. |
| docs-seeker | 405 | Finding current technical documentation through the llms.txt standard, Repomix packing and parallel source exploration. |
| repomix | 404 | Packing repositories into single AI-readable files with include and exclude patterns, XML or Markdown output, and token counts. |
| better-auth | 392 | TypeScript authentication: email and password, OAuth providers, TOTP and SMS second factors, passkeys, sessions, RBAC and rate limiting. |

The remaining 13 indexed listings range from 83 to 375 installs. The document skills sit at the bottom of that tail (`docx` 88, `pptx` 85, `xlsx` 84, `pdf` 83), which is worth knowing because they are the ones with the heaviest script bundles.

## Why This Matters for Hermes Agents

The pitch for this pack is breadth with no setup cost. A single clone gives a profile the design, backend, DevOps, testing and document workflows that most delivery tasks touch, and the skills are written as workflows with guardrails rather than as documentation summaries, so the agent gets an instruction order instead of a knowledge dump. For a profile that does research, publishing and site work, the useful overlap is `docs-seeker`, `repomix`, `context-engineering` and `code-review`, which are the four that change how an agent reasons rather than what it can build.

`code-review` is the sharpest of those. It is explicitly about refusing performative agreement, requesting review through a subagent, and demanding evidence before any completion claim, which is the same failure mode most agent runs exhibit when they report a task done without running it. `context-engineering` covers the other half of the same problem: compaction, masking, caching and memory architecture, written by someone who was fighting context limits in Claude Code rather than describing them abstractly.

The meta skills are the reason to read before copying. `skill-creator` and `template-skill` show the author's own conventions for skill structure, which is useful as a comparison point for a house style, and `docs-seeker` implements the llms.txt lookup pattern that keeps a profile from asserting facts about a library it has not read.

## Usage

| You say | What happens |
|---|---|
| "Build the API for this feature" | `backend-development` picks the framework path, lays out routes, auth and data access, and adds the security and testing checklist. |
| "These two tests flake in CI" | `debugging` routes to root cause tracing or systematic debugging, then `verification-before-completion` demands a rerun as evidence before the fix is called done. |
| "Package this repo so you can reason about it" | `repomix` packs the tree with include and exclude patterns and reports a token count before the agent reads it. |
| "Find the current docs for this library" | `docs-seeker` tries the llms.txt standard first, falls back to parallel source exploration, and packs a GitHub repo when no documentation exists. |
| "Review this PR before I merge it" | `code-review` runs the three practices: technical review of the diff, a subagent review pass, and a verification gate that blocks a success claim without evidence. |
| "Make this dashboard look less generated" | `aesthetic` and `ui-styling` work the hierarchy, spacing and component layer, with `frontend-design` writing the code. |
| "Turn this PDF into structured data" | The `pdf` sub-skill under `document-skills` reads the form and table tooling in its `scripts/` folder; read that skill before running it, given its verdicts. |

## Verification

The raw path for the top skill returned HTTP 200 on branch main when this guide was written on 2026-10-31:

```bash
curl -sL -o /dev/null -w "%{http_code} backend-development\n" \
  https://raw.githubusercontent.com/mrgoonie/claudekit-skills/main/.claude/skills/backend-development/SKILL.md
```

Expect `200`. Inspect the clone before copying, since the grouped packs are the part that silently breaks:

```bash
find /tmp/claudekit-skills/.claude/skills -name SKILL.md | wc -l
head -6 /tmp/claudekit-skills/.claude/skills/backend-development/SKILL.md
ls /tmp/claudekit-skills/.claude/skills/debugging
```

The count should print 45, the header should show `name: backend-development` with a `license: MIT` field in the frontmatter, and the listing should show four sub-skill directories beside `SKILL.md`. After the copy, `ls ~/.hermes/profiles/corpusiq/skills/debugging` should show the same four.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-31) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| backend-development | Pass | Pass | Pass |
| debugging | Warn | Pass | Pass |
| frontend-design | Pass | Pass | Pass |
| skill-creator | Pass | Pass | Warn |
| pdf | Pass | Pass | Fail |

The licensing position needs stating plainly, because it is the weakest part of this pack. There is no LICENSE file anywhere in the repository, which under default copyright means no grant to redistribute, while each `SKILL.md` carries `license: MIT` in its own frontmatter and `.claude-plugin/marketplace.json` declares `"license": "MIT"` for the `ai-ml-tools` plugin only. Treat the pack as MIT by intent, not by instrument: fine to read and use locally, unsettled if you plan to redistribute it, and worth an issue to the owner before you publish a derivative.

The `pdf` Fail is the one to respect. That sub-skill carries a script bundle that writes to real documents: filling form fields, annotating forms, converting PDFs to images, extracting field info and checking bounding boxes. None of that needs a network connection to cause damage if it is handed the wrong file, and the scanners are right to look harder at it than at a markdown-only skill. Read `document-skills/pdf/scripts` before letting an agent run it unattended.

The rest of the surface is ordinary development tooling. The 78 Python scripts concentrate in `document-skills` (32), then `media-processing`, `databases` and `ai-multimodal` at six each, with the remainder spread across `web-frameworks`, `ui-styling`, `skill-creator` and `devops`. The 22 JavaScript files are mostly `chrome-devtools` Puppeteer scripts (15), plus `payment-integration` (4) and a built `mcp-management` dist (3). The 78 XSD schemas belong to the OOXML validation sets under `document-skills/docx` and `document-skills/pptx`, and the 54 font files sit in `ui-styling/canvas-fonts`. The `debugging` Warn on Gen Agent Trust Hub and the `skill-creator` Snyk Warn are prompt-level flags rather than code findings; both skills are instructions about how to critique and how to write skills, and neither ships executables.

## Limitations

- Snapshot data, verified 2026-10-31: 17,978 combined installs across 33 indexed listings; 2,230 stars; no LICENSE file; last pushed 2026-04-03. Counts drift over time.
- No LICENSE file in the repository. Per-skill frontmatter and one marketplace entry claim MIT, so the intent is clear, but the grant itself is missing.
- The index and the tree disagree on one name: `frontend-dev-guidelines` carries 375 installs and has no directory in the current tree, while the tree's `frontend-development/` directory has no indexed listing. Treat the pair as the same intent and read the directory.
- Last pushed 2026-04-03, which is about seven months before this snapshot. Framework-specific material (`frontend-development`, `web-frameworks`, `shopify`) can lag the versions an agent is asked about, so verify against current docs before trusting version details.
- The tree holds 45 `SKILL.md` files against 33 indexed listings, and the difference is structural: the `debugging` and `problem-solving` packs contribute ten sub-skill files that are counted once at parent level, `claude-code`, `google-adk-python` and `frontend-development` are in the tree but not in the index, and `frontend-dev-guidelines` is in the index without a directory.
- Several skills need tooling that is not in the repo: FFmpeg and ImageMagick for `media-processing`, Wrangler, Docker and the Google Cloud CLI for `devops`, Node.js 18 or newer for `shopify` and `better-auth`, and Python packages plus a Gemini API key for `ai-multimodal`.

## Related

- [Dot Skills - 96-Skill Agent Engineering Collection Setup - Setup Guide](/hermes/skills/catalog/dot-skills-setup)
- [Adobe Skills - PDF, Document and Creative Suite Setup](/hermes/skills/catalog/adobe-skills-setup)
- [Build Mcp Server Setup](/hermes/skills/catalog/build-mcp-server-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install by group, not by file. `debugging` and `problem-solving` are routers whose value is in the sub-skill directories beside them, and a copy that takes only the parent `SKILL.md` leaves the agent with an index and no content.
- Put `code-review` in the profile before anything else. It is the skill that makes an agent show a rerun instead of claiming success, and it changes the quality of every other task more than any build skill here.
- Give `context-engineering` a read even if you never install it. Its compaction and masking sections describe the failure modes a long-running profile hits, and the vocabulary alone makes context problems easier to debug.
- Read `.claude-plugin/marketplace.json` before using the plugin route. Category names and contents are defined there, and the plugin route installs a category rather than the tree, so what you get depends on which one you name.
- Treat the `pdf` skill as code review material. Its scripts touch real documents, and its Snyk Fail is the only hard failure in the pack, so read the scripts before an unattended run.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
