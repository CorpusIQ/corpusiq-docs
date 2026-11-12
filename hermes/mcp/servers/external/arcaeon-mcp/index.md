---
title: "Arcaeon MCP - A Record an Agent Cannot Rewrite"
description: "Hash-chained agent ledgers driven end to end, a tampered row named by line, a source grade of our own MCP server, and a two-sided deal verdict"
category: Compliance
stars: "1 (GitHub, 2026-11-11)"
added: 2026-11-12
source: "the mcp.so feed card for /servers/arcaeon stamped 2026-11-11T23:13Z, the official registry record io.arcaeon/arcaeon 0.10.0 published 2026-11-11T17:16:40Z, the deprecated io.arcaeon/adapter record naming where it merged, the repository Arcaeon-io/arcaeon at MIT read on main, the README's verbs, limits and exit-code tables, and a local install measured on this host: initialize, tools/list and eleven tool calls over stdio including two ledger writes, a one-word tamper, a restore, a source grade of our own MCP server, a mandate and a two-sided deal dispute"
relevance: ★★★
tags: [audit, ledger, hash-chain, agent-governance, eu-ai-act, mcp-vet, witness, evidence-pack, deal, mcp, stdio, python]
last_updated: "2026-11-12"
---

# Arcaeon MCP

**An agent can be told to keep a record, and an agent that keeps its own record can also edit its own record.** Arcaeon's answer is not a policy but a data structure: every row an agent writes is hash-chained to the row before it, so an edited row, a deleted row or two swapped rows break the chain and a check names the line. What the chain cannot catch on its own is a log cut short at the end, which is why the same package ships a pin to a hosted witness, a source grader for MCP servers, a two-sided tape for a purchase, and an evidence pack built toward the EU AI Act logging duty.

```text
Server type:  stdio, local Python process
Install:      uvx --from arcaeon --with "mcp>=2.0.0,<3" arcaeon mcp
Server:       arcaeon 0.10.0 (serverInfo), protocol 2025-06-18
Components:   arcaeon-ledger 0.8.0, mcp-vet 0.0.17, arcaeon-connector 0.10.0
Registry:     io.arcaeon/arcaeon 0.10.0, published 2026-11-11T17:16:40Z
Licence:      MIT   Repository: github.com/Arcaeon-io/arcaeon
Tools:        19 listed, 17 free, 2 paid (witness_pin, witness_renew)
Capabilities: prompts, resources, tools (all three advertised)
Probe:        initialize, tools/list and 11 calls in one stdio session, plus one tamper and one restore
```

## What the server answered

`initialize` returned `arcaeon` **0.10.0** on protocol `2025-06-18` with `prompts`, `resources` and `tools` advertised, and `tools/list` returned **nineteen** tools. Seventeen are free and need no key; the two witness tools need `ARCAEON_KEY`. `arcaeon_status` is not decoration: it reports the version of each bundled component (`arcaeon-ledger` **0.8.0**, `mcp-vet` **0.0.17**, `arcaeon-connector` **0.10.0**), the split of free and paid tools, whether a key is present, the ledger path, the `~/.mcp_vet` call-record path and the price list URL, which is how a client can find out what it will be charged before it tries.

The surface groups into four jobs rather than nineteen features:

```text
Record   ledger_append  ledger_verify  ledger_verify_peer_ledger
         ledger_prove_my_conduct  ledger_declare_break
Prove    vet_scan  vet_grade  vet_audit_verify  evidence_pack_build  evidence_pack_verify
Trade    deal_mandate  deal_commit  deal_dispute  mandate_check
Read     second_read_submit  second_read_compare
Paid     witness_pin  witness_renew           (ARCAEON_KEY)
```

## The chain, driven rather than described

Two records were appended over MCP in the session: `{"tool": "search", "query": "weather"}` returning chain `40907eee6abc75a7726c7edf7eca6ce4`, then `{"tool": "send_email", "to": "ops"}` returning `a827c5af8a1a0e8495ea84d6c127bc02`. `ledger_verify` answered:

