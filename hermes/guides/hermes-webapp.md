---
title: "Run the Hermes Desktop Workspace in a Browser Tab"
description: "The Hermes Webapp serves the Desktop workspace from your own gateway: how to turn it on, what a signed-in tab can do, and how to expose it safely."
category: guides
tags: ["hermes agent", "webapp", "desktop", "remote access", "gateway"]
last_updated: "2026-11-12"
canonical: "https://www.corpusiq.io/docs/hermes/guides/hermes-webapp/"
robots: "index,follow"
---

# Run the Hermes Desktop Workspace in a Browser Tab

An agent that only exists on the machine in front of you is a tool you use when you are at that machine. The rest of the day it is a process you hope is still running, checked through a terminal that is also on that machine.

Hermes Agent v0.23.0 closed that gap. The Webapp serves the Desktop workspace from your own gateway, so the same chats, Group Chats, plugins and settings open in a browser tab on any device that can reach the gateway. Nothing leaves your hardware, and nothing is provisioned for you in someone else's cloud.

This guide covers turning it on, what a signed-in tab can actually do, and the exposure decision that comes with it.

## What the Webapp is, and what it is not

The Webapp is the Desktop workspace rendered by your gateway and served over HTTP. It is not a hosted product, not a second agent, and not a sync service. The bundle is shipped by the Docker image and the Nix package as of v0.23.0, and the workspace it serves is the same one native Desktop uses: the same session list, the same Group Chats, the same installed plugins, the same settings.

It is **off by default**. Nothing is served to a browser until you turn it on, either by setting `webapp.enabled: true` in the gateway configuration or by enabling Web Access in Desktop's settings. Once enabled, `hermes webapp` opens it, and the same screen offers serving it on your local network or behind a public URL with sign-in.

The distinction matters for how you reason about it. A hosted chat product terminates your session on infrastructure you do not control. The Webapp terminates it on the gateway you already run, which means the security question is not "do I trust the vendor" but "who can reach this port".

## One user, not a team workspace

The Webapp is single-user by design. A signed-in tab acts as you: the sessions and Group Chats it shows are the same ones native Desktop shows, not copies, and display settings follow you across devices that talk to the same machine.

That is the useful property and the limit in one sentence. Useful, because you can start a task at the desk and check on it from a laptop or a phone without moving state anywhere. Limited, because there is no per-seat isolation, no separate profile per viewer, and no permission boundary between two people sharing one signed-in tab. If two people need to use the same agent, they need two profiles; if they need different access, the answer is a different gateway, not a second login.

Treat a signed-in tab as equivalent to an open terminal on that host. That is what it is.

## What a signed-in tab can do

The workspace is the Desktop app, so the surface is wide. From a tab you can read and continue sessions, open and manage Group Chats, install and manage plugins, and change settings. Desktop plugins load inside the Webapp tab, and the tab can install desktop-only plugins, pinned to the commit the install dialog showed.

Recent release notes describe the room list being shared between Desktop and the Webapp, so a Group Chat started in one appears in the other, and each bot shows what it is doing live.

Two operational details are worth knowing before you rely on it. The page sends a Content-Security-Policy, and launch links are private to the signed-in user, so a link pasted into a shared channel does not open someone else's workspace. And when the bundle fails to boot, the page shows a Reload notice instead of a blank tab, which turns a mysterious white screen into a known failure state.

## Exposing it without handing over the machine

The gateway trusts its own bound loopback port for CORS and WebSocket origins, and the same rule covers the Webapp, the dashboard and `hermes serve`. Do not point a proxy at it from a different origin and expect the browser to cooperate; serve it from the port it bound.

For reach, pick the boring option. A tailnet, a VPN, or an SSH tunnel keeps the listener off the public internet and gives you a normal authentication boundary in front of it. A public URL with sign-in is fine when the sign-in is real and the gateway sits behind it, but it is the option you should reach for last, not first.

Four habits cover most of the risk:

- Keep it off until you need it. `webapp.enabled: true` is a decision, not a default.
- Bind it to the interface you actually use. A listener on every interface is reachable from every network the host joins.
- Put the gateway behind the same access control as the host it runs on. If you would not expose SSH there, do not expose this.
- Turn it off when you are done with the remote work. An unused listener is an unmonitored one.

## FAQ

### Is the Hermes Webapp a hosted service?

No. The Webapp is served by your own gateway from the machine that runs it. Your sessions and files stay on that machine, and nothing is provisioned in a vendor cloud. The Desktop workspace in the tab is the same workspace native Desktop shows.

### Is the Webapp on by default?

No. It is off until you enable it with `webapp.enabled: true` or through Web Access in Desktop's settings. Enabling it is what starts serving a browser-reachable workspace, which is why the setting is explicit rather than automatic.

### Can two people use the Webapp at the same time?

Not as separate users. The Webapp is single-user: a signed-in tab acts as the person who signed in, with that person's sessions, Group Chats and settings. For separate identities, run separate profiles or separate gateways instead of sharing one tab.

### How should I expose the Webapp to the internet?

Preferably you do not. Use a tailnet, a VPN, or an SSH tunnel and keep the listener off the public internet. If you do serve it behind a public URL, put real sign-in in front of it, keep it on the bound loopback port, and turn it off when the remote work is finished.

### Does the Webapp work with Desktop plugins?

Yes. Installed Desktop plugins load in a Webapp tab, and desktop-only plugins can be installed from the tab, pinned to the commit the install dialog displayed. Group Chats and their room list are shared with native Desktop rather than duplicated.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is the Hermes Webapp a hosted service?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. The Webapp is served by your own gateway from the machine that runs it. Sessions and files stay on that machine and nothing is provisioned in a vendor cloud. The Desktop workspace in the tab is the same workspace native Desktop shows."
      }
    },
    {
      "@type": "Question",
      "name": "Is the Webapp on by default?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. It stays off until you enable it with webapp.enabled set to true, or through Web Access in Desktop settings. Enabling it is what starts serving a browser-reachable workspace, which is why the setting is explicit rather than automatic."
      }
    },
    {
      "@type": "Question",
      "name": "Can two people use the Webapp at the same time?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not as separate users. The Webapp is single-user: a signed-in tab acts as the person who signed in, with that person's sessions, Group Chats and settings. For separate identities, run separate profiles or separate gateways instead of sharing one tab."
      }
    },
    {
      "@type": "Question",
      "name": "How should I expose the Webapp to the internet?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Preferably you do not. Use a tailnet, a VPN or an SSH tunnel and keep the listener off the public internet. If you do serve it behind a public URL, put real sign-in in front of it, keep it on the bound loopback port, and turn it off when the remote work is finished."
      }
    }
  ]
}
</script>

*← [All guides](index.md) | [Rewind a conversation](conversation-rewind.md) | [Hermes Desktop](/hermes/guides)*

*↑ [Section Home](/hermes/guides)*
