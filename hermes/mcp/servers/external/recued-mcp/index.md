---
title: "Recued MCP - One Gate Between Agents and Your Accounts"
description: "A server you host yourself where each agent connects through a contract naming its tools, reads pass, and writes wait for your yes with each call recorded."
category: Security / Agent Governance
stars: 1 (GitHub, AGPL-3.0, self-hosted)
added: 2026-10-27
source: "the repository recued/recued README read at 04:00Z on 2026-10-28 with pushed_at 2026-10-27T17:54:34Z, the chatmcp/mcpso submission #6266 filed 2026-10-28T01:53:06Z naming the local endpoint at port 7717 and the contract model, and recued.com returning HTTP 200 with the install script and documentation links"
relevance: ★★★
tags: [agent-governance, approval-gate, permissions, self-hosted, pii, mail, crm, calendar, agpl, streamable-http]
last_updated: "2026-10-27"
---

# Recued MCP

**Every agent architecture in this catalog answers "what can the agent do" with a prompt. Recued answers it with a contract stored outside the agent, which is the only version of the answer that survives a prompt injection.**

```
Server type:  Self-hosted (local server plus web client)
Endpoint:     http://127.0.0.1:7717/mcp by default, or a public name
Auth:         a per-agent contract key, issued from the Recued web app
Model:        reads pass, writes and deletes wait for a human yes
Recorded:     every call, in one gate
Licence:      AGPL-3.0
Repository:   github.com/recued/recued
Reaches:      mail, calendar, files, contacts, CRM records, local CLI tools
```

## Why This Matters for Operators

The gap between a demo and a deployment is not capability, it is blast radius. An agent wired to a mailbox with one broad token can send, delete and forward to anyone, and the only control is a sentence in a system prompt. Anyone who has read an injection payload knows that sentence is not a control.

This server takes the position that permission belongs on the server side and in a named artefact. Each agent connects with a contract that lists the tools it may use. Reads run immediately because they are cheap to reason about. Writes and deletes wait for the owner's approval by default, whatever the model was told, and the call is recorded. That is the same shape as the approval bands in a payments policy, applied to mail and records instead of money.

It also holds a local copy of mail, contacts and CRM records, so reads are served locally and the model is not making a round trip per question. Before the model sees warehouse data, a PII alias step swaps names, emails, organisations, phone numbers and addresses for stand-ins, while keeping the region and which people belong to the same organisation, so the model can still reason over relationships without holding the identities. The subtext is that a self-hosted server can do this step at all, which a hosted connector cannot.

## The Parts That Are Actually Hard

Three claims in the design are worth stating plainly because most tools in this class skip them.

**Encryption at rest with a recovery key the owner holds.** A 24-word recovery key is the only way back in, which is the correct choice and also a real operational risk: lose it and the data is gone, because nobody at the vendor can reset it.

**No third party in the middle.** The server runs on the owner's machine, the AI provider is whatever the owner already pays for, and the vendor takes no cut of any transaction.

**It refuses to be things it is not.** The README says outright that Recued is not a coding agent, not a general chat app, and not a runner for `SKILL.md` files, and that it is not built for open-ended questions that take many steps over a long stretch. That last sentence is the honest one: a server whose job is to gate calls is not trying to be the agent, and an operator should wire it beside their existing assistant rather than instead of it.

## Limits Worth Recording

- **Self-hosting is the cost.** Install is one command, and after that the owner runs the server, holds backups, and holds the recovery key. That is a permanent operational task, not a one-off.
- **AGPL-3.0.** Fine to run for yourself, and a serious consideration for anyone embedding it in a product.
- **Approval fatigue is the failure mode.** A contract that lists too many write tools turns the gate into a click every minute, and the predictable outcome is an owner who approves without reading. The contract should be narrow enough that its approvals are rare.
- **PII aliasing is best effort by design.** The vendor says so. It is a reduction of exposure, not a guarantee, and the stand-ins still show region and organisational grouping.
- **No call was executed in this pass.** The endpoint only exists on an installed instance, so the evidence is the repository, the submission and the site. The approval semantics are documented behaviour, not observed.
- **New.** One star, first publication in the week of this sweep.

## Wiring It Up

```bash
curl -fsSL https://recued.com/install.sh | sh
```

Then create a contract in the Recued web app, choose the tools the agent may use, copy the key, and point the agent at `http://127.0.0.1:7717/mcp` with that key. Start with read tools only and add a write tool when a specific task needs it.

## FAQ

### How is this different from a policy in my system prompt?

The prompt travels with the request and can be argued with. The contract is held by a server the agent does not control, and the write path will not execute without an approval recorded against that contract, so an injected instruction changes what the model asks for and not what it can do.

### Which accounts can it sit in front of?

Mail, calendar, files, contacts and CRM records, plus local command-line tools, with the vendor's marketplace packs extending it. It connects to any provider rather than to one vendor's account system.

### What happens if I lose the recovery key?

The data cannot be decrypted. There is no reset path, which is the property that makes the encryption meaningful and the reason the key belongs in an offline store.

### Do I still need my own assistant?

Yes. Recued gates access and does the thinking nowhere. Claude, ChatGPT, Codex or a local model stays the model, and Recued is where that model meets the owner's data on the owner's terms.
