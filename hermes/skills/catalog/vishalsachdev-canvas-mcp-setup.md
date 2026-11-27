---
title: "Canvas LMS MCP - Teaching Operations Skills Setup"
description: "vishalsachdev/canvas-mcp - 2.0K combined installs: Canvas LMS MCP server and 8 classroom workflow skills for students and educators."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/vishalsachdev-canvas-mcp-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "canvas lms", "education", "teaching"]
---

# Canvas LMS MCP - Setup Guide

**Source:** [vishalsachdev/canvas-mcp](https://www.skills.sh/vishalsachdev/canvas-mcp) via skills.sh - 2.0K combined installs across 10 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 evening sweep)
**GitHub:** [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) - 340 stars, MIT license, last pushed Nov 27, 2026, main branch; 8 workflow skills under skills/<name>/SKILL.md alongside the MCP server source.
**Category:** Canvas LMS Teaching Operations (Education)
**Quality Tier:** 🟡 Yellow - 10 of 10 listings sampled: five pass all three checks, and five carry a single Snyk Warn each.

vishalsachdev/canvas-mcp is the Canvas MCP Server, a Model Context Protocol server for Canvas LMS, the learning management system used by schools and universities. Canvas here means the LMS, not a design canvas. The server exposes role-specific tools for students, educators, learning designers, and developers, and ships eight classroom workflow skills alongside them.

The MCP server is the integration surface: it calls Canvas on the caller's own Canvas API token, so a valid Canvas API token and institution URL are required before any tool or skill will work. The eight skills are multi-step classroom workflows layered on top of those tools, covering weekly planning, bulk grading, peer review, discussion facilitation, course building, course quality checks, morning course health checks, and accessibility auditing.

## Installation

Install the MCP server first - the skills call its tools, so a skill without the server has nothing to run. For Claude Desktop, download canvas-mcp.mcpb from the latest release and double-click it; it prompts for the Canvas API URL and token. For Cursor, Codex, Zed, Windsurf, and other clients, install from source into a virtualenv:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -e .
cp env.template .env
# set CANVAS_API_TOKEN and CANVAS_API_URL in .env
```

Verify the connection with `canvas-mcp-server --test`, then add the workflow skills:

```bash
npx skills add vishalsachdev/canvas-mcp
```

Install a single skill with `npx skills add vishalsachdev/canvas-mcp -s canvas-week-plan`. The same workflows are also available as Claude Code slash commands.

## What It Provides

skills.sh publishes per-skill install counts for all 10 indexed listings. The eight most-installed skills are listed below; the remaining two are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| canvas-week-plan | 334 | student weekly planner: due dates, submission status, grades, and peer reviews across courses |
| canvas-discussion-facilitator | 244 | browse, read, reply to, and create discussion posts for students and educators |
| canvas-morning-check | 239 | educator morning health check: submission rates, struggling students, grades, deadlines |
| canvas-bulk-grading | 232 | grade an assignment, apply a rubric, bulk grade, or dry-run grades before posting |
| canvas-peer-review-manager | 229 | track peer review completion, analyze comment quality, send reminders, build reports |
| canvas-course-builder | 226 | scaffold course modules, pages, assignments, and discussions from specs or templates |
| canvas-course-qc | 221 | pre-semester quality audit: structure, content, publishing, dates, rubric coverage |
| canvas-accessibility-auditor | 219 | WCAG-oriented accessibility scan, prioritized report, guided fixes, verification |

The remaining 2 indexed listings range from 44 to 62 installs.

## Why This Matters for Hermes Agents

Canvas MCP packages a full teaching-operations surface as a single MCP server plus eight focused workflows, so an education-focused agent gets role-aware tooling without assembling Canvas API calls by hand. The server is the integration point: it talks to Canvas through the caller's own API token, which keeps permissions aligned with the account running it rather than a shared credential. The eight skills encode multi-step classroom recipes - weekly planning, morning course health checks, bulk grading, peer review management, discussion facilitation, course scaffolding, course QC, and accessibility auditing - so an agent can run a semester-start course build or a mid-semester grading pass as a repeatable procedure instead of a fresh prompt each time. The accessibility auditor and course QC skills target learning designers and map directly to WCAG-oriented and pre-semester readiness checks, work that is otherwise slow and error-prone to do by hand. The repository is actively maintained, with a large test suite and security-focused release notes, which matters for agents that will operate on student data in production.

## Usage

| You say | What happens |
|---|---|
| Plan my week | Runs canvas-week-plan to list due dates, submission status, grades, and peer reviews |
| Grade everyone who submitted Assignment 3 | Runs canvas-bulk-grading for rubric-based or dry-run grading of submissions |
| How are my students doing this morning | Runs canvas-morning-check for submission rates, struggling students, and deadlines |
| Who has not reviewed yet | Runs canvas-peer-review-manager for completion tracking, reminders, and reports |
| Scaffold a new course from this spec | Runs canvas-course-builder to create modules, pages, assignments, and discussions |
| Is this course ready for the semester | Runs canvas-course-qc for structure, content, publishing, and rubric coverage |
| Audit this course for accessibility | Runs canvas-accessibility-auditor for a WCAG-oriented scan and remediation plan |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/vishalsachdev/canvas-mcp/main/README.md | head -60
curl -sL https://raw.githubusercontent.com/vishalsachdev/canvas-mcp/main/skills/canvas-week-plan/SKILL.md | head -40
```

Both URLs return 200. After installing, run `canvas-mcp-server --test` to confirm the Canvas connection, review each skills/<name>/SKILL.md before relying on it, and re-check the security pages on skills.sh for the Warn verdicts noted below.

## Security

skills.sh verdicts for sampled skills (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| canvas-week-plan | Pass | Pass | Pass |
| canvas-discussion-facilitator | Pass | Pass | Warn |
| canvas-morning-check | Pass | Pass | Warn |
| canvas-bulk-grading | Pass | Pass | Warn |
| canvas-peer-review-manager | Pass | Pass | Warn |
| canvas-course-builder | Pass | Pass | Pass |
| canvas-course-qc | Pass | Pass | Warn |
| canvas-accessibility-auditor | Pass | Pass | Pass |
| week-plan | Pass | Pass | Pass |
| morning-check | Pass | Pass | Pass |

Across the 10 sampled skills there are 25 Pass, 5 Warn, and 0 Fail cells. Five skills pass all three checks; five carry a single Snyk Warn each (discussion facilitator, morning check, bulk grading, peer review manager, course QC).

## Limitations

- Snapshot data, verified Nov 26, 2026: 2,050 combined installs across 10 indexed listings; 340 GitHub stars; MIT license; last pushed Nov 27, 2026. Counts drift over time.
- The install index carries two near-duplicate names - week-plan (62) and morning-check (44) - with no matching directory in the current skills/ tree; the tree ships only the eight canvas-prefixed skills.
- The MCP server is the integration surface: every skill depends on the server running with a valid Canvas API token and institution URL, so no skill functions standalone.
- Local servers default to read-only since v1.19.0; editing, grading, and messaging require enabling specific write tools via ALLOWED_WRITE_TOOLS or the extension's allowed-write-tools setting.
- The public hosted server (mcp.illinihunt.org) has been retired; the supported path is local installation or self-hosting behind your own authentication.
- Five of the ten sampled skills carry a single Snyk Warn; re-check the security pages before production use.

## Related

[Education Agent Skills - 165 Teaching Skills](/hermes/skills/catalog/education-agent-skills-setup) | [AI Engineering from Scratch - Course Tutor Skills Setup](/hermes/skills/catalog/ai-engineering-from-scratch-setup) | [AI Native Camp 1 - Korean Claude Code Curriculum](/hermes/skills/catalog/ai-native-camp-bootcamp-setup) | [Build Mcp Server Setup](/hermes/skills/catalog/build-mcp-server-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the server first and verify with `canvas-mcp-server --test` before adding any skill; a skill without the server has nothing to run.
- Start with canvas-week-plan or canvas-morning-check to confirm the token scope before enabling any write tool.
- Enable only the specific write tools you use (for example edit_page_content) instead of a broad allowlist.
- Run canvas-course-qc and canvas-accessibility-auditor together for a pre-semester learning-designer pass.
- Fetch a skill's SKILL.md from the main branch to review its workflow before installing.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
