---
title: "Anthropic Skills - Official Agent Skills Repository"
description: "anthropics/skills: 4017.6K combined installs. Anthropic's Agent Skills repository covering documents, design, testing and the Claude API."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/anthropics-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-27"
tags: ["hermes skill", "agent skill", "skill setup", "anthropic", "claude", "agent skills"]
---

# Anthropic Skills - Setup Guide

**Source:** [anthropics/skills](https://www.skills.sh/anthropics/skills) via skills.sh - 4017.6K combined installs across 21 indexed listings; first documented 2026-11-27 (evening sweep)

**GitHub:** [anthropics/skills](https://github.com/anthropics/skills) - 201,604 stars, no LICENSE file at the repo root (individual skill directories carry their own LICENSE.txt files, and the README describes many skills as Apache 2.0), branch main, last pushed 2026-11-16; skills live under `skills/<name>/SKILL.md` with a `.claude-plugin/marketplace.json`.

**Category:** Agent skills reference - document creation, design, web testing, MCP server building and Claude API guidance for agent runtimes

**Quality Tier:** 🟠 Orange - Snyk fails pptx and docx; Warn cells land on skill-creator (Socket), webapp-testing (Socket and Snyk), mcp-builder (Snyk), web-artifacts-builder (Socket), doc-coauthoring (Snyk), internal-comms (Snyk) and academy-guide (Snyk).

anthropics/skills is Anthropic's implementation of skills for Claude, published as a public repository and indexed on skills.sh. Skills are folders of instructions, scripts and resources that Claude loads dynamically to handle specialized tasks in a repeatable way. The README frames the repository as a demonstration of what is possible with the skills system, spanning creative applications (art and design), technical tasks (web app testing and MCP server generation) and enterprise workflows (communications and branding).

The 21 indexed listings range from frontend-design at over a million installs down to a pair of small guides. The document skills (docx, pdf, pptx and xlsx) are the ones that power Claude's document capabilities, shared here as open source (Apache 2.0) as a reference for more complex production skills. Each skill is self-contained in its own folder with a SKILL.md file carrying the frontmatter and instructions that Claude reads.

## Installation

The README installs this repository as a Claude Code plugin marketplace. Register it, then install either the document-skills or example-skills plugin:

```text
/plugin marketplace add anthropics/skills
```

Then select `Browse and install plugins`, pick `anthropic-agent-skills`, choose `document-skills` or `example-skills`, and select `Install now`. Either plugin can also be installed directly:

```text
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```

After installing, invoke a skill by mentioning it, for example "Use the PDF skill to extract the form fields from path/to/some-file.pdf". The example skills are already available to paid plans in Claude.ai, and Anthropic's pre-built and custom skills can be used through the Claude API via the Skills API Quickstart.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| frontend-design | 1,178,349 | Distinctive, intentional visual design for new or reshaped UI: aesthetic direction, typography and choices that avoid templated defaults. |
| skill-creator | 444,827 | Create, edit and measure skills, run evals, benchmark performance and tune descriptions for better triggering. |
| pptx | 265,671 | Anything involving .pptx or .potx files: create, read, edit, combine or split decks and templates. |
| pdf | 239,231 | Read, merge, split, rotate, watermark, fill forms, encrypt and OCR PDF files. |
| docx | 227,492 | Create, read and edit Word .docx and .dotx files, including tracked changes, comments and formatting. |
| webapp-testing | 216,522 | Test local web apps with Playwright: verify frontends, debug UI, capture screenshots and read browser logs. |
| xlsx | 207,544 | Open, edit, create and convert spreadsheet files (.xlsx, .csv, .tsv), including formulas and charting. |
| mcp-builder | 148,982 | Build MCP servers in Python (FastMCP) or Node/TypeScript (MCP SDK) that expose well-designed tools. |
| canvas-design | 141,664 | Create original visual art as .png or .pdf posters and static designs. |
| web-artifacts-builder | 124,946 | Build multi-component claude.ai HTML artifacts with React, Tailwind CSS and shadcn/ui. |
| brand-guidelines | 124,727 | Apply Anthropic's official brand colors and typography to artifacts. |
| theme-factory | 108,221 | Style artifacts with one of 10 preset themes, or generate a new theme. |
| doc-coauthoring | 107,186 | Structured workflow for co-authoring documentation, proposals, specs and decision docs. |
| algorithmic-art | 100,657 | Generative art with p5.js: seeded randomness, flow fields and particle systems. |
| internal-comms | 90,487 | Company internal communications: status reports, leadership updates, newsletters, FAQs and incident reports. |
| slack-gif-creator | 84,865 | Animated GIFs optimized for Slack, with constraints and validation tools. |
| claude-api | 84,790 | Claude API and Anthropic SDK reference: models, pricing, streaming, tool use, MCP, caching and migration. |
| template-skill | 79,437 | A starting template for authoring a new skill with name and description frontmatter plus instructions. |
| discernment-nudge | 21,123 | Append short follow-up questions after substantive answers to check facts and assumptions. |
| academy-guide | 20,688 | Recommend matching Claude Academy courses and tutorials before finishing how-to replies. |

The remaining 1 indexed listing is claude-academy-guide (194 installs), which has no counterpart in the current repo tree.

The table above follows the skills.sh install index. Two names drift from the `skills/<name>/` layout: template-skill lives at `template/SKILL.md`, and claude-academy-guide carries an install count but no directory in the tree.

## Why This Matters for Hermes Agents

This repository is the reference implementation of the Agent Skills standard, so it is the best single source for how a production skill should be structured: a self-contained folder, a SKILL.md with two frontmatter fields (name and description) plus instructions, examples and guidelines. A Hermes builder wiring skills into a router can treat these as the canonical patterns to copy.

The document skills are the most instructive for scale: docx, pdf, pptx and xlsx each bundle scripts, Office Open XML schemas and validators under `scripts/office/`, showing how a skill can carry executable tooling rather than instructions alone. The README notes these are the same skills that power Claude's document capabilities, shared as a reference for complex production skills.

The repository also demonstrates a clean separation of concerns: `template/SKILL.md` is a blank starting point, `spec/agent-skills-spec.md` is the standard itself, and `.claude-plugin/marketplace.json` groups the skills into installable plugin sets. That structure is worth copying for any publisher that wants one repository to serve both a marketplace and individual installs.

Finally, the security verdicts are a useful calibration: a mostly-Markdown repository can still carry Snyk failures in its document skills, so even a vendor's official suite deserves a scan before it enters a production profile.

## Usage

| You say | What happens |
|---|---|
| "Make me a GIF of a rocket launching for Slack" | Uses slack-gif-creator to build a Slack-optimized animated GIF with validation. |
| "Create a pitch deck from this outline" | Uses pptx to build a .pptx slide deck. |
| "Extract the form fields from this PDF" | Uses pdf to read the form structure and field names. |
| "Build an MCP server that wraps this REST API" | Uses mcp-builder to scaffold a Python or Node/TypeScript MCP server. |
| "Test my local web app's login flow" | Uses webapp-testing to drive Playwright against the running app. |
| "Design a poster in this brand's colors" | Uses canvas-design for the art and brand-guidelines for colors and typography. |
| "Write a status update for leadership" | Uses internal-comms to draft the update in the company's format. |

## Verification

The README installs through the Claude Code plugin marketplace, so the cleanest pre-install check is to fetch a skill's SKILL.md directly and read its frontmatter. The layout on branch main is `skills/<name>/SKILL.md`:

```bash
curl -sL https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md
```

After a clone, confirm the skill directories and the marketplace manifest:

```bash
git clone --depth 1 https://github.com/anthropics/skills.git /tmp/anthropic-skills
ls /tmp/anthropic-skills/skills/
head -3 /tmp/anthropic-skills/skills/frontend-design/SKILL.md
cat /tmp/anthropic-skills/.claude-plugin/marketplace.json
```

The skills listing should show 19 skill directories (academy-guide through xlsx). The repo root additionally holds `template/` (the template-skill starting point), `spec/` (the Agent Skills specification) and the `.claude-plugin/marketplace.json` manifest.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-27) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| frontend-design | Pass | Pass | Pass |
| skill-creator | Pass | Warn | Pass |
| pptx | Pass | Pass | Fail |
| pdf | Pass | Pass | Pass |
| docx | Pass | Pass | Fail |
| webapp-testing | Pass | Warn | Warn |
| xlsx | Pass | Pass | Pass |
| mcp-builder | Pass | Pass | Warn |
| canvas-design | Pass | Pass | Pass |
| web-artifacts-builder | Pass | Warn | Pass |
| brand-guidelines | Pass | Pass | Pass |
| theme-factory | Pass | Pass | Pass |
| doc-coauthoring | Pass | Pass | Warn |
| algorithmic-art | Pass | Pass | Pass |
| internal-comms | Pass | Pass | Warn |
| slack-gif-creator | Pass | Pass | Pass |
| claude-api | Pass | Pass | Pass |
| template-skill | Pass | Pass | Pass |
| discernment-nudge | Pass | Pass | Pass |
| academy-guide | Pass | Pass | Warn |

This guide is Orange because Snyk fails pptx and docx. The Gen Agent Trust Hub passes all 20 sampled listings, and the Warn cells sit on skill-creator (Socket), webapp-testing (Socket and Snyk), mcp-builder (Snyk), web-artifacts-builder (Socket), doc-coauthoring (Snyk), internal-comms (Snyk) and academy-guide (Snyk). Only 20 of the 21 indexed listings were sampled; claude-academy-guide is not covered.

## Limitations

- Snapshot data, verified 2026-11-27: 4,017,603 combined installs across 21 indexed listings; 201,604 GitHub stars; no LICENSE file at the repo root; last pushed 2026-11-16. Counts drift over time.
- No LICENSE file at the repo root: individual skill directories carry their own LICENSE.txt files (doc-coauthoring has none), and the README describes many skills as Apache 2.0, so confirm per-skill terms before redistributing.
- The install index outruns the tree: claude-academy-guide carries 194 installs but has no directory in the current tree, and template-skill lives at `template/SKILL.md` rather than under `skills/`.
- The README states the skills are provided for demonstration and educational purposes only; the behavior you receive from Claude may differ from what the skills show, so test thoroughly before relying on them for critical tasks.
- The security verdicts cover 20 of the 21 indexed listings; claude-academy-guide was not sampled.

## Related

- [Anthropic Claude API Skills - Official Claude API](/hermes/skills/catalog/anthropics-claude-api-skills-setup)
- [Claude Office Skills Suite - Business Document Skills](/hermes/skills/catalog/claude-office-skills-suite-setup)
- [skill-creator - Anthropic's Skill Creation Framework](/hermes/skills/catalog/skill-creator-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Read a skill's SKILL.md before installing the whole plugin: two frontmatter fields (name and description) define what it does, and the body is the instructions Claude follows.
- Prefer the plugin install on Claude Code, since the marketplace manifest updates through the plugin system; the example skills are already live on paid Claude.ai plans.
- Treat the document skills (docx, pdf, pptx and xlsx) as the pattern for skills that ship executable tooling, not just instructions: each carries scripts and validators under `scripts/office/`.
- Use `template/SKILL.md` as your starting point for a new skill, and `spec/agent-skills-spec.md` as the standard to conform to.
- Because two document skills carry Snyk failures, re-check the skills.sh security pages before pulling the suite into a production profile.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
