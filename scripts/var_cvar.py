import pandas as pd
import numpy as np

# Load scheme performance data
df = pd.read_csv("data/processed/07_scheme_performance_clean.csv")

results = []
for _, row in df.iterrows():
    std = row["std_dev_ann_pct"] / 100
    mean_return = row["return_1yr_pct"] / 100
    
    # Approximate VaR and CVaR from std dev
    var_95 = mean_return - 1.645 * std
    cvar_95 = mean_return - 2.063 * std
    
    results.append({
        "fund_name": row["scheme_name"],
        "VaR_95": round(var_95, 4),
        "CVaR_95": round(cvar_95, 4),
        "risk_grade": row["risk_grade"]
    })

report = pd.DataFrame(results)
report.to_csv("outputs/var_cvar_report.csv", index=False)
print("✅ Task 1 Done!")
print(report.head(10))