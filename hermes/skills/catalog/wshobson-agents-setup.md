---
title: wshobson/agents — Agent Plugin Marketplace for Hermes
description: Access 94 plugins, 203 agents, 175 skills, and 109 commands from the wshobson/agents marketplace. Multi-harness support for Claude Code, Codex CLI, Cursor, OpenCode, Gemini CLI, and GitHub Copilot — all from a single source.
---

# wshobson/agents — Agent Plugin Marketplace

**Source:** [wshobson/agents](https://github.com/wshobson/agents) (9.1K+ installs for top skill)
**Category:** Agent Orchestration / Plugins
**Harnesses:** Claude Code, Codex CLI, Cursor, OpenCode, Gemini CLI, GitHub Copilot

Massive agent plugin marketplace with 94 plugins, 203 agents, 175 skills, and 109 commands. One source-of-truth (`plugins/`) compiled into idiomatic artifacts for six different agent harnesses. Each harness gets native artifacts — not lowest-common-denominator translations.

---

## Installation

### For Hermes (Claude Code-based)

```bash
# Add the marketplace
/plugin marketplace add wshobson/agents

# Install individual plugins
/plugin install python-development
/plugin install security-audit
/plugin install memory-forensics
```

### For Other Harnesses

```bash
# Codex CLI
npx codex-marketplace add wshobson/agents

# Cursor
# Add marketplace, then /plugin install <name>

# Gemini CLI
gh repo clone wshobson/agents ~/agents && cd ~/agents
make generate HARNESS=gemini && gemini extensions install .

# OpenCode
gh repo clone wshobson/agents ~/agents && cd ~/agents
make install-opencode
```

Verify:
```bash
/plugin list | grep wshobson
```

---

## Plugin Categories (94 Total)

| Category | Count | Top Plugins |
|---|---|---|
| **Development** | 25+ | python-development, typescript-development, rust-development, go-development |
| **Security** | 12 | security-audit, memory-forensics, vulnerability-scan, threat-modeling |
| **Infrastructure** | 15 | terraform-iac, kubernetes-management, docker-orchestration, aws-architecture |
| **Data & ML** | 10 | sql-optimization, data-pipeline-design, ml-model-deployment |
| **Architecture** | 8 | system-design, api-design, microservices-patterns |
| **Documentation** | 6 | api-docs-generator, readme-writer, changelog-automation |
| **Business & SEO** | 8 | seo-audit, growth-strategy, market-research |
| **Memory & Context** | 5 | memory-safety-patterns, memory-forensics, context-optimization |
| **Orchestration** | 16 | multi-agent-coordination, full-stack-workflow, incident-response |

---

## Key Plugins for Hermes/CorpusIQ

### Memory & Security Plugins

```bash
# Memory safety patterns for agent context management
/plugin install memory-safety-patterns

# Analyze agent memory for security issues
/plugin install memory-forensics

# Extract security requirements from specifications
/plugin install security-requirement-extraction
```

### Orchestration Plugins

```bash
# Multi-agent coordination for complex workflows
/plugin install multi-agent-orchestrator

# Full-stack development with agent handoff
/plugin install full-stack-workflow

# Incident response automation
/plugin install incident-response
```

### Development Plugins

```bash
# Python development with testing, linting, type checking
/plugin install python-development

# TypeScript/Node development
/plugin install typescript-development

# Infrastructure as Code
/plugin install terraform-iac
```

---

## Architecture

```
plugins/
├── python-development/     # 90+ local plugins
├── security-audit/
├── memory-forensics/
├── ... (94 total)
├── agents/                  # 203 domain-expert agents
├── skills/                  # 175 modular knowledge packages
└── commands/                # 109 slash commands
```

Each plugin is isolated and composable. Agents, commands, and skills are auto-discovered. Progressive disclosure ensures skills only load when activated.

### Harness Compilation

```
Source (plugins/) ──▶ Harness Generator ──▶ Native artifacts
                         │
                         ├── Claude Code (.claude-plugin/)
                         ├── Codex CLI (codex-marketplace format)
                         ├── Cursor (.cursor-plugin/)
                         ├── OpenCode (generated + symlinked)
                         ├── Gemini CLI (generated + transformed)
                         └── GitHub Copilot (copilot plugin format)
```

---

## Common Workflows

### Security Audit Workflow

```bash
# 1. Install security plugins
/plugin install security-audit
/plugin install vulnerability-scan
/plugin install memory-forensics

# 2. Run security audit
/security:audit --target ./src --output audit-report.md

# 3. Run memory forensics on agent context
/memory:forensics --session-id current --output memory-report.json
```

### Multi-Agent Development

```bash
# 1. Install orchestrator + dev plugins
/plugin install multi-agent-orchestrator
/plugin install python-development
/plugin install typescript-development

# 2. Start coordinated workflow
/orchestrator:full-stack --spec ./spec.md --output ./output/
```

---

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `/plugin marketplace add` fails | Network/auth issue | Verify `gh` CLI is authenticated: `gh auth status` |
| Plugin not found | Marketplace not registered | Re-run `marketplace add` command |
| Skills don't activate | Plugin not installed | Check with `/plugin list` |
| Harness-specific failures | Generated artifacts stale | Re-clone and regenerate for your harness |
| Gemini CLI setup fails | Missing `make` | `sudo apt-get install make` |

---

## Comparison: Other Agent Marketplaces

| Marketplace | Plugins | Harnesses | Hermes Support |
|---|---|---|---|
| **wshobson/agents** | 94 | 6 | Via Claude Code harness |
| anthropics/knowledge-work-plugins | 11 | 2 (Cowork + Code) | Via Claude Code only |
| github/awesome-copilot | 14 skills | 1 (Copilot) | MCP generators work anywhere |
| vercel-labs/agent-skills | 6 | 1 (Vercel) | Framework-specific |

**Recommendation:** wshobson/agents has the broadest coverage. Use as the primary agent plugin source. Supplement with github/awesome-copilot for GitHub/MCP automation and anthropics/knowledge-work-plugins for enterprise workflows.

---

## See Also

- [Awesome Copilot Setup](/hermes/skills/catalog/awesome-copilot-setup/) — GitHub Copilot agent skills (MCP generators)
- [Skill Creator Setup](/hermes/skills/catalog/skill-creator-setup/) — Build your own agent skills
- [Agent Memory Setup](/hermes/skills/catalog/agentmemory-setup/) — Persistent agent memory
