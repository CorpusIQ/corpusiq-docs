---
title: "MCP Server Discovery - November 11, 2026 (Early Morning)"
description: "A six-hour overnight window where mcpservers.org was flat to the entry count and the mcp.so feed delivered one scheduled batch of eight, and three"
category: MCP Ecosystem
added: 2026-11-11
last_updated: 2026-11-11
source: "the mcpservers.org sitemap index read from /sitemap.xml at 2026-11-11T10:00Z with all fifteen maps and their lastmod values, the mcp.so homepage read cache-busted and parsed card by card, the official MCP registry queried for all eight candidates, and local installs of the three catalogued servers measured on this host"
tags: ["mcp server", "model context protocol", "discovery", "sweep", "november 2026"]
---

# MCP Server Discovery - November 11, 2026 (Early Morning)

Fired on the **03:00 MST** tick, six hours after the evening sweep's read. The two surfaces disagreed in a way worth recording: **mcpservers.org was flat to the entry count**, with every one of the twelve server maps carrying exactly the number of URLs it carried at 21:00 MST, while the **mcp.so feed delivered one scheduled batch of eight cards stamped 08:00Z**. Three of those eight earned guides, and all three were installed and driven on this host rather than described from a README.

```text
Surfaces:    15 maps named, 12 carrying /servers/ URLs, 63,995 raw entries in those maps
             77,396 raw <url> entries across all fifteen maps (static 822, skills 12,579)
             20,405 distinct server keys, 18,588 carrying a lastmod
             newest lastmod 2026-11-10T23:48:14Z: 0 at or after the 04:14Z cutoff
Feed:        288,585 bytes read, 30 distinct cards, 22 timestamped, 8 above the cutoff
Queue:       not read this pass (no scripted reader for the authenticated submission list)
Catalogued:  3 servers, 3 guides
Crossref:    8 candidates, 6 with registry records, 2 without
```

## The window, measured

The sitemap index answered **200** and named **fifteen** maps again. Two of them are not server maps and were counted but not treated as servers (`static.xml` 822 entries, `skills.xml` 12,579). The remaining thirteen break down exactly as at the previous pass, and that exactness is the finding:

```text
priority    299   servers/1  7,588   servers/7   9,351
servers/2 5,948   servers/8  6,588   servers/9   4,031
servers/3 6,518   servers/10 2,604   servers/11    601
servers/4 6,744   servers/5   6,952   servers/6   6,756
remote       15                      total      63,995
```

Every per-map count above is identical to the 21:00 MST pass, which is arithmetic rather than assertion: a single arrival in any partition would have moved that partition by one. The sitemap index has not been re-partitioned and no URL was added or removed overnight.

