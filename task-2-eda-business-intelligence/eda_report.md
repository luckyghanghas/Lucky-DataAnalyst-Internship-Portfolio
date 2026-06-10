# Task 2 — Exploratory Data Analysis & Business Intelligence

## Executive Summary
Analysis of 1,250 cleaned retail orders totalling **$5,328,492.40 revenue** across three sales channels, four regions, eight products, and six marketing campaigns. The business is digital-first — Website and Mobile App together account for **84.8% of all revenue**. Gross margin is stable at **20.32%** but Email Offer campaigns drag margin to 13.89%, well below average. The South region carries a **7.19% return rate**, nearly double the West's 3.83%, signalling a fulfilment or product-fit problem requiring immediate review.

---

## Summary Statistics

| Metric | Value |
|---|---:|
| Total Orders | 1,250 |
| Total Revenue | $5,328,492.40 |
| Average Order Value | $4,262.79 |
| Gross Margin | 20.32% |
| Return Rate | 5.20% |
| Average Customer Rating | 3.83 / 5 |
| Date Range | Jan 2025 – Mar 2026 (15 months) |

---

## Business Questions & Findings

### Q1. Top Products by Revenue
| Product | Revenue | Orders | Return Rate |
|---|---:|---:|---:|
| Smart Watch | $1,368,210 | 152 | 7.24% |
| Mechanical Keyboard | $899,190 | 156 | 1.28% |
| Webcam Pro | $798,138 | 169 | 4.73% |
| Bluetooth Headphones | $655,422 | 151 | 5.30% |
| Portable Speaker | $600,264 | 157 | 7.64% |
| USB-C Hub | $506,904 | 161 | 6.83% |
| Laptop Stand | $296,637 | 143 | 4.90% |
| Wireless Mouse | $203,728 | 161 | 3.73% |

**Finding:** Smart Watch is the top revenue driver at $1.37M (25.7% of total), but also carries a 7.24% return rate — the second highest. Mechanical Keyboard is the most reliable product with only 1.28% returns.

### Q2. Monthly Revenue Trend
Revenue ranged from **$253,183 (Mar 2025)** to **$441,892 (Jan 2026)** — a 75% swing indicating strong seasonality. Q1 months (Jan, Feb) consistently outperform mid-year months. The trend shows recovery in late 2025 after a mid-year dip.

### Q3. Sales Channel Performance
| Channel | Revenue | Orders | Margin |
|---|---:|---:|---:|
| Website | $2,464,280 | 592 | 19.84% |
| Mobile App | $2,054,499 | 456 | 21.49% |
| Retail Store | $809,714 | 202 | 18.81% |

**Finding:** Website leads volume but Mobile App leads profitability with a 21.49% margin. Retail Store contributes only 15.2% of revenue — a support channel, not a growth engine.

### Q4. Region Return Rate
| Region | Orders | Return Rate |
|---|---:|---:|
| South | 320 | 7.19% ⚠️ |
| North | 299 | 5.69% |
| East | 292 | 4.11% |
| West | 339 | 3.83% ✅ |

**Finding:** South has a 7.19% return rate — 88% higher than West. This needs investigation into delivery times, product mix, or customer expectation mismatches in that region.

### Q5. Campaign ROI Analysis
| Campaign | Revenue | Gross Profit | Margin |
|---|---:|---:|---:|
| Search Ads | $1,034,918 | $276,020 | 26.67% ✅ |
| Organic | $946,146 | $198,462 | 20.98% |
| Referral | $904,176 | $185,195 | 20.48% |
| Influencer | $809,556 | $158,624 | 19.59% |
| Festive Sale | $789,240 | $147,123 | 18.64% |
| Email Offer | $844,456 | $117,325 | 13.89% ⚠️ |

**Finding:** Search Ads delivers the highest margin at 26.67% and the highest absolute gross profit at $276,020. Email Offer generates $844K revenue but only 13.89% margin — heavy discounting is destroying profit. Budget should shift from Email Offer to Search Ads and Organic.

### Q6. Customer Age Segment Value
| Age Group | Customers | Revenue | Rev/Customer |
|---|---:|---:|---:|
| 55+ | 184 | $1,145,018 | $6,222.92 ✅ |
| 35–44 | 201 | $1,206,868 | $6,004.32 |
| 18–24 | 154 | $884,965 | $5,746.53 |
| 25–34 | 183 | $1,032,053 | $5,639.63 |
| 45–54 | 201 | $1,059,588 | $5,271.58 |

**Finding:** 55+ customers spend the most per person at $6,222.92 — a segment often overlooked in marketing but highly valuable here.

---

## Key Strategic Insights

1. **Double down on digital** — Website + Mobile App = 84.8% of revenue. Digital-first investment is justified.
2. **Fix the South region return problem** — 7.19% return rate is costing margin. Investigate delivery SLAs and product descriptions.
3. **Reallocate Email Offer budget** — 13.89% margin vs 26.67% for Search Ads. Reducing email discounts would directly improve profitability.
4. **Target 55+ and 35–44 segments** — highest revenue per customer. Loyalty and premium product campaigns would yield strong returns.
5. **Smart Watch needs return rate attention** — Top revenue product but 7.24% return rate suggests expectation gap on product features.

---

## Dashboard
Interactive charts are available in `eda_charts.html` (static SVG charts) and `sales_dashboard.html` (full interactive 3-tab dashboard). The sales dashboard mockup is available in `sales_dashboard_mockup.xlsx`.
