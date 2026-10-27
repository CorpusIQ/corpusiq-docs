---
title: "fynk MCP - Contract Lifecycle Management for Agents"
description: "fynk MCP runs the contract lifecycle from chat: draft from templates or PDFs, set parties and signatories, approve, sign and archive."
category: Productivity
stars: 0
added: 2026-10-20
source: "mcp.so /feed page 1 (card posted 2026-10-20T15:45:49Z)"
relevance: ★★★
tags: [legal, contract-management, clm, e-signature, document-automation, remote-mcp, oauth, compliance]
last_updated: "2026-10-24"
---

# fynk MCP

**Most contract tools stop at reading. This one moves the document through its lifecycle, and the agent never reaches further than the user's own role already allows.**

```
Server type: Remote (Streamable HTTP) at https://app.fynk.com/mcp
Auth: OAuth 2.0 against fynk's EU infrastructure; the connection inherits the signing-in user's role and document permissions
Live check: POST initialize returned HTTP 401 {"message":"Unauthenticated."} (unauthenticated probe, this sweep)
Tools: the mcp.so tool listing enumerates 68; the vendor integration page advertises 47 and its help centre says the set is still expanding, so treat the count as a floor
Plans: Essential, Business and Pro, testable in the free trial, no add-on
Vendor: fynk (fynk.com), contract management software, EU-hosted
```

## Why This Matters for Operators

Every other record a business owns has a system of record. Contracts rarely do. The signed PDF lands in a shared drive or an inbox, the renewal date lives in someone's head, and the clause that limits liability sits on page 34 of a file nobody reopens until there is a dispute. The cost is not the paperwork, it is that the business cannot answer basic questions about its own commitments without a person reading files.

The reason contract data stays dark is structural: a contract is prose, and prose was not queryable until models could read it reliably. Once an agent can read the portfolio, the useful questions become ordinary. What renews before March. Which counterparties have unlimited liability. Where did we agree to 30-day payment. Those are structure questions wearing a prose costume.

fynk's contribution is that the agent does not stop at the answer. It has tools to create the next document, fill the fields, name the parties, and put it in front of a signatory, so the answer and the action live in one conversation.

## What It Actually Does

The tool surface covers the full lifecycle rather than a read-only slice:

- **Documents**: list with filters, read one in detail, pull the latest signed PDF, create from a template, from scratch, or from an uploaded PDF, copy an existing document, archive and restore.
- **Templates**: create and edit the ProseMirror body, add parties, dynamic fields and signature blocks, publish and unpublish, copy a template for another jurisdiction.
- **Parties and signatories**: account parties (your own entities) and external counterparties are distinct objects, with signatories attached per party.
- **Workflow**: move a document through draft, review, signing and done, with `workflow_state` reporting every blocker standing in the way, including who still has to approve.
- **Governance**: playbooks for automated review against predefined criteria, checkpoints that gate a stage transition, teams, tags, custom document types and metadata fields, all agent-readable so the account's own vocabulary is discoverable before it is filtered on.
- **Signing**: start signing, add or remove signatories, follow signing progress to the completion stage.

The design detail worth calling out is that fynk's own AI analyses are configurable by the agent: a custom document type or metadata field carries a `prompt` that decides whether future analyses fill it in, and the tool descriptions push the agent to write that prompt at creation time rather than leaving a field that no analysis will ever populate.

## What It Cannot Do

The connection is a pass-through of the user's own permissions. There is no elevated path for MCP, and an action the role does not allow returns a plain permission denied. The vendor is explicit that this cuts both ways: the agent can write, so the guardrail is the human confirmation step in the workflow, not a read-only boundary.

Data handling is worth stating plainly. OAuth runs against EU infrastructure under fynk's GDPR terms, but the contract content travels into whichever AI client is connected, and what that provider does with it is governed by your agreement with that provider, not by fynk. The vendor also lists share links and starting approval workflows through MCP as in progress, so those two actions may still need the fynk interface.

## FAQ

### Is this just an e-signature tool with a chat wrapper?

No. The e-signature step is one stage of a lifecycle that starts at a template or an imported PDF and continues through parties, dynamic fields, review checkpoints, approval, signing and archive. E-signature servers in this catalog send a document you already wrote; this one writes and then advances it.

### Can it answer questions about contracts we signed years ago?

That is the part that pays for itself. The portfolio is searchable and each document reports its parties, dynamic fields, metadata values, tags and timestamps, so questions about renewal dates, contract values and clauses are answered from the record rather than re-read from a file. Import an existing PDF and fynk analyses it into the same structure.

### What stops the agent sending something it should not?

Two things. The account's checkpoints and approval steps gate stage transitions, and every action lands in the audit trail under the user's name. Permission boundaries stop what the role does not allow; the workflow stops what the role allows but the process does not.

### Do we need the vendor's AI analysis to be switched on?

No. AI analysis fills metadata automatically, but everything it produces can also be set explicitly through the tools, and a field with no prompt simply stays manual.

## See Also

- [PandaDoc MCP - Document Automation and E-Signatures](/hermes/mcp/servers/external/)
- [Binderwork MCP - Startup Paperwork and SAFE Rounds](/hermes/mcp/servers/external/binderwork-mcp)
- [Legalcode MCP](/hermes/mcp/servers/external/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
