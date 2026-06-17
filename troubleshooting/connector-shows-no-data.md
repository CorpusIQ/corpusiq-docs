# Connector is green but answers come back empty

The connector status panel shows the connector as connected. Green
check. But when you ask a question — "show me last week's Shopify
orders" — Claude or ChatGPT says there's no data, or the answer is
oddly thin.

This is almost always one of four things.

## Cause 1: You authenticated the wrong account

This is the number-one cause. You have two Shopify stores. You have a
personal Google account and a work Google account. You have an old
HubSpot portal you forgot about. The OAuth flow grabbed the wrong one.

**How to check:** Disconnect the connector. Reconnect. On the vendor
consent screen, look carefully at which account is being authorized —
account name, email address, store URL. Make sure it's the one with
your actual business data.

**Fix:** Open an incognito window with only the correct account signed
in, then reconnect.

## Cause 2: The date range in your question is too narrow

If you ask "show me yesterday's orders" and yesterday was a quiet day,
you'll genuinely get nothing back. Or if you ask "show me last week's
GA4 traffic" and the GA4 property only started collecting two days ago,
last week is empty.

**How to check:** Ask the same question with a wider date range — "last
30 days" or "last 90 days." If data shows up, the connection is fine;
the original window was just empty.

## Cause 3: The vendor account itself has no data yet

You connected your QuickBooks sandbox instead of your production
company. You connected a fresh Klaviyo account that hasn't sent
campaigns yet. You connected a brand-new GA4 property with no traffic.

The connector works. There's just nothing on the other end to read.

**How to check:** Log directly into the vendor and look. If the data
isn't there either, it's not a CorpusIQ problem.

**Fix:** If you have a different account that does have data,
disconnect and reconnect with that one.

## Cause 4: Missing scopes

CorpusIQ asks for read scopes for the data it expects to query. If a
vendor lets you uncheck individual scopes during OAuth and you
unchecked one, the connector authenticates but the specific data
endpoint returns nothing.

**How to check:** The connector is green but queries for one
*specific* kind of data come back empty, while other queries against
the same connector work. Example: Shopify customer data returns
results, but Shopify orders is empty.

**Fix:** Disconnect and reconnect. On the consent screen, leave every
checkbox checked. CorpusIQ only requests read scopes.

## Still empty

If you've checked all four and the answer is still empty, ask the same
question through the vendor's own UI to confirm the data exists. Then
send support the connector name, the question you asked, and what was
returned.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
