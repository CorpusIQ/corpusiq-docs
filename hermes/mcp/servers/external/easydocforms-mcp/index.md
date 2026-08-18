---
title: "easydocforms MCP - CorpusIQ Docs"
description: Healthcare intake forms over MCP — the agent hands patients a hosted fill link and retrieves completed PDFs without PHI ever entering agent context
category: Document Intelligence
stars: n/a (new listing)
added: 2026-08-13
source: mcp.so
relevance: ★★
tags: [healthcare, forms, document-processing, pdf, phi-safe, self-hosted]
---

# easydocforms MCP

**MCP server for healthcare intake forms (Docker, API key) built on the EasyDocForms platform.** The agent imports a blank PDF, hands the patient a hosted fill link, and retrieves the completed PDF — while protected health information never enters the agent's context. The design constraint is the product: the AI orchestrates the paperwork without ever holding the sensitive data.

```
Server type: Self-hosted (Docker container)
Auth: API key (EASYDOCFORMS_API_KEY)
Endpoint: ghcr.io/easydocforms/easydocforms-mcp:latest
Tools: Live tool list served from the endpoint (see caveat below)
Pricing: EasyDocForms platform plans
Category: Document Intelligence / Healthcare
Built by: EasyDocForms (easydocforms.com) — MIT
```

## Why This Matters for Operators

Every clinic runs the same manual loop: blank intake form out, patient fills it in the waiting room, staff retypes it into the system. easydocforms collapses that into three agent steps — import the blank PDF, hand the patient a hosted fill link, retrieve the completed PDF. The patient fills on their phone; the agent files the result.

**The PHI-minimization model is the differentiator.** The hosted fill link keeps patient data out of the conversation entirely, and the `external_ref` field is an opaque correlation id — your visit or order number — that must never carry PHI. The agent coordinates paperwork without becoming a data holder, which is the architecture HIPAA-conscious operators have been asking MCP vendors for.

## Workflow

> ⚠️ This is a brand-new listing — mcp.so shows "No tools detected" (the live tool list is served from the endpoint). The documented workflow, from the maintainer's README:

1. **Import** — load a blank PDF template to convert it into a hosted fill form
2. **Hand off** — the patient receives the hosted fill link and completes it on any device
3. **Retrieve** — the agent pulls the completed PDF back for filing or review

The container's `external_ref` correlation id is the only link between your system and the form — it must never contain PHI.

## Installation

```bash
docker run -i --rm -e EASYDOCFORMS_API_KEY=edfk_live_... ghcr.io/easydocforms/easydocforms-mcp:latest
```

Or point any MCP client at the published Docker config. Source: `github.com/easydocforms/easydocforms-mcp` (MIT).

## Configuration

```json
{
  "mcpServers": {
    "easydocforms-mcp": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-e", "EASYDOCFORMS_API_KEY=edfk_live_...", "ghcr.io/easydocforms/easydocforms-mcp:latest"]
    }
  }
}
```

## Business Relevance

- **Clinic managers** cut the retype loop — intake PDFs arrive completed and filed without staff transcription
- **Practice operators** run onboarding paperwork through the agent while keeping PHI out of chat logs and model context
- **Healthcare SaaS builders** get a hosted fill-and-retrieve primitive they can embed in agent workflows instead of building their own
- **Compliance-minded operators** get a design where the agent coordinates but never holds patient data — audit-friendlier than screenshot-and-transcribe workflows

## Integration with CorpusIQ

easydocforms pairs naturally with CorpusIQ's document-intelligence and CRM connectors. A composed workflow: the agent retrieves the completed intake PDF, CorpusIQ's document connectors structure it into fields, and the HubSpot or CRM connector records the patient record and follow-up task — while the raw PHI stays in the form platform's storage, not in the agent transcript.

The philosophy matches CorpusIQ's own read-only external-source retrieval model: the agent orchestrates, the platform holds the sensitive data, and the operator stays in control of every system of record.

## Limitations

- Brand new — no track record yet (submitted to mcp.so Aug 13, 2026)
- Live tool list not yet published on the directory; verify tool names against the endpoint before building
- Docker-based — needs a container host or Docker Desktop running locally
- Healthcare-specific; little value outside intake/forms workflows
- MIT license covers the server code, but the EasyDocForms platform itself is commercial

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
