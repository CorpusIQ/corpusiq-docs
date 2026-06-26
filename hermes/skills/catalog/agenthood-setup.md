---
title: Agenthood — 14-Agent AI Engineering Team Setup Guide
description: Install and configure Agenthood's 14 specialized AI agents for Hermes — code review, security audit, architecture design, testing, and more. Drop-in Markdown skills for any agent runtime.
---

# Agenthood — Setup Guide

**Source:** [fworks-tech/agenthood](https://skills.sh/fworks-tech/agenthood) · [GitHub](https://github.com/fworks-tech/agenthood)
**Category:** Multi-Agent Architecture / Development Workflows
**npm:** `agenthood` (v3.0.0) · **License:** MIT

Agenthood packages a complete AI engineering team as 14 individual SKILL.md files. Each agent — from The Reviewer to The Auditor — is a self-contained role with defined responsibilities, communication standards, and quality gates. They work with any agent runtime including Hermes Agent, Claude Code, and Copilot.

---

## The Team

| # | Agent | Role | Best For |
|---|-------|------|----------|
| 1 | **The Architect** | System design, ADRs | Planning features, technical decisions |
| 2 | **The Auditor** | Security scanning | Vulnerability assessment, dependency audit |
| 3 | **The Debugger** | Error triage | Root cause analysis, stack trace investigation |
| 4 | **The Doorman** | Validation gates | Branch protection, CI health checks |
| 5 | **The Envoy** | Cross-provider translation | Convention validation across runtimes |
| 6 | **The Herald** | Release management | Versioning, changelog generation |
| 7 | **The Librarian** | Documentation | API references, knowledge management |
| 8 | **The Oracle** | Institutional knowledge | Authoring templates, best practices |
| 9 | **The Reviewer** | Code review | Standards enforcement, PR quality |
| 10 | **The Scribe** | Commits & PRs | Commit messages, PR descriptions |
| 11 | **The Sentinel** | Integrity monitoring | Cross-member contradiction detection |
| 12 | **The Steward** | Context economy | Provider cache strategies, token optimization |
| 13 | **The Tester** | Test coverage | TDD, edge case generation |
| 14 | **The Warden** | Code health | Complexity enforcement, technical debt tracking |

---

## Installation

### Option A: Via skills.sh (Recommended for Hermes)

```bash
# Install the full agent team
npx skills add fworks-tech/agenthood

# Or install specific agents
npx skills add fworks-tech/agenthood --skill the-reviewer
npx skills add fworks-tech/agenthood --skill the-auditor
npx skills add fworks-tech/agenthood --skill the-architect
npx skills add fworks-tech/agenthood --skill the-tester
```

### Option B: Via npm (Standalone CLI)

```bash
npm install --save-dev agenthood
npx agenthood init       # Interactive setup (~5 minutes)
npx agenthood check      # Verify installation
```

### Option C: Direct GitHub Clone

```bash
git clone https://github.com/fworks-tech/agenthood.git
cp -r agenthood/skills/* ~/.hermes/profiles/corpusiq/skills/
```

---

## Usage with Hermes Agent

### Load Individual Agents as Skills

After installing via skills.sh, each agent is available as a skill in your Hermes profile:

```bash
# Verify installed skills
hermes skills list --marketplace | grep agenthood
```

Invoke agents by their role in natural language:

```
"Run the-reviewer on the current PR diff"
"Have the-auditor scan our authentication flow"
"Ask the-architect to review the proposed database schema"
```

### Compose Agent Teams

For complex workflows, load multiple agents and let Hermes route tasks:

```
"Run the full agenthood team on this PR: the-scribe for commit messages,
the-reviewer for code quality, the-tester for coverage gaps, and
the-warden for complexity checks"
```

### Autonomous Execution

Agenthood includes a TypeScript CLI for running agents independently:

```bash
# Set LLM provider (Groq free tier, Anthropic, or OpenAI)
export GROQ_API_KEY="gsk_..."
# Or use Ollama for fully offline execution

# List available agents
npx agenthood list

# Run an agent autonomously
npx agenthood run the-scribe "write a commit message for the current diff"
npx agenthood run the-reviewer "review the changes in the last commit"
npx agenthood run the-architect "plan the implementation for issue #42"
```

---

## Key Workflows for Hermes

### PR Review Pipeline

```bash
# 1. Review code quality
hermes --skill the-reviewer "Review the PR at HEAD"

# 2. Check security
hermes --skill the-auditor "Audit dependencies and auth flow"

# 3. Verify tests
hermes --skill the-tester "Check test coverage for changed files"

# 4. Generate changelog
hermes --skill the-scribe "Generate changelog entry for this PR"
```

### Architecture Decision Records

```bash
hermes --skill the-architect "Create an ADR for our caching strategy:
- Problem: Repeated expensive queries
- Options: Redis vs in-memory vs CDN edge caching
- Constraints: <50ms p95 latency, multi-region"
```

### Security Audit Pipeline

```bash
hermes --skill the-auditor "Run full security audit:
1. Dependency vulnerability scan
2. Auth flow review
3. Secret detection in codebase
4. API endpoint exposure check"
```

---

## Provider Configuration

| Variable | Provider | Free Tier |
|----------|----------|-----------|
| `GROQ_API_KEY` | Groq (default) | [console.groq.com](https://console.groq.com) |
| `ANTHROPIC_API_KEY` | Anthropic | — |
| `OPENAI_API_KEY` | OpenAI | — |

Or use **Ollama** for fully offline execution (no API key required):

```bash
ollama pull llama3.3
npx agenthood run the-reviewer "review this code" --provider ollama
```

---

## Why This Matters

Agenthood solves a critical gap in the agent ecosystem: **standardized, composable agent roles.** Instead of every team reinventing code review agents, security auditors, and PR validators, Agenthood provides battle-tested implementations that work across runtimes.

For Hermes specifically:
- **Drop-in quality gates** — the-doorman validates branches, the-reviewer enforces standards
- **Multi-agent blueprints** — reference architecture for Hermes agent teams
- **Runtime-agnostic** — skills work with Hermes, Claude Code, Copilot, and the standalone CLI
- **Opinionated standards** — agents have real standards (they will block merges with bad commit messages)

---

## Verification

```bash
# Confirm installation
npx skills list | grep agenthood
hermes skills list --marketplace | grep agenthood

# Test an agent
npx agenthood run the-scribe "hello"

# Check skill files are accessible
ls ~/.hermes/profiles/corpusiq/skills/the-reviewer/
```

---

*[Agenthood on skills.sh →](https://skills.sh/fworks-tech/agenthood) · [GitHub →](https://github.com/fworks-tech/agenthood) · [npm →](https://www.npmjs.com/package/agenthood)*
