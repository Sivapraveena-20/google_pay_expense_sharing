# Google Pay-Inspired Expense Sharing System

A Python + Pandas based expense-splitting tool for groups of friends, inspired
by Google Pay's "split expenses" feature. Tracks who paid for what, computes
each person's net balance, and works out the minimum set of payments needed
to settle up.

## Business Use Case

Friends on a trip (or sharing any group cost) want an easy way to log shared
expenses and find out who owes whom, without manually tracking a spreadsheet
of who paid for what.

## Project Structure

```
expense_sharing_project/
├── data_model.py       # Ledger setup + adding expenses (with validation)
├── balances.py         # Calculates each person's net balance
├── settlement.py       # Works out minimal "who pays whom" transactions
├── edge_cases.py       # Refunds and partial/direct payments
├── analytics.py        # Pandas groupby analytics (spend by person/category/date)
├── visualization.py    # Matplotlib charts
├── expense_sharing.py  # Combines all modules into one ExpenseSharing class
├── main.py             # Entry point - runs a full sample scenario
├── requirements.txt
└── README.md
```

Each module contains one focused piece of functionality (a "mixin" class).
`expense_sharing.py` combines them into a single `ExpenseSharing` class, so
usage stays simple:

```python
from expense_sharing import ExpenseSharing

es = ExpenseSharing(["Alice", "Bob", "Carol"])
es.add_expense("Alice", 900, ["Alice", "Bob", "Carol"], category="Accommodation")
es.calculate_settlement()
```

## Requirements

- Python 3.9+
- pandas
- numpy
- matplotlib

Install with:

```bash
pip install -r requirements.txt
```

## How to Run

```bash
cd expense_sharing_project
python3 main.py
```

This will:
1. Add a set of sample expenses (equal split, weighted split, a refund, and a partial payment)
2. Print the full expense ledger
3. Print each person's net balance
4. Print the final settlement (who pays whom)
5. Print a per-person summary table and category-wise spend
6. Save three charts as PNG files in the current directory:
   - `spend_by_person.png` – total amount paid by each person
   - `spend_by_category.png` – spending breakdown by category
   - `net_balances.png` – who owes vs. who is owed

## Methodology

### Data Model
Every expense is stored as a **row in a Pandas DataFrame** (the ledger)
rather than as a running balance total. Columns: `expense_id, payer, amount,
participants, split_type, weights, category, date`. Keeping the raw
transaction history (instead of just balances) is what enables the
analytics and reporting features.

### Expense Splitting
- **Equal split** (default): the amount is divided evenly among all participants.
- **Weighted split**: a `weights` dict (e.g. `{"Alice": 2, "Carol": 1}`)
  determines each participant's proportional share — for cases where
  contributions/usage aren't equal.

### Settlement Logic
Net balances are computed per person (positive = owed money, negative =
owes money), then a **greedy debtor/creditor matching** algorithm pairs the
largest creditor with the largest debtor repeatedly until everyone is
settled. This produces the minimum number of payment transactions.

### Edge Cases Handled
- **Refunds**: modeled as a negative-amount expense, split the same way the
  original charge was, so it cleanly reverses through the same balance formula.
- **Partial / direct payments**: modeled as a two-person expense (one payer,
  one participant) that transfers balance directly between two people,
  without affecting the rest of the group.
- **Validation**: payer/participants must belong to the group; weighted
  splits must supply a weight for every participant.

### Analytics
Using Pandas `groupby`:
- Total spend per payer
- Total spend per category
- Total spend per date
- Combined per-person summary (amount paid, net balance, status)

### Visualization
Three Matplotlib charts (bar, pie, bar) covering spend-by-person,
spend-by-category, and net balances.

## Sample Output

```
---- Net Balances ----
{'Alice': 340.0, 'Bob': -170.0, 'Carol': -170.0}

---- Final Settlement ----
Bob pays Alice: Rs.170.00
Carol pays Alice: Rs.170.00
```

## Known Limitations / Possible Improvements

- `participants` and `weights` are stored as Python lists/dicts inside
  DataFrame cells, which isn't fully "tidy" tabular data. A production
  version would normalize this into a separate `expense_splits` table
  (one row per person per expense).
- No persistence layer yet — the ledger exists only in memory for the
  session. Could be extended to save/load from CSV or a database.
- No currency conversion — assumes all amounts are in the same currency (Rs.).
- Could add a simple CLI or web front-end for entering expenses instead of
  editing `main.py` directly.

## Author

**[Sivapraveena Palanisamy]**
- Email: vishalisibi@.com
- LinkedIn: [Sivapraveena_Palanisamy](https://www.linkedin.com/in/sivapraveena-palanisamy-/)

  
