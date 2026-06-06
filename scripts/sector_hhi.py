import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/09_portfolio_holdings_clean.csv")
df.columns = df.columns.str.strip().str.lower()

# Compute HHI per fund
def compute_hhi(group):
    weights = group["weight_pct"] / group["weight_pct"].sum()
    return np.sum(weights ** 2)

hhi = df.groupby("amfi_code").apply(compute_hhi).reset_index()
hhi.columns = ["amfi_code", "HHI"]
hhi["concentrated"] = hhi["HHI"] > 0.25

hhi.to_csv("outputs/sector_hhi.csv", index=False)

# Chart
plt.figure(figsize=(12, 5))
colors = ["red" if c else "green" for c in hhi["concentrated"]]
plt.bar(hhi["amfi_code"].astype(str), hhi["HHI"], color=colors)
plt.axhline(0.25, color="orange", linestyle="--", label="Threshold")
plt.title("Sector HHI by Fund")
plt.ylabel("HHI Score")
plt.xlabel("Fund Code")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/sector_hhi_chart.png")
print("✅ Task 6 Done!")
print(hhi.head(10))