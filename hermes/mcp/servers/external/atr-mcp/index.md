---
title: "ATR MCP - A Proxy That Cuts Tool Tokens"
description: "Sits between the assistant and its MCP servers, hides the tool list, shrinks large results and keeps the full copy so any part can be read again."
category: DevOps
stars: ★ (PyPI 1.0.0, MIT, local stdio, vendor benchmarks only)
added: 2026-10-28
source: "PyPI package atr-mcp 1.0.0 plus the repository JacobBhatt12/atr README (pushed 2026-10-28T21:53:49Z, 1 star at read) and chatmcp/mcpso issue #6332, with the savings figures quoted from the vendor's own benchmark tables and not reproduced here"
relevance: ★★
tags: [token-reduction, context, mcp-proxy, tool-search, local, pypi, mit, stdio]
last_updated: "2026-10-28"
---

# ATR MCP

**Every tool an assistant is given is billed on every message, whether it uses it or not. Ten MCP servers is a fixed cost before the first word is typed.**

```
Server type: Local (stdio), a proxy in front of your other MCP servers
Install:     pip install atr-mcp, then atr setup
Auth:        None, runs on your own machine
Tools:       4 core (find, read, call, query) plus 6 file and shell tools
Licence:     MIT, registry io.github.JacobBhatt12/atr
Cost:        Free
```

## Why This Matters for Operators

Token cost is not a pricing complaint, it is a context-window problem. The tool schemas of a handful of servers occupy the start of every conversation, and a tool result like a thousand issues or a test log occupies the middle, so the space left for the actual question shrinks twice before anyone answers.

ATR attacks both. The assistant is given four small tools instead of every schema and searches for the tool it needs at the moment it needs it, and results pass through a shrinker that keeps errors, failing tests and changed code lines while dropping the passing and the unchanged. The full result is stashed, so `atr_query` can page back into what was cut, which is the difference between a summary and a lossy filter.

It is catalogued because it is the only entry in this catalogue that sits between the assistant and its other servers rather than exposing a new data source, and because the token saving is a measurable operational number rather than a vendor adjective.

## What It Returns, Verified

`atr-mcp` **1.0.0** is on PyPI as an MCP proxy that hides tool lists and shrinks tool results, lives at `github.com/JacobBhatt12/atr` under MIT, and registers as `io.github.JacobBhatt12/atr`. The package is local stdio with no hosted endpoint, so what could be verified here is the package, the repository and the published design rather than a live `tools/list`.

The four core tools are `atr_find_tools` (searches all connected servers and returns the few that fit), `atr_read` (runs a read-only tool and shrinks the result), `atr_call` (runs a tool that changes something and can be gated by approval) and `atr_query` (reads more of a result that was cut, one page, one field or one search). Six file and shell tools sit beside them: `atr_repo_map`, `atr_search_code`, `atr_read_file`, `atr_diff`, `atr_run` and `atr_stats`.

The savings below are the vendor's own numbers, measured with their benchmark script, and are recorded as claims with the honest column kept: 1,000 GitHub issues from 429,203 tokens to 879, a 2,000-line server log from 61,072 to 208, a `git diff` with a lockfile change from 22,294 to 207, a browser page from 12,023 to 4,046, fifty tools' instructions from 12,056 to 1,508, a 303-test pytest run from 6,685 to 675, and a 60-package `pip install` from 5,977 to 697. In a live Claude Code browser task the vendor reports $0.237 to $0.110 per task, 54 percent cheaper across three runs each. On Codex the same test came back **mixed**: 84k tokens became 134k in total, while full-price tokens fell from 33k to 18k.

## Limits Worth Recording

Version 1.0.0, one week old at the time of this entry, one repository star, and every saving figure comes from the vendor's own benchmark rather than an independent run, which is why the mixed Codex result is quoted alongside the good ones. It cannot help with what an MCP server never sees: the conversation history and the assistant's own replies are outside its reach, and the vendor says so. Installing it rewrites the MCP configuration of the apps on the machine, which is why `atr setup` prints the plan first, keeps a `.atr-backup` copy of every file it touches and offers `--undo`. The safety model is explicit: secrets including `.env` files, private keys and credential JSON are never read or shown, read and change tools are separated, shell commands always ask, and file tools only see configured folders.

## FAQ

### Does it need an API key or an account?
No. It runs locally, is free, and MIT licensed.

### How much does it actually save?
The vendor measures 87.5 percent off the tool-schema cost of fifty tools and between 66 and 99.8 percent off single large results, with a 54 percent cheaper live Claude Code task. On Codex their own test was mixed, with fewer full-price tokens but more tokens overall.

### Do I lose the data it removes?
No. Shrunk results are stashed in full and `atr_query` reads any page, field or search back out of the same result.

### Which assistants does it work with?
The vendor documents Claude Code, Codex, Claude Desktop, Cursor, Windsurf, claude.ai and ChatGPT, with `atr setup` wiring the local apps it finds after showing what it will change.

### How is this different from asking a vendor to expose fewer tools?
It applies to servers you do not control. Any MCP server behind the proxy gets the same treatment without the vendor changing anything.
