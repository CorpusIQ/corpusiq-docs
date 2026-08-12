---
title: Dogfood — Setup Guide for Hermes Agents
description: Systematic exploratory QA testing of web applications using browser tools. 5-phase workflow for finding bugs, capturing evidence, and producing structured reports. 4.9K+ installs.
---

# Dogfood — Setup Guide

**Source:** [nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent) (Official)
**Skill:** `dogfood` · **Installs:** 4.9K+ · **Category:** QA / Testing
**Platform:** Linux, macOS, Windows

Dogfood is Nous Research's official skill for systematic exploratory QA testing of web applications. It guides Hermes agents through a structured 5-phase workflow — Plan, Explore, Interact, Edge Cases, Report — using the browser toolset to find bugs, capture screenshots as evidence, and produce structured bug reports.

## Installation

```bash
npx skills add nousresearch/hermes-agent@dogfood
```

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Hermes Agent | Latest version with browser toolset |
| Browser tools | `browser_navigate`, `browser_snapshot`, `browser_click`, `browser_type`, `browser_vision`, `browser_console`, `browser_scroll`, `browser_back`, `browser_press` |
| Target URL | The web application to test |
| Testing scope | Features/areas to focus on (or "full site") |

## Workflow

### Phase 1: Plan

1. Create output directory: `dogfood-output/screenshots/`
2. Identify testing scope from user input
3. Build a sitemap — pages, features, flows to test:
   - Landing/home page
   - Navigation (header, footer, sidebar)
   - Key user flows (sign up, login, search, checkout)
   - Forms and interactive elements
   - Edge cases (empty states, error pages, 404s)

### Phase 2: Explore

For each page in your plan:

1. **Navigate**: `browser_navigate(url="https://example.com/page")`
2. **Snapshot**: `browser_snapshot()` — understand DOM structure
3. **Console check**: `browser_console(clear=true)` — catch JS errors after every navigation and interaction. Silent JS errors are high-value findings.
4. **Visual assessment**: `browser_vision(question="Describe the page layout, identify visual issues, broken elements, or accessibility concerns", annotate=true)` — `annotate=true` overlays numbered `[N]` labels on interactive elements. Each `[N]` maps to ref `@eN`.

### Phase 3: Interact

For each interactive element identified:

1. Click buttons/links: `browser_click(ref="@eN")`
2. Fill forms: `browser_type(ref="@eN", text="test input")`
3. Check console after each interaction
4. Take screenshots of any issues

### Phase 4: Edge Cases

Test boundary conditions:

- Empty form submissions
- Invalid inputs (emails, passwords, special characters)
- Rapid double-clicks
- Browser back/forward navigation
- Mobile viewport (responsive testing)
- Network throttling / offline states
- 404 pages and error states

### Phase 5: Report

Produce a structured bug report in `dogfood-output/report.md`:

- **Summary**: Overall assessment (1-2 sentences)
- **Critical Issues**: Blockers with evidence screenshots
- **Major Issues**: Significant bugs affecting UX
- **Minor Issues**: Cosmetic or edge-case problems
- **Console Errors**: All JS errors found with page context
- **Recommendations**: Prioritized fix order

## Verification

After running, verify:
- Report exists at `dogfood-output/report.md`
- Screenshots captured for each issue
- Console errors are documented with page URLs

## Related Skills

- [Agent Browser Setup](/hermes/skills/catalog/agent-browser-setup/)
- [Browser Use Automation](/hermes/skills/catalog/browser-use-automation-setup)
- [Browser Act Setup](/hermes/skills/catalog/browser-act-setup/)
