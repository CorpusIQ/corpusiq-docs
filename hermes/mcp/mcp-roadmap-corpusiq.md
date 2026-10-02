---
title: "MCP Roadmap and CorpusIQ: Protocol Direction Explained"
description: "The new MCP roadmap prioritizes progressive discovery, tool result contracts, agent identity, and stateless servers. CorpusIQ shipped these patterns first. What each priority area means for governed business answers."
canonical: "/hermes/mcp/mcp-roadmap-corpusiq/"
robots: "index, follow"
tags: [mcp, roadmap, progressive-discovery, stateless, agent-identity, answerspec, governance]
last_updated: "2026-08-22"
---

# MCP Roadmap and CorpusIQ

The Model Context Protocol team publishes a roadmap that sets the direction
for protocol work. The updated roadmap (August 2026) organizes the work into
five priority areas. Several of them describe patterns CorpusIQ already
shipped. This page maps each priority area to the CorpusIQ implementation.

## Progressive discovery

The roadmap states that connecting to a server with a hundred tools means the
model pays for the entire surface before the user asks a single question, and
tool selection gets worse as the list grows. The protocol is starting a
progressive discovery effort so a server can offer a small entry point and
reveal more of its catalog as the conversation narrows.

CorpusIQ ships this pattern today. A single model-facing entry point resolves
the question into a governed workflow, and the tool surface is revealed
incrementally. The model makes one decision; CorpusIQ does the routing.

## Tool result contracts

The roadmap identifies that a tool call response can carry the same output in
more than one form, and a server developer has no way to know which form a
client will put in front of the model. The goal is to standardize one clear
contract.

CorpusIQ already defines a single output contract for business answers: the
AnswerSpec. Every answer carries the reconciliation summary, the pinned metric
definitions, the evidence chain, and the canonical text. One schema, one
contract, every client.

## Stateless servers

The 2026-07-28 specification release removed protocol-level sessions and the
initialization handshake. Servers can now scale horizontally without holding
state.

CorpusIQ builds on this: answers are self-contained. The rendered result is a
direct function of the verified tool result, so the same question renders the
same answer on any host, after any refresh, without session memory.

## Agent identity and enterprise security

The roadmap prioritizes standardized agent identity: DPoP proof of possession,
workload identity federation, and standard token exchange, so servers can
trust agents that act on behalf of users who are not present.

CorpusIQ connects to this direction with per-connector read-only OAuth, scoped
per-account access, and control-plane tooling that never touches customer
systems. The roadmap direction and the CorpusIQ security posture converge on
the same principle: an agent is a first-class identity with scoped authority.

## What this means

The protocol is standardizing the patterns CorpusIQ built first. That is the
strongest possible validation of the architecture: the single entry point,
the one output contract, stateless rendering, and agent identity are becoming
protocol primitives, and CorpusIQ ships them today for governed business
answers.

## Related pages

- [MCP Apps: Interactive UIs](/hermes/mcp/mcp-apps-interactive-ui)
- [MCP Apps Stateless Design Pattern](/hermes/mcp/mcp-apps-stateless-design)
- [ask_corpusiq: deterministic single-tool access](/hermes/mcp/ask-corpusiq)
- [MCP 2026-07-28 Spec](/hermes/mcp/mcp-spec-2026-07-28)
