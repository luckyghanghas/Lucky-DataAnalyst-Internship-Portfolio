# SQL Queries for Business Questions

## 01 Top Products By Revenue
```sql
SELECT product_name, ROUND(SUM(revenue), 2) AS revenue
FROM sales
GROUP BY product_name
ORDER BY revenue DESC
LIMIT 5;
```

## 02 Monthly Revenue Trend
```sql
SELECT month, ROUND(SUM(revenue), 2) AS revenue, COUNT(*) AS orders
FROM sales
GROUP BY month
ORDER BY month;
```

## 03 Channel Performance
```sql
SELECT sales_channel, COUNT(*) AS orders, ROUND(SUM(revenue), 2) AS revenue,
       ROUND(AVG(gross_margin) * 100, 1) AS avg_margin_pct
FROM sales
GROUP BY sales_channel
ORDER BY revenue DESC;
```

## 04 Region Return Rate
```sql
SELECT region, COUNT(*) AS orders, ROUND(AVG(returned_flag) * 100, 1) AS return_rate_pct
FROM sales
GROUP BY region
ORDER BY return_rate_pct DESC;
```

## 05 Campaign Roi Proxy
```sql
SELECT campaign, ROUND(SUM(revenue), 2) AS revenue, ROUND(SUM(gross_profit), 2) AS gross_profit,
       ROUND(SUM(gross_profit) / SUM(revenue) * 100, 1) AS gross_margin_pct
FROM sales
GROUP BY campaign
ORDER BY gross_profit DESC;
```

## 06 Age Group Value
```sql
SELECT age_group, COUNT(DISTINCT customer_id) AS customers,
       ROUND(SUM(revenue) / COUNT(DISTINCT customer_id), 2) AS revenue_per_customer
FROM sales
GROUP BY age_group
ORDER BY revenue_per_customer DESC;
```

