---
title: "lookfirst MCP - Human Approval Gate for Agent Writes"
description: "Local MCP proxy that holds each write until a named human approves the exact arguments, verifies it by read-back, masks account data, and logs a signed hash chain."
category: Security
stars: 0 (Apache-2.0, github.com/Aethelgard-Systems/lookfirst, pre-1.0)
added: 2026-11-04
source: "mcpservers.org /all newest page slug aethelgard-systems/lookfirst read through the r.jina.ai reader, plus a locally driven session: installed from github.com/Aethelgard-Systems/lookfirst into a venv, version 0.2.1, and the offline demo run end to end twice (one denial, one approval) with verify-log OK at 20 signed entries and TAMPERED detected after an entry was rewritten"
relevance: ★★★
tags: [agent-governance, human-approval, audit-log, hash-chain, read-back-verification, data-masking, mcp-proxy, apache-2.0]
last_updated: "2026-11-04"
---

# lookfirst MCP

**The question every operator asks about an agent that can write is not whether it is smart, it is what happens when it is wrong. A gate that asks "approve?" is not enough either, because the agent can answer its own prompt and the person clicking yes can be shown a summary the agent wrote.** lookfirst sits between the client and the upstream tools and answers three smaller questions instead: is this call allowed by a rule, does a named human approve these exact arguments, and did the write actually land the way it claimed.

```
Server type: Local MCP proxy (stdio, or HTTP on loopback)
Install:     pipx install git+https://github.com/Aethelgard-Systems/lookfirst
Version:     0.2.1 installed (the README still says 0.2.0 pre-1.0)
License:     Apache-2.0
Repo:        github.com/Aethelgard-Systems/lookfirst (0 stars, pushed 2026-11-05)
Commands:    serve, keygen, verify-log, check, pilot-status, demo
Clients:     Claude Desktop, Claude Code, Gemini CLI, Antigravity
Config:      lookfirst.yaml (upstreams, rules, confirmation, audit, schleuse)
```

The surface was **driven locally, not quoted**: the package was installed from the repository into a fresh virtual environment, reported `lookfirst 0.2.1` to `--version`, and the offline demo was run twice end to end, once ending in a denial and once in an approval. The demo stands up a fake bank MCP server, puts the gate in front of it and plays an agent. Both runs exited **0**.

## How a call is decided

The rule table is short and it fails closed, which is the whole point:

| Situation | Default | Why |
| --- | --- | --- |
| tool declares `readOnlyHint: true` | **allow** | reading is harmless |
| tool declares `destructiveHint: true` | **confirm** | a human decides |
| `destructiveHint: false` (a write, but reversible) | **confirm** | still a write |
| no annotations | **confirm** | unknown means ask |
| explicit `rules.tools.<name>.action` | that | rules beat annotations; `deny` never executes |

Driven in the demo, a read-only `kontostand` call passed through with `gate: allowed`, and the write `ueberweisung` stopped for a decision before anything moved.

## The approval is bound to the arguments, and a timeout is a denial

Three confirmation channels are tried in order. **Elicitation** inside the client, if the client supports it and the arguments fit inside 800 characters; a **local web page**; or a **webhook**. The webhook path is the one worth reading carefully: it receives the preview and answers on `POST /decision/<id>` with a **per-call token** that is an HMAC of the call id, so a leaked token opens nothing else, and it must echo the `args_sha256` from the preview. A missing or different hash returns **403**, so a decision applies only to the exact arguments that were shown. The web page binds its buttons the same way. Every channel shares one timeout, and **a timeout is a denial**.

The decision is logged with who made it, as `channel:actor`: `web:<user>` from an authenticating reverse-proxy header, `webhook:<actor>` from the decision body, or `elicitation:<client>` from the client's own name. In the approval run the gate returned:

```
{"status": "executed", "id": "tw-30bbf0da56147705",
 "approved_by": "elicitation:mcp", "readback": "ok",
 "readback_detail": "read-back matches", "blocked": false}
```

and the balance moved from **1,250.00 EUR to 1,129.50 EUR** for a **120.50 EUR** transfer, which is the read-back agreeing with the write. In the denial run the same tool returned `"status": "denied"` with the reason naming the channel that failed, and the balance stayed at **1,250.00 EUR**.

## Read-back: a write is never reported as done on its own word

`rules.tools.<name>.readback` names a reading tool and the fields to compare, using `$args.x` and `$result.y` placeholders. The result comes back as `ok`, `unklar` (could not verify) or `fehlgeschlagen` (mismatch) inside `structuredContent.lookfirst`. The audit log shows the sequence that makes this checkable rather than decorative: `execution_started` marked `unklar`, then `result` marked `ok`, then `readback` marked `ok` with `read-back matches`, then `execution_resolved`.

