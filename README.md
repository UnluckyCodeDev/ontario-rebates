# Ontario Electrification Rebates

A curated, searchable CSV of current Ontario electrification rebates — heat pumps, solar, batteries, EV chargers, and electrical panel upgrades — built for contractors who quote residential retrofit jobs.

## The problem

Rebate information in Ontario is hard to find. It is scattered across many different government, utility, and city websites. For a contractor trying to write a quick price quote for a customer, it takes a long time to look through old web pages, messy eligibility rules, and broken links. 

Because rebate programs open and close without warning, it is easy to make a mistake. There is no single place where a contractor can see all programs side by side or check when the data was last verified. This makes quoting jobs slow and risky for small businesses.

## What this tool does

* Puts 11 rebate programs (10 open, 1 closed) into one simple file.
* Organizes every program with the exact same data fields like name, provider, status, max amount, and rules.
* Automatically creates two clean CSV files: one master list of all programs and one list of open programs only.
* Provides search and filter functions for use in Python across program names, providers, rules, amounts, and categories.
* Adds a "last verified" date to every single row so you know the information is still fresh.

## How to search and filter

You can use the functions inside `rebates.py` to quickly query the data in your own scripts:

```python
from rebates import search, filter_by_type
import pandas as pd

df = pd.read_json("rebates.json")
print(search(df, "heat pump"))
```

## Example output

```csv
program_name,provider,incentive_type,status,category,amount_text,amount_max_cad,eligibility,source_url,last_verified
Ontario Home Renovation Savings Program (HRS),Enbridge Gas,Rebate,Open,Whole Home,"Varies by equipment (up to $7,500 for heat pumps)",7500.0,"Ontario residents, replacing qualifying HVAC or adding insulation; no EnerGuide pre-assessment required",https://www.enbridgegas.com/ontario/rebates-energy-conservation/home-efficiency-rebate,2026-10-01
Home Energy Loan Program (HELP),City of Toronto,Loan,Open,Whole Home,up to $125,000,125000.0,"Toronto low-rise property owners with clean tax histories and lender consent can get low-interest HELP loans, which can be combined with other energy rebates.",https://www.toronto.ca/services-payments/water-environment/environmental-grants-incentives/home-energy-loan-program-help/,2026-10-01
Heat Pumps,Home Renovation Savings,Rebate,Open,Heat Pump,Up to $12,000,12000.0,"To qualify for a heat pump rebate, homeowners—including landlords—must occupy an existing detached, semi-detached, row, or mobile home and be an Enbridge Gas residential customer or connected to the Ontario electricity grid.",https://www.homerenovationsavings.ca/without-assessment/heat-pumps,2026-10-01
```

## Data sources

* IESO Save on Energy (Retrofit & First Nations programs)
* Enbridge Gas (Home Renovation Savings & Affordable Housing programs)
* Natural Resources Canada (Canada Greener Homes Grant history)
* Home Renovation Savings (Direct heat pump & solar rebates)
* City of Toronto (HELP & Eco-Roof programs)
* Transport Canada (Electric Vehicle Affordability Program)

## How to run it

1. Clone the repo:
   ```bash
   git clone https://github.com/UnluckyCodeDev/ontario-rebates.git
   cd ontario-rebates
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS / Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the script:
   ```bash
   python rebates.py
   ```

The script reads `rebates.json` and automatically creates `rebates.csv` and `rebates_open.csv`.

## Project structure

```text
ontario-rebates/
├── rebates.py            # The Python script to search, filter, and make CSVs
├── rebates.json          # The main data file with all the rebate info
├── rebates.csv           # Generated file: all programs
├── rebates_open.csv      # Generated file: open programs only
├── requirements.txt      # Lists pandas as a dependency
└── README.md
```

## Limitations

* The data is researched and typed by hand, not automatically scraped. Programs can change their rules without warning.
* The maximum amount listed is the top limit of the program. It does not guarantee every applicant will get that exact amount.
* Some programs in the list are for businesses or large apartment buildings, not regular houses.
* The tool only covers programs in Ontario.

## Roadmap

* Add more programs to the list to get to 25+ entries.
* Add specific rebates for EV chargers (right now it only includes the vehicles).
* Set up a schedule to check and update the links and amounts every month.
* Make a simple website so people can search without using Python code.
* Publish the data as a public JSON feed to share this data with other contractor tools.

## About

I am a Grade 12 student in Toronto learning Python. This is the first project in my portfolio, and it connects to a business idea I am working on to help local contractors make quotes faster. Please let me know if you have any feedback.

## License

This project is licensed under the MIT License — see the LICENSE file for details.