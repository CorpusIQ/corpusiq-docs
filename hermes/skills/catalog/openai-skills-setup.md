---
title: OpenAI Skills — Official OpenAI Agent Skills for Hermes Agents
description: Production-grade PDF manipulation, CI debugging, security auditing, Linear integration, Playwright testing, and Figma implementation from OpenAI. 703K+ combined installs across 6 skills.
---

# OpenAI Skills — Setup Guide

**Source:** [openai/skills](https://skills.sh/openai/skills) (703K+ combined installs)
**Category:** Development / Security / Design
**Quality Tier:** 🟢 Production

Official skills published by OpenAI for use with Claude Code and compatible agents (including Hermes). These are production-grade, well-maintained workflows covering PDF generation, CI debugging, security auditing, project management (Linear), browser testing (Playwright), and design implementation (Figma).

---

## Installation

```bash
npx skills add openai/skills --skill pdf
npx skills add openai/skills --skill gh-fix-ci
npx skills add openai/skills --skill security-best-practices
npx skills add openai/skills --skill linear
npx skills add openai/skills --skill playwright
npx skills add openai/skills --skill figma-implement-design
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **pdf** | 10.5K | Read, create, and review PDFs with rendering and layout verification |
| **gh-fix-ci** | 7.8K | Debug failing GitHub Actions PR checks using `gh` CLI |
| **security-best-practices** | 5.8K | Language/framework-specific security reviews with auto-detection |
| **linear** | 5.2K | Manage Linear issues, cycles, and projects from the CLI |
| **playwright** | 4.7K | Browser automation and end-to-end testing with Playwright |
| **figma-implement-design** | 4.4K | Convert Figma designs into production code |

---

## Key Capabilities

### pdf — PDF Manipulation
- Render PDFs to PNGs for visual inspection (`pdftoppm`)
- Generate PDFs programmatically with `reportlab`
- Extract text with `pdfplumber` and `pypdf`
- Quality-first: verify alignment, spacing, and legibility before delivery
- Dependencies: poppler-utils, reportlab, pdfplumber, pypdf

### gh-fix-ci — CI Debugging
- Inspect failing PR checks via `gh pr checks`
- Fetch GitHub Actions logs for actionable failures
- Bundled `inspect_pr_checks.py` script handles API field drift
- Creates fix plans with approval gates before implementation
- Scope: GitHub Actions only (external providers like Buildkite are out of scope)

### security-best-practices — Security Auditing
- Auto-detects language and framework from project context
- Loads reference files for Python, JavaScript/TypeScript, and Go
- Three modes: secure-by-default coding, passive vulnerability detection, full security reports
- Produces prioritized reports with severity classifications
- Supports project-specific overrides with documentation

### linear — Project Management
- Manage Linear issues, cycles, and project tracking
- CLI-driven workflow for ticket creation and status updates

### playwright — Browser Testing
- End-to-end browser automation and testing
- Cross-browser testing with Playwright's API

### figma-implement-design — Design-to-Code
- Convert Figma design files into production-ready code
- Handles component extraction, styling, and layout implementation

---

## Quick Start

```bash
# PDF generation
npx skills use openai/skills@pdf

# Debug failing CI
npx skills use openai/skills@gh-fix-ci

# Security audit
npx skills use openai/skills@security-best-practices
```

---

## Verification

```bash
npx skills list | grep "openai/skills"
# Expected: 6 skills listed with install counts
```

---

## Notes

- These are official OpenAI skills — well-maintained and updated regularly
- All skills use `npx skills add` for installation (standard marketplace workflow)
- The `security-best-practices` skill is especially valuable for Hermes agents working on production codebases
- `gh-fix-ci` includes a bundled Python script for reliable CI inspection (works around `gh` CLI field drift)
- PDF skill prefers visual verification — renders to PNG before declaring output ready
