---
title: Silvertongue MCP - Writing Voices With Sources
description: "Keyless MCP server serving studied writing voices as VOICE.md resources, plus a packet builder for format, length and intensity, with release digests."
category: Content & Writing
stars: n/a (new listing)
added: 2026-10-29
source: "mcp.so GitHub issue #6416"
relevance: ★★
tags: [writing, content, copywriting, voice, prompts, resources, keyless, remote-mcp]
last_updated: "2026-10-29"
---

# Silvertongue MCP

**An open catalogue of writing styles, versioned and sourced, that an agent can adopt for one post and drop for the next - with every voice's research linked rather than implied.**

Silvertongue runs at `https://mcp.silvertongue.dev/mcp` over Streamable HTTP, keyless and free. A bare `initialize` answered **HTTP 200** as `silvertongue` version **0.1.2** with tools, resources and prompts capabilities. `resources/list` returned **27 `VOICE.md` documents** of about 3 to 4 KB each, and `tools/list` returned four tools.

```
Server type: Remote (Streamable HTTP)
Auth: none (free, read-only)
Endpoint: https://mcp.silvertongue.dev/mcp
Tools: 4
Resources: 27 VOICE.md profiles
Prompt: write_as
Registry identity: dev.silvertongue/silvertongue@0.1.0
Built by: Silvertongue (auscaster.com); repo github.com/auscaster/silvertongue
```

## Why This Matters for Operators

"Write it in my voice" is the request every content workflow starts with and almost none of them satisfy, because the input is a sample paragraph and the output is a generic impression of energy. The root cause is that style is a set of decisions - sentence length, what gets cut, how a claim is introduced, when a number replaces an adjective - and a sample does not state which decision it is showing.

This server turns style into a studied, citable artifact: each voice documents what was read, what the observations were, a handwritten example, its strengths and its limits. That makes the output reviewable. When a draft reads wrong, the argument is about a rule in a document rather than about taste.

The second decision is provenance. Every response carries a `release_id` digest, so a voice pinned in one campaign can be reproduced after the catalogue moves. `get_changes` compares the IDs an agent has cached against the current release and reports which voices were added, re-studied as a new edition, or removed.

## Tools and Capabilities

| Tool | What it does |
|---|---|
| `search_voices` | Find a voice by name, by lane, or by what the writing should do - a roast, a launch post, a plain explanation, a speech |
| `get_voice` | The full profile: VOICE.md, every source studied with a note on what it shows, the observations drawn, a handwritten example, licence and attribution |
| `get_voice_packet` | Instructions for writing in one voice at a format, length, platform, intensity and edge, carrying the full VOICE.md and an exact length target fitted to the platform's limit |
| `get_changes` | Diff cached voice IDs against the current release: added, re-studied, removed |

Lanes are `tech`, `celebrity`, `comedy`, `classics` and `politicians`. Each `VOICE.md` is also exposed as a resource, so a client can read a profile without a tool call. The `write_as` prompt switches the conversation to one voice in a single step.

The packet is the piece that makes this practical for operators. It carries the rules that keep the user's own facts and identity intact, and it opens with a line that replaces any earlier voice, so a post can be written in one style and the next in another without the conversation dragging the first one along.

## What to Watch

The server states its own limit plainly: profiles are **unofficial studies of public writing technique**, and the people named did not write or endorse them. That is the correct framing and it should stay the framing in any published use. A marketing team adopting a named-public-figure voice for outbound content is making a brand and legal decision, not a stylistic one, and a voice that imitates a living person's public persona carries risks that a plain instruction like "write plainly, cut the adjectives" does not.

Licensing splits by asset: the code is Apache-2.0, the voice profiles are CC BY 4.0, which requires attribution when a profile is reused.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [All sweep reports](/hermes/mcp/sweeps/)

## FAQ

### What is Silvertongue MCP?

A hosted, keyless, read-only MCP server serving an open catalogue of studied writing voices, so an agent can find a voice, read how it was researched, and write a draft in it with the user's own model.

### Does it need an API key or an account?

No. The endpoint answered `initialize` with HTTP 200 without credentials, and all four tools are read-only.

### How many voices does it carry?

Twenty-seven `VOICE.md` profiles were listed as resources at the time of this pass, across the tech, celebrity, comedy, classics and politicians lanes, plus a `write_as` prompt and a packet builder.

### Can the output stay reproducible after the catalogue changes?

Yes. Every response carries a `release_id` digest that pins the catalogue release, and `get_changes` reports additions, new editions and removals against the IDs an agent has cached.

### Can I use a named person's voice in my marketing?

The profiles are unofficial studies of public writing technique and the people named did not write or endorse them. Reusing a profile requires CC BY 4.0 attribution, and imitating a living person's persona for outbound content is a brand and legal decision rather than a formatting choice.
