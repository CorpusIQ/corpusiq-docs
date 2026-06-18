---
title: Development Skills
description: Software development workflows for Hermes agents — GitHub PRs, code review, CI/CD, testing, codebase inspection, and project management. 10+ production skills.
---

# Development Skills

Development skills cover the full software delivery lifecycle — from cloning a repo to shipping a merged PR with passing CI. These are the skills that turn Hermes into a capable development teammate: not just generating code, but managing branches, reviewing diffs, triaging issues, running test suites, and coordinating across multiple repositories.

## Skill Categories

### GitHub Workflows

The backbone of any development pipeline. These skills cover every GitHub interaction a developer performs daily.

**`github-pr-workflow`** — Full PR lifecycle management. Creates feature branches from issues, commits changes with conventional commit messages, opens pull requests with generated descriptions, monitors CI status, and merges when checks pass. Handles branch naming conventions (`feat/`, `fix/`, `chore/`) and automatically links PRs to issues via closing keywords.

**`github-auth`** — Authentication setup for all GitHub access methods. Configures HTTPS token-based auth, SSH key generation and registration with GitHub, and `gh` CLI authentication. Includes verification that `git push` actually works before proceeding — the most common failure point in automated Git workflows.

**`github-repo-management`** — Repository lifecycle operations. Clones repos with correct depth for automation (shallow clones save bandwidth), creates new repos with appropriate `.gitignore` and license templates, forks upstream repos for contribution workflows, and manages remote configurations for multi-repo coordination.

**`github-issues`** — Issue triage and management. Creates issues from templates, assigns labels based on content analysis, estimates effort from description complexity, and links related issues. The triage workflow: scan new issues → classify by type (bug/feature/docs) → label by component → assign to appropriate milestone → estimate effort.

### Code Review

Code review is the highest-leverage development activity. These skills enforce review discipline that catches bugs before they ship.

**`github-code-review`** — Systematic PR review with inline comments. The workflow: fetch PR diff → analyze changed files by risk (config changes > auth changes > business logic > docs) → check for common anti-patterns (missing error handling, hardcoded secrets, untested edge cases) → write inline comments with exact line references → submit review with approve/request-changes decision.

**`code-review-excellence`** (marketplace, 22K installs) — Review standards and anti-pattern detection. Covers: what to look for in each language (Python: type hints, exception handling; TypeScript: null checks, promise handling), how to write actionable review comments (state the problem, show the fix, explain the impact), and when to approve vs. request changes.

**`requesting-code-review`** (marketplace, 121K installs) — How to prepare a PR for review. Break large changes into reviewable commits, write PR descriptions that explain "what" and "why" not just "how", self-review before requesting, and respond to review feedback constructively.

### CI/CD and Testing

**`deployment-pipeline-design`** (marketplace, 9K installs) — CI/CD pipeline architecture. Designs pipelines for monorepos and multi-service architectures. Covers: build matrix strategies, cache optimization for faster CI, environment-specific deployment gates, and rollback automation.

**`webapp-testing`** (marketplace, 92K installs) — Browser-based application testing via Playwright. Writes test scenarios, handles authentication in tests, and verifies visual regressions. Integrates with CI for pre-merge testing gates.

**`python-testing-patterns`** (marketplace, 24K installs) — Python test patterns: fixture factories, parametrized tests, mock discipline (mock at the boundary, not internally), and test organization for large codebases.

**`e2e-testing-patterns`** (marketplace, 18K installs) — End-to-end test design patterns. Page object model, data seeding strategies, test isolation, and flaky test remediation.

### Codebase Inspection and Analysis

**`codebase-inspection`** — Deep codebase analysis. Uses `pygount` or similar tools to measure lines of code by language, identifies largest files and directories, calculates language ratios, and surfaces complexity hotspots. The output is a codebase health report: total LOC, language breakdown, top-10 largest files, dependency graph density, and recommendations for refactoring targets.

**`simplify-code`** — Parallel code cleanup. Spawns three sub-agents to independently analyze recent code changes, each producing a simplification proposal. The orchestrator merges non-conflicting improvements and flags conflicts for human resolution. This catches redundant abstractions, over-engineered patterns, and code that can be expressed more clearly.

### Project Management

**`kanban-worker`** — Hermes-native Kanban board operations. Manages work-in-progress limits, moves tasks between columns, and enforces completion criteria before marking items done. Integrates with Monday.com and Notion for team visibility.

**`notion-automation`** (marketplace, 2.7K installs) — Notion workspace automation. Creates and updates database entries, manages page hierarchies, and syncs development status with project tracking.

## Workflow Patterns

### The Standard PR Pipeline

The most common workflow chains multiple development skills:

1. **`github-issues`** — Create or pick up an issue, assign it to yourself
2. **`github-pr-workflow`** — Create branch, implement fix, open PR with description
3. **`github-code-review`** — Self-review the PR, check for anti-patterns
4. **`webapp-testing`** or **`python-testing-patterns`** — Run the test suite
5. **`github-pr-workflow`** — Monitor CI, merge when green

Each skill verifies its own output before handing off to the next. If CI fails at step 5, the agent loops back to step 2 with the failure context.

### Codebase Health Audit

Run this weekly to catch degradation before it compounds:

1. **`codebase-inspection`** — Generate health report (LOC trends, complexity hotspots)
2. **`simplify-code`** — Target the top-3 largest files for simplification
3. **`github-issues`** — Create refactoring issues for anything that can't be fixed immediately

## Installing Development Skills

```bash
# Native skills load automatically with Hermes
# Marketplace skills install with npx:

npx skills add obra/superpowers@requesting-code-review
npx skills add obra/superpowers@receiving-code-review
npx skills add wshobson/agents@code-review-excellence
npx skills add wshobson/agents@python-testing-patterns
npx skills add wshobson/agents@e2e-testing-patterns
npx skills add wshobson/agents@deployment-pipeline-design
npx skills add anthropics/skills@webapp-testing
npx skills add github/awesome-copilot@git-commit
npx skills add github/awesome-copilot@gh-cli
npx skills add xixu-me/skills@github-actions-docs
```

## Verifying Skills Work

After installing development skills, run a verification workflow:

```bash
# Clone a test repo and run inspection
hermes execute "Inspect the codebase at ./my-project and report LOC by language"

# Test PR workflow on a practice repo
hermes execute "Create a branch, add a README fix, and open a PR"
```

All development skills include verification steps — they confirm `git push` succeeded, CI is actually running, and the PR is visible on GitHub before reporting success. No "fire and forget" assumptions.
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
