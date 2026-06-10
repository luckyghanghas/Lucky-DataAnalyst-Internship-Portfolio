# Task 3 — Deep-Dive Analysis & Interactive Dashboarding

## Objective
Go beyond summary statistics and perform structured segment, channel, and category analysis to identify where the business should focus its next investment.

---

## Core KPIs Defined

| KPI | Formula | Why It Matters |
|---|---|---|
| Revenue | SUM(revenue) | Top-line business scale and growth direction |
| Average Order Value (AOV) | Revenue / Orders | Measures basket strength and upsell opportunity |
| Gross Margin | Gross Profit / Revenue | Shows whether growth is profitable |
| Return Rate | Returned Orders / Total Orders | Highlights product-fit and satisfaction risk |
| Customer Rating | AVG(customer_rating) | Captures post-purchase experience quality |
| Revenue per Customer | Revenue / Unique Customers | Measures customer lifetime value proxy |

---

## Deep-Dive Focus Areas

### 1. Channel Performance Deep-Dive

| Channel | Revenue | Orders | AOV | Gross Margin | Return Rate | Avg Rating |
|---|---:|---:|---:|---:|---:|---:|
| Website | $2,464,280 | 592 | $4,161 | 19.84% | 4.90% | 3.80 |
| Mobile App | $2,054,499 | 456 | $4,506 | 21.49% | 4.82% | 3.86 |
| Retail Store | $809,714 | 202 | $4,009 | 18.81% | 6.44% | 3.82 |

**Analysis:**
- Website leads volume (592 orders, 46.2% revenue share) but Mobile App leads on every profitability metric — higher AOV ($4,506 vs $4,161), higher margin (21.49% vs 19.84%), and lower return rate (4.82% vs 4.90%).
- The gap between Website and Mobile App revenue ($409K) is closeable with focused app retention investment.
- Retail Store has the highest return rate at 6.44% — 34% above the digital average. Physical browsing likely creates expectation mismatches not present in detailed online listings.

**Recommendation:** Invest in Mobile App retention campaigns (push notifications, loyalty points). Reduce Retail Store's role to showroom/support rather than revenue primary.

---

### 2. Product Category Deep-Dive

| Category | Revenue | Orders | AOV | Gross Margin | Return Rate |
|---|---:|---:|---:|---:|---:|
| Accessories | $1,609,822 | 478 | $3,368 | 21.48% | 4.81% |
| Wearables | $1,368,210 | 152 | $9,001 | 15.24% | 7.24% |
| Audio | $1,255,686 | 308 | $4,076 | 21.06% | 5.84% |
| Office | $1,094,775 | 312 | $3,509 | 24.13% | 4.17% |

**Analysis:**
- Accessories is the volume leader with 478 orders and a healthy 21.48% margin and low 4.81% return rate — the most balanced category.
- Wearables (Smart Watch) has the highest AOV at $9,001 but also the highest return rate at 7.24% and the lowest margin at 15.24%. High price + high returns = margin risk. Product descriptions and expectation-setting need improvement.
- Office products are the hidden gem: highest margin at 24.13% and lowest return rate at 4.17% — a stable, profitable category worth promoting more.
- Audio carries a 5.84% return rate above the 5.20% average, suggesting post-purchase dissatisfaction on sound quality expectations.

**Recommendation:** Promote Office category in campaigns (best margin, lowest returns). Add detailed spec comparison tools for Wearables to reduce return rate.

---

### 3. Regional Deep-Dive

| Region | Revenue | Orders | Gross Profit | Return Rate | Gross Margin |
|---|---:|---:|---:|---:|---:|
| West | $1,451,299 | 339 | $273,233 | 3.83% ✅ | 18.83% |
| South | $1,301,485 | 320 | $250,427 | 7.19% ⚠️ | 19.24% |
| North | $1,288,065 | 299 | $315,504 | 5.69% | 24.49% |
| East | $1,287,644 | 292 | $243,585 | 4.11% | 18.92% |

**Analysis:**
- West leads revenue ($1.45M) with the lowest return rate at 3.83% — best performing region overall.
- South has a 7.19% return rate — 88% higher than West. This is a significant outlier requiring investigation. Possible causes: longer delivery times in South, different product mix, or demographic mismatch.
- North has the highest gross margin at 24.49% despite lower revenue — driven by higher-margin product mix (more Office and Accessories, fewer Wearables).
- Revenue is remarkably balanced across South, North, and East (within $14K of each other) suggesting no dominant regional market — growth can come from any region with the right campaign.

**Recommendation:** Investigate South region delivery SLAs and product return reasons. Replicate North's high-margin product mix strategy in other regions.

---

### 4. Customer Segment Deep-Dive

| Age Group | Revenue | Customers | Rev/Customer | Orders | Return Rate |
|---|---:|---:|---:|---:|---:|
| 35–44 | $1,206,868 | 201 | $6,004 | 268 | 4.98% |
| 55+ | $1,145,018 | 184 | $6,223 | 259 | 5.10% |
| 45–54 | $1,059,588 | 201 | $5,272 | 267 | 4.98% |
| 25–34 | $1,032,053 | 183 | $5,640 | 246 | 5.46% |
| 18–24 | $884,965 | 154 | $5,747 | 210 | 5.19% |

**Analysis:**
- 55+ customers have the highest revenue per customer at $6,223 despite the smallest customer base (184) — underserved but highly valuable.
- 35–44 is the largest revenue segment at $1.21M with a healthy return rate of 4.98%.
- 25–34 has the highest return rate at 5.46% — this age group may be more price-sensitive and likely to return if expectations aren't met precisely.
- The 18–24 segment has the smallest customer base (154) but a per-customer value of $5,747 — strong potential for acquisition campaigns targeting younger buyers.

**Recommendation:** Create VIP loyalty programme for 55+ and 35–44 segments. For 25–34, focus on accurate product descriptions and easy returns to build long-term trust.

---

## Monthly Trend Analysis

Revenue peaked at **$441,892 in Jan 2026** (+35% above the 15-month average of $355,233) suggesting strong post-holiday or Q1 budget-release buying. The lowest month was **Mar 2025 at $253,183** (29% below average). There is a clear Q1 spike pattern visible in both 2025 and 2026.

Gross profit margin also spiked in Jan 2026 at **30.44%** — 10 percentage points above the baseline — indicating premium products (likely Wearables/Accessories) dominated that month's sales mix.

---

## Dashboard Contents

The interactive dashboard (`interactive_dashboard.html`) includes:
- **KPI cards**: Revenue, Orders, AOV, Gross Margin, Return Rate
- **Channel performance table** with margin and return rate
- **Regional performance table** with gross profit
- **Product category breakdown** with margin comparison
- **Monthly revenue trend** — last 8 months bar chart
- **Top products table** by revenue

---

## Summary Recommendations

| Priority | Action | Expected Impact |
|---|---|---|
| High | Fix South region returns (7.19%) | Margin recovery + customer trust |
| High | Shift budget from Email Offer to Search Ads | +7.78pp margin improvement |
| Medium | Mobile App retention campaign | Revenue gap closure with Website |
| Medium | Promote Office category (24.13% margin) | Profitable mix improvement |
| Low | VIP programme for 55+ segment | Lifetime value increase |
