---
title: "AgentGrid MCP - Shared Workspace for Agents"
description: "Anima's hosted workspace where humans and agents build, host, publish and review live apps, docs and files, with every artifact a real git repository."
category: Productivity
stars: n/a (hosted platform, agentgrid.io)
added: 2026-10-01
source: "mcp.so feed + server page (agentgrid-io)"
relevance: ★★★
tags: [agent-workspace, collaboration, artifacts, publishing, git, review-workflow, remote-mcp]
---

# AgentGrid MCP

**A governed workspace where agents and humans ship artifacts together.** AgentGrid, by Anima, gives any MCP-capable agent a shared home for live apps, docs and files. Everything the agent creates lands as an artifact in a team workspace, each one a real git repository that can be cloned, committed to, reviewed and published to a live URL.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth
Endpoint: https://api.agentgrid.io/v1/mcp
Tools: 10
Pricing: not published on the listing
Category: Productivity / collaboration
Built by: Anima
```

## Why This Matters for Operators

The hard part of agent output is rarely the generation, it is where it goes. Chat replies evaporate, local files are invisible to the team, and a staging deploy is heavier than the task deserves. AgentGrid answers that with a workspace: the agent builds in a place the team can see, edit and share, and it can publish a live public URL or take it down again.

The review surface is the differentiating part. Humans leave change requests pinned to a specific spot, either a DOM location in an app or a text range in a document, and the agent reads those comments, replies, and resolves them by carrying a trailer in its commit message. That gives a durable trail of what was asked and what commit answered it, instead of an approval that only exists in a chat scroll.

Because every artifact is a real git repository, the workflow degrades gracefully. An agent with shell and network access can clone and push normally; an agent without them uses the built-in explore and edit tools, which touch the same repository and need no local git at all.

## Key Capabilities

- **Build from a prompt, URL or Figma design.** Describe an app, clone a site, or hand over Figma frames and get a running app at a live URL.
- **Host existing code.** Import a project or start an empty repo and push to it.
- **Edit any artifact over git.** Clone, commit and push; artifacts are real repositories.
- **Publish and unpublish.** Put an artifact on a live public URL, or take it down.
- **Read and edit files without a shell.** List, search and read artifact files and commit history, and apply revisions, with no shell, git or network of your own.
- **Work review comments.** Read change requests, reply without closing, resolve with a commit trailer, or close with a note.
- **Manage workspaces and access.** List workspaces and capabilities, and list artifacts per workspace.

## Setup

Claude Code plugin:

```
/plugin marketplace add AnimaApp/mcp-server-guide
/plugin install anima@mcp-server-guide
```

Claude Code manual:

```
claude mcp add --transport http anima https://api.agentgrid.io/v1/mcp
```

Restart the client, run `/mcp`, select anima and authenticate in the browser. Any MCP client supporting remote servers can connect with the endpoint URL.

## Considerations

Access is scoped per workspace with read, write, share and publish capabilities, and an empty workspace list means nothing has been granted rather than that the team has none. Artifact listings are capped, so an agent should report what it found, never a total. Git access tokens handed out for local development are short-lived and scoped to a single artifact, and cannot be renewed: on expiry, request a fresh remote URL and reset it. Pricing is not published on the listing.

## FAQ

### What is AgentGrid MCP?
A hosted MCP server by Anima that gives agents a shared team workspace for building, hosting, publishing, reviewing and sharing live apps, docs and files.

### Are AgentGrid artifacts version controlled?
Yes. Every artifact is a real git repository, so it can be cloned, committed to and pushed, and history can be inspected.

### Can an agent without a shell edit AgentGrid files?
Yes. The built-in explore and edit tools list, search, read and modify artifact files and commit history with no shell, git or network access required.

### What is the AgentGrid MCP endpoint?
https://api.agentgrid.io/v1/mcp, a remote Streamable HTTP server authenticated with OAuth.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ](https://corpusiq.io) - 40+ business data connectors for AI agents