Two numbers about the key set need care, because they are **not** a set diff. Normalising each URL to the first two path segments after `/servers/` gives **20,405** distinct keys this pass; the previous pass reported **20,411** distinct server URLs using its own normalisation, which was not retained, so the six-key difference is a method difference and is recorded as one rather than as six removals. The decisive measure for the window is the `lastmod` each entry carries: **18,588** keys carry one, the newest across all fifteen maps is **2026-11-10T23:48:14Z**, **nine** sit above 22:50Z (inside the previous pass's own read window), and **none** sits at or after the 04:14Z cutoff. Nothing was published to this surface in the 5.5 hours between the reads.

The mcp.so homepage answered **200** at **288,585** bytes and was parsed card by card rather than with a global timestamp regex, which matters: the timestamps live in the `title` attribute of the relative-time span and a naive regex pairs the wrong card with the wrong time. The page carried **32** card anchors resolving to **30** distinct slugs, **22** of them timestamped. **Eight** sat above the cutoff, and all eight carry the same stamp:

```text
2026-11-11T08:00Z   vibe-shield, usb-rea, unslop, tandoor-recipe-mcp,
                    dead-letter, ctxvault, caprock, agent-vscreen
```

One stamp on eight cards is a scheduled publish batch, not eight discoveries, and it is the same shape recorded on November 8 when an eighteen-card cohort landed with stamps four hours apart from the clock. The eight were then resolved one by one through the official registry and each was read at its source before any disposition was written:

```text
dead-letter          io.github.BigCactusLabs/dead-letter 0.4.10
ctxvault             io.github.Filippo-Venturini/ctxvault 0.9.1
vibe-shield          io.github.avivgerz-hue/vibe-shield 2.1.2
unslop               io.github.avivgerz-hue/unslop 2.1.1   and io.github.0design/unslop 0.1.0
usb-rea              io.github.emirmrkaljevic/usb-rea 0.2.1 and 0.3.0
tandoor-recipe-mcp   io.github.Cliftonz/tandoor-recipe-mcp 3.4.0 and 3.4.1
caprock              no registry record
agent-vscreen        no registry record
```

The `unslop` pair is a genuine collision rather than a duplicate: two different records under the same product name, `io.github.0design/unslop` at 0.1.0 described as a read-only canon of design rules and `io.github.avivgerz-hue/unslop` at 2.1.1 as an auditing tool. A registry search that stops at the first hit would have graded the wrong product.

## Catalogued: 3 servers, 3 guides

All three are local-first: a Python tool that runs on the operator's own files, a Node CLI that scans the code an agent wrote, and a Python memory server whose vaults are directories. None has a remote endpoint to authenticate against, so the evidence standard for this pass was inverted: instead of a handshake, each was **installed and driven**, and where a tool has a limit it is named with the run that showed it.

**[dead-letter MCP](/hermes/mcp/servers/external/dead-letter-mcp/)** converts exported `.eml` and `.mbox` mail, Gmail Takeout named explicitly, into Markdown with YAML front matter. `initialize` returned `dead-letter` **0.4.10** on protocol `2025-06-18` with `prompts`, `resources` and `tools` advertised, and `tools/list` returned exactly **five**: `convert_eml`, `convert_eml_to_bundle`, `convert_directory`, `convert_mbox` and `get_diagnostics`, the last of which is the only one annotated `readOnlyHint: true`. `resources/list` and `prompts/list` returned **zero** entries with both capabilities advertised, which is worth knowing before a client renders an empty panel. A crafted message with a duplicated plain-text part, an HTML signature table and a tracking pixel converted to **465** bytes of Markdown: one body, the signature preserved as a table, the date normalised to ISO 8601 UTC from a `-0500` header, and the tracking pixel **still present** until `--strip-tracking-pixels` was added. `--strip-signatures` did **not** remove the table-shaped signature, which is the honest limit of a delimiter heuristic. The licence decides the use case before the install does: PolyForm Noncommercial 1.0.0, "any noncommercial purpose is a permitted purpose", with no commercial licence published, so an internal pipeline at a company is outside the grant. First entry here that converts a mail archive rather than reading a mailbox: [emailmd MCP](/hermes/mcp/servers/external/emailmd-mcp/) writes outbound email and the mailbox connectors read a live account.

**[Vibe Shield MCP](/hermes/mcp/servers/external/vibe-shield-mcp/)** is a static security scanner for AI-written code with a second command that audits agent surface. On a crafted Next.js route with four defects it returned **GRADE F, 0/100, 5 critical** in **26 ms** with **80** active rules: three unguarded mutation routes, one concatenated SQL statement, one record owner taken from the request body, and one hardcoded credential that the report **redacted** in its own output. Exit codes were measured three ways on the same fixture (plain scan **1**, `--fail-on critical` **1**, `--format json` **1**) and once on a clean control (`GRADE A+`, **0**), so the gate is on by default for criticals. The score object explains its own arithmetic: `score.ceiling` is `{"severity":"critical","limit":29}`, so one critical caps any result at 29. `audit-skills` then ran a poisoned `SKILL.md` and **caught the exfiltration** (`VSB-AGENT-002`, a `curl` posting the environment to a remote host) while flagging neither "ignore all previous instructions" nor "never mention this section", which is the boundary worth publishing: across **12** agent-surface rules it detects what an instruction does, not what it asks a reader to hide. The repository is four days old with 26 stars, stated plainly because a security dependency's age is part of its risk.

**[CtxVault MCP](/hermes/mcp/servers/external/ctxvault-mcp/)** organises agent memory into typed vaults: documents by meaning, procedures by name, and statements on two timelines. `tools/list` returned **17** tools, more than the eleven the README names, including the four that make the design distinct: `supersede_episode`, `revise_episode`, `dispute_episodes` and `episode_history`. The lifecycle was run end to end on a throwaway vault. Two statements about the same customer, one from an invoice and one from a contract amendment, both stayed **open** after the second write, so an append does not correct anything by itself. `supersede` then closed the first at the exact microsecond the replacement opened, kept its own source, and recorded `superseded by` pointing at the new record, with nothing deleted. The install is the cost to plan for: `uv tool install ctxvault` produced both executables and occupies **5.9 GB**, because `sentence-transformers` and `chromadb` are hard dependencies and resolve the PyTorch stack on Linux. Two version facts from the same run: the package is **0.9.1** while the server reports `ctxvault 1.30.0`, and an episodic vault builds **no vectors** unless an embedding model is named at init. Not first of class here, but the first entry where the correction itself is a tool with a closing timestamp: the memory neighbours ([agentic-memory](/hermes/mcp/servers/external/agentic-memory-mcp/), [mcp-long-term-memory](/hermes/mcp/servers/external/mcp-long-term-memory), [spm-structured-project-memory](/hermes/mcp/servers/external/spm-structured-project-memory)) carry persistence and project state without it.

## Also identified this pass (not catalogued)

Five held, each with the reason measured rather than assumed:

- **caprock** (43 stars, Apache-2.0, Go and Tauri, no registry record): an agentic development environment that runs several coding agents side by side and follows a pull request to release with what the agents spent on it. Held on two measured grounds, not on taste: it is a desktop application with a companion plugin rather than a server an assistant can attach to, and its positioning names Gemini CLI among the four agents it hosts, which is outside the surfaces this documentation speaks to. A worthwhile tool that is not this catalog's subject.
- **unslop** (20 stars, MIT, two registry records under one name): a UI design craft audit of 72 rules across seven pillars. Held as class-owned: [CoDesign](/hermes/mcp/servers/external/codesign-mcp/) carries the editable design engine and [Design Context Bridge](/hermes/mcp/servers/external/design-context-bridge-mcp) carries Figma-to-code, so the design class has two owners and a third does not need a page. The registry collision above is recorded because it will mislead the next pass.
- **usb-rea** (MIT, registry `io.github.emirmrkaljevic/usb-rea` 0.2.1 and 0.3.0): reverse engineers a USB gadget by capturing vendor-app traffic and generating a Python driver. Held on audience rather than on quality: it is hardware reverse engineering, and no entry in this catalog serves a business operator through a USB bus.
- **tandoor-recipe-mcp** (MIT, registry 3.4.0 and 3.4.1, **306** tools, a `preview_*` sibling for every destructive delete): the most carefully built server in the batch and still a household surface. Held on subject, with one detail recorded for anyone who disagrees: it requires **Node 24** or later, where this host runs Node 22, so the install would have needed a second runtime for a recipes app.
- **agent-vscreen** (56 stars, MIT, Kotlin, no registry record): a background virtual screen for Android agents that operates apps on an invisible display while the phone stays in the user's hands, through Shizuku with no root. Held because there is nothing to measure from a server: the endpoint is `http://127.0.0.1:18765/mcp` on the device, so every claim in its README is unverified from here. It is the closest thing in this batch to a first of class, and it is held rather than dismissed: a re-check needs an Android device, not another read.

## Ops details that held

- The mcp.so timestamps are **UTC** in the `title` attribute of the relative-time span, and the card anchors must be paired with the nearest following title inside a few thousand characters. `288,585` bytes produced **32** anchors and **30** distinct slugs on this read.
- Reading `lastmod` per entry is the only window measure that survives a normalisation change between passes. The raw per-map counts are the second check: identical counts across twelve maps is proof no URL moved.
- A single `08:00Z` stamp on eight cards is a batch, not a trend, and the same shape was recorded on November 8. Treating it as eight discoveries would have produced eight guides for one publisher's schedule.
- The submission queue was **not** read this pass. It needs an authenticated chatmcp session and no scripted reader exists in this profile, so the feed and the sitemap carried the window alone. It is named here rather than silently omitted.
