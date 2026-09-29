---
title: "OpenGATE MCP - Deterministic Grounding Checks for AI Answers"
description: "Evidence-grounding checks for AI systems that must justify answers: facts present, numbers traceable to the source, abstention over fabrication."
category: Compliance
stars: 2
added: 2026-09-29
source: mcpservers.org
relevance: ★★★
tags: [rag, grounding, evaluation, verification, ci-cd, document-qa, hallucination, self-hosted]
---

# OpenGATE MCP

**Deterministic grounding verification for AI systems.** OpenGATE checks whether an AI system can prove every answer from the evidence it was given - required facts present, every number traceable to the source, and abstention when the context cannot answer. No LLM judge and no grader model: the scorers are pure logic, so results are reproducible, free and fast enough to run on every answer or gate every commit.

```
Server type: Local stdio (npm), plus GitHub Action, Docker and PyPI
Auth: None (offline suite runs keyless)
Endpoint: npx @pharmatools/opengate-mcp
Tools: 7 scorer families (citation-detection, claim-extraction, verdict-accuracy, redaction, simplification, retrieval, grounding)
Pricing: Free (MIT)
Category: Compliance
Built by: PharmaTools.AI (github.com/nickjlamb/opengate)
```

## Why This Matters for Operators

AI systems that answer from documents and data - RAG pipelines, document-QA tools, legal and scientific assistants - can look fluent and still be wrong. OpenGATE turns grounding failures into numbers you can track. Every check is deterministic, so the same gold set and the same system always produce the same scorecard, stamped with the git SHA.

The real operator value is the regression gate. Change a prompt, model or pipeline, and OpenGATE diffs the new scorecard against a saved baseline: improved or held deploys, regressed fails the build. Reliability stops being a feeling and becomes a build artifact, exactly like test coverage in traditional software.

## Tools & Capabilities

| Scorer | What it measures |
|---|---|
| citation-detection | Per-claim citation set exact-match and Jaccard, supported-style accuracy |
| claim-extraction | Precision, recall and F1 vs gold; non-claim leakage; verbatim fidelity |
| verdict-accuracy | Exact and adjacency accuracy; passage hallucination rate; consistency, latency and cost |
| redaction | Recall on gold identifiers with leaks as named failures; over-redaction and known-gap tracking |
| simplification | Faithfulness of rewrites: anchor recall, fabricated numbers, length gates |
| retrieval | Fidelity of retrieved records vs the authority: anchor fields plus structural invariants |
| grounding | Generic RAG: answer-anchor recall, fabrication vs context, and abstention |

Tool names are served from the endpoint; the CLI, GitHub Action, Python package (`pip install opengate-grounding`) and Docker image (`pharmatools/opengate`) ship the same scorer set, and `npx @pharmatools/opengate init` scaffolds gold cases plus a CI gate.

## Installation

```bash
claude mcp add opengate -- npx -y @pharmatools/opengate-mcp
```

Offline evaluation of the bundled 39-case gold set: `npx @pharmatools/opengate`. Point `opengate.http.json` at your endpoint and add `--online --ci` to gate your own system. Full walkthrough at github.com/nickjlamb/opengate (docs/GETTING-STARTED.md).

## Configuration

```json
{
  "mcpServers": {
    "opengate": {
      "command": "npx",
      "args": ["-y", "@pharmatools/opengate-mcp"]
    }
  }
}
```

The generic HTTP adapter is a no-code path for REST-backed systems: endpoint paths and headers live in `opengate.http.json` with `${ENV}` interpolation, so no adapter code is needed for most API-shaped systems.

## Business Relevance

- **Compliance and QA teams** gate document-QA and extraction pipelines on proof that answers cite real source passages
- **Engineering leads** put grounding checks in CI next to unit tests, with regressions failing the build on the spot
- **Agencies shipping client-facing AI assistants** get a reproducible, auditable scorecard per model or prompt change
- **Legal and healthcare operators** run deterministic redaction and fidelity checks where an LLM judge would itself be a risk

## Integration with CorpusIQ

CorpusIQ answers are grounded in live business data through its connectors - Stripe revenue, QuickBooks invoices, GA4 traffic, HubSpot deals. OpenGATE adds the verification layer on top: run CorpusIQ's answers against an OpenGATE adapter built on real business documents, and every claim is checked against the source text instead of being taken on faith. The composed workflow is connect, answer, verify - with the scorecard archived next to the answer.

## Limitations

- Brand new project (2 GitHub stars), pre-1.0 interfaces may still shift
- Gold cases are hand-labelled, so a new domain starts with a smaller benchmark set
- Online scorers require writing or configuring an adapter for your system
- Deterministic checks catch grounding failures, not general answer quality - pair with an eval framework like DeepEval for broader metrics
- stdio local server; no hosted SaaS endpoint

## FAQ

### Does OpenGATE use an LLM to judge answers?

No. Scorers are deterministic checks against hand-labelled gold cases - pure logic, no grader model. Judgment lives in the gold set, which makes results reproducible and free to run in CI.

### What is the difference between OpenGATE and eval frameworks?

General frameworks like DeepEval evaluate broadly, usually with an LLM judge. OpenGATE verifies the narrower promise that every answer is grounded in evidence - provenance, traceable numbers and abstention - and diffs every run against a baseline.

### Can I gate my existing RAG system without writing code?

Yes. The generic HTTP adapter reads endpoint paths and headers from `opengate.http.json`, and the GitHub Action (`uses: nickjlamb/opengate@v0`) drops the gate into any repo.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
