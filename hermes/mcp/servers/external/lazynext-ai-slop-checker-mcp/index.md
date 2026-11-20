---
title: "Lazynext AI Slop Checker MCP - 279 Rules, Score 0-100"
description: "A deterministic scanner that scores AI-slop writing and design tells from 0 to 100, names all 279 rules and returns a fix per match. Keyless."
category: "Content Quality / AI Governance"
stars: "n/a (hosted endpoint; product code lives in a public MIT monorepo)"
added: 2026-11-20
source: "the mcp.so submission queue entry #7687 filed 2026-11-20T05:29:26Z and its mcp.so listing page, a keyless initialize and full tools/list on 2026-11-20, eight driven tools/call requests (list_rules, three scan_text, one scan_html, one rewrite_text, one judge, one empty-input probe) with a repeat call proving determinism, npm registry @lazynext/ai-slop-checker 1.4.4 created 2026-11-19T07:41:35Z, and the vendor page fetched to HTTP 200"
relevance: ★★★
tags: [content-quality, ai-detection, copywriting, design-review, linting, deterministic, remote, keyless, no-auth, free-tier]
last_updated: "2026-11-20"
---

# Lazynext AI Slop Checker MCP

**Everyone now ships copy that was written by a model, and most of it reads the same. This server turns that complaint into a number with a rule id and a fix against every hit, and it answers without a key.**

```text
Server type:   remote Streamable HTTP, stateless (no Mcp-Session-Id issued)
Endpoint:      https://slop-checker.lazynext.com/mcp
Server:        lazynext-ai-slop-checker 1.4.4, negotiated protocol 2025-03-26
Registry:      no record under com.lazynext for this product (see the registry note below)
Package:       @lazynext/ai-slop-checker 1.4.4 on npm, created 2026-11-19T07:41:35Z
Vendor page:   https://slop-checker.lazynext.com (HTTP 200, 11,067 bytes)
Auth:          none. A free hosted tier; the vendor states the scanner runs offline with no LLM
Tools:         7, all keyless
```

## What the server is

The product is a lint pass for prose and for interface markup. `list_rules` returns a fixed corpus of **279 rules across 27 categories**, each rule carrying an id, a severity from 1 to 3, a match kind (`word`, `phrase`, `regex`), the offending pattern and a fix written in plain language. The categories are the argument:

```text
word-ban            filler-phrases     business-jargon    throat-clearing
faux-insight        binary-contrast    colon-reveal       importance-puffery
weasel-attribution  fake-strong-verb   adverb-overuse     rhetorical-setup
negative-listing    dramatic-fragment  summary-recap      em-dash
superficial-analysis meta-commentary   vague-declarative  false-agency
passive-voice       design-color       design-type        design-copy
design-component    design-motion      design-layout
```

Sixteen of those categories are about sentences that announce instead of saying, six are about interface defaults (gradient text, kicker labels, stat rows, glassmorphism, marquees), and one is a rule against em-dashes.

## The seven tools

| Tool | Input | What comes back |
|---|---|---|
| `list_rules` | none | the full corpus: 279 rules with id, category, severity, kind, match, fix |
| `scan_text` | `text`, optional `rewrite`, `profile` (`default` / `strict` / `lenient`) | score 0 to 100, verdict, per-category points, every match with context and a fix |
| `scan_html` | `html`, optional `profile` | the text rules plus the design rules, run over markup |
| `scan_project` | `dir`, optional `topFiles`, `profile` | a pooled report over a directory tree, prose and markup and code lenses |
| `scan_render` | `snapshot` or `url` | the rendered-tier checks: kicker size, gradient text, tracked caps, marquee, fold budget |
| `rewrite_text` | `text` | conservative whole-word and phrase swaps only, plus the change list |
| `judge` | `text`, `html` or `dir` | the 5-question review, the craft floor, refusal scaffolds and a machine verdict |

Verdict bands as measured: **clean** at 0, then **light**, then **moderate**. A score is points-weighted, not a match count, so one severity-3 phrase can weigh more than three severity-1 words.

## Runs, measured on 2026-11-20

**Clean copy scores zero, and it is not a lenient zero.** A four-sentence factual paragraph with numbers in it came back `score 0`, `verdict clean`, `totalPoints 0`, `matches []`.

