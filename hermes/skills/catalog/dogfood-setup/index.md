---
title: Dogfood - Setup Guide for Hermes Agents
description: "Systematic exploratory QA testing of web applications using browser tools. 5-phase workflow for finding bugs, capturing evidence, and producing structured."

canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/dogfood-setup/"
robots: "index,follow"
last_updated: "2026-11-27"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Dogfood - Setup Guide

**Source:** [nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent) (Official)
**Skill:** `dogfood` · **Installs:** 4.9K+ · **Category:** QA / Testing
**Platform:** Linux, macOS, Windows

Dogfood is Nous Research's official skill for systematic exploratory QA testing of web applications. It guides Hermes agents through a structured 5-phase workflow - Plan, Explore, Interact, Edge Cases, Report - using the browser toolset to find bugs, capture screenshots as evidence, and produce structured bug reports.

## Installation

```bash
npx skills add nousresearch/hermes-agent@dogfood
```

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Hermes Agent | Latest version with the browser tool (`browser_exec`) |
| Browser tool | `browser_exec` - the built-in `browser_*` tools were removed in v0.23.0, see [Upgrading Hermes](/hermes/setup/upgrading) |
| Target URL | The web application to test |
| Testing scope | Features/areas to focus on (or "full site") |

## Workflow

> Browser automation runs through `browser_exec`. Each call is Python, and the helpers (`new_tab`, `goto_url`, `page_info`, `js`, `fill_input`, `click_at_xy`, `capture_screenshot`, `cdp`) are pre-imported, so one call can drive a whole page.

### Phase 1: Plan

1. Create output directory: `dogfood-output/screenshots/`
2. Identify testing scope from user input
3. Build a sitemap - pages, features, flows to test:
   - Landing/home page
   - Navigation (header, footer, sidebar)
   - Key user flows (sign up, login, search, checkout)
   - Forms and interactive elements
   - Edge cases (empty states, error pages, 404s)

### Phase 2: Explore

For each page in your plan:

1. **Navigate**: `new_tab("https://example.com/page")`, then `wait_for_load()`
2. **Read the page**: `page_info()` for the title and state, `js("document.body.innerText.slice(0, 2000)")` for the text
3. **Console check**: run the interaction inside `js("...")` and read what the page records, or inspect the browser protocol through `cdp("Runtime.evaluate", expression="...")`. Silent JS errors are high-value findings.
4. **Visual assessment**: `capture_screenshot()` returns a file path, then load that path with the vision tool to describe layout, broken elements and accessibility concerns

### Phase 3: Interact

For each interactive element identified:

1. Click buttons/links: `js("document.querySelector('selector').click()")`, or `click_at_xy(x, y)` for a coordinate
2. Fill forms: `fill_input(selector, "test input")`
3. Re-read the page and re-check for JS errors after each interaction
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

- [Agent Browser Setup](/hermes/skills/catalog/agent-browser-setup)
- [Browser Use Automation](/hermes/skills/catalog/browser-use-automation-setup)
- [Browser Act Setup](/hermes/skills/catalog/browser-act-setup)
