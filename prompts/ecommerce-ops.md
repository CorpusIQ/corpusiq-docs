# Ecommerce and marketplace prompts

For **Shopify**, **eBay**, **Amazon Seller**, and **GunBroker** operators.

---

### "How's my store doing?"

**What this does:** Full ecommerce review — cash, ad performance,
inventory, product profitability, refunds, abandoned carts, LTV, CAC.
**Connectors used:** Shopify, Google Ads, Meta Ads, TikTok, GA4,
QuickBooks.
**Behind the scenes:** `ecommerce-command-center` skill.
**Sample answer shape:** Multi-section store health brief covering
revenue, traffic, ads, inventory, refunds, and unit economics.

---

### "What are my best-selling SKUs this month?"

**What this does:** Top products by units and revenue.
**Connectors used:** Shopify.
**Behind the scenes:** `get_shopify_popular_products` +
`list_shopify_orders`.
**Sample answer shape:** Ranked product list with units, revenue, and
average order contribution.

---

### "Which Shopify SKUs are slow movers?"

**What this does:** Identifies inventory sitting with low sell-through.
**Connectors used:** Shopify.
**Behind the scenes:** `get_shopify_inventory` joined to recent order
velocity.
**Sample answer shape:** Slow-mover list with on-hand units and days
of cover at current velocity.

---

### "Are any orders looking risky?"

**What this does:** Pulls Shopify's risk flags.
**Connectors used:** Shopify.
**Behind the scenes:** `get_shopify_risky_orders`.
**Sample answer shape:** Order list with risk reason per order.

---

### "Who are my repeat customers?"

**What this does:** Repeat-buyer cohort with order count and lifetime
spend.
**Connectors used:** Shopify.
**Behind the scenes:** `get_shopify_repeat_customers`.
**Sample answer shape:** Customer list ranked by repeat orders and
total spent.

---

### "Show me a summary of orders for the last 30 days."

**What this does:** Order volume, revenue, average order value, status
breakdown.
**Connectors used:** Shopify.
**Behind the scenes:** `get_shopify_order_summary`.
**Sample answer shape:** Topline order stats for the window.

---

### "How's my eBay seller account doing?"

**What this does:** Full eBay seller pulse — standards profile,
GMV, listing traffic, customer service metrics, funds.
**Connectors used:** eBay.
**Behind the scenes:** `ebay-marketplace-pulse` skill.
**Sample answer shape:** Seller standards verdict, GMV trend,
traffic metrics, defect rates, and funds available.

---

### "What's my eBay defect rate?"

**What this does:** Pulls the customer service metrics specifically.
**Connectors used:** eBay.
**Behind the scenes:** `get_ebay_customer_service_metric`.
**Sample answer shape:** INAD and INR rates with target threshold
comparison.

---

### "How many GunBroker listings do I have, and how many are about to
end?"

**What this does:** Live inventory snapshot for GunBroker sellers.
**Connectors used:** GunBroker.
**Behind the scenes:** `get_gunbroker_inventory_summary`.
**Sample answer shape:** Active listing count, ending-soon count, and
key category breakdowns.

---

### "What did I sell on GunBroker in the last 30 days?"

**What this does:** Sold listings with revenue.
**Connectors used:** GunBroker.
**Behind the scenes:** `list_gunbroker_items_sold`.
**Sample answer shape:** Sold-item list with sale price and date,
plus revenue total.

---

### "How are Amazon orders trending?"

**What this does:** Amazon Seller orders for the recent window.
**Connectors used:** Amazon Seller.
**Behind the scenes:** `get_amazon_seller_orders`.
**Sample answer shape:** Recent order list and revenue total. Note:
Amazon's API exposes a smaller surface than Shopify or eBay — this is a
high-level view, not a deep dive.