## The log is a signed hash chain, and the demo proves it detects an edit

`lookfirst keygen` creates an Ed25519 signing key once, mode 0600, and every decision, execution and read-back is appended to a JSONL log with a hash chain over it. `lookfirst verify-log` walked the approval run to **OK, 20 signed and chained entries**. The demo then rewrites the decision entry so it looks as if no human ever approved, and the same command returns **TAMPERED: line 6, hash mismatch (entry modified)**.

The documented weakness is worth stating because the vendor states it: if the log is truncated at the end **and** the `.head` sidecar is deleted, the remaining chain still looks intact and `verify-log` exits 0 with a warning. The answer is `--trusted-head /protected/audit.head`, an external signed checkpoint kept outside the write access of whoever could truncate the log; a missing or forged checkpoint fails with exit 2.

## The privacy filter changes what the model is allowed to see

The `schleuse` block masks values on the way back to the client. In the demo the agent received:

```
2026-10-20 -89.90 EUR [[NAME_5f082d9345d7db2a9a0690d2eaf3cd7b]] [[IBAN_c30e2f3ca94c03562ae517ce97e88685]]
```

The model only ever sees the placeholder. Passing it back in a later call works, because the gate resolves it internally, and an invented placeholder is refused: **"Denied: unknown or expired placeholder [[IBAN_000000]]"**. Recognised shapes include IBANs (checksum-validated, and invalid-looking ones masked too), card numbers by Luhn, e-mails, phone numbers, and credentials with a known shape (GitHub, OpenAI, Anthropic, AWS, Slack, Stripe, Hugging Face, Google keys, JWTs, private keys), plus values under keys such as `password`, `token` and `api_key` in structured results.

The vendor's own limit is the important sentence: this is a deterministic pattern filter, so an IBAN split by a line break, text with zero-width characters, or a secret that is only Base64-encoded in free text is **not** recognised, and `db_password` and `access_token` are pinned as known gaps. It reduces leakage; it does not anonymise.

## Limits, stated by the vendor and confirmed here

- **Not a production release.** The README says so directly: 0.2.0 pre-1.0, no long-term field experience, real use needs your own tests and sign-off. The installed version reports **0.2.1**.
- **An autonomous client can approve itself through elicitation.** If the client auto-answers, the approval is the agent's. The fix is `confirm.elicitation: false` so only the web page or webhook can approve, **and** keeping the agent off that page at the network level: a separate OS user is not enough, because every local user reaches loopback.
- **The web page has no login.** It trusts only requests whose `Host` is this server and that are not cross-site, plus a per-process CSRF token, and it is meant for `127.0.0.1` only.
- **HTTP transport does not identify the caller.** Without `http.token_file` it only starts on loopback, and every local process can call tools; with it, each request needs a bearer token. The token is authentication, not encryption: beyond the local host you need TLS or another protected transport in front.
- **The gate cannot cover other routes to the same system,** or same-user access to the keys and the rules file.
- Windows is untested. The repository is three weeks old with **0 stars**, one vendor, and no independent users, so the code is the evidence, not a track record.

## Where it sits in this catalogue

The neighbours measure and isolate; this one decides and records. [kosa8](/hermes/mcp/servers/external/kosa8-mcp/) runs each tool server in its own microVM and pins tool definitions against change, which is the right answer to a host that runs somebody else's program. TrustScan inspects one server or skill, AgentTrust returns one endpoint decision and glc PromptGuard scores one prompt or tool output, all of which judge a thing before it runs. **None of them stops a specific write at the argument level, names the human who approved it, verifies the result by reading it back, and keeps a chain you can point at in a dispute.** That combination is the gap this entry fills, and it is the same question a business asks of its own agents in finance, procurement and support.

## FAQ

### Does it need an account or a key?

No. It runs locally, signs with a key you generate, and calls upstream servers with the credentials you already configured.

### What happens if nobody answers a confirmation?

The call is denied. A timeout is a denial on every channel.

### Can it approve from Slack or a phone?

The webhook channel is the path: it receives the preview and answers with a per-call token and the argument hash, so any receiver you build can carry the decision, provided it shows the escaped display fields rather than the raw arguments.

### Can an agent edit the log to hide a decision?

The demo does exactly that and `verify-log` reports the line and the mismatch. The residual case is end-truncation plus deletion of the sidecar, closed by an external `--trusted-head` checkpoint.
