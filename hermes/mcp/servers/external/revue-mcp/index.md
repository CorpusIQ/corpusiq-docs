---
title: "Revue MCP - Agent-Opened Git Diffs in Your Browser"
description: "A local binary that opens an agent's uncommitted changes in a browser and pins an annotation to the exact line."
category: "Development / Code Review"
stars: "0 (github.com/jmsheas3/revue, created 2026-11-03, v0.3.0)"
added: 2026-11-20
source: "the mcp.so submission queue entry #7724 filed 2026-11-20T17:23:06Z, the v0.3.0 Linux ARM64 release asset verified against the vendor SHA256SUMS (4c6f2783...), and a driven stdio session on 2026-11-20 covering initialize, the full tools/list of ten tools, eight tools/call requests, three refusal paths and the served viewer page"
relevance: ★★
tags: [git, diff, code-review, coding-agents, browser-ui, local, stdio, mit, rust]
last_updated: "2026-11-20"
---

# Revue MCP

**Every coding agent ends the same way: a wall of diff in a terminal, and a human scrolling it. This server gives the agent a second verb, which is to open the change in a browser, point at a line and leave a note there.**

```text
Server type:   local stdio, built into the same binary as the viewer
Binary:        revue 0.3.0 (55e7bd9), MIT, Rust, single static file
Install:       unpack the release tarball for the platform, run `revue mcp`
Auth:          none; it reads the local git repository it is started in
Tools:         10, all driven in this pass
Network:       binds 127.0.0.1 only; nothing leaves the machine
```

## What the server is

Revue is a git change viewer that runs as a local web app, plus an MCP server in the same binary. The `initialize` instructions state the job from the agent's side, and the wording is the design:

> revue is a git change viewer in the user's browser. When the user asks to see, show or review code changes ("show me the changes", "what did you change?", "let me see the diff", "review this branch"), open them in revue with revue_open instead of printing a diff in the chat.

That last clause is the whole idea. The tool does not summarise a diff into a chat message; it moves the conversation into a view where the line is visible and an annotation can sit under it.

## The ten tools

| Tool | What it does, measured |
|---|---|
| `revue_open` | opens the overview of all changes, returns the URL and the server line |
| `revue_show` | shows a file, optionally at `line` / `endLine`, in diff or whole-file view |
| `revue_annotate` | leaves a note on a line or range, and moves the tab to it |
| `revue_annotations` | lists or clears notes, per view or across views |
| `revue_changes` | changed files with status and line counts, as text |
| `revue_diff` | unified diff of one file or all changed files, as text |
| `revue_log` | recent commits |
| `revue_definitions` | where an identifier is defined (the Ctrl+click search) |
| `revue_status` | running servers, port, lifetime, note storage, open tabs |
| `revue_stop` | stops a server this MCP started |

Every view-dependent tool takes the same view arguments (`mode` of `working`, `commit` or `branch`, plus `ref` / `base` / `head`), so an agent can review uncommitted work, one commit, or a branch against its base without checking anything out.

## Driven: eight calls in a real repository

The session ran in a three-line Python repo with one modified file (`billing.py`, **+7 -2**) and no other changes.

**`revue_changes`** answers in one line of prose plus a stat line:

```text
1 file(s) changed, +7 -2 (working tree vs HEAD). Status: M modified, A added, D deleted, R renamed, C copied, U untracked.
M  billing.py  +7 -2
```

**`revue_diff`** returns the unified diff itself, hunk header intact, plus a trailing blank line: the tool gives the agent text, not a picture of text.

**`revue_definitions`** with `name: "subtotal"` returns `* billing.py:1  function  def subtotal(items):`, which is the definition site at the revision the view shows rather than in the working copy only.

**`revue_show`** with `path: billing.py`, `line: 8` returns a URL with the view, file and line encoded in the fragment:

```text
revue for /tmp/revue-demo
URL: http://127.0.0.1:37383/#mode=working&file=billing.py&view=file&line=8
Server: reused (session, port 37383)
Browser: opened a new tab
```

**`revue_annotate`** on `billing.py:8-9` with `text` returned `Added note 586f4478 on billing.py:8-9 (working tree vs HEAD; stored in file)`, and `revue_annotations` then listed it with the author taken from the client name:

