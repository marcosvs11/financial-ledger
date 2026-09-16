# Financial Ledger

English | [Português (Brasil)](README.pt-BR.md)

A personal finance tracker being developed in Python. The first version will run in the terminal and let users record income and expenses, view transactions, and check their balance.

## Status

Initial setup and planning. The features listed below are planned and have not been implemented yet.

## First release

- [ ] Record income with a description and an amount.
- [ ] Record expenses with a description and an amount.
- [ ] List recorded transactions.
- [ ] Calculate total income, total expenses, and the balance.
- [ ] Save transactions to a CSV file and load them when the application starts.
- [ ] Validate user input and handle expected file errors.

## Transaction data

Each transaction will contain:

- **Type:** income or expense.
- **Description:** what the transaction refers to.
- **Amount:** the monetary value of the transaction.

## Development steps

1. Build the terminal menu and record transactions in memory.
2. Implement transaction listing and balance calculations.
3. Add CSV persistence.
4. Check validation and error handling, and document how to run the application.

The first release will be complete when users can record and list transactions, calculate the balance, and recover their data after closing and reopening the application, with the basic validation working.

## Technology

- **Python 3:** planned application language.
- **Python standard library:** including the `csv` module for persistence.
- **Git and GitHub:** version control and project documentation.

The initial scope uses only the Python standard library; no third-party packages are required for the planned features.

## Getting started

Clone the repository:

```bash
git clone https://github.com/marcosvs11/financial-ledger.git
cd financial-ledger
```

The application does not have a runnable version yet. Execution instructions will be added when the first working version is available.

## Learning goals

Consolidate Python fundamentals through a complete project: functions, data structures, modules, input validation, exception handling, CSV files, and version control.
