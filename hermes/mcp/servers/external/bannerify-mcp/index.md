---
title: "Bannerify MCP - Render Templates Into Images and PDFs"
description: "Turn a designed template and a row of data into a PNG, JPEG, WebP or PDF from chat, with the layers you are allowed to change."
category: Design
stars: ★★★ (401 + AuthKit metadata verified, 6 tools published)
added: 2026-10-29
source: "live probe of https://api.bannerify.co/mcp answering HTTP 401 invalid_token and RFC 9728 discovery at https://api.bannerify.co/.well-known/oauth-protected-resource naming AuthKit authorization server and resource_name Bannerify, plus the vendor documentation at bannerify.co/docs/mcp/overview read 29 October 2026"
relevance: ★★
tags: [design, image-generation, pdf, templates, open-graph, marketing-assets, oauth, remote-mcp]
last_updated: "2026-10-29"
---

# Bannerify MCP

**The image that ships with a hundred products is designed once and rendered a hundred times. When an assistant is asked for it, the answer is usually to generate a new picture from scratch, which is the one thing that guarantees it will not match the brand.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://api.bannerify.co/mcp
Auth:        OAuth with dynamic client registration, free account
Discovery:   https://api.bannerify.co/.well-known/oauth-protected-resource
Registry:    io.github/bannerify/bannerify
Docs:        bannerify.co/docs/mcp/overview
```

## Why This Matters for Operators

There are two different jobs behind "make me an image". One is inventing a picture, which the generation servers in this catalogue do. The other is rendering a picture that a designer already specified, with new text and new data, at the right size, in the right format. The second job is the one that runs a store, a blog and a social calendar, and it is the one a general image model is worst at, because re-rolling a design introduces new differences on every call.

This server renders instead of inventing. It lists your templates and the layers you can change in each, then renders an image or a PDF from one, in PNG, JPEG, WebP or PDF, in the same request. When no template fits, a second path composes a one-off image from shapes.

The boundary between those two paths is the useful part: the template path keeps the design fixed and varies the data, and the operator keeps control of what the design is.

## What Was Verified

A bare `initialize` POST to `https://api.bannerify.co/mcp` returned **HTTP 401** with `{"error":"invalid_token","error_description":"Missing bearer token"}`. The protected-resource document at `https://api.bannerify.co/.well-known/oauth-protected-resource` returned:

```
resource:               https://api.bannerify.co/mcp
authorization_servers:  https://progressive-cushion-36.authkit.app
bearer_methods_supported: header
resource_name:          Bannerify
resource_documentation: https://bannerify.co/docs/mcp/overview
```

The same document is served at `/.well-known/oauth-protected-resource/mcp`, which returned 200. The vendor's MCP page confirmed the endpoint, the Streamable HTTP transport, and that sign-in happens through the client rather than an API key, with a free Bannerify account and at least one template for the template tools.

## The Tools

Six tools are published on the submission:

- **`list_templates`** lists the templates available to the account.
- **`get_template`** returns one template and the layers that can be changed in it.
- **`get_project`** returns a project's context.
- **`create_image`** renders an image from a template, as PNG, JPEG or WebP.
- **`create_pdf`** renders a PDF from a template.
- **`create_image_from_shapes`** composes a one-off image when no template fits.

## Limits Worth Recording

Credential-gated by design, so the surface was catalogued on a 401 plus discovery metadata plus the vendor's published documentation, and the six tools are the vendor's list rather than a live `tools/list`.

A template needs a designer or a previous design. The value of this entry depends on having a template that is worth keeping fixed, and a business with no design system gets less from it than from a generation server.

The docs navigation also lists PDFs and a video path in beta, plus signed URLs and spreadsheet-driven generation, which are not part of the six published MCP tools and are therefore not claimed here.

## FAQ

### Do I need an API key?
No. It uses OAuth with dynamic client registration and a free account, and the client performs the sign-in. There is no key to paste.

### What formats can it return?
PNG, JPEG, WebP and PDF, with the format selected in the same request that renders the asset.

### Can it change only the text on a design?
Yes, that is the point of the template path. `get_template` shows which layers may be changed, so the agent varies data and leaves the design alone.

### What if the account has no suitable template?
`create_image_from_shapes` composes a one-off image from shapes instead, which is a composition of primitives rather than a rendered design.

### Where does the authorization server live?
It is hosted on AuthKit at `https://progressive-cushion-36.authkit.app`, named by the protected-resource document, which is how a client with MCP authorization discovers it automatically.
