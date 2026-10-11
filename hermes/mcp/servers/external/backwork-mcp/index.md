---
title: "Backwork MCP - Medicare Policy and Prior Auth Research"
description: "Research Medicare and payer policies, check prior authorization and claim risk, and prepare denial appeals from your assistant, sourced."
category: Healthcare Operations
stars: n/a (new listing)
added: 2026-10-10
source: "mcpservers.org /all (page 2) + vendor page (backworkhealth.com docs); catalogued at the October 10, 2026 evening sweep"
relevance: ★★★
tags: [healthcare, medicare, prior-authorization, claims, compliance, clinical-ops, remote-mcp]
---

# Backwork MCP

**Official MCP server for Backwork, a Medicare and payer policy intelligence platform** - research coverage, prior authorization, claim risk and drug formulary evidence from the assistant, with every fact carrying numbered citations back to the policy it came from. Eight workflow-level tools (deliberately not a 1:1 API wrapper), a read-only OAuth grant by default, MCP Apps cards in ChatGPT, and a Claude Code plugin that bundles four clinical-research skills. The healthcare-ops find of the October 10 evening sweep, catalogued with the hosted endpoint probed live (initialize returns 401, `missing_bearer_token`).

```
Server type: Remote (Streamable HTTP at https://backworkhealth.com/mcp) or local stdio via npx -y @backwork/mcp
Auth: OAuth in the browser (read-only grant unless scopes include write) or a Backwork API key (bwk_live_...)
Tools: 8 workflow tools (backwork_coverage_lookup, backwork_policy_research, backwork_claim_validation, backwork_prior_auth_research, backwork_drug_formulary_research, backwork_compliance_review, backwork_webhook_management, backwork_system_health)
Category: Healthcare Operations
Built by: Backwork (backworkhealth.com; repo github.com/tylergibbs1/backwork-mcp, MIT; registry io.github.tylergibbs1/backwork-mcp)
```

## Why This Matters for Operators

Ask a clinic's staff where the rule for a denied claim lives and you get a shrug: it is split across Medicare LCDs and NCDs, each MAC's articles, and commercial payer policies, updated on their own schedules. Backwork turns that pile into a research surface - which policy lists these codes, what documentation a prior auth needs, what the denial risk is, whether a commercial formulary covers a drug - and grounds every answer in a named policy with citations. For practices, billing teams and consultants, it compresses the lookups that eat hours per claim into one conversation, and the compliance-review tool watches policy changes so nothing quietly moves underneath a workflow.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `backwork_coverage_lookup` | Look up procedure codes and combine code details, policy evidence, prior authorization, claim risk, jurisdiction comparison and spending evidence; with a `payer` filter, code details list only that payer's policies |
| `backwork_policy_research` | Actions: `compare` codes side by side across Medicare contractors (MACs) with coverage counts, `search` matching policies with payer and number, `get` one policy's summary and criteria, `criteria` matching excerpts, `changes` recent policy changes, `jurisdictions` each MAC and its states |
| `backwork_claim_validation` | Validate claim coverage, documentation requirements, denial risk and optional policy-specific criteria |
| `backwork_prior_auth_research` | Prior-auth determination and confidence, codes requiring authorization, documentation to gather, known gaps and numbered citations; can also run a background job that searches public payer websites |
| `backwork_drug_formulary_research` | Commercial pharmacy-benefit evidence from CVS Caremark, Express Scripts and UnitedHealthcare / Optum Rx |
| `backwork_compliance_review` | Compliance stats and unreviewed policy changes; with an API key, acknowledge changes |
| `backwork_webhook_management` | Manage webhook endpoints (one event, `compliance.acknowledged`); needs a write-scoped API key |
| `backwork_system_health` | API health and dependency status; API-key connections only |

## Installation

```json
{
  "mcpServers": {
    "backwork": {
      "url": "https://backworkhealth.com/mcp"
    }
  }
}
```

Claude Code: `claude mcp add --transport http backwork https://backworkhealth.com/mcp`, then finish the browser login and consent. Claude Desktop, Cursor, VS Code and Codex configurations are documented, and there is a Claude Code plugin with four skills (prior authorization, coverage checks, policy changes, denial appeal prep): `/plugin marketplace add tylergibbs1/backwork-mcp` and `/plugin install backwork@backwork`. New accounts start with 100 free credits.

## Configuration and Safety

- OAuth grants are read-only unless scopes include `write`: write-scope actions (webhook management, compliance acknowledgements) are withheld from a read-only connection, and the hosted endpoint rejects a raw API key passed as a bearer token.
- The local `npx -y @backwork/mcp` process uses `BACKWORK_API_KEY` (`bwk_`); the server validates or introspects every token per request and does not store OAuth tokens.
- Results carry provenance: `source_urls`, `authority`, `retrieved_at` and `as_of` per fact, plus applicability notes; Medicare content carries a non-Medicare disclaimer when relevant and commercial policy headers where payer type matters.
- Rate limits follow the API plan; the docs point at a higher-capacity plan when the reset window is hit.

## Business Relevance

- **Medical practices and clinics**: check coverage and prior-auth requirements before the visit or the claim, so staff know the documentation to gather while there is still time to gather it.
- **Billing companies and RCM teams**: validate claims against the policy evidence and see denial risk with citations - and the policy-change feed means the rulebook moving no longer shows up first as a rejected claim.
- **Consultants and compliance leads**: review policy changes with an acknowledgment trail, and pull formulary evidence from the three largest commercial PBMs in the same surface.

## Integration with CorpusIQ

Policy answers and business answers complete each other. Ask Backwork what Medicare or a payer requires for a code, then ask CorpusIQ how your own numbers look - claim, revenue and schedule patterns from the systems you already connect - and keep both in one thread, each traceable to its source.

## Limitations

- The MCP server is a research and validation surface; it does not submit claims or prior authorizations, and the practice management system remains the system of record.
- Prior-auth jobs against public payer websites run as background tasks and show as pending until polled again.
- Some tools and actions are gated by credential scope (read-only OAuth hides webhook management and compliance acknowledgement; `backwork_system_health` is API-key only).
- Coverage depth follows the platform's policy library; confirm anything high-stakes against the linked policy document, as with any research tool.

## FAQ

### Do I need an API key or is OAuth enough?

OAuth is enough for the research core - coverage, policy, claim, prior-auth and formulary tools - and grants read-only by default. An API key unlocks the extra actions: compliance acknowledgements and webhook management.

### Does it write anything into our systems?

No. The tools research, validate and report; the only writes are inside Backwork itself (acknowledging a reviewed policy change, managing Backwork webhooks), and those need a write-scoped credential.

### What sources does it cite?

Medicare LCDs, Articles and NCDs, MAC jurisdiction data, and commercial payer policy documents, with per-fact `source_urls` and retrieval timestamps; drug formulary evidence comes from CVS Caremark, Express Scripts and UnitedHealthcare / Optum Rx.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
