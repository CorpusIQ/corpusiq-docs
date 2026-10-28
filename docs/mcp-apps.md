---
title: "MCP Apps - Interactive UI Inside the Chat"
description: "MCP Apps render an interactive HTML interface inside the AI chat. How the extension works, its sandbox security model, client support, and what to verify."
canonical: "https://www.corpusiq.io/docs/mcp-apps/"
robots: "index,follow"
last_updated: "2026-10-28"
tags: ["mcp apps", "model context protocol", "interactive ui", "mcp server"]
---

# MCP Apps: interactive answers instead of walls of text

A business question usually ends the same way in an AI chat. A paragraph of prose, three numbers buried inside it, and a source you have to take on faith.

MCP Apps change the delivery, not the data. The server returns an interactive interface that the AI client renders inside the conversation. Tables, charts, filter controls, and source lists, in the same thread where you asked the question.

This page explains the mechanism, the security model, and the questions worth asking before you trust a vendor claim about it.

## The short version

- A tool declares that it has a user interface, using a `ui://` resource reference in its metadata.
- The client fetches that resource. It is an HTML page, usually with its CSS and JavaScript bundled in.
- The client renders it in a sandboxed iframe inside the chat.
- The page talks to the client over `postMessage`, and can call the server's tools through that channel.
- If the client does not support the extension, the tool falls back to text or structured data.

Nothing about the answer changes. The numbers still come from your connected tools. What changes is whether you read them or see them.

## How rendering actually happens

MCP Apps is an extension to the core Model Context Protocol specification, not a replacement for it. The core stays: tools, resources, prompts, transports. The extension adds one binding between a tool and a piece of interface.

**1. The tool declares its interface.** The tool descriptor carries a `_meta.ui.resourceUri` field pointing at a `ui://` resource. That declaration is what lets the client preload the interface before the tool is even called, so the surface is ready when the data arrives.

```json
{
  "name": "business_recap",
  "description": "Summarise this week across connected sources.",
  "inputSchema": { "type": "object", "properties": {} },
  "_meta": {
    "ui": {
      "resourceUri": "ui://corpusiq/visual-recap-v2.html"
    }
  }
}
```

**2. The client fetches the resource.** Resources are served as `text/html` pages with a profile that marks them as app views, commonly declared as `text/html;profile=mcp-app`. Servers may also advertise the extension identifier `io.modelcontextprotocol/ui` during initialization, which tells the client up front that app views exist.

**3. The client renders it in a sandboxed iframe.** The iframe sits inside the conversation. The declared `_meta.ui` object can carry a `csp` list of allowed external origins and a `permissions` block for optional capabilities such as camera or microphone. Anything not declared is not reachable.

**4. The two sides talk over JSON-RPC.** The app and the host exchange messages through `postMessage`. Some methods mirror core MCP, such as `tools/call`. Others belong to the extension, such as `ui/initialize`. Through that channel the app can request tool calls, receive fresh results, and update the model's context.

The practical consequence: an app view is not a screenshot and not an image. It is live code with a narrow, host-controlled channel back to the data.

## Why this matters for business answers

Text is a lossy container for a business answer. The reader has to reconstruct the table in their head, guess which figures are comparable, and hunt for where a number came from.

An app view fixes the three failures that matter most in operator work:

| Failure with text-only answers | What an app view does |
|---|---|
| Numbers arrive without shape | Renders the table or chart, with units and periods visible |
| Sources are asserted, not shown | Lists the source record per row, so a figure can be traced |
| Every follow-up needs another prompt | Keeps controls in place, so a different period or segment is one click |

It also keeps the work in one place. A linked dashboard lives behind a separate login, a separate tab, and a separate mental bookmark. The app view lives in the thread that produced it, next to the reasoning that led there.

## The security model, stated plainly

An app view runs code written by the server author inside a client the user trusts. That arrangement only works because of the sandbox, so it is worth knowing exactly what the sandbox does and does not do.

**What it prevents.** The iframe cannot reach the parent page's DOM, cannot read the host's cookies or local storage, cannot navigate the parent frame, and cannot execute script in the parent context. All communication crosses one boundary: `postMessage`.

