---
title: "MCP Server Discovery - November 20, 2026 (Supplement)"
description: "An hour in which the directory did not move, the feed carried one card and the queue one arrival, and both turned into guides."
category: "MCP Ecosystem"
last_updated: "2026-11-20"
---

# MCP Server Discovery - November 20, 2026 (Midday Supplement)

Fired on the **11:00 MST** tick, one hour after the midday sweep closed at **17:42Z**. The directory came back identical to that pass's capture on every reading, so the whole window is one feed card and one queue arrival, and both of them earned a guide: the first cloud dev VM surface in this catalog and the first tool whose job is showing a human what an agent changed.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, sixteen maps named, TWELVE numbered server maps
raw <loc>, maps 1-12          66,963   against 66,963 at the 17:01Z midday capture  (0)
  servers/1  ..... 7,588     servers/7  ..... 9,351     sums to 66,963 exactly
  servers/2  ..... 5,949     servers/8  ..... 6,590
  servers/3  ..... 6,518     servers/9  ..... 4,022
  servers/4  ..... 6,746     servers/10 ..... 2,608
  servers/5  ..... 6,954     servers/11 ..... 2,638
  servers/6  ..... 6,756     servers/12 ..... 1,243
priority-servers.xml          299 raw,  34 distinct keys
remote-mcp-servers.xml         15 raw
distinct rows, deduped        67,277   IDENTICAL to the midday capture
key additions / removals      0 / 0
lastmod rows at or after the cutoff   0
mcp.so /feed                  200, 157,974 bytes, 34 anchors, 30 stamps
                              ONE card above the cutoff, shipped
submission queue              #7724 only, body read in one authenticated call
```

The flat reading is the strong form, not a count: both captures were written to disk, the row count matches at **67,277**, the set diff returns nothing in either direction, and the newest `lastmod` on the surface still predates **17:00Z**. Three independent readings agree that no product arrived on this surface, so the window's material came entirely from the two push surfaces.

`/all` was not re-read: **403** by edge policy, the standing condition since 4 November.

## The feed, and the queue

The mcp.so feed answered **200** at **157,974** bytes with **34** anchors, **30** stamps and exactly **one** card above the cutoff:

```text
homemade                  servers   18:01Z
```

The submission queue carried one arrival inside the hour, **#7724**, filed **17:23:06Z**. The entry below it, **#7723** (NotePorter), was filed at **16:50:47Z** and is already dispositioned in the midday sweep, so it was not re-triaged.

One mechanic is worth carrying forward: this pass read the mcp.so detail page for `homemade` with a **direct** request and a browser user agent, and it answered **200** at **79,740** bytes. The midday sweep had recorded `r.jina.ai` answering **401 bad IP reputation** on every detail page it tried, so the reader proxy being refused is not the same as the detail route being unreadable. Try the direct route first, and keep the proxy as the fallback rather than the first move.

## Catalogued, with guides

### Homemade - cloud dev VMs with the coding agent signed in

[Guide](/hermes/mcp/servers/external/homemade-mcp/) - remote Streamable HTTP at `https://api.homemade.dev/mcp`, submitted by the founder and marked *Verified* and *Featured* on its mcp.so card.

The product is a Linux VM per project, started from a repository with dependencies installed and services running, a preview URL for every port, and Claude Code, Codex, OpenCode, pi, Kimi and Grok installed and signed in inside the machine. The MCP surface is claimed as one tool per public API operation, and the vendor's own OpenAPI **3.1.0** document is the checked form of that claim: **28** paths, **41** operations, six families, with the VM family carrying **17** of them including `execVm`, `sendToAgent` and the sleep and wake pair.

Authentication is measured to the document level and no further: an anonymous `initialize` answers **401** with a complete challenge naming `resource_metadata` and the scopes `api offline_access`, both protected-resource routes answer **200** and agree, and the issuer document offers authorization code with **PKCE S256**, dynamic registration, `client_credentials` and refresh. A Bearer API key is the second accepted path, and the refusal body names both. **No tool was called**, because neither path can be completed from this host, and the guide says so rather than implying a drive.

Pricing was reproduced from the vendor's own rate table: nano at **$0.012** an hour is **$8.76** always on, and the large size at **$0.18** is **$131.40**, every figure matching the page's own column at **730** hours. The free Hobby tier is **25** computer-hours a month on nano or tiny only; Pro is **$20** with **$20** of running time included. The vendor's `llms.txt` names the non-fits too: no GPU, Linux only, not for thousands of short snippets a second, no self-hosted deployment.

**A name collision to record:** the official registry's `homemade` is an unrelated Israeli lunch service (`com.homemade-global/homemade`, website `homemade-global.com`). Three searches for this product returned zero registry records, so the cloud-VM vendor is unlisted there.

The distinct slice against the catalog's existing sandbox entry is the hosted coding agent and the preview URL, not the microVM primitive.

### Revue - the agent opens its own diff, and annotates it

[Guide](/hermes/mcp/servers/external/revue-mcp/) - local stdio, a single MIT-licensed Rust binary, queue entry **#7724**.

The catalog had no owner for the review step itself: the git-adjacent entries act on repositories over an API, and none of them shows a human what changed. Revue does that from the agent's side. Ten tools, all driven on a synthetic three-line repository in this pass: `revue_changes` returned **1 file(s) changed, +7 -2**; `revue_diff` returned the unified diff itself; `revue_definitions` on `subtotal` returned `* billing.py:1 function def subtotal(items):`; `revue_show` returned a fragment URL encoding the mode, file, view and line; `revue_annotate` created note **586f4478** on `billing.py:8-9`, `revue_annotations` listed it with the client name as author and then cleared it; `revue_status` reported the port, pid, lifetime, note storage and open-tab count; `revue_open` and `revue_stop` answered in the same shape. The viewer answered **200** at **10,092** bytes.

Three refusals were recorded as measurements rather than smoothed over: a missing path and a `../../etc/passwd` traversal both refused with the repository boundary and the relative-path convention in one line, and two wrong argument names (this pass's own vocabulary, `identifier` and `note`) refused with the accepted set named, so the retry succeeded first time.

Two limits are worth carrying: the binary must live on the machine the agent runs on because the server binds `127.0.0.1` with no hosted endpoint, and the `Browser: opened a new tab` line is printed even on a host with no display and no browser, so it is an intent line and not a success receipt. The project is three weeks old, created **2026-11-03** with **0** stars and a first release on **2026-11-18**; the guide carries that date rather than presenting the tool as established.

## Held or carried, and why

Nothing else arrived in the hour, so no new hold was needed. Carried from the midday sweep without re-triage: its eight unresolved feed cards, which the direct-route mechanic above may resolve in a later pass, and its **27** dispositions. Carried from the queue: **#7723** NotePorter, a macOS-only stdio app with nothing drivable from a Linux host.

## Counts

```text
canonical      66,963 against 66,963          0 raw, 0 keys, 0 lastmod rows
feed           157,974 bytes, 1 card above the cutoff, 1 shipped
queue          1 arrival, 1 shipped
catalogued     2, both with guides
held           0 new
guide tree     1,224 to 1,226 directories
hermes/mcp     1,681 to 1,684 Markdown files
```
