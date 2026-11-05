---
title: "WISEPIM Commerce Reference MCP - EU Trade Rules"
description: "Three offline read-only tools for ecommerce product data: EU customs heading lookup, field checklists for 12 marketplaces, and EU green-claims screening."
category: Commerce / Compliance
stars: ★★ (local package inspected, tools documented, offline)
added: 2026-11-02
source: "the mcp.so homepage card wisepim-commerce-reference created at 2026-11-02T21:25:07Z, the release package lldiegon/wisepim-commerce-mcp v1.0.0 and its README, the official registry name io.github.lldiegon/wisepim-commerce-mcp, and the vendor sources page at wisepim.com/hs-codes and wisepim.com/channel-requirements"
relevance: ★★★
tags: [ecommerce, hs-codes, customs, product-data, marketplaces, green-claims, eu-2024-825, compliance, offline, stdio]
last_updated: "2026-11-04"
---

# WISEPIM Commerce Reference MCP

**The rules that decide whether a product can be listed are scattered across a customs nomenclature, twelve marketplace field specs and a European directive. None of them are in the product spreadsheet, and all three are read by a person under time pressure, in a language they may not be reading natively.**

```
Server type:  Local (stdio, Node.js 22 or later)
Package:      versioned tarball from GitHub Releases, v1.0.0
Install:      npx --package <release tarball> wisepim-commerce-mcp
Bundle:       .mcpb file published in Releases
Auth:         none, no credentials
Network:      none per the package description, no telemetry, no outbound requests
Tools:        3, offline and read-only
Registry:     io.github.lldiegon/wisepim-commerce-mcp
```

## What it does

Three reference tools, each one a lookup against a packaged dataset rather than a call to a service.

| Tool | What it answers |
| --- | --- |
| `lookup_hs_heading` | Which EU Combined Nomenclature 2026 chapter and four-digit heading covers this product, by code or English keywords? |
| `marketplace_requirements` | What field checklist does this marketplace or channel publish, across 12 of them? |
| `check_green_claims` | Does this marketing copy contain phrases that EU Directive 2024/825 puts under scrutiny? |

`lookup_hs_heading` returns candidates for review and the package states plainly that it does no duty calculation and no binding classification, which is the correct scope: a customs heading is decided by a customs authority, and a lookup narrows the reading.

`marketplace_requirements` packages the vendor's published field checklists for twelve marketplaces and commerce channels, with the instruction to verify category-specific requirements with the channel before submitting. That caveat matters, because marketplace specs change without notice and a stale checklist is worse than none.

`check_green_claims` is the one with a deadline attached. It screens copy in English, Dutch, German and French for phrases relevant to Directive (EU) 2024/825, the green claims rules that make unsubstantiated environmental wording a compliance problem rather than a marketing choice. The package states that the screening covers textual signals only and cannot establish legal compliance, and it ships the phrase list inside the package rather than behind a service.

## What this pass measured, and what it did not

This entry was found on the mcp.so newest page with a creation stamp of **2026-11-02T21:25:07Z**, which is above the previous sweep's newest card. The detail page resolves to a GitHub release tarball at **v1.0.0** and to `github.com/lldiegon/wisepim-commerce-mcp`, and the official registry name is `io.github.lldiegon/wisepim-commerce-mcp`.

There is no hosted endpoint, because the server is stdio and offline by design. So **no tool was called**, and this guide states that tier rather than implying a driven session. What was verified is the artefact: the published README, the exact install line pointing at a versioned release tarball rather than a floating package name, and the sources the vendor cites, which are the EU Combined Nomenclature 2026 with Implementing Regulation (EU) 2025/1926, the channel requirement pages packaged on 2026-11-02, and Directive (EU) 2024/825.

Two properties are worth calling out because they are unusual and checkable. The install is a **pinned release tarball**, not an npm `latest` range, so an upgrade is a deliberate change of URL rather than a silent one. And the server takes **no credentials and makes no outbound requests**, which is both the vendor's claim and the only sensible reading of a package whose entire value is a local reference table.

An operator should still treat it as third-party code: it runs on the same machine as the client, so read the package or run it in a container the same way you would any other local server.

## Where this sits in the catalog

Nothing in the catalog covers this ground. The commerce entries read a store rather than a rulebook: [Mamba Ecommerce Platform Profiler](/hermes/mcp/servers/external/mamba-ecommerce-platform-profiler/) profiles a platform, [Shopify Speed Check](/hermes/mcp/servers/external/shopify-speed-check-mcp/) audits storefront speed. The trade entries answer market questions rather than listing questions: [EU Trade Explorer](/hermes/mcp/servers/external/eu-trade-explorer-mcp) and [Gemalli B2B Trade MCP](/hermes/mcp/servers/external/gemalli-b2b-trade-mcp/) work the cross-border trade angle.

And the green claims surface is new in the strict sense: **no guide in this catalog mentioned Directive 2024/825 or green claims before this entry.** For an operator selling into the EU, that is the one tool here with a regulatory clock on it.

## Connect it

```json
{
  "mcpServers": {
    "wisepim-commerce": {
      "command": "npx",
      "args": [
        "--yes",
        "--package",
        "https://github.com/lldiegon/wisepim-commerce-mcp/releases/download/v1.0.0/wisepim-commerce-mcp-1.0.0.tgz",
        "wisepim-commerce-mcp"
      ]
    }
  }
}
```

Node.js 22 or later, no key, no sign-in. Bundle-capable clients can open the `.mcpb` file from the releases page instead.

Prompts that fit the three tools:

- "We are listing a linen shirt on Amazon and Zalando. What product fields does each channel expect, and which heading would this ship under?"
- "Review this product page copy for environmental claims that EU Directive 2024/825 would question."

## Do not use it as

- **A customs classification.** The tool returns candidates for review and says it does not classify. The binding decision belongs to a customs authority.
- **A legal opinion on green claims.** It flags phrases. Whether a specific claim is substantiated, and how, is a legal and evidence question.
- **A live feed of marketplace specs.** The checklists are packaged, not fetched. Re-check with the channel before a launch.
- **A duty or landed-cost calculator.** No rates, no calculation.

## FAQ

### Does it need an account or a key?
No. It is a local package with no credentials and, per its description, no outbound requests and no telemetry.

### Which marketplaces are covered?
Twelve marketplace and commerce channel field checklists ship in the package. The vendor does not name all twelve in the README, so read `marketplace_requirements` output rather than assuming your channel is in the set.

### Which languages does the green claims scanner read?
English, Dutch, German and French.

### Is the customs data current?
The vendor cites the EU Combined Nomenclature 2026 and Implementing Regulation (EU) 2025/1926, and packages the channel requirements as of 2026-11-02. Both are snapshot dates, not a live feed.

### Why pin a tarball instead of using npm?
That is how the vendor publishes it, and it has a security property worth keeping: the version you audited is the version you run.
