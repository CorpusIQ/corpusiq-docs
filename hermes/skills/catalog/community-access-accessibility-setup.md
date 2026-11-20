---
title: "Accessibility Agents - WCAG 2.2 AA Review Suite Setup"
description: "community-access/accessibility-agents: WCAG 2.2 AA accessibility review for coding agents - 113 skills, edit gate, scanners - 7.9K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/community-access-accessibility-setup/"
robots: "index,follow"
last_updated: "2026-11-20"
tags: ["hermes skill", "agent skill", "skill setup", "accessibility", "WCAG", "a11y"]
---

# Accessibility Agents - Setup Guide

**Source:** [community-access/accessibility-agents](https://www.skills.sh/community-access/accessibility-agents) via skills.sh - 7.9K combined installs across 96 indexed listings; first seen Nov 20, 2026 (Nov 20, 2026 morning sweep)
**GitHub:** [Community-Access/accessibility-agents](https://github.com/Community-Access/accessibility-agents) - 451 stars, MIT licence, main branch, last pushed Nov 16, 2026. 113 skills under `skills/<name>/SKILL.md`, dispatched by six entry-point skills (746 files in the tree).
**Category:** Web Accessibility
**Quality Tier:** 🟡 Yellow - 5 Warn among 20 sampled verdicts (all Snyk: playwright-testing, web-scanning, github-a11y-scanner, github-scanning, github-analytics-scoring); MIT licence.

Accessibility Agents packages WCAG 2.2 AA enforcement for agentic coding as a set of Agent Skills, read natively by Claude Code, Codex, GitHub Copilot, Gemini CLI, Antigravity and ChatGPT with no per-client copies. Six entry-point skills (accessibility-lead, web-accessibility-wizard, document-accessibility-wizard, markdown-a11y-assistant, developer-hub and github-hub) dispatch a further 107 specialist, helper and reference skills by name, which keeps the whole package at about 1,100 tokens before the model says anything.

The 96 skills.sh listings reflect the marketplace API cap, so the listing count and the 7.9K combined-install figure are floors rather than exact totals. The repository tree documents 113 skills, and the high-install listing names map to knowledge-domain reference skills under `skills/kb-<name>/SKILL.md` (for example, design-system lives at `skills/kb-design-system/` and playwright-testing at `skills/kb-playwright-testing/`).

## Installation

Install as a plugin (on Gemini CLI, an extension), which loads the skills, the hooks and the MCP server registration:

```text
Claude Code   /plugin marketplace add Community-Access/accessibility-agents
              /plugin install accessibility-agents@community-access
Copilot CLI   copilot plugin marketplace add Community-Access/accessibility-agents
              copilot plugin install accessibility-agents@community-access
Codex         codex plugin marketplace add Community-Access/accessibility-agents
              codex plugin add accessibility-agents@community-access
Gemini CLI    gemini extensions install https://github.com/Community-Access/accessibility-agents
```

On Codex the plugin loads the skills and the MCP server only (Codex no longer loads plugin hooks), so run `npm run setup` there to add the edit gate. Directly from a checkout, for Antigravity or any client without the plugin:

```bash
npm install
npm run setup
```

`npm run setup` copies the skills to `~/.agents/skills` and writes the hook manifest where the client is present. The installer never overwrites a hooks file or a skill you have edited; run it with the `--dry-run` flag first to print every action without applying it. For the optional scanners, run `npm install --prefix mcp-server`, then `npx playwright install chromium` in `mcp-server/`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| mobile-accessibility | 412 | Mobile audits: React Native, Expo, iOS and Android labels, roles and touch targets |
| playwright-testing | 316 | Playwright browser testing and behavioural scans |
| cognitive-accessibility | 278 | Cognitive accessibility: plain language, WCAG 2.2 cognitive criteria, COGA guidance and auth UX |
| design-system | 257 | Design-system accessibility: framework token paths and component patterns |
| accessibility-rules | 243 | Accessibility rules reference: the criteria each finding cites |
| lighthouse-scanner | 232 | Lighthouse accessibility scanning integration |
| framework-accessibility | 221 | Framework-specific accessibility patterns across web frameworks |
| report-generation | 216 | Report rendering: score computation and delta against the previous run |
| web-scanning | 213 | Web UI scanning across ARIA, keyboard, focus, forms and contrast |
| testing-strategy | 213 | Testing strategy for accessibility checks |
| markdown-accessibility | 209 | Markdown audits: link text, alt text, heading order, tables, emoji and diagrams |
| web-severity-scoring | 206 | Severity scoring for web accessibility findings |
| github-a11y-scanner | 205 | GitHub repository accessibility scanning |
| ci-integration | 204 | CI integration: run the accessibility gates in a pipeline |
| github-scanning | 201 | GitHub issue and pull request scanning |
| document-scanning | 201 | Document scanning: Office, PDF and ePub files |
| github-analytics-scoring | 199 | GitHub accessibility analytics and scoring |
| office-remediation | 196 | Office document remediation scripts |
| data-visualization-accessibility | 177 | Charts, graphs and dashboards: SVG ARIA, table alternatives, safe palettes |
| email-accessibility | 170 | HTML email accessibility under email client rendering constraints |
| media-accessibility | 164 | Media accessibility for audio and video content |

The remaining 75 indexed listings range from 34 to 132 installs (python-development 132; help-url-reference 130; github-workflow-standards 129; legal-compliance-mapping 127; severity-mapping 77; accessibility-lead 46; the rest at 34 to 45).

## Why This Matters for Hermes Agents

Models forget accessibility while generating code. Accessibility Agents makes that harder by routing the work to a specialist, blocking edits to user-facing files until the accessibility lead has reviewed, and rendering audit reports from structured findings instead of memory. For a Hermes agent, accessibility is enforced by the package rather than left to the model's recall of WCAG 2.2 AA, which drifts. The six entry points keep context cost low: the package sits around 1,100 tokens until a router names a specialist. The scanners run locally with no telemetry, no account and no key, so audit data stays on the machine. The edit gate is the piece that most changes behaviour: a write to a user-facing file is refused until the review completes, on every client that supports hooks.

## Usage

| You say | What happens |
|---|---|
| Audit this React app for accessibility issues | accessibility-lead reviews the web UI across ARIA, keyboard, focus, forms, contrast and modals |
| Check these Word, Excel and PDF documents | document-accessibility-wizard scans the Office, PDF and ePub files and generates remediation scripts |
| Review this markdown README for accessibility | markdown-a11y-assistant audits link text, alt text, heading order, tables, emoji and diagrams |
| Stop me from shipping inaccessible UI | the edit gate hook refuses writes to user-facing files until the accessibility lead completes |
| Give me an accessibility report with a score | findings are collected as JSON, a script renders the report and shows the delta against the previous run |
| Run the accessibility checks in CI | ci-integration wires the gates into a pipeline and the verify gates run on the change |

## Verification

```bash
# after a checkout install, confirm the skills landed
ls ~/.agents/skills/
# review one entry-point skill before relying on it
curl -sL https://raw.githubusercontent.com/community-access/accessibility-agents/main/skills/accessibility-lead/SKILL.md
# run the repo's own sixteen verification gates
npm run verify
```

The raw SKILL.md URL above was probed Nov 20, 2026 and returned HTTP 200.

## Security

skills.sh verdicts for sampled skills (verified Nov 20, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| mobile-accessibility | Pass | Pass | Pass |
| playwright-testing | Pass | Pass | Warn |
| cognitive-accessibility | Pass | Pass | Pass |
| design-system | Pass | Pass | Pass |
| accessibility-rules | Pass | Pass | Pass |
| lighthouse-scanner | Pass | Pass | Pass |
| framework-accessibility | Pass | Pass | Pass |
| report-generation | Pass | Pass | Pass |
| web-scanning | Pass | Pass | Warn |
| testing-strategy | Pass | Pass | Pass |
| markdown-accessibility | Pass | Pass | Pass |
| web-severity-scoring | Pass | Pass | Pass |
| github-a11y-scanner | Pass | Pass | Warn |
| ci-integration | Pass | Pass | Pass |
| github-scanning | Pass | Pass | Warn |
| document-scanning | Pass | Pass | Pass |
| github-analytics-scoring | Pass | Pass | Warn |
| office-remediation | Pass | Pass | Pass |
| data-visualization-accessibility | Pass | Pass | Pass |
| email-accessibility | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 20, 2026: 7,868 combined installs across 96 indexed listings; 451 GitHub stars; MIT licence; last pushed Nov 16, 2026. Counts drift over time.
- The 96-listing count is the skills.sh API cap, so the listing count and the combined-install figure are floors rather than exact totals; the tree documents 113 skills.
- Only 20 of 96 listings carry skills.sh verdicts; the other 76 are unverified on that platform.
- Many high-install listing names are knowledge-domain reference skills: the indexed name maps to `skills/kb-<name>/SKILL.md` (for example, design-system is `skills/kb-design-system/` and playwright-testing is `skills/kb-playwright-testing/`).
- The optional scanners (Playwright, @axe-core/playwright, pdf-lib and the veraPDF CLI) are not bundled; the MCP server bundle itself needs no npm install.

## Related

- [AccessLint Skills - WCAG 2.2 Accessibility Audit Suite Setup](/hermes/skills/catalog/accesslint-skills-setup)
- [UX UI Agent Skills - Design Gates for Coding Agents](/hermes/skills/catalog/ux-ui-agent-skills-setup)
- [Frontend Design Skills - UI Composition and UX Review](/hermes/skills/catalog/hueyexe-frontend-agent-skills-setup)
- [design-review - Visual UI Audit & Fix Setup](/hermes/skills/catalog/design-review-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start from one of the six entry points rather than loading specialists directly; the routers keep the whole package near 1,100 tokens.
- Run `npm run verify` after any local edit to a SKILL.md; the sixteen gates each name the standard they check.
- Use `npm run measure`, `npm run measure:dispatch` and `npm run probe:mcp` to inspect per-client token cost and the 39-tool MCP surface before wiring automation.
- Install the optional scanners only when a tool asks for them: Playwright and @axe-core/playwright for browser scans, pdf-lib for PDF form conversion, the veraPDF CLI for PDF checks.
- On Codex, use `npm run setup` to add the edit gate, since Codex no longer loads plugin hooks.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