```text
ok: true   rows: 2   chained: 2   prechain: 0   first_break: null
breaks: 0  verified_scope: "full"  declared_breaks: 0
calls_record: { ok: true, rows: 3, chained: 3, breaks: 0 }
```

That `calls_record` block is the detail worth noticing. The server keeps its own second ledger of the MCP calls it served, hash-chained the same way, at `arcaeon.calls.jsonl` beside the data ledger, with a later `vet_audit_verify` reading a third one at `~/.mcp_vet/audit.jsonl` that recorded the grading call with `rows: 1` and `chain intact`. An agent therefore has to break two chains to hide a call that was served.

One word was then changed in the first row, `weather` to `sunshine`, with the file edited outside the server:

```text
ok: false   rows: 2   chained: 2
first_break: "line 1: chain mismatch"
breaks: 1   verified_scope: "full"
```

Restoring the original bytes returned `ok: true` with `breaks: 0`, so the check reads the file rather than a cached verdict. This is the whole product in three calls, and the three-valued verdict is the second half of it: `ok: true` means every row verified, `ok: null` is COULD NOT LOOK, and the CLI maps those to exit `0`, `2` and `3`, with `1` for a bad finding. The README states the consequence plainly: **exit 3 is never a pass**, and any summary the tool prints over many logs shows how many were VERIFIED, how many BROKEN and how many COULD NOT LOOK, never one rate, because "98 percent verified" hides whether the other 2 were broken or simply never read.

## It grades an MCP server by reading it, and said something unflattering about ours

`vet_grade` takes a path and reads the bytes. Pointed at one of our own Python MCP servers on this host it returned `source_sha256` `a8bdaba8bcf442b3f7617ace7dec4e41ecc95b8c3617555d1f9be29443a86e1d`, nine checks (`unsafe-exec`, `unsafe-deser`, `ssrf`, `path-traversal`, `zero-auth`, `secret-in-code`, `audit-record`, `unreceipted-allow`, `except-returns-success`) and two findings:

```text
unsafe-exec  high    line 105  subprocess.run(..., shell=True) - shell injection surface
audit-record medium  line 118  records a call; gate 2 (completeness) unmet:
                               missing tool name, timestamp, args/input digest
                               gates: presence true, completeness false,
                                      tamper_evidence true, reconstructability false
```

Both are correct about that file. The audit finding is the one that matters here, because it separates "there is a log line" from "the log line would survive an audit": the presence gate passed and the completeness gate failed on exactly the fields an investigator needs. The report also ships its own blind spots in the artifact rather than a score alone. The first one says the battery reads bytes and never sends the server any, that when they measured their own published packages three died outright on a single line of invalid UTF-8 arriving on stdin and several more answered hostile input with silence, and that this grader read every one of those servers as clean and would again.

## A purchase with two tapes, and a verdict at commit one

`deal_mandate` recorded a buyer's authority (`acme-supply`, up to `500.00` USD) and returned mandate digest `sha256:json-c14n:v1:37ea6a58318a8d5e000c9e0b59cd90600e49bbd626e63ffd22f3ce4142f4a7ef` with the scope read back as `acme-supply, up to 500.00 USD`. Two commits were then written, deliberately disagreeing: the buyer's at `39.00` and the seller's at `41.00`, the classic two-dollar gap. `deal_dispute` over the two files answered:

```text
verdict: ALTERED
at: commit#1
reason: mandate_digest mismatch; commit #1 differs between the tapes
        in mandate_digest, terms.total (buyer row 2, seller row 1)
counts: buyer 2, seller 1
```

The verdict names the step, the side and the field, and it also records what it cannot see: `MATCHED` would have meant two recorders agreed, not that either told the truth, and a call that crossed neither instrumented seam leaves no row on either tape.

