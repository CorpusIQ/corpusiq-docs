---
title: "AnythingMCP - 732 Connectors and a Company Brain Behind One"
description: "An AGPL self-hosted gateway that registers tools at runtime from REST, SOAP, GraphQL, OData, SQL and IMAP sources, keeps a company knowledge graph"
category: "Business Systems"
stars: "775 (GitHub, 2026-11-11)"
added: 2026-11-11
source: "the mcpservers.org listing helpcode-ai/anythingmcp carrying a lastmod of 2026-11-11T09:09:28Z, the official registry record io.github.HelpCode-ai/anythingmcp at 0.10.0 read by exact name, the repository server.json declaring 0.53.0, README.md and docker-compose.quickstart.yml on main, the OAuth protected-resource and authorization-server documents on cloud.anythingmcp.com, Docker Hub metadata, the GitHub repository metadata, and a self-host attempt made on this host: engine pull, a forced amd64 pull, a Postgres 17 container brought healthy, and the app container's exit measured"
relevance: ★★★
tags: [mcp gateway, connectors, erp, sap, odoo, sql, soap, knowledge graph, memory, self-hosted, governance, agpl, docker]
last_updated: "2026-11-11"
---

# AnythingMCP

**The connector problem is that every system a company runs has its own idea of identity, and the agent is the only participant with none.** A customer exists in SAP, in Odoo, on a marketplace, and in a spreadsheet on a file server, with three identifiers and no relationship. AnythingMCP is an open-source, self-hosted gateway that answers both halves of that: it turns 700-plus named systems and any REST, SOAP, GraphQL, OData, SQL or mail source into MCP tools at runtime, and it keeps a knowledge graph of how those systems connect so an agent can link the customer to the orders without being told the join.

```text
Server type:  self-hosted gateway (Docker) or hosted cloud, Streamable HTTP
Hosted:       https://cloud.anythingmcp.com/mcp  -> 401 keyless, OAuth metadata present
Self-host:    http://localhost:4000/mcp behind a first-account bootstrap
Server:       registry record io.github.HelpCode-ai/anythingmcp is at 0.10.0
              repository server.json on main declares 0.53.0
Licence:      AGPL-3.0 (Community), Enterprise for SSO, SCIM, extended File Search
Image:        helpcodeai/anythingmcp:latest, 258.7 MB, amd64 only, 60,677 pulls
Install:      measured on this host and it does not start on arm64 (see below)
```

## The three connector counts, and which one is a measurement

There is no single number, and the gap between them is the honest finding:

```text
README header       732 connectors, 12,000+ tools, 42 need no API key
README feature table 696 catalog connectors, plus your own sources
registry record 0.10.0  255 connectors  (published earlier)
repo server.json 0.53.0  "732 connectors (SAP, ERP, SQL), file search, memory and skills"
```

The registry holds a **stale** record. Its exact-name lookup resolves `io.github.HelpCode-ai/anythingmcp` at version **0.10.0** described as *"255 connectors + any REST/SOAP/GraphQL/SQL as MCP tools for Claude & ChatGPT. Self-hosted, AGPL."* while the repository's `server.json` on main declares **0.53.0** with the 732-connector description and a declared remote at `https://cloud.anythingmcp.com/mcp`. One more quirk that will waste a later pass's time: a registry search for the product name `anythingmcp` returned **no** records, and only the fully namespaced `io.github.HelpCode-ai/anythingmcp` resolved it. Searching a registry by the name on the box is not the same query as searching it by the name in the record.

## What the hosted endpoint declares

A keyless `initialize` against `https://cloud.anythingmcp.com/mcp` answers **HTTP 401** with a JSON-RPC body, `{"code":-32001,"message":"Authentication required."}`, and `WWW-Authenticate: Bearer realm="AnythingMCP MCP Server", resource_metadata="https://cloud.anythingmcp.com/.well-known/oauth-protected-resource/mcp"`.

The two metadata documents disagree in a way a client has to handle:

```text
protected-resource   resource https://cloud.anythingmcp.com/mcp
                     authorization_servers [https://cloud.anythingmcp.com]
                     scopes_supported []            <- empty
                     bearer_methods ["header"], mcp_versions_supported ["2025-06-18"]

authorization-server issuer, /authorize, /token, /register
                     grant_types authorization_code, refresh_token, client_credentials
                     token_endpoint_auth_methods none, client_secret_post, client_secret_basic
                     scopes_supported ["openid", "email"]
                     code_challenge_methods ["S256"]
```

The resource document declares **no scopes at all** while the authorization server advertises only `openid` and `email`, so an MCP client cannot learn from discovery which capabilities its connection will carry. On a gateway whose whole purpose is per-tool authorization that is the one document worth fixing first: the consent screen is where an administrator is supposed to grant a narrow slice, and today the client has nothing to request. `client_credentials` in the grant list is also unusual for a per-person connector and worth understanding before an admin approves one.

## The self-host path, measured

