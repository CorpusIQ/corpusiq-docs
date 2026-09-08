---
title: JsonCut MCP - Video and Image Authoring for Agents
description: Give an external agent focused access to JsonCut editable projects, media, templates, visual review and rendering. Bounded edits, upload tickets, review frames and pinned renders through a hosted endpoint with an X-API-Key header.
category: Content
stars: n/a (new listing)
added: 2026-09-08
source: mcpservers.org
relevance: ★★
tags: [video-editing, image-editing, creative-production, rendering, templates, media, remote-mcp]
---

# JsonCut MCP

**Remote MCP server (Streamable HTTP, API key)** - JsonCut gives an external agent focused access to editable projects, media, templates, visual review and rendering. The V2 tool family (jsoncut_v2_*) carries a full authoring loop: read the authoring guide, work in durable projects, upload media through short-lived tickets, make bounded edits, review visual frames, then render the pinned final version.

```
Server type: Remote (Streamable HTTP)
Auth: API key (X-API-Key header)
Endpoint: https://mcp.jsoncut.com/mcp
Tools: jsoncut_v2_* authoring set (projects, templates, media, review, render)
Pricing: JsonCut platform plans
Category: Content
Built by: JsonCut (jsoncut.com)
```

## Why This Matters for Operators

Video and image production for agents usually means handing a prompt to a generator and hoping the output survives review. **JsonCut MCP gives the agent an editing surface instead**: a project holds the media and its optimistic version, edits are bounded to what changed, and visual review frames or a contact sheet come back before anything is committed to a render. The agent can repair only visible problems and pin the final version - the loop a human editor would run, compressed into tool calls.

The upload-ticket design matters for operators with private assets. Large or private local files go through a one-shot ticket scoped to a single project or template that expires in 60 to 900 seconds and reveals no object-storage credentials - so a production asset never leaves a controlled path.

## Tools & Capabilities

| Area | Capability |
|---|---|
| Authoring guide | `jsoncut_v2_get_authoring_guide` - read once at the start of a creation task |
| Projects | Create and work in durable projects for iterative image or video work |
| Templates | Search templates and read `jsoncut_v2_get_template_inputs` to satisfy the discovered contract |
| Media | Bounded Base64 upload for small files; `jsoncut_v2_create_upload_ticket` for large or private files |
| Editing | Bounded edits preserving the current optimistic version |
| Review | Request visual review frames or a contact sheet before rendering |
| Rendering | Render the pinned final version |

A legacy V1 endpoint (https://mcp.jsoncut.com/legacy/mcp) remains frozen for JSON-job compatibility - new integrations should use the V2 endpoint only, never both.

## Installation

```bash
claude mcp add jsoncut --transport http https://mcp.jsoncut.com/mcp
```

Full V2 tool reference and recommended agent loops: https://jsoncut.com/docs/mcp-tools/

## Configuration

```json
{
  "mcpServers": {
    "jsoncut": {
      "type": "http",
      "url": "https://mcp.jsoncut.com/mcp",
      "headers": {
        "X-API-Key": "${JSONCUT_API_KEY}"
      }
    }
  }
}
```

Send the JsonCut API key as the X-API-Key header and grant only the scopes needed for projects, templates, media, renders and resource discovery.

## Business Relevance

- **Creative teams** get an agent that edits inside real projects instead of generating throwaway one-shots
- **Marketing operators** reuse brand templates by contract, with render values validated against discovered template inputs
- **E-commerce teams** iterate product visuals with review frames before paying for final renders
- **Agencies** keep client work separated by scoped API keys and durable projects

## Integration with CorpusIQ

JsonCut complements the CorpusIQ analytics and commerce connectors: GA4 and Shopify surface the products and campaigns worth creative investment, and JsonCut turns that signal into edited, reviewed, rendered assets. The composed workflow is pick-a-winner-then-produce-the-asset - CorpusIQ reads the business to find the product or angle, JsonCut executes the creative edit loop, and the review-frame step keeps a human in control of what ships.

## Limitations

- Brand new listing (September 7, 2026) - no track record yet
- API-key auth with scoping discipline required per integration
- Hosted only - no self-host option
- V1/V2 endpoint split can confuse legacy clients (V1 is frozen, feature development is V2-only)
- Render and media costs sit on the JsonCut platform plans

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Shotstack MCP - Video Editing API for AI Agents](/hermes/mcp/servers/external/shotstack-mcp/)
- [Treza MCP - AI Video Pipelines to Social Channels](/hermes/mcp/servers/external/treza-mcp/)
