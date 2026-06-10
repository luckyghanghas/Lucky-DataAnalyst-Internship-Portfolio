# Task 4 — Data Storytelling & Statistical Validation

## Business Context
The business is growing through digital channels, with Website and Mobile App responsible for 84.8% of total revenue ($5.33M). The core strategic question is whether to treat these channels differently from an investment and experience-management perspective. To answer this objectively, statistical hypothesis testing was used to compare customer satisfaction rates across the two digital channels.

---

## Business Story Arc

1. **Data is clean and trustworthy** — 1,250 orders after removing duplicates, fixing dates, and correcting outliers.
2. **Digital channels dominate** — Website (46.2%) + Mobile App (38.6%) = 84.8% of revenue.
3. **Profitable growth is not guaranteed** — Email Offer campaigns run at only 13.89% margin vs 26.67% for Search Ads. South region returns at 7.19% cost margin.
4. **Statistical validation confirms channel parity** — No significant difference in customer satisfaction between Website and Mobile App.
5. **Invest in both digital channels, fix the operational gaps** — return rates and campaign efficiency are the real levers.

---

## Statistical Hypothesis

**H₀ (Null):** The proportion of high-satisfaction orders (rating ≥ 4) is the same for Website and Mobile App customers.

**H₁ (Alternative):** Mobile App orders have a different high-satisfaction rate than Website orders.

**Significance level:** α = 0.05 (two-tailed)

---

## Tests Performed

Three independent tests were run in Python using `scipy.stats` to provide triangulated evidence (`scripts/hypothesis_testing.py`):

1. **Two-Proportion Z-Test** — Compares satisfaction rates between channels
2. **Chi-Square Test of Independence** — Tests whether satisfaction class (High/Low) is associated with channel
3. **Welch's T-Test** — Compares mean raw ratings allowing for unequal variances

---

## Results

### Test 1: Two-Proportion Z-Test

| Measure | Website | Mobile App |
|---|---:|---:|
| Total Orders | 592 | 456 |
| High-Satisfaction (Rating ≥ 4) | 408 (68.92%) | 322 (70.61%) |
| Difference (App − Web) | — | +1.69pp |

| Statistic | Value |
|---|---:|
| Z-statistic | −0.5918 |
| P-value | 0.5540 |
| 95% CI for difference | −3.91% to +7.30% |

**Decision:** Fail to reject H₀ (p = 0.5540 > 0.05)

---

### Test 2: Chi-Square Test of Independence

| | High Satisfaction | Low Satisfaction |
|---|---:|---:|
| Website | 408 | 184 |
| Mobile App | 322 | 134 |

| Statistic | Value |
|---|---:|
| Chi-square statistic | 0.2746 |
| P-value | 0.6003 |
| Degrees of Freedom | 1 |

**Decision:** Fail to reject H₀ (p = 0.6003 > 0.05). Satisfaction class is independent of sales channel.

---

### Test 3: Welch's T-Test (Mean Ratings)

| Measure | Website | Mobile App |
|---|---:|---:|
| Average Rating | 3.8024 | 3.8596 |
| Difference | — | +0.0572 |

| Statistic | Value |
|---|---:|
| T-statistic | −0.8650 |
| P-value | 0.3873 |

**Decision:** Fail to reject H₀ (p = 0.3873 > 0.05)

---

## Overall Conclusion

All three tests consistently fail to reject H₀ at the 5% significance level. The observed differences in satisfaction rates and average ratings between Website and Mobile App are **not statistically significant** and can be attributed to random sampling variation.

The 95% confidence interval (−3.91% to +7.30%) spans zero, confirming that the true population difference could plausibly be zero or either direction.

**Business interpretation:** Both digital channels deliver statistically equivalent customer experiences. Investment decisions should be driven by margin efficiency and growth potential — not customer satisfaction differences, which are negligible.

---

## Calls to Action

| Priority | Action | Rationale |
|---|---|---|
| 🔴 High | Fix South region return rate (7.19%) | 88% above West's rate — operational/product issue |
| 🔴 High | Reallocate Email Offer budget to Search Ads | 26.67% vs 13.89% margin — 12.78pp gap |
| 🟡 Medium | App-first retention campaign | Mobile App leads on all profitability metrics |
| 🟡 Medium | Improve Wearables product descriptions | 7.24% return rate is the highest of any category |
| 🟢 Low | Build CLV model for 55+ segment | $6,222/customer — highest value, underserved |

---

## Technical Notes

- All tests performed in Python using `scipy.stats` — see `scripts/hypothesis_testing.py`
- Dataset: 1,048 ratings used (592 Website + 456 Mobile App; Retail Store excluded as not part of hypothesis)
- High-satisfaction threshold: rating ≥ 4 (out of 5)
- All tests are two-tailed at α = 0.05