**What the host controls.** The client decides which tools an app may call and which capabilities it may use. A host can narrow or disable features per app. The app does not set its own permissions.

**What the app declares.** External origins it needs to load from, through `csp`. Optional capabilities it wants, through `permissions`. Declaring them is not the same as receiving them.

**What the sandbox does not decide.** Whether the data behind the view is correct, whether the server retains anything, and whether the tool is read-only. Those are properties of the server, not the rendering layer. A polished interface is not evidence of a sound data path. Judge the server on its own terms, then judge the interface separately.

## Which clients support it

Support is an extension-level property, and it moves. At the time of writing the clients documented as supporting MCP Apps include Claude, Claude Desktop, VS Code GitHub Copilot, Microsoft 365 Copilot, Goose, Postman, MCPJam, and Archestra.AI. ChatGPT is not on that list, because ChatGPT ships its own app and widget platform rather than the extension.

Two rules follow from that:

1. **Always check the client matrix, not a vendor's marketing page.** Extension support is listed per client and changes with client releases.
2. **The fallback is part of the contract.** Any server that only works when the interface renders is a server that breaks on every other client. Text and structured data must carry the same answer.

## How CorpusIQ uses it

CorpusIQ serves app views as versioned resources, with a canonical `ui://` URI per release and every previously issued URI kept readable as a compatibility alias. Tool descriptors point at the current canonical URI. The version is in the URI because cached HTML and stale markup are the same problem wearing different clothes.

Three properties are deliberate:

- **The view is a renderer, not a second data path.** The interface reads the same tool result the text answer uses. It cannot widen what the connector can reach.
- **Every view degrades.** Where the client does not render app views, the same tool returns the structured result as cited text.
- **The interface is served by us, not by the client.** That is the difference between a branded answer and a paragraph that any other server could have produced.

For ChatGPT, CorpusIQ uses OpenAI's own app surface rather than the MCP Apps extension. For Claude and other clients that support the extension, the `ui://` resources are served directly. The data layer underneath is the same in both cases.

The MCP transport, tool naming, and scoping are covered in [MCP architecture](how-it-works/mcp-architecture.md). The data-retention rules that apply to every view are in [Privacy and security](how-it-works/privacy-and-security.md). The short community-hub summary of the same extension is [MCP Apps: interactive UIs inside Claude](hermes/mcp/mcp-apps-interactive-ui.md).


## What to check before trusting an "interactive" claim

A vendor can say "interactive" about a static image, an embedded chart, or a link to a dashboard. Four checks separate the real thing from the label:

**1. Is there a resource, or only a picture?** Ask for the `ui://` URI. If the answer is an image or a screenshot, there is no app view.

**2. Is the tool actually bound to it?** The descriptor carries `_meta.ui.resourceUri`. Without that binding, the interface is decorative, because the client cannot associate it with a tool result.

**3. Does it degrade?** Disconnect the interface. If the answer becomes unusable, the server treats rendering as a requirement rather than a presentation choice.

**4. Is the interface versioned?** Cached markup outlives fixes. A canonical URI that changes with every release, with old URIs kept alive as aliases, is the sign of a team that has shipped one before.

## FAQ

**Does an MCP App mean the AI can change my data?**
Not by itself. The extension governs rendering and the message channel between the view and the client. Write access depends on the tools the server exposes and the permissions granted at connect time. CorpusIQ's external retrieval is read-only, and configuration controls are separately scoped.

**Do app views work in every AI client?**
No. Support is per client and per extension version. Check the client matrix for the assistant you use, and confirm the server returns a usable text answer without the interface.

**Is my data copied into the interface?**
The view renders the result of the tool call the client already made. Whether anything is stored afterwards is a server property, not a rendering property, so read the retention terms of the server rather than inferring storage from the interface.

**Why does the interface live inside the chat instead of a link?**
Because the context does. A view rendered in the thread keeps the question, the answer, the sources, and the controls in one place, with no second login and no lost bookmark.

**How do I tell a good app view from a polished static one?**
Interact with it. Change the period, change the segment, click a source. If the state moves and the source list follows, it is a live view. If nothing responds, it is a picture with a nice border.

---

Ready to see the difference on your own data? [Connect a source](https://corpusiq.io) and ask a question that has a table for an answer.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*

