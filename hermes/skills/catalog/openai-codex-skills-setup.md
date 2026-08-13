---
title: OpenAI Codex Skills — Official Skills Catalog for AI Coding Agents
description: OpenAI's official skills catalog for Codex CLI — PDF generation, CI/CD fixes, security auditing, Playwright testing, and Figma design implementation. 38K+ combined installs.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/openai-codex-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# OpenAI Codex Skills — Setup Guide

**Source:** [openai/skills](https://skills.sh/openai/skills) (38K+ combined installs)
**GitHub:** [openai/skills](https://github.com/openai/skills) (24K+ ⭐)
**Category:** Agent Infrastructure / Coding Agents
**Quality Tier:** 🟢 Production

OpenAI's official skills catalog for Codex CLI — their agentic coding tool. These skills extend Codex with PDF generation, GitHub CI/CD automation, security best practices, Linear issue tracking integration, Playwright browser testing, and Figma-to-code design implementation. For Hermes agents that use Codex as an implementation backend, these skills add production-ready capabilities.

---

## Installation

```bash
# Document generation
npx skills add openai/skills --skill pdf

# CI/CD + GitHub automation
npx skills add openai/skills --skill gh-fix-ci

# Security
npx skills add openai/skills --skill security-best-practices

# Issue tracking + testing
npx skills add openai/skills --skill linear
npx skills add openai/skills --skill playwright

# Design implementation
npx skills add openai/skills --skill figma-implement-design
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **pdf** | 10.4K | Generate, parse, and manipulate PDF documents programmatically |
| **gh-fix-ci** | 7.8K | Diagnose and fix GitHub Actions CI/CD pipeline failures |
| **security-best-practices** | 5.7K | Security audit workflows — dependency scanning, secret detection, OWASP patterns |
| **linear** | 5.2K | Linear issue tracking integration — create, update, and query issues |
| **playwright** | 4.7K | Browser automation testing with Playwright — E2E tests, visual regression |
| **figma-implement-design** | 4.4K | Convert Figma designs to production code with component matching |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Codex CLI** | `npm install -g @openai/codex` (or `npx @openai/codex`) |
| **OpenAI API key** | Required for Codex agent usage |
| **Node.js 18+** | Required for Codex runtime |

---

## Key Capabilities

### Document Generation (pdf)
Generate professional PDF reports, invoices, and documentation directly from code. Supports PDF parsing for data extraction and template-based generation.

### CI/CD Automation (gh-fix-ci)
Intelligently diagnose GitHub Actions failures by reading workflow logs, identifying root causes, and proposing fixes. Handles common failure patterns: dependency resolution, environment variables, artifact uploads.

### Security Auditing (security-best-practices)
Automated security review workflows covering OWASP Top 10, dependency vulnerability scanning (npm audit, pip audit), secret detection, and secure coding patterns.

### Browser Testing (playwright)
Write and execute Playwright tests for web applications. Includes visual regression testing, accessibility audits, and multi-browser coverage.

### Design-to-Code (figma-implement-design)
Parse Figma design files and generate matching React/Vue components with accurate styling, spacing, and responsive breakpoints.

---

## Quick Start

```bash
# 1. Install Codex CLI
npm install -g @openai/codex

# 2. Add the CI fix skill
npx skills add openai/skills --skill gh-fix-ci

# 3. Fix a broken CI pipeline
codex "Using the gh-fix-ci skill, diagnose why the main branch CI is failing"

# 4. Generate a PDF report
npx skills add openai/skills --skill pdf
codex "Using the pdf skill, generate a sprint review report from the last week of commits"
```

---

## Verification

```bash
# Check installed OpenAI skills
npx skills list | grep openai/skills

# Verify Codex can use them
codex "list available skills" 2>&1 | grep -i openai
```

---

## Notes

- These are the Codex-equivalent of Anthropic's Claude Code skills — both extend their respective agentic coding tools
- The `gh-fix-ci` skill is particularly valuable for Hermes agents managing GitHub Actions across multiple repos
- `figma-implement-design` requires Figma API access token for private design files
- For Hermes agents using Codex as an implementation backend, add the full skill set to unlock PDF, CI, security, and testing capabilities
- Distinct from `anthropics/claude-code` skills — both catalogs serve the same purpose (agent extensibility) but for different agent runtimes
