# Finance Tracker (CLI)

A menu-driven command-line expense tracker built in pure Python. Add expenses, view them, see totals, filter by category — and your data survives between runs via JSON persistence.

Built as **v1 of an evolving project**: later versions add error handling, functions refactor, OOP structure, packaging, and tests.

---

## Features

| Option | Feature | What it does |
|---|---|---|
| 1 | Add Expense | Records name, amount, and category; saves to disk immediately |
| 2 | View Expenses | Numbered list of all expenses |
| 3 | Total Spend | Sum of all recorded amounts |
| 4 | Filter by Category | Shows matching expenses (case-insensitive) with subtotal |
| 5 | Exit | Quits the app; data is already saved |

## Tech

- **Python 3.14** — no external dependencies; standard library only (`json`)
- **uv** — project and environment management
- **ruff** — formatting and linting
- **git** — version control

## Data Model

Each expense is a dictionary; the collection is a list of dictionaries:

```json
[
  {"name": "Coffee", "amount": 150.0, "category": "food"},
  {"name": "Bus pass", "amount": 500.0, "category": "travel"}
]
```

This list-of-dicts shape is the same record-collection pattern that underpins real-world applications (contacts, catalogs, playlists).

## Persistence Logic

- **On startup:** load `expenses.json` if it exists; otherwise start with an empty list (`try/except FileNotFoundError`).
- **On every add:** rewrite the full list to disk (`json.dump`, write mode).
- **Invariant:** the file always matches memory, so exit needs no save step and data can never be stale.

```
start ──► file exists? ──► load : start empty
loop  ──► add expense ──► append ──► save()
exit  ──► nothing to do (disk already current)
```

## Getting Started

```bash
# create and enter the project (uv manages Python + environment)
uv init finance-tracker --python 3.14
cd finance-tracker

# run
uv run main.py
```

On first run there is no data file; add an expense and `expenses.json` is created automatically.

### Development commands

```bash
uv run ruff format .   # auto-format
uv run ruff check .    # lint
```

## Project Structure

```
finance-tracker/
├── main.py            # the application
├── expenses.json      # data file (auto-created, git-ignored)
├── pyproject.toml     # project config and dependencies
├── uv.lock            # locked dependency versions
└── .python-version    # pinned Python version
```

## Topics Covered

Variables · input/type conversion · f-strings · `while True` menu loop · `break` · if/elif/else · truthiness · `for` loops · `enumerate()` · lists · dictionaries · list of dicts · list comprehensions · generator expressions in `sum()` · `.lower()` normalization · `json` (load/dump) · `with open()` context manager · `try/except FileNotFoundError` · uv · ruff · git

## Known Limitations (intentional — scheduled fixes)

| Limitation | Planned fix |
|---|---|
| Non-numeric amount input crashes the app | Error handling & validation (next milestone) |
| Single flat file, no edit/delete of expenses | Functions refactor, then expanded operations |
| All logic in one file | Functions → OOP → package structure in later versions |

## Roadmap

- [x] v1 — core menu app: add, view, total, filter
- [x] v1.1 — JSON persistence
- [ ] v2 — input validation & error handling
- [ ] v3 — refactor into typed functions
- [ ] v4 — OOP model (`Expense`, `Tracker` classes)
- [ ] v5 — package structure, tests (pytest), CI

---

*Part of the Python Core curriculum — learning.nexolv.ai*