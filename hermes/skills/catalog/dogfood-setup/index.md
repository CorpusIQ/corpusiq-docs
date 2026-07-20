---
title: Dogfood — Systematic Web App QA Testing for Hermes Agents
description: Official Nous Research skill for systematic exploratory QA testing using Hermes browser tools. 5-phase methodology: Plan → Explore → Collect Evidence → Categorize → Report. 4,700+ installs.
---

# Dogfood — Setup Guide

**Source:** [nousresearch/hermes-agent](https://github.com/NousResearch/hermes-agent) (Official)
**Skill:** `dogfood` · **Installs:** 4,700+ · **Category:** QA / Testing
**Platform:** Linux, macOS, Windows

Systematic exploratory QA testing of web applications using Hermes' built-in browser toolset. Navigate, interact, capture evidence, and produce structured bug reports — all from agent conversations.

---

## Installation

```bash
# Install via skills.sh
npx skills add nousresearch/hermes-agent --skill dogfood -g -y

# Or clone the full repo
git clone https://github.com/NousResearch/hermes-agent.git
# Skill is at: hermes-agent/skills/dogfood/SKILL.md
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | v0.16.0+ with browser toolset enabled |
| **Browser Tools** | `browser_navigate`, `browser_snapshot`, `browser_click`, `browser_type`, `browser_vision`, `browser_console`, `browser_scroll`, `browser_back`, `browser_press` |
| **Target URL** | The web application to test |

---

## The 5-Phase Workflow

Dogfood provides a systematic 5-phase methodology for exploratory QA:

### Phase 1: Plan

Create the output directory structure and build a testing sitemap:

```
{output_dir}/
├── screenshots/       # Evidence screenshots
└── report.md          # Final report
```

Identify testing scope:
- Landing/home page
- Navigation (header, footer, sidebar)
- Key user flows (sign up, login, search, checkout)
- Forms and interactive elements
- Edge cases (empty states, error pages, 404s)

### Phase 2: Explore

For each page or feature:

1. **Navigate**: `browser_navigate(url="https://example.com/page")`
2. **Snapshot DOM**: `browser_snapshot()`
3. **Check console**: `browser_console(clear=true)` — silent JS errors are high-value
4. **Annotated screenshot**: `browser_vision(question="Describe the page layout, identify visual issues", annotate=true)`
5. **Test interactions**: Click buttons, fill forms, test keyboard nav, scroll content
6. **After each interaction**: Check console + visual changes

### Phase 3: Collect Evidence

For every issue found:
- Screenshot the issue: `browser_vision(question="Capture the issue", annotate=false)`
- Record: URL, steps to reproduce, expected vs actual behavior, console errors
- Classify: Severity (Critical/High/Medium/Low), Category (Functional/Visual/Accessibility/Console/UX/Content)

### Phase 4: Categorize

- Review all collected issues
- De-duplicate — merge same bugs in different places
- Assign final severity and category
- Sort by severity (Critical first)

### Phase 5: Report

Generate structured bug report with:
- Executive summary (totals, breakdown by severity)
- Per-issue sections (severity badge, URL, repro steps, expected/actual, screenshots)
- Summary table of all issues
- Testing notes (what was tested, what wasn't, blockers)

---

## Tools Reference

| Tool | Purpose |
|------|---------|
| `browser_navigate` | Navigate to URL |
| `browser_snapshot` | DOM accessibility tree snapshot |
| `browser_click` | Click element by ref (`@eN`) |
| `browser_type` | Type into input field |
| `browser_scroll` | Scroll page up/down |
| `browser_back` | Go back in history |
| `browser_press` | Press keyboard key |
| `browser_vision` | Screenshot + AI analysis; `annotate=true` for element labels |
| `browser_console` | JS console output and errors |

---

## Best Practices

- **Always check `browser_console()` after navigation and interactions** — silent JS errors are the most valuable findings
- **Use `annotate=true` with `browser_vision`** for reasoning about interactive element positions
- **Test with valid AND invalid inputs** — form validation bugs are common
- **Scroll through long pages** — content below the fold may have rendering issues
- **Test navigation flows end-to-end** — multi-step processes often break
- **Check edge cases**: empty states, very long text, special characters, rapid clicking
- **Use `MEDIA:<screenshot_path>`** in reports to embed evidence inline

---

## Example Usage

```
User: "Dogfood https://corpusiq.io — focus on the signup flow and pricing page"

Agent:
1. Creates output directory structure
2. Navigates to corpusiq.io, takes snapshot, checks console
3. Tests signup flow: fills form, submits, validates redirect
4. Tests pricing page: checks all plans visible, toggle works, CTA buttons
5. Collects evidence for any issues found
6. Generates structured report with severity-classified findings

Output: dogfood-output/report.md with screenshot evidence
```

---

## Related Skills

- [Agent Browser Setup Guide](/hermes/skills/catalog/agent-browser-setup/) — Vercel Labs browser automation
- [Browser Act Setup Guide](/hermes/skills/catalog/browser-act-setup/) — Browser-based action execution
