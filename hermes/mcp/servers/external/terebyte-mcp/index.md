---
title: "Terebyte MCP - One Encrypted Room for an Agent"
description: "Give an agent a single room in an encrypted vault, opened by a six-character code, with the scope and the clock chosen by the owner."
category: Storage
stars: ★★★ (pairing model and package verified, v0.1.1)
added: 2026-10-29
source: "npm package terebyte 0.1.1 (Apache-2.0, bin terebyte) read from the npm registry on 29 October 2026 and the vendor submission with its pairing flow and tool scope"
relevance: ★★★
tags: [storage, encryption, files, least-privilege, pairing-code, sealed-link, local-mcp]
last_updated: "2026-10-29"
---

# Terebyte MCP

**Handing an agent a drive is how people hand it everything. The interesting design question is not whether an agent can read your files, but which ones it was ever able to see.**

```
Server type: Local (stdio)
Install:     npx -y terebyte mcp
Package:     terebyte 0.1.1 on npm, Apache-2.0
Runtime:     Node 22 or newer
Pairing:     6-character code, approved in the Terebyte app
Scope:       one room, permissions and duration chosen by the owner
Crypto:      encrypted and decrypted on the machine that runs the server
```

## Why This Matters for Operators

Every file-oriented connector in this catalogue has the same shape: a credential opens a store and the agent can reach whatever that credential reaches. For a business holding client documents, that is the wrong default, because the scope of the grant is the whole account and the grant does not expire by itself.

Terebyte inverts it. The agent gets **one room** and the vendor states the boundary as the product: it sees that room and nothing else. The member opens that room to the agent deliberately, pairs with a **six-character code** typed into the Terebyte app, and chooses **what the agent may do and for how long**. Terebyte is end-to-end encrypted, and everything is encrypted and decrypted on the computer running the server, so the vendor's own servers see sealed bytes.

For an operator the practical version is this: a client's documents can sit in a room, a working session can be opened to an assistant with a clock on it, and the rest of the vault is not part of the conversation at all. That is a consent design rather than an access-control setting, and it is the reason this entry exists.

## What It Does

The submission names the operations the agent performs inside the room: list, read and write files, make a **Sealed Link**, and use the room's board. The pairing is not a config file with a token in it. The first call prints a six-character code, the member opens Rooms, Connect an agent in Terebyte, types the code and approves the door.

```json
{
  "mcpServers": {
    "terebyte": {
      "command": "npx",
      "args": ["-y", "terebyte", "mcp"]
    }
  }
}
```

The one-line install the vendor publishes is `claude mcp add terebyte -- npx -y terebyte mcp`, and the npm package is `terebyte` **0.1.1**, Apache-2.0, with a single `terebyte` binary. Note the package name has no hyphen and no scope: `terebyte`, while the product is Terebyte.

## What Was Verified

The npm registry entry for `terebyte` resolved on 29 October 2026 at version **0.1.1**, licence **Apache-2.0**, with the description stating the pairing model directly: pair with a member's app by a six-character code, then read and write the rooms they open to you, encrypted on this computer. The package declares a `terebyte` bin. The registry record carries no repository URL, so the package and the vendor site `terebyte.com/connect` are the published evidence rather than a public source tree.

## Limits Worth Recording

This is an early package at **0.1.x**, so the surface is expected to move and no tool count is asserted here.

The pairing code is a bootstrap, not a credential to reuse. It is typed in by the member and paired to a connection, and the permission and duration the member sets are the actual control.

Encrypted at the client means the vendor cannot recover a lost key, which is the honest trade in every end-to-end design and should be stated to whoever owns the room before documents go in.

## FAQ

### How does the agent get access?
It does not get a token in a file. The first call prints a six-character code, the member enters it in the Terebyte app under Rooms, Connect an agent, and approves the door.

### What can the agent see?
One room that the member opened to it, and nothing else in the vault. The member sets what it may do and for how long.

### Where does encryption happen?
On the computer running the server. Terebyte's servers hold sealed bytes, so the plaintext never leaves the machine that has the key.

### What can a Sealed Link do?
It is the sharing primitive the server exposes inside the room, alongside file read and write and the room's board.
