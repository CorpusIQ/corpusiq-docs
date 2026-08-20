---
title: "LicenseGuard MCP - License Compliance Verdicts by Distribution Model"
description: "MCP server that evaluates open-source dependency licenses against how you ship your software: SaaS, on-prem, or internal — with clause-cited verdicts, manifest and lockfile audits, and a hosted no-auth endpoint"
category: Compliance & Regulatory
stars: n/a (new listing)
added: 2026-08-20
source: "mcp.so GitHub issue #3658"
relevance: ★★★
tags: [license-compliance, open-source-licensing, dependency-audit, legal-compliance, agpl, gpl, supply-chain, remote-mcp]
---

# LicenseGuard MCP

**Remote MCP server (Streamable HTTP, no auth) plus a local stdio image — dependency license verdicts computed against your distribution model.** Generic scanners answer "what license is this?" and warn on everything. LicenseGuard answers "does this dependency's license obligate you, given how you ship?" — the same AGPL-3.0 dependency is blocked for a SaaS product, allowed for internal-only use, and allowed as a build-time devDependency that never reaches the artifact. Verdicts are stated with the clause cited, and the tool explicitly does not tell you what to do.

```
Server type: Hosted remote (Streamable HTTP) + local stdio (Docker)
Auth: None (stateless, no session state)
Endpoint: https://license-guard.rcc-aoki.workers.dev/mcp
Tools: 3 (single dependency, manifest audit, license explainer)
Pricing: Free (Phase 0 public service)
Category: Compliance / Supply Chain
Built by: rccaoki-wq (Apache-2.0)
```

## Why This Matters for Operators

License risk is a shipping problem, not a scanning problem. The expensive failure mode is a false positive the team learns to ignore — a tool that blocks every GPL-family dependency trains people to click through, and the one real AGPL §13 network-clause hit gets shipped anyway. LicenseGuard's distribution-model split is the fix: `check_dependency_license` gives a verdict for exactly how your software reaches users, and `explain_license` shows what a license requires across every distribution model so the reasoning is auditable, not a red badge.

The manifest audit is where operators get real leverage. Problem licenses usually arrive transitively — a dependency of a dependency — so `check_manifest_licenses` runs against lockfiles including `package-lock.json` v2/v3, which embeds a license per entry and audits the full transitive tree with zero network lookups against the exact versions that will ship. And the tool's integrity stance is unusual: an incomplete scan is never reported as clean. Unresolvable dependencies surface as `not-checked` or `review` and count in the summary, so a partial audit cannot masquerade as a passed one.

## Tools & Capabilities

| Tool | When to call it |
|---|---|
| `check_dependency_license` | Before adding a single dependency — verdict for your distribution model |
| `check_manifest_licenses` | Audit a whole manifest or lockfile, transitive deps included |
| `explain_license` | What a license requires across every distribution model, clause-cited |

Supported ecosystems: npm, PyPI, Go modules, crates.io. Lockfile formats: `package-lock.json` (v2/v3, zero network lookups), `pnpm-lock.yaml`, `yarn.lock`, `go.sum`, `Cargo.lock`, `poetry.lock`, `uv.lock`; direct manifests: `package.json`, `requirements.txt`, `go.mod`, `Cargo.toml`. A plain JSON API and an agent-facing index at `/llms.txt` mirror the same verdicts.

## Installation

```bash
claude mcp add licenseguard --transport http https://license-guard.rcc-aoki.workers.dev/mcp
```

Local stdio mode keeps your manifest on the machine (only package names and versions are sent to public registries for license lookup):

```bash
git clone https://github.com/rccaoki-wq/license-guard && cd license-guard
docker build -t licenseguard .
claude mcp add licenseguard -- docker run -i --rm licenseguard
```

Both paths run the same policy engine and are pinned together by an end-to-end suite, so hosted and local verdicts cannot disagree.

## Configuration

```json
{
  "mcpServers": {
    "licenseguard": {
      "type": "http",
      "url": "https://license-guard.rcc-aoki.workers.dev/mcp"
    }
  }
}
```

No authentication and no session state — the endpoint is stateless and public.

## Business Relevance

- **SaaS product teams** get AGPL/GPL verdicts that match reality: network-accessible software triggers §13, internal tools do not
- **Agency and consultancy operators** run a license audit on vendor or subcontractor code before accepting delivery
- **Compliance leads** get clause-cited verdicts to attach to a release or due-diligence record instead of scanner noise
- **Engineering managers** see lockfile-level transitive audits without sending the codebase anywhere

## Integration with CorpusIQ

LicenseGuard MCP is the compliance edge of a software-shipping operator's stack, and it complements the CorpusIQ read surface in two directions. For agencies and consultancies, the CorpusIQ HubSpot or QuickBooks connectors hold the client and billing record while LicenseGuard supplies the deliverable's license posture — the due-diligence artifact joins the deal file. For product teams, the audit verdicts feed release documentation that the CorpusIQ Drive connector stores and indexes, so compliance evidence is retrievable per release rather than living in a single engineer's notes. The direction of flow: LicenseGuard MCP evaluates dependencies; CorpusIQ reads the business and document systems the verdicts attach to.

## Limitations

- Phase 0 service — the maintainer is explicitly measuring willingness to pay before building further (GitHub App phase pending)
- Verdict scope is license obligation only; it does not scan for CVEs, malware, or provenance
- Hosted endpoint carries no SLA and no auth — treat as advisory for sensitive audits (local stdio mode exists for that)
- Registry lookups depend on public registries being reachable for ecosystems outside package-lock v2/v3
- Brand new listing — no community track record yet

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
