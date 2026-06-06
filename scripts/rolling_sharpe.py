import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/07_scheme_performance_clean.csv")

# Top 5 funds by sharpe ratio
top5 = df.nlargest(5, "sharpe_ratio")

plt.figure(figsize=(10, 6))
plt.barh(top5["scheme_name"], top5["sharpe_ratio"], color="steelblue")
plt.xlabel("Sharpe Ratio")
plt.title("Top 5 Funds by Sharpe Ratio")
plt.tight_layout()
plt.savefig("outputs/rolling_sharpe_chart.png")
print("✅ Task 2 Done!")