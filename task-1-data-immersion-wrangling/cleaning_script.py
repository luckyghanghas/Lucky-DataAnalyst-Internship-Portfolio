from datetime import datetime

import pandas as pd

raw_path = "../data/raw/sales_transactions_raw.csv"
cleaned_path = "../data/cleaned/sales_transactions_cleaned.csv"

df = pd.read_csv(raw_path)
df = df.drop_duplicates(subset=["order_id"], keep="first")

def parse_order_date(value):
    text = str(value).strip()
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y"):
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            continue
    return pd.NaT

df["order_date"] = df["order_date"].apply(parse_order_date)
df = df.dropna(subset=["order_date"])

df["region"] = df["region"].astype(str).str.strip().str.title()
df["sales_channel"] = df["sales_channel"].astype(str).str.strip().str.title()
df["payment_method"] = df["payment_method"].fillna("Unknown").replace("", "Unknown")
df["customer_age"] = pd.to_numeric(df["customer_age"], errors="coerce")
df["customer_age"] = df["customer_age"].fillna(df["customer_age"].median()).astype(int)

numeric_cols = ["quantity", "unit_price", "discount_rate", "revenue", "cost", "delivery_days", "customer_rating"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

expected_revenue = df["unit_price"] * df["quantity"] * (1 - df["discount_rate"])
ratio = df["revenue"] / expected_revenue
outliers = (ratio > 1.8) | (ratio < 0.5)
df.loc[outliers, "unit_price"] = df.loc[outliers, "unit_price"] / 10

df["revenue"] = (df["unit_price"] * df["quantity"] * (1 - df["discount_rate"])).round(2)
df["gross_profit"] = (df["revenue"] - df["cost"]).round(2)
df["gross_margin"] = (df["gross_profit"] / df["revenue"]).round(4)
df["month"] = pd.to_datetime(df["order_date"]).dt.to_period("M").astype(str)
df["age_group"] = pd.cut(
    df["customer_age"],
    bins=[17, 24, 34, 44, 54, 70],
    labels=["18-24", "25-34", "35-44", "45-54", "55+"],
).astype(str)
df["returned_flag"] = df["returned"].map({"Yes": 1, "No": 0})

df.to_csv(cleaned_path, index=False)
print(f"Cleaned rows: {len(df):,}")
