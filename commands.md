# Terminal Record: Seabreeze Inn

## 1. Building the project

```
mkdir seabreeze-inn
cd seabreeze-inn
python3 -m venv .venv
source .venv/bin/activate
pip install pytest ruff
touch business_rules.py main.py commands.md README.md
mkdir tests
touch tests/__init__.py tests/test_business_rules.py
echo ".venv/" > .gitignore
echo "__pycache__/" >> .gitignore
pip freeze > requirements.txt
git init
git add .
git commit -m "Set up project structure and gitignore"
gh repo create seabreeze-inn --public --source=. --remote=origin --push
```

## 2. The virtual environment

```
which python3
```

```
/home/theo/seabreeze-inn/.venv/bin/python3
```

The path is inside my `.venv` folder, so the virtual environment is on.

## 3. The project structure

```
tree -L 2
```

```
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files
```

`__pycache__` is on my computer but not in the repo, because `.gitignore` ignores it.

## 4. Every function and test

```
rg 'def '
```

```
business_rules.py
12:def calculate_room_cost(nightly_rate: float, nights: int) -> float:
17:def get_stay_discount(nights: int, corporate: bool = False) -> float:
27:def calculate_stay_total(
39:def requires_credit_check(total: float) -> bool:
44:def gets_welcome_package(nights: int, total: float) -> bool:
49:def total_reserved(stays: list) -> float:
59:def largest_stay(stays: list) -> str:
73:def format_stay_line(

tests/test_business_rules.py
13:def test_room_cost_is_rate_times_nights():
17:def test_no_discount_below_4_nights():
21:def test_six_percent_at_exactly_4_nights():
25:def test_six_percent_at_13_nights():
29:def test_eighteen_percent_at_exactly_14_nights():
33:def test_corporate_under_4_nights_gets_six_percent():
37:def test_14_nights_beats_corporate_floor():
41:def test_cleaning_fee_at_exactly_300():
45:def test_no_cleaning_fee_just_above_300():
49:def test_credit_check_at_exactly_2000():
53:def test_no_credit_check_just_below_2000():
57:def test_welcome_package_at_exactly_6_nights():
61:def test_no_welcome_package_at_5_nights():
65:def test_welcome_package_at_exactly_1000_total():
69:def test_no_welcome_package_just_below_1000_total():
73:def test_total_reserved_adds_every_stay():
81:def test_total_reserved_of_empty_list_is_zero():
85:def test_largest_stay_returns_biggest_guest():
93:def test_largest_stay_tie_goes_to_first():
101:def test_largest_stay_of_empty_list_is_empty_string():
105:def test_stay_line_shows_yes_and_no():
```

`business_rules.py` has 8 functions and `test_business_rules.py` has 21 tests.

## 5. Which files print

```
rg -l 'print'
```

```
main.py
```

Only `main.py` prints. `business_rules.py` is not listed because it has no `print()`; its functions just return values.

## 6. The commit history

```
git log --oneline
```

```
88c7fb2 (HEAD -> main, origin/main) Add main.py stay report
d5570cb Add largest stay and report line functions with tests
56216b4 Add total reserved loop with tests
2cf5226 Add stay total, credit check, and welcome package with tests
0cbbeee Add room cost and stay discount with tests
883eea7 Set up project structure and gitignore
```

There were 6 commits at that point.
