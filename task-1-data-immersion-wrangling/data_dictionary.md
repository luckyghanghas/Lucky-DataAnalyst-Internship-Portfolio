# Data Dictionary

| Column | Type | Business relevance |
|---|---|---|
| order_id | Text | Unique order identifier used for transaction-level joins. |
| order_date | Date | Purchase date standardized to ISO format. |
| customer_id | Text | Customer key used to calculate repeat purchase and cohort behavior. |
| customer_age | Integer | Customer age after median imputation for missing values. |
| region | Text | Sales region: North, South, East, or West. |
| sales_channel | Text | Acquisition/sales channel: Website, Mobile App, or Retail Store. |
| product_name | Text | Product purchased. |
| category | Text | Product family used for product-level analysis. |
| quantity | Integer | Units purchased in the order. |
| unit_price | Decimal | Unit selling price before discount. |
| discount_rate | Decimal | Order discount percentage stored as a decimal. |
| revenue | Decimal | Net order revenue after discount. |
| cost | Decimal | Estimated fulfillment/product cost. |
| gross_profit | Decimal | Revenue less cost. |
| gross_margin | Decimal | Gross profit divided by revenue. |
| campaign | Text | Marketing campaign or source credited to the order. |
| payment_method | Text | Payment mode, with blanks replaced by Unknown. |
| delivery_days | Integer | Days taken to deliver the order. |
| customer_rating | Integer | Customer rating from 1 to 5. |
| returned | Text | Yes/No return indicator. |
| returned_flag | Integer | Return indicator converted to 1/0 for calculations. |
| month | Text | Year-month field used for time-series reporting. |
| age_group | Text | Customer age band for segmentation. |