The same three-valued logic showed up unprompted. `second_read_compare` pointed at two ledgers where one did not exist returned `COULD NOT LOOK` with exit `3` and a `fraction_reason` reading `ledger a (readings.jsonl) does not exist`, rather than a 0 percent agreement that would read as a finding. `second_read_submit` also refuses to file a reading without a `claim_id`, which is a schema fact worth knowing before wiring it.

## One package where there were thirteen, and what that broke

Before 0.9 this was thirteen packages (`arcaeon-ledger`, `arcaeon-adapter`, `arcaeon-receipt`, `arcaeon-audit`, `arcaeon-mcp-vet`, `arcaeon-once`, `arcaeon-compact`, `arcaeon-continuity`, `arcaeon-baseline`, `arcaeon-dedup`, `arcaeon-distill`, `arcaeon-meter`, `arcaeon-all`). Each old name gets one last release that installs `arcaeon` and keeps the old import working with a warning, and `MIGRATION.md` lists every moved exit code with `--legacy-exit` as the bridge for a gate wired to the old numbers.

Two registry consequences are recorded because they cost time in any migration. The `io.arcaeon/adapter` record now reads **deprecated** with the message `Merged into io.arcaeon/arcaeon (pip install arcaeon; server: arcaeon mcp)`. And the README carries a note addressed to registry listings: before 0.9 `uvx arcaeon` started the server, it still does for 30 days when no verb is given and stdin is not a terminal, and the fallback is removed in 1.0.0, so the command to write down is `arcaeon mcp`. The earlier guide in this catalog, [Arcaeon Ledger MCP](/hermes/mcp/servers/external/arcaeon-ledger-mcp/), documents the pip-installable ledger as it stood in August; this page is the consolidated package, and the ledger is now one verb among many.

## What it proves, and the five things it says it does not

The limits section is unusually specific and belongs here rather than in a footnote. Tamper-evident is not tamper-proof: anyone who can write the file can change it, they just cannot do it without the check naming the line. The hosted witness at `witness.arcaeon.io` is operated by the same people who make the package, so a pin is not an unrelated second party, and who operated the witness at the time of a given pin is unknown to an outside reader until a custody record is published. The daily anchor is a clock, not a party: it fixes when pins existed and says nothing about whether they were right. Truncation is caught only by a pin, never by the chain. Truth and authorship are not proven at all, since the chain records whatever was written and a full rewrite from row one carries its own author field.

The write envelope is honest about cost: each row is flushed and synced before the next, about **18 ms** a row, so 102,000 rows took roughly 22 minutes, while reading is fast, with a 50 MB log verified in about 2.5 seconds. `evidence_pack_build` and `evidence_pack_verify` turn one agent and one time window into a folder with a manifest that rehashes file by file, which is the shape an auditor can be handed; `ledger_verify_peer_ledger` does the same for a JSONL tape another agent sends you, and `ledger_declare_break` exists so an agent whose ledger was written into out of band can name the break instead of hiding it.

## Where it fits

This is the entry in the catalog that answers a question a compliance officer asks and most logging tools dodge: **what exactly can you prove about what the agent did, and what can I check without trusting you.** A hash chain answers "was this record edited after the fact". A pin answers "was it cut short". A source grade answers "does this server look wrong before we connect it". A two-sided deal tape answers "did we both record the same purchase". None of them answer "is it true", the vendor says so in its own README, and that boundary is precisely why the page is useful: it tells an operator what a defensible record looks like, and where the defensibility stops.

The nearest neighbours here solve different halves. [AgentKeyGate](/hermes/mcp/servers/external/agentkeygate-mcp/) controls which credential an agent may use and logs the use, and this records what the agent did in a form a third party can check. [AnythingMCP](/hermes/mcp/servers/external/anythingmcp/) gates a company's systems behind one endpoint with permissions, and Arcaeon sits beside it as the evidence trail rather than the door.
