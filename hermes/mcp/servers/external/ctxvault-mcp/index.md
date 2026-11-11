---
title: "CtxVault MCP - Memory You Correct Instead of Overwrite"
description: "Local memory for agents as typed vaults: documents by meaning, procedures by name, and facts on two timelines. Seventeen MCP tools measured, a live supersede that closed the old statement at the exact moment the new one started, and a 5.9 GB install footprint you should know before you begin"
category: "Memory & Knowledge"
stars: "62 (GitHub, 2026-11-11)"
added: 2026-11-11
source: "the mcp.so feed card for /servers/ctxvault read 2026-11-11T10:00Z, the GitHub repository Filippo-Venturini/ctxvault, the PyPI metadata for 0.9.1 and its dependency set, the official registry record io.github.Filippo-Venturini/ctxvault 0.9.1, and a local install measured on this host: tool install footprint, initialize, tools/list, resources/list and prompts/list over stdio, plus a full episodic lifecycle run through the CLI on a throwaway vault"
relevance: ★★★
tags: [memory, agent-memory, episodic, temporal, vaults, rag, chromadb, embeddings, mcp, local-first, python]
last_updated: "2026-11-11"
---

# CtxVault MCP

**Append-only memory is a liability dressed as a feature.** The question an operator actually asks is not "what does the assistant remember", it is "what did we believe on the third, and who changed it". A vector store answers the first with a similarity search and the second with nothing. CtxVault splits memory into **vaults**, three types of them, and gives the factual type two timelines: when a statement is true in the world, and when the vault learned it.

```text
Server type:  stdio, local Python process (also HTTP and a CLI on the same vaults)
Install:      uv tool install ctxvault        executables: ctxvault, ctxvault-mcp
Server:       ctxvault 1.30.0 (serverInfo)    Package: 0.9.1 on PyPI    Protocol: 2025-06-18
Registry:     io.github.Filippo-Venturini/ctxvault 0.9.1    Licence: MIT    Python >= 3.10
Tools:        17 measured (2 vault discovery, 5 semantic, 3 skill, 7 episodic, 1 warmup)
Resources:    0   Prompts: 0   Capabilities advertise both, both empty
Footprint:    5.9 GB installed, because sentence-transformers and chromadb are hard dependencies
```

## What the three vault types are for

The README draws the distinction in cognitive-architecture terms, and it is worth restating in operator terms because it changes what you ask the assistant to do:

```text
Semantic   documents (PDF, DOCX, MD, TXT) chunked and embedded into a local index
           read by meaning: a query returns the closest chunks with their source
Skill      procedures in markdown, each with a name and a description
           read by name: the agent lists the skills and reads the one it needs
Episodic   statements with two timelines, valid_from/valid_to and known_at
           read by entity, validity and source, as of today or any past date
```

The reason to separate them is isolation. Each vault is an independent index on disk, and the config file makes that explicit:

```json
{"vaults": {"client-facts": {"type": "episodic",
                             "vault_path": ".ctxvault/vaults/client-facts",
                             "db_path": ".ctxvault/vaults/client-facts/episodes.db",
                             "restricted": false, "allowed_agents": []}}}
```

One directory, one SQLite file, one access list per vault. Isolation is a filesystem boundary rather than a metadata filter, which is why `--restricted` with an `allowed_agents` list is a real control and not a prompt instruction. A semantic vault defaults to the `all-MiniLM-L6-v2` sentence-transformer; an episodic vault builds **no vectors** unless an embedding model is named for it at init, so the episodic tier runs without an embedding cost at all.

## The seventeen tools, measured

`tools/list` returned more than the README's eleven named tools:

```text
discovery   list_vaults, warmup_status
semantic    query, list_docs, write_doc
skill       list_skills, read_skill, write_skill
episodic    write_episode, query_episodes, invalidate_episode, supersede_episode,
            revise_episode, confirm_episode, dispute_episodes, episode_history, list_entities
```

`warmup_status` exists because the embedding model loads asynchronously: the server answers before the model is ready, and a query that arrives too early fails for a reason the model needs told. That is a small tool that prevents a misdiagnosed failure, and it is the kind of thing a server only has if it was used in anger.

