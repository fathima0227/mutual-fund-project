import pandas as pd

df = pd.read_csv("data/processed/08_investor_transactions_clean.csv")
df.columns = df.columns.str.strip().str.lower()

# Only SIP transactions
df = df[df["transaction_type"] == "SIP"]
df["transaction_date"] = pd.to_datetime(df["transaction_date"])
df = df.sort_values(["investor_id", "transaction_date"])

# Investors with 6+ SIP transactions
sip_counts = df.groupby("investor_id").filter(lambda x: len(x) >= 6)

# Gap between transactions
sip_counts = sip_counts.copy()
sip_counts["prev_date"] = sip_counts.groupby("investor_id")["transaction_date"].shift(1)
sip_counts["gap_days"] = (sip_counts["transaction_date"] - sip_counts["prev_date"]).dt.days

# Average gap per investor
avg_gap = sip_counts.groupby("investor_id")["gap_days"].mean().reset_index()
avg_gap.columns = ["investor_id", "avg_gap_days"]
avg_gap["at_risk"] = avg_gap["avg_gap_days"] > 35

avg_gap.to_csv("outputs/sip_continuity.csv", index=False)
print("✅ Task 4 Done!")
print(f"Total investors: {len(avg_gap)}")
print(f"At-risk investors: {avg_gap['at_risk'].sum()}")