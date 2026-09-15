---
title: PolicyForge MCP - Legal Policies from Your Codebase
description: "Hosted MCP server that generates, audits, and version-tracks legal policies - privacy, terms, cookies, EULAs, disclaimers, HIPAA BAAs - from your codebase through OAuth, API key, or local npx."
category: Compliance
stars: n/a (new listing, policyforge/mcp; license not declared)
added: 2026-08-29
source: mcpservers.org /all page 1
relevance: ★★
tags: [mcp-server, legal-policies, privacy-policy, terms-of-service, hipaa-baa, compliance, gdpr, remote-mcp]
---

# PolicyForge MCP

**A hosted MCP server that generates legal policies - privacy policies, terms of service, cookie policies, refund policies, EULAs, disclaimers, and HIPAA Business Associate Agreements - directly from your AI coding tools, filling the details from your codebase and dropping the policy into the project.** Policies are version-tracked, and the compliance-audit tools (audit_compliance, check_policy_freshness) are free and unlimited, so the audit loop never touches quota.

```
Server type: Remote (Streamable HTTP) + local npx
Auth: OAuth (browser sign-in), API key header, or POLICYFORGE_API_KEY env var
Endpoint: https://policyforge.co/api/mcp
Tools: 11 (generate_policy, generate_baa, audit_compliance, version control, more)
Pricing: Free 2 policies/mo + 3 bonus on first connect; Pro for HIPAA BAAs
Category: Compliance / Legal
Built by: PolicyForge (policyforge.co); repo policyforge/mcp
```

## Why This Matters for Operators

Every SaaS needs a privacy policy, terms, and usually more, and the expensive part is not writing them - it is keeping them honest as the product changes. PolicyForge attacks both ends: generation fills the policy from a codebase scan (what data is collected, what integrations exist), and the audit tools continuously compare what the code now does against what the policy discloses, with drift checks that diff the current scan against the manifest stored at generation time.

The version model is built for legal review: every update and regeneration saves a snapshot, links keep working across edits, and restores are themselves reversible. Free-tier audits are unlimited, so an operator can wire a compliance check into a routine workflow without paying per check.

**Policies generated from the code, then continuously audited against it, with version history for legal review.**

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `generate_policy` | Generate a policy and return Markdown plus a hosted URL; consumes one policy from quota |
| `generate_baa` | Generate a HIPAA Business Associate Agreement from 45 CFR 164.504(e) clauses, validated clause by clause; Pro plan, never publicly hosted |
| `regenerate_policy` | Re-run the engine with changed business context; same ID and URL, previous content saved as a version |
| `update_policy` | Hand-edit in place; same ID and URL so published links keep working |
| `audit_compliance` | Gap analysis: what the code does versus what the policy discloses (free, unlimited) |
| `check_policy_freshness` | Drift detection: diff the current codebase scan against the generation-time manifest (free, unlimited) |
| `list_policy_versions`, `restore_policy_version` | Version history with snapshot-before-every-change and reversible rollbacks |
| `list_policies`, `get_policy`, `delete_policy` | Account-level policy management |

## Installation

```bash
claude mcp add -s user --transport http policyforge https://policyforge.co/api/mcp
```

Omit the header to use OAuth. For local stdio: `npx -y @policyforge/mcp` with POLICYFORGE_API_KEY set. A PolicyForge account is required first (free, no card).

## Configuration

```json
{
  "mcpServers": {
    "policyforge": {
      "type": "http",
      "url": "https://policyforge.co/api/mcp"
    }
  }
}
```

Restart the client after config changes and run /mcp to authenticate. All three connection modes expose the same tools.

## Business Relevance

- **Founders launching a product** generate privacy, terms, and cookie policies in one conversation, then keep them version-tracked.
- **Compliance operators** run unlimited code-vs-disclosure audits and drift checks on a schedule.
- **Healthcare-adjacent vendors** produce HIPAA BAAs built from the required 45 CFR 164.504(e) clauses with clause-by-clause validation.
- **Legal reviewers** work against version history and stable hosted URLs instead of email attachments.

## Integration with CorpusIQ

PolicyForge's audit loop is a natural companion to CorpusIQ's operations data: a CorpusIQ workflow that already knows the business context - which connectors pull which data, from QuickBooks to Shopify - can feed that context into PolicyForge's generation and then run audit_compliance checks as part of the same routine that reviews the company's data practices. The audit verdicts land alongside the operational reports, so compliance state and business state are reviewed in one pass rather than in a separate legal silo.

## Limitations

- Brand new listing - first sweep August 29, 2026; repo carries no declared license.
- AI-generated legal documents are drafts - the vendor's own framing; final review by counsel still applies.
- Free tier caps generation (2/mo + 3 bonus on first connect); audits are the unlimited free surface.
- HIPAA BAAs require the Pro plan and are never publicly hosted.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [PassportCraft MCP - EU Digital Product Passport Compliance](/docs/hermes/mcp/servers/external/passportcraft-mcp)
- [Legalize MCP - Point-in-Time Legislation with Git Provenance](/docs/hermes/mcp/servers/external/legalize-mcp)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
