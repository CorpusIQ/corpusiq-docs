---
title: Ashima Meta-Routing Orchestration Setup Guide
description: Install and configure doucoo/ashima — a 4-skill meta-routing package for Hermes Agent with Aria (coding), Duet (dual-perspective reasoning), and Chorus (documentation orchestration)
---

# Ashima — Meta-Routing Orchestrator Setup

**Source:** [doucoo/ashima](https://github.com/doucoo/ashima)
**Stars:** 1 ⭐ | **License:** Apache-2.0
**Created:** June 24, 2026
**Package:** 4 skills (ashima router + aria + duet + chorus)

---

## 1. What It Is

Ashima is a meta-routing skill for AI agent orchestration. Named after the Yi legend of Ashima (a young woman celebrated for her singing), it provides three specialized voices:

| Voice | Mode | What It Does |
|-------|------|--------------|
| **Aria** | Coding Orchestration | One voice, precise and structured. Orchestrates Codex to implement + Claude to review, with scoped delegation and explicit verification gates |
| **Duet** | Dual-Perspective Reasoning | Two voices in dialogue. Fans a question to Claude-side and GPT-side perspectives, presents both, runs critique rounds |
| **Chorus** | Documentation Orchestration | All voices together. Gathers repo context, drafts docs/changelogs/release notes, routes through independent fact-check review |

The **ashima router** auto-detects the task type and dispatches to the correct voice:
- Code → `aria`
- Side-by-side viewpoints → `duet`
- Prose documentation → `chorus`

## 2. Prerequisites

- Hermes Agent installed (plugin or standard)
- Access to both Claude and GPT/Codex provider backends (for duet mode)
- Codex CLI installed (for aria mode — optional, falls back to in-agent implementation)
- Git

## 3. Installation

```bash
git clone https://github.com/doucoo/ashima.git
cp -r ashima/ashima  ~/.hermes/skills/ashima
cp -r ashima/aria   ~/.hermes/skills/aria
cp -r ashima/duet   ~/.hermes/skills/duet
cp -r ashima/chorus ~/.hermes/skills/chorus
```

### Verify Installation

```bash
hermes skills list | grep -E "ashima|aria|duet|chorus"
```

Expected output:
```
ashima     — Ashima Orchestration Router
aria       — Coding Orchestration (Codex + Claude)
duet       — Dual-Perspective Reasoning
chorus     — Documentation Orchestration
```

## 4. Configuration

### Provider Setup for Duet

Duet requires access to both Claude and GPT perspectives. Configure in `~/.hermes/config.yaml`:

```yaml
providers:
  claude:
    api_key_env: ANTHROPIC_API_KEY
    model: claude-sonnet-4-20250514
  
  gpt:
    api_key_env: OPENAI_API_KEY
    model: gpt-4o
```

### Aria Codex Integration

Aria defaults to using Codex CLI for implementation. Ensure Codex is available:

```bash
# Verify Codex CLI
codex --version

# If not installed
npm install -g @openai/codex
```

## 5. Usage

### Manual Invocation

```bash
# Route to specific voice
hermes -s ashima "ashima aria — implement the auth module"
hermes -s ashima "ashima duet — compare microservices vs monolith"
hermes -s ashima "ashima chorus — write release notes for last 5 commits"

# Auto-route (ashima detects task type)
hermes -s ashima "ashima — help me refactor the database layer"
```

### From Within a Session

```
/skill ashima aria — fix the race condition in queue.py
/skill ashima duet — should we use Redis or Postgres for caching?
/skill ashima chorus — document the API endpoints
```

## 6. CorpusIQ Use Cases

| Use Case | Voice | Why |
|----------|-------|-----|
| **Feature implementation** | Aria | Codex implements, Claude reviews — built-in code review pipeline |
| **Architecture decisions** | Duet | Independent Claude vs GPT analysis before committing to architecture |
| **Release documentation** | Chorus | Gathers diffs, drafts changelog, fact-checks against actual code |
| **Bug fix triage** | Aria | Verified fix with explicit acceptance criteria before deployment |
| **Strategy exploration** | Duet | Compare two model perspectives on growth strategy or pricing |

## 7. Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `hermes skills list` shows nothing | Skills not in `~/.hermes/skills/` | Verify cp paths; check `hermes config get skills.path` |
| Duet only gets one perspective | Only one provider configured | Add both Claude and GPT providers; verify API keys |
| Aria can't find Codex | Codex CLI not installed or not in PATH | Install Codex: `npm install -g @openai/codex` |
| Auto-routing picks wrong voice | Ambiguous task description | Be more explicit: "ashima aria — implement..." bypasses routing |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [June 24 Discovery](/hermes/skills/marketplace/new-june24-2026/) →*
