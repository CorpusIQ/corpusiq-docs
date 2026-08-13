---
title: Addy Osmani — Production-Grade Agent Skills for Hermes
description: 20 engineering skills from Google Chrome's Addy Osmani covering CI/CD, code review, performance optimization, security hardening, debugging, test-driven development, and shipping best practices. 80.5K GitHub stars, 14.1K+ installs.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/addyosmani-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Addy Osmani — Agent Skills Setup Guide

**Source:** [addyosmani/agent-skills](https://skills.sh/addyosmani/agent-skills) (14.1K+ combined installs)
**GitHub:** [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) (80,523 ⭐)
**Category:** Developer Tools / Engineering
**Quality Tier:** 🟢 Production

Production-grade engineering skills for AI coding agents, authored by Addy Osmani (Google Chrome Engineering Lead, author of "Learning JavaScript Design Patterns"). These 20 skills encode battle-tested engineering practices — CI/CD automation, security hardening, performance optimization, code review, debugging, test-driven development, and shipping workflows — proven across real-world production systems.

---

## Installation

```bash
# Install the core engineering skills:
npx skills add addyosmani/agent-skills --skill ci-cd-and-automation
npx skills add addyosmani/agent-skills --skill code-review-and-quality
npx skills add addyosmani/agent-skills --skill security-and-hardening
npx skills add addyosmani/agent-skills --skill performance-optimization
npx skills add addyosmani/agent-skills --skill debugging-and-error-recovery
npx skills add addyosmani/agent-skills --skill test-driven-development
npx skills add addyosmani/agent-skills --skill shipping-and-launch

# Install additional skills as needed:
npx skills add addyosmani/agent-skills --skill api-and-interface-design
npx skills add addyosmani/agent-skills --skill planning-and-task-breakdown
npx skills add addyosmani/agent-skills --skill observability-and-instrumentation
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **ci-cd-and-automation** | 14.1K | Automate CI/CD pipelines, GitHub Actions, deployment workflows |
| **api-and-interface-design** | — | Design RESTful APIs, GraphQL schemas, and interfaces |
| **browser-testing-with-devtools** | — | End-to-end browser testing with Chrome DevTools |
| **code-review-and-quality** | — | Conduct thorough code reviews with quality gates |
| **code-simplification** | — | Simplify complex code, reduce technical debt |
| **context-engineering** | — | Optimize context windows and prompt engineering for agents |
| **debugging-and-error-recovery** | — | Systematic debugging and error recovery patterns |
| **idea-refine** | — | Refine and validate product/feature ideas |
| **incremental-implementation** | — | Implement features incrementally with safe rollouts |
| **interview-me** | — | Conduct technical interview practice sessions |
| **observability-and-instrumentation** | — | Add logging, metrics, tracing to production systems |
| **performance-optimization** | — | Profile and optimize web app performance (Core Web Vitals) |
| **planning-and-task-breakdown** | — | Break down complex features into implementable tasks |
| **security-and-hardening** | — | Security audit, vulnerability scanning, hardening |
| **shipping-and-launch** | — | Production launch checklists, rollback plans, monitoring |
| **source-driven-development** | — | Read and understand existing codebases before modifying |
| **spec-driven-development** | — | Write specifications before implementation |
| **test-driven-development** | — | TDD workflow: red-green-refactor cycles |
| **using-agent-skills** | — | Meta-skill for effectively using and composing agent skills |

---

## Key Capabilities

### CI/CD & Automation (ci-cd-and-automation)
The flagship skill at 14.1K installs. Automates GitHub Actions workflow creation, deployment pipeline configuration, artifact management, and release automation. Handles multi-environment deployments with approval gates and rollback strategies.

### Code Quality & Review
- **code-review-and-quality**: Automated code review with style, security, and performance checks
- **code-simplification**: Identifies over-engineered code and proposes simpler alternatives
- **source-driven-development**: Reads and analyzes existing code before making changes — prevents breaking patterns

### Performance & Observability
- **performance-optimization**: Core Web Vitals optimization, bundle analysis, render performance
- **observability-and-instrumentation**: OpenTelemetry integration, structured logging, custom metrics
- **browser-testing-with-devtools**: Performance profiling, memory leak detection, network waterfall analysis

### Security & Launch
- **security-and-hardening**: Dependency scanning, secret detection, OWASP Top 10 mitigation
- **shipping-and-launch**: Production readiness checklist, feature flags, canary deployments
- **test-driven-development**: Red-green-refactor with Jest, Vitest, and Playwright

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js** | 18+ |
| **GitHub CLI** | For ci-cd-and-automation (Actions workflows) |
| **Chrome/Chromium** | For browser-testing-with-devtools |
| **Docker** | Optional — for isolated test environments |

---

## Quick Start

```bash
# 1. Install the most-used skill
npx skills add addyosmani/agent-skills --skill ci-cd-and-automation

# 2. Trigger in Hermes — the skill loads when its conditions match
# Example: "Set up a CI/CD pipeline for this repo" triggers ci-cd-and-automation
# Example: "Review this PR for security issues" triggers security-and-hardening

# 3. Verify installation
npx skills list | grep addyosmani
```

---

## Verification

```bash
# Check installed skills
npx skills list | grep "ci-cd-and-automation"

# Test — ask Hermes a relevant engineering question
# "Create a GitHub Actions workflow that runs tests and deploys to staging"
```

---

## Notes

- Authored by **Addy Osmani**, Google Chrome Engineering Lead — these skills encode production patterns used at Google scale
- The **ci-cd-and-automation** skill is the most popular (14.1K installs) and the primary entry point
- Skills are designed to compose together — e.g., combine `test-driven-development` → `code-review-and-quality` → `ci-cd-and-automation` for a complete quality pipeline
- **context-engineering** is particularly relevant for Hermes agents — it teaches agents to manage their own context windows efficiently
- These skills complement the existing `security-and-hardening-setup` and `ci-cd` catalog entries but add Addy's specific production-grade patterns
- GitHub topics include: `agent-skills`, `antigravity`, `claude-code`, `codex`, `cursor` — indicating multi-agent compatibility
