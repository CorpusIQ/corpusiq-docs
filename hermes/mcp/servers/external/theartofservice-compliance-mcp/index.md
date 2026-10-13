---
title: "The Art of Service MCP - Compliance Framework Crosswalks"
description: "Query a compliance knowledge graph of 960+ frameworks, 46,000+ controls and 315,000+ cross-framework mappings, then find a course that covers them."
category: Compliance
stars: n/a (new listing)
added: 2026-10-12
source: "chatmcp/mcpso issue #5218 (Oct 12, 2026 evening sweep)"
relevance: ★★
tags: [compliance, frameworks, iso-27001, nist, pci-dss, crosswalk, controls, audit, remote-mcp]
---

# The Art of Service Compliance Intelligence MCP

**Remote MCP server (Streamable HTTP, no key for the catalogue and light graph use)** - a compliance knowledge graph from The Art of Service: 969 frameworks, 46,074 controls and 315,000+ cross-framework mappings, plus a course catalogue of 300,000+ self-paced professional courses. Ask which ISO 27001 controls map to NIST or PCI DSS, read a control with its cross-references, run a coverage report across standards, and then find the course that closes the gap.

```
Server type: Remote (Streamable HTTP)
Auth: none for the catalogue and light graph use; API key for volume
Endpoint: https://api.theartofservice.com/mcp
Tools: 33 (framework and control search, control cross-references, cross-framework mapping, coverage reports, crosswalk pairs with provenance, course search and purchase links, weekly signals, adoption reporting)
Pricing: catalogue tools free with no rate limit; compliance graph free for light use, keys for volume
Category: Compliance / Security
Built by: The Art of Service (theartofservice.com, hosted service)
Website: compliance.theartofservice.com
Listing: chatmcp/mcpso issue #5218 (Oct 12, 2026 evening sweep)
```

## Why This Matters for Operators

Compliance work is mostly translation between frameworks: a customer asks for SOC 2, a regulator asks about ISO 27001, an insurer wants NIST, and the team needs to know which control satisfies all three without buying three separate audits. That translation normally lives in expensive spreadsheets and consultant time. This server turns it into lookups: search frameworks and controls, read a control with its cross-references, map controls between two standards, and produce a coverage report that shows what one framework's requirements already satisfy in another.

The crosswalk side is deliberately candid: reviewed crosswalk pairs come with their provenance, and the mappings that were refused are readable too, so an answer can distinguish a verified mapping from a suggested one. For teams running training programs, the course catalogue closes the loop by finding the course that covers two or more standards together.

## Tools & Capabilities

| Tool group | Purpose |
|---|---|
| Frameworks and controls | agent_search_frameworks, agent_get_framework, agent_get_framework_controls, agent_get_framework_controls_by_name, agent_get_control, agent_get_control_cross_references: browse the graph and read controls with their references |
| Crosswalks | agent_cross_framework_map, agent_coverage_report, agent_combined_coverage, agent_list_crosswalk_pairs, agent_crosswalk_pair, agent_crosswalk_provenance, agent_crosswalk_refuted, agent_buy_crosswalk, agent_buy_review: map and report coverage between standards, with provenance and refused pairs |
| Courses | agent_search_courses, agent_get_course, agent_courses_for_frameworks, agent_list_course_frameworks, agent_search_course_content, agent_buy_course: find and buy the course that covers the gap |
| Signals | agent_signals_this_week, agent_capital_by_function, agent_controls_touched_by, agent_signal_exposure: weekly market signals tied to controls and functions |
| Adoption | adoption_list_engagements, adoption_get_adoption_summary, adoption_get_report: adoption reporting for engagements |
| Meta | agent_search, agent_platform_stats, agent_pricing_info |

## Installation

```bash
claude mcp add --transport http theartofservice https://api.theartofservice.com/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "theartofservice": {
      "type": "http",
      "url": "https://api.theartofservice.com/mcp"
    }
  }
}
```

## Business Relevance

- **Security and compliance leads** can map an existing certification to the framework a customer or insurer is asking about, and show the crosswalk behind the answer.
- **Sales teams answering security questionnaires** can pull the control texts and cross-references instead of promising to get back to the prospect.
- **Training and HR programs** can find courses that cover multiple standards at once and link to the purchase page.
- **GRC tooling and consultancies** can use the graph as a reference layer behind their own workflows.

## Integration with CorpusIQ

CorpusIQ answers from the operational systems; the compliance graph answers what the standards say. Connect the sources that carry the evidence - a GitHub or Jira source for change control, a cloud-billing or inventory source for asset scope - and ask which ISO 27001 controls the current evidence set covers, where the gaps are against the customer's requested framework, and which control language satisfies both. The evidence comes from the source of record; the mapping and its provenance come from the graph.

## Limitations

- The graph is a reference layer, not an audit: mapping a control across frameworks does not certify anything, and reviewed crosswalks carry their own provenance notes.
- Course tools are a commercial catalogue; purchase links are handed to the user and the transaction happens on the vendor's storefront.
- Free for light use with keys for volume; heavy org-wide use should confirm terms via agent_pricing_info.

## FAQ

### Do I need an API key?

No for the course catalogue and light compliance-graph use. The vendor issues keys for volume use; the endpoint answers keyless initialize and light queries without credentials.

### What does "refused mappings" mean in the crosswalk tools?

The graph records not only reviewed crosswalk pairs but also the mappings that were evaluated and refused, with provenance. That lets an assistant say a mapping is not supported instead of implying one exists.

### Which frameworks are covered?

969 frameworks as of launch, from ISO and NIST families to PCI DSS and industry frameworks; search first with agent_search_frameworks to confirm a specific standard is present.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
