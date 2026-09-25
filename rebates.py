import json
import pandas as pd

with open("rebates.json", "r", encoding="utf-8") as f:
    rebates = json.load(f)

df = pd.DataFrame(rebates)
df.to_csv("rebates.csv", index=False)

def search(df, keyword):
    """Return rows where keyword appears in the program name, eligibility, or amount."""
    keyword = keyword.lower()

    mask = (
        df["program_name"].str.lower().str.contains(keyword, na=False) 
        | df["provider"].str.lower().str.contains(keyword, na=False)
        | df["eligibility"].str.lower().str.contains(keyword, na=False)
        | df["amount"].str.lower().str.contains(keyword, na=False)
    )
    return df[mask]

def filter_by_type(df, incentive_type):
    """Return rows with an exact match on incentive_type."""
    return df[df["incentive_type"] == incentive_type]

print(df)
print(f"\nWrote {len(df)} rebates to rebates.csv")

print("\n--- Search: 'heat pump' ---")
print(search(df, "heat pump"))

print("\n--- Search: 'Enbridge' ---")
print(search(df, "Enbridge"))

print("\n--- Grants only ---")
print(filter_by_type(df, "Grant"))