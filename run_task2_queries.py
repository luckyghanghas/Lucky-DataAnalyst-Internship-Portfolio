"""
Run all Task 2 SQL queries against the SQLite database (or load from CSV if needed).
"""
import sqlite3
import pandas as pd
import os

DB_PATH  = "task-2-eda-business-intelligence/sales_analysis.sqlite"
CSV_PATH = "data/cleaned/sales_transactions_cleaned.csv"

# ── Connect / load data ──────────────────────────────────────────────────────
conn = sqlite3.connect(DB_PATH)

# Check if sales table exists; if not, load from CSV
tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", conn)
if "sales" not in tables["name"].values:
    print("Table 'sales' not found — loading from CSV...")
    df = pd.read_csv(CSV_PATH)
    df.to_sql("sales", conn, if_exists="replace", index=False)
    print(f"Loaded {len(df):,} rows into 'sales' table.\n")
else:
    count = pd.read_sql("SELECT COUNT(*) AS n FROM sales", conn).iloc[0,0]
    print(f"Connected to DB — 'sales' table has {count:,} rows.\n")

# ── Helper ────────────────────────────────────────────────────────────────────
def run(title, sql):
    print("=" * 70)
    print(f"  {title}")
    print("=" * 70)
    df = pd.read_sql(sql, conn)
    print(df.to_string(index=False))
    print()

# ── Q1: Top Products by Revenue ───────────────────────────────────────────────
run("Q1. TOP PRODUCTS BY REVENUE", """
SELECT
    product_name,
    ROUND(SUM(revenue), 2)                     AS total_revenue,
    COUNT(*)                                    AS orders,
    ROUND(AVG(unit_price), 2)                   AS avg_price,
    ROUND(AVG(returned_flag) * 100, 2)          AS return_rate_pct
FROM sales
GROUP BY product_name
ORDER BY total_revenue DESC
LIMIT 8
""")

# ── Q2: Monthly Revenue Trend ─────────────────────────────────────────────────
run("Q2. MONTHLY REVENUE TREND", """
SELECT
    month,
    ROUND(SUM(revenue), 2)            AS total_revenue,
    COUNT(*)                           AS orders,
    ROUND(SUM(gross_profit), 2)       AS gross_profit,
    ROUND(AVG(gross_margin) * 100, 2) AS margin_pct
FROM sales
GROUP BY month
ORDER BY month
""")

# ── Q3: Sales Channel Performance ────────────────────────────────────────────
run("Q3. SALES CHANNEL PERFORMANCE", """
SELECT
    sales_channel,
    COUNT(*)                                    AS orders,
    ROUND(SUM(revenue), 2)                      AS total_revenue,
    ROUND(SUM(gross_profit), 2)                 AS gross_profit,
    ROUND(AVG(gross_margin) * 100, 1)           AS avg_margin_pct,
    ROUND(AVG(returned_flag) * 100, 1)          AS return_rate_pct
FROM sales
GROUP BY sales_channel
ORDER BY total_revenue DESC
""")

# ── Q4: Region Return Rate ────────────────────────────────────────────────────
run("Q4. REGION RETURN RATE", """
SELECT
    region,
    COUNT(*)                                    AS orders,
    ROUND(SUM(revenue), 2)                      AS total_revenue,
    ROUND(SUM(gross_profit), 2)                 AS gross_profit,
    ROUND(AVG(returned_flag) * 100, 1)          AS return_rate_pct
FROM sales
GROUP BY region
ORDER BY return_rate_pct DESC
""")

# ── Q5: Campaign ROI ──────────────────────────────────────────────────────────
run("Q5. CAMPAIGN ROI", """
SELECT
    campaign,
    COUNT(*)                                              AS orders,
    ROUND(SUM(revenue), 2)                                AS total_revenue,
    ROUND(SUM(gross_profit), 2)                           AS gross_profit,
    ROUND(SUM(gross_profit) / SUM(revenue) * 100, 1)     AS gross_margin_pct
FROM sales
GROUP BY campaign
ORDER BY gross_margin_pct DESC
""")

# ── Q6: Age Group Value ───────────────────────────────────────────────────────
run("Q6. CUSTOMER AGE GROUP VALUE", """
SELECT
    age_group,
    COUNT(DISTINCT customer_id)                              AS unique_customers,
    ROUND(SUM(revenue), 2)                                   AS total_revenue,
    ROUND(SUM(revenue) / COUNT(DISTINCT customer_id), 2)     AS revenue_per_customer,
    ROUND(AVG(returned_flag) * 100, 1)                       AS return_rate_pct
FROM sales
GROUP BY age_group
ORDER BY revenue_per_customer DESC
""")

conn.close()
print("=" * 70)
print("  ALL 6 QUERIES COMPLETED SUCCESSFULLY")
print("=" * 70)
