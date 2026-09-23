import json
import pandas as pd

with open("rebates.json", "r", encoding="utf-8") as f:
    rebates = json.load(f)

df = pd.DataFrame(rebates)
df.to_csv("rebates.csv", index=False)

print(df)
print(f"\nWrote {len(df)} rebates to rebates.csv")