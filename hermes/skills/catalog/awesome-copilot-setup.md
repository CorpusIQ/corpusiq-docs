---
title: github/awesome-copilot — MCP Server Generators & GitHub Automation for Hermes
description: Install skills from github/awesome-copilot (13.1K+ installs) — MCP server generators (TypeScript/Python), GitHub workflow automation, and documentation tools. Works with GitHub Copilot and adaptable to Hermes agents.
---

# github/awesome-copilot — Setup Guide

**Source:** [github/awesome-copilot](https://github.com/github/awesome-copilot) (13.1K installs for top skill)
**Category:** Agent Tools / GitHub Automation
**Harness:** GitHub Copilot (native); skills usable in any agent via skills.sh

Community-created collection of custom agents, instructions, skills, hooks, workflows, and plugins for GitHub Copilot. Contains MCP server generators, GitHub workflow automation, documentation tools, and deployment helpers. Skills are installable via `npx skills add` and work across agent harnesses.

---

## Installation

### Via skills.sh (Universal)

```bash
# MCP Server Generator (TypeScript) — 11.3K installs
npx skills add github/awesome-copilot@typescript-mcp-server-generator

# MCP Server Generator (Python) — 9.9K installs
npx skills add github/awesome-copilot@python-mcp-server-generator

# MCP CLI tools — 9.5K installs
npx skills add github/awesome-copilot@mcp-cli

# GitHub Issues automation — 13.1K installs
npx skills add github/awesome-copilot@github-issues

# Memory merger — 12.7K installs
npx skills add github/awesome-copilot@memory-merger
```

### Via GitHub Copilot

```bash
# Register the marketplace (if not pre-registered)
copilot plugin marketplace add github/awesome-copilot

# Install individual skills
copilot plugin install typescript-mcp-server-generator@awesome-copilot
copilot plugin install github-issues@awesome-copilot
```

Verify:
```bash
npx skills list | grep awesome-copilot
```

---

## Available Skills (14 Total)

| Skill | Installs | Category | Hermes Relevance |
|---|---|---|---|
| **github-issues** | 13.1K | GitHub Automation | ✅ High — automate issue creation/management |
| **microsoft-docs** | 13.2K | Documentation | ⬜ Medium — Microsoft-specific |
| **typescript-mcp-server-generator** | 11.3K | MCP | ✅ High — generate MCP servers for Hermes |
| **java-docs** | 10.3K | Documentation | ⬜ Low — Java-specific |
| **python-mcp-server-generator** | 9.9K | MCP | ✅ High — generate Python MCP servers |
| **create-github-action-workflow-specification** | 9.8K | CI/CD | ✅ High — GitHub Actions for Hermes CI |
| **mcp-cli** | 9.5K | MCP | ✅ High — CLI tools for MCP server management |
| **azure-deployment-preflight** | 9.4K | Deployment | ⬜ Medium — Azure-specific |
| **csharp-docs** | 9.1K | Documentation | ⬜ Low — C#-specific |
| **create-github-pull-request-from-specification** | 9K | GitHub | ✅ High — automated PR creation |
| **create-github-issues-feature-from-implementation-plan** | 9K | GitHub | ✅ High — spec-to-issues automation |
| **github-copilot-starter** | 8.8K | Onboarding | ⬜ Medium — Copilot onboarding |
| **create-github-issues-for-unmet-specification-requirements** | 8.8K | GitHub | ✅ High — gap analysis automation |
| **memory-merger** | 12.7K | Memory | ✅ High — merge agent memory across sessions |

---

## Key Skills for Hermes/CorpusIQ

### MCP Server Generators

Generate working MCP servers from natural language specifications:

```bash
# TypeScript MCP server
npx skills add github/awesome-copilot@typescript-mcp-server-generator

# Python MCP server
npx skills add github/awesome-copilot@python-mcp-server-generator
```

**Use case:** When you need a new MCP connector for Hermes (e.g., "Connect to HubSpot API"), invoke the generator skill and it produces a complete, working MCP server with tool definitions, authentication, and error handling.

### GitHub Workflow Automation

```bash
# Auto-create GitHub issues from implementation plan
npx skills add github/awesome-copilot@create-github-issues-feature-from-implementation-plan

# Auto-create PR from specification
npx skills add github/awesome-copilot@create-github-pull-request-from-specification

# Find unmet requirements and create issues
npx skills add github/awesome-copilot@create-github-issues-for-unmet-specification-requirements

# Create GitHub Actions workflows
npx skills add github/awesome-copilot@create-github-action-workflow-specification
```

### Memory Merger

```bash
npx skills add github/awesome-copilot@memory-merger
```

Merges agent memory across sessions. 12.7K installs. Already documented in [Memory Merger Setup](/hermes/skills/catalog/memory-merger-setup/).

---

## Integration with Hermes Agent

### Using MCP Server Generators

When you need a new MCP connector:

1. **Describe the target API:**
   ```
   "Create an MCP server for the HubSpot CRM API with tools for:
   - list_contacts(filter, limit)
   - get_contact(id)
   - create_contact(properties)
   - search_deals(query)"
   ```

2. **The generator produces:**
   - `server.py` or `server.ts` with complete MCP implementation
   - `package.json` / `requirements.txt` with dependencies
   - Authentication handling (OAuth, API key, etc.)
   - Tool definitions with proper input schemas
   - Error handling and rate limiting

3. **Deploy to Hermes:**
   ```bash
   # Add to Hermes MCP config
   hermes mcp add ./generated-server/server.py --name hubspot
   hermes mcp test hubspot
   ```

### GitHub Workflow Automation

```bash
# From Hermes: convert a feature spec into GitHub issues
cat feature-spec.md | hermes tool call github-issues-from-spec

# Create a PR with all changes
hermes tool call create-pr-from-spec --spec feature-spec.md --branch feature/xyz
```

---

## Comparison: MCP Server Generation Approaches

| Approach | github/awesome-copilot | anthropics/skills@mcp-builder | Manual |
|---|---|---|---|
| **Install base** | 11.3K (TS), 9.9K (Py) | 91K | — |
| **Languages** | TypeScript + Python | Multiple | Any |
| **Automation** | Full generation from spec | Guided building | Manual coding |
| **Hermes integration** | Via skills.sh install | Via skills.sh install | Direct |
| **Best for** | Quick MCP server creation | Complex multi-tool servers | Custom requirements |
| **Learning curve** | Low — natural language spec | Medium — MCP knowledge needed | High — MCP protocol expertise |

**Recommendation:** Use `typescript-mcp-server-generator` or `python-mcp-server-generator` for rapid MCP connector creation. Fall back to `anthropics/skills@mcp-builder` for complex servers requiring multiple transports or advanced features.

---

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `npx skills add` fails | Network/auth issue | Check npm registry access: `npm ping` |
| MCP generator produces errors | Missing dependencies | Install deps before running: `pip install mcp` or `npm install @modelcontextprotocol/sdk` |
| GitHub issues creator fails | Missing `gh` CLI auth | `gh auth login` |
| Memory merger not working | Session DB locked | Close other Hermes sessions first |
| Skill not recognized by Copilot | Marketplace not registered | `copilot plugin marketplace add github/awesome-copilot` |

---

## See Also

- [MCP Builder Setup](/hermes/skills/catalog/) — Anthropic's MCP builder (91K installs)
- [Memory Merger Setup](/hermes/skills/catalog/memory-merger-setup/) — Already covered in catalog
- [Skill Creator Setup](/hermes/skills/catalog/skill-creator-setup/) — Build your own skills (318K installs)
- [wshobson Agents Marketplace](/hermes/skills/catalog/wshobson-agents-setup/) — 94-plugin marketplace
- [Build MCP Server Setup](/hermes/skills/catalog/build-mcp-server-setup/) — Manual MCP server building
