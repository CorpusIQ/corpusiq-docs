# Connector authentication failed

You clicked "Connect Shopify" (or any other connector). The browser
bounced you to the vendor, you signed in, you approved — and CorpusIQ
came back with an error, or the connector status still shows as not
connected.

This page walks the four common causes and the fix for each.

## Cause 1: You signed in with the wrong account

The most common one. You have two Google accounts open in the same
browser, or two Shopify stores under different emails. The OAuth flow
authorized the wrong one.

**Symptom:** The connection looks like it worked but the data you
expected isn't there. Or the connection itself failed because the
account doesn't have permissions for the resource you're trying to read
(e.g. no Shopify admin access).

**Fix:**
1. Open a new private/incognito browser window.
2. Make sure you're signed into **only** the right account.
3. Reconnect from CorpusIQ. The OAuth screen should clearly show which
   account is about to be authorized — verify it before approving.

## Cause 2: You denied or skipped a permission scope

Some vendors show several permission toggles on the consent screen and
let you uncheck them. If you uncheck a scope CorpusIQ needs (e.g.
"read orders" for Shopify), the connection completes but every query
fails.

**Symptom:** Connection green. Queries return "permission denied" or
empty results.

**Fix:**
1. Disconnect the connector from CorpusIQ.
2. Reconnect. On the vendor consent screen, **leave every requested
   scope checked**. CorpusIQ only asks for read scopes — there are no
   write scopes to worry about.

## Cause 3: The vendor blocked the OAuth request

A few vendors (especially Microsoft 365 in some tenants, Google
Workspace with admin-managed accounts) will block third-party apps
unless an admin pre-approves them. Some Shopify Plus stores also
enforce this.

**Symptom:** The vendor's screen says "Your administrator must approve
this app" or similar. You never reach the consent screen.

**Fix:** Ask your IT admin (or Google Workspace / Microsoft 365 admin)
to approve CorpusIQ in the vendor's admin console. Send them the app
name "CorpusIQ" and the connector you're trying to add. After
approval, try again from CorpusIQ.

## Cause 4: The token expired or was revoked

If you connected weeks ago and queries used to work, the token has
likely expired or been revoked from the vendor side (somebody clicked
"remove" in Google's connected apps page, or the password was changed).

**Symptom:** Connection shows red or "needs reauth." Queries fail with
"token invalid."

**Fix:**
1. Disconnect from CorpusIQ.
2. Reconnect. CorpusIQ will run a fresh OAuth flow and get a new token.

## Still failing

If none of the above worked, collect:
- The exact connector name.
- The exact error text you saw (screenshot is fine).
- The vendor account email you used.

Email support. There's a per-connector page in
[../connectors/](../connectors/) with vendor-specific quirks worth
checking too.
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
