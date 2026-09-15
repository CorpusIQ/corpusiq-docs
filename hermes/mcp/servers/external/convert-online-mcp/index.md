---
title: "Convert.Online MCP - File Conversion for AI Assistants"
description: "Remote MCP server that converts files between 400+ formats - images, video, audio, documents, ebooks, fonts and CAD - from inside the conversation. Five tools: list formats, list options, upload a local file, convert, and check a job. OAuth or API key at mcp.convert.online; also in the official MCP registry as online.convert/file-converter."
category: Productivity
stars: n/a (new listing)
added: 2026-09-14
source: "mcpservers.org /all page 1 (Sep 14 evening crawl) + vendor docs at convert.online"
relevance: ★★
tags: [file-conversion, productivity, formats, documents, images, video, audio, oauth, api-key, remote-mcp, official-registry]
---

# Convert.Online MCP

**Convert any file without leaving the conversation.** Convert.Online runs file conversion as an MCP server: images, video, audio, documents, ebooks, fonts and CAD across more than 400 formats. An assistant lists what can convert to what, checks the options a given conversion accepts, uploads a local file when it is not on the web, converts, and returns a download link.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (recommended) or API key
Endpoint: https://mcp.convert.online (401-verified live, Sep 14 2026)
Tools: 5
Registry: online.convert/file-converter (official MCP registry) and Smithery
Pricing: Conversions count toward your Convert.Online plan
Category: Productivity
```

## Why This Matters for Operators

File format friction is small until it is constant: a client sends a .pages file, a vendor portal wants TIFF, the podcast needs MP3 at a specific bitrate, the print shop wants a font family packaged, and every request means finding the right web tool and re-uploading. This server makes conversion a sentence: "convert this deck to PDF and give me a link", "make a web-ready MP4 from this MOV", "what can this DXF convert to?"

Because the assistant can read the conversion's own options list, it picks exact settings (quality, size, codecs) rather than guessing, and every conversion runs on your account with the result returned as a download link.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `list_formats` | All input formats, or the targets a given input can convert to |
| `list_options` | The settings a specific conversion accepts, with exact names |
| `create_upload` | Send a file from your device when it is not on the web; any size |
| `convert` | Convert from a source URL or an uploaded file; returns a job id and a download link when ready |
| `get_job` | Check a conversion's status and fetch its result |

## Installation

**Recommended (OAuth):** in your assistant, add a custom connector (sometimes called an MCP server) and paste the URL:

```
https://mcp.convert.online
```

Sign in, press Allow, and conversions run on your account. The assistant never sees your password or a key; it receives a revocable token only. Revoke anytime from the dashboard.

**Alternative (API key) for config-file clients:** create a key at Dashboard, API Keys, then:

```json
{
  "mcpServers": {
    "convert-online": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.convert.online",
        "--header", "Authorization: Bearer YOUR_API_KEY"]
    }
  }
}
```

Any MCP client can connect the same way by pointing at `https://mcp.convert.online` with the Authorization header.

**Client support at catalog time:** Claude is verified end to end. ChatGPT offers custom connectors in developer mode but its sign-in does not complete (a known issue affecting other MCP servers too). The consumer Gemini app has no custom-connector option yet; Gemini Enterprise and the Gemini CLI do.

## Business Relevance

- **Ops and admin teams** convert the file the client actually sent into the format the portal actually wants.
- **Marketing teams** produce web-ready media variants (format, size, codec) without a desktop converter.
- **Agencies** standardize deliverables: every handoff in the same formats, produced the same way.
- **Anyone who receives files** in the wrong shape gets a one-line fix instead of a tool hunt.

## Integration with CorpusIQ

Conversion is plumbing; the value is what flows through it. With a CorpusIQ connection, the same assistant reads the business data behind the file - invoices and books from QuickBooks, orders from Shopify, revenue from Stripe, traffic from GA4 - with source-cited answers, and then uses Convert.Online to reshape the output: a report exported as PDF, a chart sheet as an image, a deck as slides. Analysis, verification and formatting chain in one conversation.

## Limitations

- **Plan-based pricing**: conversions count toward your Convert.Online plan; per-conversion costs are not enumerated on the listing.
- **OAuth requires a browser**; headless setups need an API key instead.
- **ChatGPT sign-in does not currently complete** (platform issue, not specific to this server); Claude is the verified client.
- **API key is your credential**: treat it like a password and revoke from the dashboard if leaked.
- **New listing** with no third-party track record at catalog time.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
