---
title: Replicas Agent Skill — Cloud Workspace Coding Agent Setup
description: "replicas-group/skill — replicas-agent (34.7K installs): background coding agent guide for Replicas cloud workspaces with previews, Slack, Linear, GitHub, Google Workspace, Docker, and media sharing integrations."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/replicas-agent-skill-setup/"
robots: "index,follow"
last_updated: "2026-08-15"
tags: ["hermes skill", "agent skill", "skill setup", "cloud workspace", "coding agent"]
---

# Replicas Agent Skill — Setup Guide

**Source:** [replicas-group/skill](https://skills.sh/replicas-group/skill)
**GitHub:** [replicas-group/skill](https://github.com/replicas-group/skill)
**Skills:** 1 skill (`replicas-agent`) · 34.7K installs
**Category:** Cloud Workspaces & Coding Agents
**First Seen:** March 17, 2026 (catalogued August 15, 2026 sweep)
**Quality Tier:** 🟢 Production (all three security audits pass)

replicas-agent is the operating guide for a background coding agent running inside a Replicas cloud workspace (a remote VM). It covers exposing local services as public preview URLs, messaging and file operations on Slack, issue and comment workflows on Linear and GitHub, creating and editing Google Docs/Sheets/Forms, managing Docker containers and the daemon, sharing screenshots, recordings, diagrams, and audio inline in Replicas chat, and managing automations, environment variables, repos, and `replicas.json` via the pre-installed `replicas` CLI.

---

## Installation

```bash
npx skills add replicas-group/skill --skill replicas-agent
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Replicas workspace** | A Replicas cloud workspace (remote VM) with the `replicas` CLI pre-installed |
| **Node.js + npx** | For the installer |
| **Service accounts** | Slack, Linear, GitHub, and Google Workspace credentials for the integrations |

## What It Provides

| Capability | Notes |
|---|---|
| Previews | Expose local services as public preview URLs for human review |
| Slack | Send messages, read threads, upload files |
| Linear | Fetch issues, update state, comment |
| GitHub | Repository and issue workflows |
| Google Workspace | Create and edit Docs, Sheets, and Forms |
| Docker | Manage containers and the Docker daemon |
| Media sharing | Screenshots, recordings, diagrams, and audio inline in chat |
| Configuration | Automations, env vars, repos, and `replicas.json` via the `replicas` CLI |

## Quick Start

1. `npx skills add replicas-group/skill --skill replicas-agent`
2. In a Replicas workspace: "start the dev server and expose it as a public preview"
3. "Post a screenshot of the running app to the Slack channel and comment the issue on Linear"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Preview reviews** | Public preview URLs for stakeholder review of dashboard and docs changes |
| **Multi-tool reporting** | Slack + Linear + GitHub integration pattern for agent work logs |
| **Container ops** | Docker management patterns for MCP server deployments |
| **Media in chat** | Screenshot/diagram sharing pattern for reporting agent output inline |

## Limitations / Verification

- Scoped to Replicas cloud workspaces — outside that environment it is a pattern reference
- Requires a Replicas account and workspace

```bash
npx skills add replicas-group/skill --skill replicas-agent   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [VPS Server Management Setup](/hermes/skills/catalog/vps-server-management-setup/) — remote VM operations

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*

*Powered by CorpusIQ*