`query_episodes` exposes `valid_at`, `known_at`, `include_closed`, `entities`, `order_by` and `limit`. Those two timestamps are the whole product. `valid_at` asks what was true in the world on a date; `known_at` asks what the vault had already been told by a date. They are different questions and a single timestamp answers neither.

## The lifecycle, actually run

A throwaway episodic vault was created and given two statements about the same customer, one from an invoice and one from a contract amendment:

```text
Northfield Supply pays on Net 30.     source: invoice 2026-06            → open
Northfield Supply pays on Net 45.     source: contract amendment 2026-10 → open
```

**Both stayed open.** Writing the correction did not close the original, which is the first real thing to know about this design: `write_episode` appends, and a vault that is only ever appended holds a live contradiction. The listing even says so, ordering both as open records with a relevance score of 1.000.

`supersede` on the first episode then produced:

```text
Episode superseded.
  Northfield Supply pays on Net 45.
     2026-11-11T10:11:55.185259+00:00 → open
     source contract amendment 2026-10      id: cc8b4304d43e4c90b5f300e2c62f72c0

history of 581bba572d4f40839bede02375d3bd8e:
  Northfield Supply pays on Net 30.
     2026-11-11T10:11:48.122331+00:00 → closed 2026-11-11T10:11:55.185259+00:00
     source invoice 2026-06
     superseded by: cc8b4304d43e4c90b5f300e2c62f72c0
```

The old statement closed at the exact microsecond the new one opened, it kept its own source, and it points at what replaced it. Nothing was deleted, so "what did we believe before the amendment" is answerable, and "why does the vault believe Net 45" is answerable from the chain rather than from a guess.

The verbs around that are the design, and they are not synonyms:

```text
supersede   the world changed; the old statement closes where the new one starts
revise      the world did not change, the statement is now said better; keeps its attestations
invalidate  something ended and nothing replaces it; closed, not deleted
confirm     the same statement was asserted again; a repetition is recorded, not a new row
dispute     two open statements cannot both hold and you cannot tell which is wrong;
            neither is closed, so the contradiction stays visible instead of being resolved
```

`dispute` is the one that separates this from a knowledge base. Most systems resolve a conflict by keeping the newest or the most confident; this one lets the conflict stand as a fact about the evidence, which is closer to how an operator actually treats two sources that disagree.

## What the footprint costs you

`uv tool install ctxvault` installed cleanly and produced both executables, and the directory it occupies is **5.9 GB**. The dependency list explains it: `chromadb>=1.3.0` and `sentence-transformers>=5.0.0` are hard requirements, not extras, so a Linux install resolves the PyTorch stack including the CUDA runtime wheels whether or not a GPU exists. A first `uvx ctxvault mcp` run therefore spends minutes and gigabytes before the server answers. On a laptop that is a real cost; on a server with an ephemeral disk it is a reason to pin a volume.

Two version facts from the same install: the **package** is 0.9.1 while the **server** reports `ctxvault 1.30.0`, so a client logging the handshake version is not logging the package version; and `resources/list` and `prompts/list` returned zero entries with both capabilities advertised.

## Where it fits

Three uses are within the measured surface. A shared semantic vault per team, so documents are retrieved with their source instead of pasted into a prompt. A skill vault, so procedures are read by name rather than embedded and pattern-matched. And an episodic vault for the facts that change: prices, terms, owners, delivery promises, any statement whose history is worth more than its current value.

The nearest neighbours in this catalog own other halves of memory. [agentic-memory MCP](/hermes/mcp/servers/external/agentic-memory-mcp/) and [mcp-long-term-memory](/hermes/mcp/servers/external/mcp-long-term-memory/) carry conversation persistence, and [spm-structured-project-memory](/hermes/mcp/servers/external/spm-structured-project-memory/) holds project state. None of them put the correction itself in the tool list with a closing timestamp on the statement it replaces, which is the mechanic measured here.

Two limits to carry into a deployment. The five GB is permanent, not a first-run cost that disappears. And the append-versus-supersede distinction is a discipline the agent has to hold: nothing in the write path enforces it, so a memory policy that says "supersede, never re-state" has to live in the skill or the system prompt rather than in the vault.
