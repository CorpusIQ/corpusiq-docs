---
title: "ChatGPT Can't See CorpusIQ - CorpusIQ Docs"
description: "You installed the CorpusIQ app in ChatGPT or wired the MCP connector but ChatGPT cannot see your CorpusIQ data. Step-by-step fixes for the most common integration failures."
last_updated: "2026-11-07"
---
# ChatGPT can't see CorpusIQ

You installed CorpusIQ in ChatGPT (or wired the MCP connector) and pointed it
at your account. But ChatGPT isn't using the CorpusIQ tools. Either the
integration isn't listed, or it's listed but every query fails.

The happy path is in
[/docs/quick-start](/docs/quick-start).
This page covers what to do when it didn't work.

## Cause 1: The integration is installed but not available in this chat

Installing an app or a connector does not always enable it for every
conversation. In a chat, open the tools icon and confirm CorpusIQ is listed
for that conversation.

**Fix:** In the chat, click the tools icon and select CorpusIQ. Then ask a
question that needs your business data, like "what were my last 5 Shopify
orders."

## Cause 2: The workspace or plan blocks the integration

MCP support is available on ChatGPT Plus, Team, and Enterprise. The free tier
has limited MCP capabilities, and on a workspace an admin can disable an
integration for everyone.

**Fix:** Confirm you are signed in to the account or workspace where the
integration was installed. If a workspace admin manages apps, ask them to
enable CorpusIQ.

## Cause 3: You haven't completed the in-chat OAuth

Even when the integration is installed correctly, your first message that
triggers a CorpusIQ tool call will prompt you to authenticate with CorpusIQ.

**Symptom:** ChatGPT acts like CorpusIQ doesn't exist, or says it can't access
your data, even though the integration is installed.

**Fix:** Ask something that requires CorpusIQ, like "show me my last 5 Shopify
orders." If a "Sign in to CorpusIQ" button appears, click it and sign in with
the email tied to your CorpusIQ account.

## Cause 4: Wrong MCP endpoint URL (manual connector route only)

If you added CorpusIQ yourself under **Settings → Connectors → Add MCP
server**, the URL and personal token must match exactly what your CorpusIQ
account shows.

**How to check:** Compare the URL to the one in your CorpusIQ
**Settings → Integrations → ChatGPT MCP**. Character for character. Trailing
slashes matter. `http` vs `https` matters. A stale personal token fails the
same way.

## Cause 5: No data source is connected on the CorpusIQ side

Tools can be reachable while every source is still unauthenticated. CorpusIQ
returns real connector status, so this is visible rather than silent.

**How to check:** Ask "list my CorpusIQ connectors and their status." Most
will read "Not connected" until you authenticate each one. Connect the source
you care about, then ask again. See
[/docs/quickstart/03-connect-chatgpt](/docs/quickstart/03-connect-chatgpt) for
the setup path.

## Cause 6: A legacy Custom GPT that no longer runs

OpenAI retires custom GPTs on **December 11, 2026** (February 11, 2027 only for
FedRAMP and Enterprise workspaces with an approved deferral), and custom GPT
actions do not transfer. A GPT you built around CorpusIQ actions stops
working.

**Fix:** Use the CorpusIQ listing in the ChatGPT app store instead. It needs no
GPT of your own. See
[/docs/quickstart/03-connect-chatgpt](/docs/quickstart/03-connect-chatgpt).

## Still stuck

Send support:
- Screenshot of the connector or app configuration in ChatGPT (redact tokens).
- The exact message that failed and the response you got.
- Your CorpusIQ account email and the connected source you were querying.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
