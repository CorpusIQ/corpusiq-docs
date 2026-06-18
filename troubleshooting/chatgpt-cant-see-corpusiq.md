# ChatGPT can't see CorpusIQ

You set up a custom GPT (or used the ChatGPT MCP connector flow) and
pointed it at CorpusIQ. But ChatGPT isn't using the CorpusIQ tools.
Either the connector isn't listed, or it's listed but every query
fails.

The happy path is in
[../quickstart/03-connect-chatgpt.md](../quickstart/03-connect-chatgpt.md).
This page covers what to do when it didn't work.

## Cause 1: The custom GPT was saved without the action

When you build a custom GPT in ChatGPT, you have to **add the CorpusIQ
action and save the GPT**. It's easy to fill out the config and
navigate away without hitting save.

**Fix:** Open the custom GPT in edit mode. Scroll to the Actions
section. Confirm the CorpusIQ action is listed. Hit save.

## Cause 2: Wrong MCP endpoint URL

The CorpusIQ MCP endpoint for ChatGPT has a specific URL. If the URL in
your custom GPT's action config doesn't match what the CorpusIQ team
gave you, ChatGPT can't reach the server.

**How to check:** Compare the URL in your action config to the exact
URL in
[../quickstart/03-connect-chatgpt.md](../quickstart/03-connect-chatgpt.md).
Character for character. Trailing slashes matter. `http` vs `https`
matters.

## Cause 3: OAuth redirect URL mismatch

When you set up the custom GPT's OAuth, you have to give CorpusIQ the
exact redirect URL ChatGPT uses. If that URL is registered wrong on
CorpusIQ's side, the OAuth handshake fails with "redirect URI mismatch."

**Symptom:** You click "Authenticate" inside the custom GPT, get
bounced to a CorpusIQ login page, sign in, and the redirect back to
ChatGPT errors out.

**Fix:** The redirect URL CorpusIQ accepts is typically
`https://chat.openai.com/aip/<your-gpt-id>/oauth/callback`. The
CorpusIQ team registers this on their side when you set up the
connector. If the URL ChatGPT generated doesn't match, send it to
support and they'll update the registration.

## Cause 4: You haven't completed the in-chat OAuth

Even after the GPT is configured correctly, your first message that
triggers a CorpusIQ tool call will prompt you to authenticate with
CorpusIQ. You have to click through that — sign in with the email tied
to your CorpusIQ account — for ChatGPT to get a token.

**Symptom:** The GPT acts like CorpusIQ doesn't exist, or says it can't
access your data, even though the action is configured.

**Fix:** Ask the GPT something that requires CorpusIQ, like "show me my
last 5 Shopify orders." If a "Sign in to CorpusIQ" button appears,
click it and complete the flow.

## Cause 5: The MCP endpoint isn't responding

Sometimes the server is up but a transient error or a specific JWT
issue blocks the response. ChatGPT will silently treat this as "no
tools available."

**How to check:** Open the CorpusIQ web app (or wherever you manage
your CorpusIQ account) and confirm your subscription is active and the
MCP endpoint is enabled. If everything looks right but ChatGPT still
can't see tools, email support with your account email and the custom
GPT name.

## Cause 6: Free-tier ChatGPT plan

Custom GPT actions require a paid ChatGPT plan (Plus, Team, or
Enterprise) for both the builder and the user. If you're on the free
plan, actions are not available.

**Fix:** Upgrade, or use Claude Desktop instead — see
[claude-cant-see-corpusiq.md](claude-cant-see-corpusiq.md) for the
parallel setup.

## Still stuck

Send support:
- The custom GPT name and a screenshot of its Actions configuration
  (redact tokens).
- The exact message that failed and the response you got.
- Your CorpusIQ account email.
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