**Slop scores immediately, and the same text scores the same twice.** A 165-character paragraph of marketing filler returned **37 / 100, moderate, 13 points, 6 matches** on two consecutive calls, which is the determinism claim verified rather than repeated. A longer five-sentence version (518 characters) returned **59 / 100, moderate, 25 points, 13 matches** spread across five categories (8 word-ban, 2 filler-phrase, 1 business-jargon, 1 adverb-overuse, 1 summary-recap); a different 130-character paragraph of filler under `profile strict` returned **47 / 100, 18 points**.

Every match carries a fix written for a human, not a linter code:

```text
w-cutting-edge  severity 3  "State what is new about it, concretely."
w-leverage      severity 2  "Use 'use', 'build on', or 'take advantage of' with a concrete subject."
w-unlock        severity 2  "State what becomes possible."
w-delve         severity 2  "Use 'explore', 'examine', or simply 'look into' - or state what you actually did."
f-lets-dive     severity 2  "Start the next section; you don't need the handshake."
```

**The rewrite is deliberately timid.** `rewrite_text` on a 300-character slice made **four** swaps (`leverage` to `use`, `unlock` to `enable`, `seamless` to `smooth`, `navigate` to `handle`) and left `cutting-edge`, `paradigm shift` and the `It's not X; it's Y` construction in place. It is a synonym pass, not an editor, so a team that ships the rewritten output unchanged still ships most of the tells.

**The design tier reads markup, not screenshots.** A 206-byte section with a kicker label, a gradient-text headline and a stat row returned **13 / 100, light, 4 points** and flagged two things: the word `Unlock`, and the CSS tell itself, `-webkit-background-clip:text`, with the fix "Solid color; build hierarchy with size and weight."

**The judgement layer separates machine facts from human steps.** `judge` on the 112-character filler paragraph returned:

```text
summary.verdict          REVIEW
summary.reasons          ["copy objections: 6 AI-dialect tell(s) in the copy"]
machineChecked           floorItemsTotal 6, floorFlagged 0, floorOk 0, floorUnchecked 6,
                         objections 6, copyTells 6, designTells 0
humanStepsRequired       true
```

That is unusually honest for a scoring tool: contrast and alignment cannot be measured from text, so all six craft-floor items come back `unchecked` on a text scan and the tool says so in its own note. The consequence is the useful part - on text input the floor can never be *cleared*, so a REFUSE cannot be argued away by a passing score.

## Where it stops

- **`scan_project` and a `dir` argument are local-only by nature.** This is a hosted endpoint, so a path in `scan_project` or `judge` points at the *server's* filesystem, not the caller's. Run the npm package locally (`npx @lazynext/ai-slop-checker`) or the browser page for a folder scan; do not hand a path to the remote endpoint and expect your own tree back.
- **An empty document passes.** `scan_text` with `text: ""` returned `score 0`, `verdict clean`. There is no minimum-length guard, so a pre-publish gate wired to this score alone will wave through a blank file. Check length before the score.
- **No `instructions` block.** The `initialize` response carries the server name and version and nothing else, so the tool descriptions are the whole contract.
- **Protocol negotiated down to 2025-03-26** while the request offered 2025-06-18. Nothing in this surface needs the newer revision, but a client that assumes output schemas should note that none are published.
- **Registry note.** A registry search for `lazynext` returns one record, `com.lazynext/accessibility-checker` 1.0.0, a different product from the same publisher. The slop checker is discoverable through the feed, the npm package and its own page, not through a registry record under its own name.
- **The class is not empty, only uncatalogued.** The official registry carries three other slop-score entries (`app.vercel.slopcheck-one/slopcheck`, `com.clawhard/slopscore`, `com.cleanslop/cleanslop`). None of them publishes a rule corpus, which is what makes this one worth a guide rather than a hold.

## Add it to Hermes

```bash
hermes mcp add slopcheck --url https://slop-checker.lazynext.com/mcp
hermes mcp test slopcheck
```

Then ask it the question it is built for: *score this landing page copy and give me the fixes in priority order.* The output is a list a writer can act on, with rule ids that survive the next rewrite, which is what a style guide needs to stay enforced after the person who wrote it moves on.

## Why it earns a slot

A content team's real failure is not that one page reads like a model. It is that the same twelve phrases reappear in every page, and nobody can point at them fast enough to stop it. This server makes the list finite - 279 named patterns, a score that moves when the copy moves, and a fix beside every hit - and it does it deterministically, offline and free, which means it can sit in a pre-publish step rather than in a review meeting.
