# ISM3232 Midterm: Seabreeze Inn

- **Name:** Theodore Major
- **Version:** 1.0
- **Date:** October 24, 2026

## What This Program Does

This program calculates stay costs and generates reports for Seabreeze Inn. All pricing logic, fees, and checks are handled by eight functions in business_rules.py. The main.py file processes eight guest records through these functions and prints a summary. The final report shows individual balances, total revenue, average spend, the top spender, and counts for credit checks and welcome packages.

## Business Rules

1. Room cost is daily rate multiplied by the number of nights
2. Fewer than 4 nights is a 0% discount if you stay for 4 through 13 nights your discount is 6% and if you stay for 14 or more nights you get a discount of 18%
3. Corporate guests get a discount of 6% however they get the 18% if they stay for 14 or more nights just like regular guests
4. If the discounted cost is $300 or less a $40 cleaning fee is added
5. If the total is $2000 or more a credit check is required
6. If a stay is $1000 or more and it runs more than 5 nights it is required to receive a welcome package

## How to Run

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

## How to Test

```
ruff format .
ruff check .
pytest -v
```

I wrote 21 tests.

## Files in This Repository

- `business_rules.py`: the constants and the eight functions
- `main.py`: the sample stays and the report
- `tests/test_business_rules.py`: the pytest tests
- `tests/__init__.py`: empty file so the tests can import the functions
- `commands.md`: the terminal commands that built and checked the project, with their output
- `README.md`: this file
- `requirements.txt`: the packages to install
- `.gitignore`: keeps `.venv/` and `__pycache__/` out of the repo

## AI Use Statement

I did not use AI on this project.