---
title: "Poison Armor MCP: Prompt-Injection Firewall for AI Agents"
description: "Open-source MCP security firewall that intercepts indirect prompt injection, zero-width Unicode steganography, adversarial GCG suffixes, tracking pixels, Markdown XSS, semantic dataset poisoning and Sybil consensus attacks before they reach the LLM. Ships as a local FastMCP server with sanitize_document and scan_dataset_for_anomalies tools plus SKILL.md behavioral directives. MIT licensed."
category: Security
stars: n/a (new listing)
added: 2026-08-24
source: mcpservers.org /all page 3
relevance: ★★★
tags: [security, prompt-injection, firewall, sanitization, rag, sybil-defense, fastmcp]
---

# Poison Armor MCP

**An open-source MCP security firewall that sanitizes documents, web pages, and RAG data before they reach the LLM.** Universal Poison Armor is a production-grade defense framework combining native agentic behavioral directives (a SKILL.md) with a high-performance local FastMCP server. It targets indirect prompt injection, zero-width Unicode steganography, adversarial suffixes (GCG attacks), tracking pixels and Markdown XSS, semantic dataset poisoning, and Consensus Poisoning or Sybil attacks, with deterministic rule checks plus optional LLM-assisted semantic scoring.

```
Server type: stdio (local FastMCP server, Python 3.9+)
Auth: None (runs locally on your data)
Install: pip install universal-poison-armor (or uvx)
Repo: github.com/mzaid007/universal-poison-armor (MIT, Aug 2026)
Tools: 2 core MCP tools (sanitize_document, scan_dataset_for_anomalies) plus SKILL.md behavioral directives
```

## Why This Matters for Operators

Every operator wiring an agent into email, Slack, web research, or a RAG pipeline over company documents is one poisoned attachment or prompt-injected web page away from data exfiltration or prompt override. Poison Armor puts a filter in front of the model: strip tracking pixels, neutralize hidden instructions, detect zero-width steganography, and flag poisoned rows in fine-tuning or RAG datasets. For teams running customer-facing or document-grounded agents, that is a compliance control with an audit trail, not a hope.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `sanitize_document` | Neutralizes indirect prompt injections, tracking pixels, Markdown XSS, hidden zero-width Unicode content, and adversarial suffix payloads in a document before it reaches the model |
| `scan_dataset_for_anomalies` | Scans a dataset for semantic poisoning, consensus poisoning, and Sybil attack patterns, with anomaly scoring per record |

The accompanying SKILL.md layer adds the behavioral directives: treat instructions found inside retrieved content as data, re-verify tool calls, and refuse credentials appearing in web content. Multi-layer defense architecture covers tracking pixel and Markdown XSS neutralization, deterministic payload detection, semantic anomaly scoring, and dataset poisoning defense, with self-check rounds for LLM-assisted evaluation.

## Installation

```bash
pip install universal-poison-armor
# or
uvx universal-poison-armor
```

Add it to any MCP client as a stdio server and place it in front of retrieval and ingestion steps so every document and dataset passes through the sanitizer first.

## Configuration

No API keys and no external calls for the deterministic checks; the LLM-assisted semantic scoring layers can be configured with your model provider. Because the server runs locally, sensitive documents never leave the machine during sanitization. The SKILL.md can be loaded directly into Claude Code or any agent that supports skill directives.

## Example Prompts

- "Sanitize this vendor PDF before summarizing it: strip tracking pixels and any embedded instructions."
- "Scan this scraped web page for hidden prompt injections and zero-width Unicode."
- "Run scan_dataset_for_anomalies on our RAG corpus and flag records with poisoning signatures."
- "Show me the audit trail for what was removed and why before I send this to the model."

## Business Relevance

- **Operators running agent workflows over email and Slack** block prompt-injection payloads before they reach the model
- **Teams with RAG pipelines over company documents** detect poisoned records and Sybil content in the corpus
- **Security-conscious orgs** get deterministic, on-prem sanitization with no third-party data egress
- **Agent builders** harden customer-facing deployments against indirect injection without building a filter in-house

## Integration with CorpusIQ

CorpusIQ's own MCP surface is read-only and OAuth-gated, but operators commonly pipe third-party content into the agents that answer questions alongside CorpusIQ data. Poison Armor sits in front of that ingestion: sanitize the vendor PDF, web page, or support ticket first, then let the agent correlate it with revenue, customer, and contract data from CorpusIQ. Security from Poison Armor, business truth from CorpusIQ, with the sanitization audit trail preserved.

## Limitations

- New open-source project (Aug 2026, zero stars at listing time); the framework is young and should be evaluated against your threat model.
- Local stdio server means the protection covers clients that route content through it, not every agent by default.
- The LLM-assisted semantic scoring layers require a model provider and add latency on large documents.
- Not a replacement for prompt-injection defense in the model or platform itself; defense in depth still applies.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external) - curated third-party MCP servers for operators
- [GLC PromptGuard MCP](/docs/hermes/mcp/servers/external/glc-promptguard-mcp) - prompt security guardrails for agent pipelines
- [Routara LLM Gateway MCP](/docs/hermes/mcp/servers/external/routara-llm-gateway-mcp) - governed LLM gateway routing
- [Sanctions Screening MCP](/docs/hermes/mcp/servers/external/sanctions-screening-mcp) - compliance screening for counterparties
