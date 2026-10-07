---
description: >-
  Set up CorpusIQ in Microsoft Teams, connect your own AI key, and choose
  private answers or intentional sharing in group chats and team channels.
canonical: "https://www.corpusiq.io/docs/chat-apps/getting-started-teams/"
robots: "index,follow"
last_updated: "2026-10-07"
title: "Getting started in Microsoft Teams"
tags: ["microsoft teams", "getting started", "documentation"]
---

# Getting started in Microsoft Teams

CorpusIQ answers questions using the business tools you connect. Ask privately
in a personal chat, or explicitly share an answer with a group or team channel.

## Before you start

You need:

- An [active CorpusIQ account](https://www.corpusiq.io/register) with an eligible
  trial or subscription. You will explicitly link this account to your Microsoft
  identity; the two email addresses do not need to match.
- Permission to access the business data sources you connect to CorpusIQ.
- Your own supported AI provider key: OpenAI, Anthropic, or Azure OpenAI.
  Provider usage charges are separate from your CorpusIQ subscription.
- Permission to install the app and consent to sign-in. Your Microsoft tenant
  may require an administrator to approve the app.

Send `help`, `hi`, or `hello` to see setup guidance before signing in. You do not
need a CorpusIQ account or AI key to read help. Never paste passwords, access
tokens, or provider keys into a Teams conversation.

## Step 1 - Sign in privately

1. Open the CorpusIQ app's personal chat in Microsoft Teams.
2. Send `corpusiq-login` and use the sign-in prompt.
3. Sign in with your Microsoft account. If Microsoft requests administrator
   approval, contact your tenant administrator.
4. On first use, follow the private CorpusIQ account-link prompt and sign in to
   the CorpusIQ account you want to use. Approve only a code you initiated in
   your own personal chat. This proves control of both accounts; matching email
   addresses alone never links them.
5. If you do not have a CorpusIQ account, use the
   [registration link](https://www.corpusiq.io/register), then return to the
   personal chat and send `corpusiq-login` again.

Channel conversations cannot perform the same bot SSO flow as personal chats.
If you start in a channel, use the bot's link to its personal chat, finish
sign-in there, and return to the channel. Do not share a sign-in link or
credential with another participant to give them access to your account.

If sign-in fails, see [troubleshooting](troubleshooting.md) or
[contact support](https://www.corpusiq.io/support).

## Step 2 - Configure your AI key and data sources

1. Sign in to [CorpusIQ](https://www.corpusiq.io/login).
2. Open your AI model settings and configure OpenAI, Anthropic, or Azure OpenAI.
   Enter the key in the dashboard, not in Teams.
3. Connect the business tools you want to ask about and grant only the access
   you intend to use.

CorpusIQ uses your provider configuration for your requests. It does not fall
back to a CorpusIQ-owned provider key when your configuration is missing. With
Azure OpenAI, use your own endpoint and model deployment; model requests are
sent to that configured endpoint.

## Step 3 - Choose a private or shared answer

### Private questions

Message CorpusIQ directly in its personal chat. For example:

> How many website sessions did we have over the last seven days?

The answer uses your connected sources. Missing permissions, disconnected
sources, or provider errors are reported rather than presented as an empty
successful answer.

### Group chats and team channels

Mention the bot and use `corpusiq-share` followed by the question you want
answered publicly in that conversation. For example:

> @CorpusIQ corpusiq-share How many website sessions did we have over the last seven days?

The reply is visible to everyone who can read that group or channel thread.
**Only share data you are authorized to disclose to those participants.** The
bot runs the request using your own CorpusIQ identity and AI configuration;
it does not give other participants access to your account or connectors.

An ordinary question without `corpusiq-share` receives guidance instead of
automatically publishing business data. For account setup and connector status,
use the personal chat. If a channel asks you to sign in privately, complete that
step and send the sharing request again when you return.

Shared answers let participants discuss the same result in the conversation.
They do not create a shared CorpusIQ account or persistent team-wide AI memory.

## Commands

| Command | What it does |
|---|---|
| `help` or `corpusiq-help` | Shows commands, setup, and sharing guidance without sign-in. |
| `corpusiq-login` | Links your own CorpusIQ account. Start from personal chat for channel use. |
| `corpusiq-logout` | Disconnects your CorpusIQ identity from this Teams app. |
| `corpusiq-status` | Shows connector status; use personal chat for account details. |
| `corpusiq-share <question>` | Intentionally shares an answer in the current group or channel conversation. |

For more question examples, see [asking questions](asking-questions.md).
For setup or account assistance, use [Help & Support](https://www.corpusiq.io/support)
or [contact us](https://www.corpusiq.io/contact).
