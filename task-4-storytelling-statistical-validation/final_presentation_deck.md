# Final Presentation Deck — Retail Sales Analytics

**Title:** Retail Sales Analytics: From Clean Data to Growth Decisions
**Audience:** Executive / Senior Management
**Purpose:** Present data-driven findings and statistical validation to guide the next investment decision

---

## Slide 1 — Title

**Retail Sales Analytics: From Clean Data to Growth Decisions**
ApexPlanet Software Pvt. Ltd. — Data Analytics Internship Capstone
Presenter: Lucky Ghanghas | Dataset: 1,250 retail transactions | Period: Jan 2025 – Mar 2026

---

## Slide 2 — The Business Question

> *"Where should the business invest next to grow revenue without damaging margin or customer experience?"*

Three sub-questions driving this analysis:
1. Which channels, products, and campaigns are driving profitable growth?
2. Are there segments or regions with fixable problems eroding margin?
3. Is the Mobile App customer experience statistically different from Website?

---

## Slide 3 — Dataset and Preparation

**Raw data:** 1,260 orders across 23 fields
**Cleaning steps performed:**
- Removed 10 duplicate order IDs
- Standardised 3 mixed date formats (ISO, DD/MM/YYYY, MM-DD-YYYY) to YYYY-MM-DD
- Imputed 3 missing customer ages with median (32 years)
- Replaced 4 blank payment methods with "Unknown"
- Corrected 2 revenue outliers (unit price scale errors — divided by 10)
- Recalculated revenue from base fields: unit_price × quantity × (1 – discount_rate)

**Final dataset:** 1,250 rows | 23 columns | 0 nulls in critical fields

---

## Slide 4 — Current Performance Snapshot

| KPI | Value | Benchmark Signal |
|---|---:|---|
| Total Revenue | $5,328,492 | Baseline |
| Total Orders | 1,250 | Avg 83/month |
| Average Order Value | $4,262.79 | High-ticket products |
| Gross Margin | 20.32% | Below 20% = risk zone |
| Return Rate | 5.20% | South region at 7.19% ⚠️ |
| Avg Customer Rating | 3.83 / 5 | Room for improvement |

---

## Slide 5 — Revenue Mix: Digital Dominates

**By Channel:**
- Website: $2,464,280 (46.2%) — volume leader
- Mobile App: $2,054,499 (38.6%) — profitability leader (21.49% margin)
- Retail Store: $809,714 (15.2%) — support channel only

**Key finding:** Mobile App beats Website on every profitability metric (AOV, margin, return rate). The $409K revenue gap is closeable with app-first retention investment.

---

## Slide 6 — Product & Campaign Story

**Best products:** Smart Watch leads revenue ($1.37M) but has a 7.24% return rate — the product description needs improvement to set accurate expectations.

**Best margin product category:** Office (24.13%) with the lowest return rate (4.17%) — currently undermarketed.

**Campaign ROI gap:**
- Search Ads: 26.67% margin ✅
- Email Offer: 13.89% margin ⚠️

Reallocating Email Offer budget to Search Ads could add ~$100K in gross profit annually.

---

## Slide 7 — Deep-Dive: The South Region Problem

South region: **7.19% return rate** vs portfolio average of 5.20%

This represents ~23 extra returns per year (above average rate). At an average order value of $4,069, this costs approximately **$93K in returned revenue** annually in the South region alone.

Possible causes:
- Longer delivery times creating expectation mismatches
- Product mix differences (more Wearables sold in South)
- Regional customer service quality gap

**Action:** Audit South region fulfilment SLAs and product-level return reasons.

---

## Slide 8 — Statistical Validation: Website vs Mobile App

**Hypothesis:** Is the Mobile App customer satisfaction rate statistically different from Website?

**Three tests performed on 1,048 ratings (592 Website + 456 Mobile App):**

| Test | Statistic | P-Value | Decision |
|---|---:|---:|---|
| Two-Proportion Z-Test | z = -0.5918 | p = 0.5540 | Fail to reject H₀ |
| Chi-Square Independence | χ² = 0.2746 | p = 0.6003 | Fail to reject H₀ |
| Welch's T-Test | t = -0.8650 | p = 0.3873 | Fail to reject H₀ |

**Conclusion:** At 5% significance level, there is **no statistically significant difference** in customer satisfaction between Website and Mobile App (all p > 0.05). Both channels deliver equivalent customer experience — strategy should focus on growing both, not choosing between them.

95% CI for satisfaction rate difference (App − Web): **−3.91% to +7.30%**

---

## Slide 9 — Recommendations

| Priority | Recommendation | Business Impact |
|---|---|---|
| 🔴 High | Fix South region return pipeline | Recover ~$93K/year in returned revenue |
| 🔴 High | Shift Email Offer budget → Search Ads | +~$100K gross profit/year |
| 🟡 Medium | Mobile App retention campaign | Close $409K revenue gap with Website |
| 🟡 Medium | Promote Office category products | Best margin (24.13%) + lowest returns |
| 🟢 Low | VIP programme for 55+ customers | Highest rev/customer at $6,222 |

---

## Slide 10 — Next Steps

1. **Automate monthly dashboard refresh** — connect cleaned CSV to live BI tool (Power BI / Tableau)
2. **Add Customer Lifetime Value (CLV)** metric — current data allows cohort-based CLV calculation
3. **Connect marketing spend data** — current ROI is gross margin proxy only; true ROAS requires spend figures
4. **Track NPS alongside ratings** — customer_rating (1–5) is a satisfaction proxy; NPS would give a more actionable loyalty signal
5. **A/B test product descriptions for Wearables** — to reduce 7.24% return rate with better expectation-setting content
