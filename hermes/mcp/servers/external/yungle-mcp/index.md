---
title: "Yungle MCP - File Delivery and Receipts for AI Agents"
description: "Send large files from an AI assistant as private download links, with transfer receipts and approval on every emailed send."
category: Productivity
stars: 1
added: 2026-09-29
source: mcpservers.org
relevance: ★★
tags: [file-transfer, file-sharing, downloads, webhooks, delivery, receipts, oauth, remote-mcp]
---

# Yungle MCP

**Private, resumable file delivery from your assistant.** Yungle is a WeTransfer alternative built for AI workflows: an MCP server, CLI, typed SDKs and webhooks over one public REST API, with EU-hosted (Germany) storage. The assistant shares files as download links and tracks who downloaded what - and every emailed send waits for your approval.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth browser sign-in, no key to copy
Endpoint: https://yungle.co/mcp
Tools: transfers (send, list, status), receipts (who downloaded what), expiring links, approval-gated emails
Pricing: Free tier; paid plans add webhook events and collections (yungle.co)
Category: Productivity
Built by: Hein De Wilde (github.com/heindewilde/yungle-clients, MIT)
```

## Why This Matters for Operators

Client file delivery is a small task that eats real time - uploading renders, chasing confirmations, re-sending after a missed deadline. Yungle gives that whole loop to an assistant: ask what arrived, share files, and approve every send before an email leaves. Uploads resume after a dropped connection or a closed laptop lid, so large renders survive flaky networks.

The safety model is designed for agent use. There is no tool that deletes, revokes or invites, and everything the server returns is labelled as untrusted data because a filename can carry a prompt injection. A browser sign-in can make links but never email anyone, so a phished sign-in code cannot be used to mail strangers.

## Tools & Capabilities

| Capability | Purpose |
|---|---|
| Send transfers | Share files or folders as private links, with resumable uploads and expiry |
| Transfer status | Who downloaded what, and which deliveries expire this week |
| Receipts | Download receipts per recipient, surfaced through webhook events |
| Approval gate | Every emailed send is prepared by the assistant and confirmed by you |
| Expiring links | Time-boxed links for confidential deliveries |

Tool names are served from the endpoint; the REST API is OpenAPI 3.1 documented at yungle.co/developers/reference, and the CLI, TypeScript and Python SDKs cover the same surface.

## Installation

```bash
claude mcp add yungle --transport http https://yungle.co/mcp
```

Sign in once through the browser - no key to copy. In Claude's connector directory, add Yungle and sign in. For a local server with an API key instead, `yungle mcp install` writes the config for Claude Desktop, Claude Code, Cursor or Windsurf.

## Configuration

```json
{
  "mcpServers": {
    "yungle": {
      "url": "https://yungle.co/mcp"
    }
  }
}
```

## Business Relevance

- **Creative and production teams** deliver large renders to clients with download receipts instead of chase emails
- **Agencies** send final assets with expiry windows and webhook-driven status tracking
- **Consultants** hand over deliverables from the assistant, with every emailed send approved
- **Dev shops** wire CI build artefacts to clients through the GitHub Action

## Integration with CorpusIQ

Yungle covers delivery while CorpusIQ covers the engagement. A composed workflow: CorpusIQ assembles the deliverable context through its connectors - invoice status from QuickBooks, project data from the CRM, usage from GA4 - and the assistant prepares the delivery through Yungle with an approval step before the email goes out. Webhooks then close the loop: transfer downloaded, project updated, next step scheduled.

## Limitations

- Young project (1 GitHub star); the API surface is stable but the vendor ecosystem is new
- No delete, revoke or invite tools by design - transfers expire, they are not recalled
- Free tier limits; webhook events for collections require a paid plan
- Email sending requires either an API-key sign-in or an explicit confirmation per send

## FAQ

### Can the assistant email files without my approval?

No. A browser sign-in makes links but never emails anyone, and every emailed send is prepared by the assistant and confirmed by you before it leaves.

### What happens if an upload is interrupted?

Uploads are resumable: re-run the send and it continues from the last committed part instead of starting over.

### Where are files stored?

Files are hosted in the EU (servers in Germany), with private links and optional expiry windows.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
