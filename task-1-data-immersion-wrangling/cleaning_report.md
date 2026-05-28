# Task 1 - Data Immersion & Wrangling

## Objective
Prepare a sales transaction dataset for analysis by profiling the raw data, fixing quality issues, and creating a clean analysis-ready file.

## Dataset Overview
- Raw rows received: 1,260
- Final cleaned rows: 1,250
- Date range after cleaning: 2025-01-01 to 2026-03-26
- Business grain: one row per order

## Data Quality Issues Found
| Issue | What I found | Treatment |
|---|---:|---|
| Duplicate orders | 10 rows | Removed by keeping the first record for each `order_id`. |
| Mixed date formats | Multiple formats such as yyyy-mm-dd, dd/mm/yyyy, and mm-dd-yyyy | Parsed and standardized to ISO date format. |
| Inconsistent text casing | Region values appeared as lowercase in some rows | Trimmed whitespace and converted to title case. |
| Missing payment method | 4 rows | Replaced blanks with `Unknown` to preserve the transaction. |
| Missing customer age | 3 rows | Filled with median age to avoid losing useful sales records. |
| Revenue outliers | 2 visible pricing/revenue scale errors | Corrected unit price scale and recalculated revenue from base fields. |

## New Fields Created
- `gross_profit`: revenue minus cost.
- `gross_margin`: gross profit divided by revenue.
- `month`: reporting month for trends.
- `age_group`: customer segment based on age.
- `returned_flag`: numeric return indicator for dashboards and statistics.

## Final Output
The cleaned file is saved at `data/cleaned/sales_transactions_cleaned.csv`.
