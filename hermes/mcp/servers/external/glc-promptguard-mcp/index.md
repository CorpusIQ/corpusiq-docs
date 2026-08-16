---
title: glc PromptGuard MCP
description: Source-aware prompt-injection gate for user prompts, RAG chunks, and tool outputs — intent-aware scoring before anything reaches the model
category: Security
stars: n/a (new listing)
added: 2026-08-13
source: mcpservers.org
relevance: ★★
tags: [prompt-injection, security, guardrails, rag, llm-security, injection-detection, remote-mcp]
---

# glc PromptGuard MCP

**Remote MCP server (Streamable HTTP, bearer token) — an eight-layer, source-aware security gate that checks user prompts, RAG chunks, and tool outputs before they reach the main model or agent tool loop.** PromptGuard evaluates intent × source context × impact rather than keyword matching, and returns a typed verdict: `injection: true|false` plus score, intent, policy, and an optional spotlight explaining what triggered the flag.

```
Server type: Remote (Streamable HTTP)
Auth: Bearer token — agents self-register for an auto-approved token
Endpoint: https://mcp.glc-rag.hu/mcp
Tools: 2 (promptguard_check, canary probe)
Pricing: Credit-based per check
Category: Security / LLM Guardrails
Built by: glc-rag.hu (service version 0.3.26)
```

## Why This Matters for Operators

The injection risk in agent stacks is not hypothetical — it is the number one failure mode operators cite when agents touch production data. PromptGuard's design answers the part most tools miss: context matters. The same text is treated differently depending on where it came from — `user_prompt`, `rag_chunk`, or `tool_result` each switches the policy, because a snippet pulled from a document you are grounding on is a different threat than a prompt typed by an external user.

**The placement rule is the architecture.** The maintainer is explicit: the host must call `promptguard_check` before every main LLM call — never via the model's own tool-choice. That keeps the guard outside the model's reach, which is what makes it a guard instead of a suggestion. A secondary canary probe tests whether tools are being hijacked.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `promptguard_check` | Check one untrusted text delta for prompt injection (intent + source + impact). Returns `injection: true|false`, score, intent, policy, optional spotlight. Inputs: `text` (the new delta, not full history), `context` (user_prompt / rag_chunk / tool_result), optional `locale` for audit logging. |
| `canary` | Secondary tool-hijack probe — verifies tools are not being redirected or abused |

The classifier is multilingual; the `locale` field is for audit logging only and does not switch models or rules. Degraded-path behavior is explicit: on classifier timeout or missing key, the gate returns a structural result rather than failing open silently.

## Installation

```bash
claude mcp add --transport http promptguard https://mcp.glc-rag.hu/mcp
```

Self-register as an agent at `mcp.glc-rag.hu/guide/agent` with `account_type=agent` for an auto-approved token. Markdown guides: `mcp.glc-rag.hu/guide/promptguard.md`, methodology at `mcp.glc-rag.hu/guide/promptguard-methodology.md`.

## Configuration

```json
{
  "mcpServers": {
    "promptguard": {
      "url": "https://mcp.glc-rag.hu/mcp",
      "headers": {
        "Authorization": "Bearer mcp_YOUR_TOKEN"
      }
    }
  }
}
```

## Business Relevance

- **Operators running agents on customer-submitted text** gate every inbound prompt before it reaches the model
- **RAG pipeline owners** check chunks at retrieval time — the `rag_chunk` context catches poisoned documents before they ground an answer
- **Teams wiring tools into production agents** verify tool outputs on the way back in, closing the indirect-injection path
- **Security leads** get typed verdicts with intent and policy fields, not a probability score to interpret

## Integration with CorpusIQ

PromptGuard is the guard layer for the CorpusIQ data plane. A composed workflow: an operator's agent grounds answers on CorpusIQ connector data (QuickBooks, HubSpot, Stripe), and PromptGuard screens both the user's prompt and any RAG chunks from external documents before the model sees them. CorpusIQ's read-only external-source retrieval model already limits what data can be exfiltrated; PromptGuard limits what a malicious prompt can make the model do with the data it does see.

For agent builders offering CorpusIQ-powered assistants to their own users, the pair is the standard sandwich: scoped data access underneath, injection gate on top.

## Limitations

- New service (v0.3.26) — young, single-vendor, small footprint
- Credit-based pricing; checks cost credits even on degraded structural paths
- Host-side integration required — the guard only works if your orchestrator calls it before every LLM call
- The maintainer is explicit it is "not 100% security" — host must still gate tools
- Hungarian-hosted service (glc-rag.hu) — review data-residency fit for regulated workloads

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
