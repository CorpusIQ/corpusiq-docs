---
title: "Exomem MCP - CorpusIQ Docs"
description: Local Markdown and Obsidian memory substrate for MCP agents — hybrid FTS5 and vector search, governed review queues, and evidence that stays in plain files.
category: Productivity
stars: n/a (new listing)
added: 2026-08-17
source: mcpservers.org
relevance: ★★
tags: [memory, knowledge-base, obsidian, markdown, hybrid-search, sqlite-fts5, local-first, self-hosted]
---

# Exomem MCP

**Self-hosted MCP server (local, no account)** — Exomem runs agent memory over the Markdown knowledge base you already own: a plain folder or an Obsidian vault. Claude Code, Codex, and Cursor get durable context with hybrid keyword-plus-vector search, governed review queues, and evidence that stays in plain files. AGPL-3.0, `pip install exomem`, from Substrate Systems.

```
Server type: Self-hosted (stdio / local, plus CLI and REST surfaces)
Auth: none — no account, nothing leaves your machine in the lean install
Install: pip install exomem
Tools: search, capture, notes, evidence, audit, and review queues (MCP tools mirror the CLI/REST registry)
Pricing: open source (AGPL-3.0); hosted Exomem is a friends-only private alpha
Category: Memory
Built by: Substrate Systems (substratesystems.io/exomem)
```

## Why This Matters for Operators

Every cloud memory service extracts your notes into a vector database you never get back — the memory becomes a derived copy in someone else's infrastructure. Exomem inverts that: the Markdown files are the memory, and the index is a local SQLite sidecar next to them.

**The mechanism that matters is governed memory**: source material, compiled notes, typed entities, evidence, and supersession history remain plain files you can open, grep, and version. Supersession lives in the file (`status: superseded` + `superseded_by`), not in a hidden database — so when a decision gets overturned, the trail is reviewable. Batch embeddings are measured at 256 on 16 GB cards, with methodology published so you can reproduce the numbers on your own vault.

## Tools & Capabilities

| Area | Purpose |
|---|---|
| Search & capture | Hybrid keyword (SQLite FTS5) + vector (sqlite-vec) retrieval over typed Markdown |
| Notes & entities | Compiled notes, typed entities, and evidence records |
| Audit & review queues | Review queues for captured material and an audit surface |
| Media ingestion | Local OCR, ASR, PDF/Office extraction, and CLIP image indexing |
| CLI / REST | The same operation registry serves CLI, REST, and MCP tools |

Measured on a 50,000-note corpus: 864 ms hybrid find end-to-end (hot cache off), sub-10 ms keyword lanes from FTS5.

## Installation

```bash
pip install exomem
exomem --help
# extras: local embeddings, CLIP, OCR, ASR
```

Works with Claude Code, Claude Desktop, Codex, Cursor, or any MCP client. GPU is optional — the lean install has no cloud dependency.

## Configuration

Add the local server to your MCP client pointing at the `exomem` binary, with your vault folder as the knowledge base. The CLI (`kb` / `exomem`) and a personal REST facade expose the same memory for non-MCP workflows.

## Business Relevance

- **Operators with Obsidian vaults** get agent memory over files they already own — no migration into a new app.
- **Research-heavy teams** get review queues so captured material is governed before it becomes durable context.
- **Security-conscious operators** get a lean install where nothing is uploaded, ever.
- **Founders running local AI stacks** get memory that is inspectable infrastructure, not hidden assistant state.

## Integration with CorpusIQ

Exomem complements CorpusIQ's research and governance layers. Market research notes from the research intelligence framework can live in a vault the agent searches with Exomem, while CorpusIQ's canonical facts and metric specs stay the declared source of truth — Exomem's evidence and supersession records make the "declared vs observed" distinction auditable. The file-native design pairs naturally with the docs repo workflow: a memory note, a decision, and its supersession can all travel through git.

## Limitations

- Brand new — no track record yet; listing appeared August 17, 2026.
- Local-first means no built-in multi-machine sync — the vault is wherever your files are.
- Embedding extras (CLIP, OCR, ASR) add dependencies; the lean install is search-only.
- Hosted option is a friends-only private alpha with no public checkout.
- AGPL-3.0 licensing matters if you embed it in a proprietary product.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
