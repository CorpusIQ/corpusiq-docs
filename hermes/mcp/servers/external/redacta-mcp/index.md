---
title: "Redacta MCP - Clinical Pseudonymisation for AI Agents"
description: "Pseudonymises patient identifiers in clinical documents before AI processing, with a reversal map kept on your side of the boundary."
category: Compliance
stars: 9
added: 2026-09-29
source: mcpservers.org
relevance: ★★★
tags: [pii, pseudonymisation, healthcare, hipaa, gdpr, privacy, clinical, self-hosted]
---

# Redacta MCP

**Clinical documents pseudonymised before AI ever sees them.** Redacta replaces patient identifiers with labelled tokens - `[PATIENT_NAME_1]`, `[NHS_NUMBER_1]`, `[DATE_OF_BIRTH_1]` - while leaving clinical meaning intact, and returns a redaction report alongside the cleaned text. The token map stays on your machine, so identifiers can be restored locally after the AI step. Redact, process, re-identify: identifiers never cross the boundary.

```
Server type: Local stdio (npm), plus self-hosted HTTP service on Kubernetes
Auth: None (local); OAuth not required
Endpoint: npx -y redacta-mcp
Tools: deterministic pattern layer, reasoning pass, self-check, reinstate (re-identification), Safe Harbor mode
Pricing: Free (MIT-0); fixed-price design-partner integrations for production teams
Category: Compliance
Built by: PharmaTools.AI (github.com/nickjlamb/redacta)
```

## Why This Matters for Operators

Healthcare and clinical operators are adopting AI agents for summaries, triage notes and letters - and the blocker is almost always the same: identifiable text leaving the controlled environment. Redacta moves the privacy boundary to your side. Text is pseudonymised inside your infrastructure, the token map never leaves, and raw identifiers only ever exist on your machine.

The engine works in two layers. Deterministic patterns catch fixed-format identifiers - NHS numbers with Modulus-11 validation, UK National Insurance numbers, dates of birth, postcodes, phone numbers, emails, hospital and MRN numbers, plus US SSN and ZIP codes. A reasoning pass handles what patterns cannot: patient names told apart from the clinicians treating them, relatives, carers and addresses. A final self-check re-reads the output for anything that slipped through before the report is written.

## Tools & Capabilities

| Capability | Purpose |
|---|---|
| Structured redaction | Deterministic matching of fixed-format identifiers, Python standard library only, no network |
| Reasoning pass | Agent-assisted handling of free-text names, relatives, carers and addresses |
| Self-check | Final re-read for any identifier that slipped through, before the report is written |
| Re-identification | Restore original values from the token map after external AI processing |
| Safe Harbor mode | HIPAA Safe Harbor pass: all dates, specific ages, fax, licence, device serial, VIN and beneficiary numbers |
| Gateway service | Self-hosted HTTP redact/reinstate service with a plain-YAML Kubernetes deployment |

Tool names are served from the endpoint; the same engine ships as an iOS app, agent skill, TypeScript and Python libraries, CLI and FigJam plugin.

## Installation

```bash
claude mcp add redacta -- npx -y redacta-mcp
```

The agent-skill form installs with `openclaw skills install redacta`; the CLI with `npx redacta-cli`. Self-hosting teams build the gateway service from `gateway-service/` and deploy the bundled Kubernetes YAML (two stateless replicas, health probes, no-PHI logging).

## Configuration

```json
{
  "mcpServers": {
    "redacta": {
      "command": "npx",
      "args": ["-y", "redacta-mcp"]
    }
  }
}
```

No API key and no network dependency in the pattern layer. A one-page security and data-protection summary for DPO review is published at pharmatools.ai/redacta-security.

## Business Relevance

- **Clinical teams and telehealth operators** run patient letters and notes through AI without identifiable text leaving the boundary
- **DPOs and compliance leads** get a documented, DPO-friendly data-flow story plus a redaction report per document
- **Health-tech builders** embed the engine in pipelines through the TypeScript or Python library instead of re-implementing identifier detection
- **Kubernetes operators** deploy the gateway service in-cluster so pseudonymisation happens before any external AI call

## Integration with CorpusIQ

CorpusIQ aggregates business data through its connectors - practice management systems, billing and document stores - and Redacta protects the clinical edge of that data. A composed workflow: CorpusIQ pulls a patient letter from the document store, Redacta pseudonymises it at the boundary, the AI drafts or summarises, and reinstate restores identifiers locally before the letter returns to the record. The redaction report travels with the document as an audit artifact.

## Limitations

- Strong first line of defence, not a guarantee - review the redaction report before sharing text
- Reasoning pass benefits from an agent; the deterministic layer alone misses free-text names
- Small project (9 GitHub stars), engine still maturing
- Self-hosting requires Kubernetes for the gateway service
- Clinical scope only; not a general-purpose PII scrubber for arbitrary domains

## FAQ

### Does the token map ever leave my machine?

No. The reversal map is kept out of agent context, and the gateway service keeps raw identifiers inside your boundary. Only tokenised text crosses to the AI tool.

### What is Safe Harbor mode?

Asking for HIPAA Safe Harbor applies a stricter pass: all dates, specific ages over 89, and remaining HIPAA identifiers such as fax numbers, certificate numbers, device serials and beneficiary numbers.

### Can I run it without internet access?

Yes. The structured layer is a Python standard library script with no network calls, so redaction runs fully offline - useful for air-gapped clinical environments.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
