import pandas as pd

rebates = [
    {
        "program_name": "Canada Greener Homes Grant",
        "incentive_type": "Grant",
        "amount": "$5,000 max",
        "eligibility": "Homeowners, primary residence, pre/post retrofit EnerGuide audit required",
        "source_url": "https://natural-resources.canada.ca/energy-efficiency/homes/canada-greener-homes-initiative",
        "last_verified": "2026-09-22",
    },
    {
        "program_name": "Enbridge Home Efficiency Rebate Plus",
        "incentive_type": "Rebate",
        "amount": "Up to $7,100",
        "eligibility": "Enbridge gas customers in Ontario, home built before 2020",
        "source_url": "https://www.enbridgegas.com/home-efficiency-rebate-plus",
        "last_verified": "2026-09-22",
    },
    {
        "program_name": "IESO Save on Energy – Retrofit Program",
        "incentive_type": "Incentive",
        "amount": "Varies by meansure",
        "eligibility": "Ontario businesses, pre-approval required",
        "source_url": "https://saveonenergy.ca/For-Business-and-Industry/Programs-and-incentives/Retrofit-Program", # the only working/alive url
        "last_verified": "2026-09-22",
    },
]

df = pd.DataFrame(rebates)
df.to_csv("rebates.csv", index=False)

print(df)
print(f"\nWrote {len(df)} rebates to rebates.csv")