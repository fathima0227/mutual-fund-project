import pandas as pd

df = pd.read_csv("data/processed/08_investor_transactions_clean.csv")
df.columns = df.columns.str.strip().str.lower()

# Extract year from transaction date
df["transaction_date"] = pd.to_datetime(df["transaction_date"])
df["year"] = df["transaction_date"].dt.year

# First transaction year per investor = cohort
cohort_year = df.groupby("investor_id")["year"].min().reset_index()
cohort_year.columns = ["investor_id", "cohort_year"]
df = df.merge(cohort_year, on="investor_id")

# Filter 2024/2025 cohorts
df = df[df["cohort_year"].isin([2024, 2025])]

# Group by cohort year and transaction type
cohort = df.groupby(["cohort_year", "transaction_type"]).agg(
    avg_amount=("amount_inr", "mean"),
    total_invested=("amount_inr", "sum"),
    investor_count=("investor_id", "nunique")
).reset_index()

cohort.to_csv("outputs/cohort_analysis.csv", index=False)
print("✅ Task 3 Done!")
print(cohort)