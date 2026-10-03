---
title: "ASOgenic MCP - App Store Optimization for Agents"
description: "MCP for App Store Optimization: research Apple keywords, write and validate metadata, manage screenshots and submit to review."
category: "Marketing"
stars: n/a (hosted platform, asogenic.com)
added: 2026-10-02
source: "mcpservers.org server page (asogenic-com-docs)"
relevance: ★★
tags: [aso, app-store, keywords, mobile, metadata, apple, remote-mcp]
---

# ASOgenic MCP

**Remote MCP server (Streamable HTTP, per-account bearer key)** - ASOgenic runs an App Store Optimization pass from an agent: research Apple keywords, write and validate metadata, manage screenshots and submit to App Store review, using the operator's own App Store Connect credentials.

```
Server type: Remote (Streamable HTTP)
Auth: Per-account bearer API key, with App Store Connect credentials held client-side
Endpoint: https://mcp.asogenic.com/mcp
Tools: keyword research, metadata validation, screenshot management and submission
Pricing: ASOgenic account required
Category: Marketing
Built by: ASOgenic (asogenic.com)
```

## Why This Matters for Operators

App Store rankings live or die on metadata, and the ASO loop is normally a scatter of spreadsheets, keyword tools and App Store Connect tabs. ASOgenic collapses it into one agent surface: research a keyword, draft and validate the metadata that uses it, then move screenshots and submit, all from the assistant.

**The credential split is the security feature.** The agent holds the App Store Connect `.p8` key in its own environment; the ASOgenic server mints short-lived JWTs from it per request and never stores the key in the cloud, and the dashboard only issues and manages the platform key without ever seeing the Apple credentials.

## Tools & Capabilities

| Capability | Purpose |
|---|---|
| Keyword research | Research Apple keywords for the app's category and market |
| Metadata authoring | Write and validate App Store metadata against the listing rules |
| Screenshot management | Manage and update App Store screenshots |
| Release submission | Submit to Apple review through App Store Connect |
| `asogenic_auth_status` | Verify that App Store Connect credentials are configured and valid |

## Installation

1. Create a platform key in the ASOgenic dashboard (shown once).
2. Add the MCP server to the client config pointing at `https://mcp.asogenic.com/mcp` with the key in the `Authorization` header.
3. Provide `ASC_KEY_ID`, `ASC_ISSUER_ID` and `ASC_P8_PATH` (or `ASC_P8_PEM`) in that server's `env` block.
4. Verify with `asogenic_auth_status`, expecting `asc_configured: true` and `asc_valid: true`.

A plain-text runbook at `https://asogenic.com/setup` can be pasted into a compatible client.

## Configuration

```json
{
  "mcpServers": {
    "asogenic": {
      "url": "https://mcp.asogenic.com/mcp",
      "headers": {
        "Authorization": "Bearer <your key>"
      }
    }
  }
}
```

MCP OAuth discovery is not enabled yet, so clients asking for OAuth should use the API-key path until that compatibility layer ships.

## Business Relevance

- **Mobile growth teams** run the keyword research to metadata validation loop in one agent.
- **App marketers** update screenshots and listing copy without opening App Store Connect by hand.
- **Indie developers** get an ASO workflow that would otherwise need a paid tool plus manual submission.
- **Agencies** run the same pass across several client apps with per-account keys.

## Integration with CorpusIQ

ASOgenic covers the store-listing surface while CorpusIQ covers the business behind it. An agent can validate App Store metadata during a release and, in the same workflow, read the merchant's Shopify or Stripe data to see whether the release moved installs to revenue. The store listing is the acquisition end; CorpusIQ's connectors are the conversion and revenue end, so an operator can trace keyword change to revenue movement without a manual join.

## Limitations

- Brand new, no track record yet.
- Requires an ASOgenic account and App Store Connect credentials.
- MCP OAuth discovery is not yet enabled; the bearer API key is the supported path.
- The `.p8` key must be stored carefully in the client environment.
- App Store scope only, and submission still passes Apple's own review.

## FAQ

### Where does my App Store Connect key live?

In the MCP client's own environment. The ASOgenic server mints short-lived JWTs from it per request and never stores the key in the cloud.

### Is OAuth supported?

Not yet. The hosted endpoint currently supports a per-account bearer API key, which the docs recommend for unattended automation.

### How do I know the credentials are working?

Call `asogenic_auth_status`; you want `asc_configured: true` and `asc_valid: true`.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