The quickstart is deliberately short. A compose file pulls a published image, requires `JWT_SECRET` and `ENCRYPTION_KEY` (the app refuses to boot on placeholder values, by design), pins both ports to `127.0.0.1`, and starts a `postgres:17-alpine` behind it. The first account to register **becomes admin**, open registration is off afterwards, and the endpoint is `/mcp` on the API port with a `/health` probe.

This host is **aarch64**, and that is where the install stopped:

```text
podman pull helpcodeai/anythingmcp:latest
  -> choosing an image from manifest list: no image found in image index
     for architecture arm64, variant "v8", OS linux

podman pull --arch amd64 helpcodeai/anythingmcp:latest
  -> succeeded, digest 1ccaeb4533d4538069c6b9d09cdb7e1275c22a256745407ba6e63a92fcd64d78

podman run ... helpcodeai/anythingmcp:latest
  -> Exited (255) after 8 seconds
     exec /usr/local/bin/docker-entrypoint.sh: exec format error
```

The Postgres half is not the problem: `postgres:17-alpine` started on the same podman network and `pg_isready` answered *accepting connections* before the app was attempted. The blocker is that the published image is **amd64 only** with no arm64 manifest, and this host registers no amd64 binfmt handler, so the forced pull lands and then cannot execute. On an Apple Silicon laptop Docker Desktop ships its own emulation and the vendor documents the same pin working that way; on a Linux arm64 server the practical options are `qemu-user-static` binfmt registration or an amd64 machine. The repository states the cause plainly itself: arm64 is blocked upstream by a Prisma bug, and the quickstart comment says so.

Nothing was therefore driven: no `tools/list`, no connector, no knowledge graph, no audit line. What follows is the vendor's published design, read from the repository, and each claim is marked as theirs rather than measured here.

## What the vendor says it does

- **Runtime tools from any source.** 696 catalog connectors plus your own REST/OpenAPI, SOAP, GraphQL, OData, SQL, IMAP/SMTP or MCP source. Tools register at runtime, which is the difference between a fixed tool list and a system added on a Tuesday.
- **File search with page-level answers.** Indexes SFTP, FTP/FTPS, WebDAV (Nextcloud, NAS), S3 or a network share, every PDF page and Excel row with its column names, Outlook mails with attachments, and answers with file, page and date.
- **File share.** Expiring, revocable links for exported files, internal or public.
- **Company memory.** A fact saved in one AI client is found in another, personal and company scopes, with folders and role limits.
- **AI skills.** Written procedures, approved by an admin, learned from real requests and corrected errors.
- **Knowledge graph.** How the systems connect, so the customer in one system is linked to their orders in another without being told.
- **Code Mode.** Several tool calls collapse into one short program run in a sandbox with no secrets and no network; write access is Enterprise.
- **Governance.** Per-role, per-tool permissions, **response mapping that drops fields before they reach the model**, an audit log of every call, SSO and SCIM from the directory (Enterprise).

Editions as published: **Community** is free under AGPL-3.0 for commercial use up to **3 active users** with unlimited connectors and MCP servers; **Enterprise** adds users, single sign-on, SCIM, File Search beyond a 30-day trial and support. The hosted cloud is the same code run by the vendor in **Frankfurt** with a **7-day** trial, and the vendor states **16,000+ workspaces** and **1.5M+ AI tool calls a month**, vendor figures unverified from here. GitHub reads **775 stars**, 126 forks, repository created **2026-02-28**, pushed **2026-11-11**, **41** open issues, AGPL-3.0.

## Why it earns a page in this catalogue

Because it is the only entry here that treats the tool surface itself as the product, and an operator running four systems behind one assistant will recognise every part of it. The neighbours make the distinction concrete. [Cotlet MCP](/hermes/mcp/servers/external/cotlet-mcp/) solves the app-with-no-API problem by putting a real Chrome in the loop; AnythingMCP solves it by wrapping the API where one exists and requiring a connector definition where none does. [AgentKeyGate](/hermes/mcp/servers/external/agentkeygate-mcp/) answers "how does the agent use a key it never sees" from the credential side; AnythingMCP answers it from the platform side, storing the credential encrypted and dropping fields from the response before the model reads them. [n8n MCP](/hermes/mcp/servers/external/n8n-mcp/) automates a workflow, [Tuqui MCP](/hermes/mcp/servers/external/tuqui-odoo-mcp/) reads one ERP, and [mcp-billing-gateway](/hermes/mcp/servers/external/mcp-billing-gateway/) meters what a call costs.

**The limits, plainly.** No handshake was completed and no tool was called, so every capability above is the vendor's description rather than a measured surface. The image does not run on this architecture, the protected-resource document declares no scopes, the registry record is three minor versions behind the repository, and the connector count reads 732, 696 or 255 depending on which document you open. The starting move for an operator on amd64 is the quickstart compose and a first account, which makes the admin bootstrap and the per-tool permission screen verifiable in about half an hour; on arm64, register the binfmt handler first or do not start.
