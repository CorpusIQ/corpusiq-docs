---
title: "Engram MCP - Git-Backed Shared Memory Dashboard for AI"
description: "Engram MCP server - self-hosted memory with dashboard UI backed by a git repository of markdown files."
category: mcp
tags: [mcp-server, memory, knowledge-management, git-backed, self-hosted, dashboard]
last_updated: 2026-10-30
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/engram-mcp/"
robots: "index,follow"

---

# Engram MCP Server - Git-Backed Memory Dashboard

Engram is a self-hosted MCP server + dashboard that gives AI agents shared memory over a git-backed folder of markdown files. What differentiates it from other memory servers: search is authoritative - it always returns the latest committed version, not a stale embedding. The dashboard provides human visibility into what agents are remembering.

**Source:** awesome-mcp-servers PR #9807 (discovered July 19, 2026)
**Category:** Knowledge & Memory
**Author:** rwnalds
**Repo:** https://github.com/rwnalds/engram
**Status:** Active

## Why This Matters

Most vector-based memory solutions have a fundamental problem: the embedding and the source document drift apart. Engram solves this by making the source of truth a git repository of markdown files - every write is a commit, every read is from HEAD. The dashboard lets humans audit what agents are writing, edit memories directly, and roll back bad writes via git.

## Installation

Engram is a self-hosted server with a persistent volume, so run it as a container - Railway, Render,
Fly, or your own box. Serverless (Vercel) will not work: Engram holds a volume, a file watcher and an
in-memory index that a serverless function cannot keep alive.

```bash
# Prebuilt image (the -app image serves HTTP; plain `engram:latest` is the stdio server)
docker run -d \
  -p 3000:3000 \
  -v engram-data:/data \
  -e ENGRAM_DATA_DIR=/data \
  ghcr.io/rwnalds/engram-app:latest
```

Then open the dashboard, connect your vault repo under **Workspaces** (by URL + token, or GitHub
OAuth), and create an MCP token on the **Connect** page.

Note on the package name: `npm install -g engram-mcp` is a **different, unrelated product** (ngrm.ai).
It is not this server and does not expose these tools.

## Connecting an MCP Client

Engram speaks HTTP at `POST /api/mcp` with a bearer token. Token scope decides what the agent sees: a
`read` token never sees the write tools.

```bash
claude mcp add --transport http engram https://<your-host>/api/mcp \
  --header "Authorization: Bearer <token>"
```

## Key Tools

15 tools, split by token scope. `brain_capture` appears only when the Curator is set to `full`.

| Tool | Access | Description |
|------|--------|-------------|
| `brain_search` | read | Search the active vault |
| `brain_read` | read | Read a note |
| `brain_list` | read | List notes in a folder |
| `brain_recent` | read | Recently changed notes |
| `brain_tree` | read | Folder tree for the vault |
| `brain_backlinks` | read | Inbound links to a note |
| `brain_graph` | read | Link graph around a note |
| `brain_schema` | read | Vault schema and conventions |
| `brain_write` | write | Create a note |
| `brain_edit` | write | Edit an existing note |
| `brain_append` | write | Append to a note |
| `brain_move` | write | Move or re-file a note |
| `brain_supersede` | write | Replace a note, keeping the prior version |
| `brain_create_folder` | write | Create a folder |
| `brain_delete` | write | Delete a note |

The read/write split is enforced server-side: an agent holding a read-scope token cannot call the
write tools at all.

## Dashboard

Engram includes a web dashboard at `http://localhost:3001` where humans can:
- Browse all agent-written memories
- Edit or delete entries manually
- View git history and diffs
- Roll back to any previous version

## CorpusIQ Relevance

Engram's git-backed approach is philosophically aligned with how CorpusIQ already operates (GBrain's markdown vault, git-tracked docs). Could serve as a lighter alternative to GBrain for teams that want agent memory without the full knowledge graph infrastructure.

## See Also

- [[sweeps/sweep-july19-2026]]
- Linksee Memory
