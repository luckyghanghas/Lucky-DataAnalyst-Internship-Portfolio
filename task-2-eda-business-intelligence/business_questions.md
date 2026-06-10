# Business Questions — SQL Queries

All queries run against the `sales` table loaded from `data/cleaned/sales_transactions_cleaned.csv`.

---

## Q1. Which products generated the most revenue?

```sql
SELECT
    product_name,
    ROUND(SUM(revenue), 2)                          AS total_revenue,
    COUNT(*)                                         AS orders,
    ROUND(AVG(unit_price), 2)                        AS avg_price,
    ROUND(AVG(returned_flag) * 100, 2)               AS return_rate_pct
FROM sales
GROUP BY product_name
ORDER BY total_revenue DESC
LIMIT 8;
```

**Insight:** Smart Watch leads with $1.37M revenue. Mechanical Keyboard has the lowest return rate at 1.28%.

---

## Q2. How is revenue trending month by month?

```sql
SELECT
    month,
    ROUND(SUM(revenue), 2)       AS total_revenue,
    COUNT(*)                      AS orders,
    ROUND(SUM(gross_profit), 2)  AS gross_profit,
    ROUND(AVG(gross_margin) * 100, 2) AS margin_pct
FROM sales
GROUP BY month
ORDER BY month;
```

**Insight:** Jan 2026 was the peak month at $441,892. Mar 2025 was the lowest at $253,183 — a 75% swing showing strong seasonality.

---

## Q3. Which sales channel is the strongest?

```sql
SELECT
    sales_channel,
    COUNT(*)                                         AS orders,
    ROUND(SUM(revenue), 2)                           AS total_revenue,
    ROUND(SUM(gross_profit), 2)                      AS gross_profit,
    ROUND(AVG(gross_margin) * 100, 1)                AS avg_margin_pct,
    ROUND(AVG(returned_flag) * 100, 1)               AS return_rate_pct
FROM sales
GROUP BY sales_channel
ORDER BY total_revenue DESC;
```

**Insight:** Website leads revenue at $2.46M (46.2% share). Mobile App has the best margin at 21.49%. Retail Store lags at 15.2% share.

---

## Q4. Which region has the highest return rate?

```sql
SELECT
    region,
    COUNT(*)                                         AS orders,
    ROUND(SUM(revenue), 2)                           AS total_revenue,
    ROUND(SUM(gross_profit), 2)                      AS gross_profit,
    ROUND(AVG(returned_flag) * 100, 1)               AS return_rate_pct
FROM sales
GROUP BY region
ORDER BY return_rate_pct DESC;
```

**Insight:** South region has the highest return rate at 7.19% — nearly double West's 3.83%. Needs investigation into delivery quality or product mix.

---

## Q5. Which marketing campaign delivers the best ROI?

```sql
SELECT
    campaign,
    COUNT(*)                                         AS orders,
    ROUND(SUM(revenue), 2)                           AS total_revenue,
    ROUND(SUM(gross_profit), 2)                      AS gross_profit,
    ROUND(SUM(gross_profit) / SUM(revenue) * 100, 1) AS gross_margin_pct
FROM sales
GROUP BY campaign
ORDER BY gross_margin_pct DESC;
```

**Insight:** Search Ads leads margin at 26.67%. Email Offer is the weakest at 13.89% — heavy discounting eroding profit.

---

## Q6. Which customer age group delivers the most value per customer?

```sql
SELECT
    age_group,
    COUNT(DISTINCT customer_id)                              AS unique_customers,
    ROUND(SUM(revenue), 2)                                   AS total_revenue,
    ROUND(SUM(revenue) / COUNT(DISTINCT customer_id), 2)     AS revenue_per_customer,
    ROUND(AVG(returned_flag) * 100, 1)                       AS return_rate_pct
FROM sales
GROUP BY age_group
ORDER BY revenue_per_customer DESC;
```

**Insight:** 55+ customers have the highest revenue per customer at $6,222.92. The 45-54 segment is the least valuable at $5,271.58 — a potential gap for targeted campaigns.
