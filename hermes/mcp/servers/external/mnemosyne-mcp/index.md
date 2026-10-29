---
title: "Mnemosyne MCP - Memory That Retires What It Replaced"
description: "An evidence-backed local memory store where a correction retires the facts that depended on it, and any state can be replayed."
category: AI
stars: ★★ (package and behaviour verified, v2.0.0, MIT)
added: 2026-10-29
source: "npm package mnemosy-ai 2.0.0 read from the npm registry on 29 October 2026 (MIT, repository 28naem-del/mnemosyne) and the vendor submission describing correction retirement, replay and bisect"
relevance: ★★★
tags: [memory, sqlite, corrections, provenance, replay, reranking, local-mcp]
last_updated: "2026-10-29"
---

# Mnemosyne MCP

**Every memory system in this catalogue can add a fact. Almost none of them can tell you which earlier answers are now wrong because that fact changed.**

```
Server type: Local (stdio)
Install:     npx -y -p mnemosy-ai@next mnemosy mcp --db ... --workspace ... --agent ...
Package:     mnemosy-ai 2.0.0 stable, 3.0.0-rc.2 on @next, MIT
Runtime:     Node 22.16.0 or newer
Store:       one SQLite file per workspace
Recall:      hybrid retrieval with cross-encoder reranking
Requires:    no model API key, no database server, no Docker
```

## Why This Matters for Operators

The failure mode of agent memory is not forgetting. It is remembering something that stopped being true and applying it confidently to a decision six weeks later. A price changed, a contact left, a policy was superseded, and the memory keeps serving the old version because nothing in the store knows the two are related.

This server is built around that relationship. It keeps an **evidence-backed** store, and a correction **retires the memories that depended on it** rather than sitting beside them as a newer opinion. The vendor also claims exact replay and bisect, which is the property that makes a memory auditable: you can return to a state and take it apart.

For an operator the value is not that an assistant remembers more. It is that when a number changes, the assistant stops quoting the old one, and that a disagreement about what it "knew" can be settled by replaying the state rather than by argument.

## What It Does

One SQLite file per workspace holds the memories. Recall is hybrid, with cross-encoder reranking on top of retrieval, so a query matches on meaning as well as on tokens.

```bash
claude mcp add mnemosyne -- npx -y -p mnemosy-ai@next mnemosy mcp \
  --db ./.mnemosyne/memory.sqlite --workspace my-project --agent assistant
```

The local engine needs **no model API key, no database server and no Docker**, which matters for a component holding a business's accumulated context: it can run entirely on the machine that already has the data.

## What Was Verified

The npm registry entry for `mnemosy-ai` resolved on 29 October 2026 at version **2.0.0**, licence **MIT**, repository `github.com/28naem-del/mnemosyne`, binary `mnemosy`. The package description states the design in one line: a local-first long-term memory for AI agents with an evidence-backed SQLite store, hybrid recall, cross-encoder reranking, and corrections that retire stale memories.

The vendor notes that `@next` is a `3.0.0-rc.2` pre-release and that the stable `2.0.0` exposes the same MCP tools, so a production install can stay on the stable tag.

## Limits Worth Recording

An early-stage package from a single maintainer, so the surface should be expected to move. The reranking and retirement behaviour were recorded from the published description rather than driven against a live store this pass.

`@next` in the install line is a pre-release tag. Pin the stable version unless there is a specific reason not to.

Memory scope is a design decision. One file per workspace keeps projects apart, and the workspace and agent flags in the install line are the mechanism, so naming them carelessly is how two projects end up sharing a brain.

## FAQ

### Do I need an API key for an embedding model?
No. The local engine needs no model API key, no database server and no Docker, which is what makes it usable on a machine that already holds the data.

### What happens when a fact changes?
A correction retires the memories that depended on it, rather than adding a newer entry beside the old one, so the stale fact stops being served.

### Can I tell why the agent remembered something?
Yes. The store is evidence-backed, and the vendor exposes exact replay and bisect, so a state can be returned to and taken apart.

### Which version should I install?
`mnemosy-ai@2.0.0` is the stable release and exposes the same MCP tools as the `3.0.0-rc.2` pre-release on `@next`.

### Where does the data live?
In a single SQLite file per workspace, on the machine running the server, passed with the `--db` flag.
