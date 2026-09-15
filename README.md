# OOP Bank Account & Pandas Analysis

A simple and structured Object-Oriented Banking System paired with data analysis in Python. This project tracks transactions using custom OOP logic, exports data automatically to a CSV file, and analyzes the dataset using Pandas.

## Features

- **Object-Oriented Architecture:** Encapsulates account logic inside a custom `BankAccount` class for handling deposits, withdrawals, and balance updates.
- **Transaction History Tracking:** Log every deposit and withdrawal dynamically with exact timestamps, transaction types, and remaining balances.
- **Automated CSV Export:** Converts stored transaction dictionaries into a structured `bank_transactions.csv` dataset automatically.
- **Pandas Data Summarization:** Reads the exported CSV file using Pandas to compute data heads, total transaction volume, operation counts, and detailed descriptive statistics.

---

## Core Concepts Covered

This project demonstrates foundational Python and Data Science concepts:

- **OOP (Classes & Methods):** Modular class definitions (`BankAccount`, `deposit`, `withdraw`, `_add_transaction`, `export_to_csv`).
- **Data Manipulation (Pandas):** Utilizing Pandas methods like `read_csv()`, `head()`, `sum()`, `value_counts()`, and `describe()`.
- **File Handling & Timestamps:** Automatic file generation and tracking execution times using Python's `datetime` module.

---

## Project Structure

| File | Description |
| :--- | :--- |
| `main.py` | Main script containing OOP logic, CSV exporter, and Pandas analysis |
| `bank_transactions.csv` | Auto-generated dataset storing complete transaction history |
| `README.md` | Comprehensive project documentation |

---

## Sample Output

```text
Successfully deposited $1500. Current Balance: $6500.0
Successfully withdrew $700. Current Balance: $5800.0
Successfully withdrew $300. Current Balance: $5500.0
Successfully deposited $2000. Current Balance: $7500.0
Transactions saved to bank_transactions.csv

==================================================
             PANDAS DATASET ANALYSIS
==================================================

1. Data Head:
  Account_Number Holder_Name        Type  Amount  Balance_After            Timestamp
0        ACC1001    Shrikant     Deposit    1500         6500.0  2026-09-15 19:10:23
1        ACC1001    Shrikant  Withdrawal     700         5800.0  2026-09-15 19:10:23
2        ACC1001    Shrikant  Withdrawal     300         5500.0  2026-09-15 19:10:23
3        ACC1001    Shrikant     Deposit    2000         7500.0  2026-09-15 19:10:23

2. Total Volume Processed:
$4500

3. Transactions Count by Type:
Type
Deposit       2
Withdrawal    2
Name: count, dtype: int64

4. Summary Statistics:
            Amount  Balance_After
count     4.000000       4.000000
mean   1125.000000    6325.000000
std     767.571929     888.350531
min     300.000000    5500.000000
25%     600.000000    5725.000000
50%    1100.000000    6150.000000
75%    1625.000000    6750.000000
max    2000.000000    7500.000000
==================================================
