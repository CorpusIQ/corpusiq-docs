---
title: "GitLab MCP - CorpusIQ Docs - CorpusIQ Docs"
description: "GitLab MCP server for AI clients - manage projects, merge requests, issues, pipelines, wiki and releases over stdio, SSE or Streamable HTTP"
category: Developer Tools
stars: 1,898
added: 2026-08-18
source: mcp.so GitHub issues
relevance: ★★
tags: [gitlab, devops, merge-requests, issues, pipelines, project-management, self-hosted, oauth]
---

# GitLab MCP (zereight/gitlab-mcp)

**GitLab MCP server for AI clients — manage projects, merge requests, issues, pipelines, wiki pages, releases, tags, and milestones through stdio, SSE, or Streamable HTTP.** Auth supports personal access tokens, OAuth, a read-only mode, and remote authorization. Actively maintained since February 2025 with 1,898 stars, npm package `@zereight/mcp-gitlab`, and an official MCP registry listing.

```
Server type: stdio, SSE, or Streamable HTTP
Auth: PAT, OAuth, or read-only mode
Install: npx -y @zereight/mcp-gitlab or brew install zereight/gitlab-mcp/zereight-mcp-gitlab
Tools: Projects, MRs, issues, pipelines, wiki, releases, tags, milestones
Pricing: Free (MIT-style open source)
Category: Developer Tools / Engineering Operations
Built by: zereight (repo: zereight/gitlab-mcp, docs: zereight.github.io/gitlab-mcp)
```

## Why This Matters for Operators

Operators running engineering teams on GitLab — especially self-hosted GitLab — live in two surfaces: the code platform and the business tools. This MCP puts the code platform's management layer (issues, MRs, pipelines, milestones) inside the agent that already writes the status updates, so sprint standups, release checks, and merge-request triage happen from chat instead of browser tabs.

**Read-only mode is the sane default.** Connect with a read-only token for status and reporting use cases; enable write scopes only where the agent is trusted to act. The three transports (stdio for local agents, SSE and Streamable HTTP for remote or self-hosted instances) cover every deployment shape.

## Tools & Capabilities

| Area | What it does |
|---|---|
| Projects | Project metadata and settings |
| Merge requests | List, inspect, review, approve, merge |
| Issues | Create, read, update, comment, close |
| Pipelines | Trigger, watch, read logs and status |
| Wiki | Read and write wiki pages |
| Releases / tags | Manage releases and tags |
| Milestones | Track and update milestones |

Supports GitLab.com and self-hosted instances via a configurable API base URL.

## Installation

```bash
npx -y @zereight/mcp-gitlab
# or
brew install zereight/gitlab-mcp/zereight-mcp-gitlab
```

```json
{
  "mcpServers": {
    "gitlab": {
      "command": "npx",
      "args": ["-y", "@zereight/mcp-gitlab"],
      "env": {
        "GITLAB_PERSONAL_ACCESS_TOKEN": "glpat-YOUR_TOKEN",
        "GITLAB_API_URL": "https://gitlab.example.com"
      }
    }
  }
}
```

## Configuration

Create a personal access token with the minimum scopes for the intended use — `read_api` for read-only reporting, `api` where the agent must act. For self-hosted instances, set `GITLAB_API_URL` to the instance root. Remote deployment runs the server with SSE or Streamable HTTP and the remote authorization flow.

## Business Relevance

- **Engineering leads** get MR and pipeline status in the same chat where they write stakeholder updates
- **Self-hosted GitLab shops** connect agents to the internal instance without exposing it publicly
- **Release operators** script release and tag checks from the agent
- **Project managers** track issues and milestones without switching surfaces

## Integration with CorpusIQ

CorpusIQ covers the business data plane — finance, commerce, marketing, CRM. GitLab MCP covers the engineering data plane — code, MRs, pipelines. The two are the classic "business + build" pair for a product company.

The composed workflow: CorpusIQ answers "how did the release perform" (revenue, sessions, funnel) while GitLab MCP answers "what shipped and what's in flight" (MRs merged, pipelines green, issues closed). A single agent session can reconcile deployment events with business impact — the release retrospective writes itself.

## Limitations

- Write operations require PAT scopes beyond read-only — scope discipline is on the operator
- Server manages GitLab only; no GitHub or Bitbucket coverage
- Self-hosted instances need reachable API URL from wherever the agent runs
- Dev-tool class server — value concentrates where engineering output is the business
