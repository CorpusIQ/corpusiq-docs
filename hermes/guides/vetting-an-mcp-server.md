---
title: "How to Vet an MCP Server Before You Connect It"
description: "A 10-minute operator checklist for MCP servers: read the tool list before authorizing, probe the endpoint, inspect the OAuth discovery document, and decide what the server is allowed to see."
category: guides
tags: ["mcp server", "security", "oauth", "tool review", "model context protocol"]
last_updated: 2026-10-21
canonical: "https://www.corpusiq.io/docs/hermes/guides/vetting-an-mcp-server/"
robots: "index,follow"
---

# How to Vet an MCP Server Before You Connect It

An MCP server is a program that receives your credentials, reads data on the other side of them, and writes text that a language model then treats as context. Connecting one is a small but real security decision.

Most operators approve that decision in four seconds: click connect, accept the OAuth screen, ask a question. The vetting below takes about ten minutes and replaces the click with evidence.

You do not need to read source code to do it. You need to look at four artifacts: the tool list, the transport handshake, the OAuth discovery document, and the vendor's maintenance trail.

## Step 1: Read the tool list before you authorize anything

Every MCP server publishes its tools. You can ask for them without an account, and a server that refuses to list tools before authentication is telling you something useful: the tool list itself is gated.

```bash
curl -s -X POST https://mcp.example.com/mcp \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"probe","version":"0.1"}}}'
```

Then call `tools/list` with the same endpoint. What you are looking for is not the number of tools. It is the verb in each tool name.

| Tool name pattern | What it means | Default posture |
|---|---|---|
| `get_*`, `list_*`, `search_*`, `read_*` | Reads data and returns it | Acceptable with a read-scoped credential |
| `create_*`, `update_*`, `delete_*`, `send_*` | Changes state on the vendor side | Needs a reason, an owner, and a separate credential |
| `run_*`, `execute_*`, `invoke_*` | Runs code or calls arbitrary endpoints | Treat as remote code execution until proven otherwise |

A server that offers nine read tools and one `delete_customer` hands your model all ten. If the agent can choose a tool, the agent can choose that one. Read-only access is enforced by the credential you issue, not by the description you read.

## Step 2: Count the tools rather than trusting the marketing

Vendor pages say "40+ tools". The tool list says how many exist. Count them, then check whether the count on the landing page matches the count in `tools/list`.

A mismatch is not always a lie. It is always worth one sentence of doubt: the page may describe an older version, a paid tier, or a roadmap. But if the page promises a capability and the list does not contain it, connect accordingly.

Also read the description text of each tool. Descriptions are prompt context. A description that instructs the model how to behave beyond the tool's own job, or one that embeds instructions to fetch and follow external content, is a tool-poisoning pattern. You are not being paranoid; the description is literally part of the prompt the model receives.

## Step 3: Probe the handshake to learn what you are connecting to

The `initialize` response tells you the protocol version, the server name and version, and which capabilities the server claims.

```json
{"result": {"protocolVersion": "2025-06-18",
            "serverInfo": {"name": "example-tools", "version": "1.4.0"},
            "capabilities": {"tools": {}, "resources": {}}}}
```

Three things to record:

- **Transport.** A remote endpoint over Streamable HTTP is reachable by the vendor and by anything that holds the token. A local stdio server runs on your machine and can touch your filesystem. Those are different risk shapes and they deserve different credentials.
- **Protocol version.** An endpoint pinned to an old protocol revision will drift out of compatibility with newer clients. Not fatal, but a maintenance signal.
- **Capabilities.** `tools` is normal. `resources` means the server can push content into context, not just answer calls. `sampling` means the server can ask your client to run a model call of its own choosing.

## Step 4: Read the OAuth discovery document

If the server uses OAuth, it publishes how. Two well-known paths cover most deployments:

```
/.well-known/oauth-authorization-server
/.well-known/oauth-protected-resource
```

From the first document you can see the grant types, whether PKCE with S256 is required, whether dynamic client registration is open, and where tokens are issued. What you want to see:

- `authorization_code` with PKCE S256 for interactive use
- `refresh_token` so the connection does not silently die every hour
- a token endpoint on the vendor's own domain, not a redirect through an unrelated host

What you do not want to see: an implicit grant, a password grant, a token endpoint on a domain that has nothing to do with the vendor, or no discovery document at all alongside a promise of "secure OAuth".

If the server takes a static API key instead, the key is the whole security model. Create it as a separate key, name it after the integration, scope it to read-only if the vendor allows scopes, and set an expiry.

## Step 5: Decide the blast radius before the first call

Answer these four questions in writing, in your own notes, before you connect:

| Question | Why it matters |
|---|---|
| Which systems does this server reach? | One server that touches both billing and marketing data has the union of both risks |
| Can its credential write anywhere? | A read-only token turns a bad tool into a failed call instead of a changed record |
| Who else holds that credential? | Shared keys remove your ability to tell who did what |
| What happens at revocation? | You want a one-click revoke that does not break unrelated integrations |

If you cannot answer the first question, you do not yet know what you are connecting. Start with the narrowest scope the vendor offers and widen only after the first workflow proves useful.

## Step 6: Check the maintenance trail

A server is a dependency. Dependencies get abandoned, and an abandoned server with a live token is a standing risk. Look for a version number in `serverInfo`, a changelog or release history, an issue tracker with recent activity, and documentation that names the vendor's own domain.

The weakest signal is a directory listing. Directories are self-serve, they list servers that have never answered a request, and a card on a marketplace page is not evidence that the endpoint runs. The strongest signal is a successful `initialize` against the live endpoint today.

## Red flags that end the review

- Tools that execute arbitrary commands, shell strings, or URLs, presented as a convenience
- A tool description that tells the model to ignore previous instructions, or to fetch and follow external content
- Credentials requested for a system the advertised tools never touch
- OAuth with no PKCE, or a redirect URI that leaves the vendor's domain
- No discoverable tool list, no version, no documentation, no repository
- A directory listing as the only evidence the server exists

## What to keep in your inventory

For each server you connect, record five fields: the endpoint, the transport, the credential scope, the date you last probed it, and the owner inside your team. That table answers the two questions that actually arrive later: what can this agent reach, and who do we ask before turning it off.

## Where this fits

MCP turns a chat window into an interface to real systems. The same property that makes it useful, a model that can call tools against your data, is the property worth ten minutes of inspection.

The order is always the same: read the tools, probe the endpoint, read the discovery document, narrow the credential, then connect.

*← [All guides](index.md) | [MCP servers for business operators](mcp-servers-business-operators.md) | [MCP Guide](/hermes/mcp)*

*↑ [Section Home](/hermes/guides)*