```text
1 note(s) in working tree vs HEAD, stored in file:
[586f4478] billing.py:8-9 by probe
    Agent note: check the rounding order here.
```

`revue_annotations` with `action: clear`, `all: true` removed it and the next list read `No notes in working tree vs HEAD of /tmp/revue-demo.` The notes are held per view and per repository, and with `--notes file` they persist to `.git/revue/notes.json`, which git never commits; the file was present after the call and read `[]` once cleared.

**`revue_status`** reported the server line an operator needs when more than one is running:

```text
/tmp/revue-demo
  port 37383, pid 2118617, session, notes in file, 0 tab(s) open (0 can follow navigation), 0 note(s)
```

`revue_open` and `revue_stop` both answered in the same shape; stop printed `Stopped the revue server for /tmp/revue-demo (port 37383).`

The viewer itself answered **200** at **10,092** bytes with the title `revue`, a single-page shell that loads its state from the same server.

## Refusals that name the fix

Two path refusals were exact and both stayed inside the repository boundary:

```text
nope.py            -> nope.py is not in this view of the repo (paths are relative to /tmp/revue-demo)
../../etc/passwd   -> ../../etc/passwd is not in this view of the repo (paths are relative to /tmp/revue-demo)
```

Traversal outside the repo is refused by the same message that explains the relative-path convention, which is the useful shape: the caller learns both the rule and the fix.

Two argument errors, caused by this pass's own wrong vocabulary, were equally explicit:

```text
unknown argument "identifier" (revue_definitions takes: name, path, side, repo, git, mode, ref, base, head, persist)
unknown argument "note" (revue_annotate takes: path, line, endLine, text, side, author, show, ...)
```

The prose calls it an identifier and a note; the schema calls it `name` and `text`. The error names the accepted set, so the correction is one retry, and both retries succeeded.

## Limits worth recording

- **Local only, by design.** The binary must exist on the machine the agent runs on, and the server binds `127.0.0.1`. There is no hosted endpoint, so this is not a remote MCP surface and cannot be reached from another host.
- **`Browser: opened a new tab` is not evidence a tab opened.** On this host there is no `DISPLAY` and no browser, and the tool still printed that line. Treat it as an intent line, not a success receipt; the URL on the line above is the reliable part.
- **Requires git and a 2024-or-later browser.** The vendor states Chrome or Edge **123**, Firefox **121**, Safari **17.5**, and that the Windows build is experimental.
- **No file is written into the repository** except optionally `.git/revue/notes.json`, and the vendor states changes to files only happen when a branch is checked out from the UI.
- **The repo is young.** Created **2026-11-03**, **0** stars, and **three** releases in two weeks: **v0.1.0** on **2026-11-06**, **v0.2.0** on **11-07**, **v0.3.0** on **11-18**. The tool contract is complete and the refusals are disciplined, but this is a three-week-old project and the guide should be read with that date attached.

## Install, verified

The release assets are listed with a `SHA256SUMS` file, and the ARM64 asset this host needs matches it:

```text
4c6f278346ab69bdd44521928522664304a8ded5d40cc23336f35e2504ef0ede  revue-linux-arm64.tar.gz
```

Download, verify, unpack, and place the binary on `PATH`; then register it with the client:

```json
{
  "mcpServers": {
    "revue": { "command": "revue", "args": ["mcp"] }
  }
}
```

Claude Code takes `claude mcp add revue -- revue mcp` (or `-s user` for every project), and `--notes file` after `mcp` makes annotations survive a restart.

## Why it earns a place in this catalog

This is the first entry whose job is **showing a human what an agent changed**, rather than reading or writing a repository through an API. The catalog's git-adjacent entries (GitHub MCP and Giteasy, catalogued in the external index) act on repositories over an API; revue acts on the review step itself. For an operator running coding agents, that is the missing half of the loop: the agent finishes, and the change is still just text until someone looks at it.

**Disclosure:** the tools were driven on a synthetic three-line repository created for the test, so the diff, the note and the refusal paths are real measurements, and the repository contents are not a customer's.
