import pandas as pd

def recommend_funds(risk_appetite):
    df = pd.read_csv("data/processed/07_scheme_performance_clean.csv")
    df.columns = df.columns.str.strip().str.lower()
    
    filtered = df[df["risk_grade"] == risk_appetite]
    top3 = filtered.nlargest(3, "sharpe_ratio")[
        ["scheme_name", "sharpe_ratio", "risk_grade", "return_1yr_pct"]
    ]
    print(f"\n🏆 Top 3 {risk_appetite} Risk Funds:")
    print(top3.to_string(index=False))
    return top3

all_results = []
for appetite in ["Low", "Moderate", "High", "Very High"]:
    result = recommend_funds(appetite)
    all_results.append(result)

final = pd.concat(all_results)
final.to_csv("outputs/recommender_output.csv", index=False)
print("\n✅ Task 5 Done!")