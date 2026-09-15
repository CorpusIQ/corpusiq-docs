---
title: "Zetesis MCP - Scientific Due Diligence on Claims and Pitches"
description: "Keyless hosted MCP that runs scientific due diligence on any biomedical, clinical or AI/ML claim: routes the claim to its scientific class, searches Europe PMC, ClinicalTrials.gov, openFDA, NIH RePORTER and SEC EDGAR, and returns a graded evaluation with a hard identifier on every source, sealed in a verifiable attestation."
category: Research
stars: "n/a (new listing, reutavidan/zetesis)"
added: 2026-09-01
source: "chatmcp/mcpso issue #3879 (Sep 1, 2026 night sweep)"
relevance: ★★
tags: [mcp-server, due-diligence, research, biomedical, clinical-trials, fda, scientific-review, remote-mcp, keyless]
---

# Zetesis MCP

**Keyless scientific due diligence for agents.** Zetesis takes a claim, abstract, paper or pitch deck and returns what a domain reviewer would ask, the failure patterns that caught comparable claims before, and the public evidence bearing on it. Every source carries a hard identifier (PMID, DOI, NCT, NIH grant number or SEC filing reference) that was retrieved, not generated. Live-probed Sep 1, 2026: all 4 tools captured from the endpoint with no account or API key.

```
Server type: Hosted, remote (Streamable HTTP)
Endpoint: https://api.zetesis.science/mcp
Auth: None - no account, no token (verified live)
Tools: 4 (live-probed: zetesis_scope, zetesis_evidence, evaluate_claim, verify_attestation)
Registry: io.github.reutavidan/zetesis v0.2.0 (active)
License: MIT
Built by: Zetesis (zetesis.science)
```

## Why This Matters for Operators

Diligence on scientific claims is the highest-cost check an operator can skip. Whether you are screening a biotech investment, validating a vendor's clinical marketing, or checking a medical-AI pitch deck, the questions a domain reviewer would ask are exactly the questions nobody on a lean team is equipped to ask.

First, **reviewer-grade question sets, not search results.** `zetesis_scope` routes the claim to its scientific class (genomics, single-cell, CRISPR screens, clinical trials, real-world evidence, diagnostics and more) and returns the diligence apparatus for it: questions structured by substrate, methods, cohort and risk of bias, plus a failure-pattern taxonomy with named precedents.

Second, **hard identifiers on every source.** `zetesis_evidence` searches Europe PMC, ClinicalTrials.gov, openFDA and NIH RePORTER and returns a deduplicated bundle where every reference carries a retrievable identifier. Nothing is hallucinated; unfindable support simply fails to appear.

Third, **year-fenced retrieval and tamper-evident output.** Retrieval can be fenced to a year so a claim is judged on what was knowable at the time, and `evaluate_claim` seals the graded evaluation in a verifiable attestation.

## Tools and Capabilities

All 4 tools were captured live from the endpoint on Sep 1, 2026 (serverInfo: zetesis v1.28.1, no auth).

| Tool | What it does |
|------|--------------|
| `zetesis_scope` | Routes a claim to its scientific class and returns the diligence apparatus: reviewer questions by substrate/methods/cohort/bias-risk plus a failure-pattern taxonomy with named precedents. Runs no model. |
| `zetesis_evidence` | Runs the searches against Europe PMC, ClinicalTrials.gov, openFDA and NIH RePORTER and returns a deduplicated evidence bundle with PMID/DOI/NCT/grant identifiers on every source. Runs no model, returns in under a second. |
| `evaluate_claim` | Runs the hosted engine end to end: a graded reading of the claim against the scoped evidence. Slower by design. |
| `verify_attestation` | Confirms an evaluation's claim, evidence and conclusion have not been altered since it was signed. |

The issue body also cites SEC EDGAR among the registers; the live tool descriptions list the four biomedical sources above. The evidence tools send nothing to any model provider.

## Installation

```bash
claude mcp add --transport http zetesis https://api.zetesis.science/mcp
```

No account, no key, no sign-in. Paste the endpoint into any MCP client and call `zetesis_scope` first, then `zetesis_evidence`.

## Configuration

```json
{
  "mcpServers": {
    "zetesis": {
      "type": "http",
      "url": "https://api.zetesis.science/mcp"
    }
  }
}
```

That is the entire configuration. The server is read-only and stateless; the two evidence tools run no language model and cost nothing to run.

## Business Relevance

- **Investors and funds** screen biotech, medtech and AI-health pitch decks with the same question set a domain reviewer would bring, before paying for expert diligence.
- **Operators buying clinical or AI-health products** verify vendor claims against ClinicalTrials.gov and openFDA instead of trusting marketing collateral.
- **Analysts and consultants** produce cited, attestation-sealed diligence memos where every identifier can be followed to the source.
- **Legal and compliance teams** get a year-fenced evidence trail that holds up when a claim is later challenged.

## Integration with CorpusIQ

Zetesis composes with CorpusIQ as the evidence layer behind financial and vendor decisions. A CorpusIQ workflow that pulls a company's filings or funding data can hand the company's core scientific claim to Zetesis and get back reviewer questions plus cited evidence, then attach the sealed attestation to the deal memo in the operator's documents. The operator keeps one governance point: CorpusIQ supplies the business context and Zetesis supplies the scientific ground truth, and every identifier links a conclusion back to its cited source.

## Limitations

- New listing with no public adoption data; the repo (reutavidan/zetesis) is fresh and unstarred.
- Hosted engine: `evaluate_claim` runs the vendor's grading model, so evaluations depend on the vendor's uptime and model version.
- Coverage is biomedical, clinical and AI/ML claims; it is not a general-purpose web researcher.
- Year fencing depends on the source registers' date fields; verify the fence on claims where timing is material.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [Edgrapi MCP - SEC EDGAR Structured Data for Agents](/docs/hermes/mcp/servers/external/edgrapi-mcp)
- [Legalize MCP - Point-in-Time Legislation with Git Provenance](/docs/hermes/mcp/servers/external/legalize-mcp)
- [World Monitor MCP - Global Intelligence: Markets, Risk, Supply Chains & Procurement](/docs/hermes/mcp/servers/external/world-monitor-mcp)
