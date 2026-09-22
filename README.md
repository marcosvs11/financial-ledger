# Financial Ledger

English | [Português (Brasil)](README.pt-BR.md)

A terminal application for tracking personal income and expenses. Record transactions, review individual entries, and calculate total income, total expenses, and the balance. Data is stored locally in a CSV file and remains available after the application closes.

## Status

The first working version is implemented. It uses Python's standard library and includes input validation, CSV persistence, and manual checks documented in [TESTING.md](TESTING.md).

This is a learning project. Current limitations and possible improvements are listed below.

## Features

- [x] Record income with a description and an amount.
- [x] Record expenses with a description and an amount.
- [x] List recorded transactions.
- [x] Calculate total income, total expenses, and the balance.
- [x] Save transactions to CSV and read them when listing entries or viewing the summary.
- [x] Validate menu choices, descriptions, and amounts.
- [x] Display transaction amounts with two decimal places.
- [x] Abbreviate long descriptions in the list while preserving the complete text in the CSV.

## Requirements

Python 3.12 or later.

Git, if cloning the repository using the commands below.

No third-party Python packages are required. The application uses csv for file storage and Decimal for monetary values and calculations.

## Getting started

Check your Python version:

python3 --version

Clone the repository and run the application from its directory:

git clone https://github.com/marcosvs11/financial-ledger.git
cd financial-ledger
python3 main.py

On the first run, the application creates financial_ledger.csv with its header if the file does not exist. Subsequent runs preserve the existing transactions.

## Usage

1 — Add income
Enter a description and the amount received.

2 — Add expense
Enter a description and the amount paid.

3 — List transactions
Display each transaction's type, description, and amount.

4 — View summary
Display total income, total expenses, and the balance.

5 — Exit
Close the application.

Income and expense amounts are entered as positive numbers. The balance is calculated as income minus expenses and can be negative.

Descriptions longer than 21 characters are displayed as the first 18 characters followed by .... The complete description remains in the CSV.

## Input rules

- Menu choices must be integers from 1 to 5.

- Descriptions must contain text; empty input and spaces alone are rejected. Leading and trailing spaces are removed.

- Amounts must be positive, finite numbers with at most two decimal places.

- A dot or comma can be used as the decimal separator: 5, 12.3, 12.30, and 12,30 are valid examples.

- Enter amounts without R$ or thousands separators. For example, use 1500,50 or 1500.50.

- Invalid input prompts the user to try again.

Amounts in the transaction list are shown with R$, a decimal point, and two decimal places, such as R$5.00 and R$12.30.

## CSV storage

The file uses UTF-8 encoding and these columns:

Column: type, description, amount.

Content: income or expense, Complete transaction description, Numeric text without a currency symbol, using a dot when a decimal separator is needed.

Example:

type,description,amount
income,Freelance,250
expense,"Café, pão e leite",12.30

Each transaction is saved when registered. Stored amounts do not need trailing zeros; the transaction list applies the two-decimal format when displaying them.

The CSV path is relative to the terminal's current directory. Run the program from the project directory to keep using the same file. Running it from another directory can create or use a different CSV.

The local financial_ledger.csv is excluded from version control through .gitignore.

## Project files

 Files            Responsibility

main.py -> Application flow and menu actions.

interface.py -> Titles and menu display.

validation.py -> Reading and validating user input.

file.py -> CSV initialization, transaction storage, listing, and summary calculations.

TESTING.md -> Manual test procedures and observed results.

## Testing

[TESTING.md](TESTING.md) currently documents two manual tests: long-description alignment and amount formatting with two decimal places. Each record includes the procedure, expected result, observed result, and status.

Use fictional data when repeating the tests. The repository does not yet include an automated test suite.

## Known limitations

- The application expects an existing CSV to have the correct header and valid transaction data. It does not repair empty or malformed existing files; invalid data can interrupt execution.

- Permission errors and other file read/write failures do not yet have user-friendly handling.

- Transactions cannot be edited or deleted through the menu.

Possible improvements include handling expected file errors and adding automated tests. These improvements are not implemented in the current version.

## Learning goals

Consolidate Python fundamentals through a complete project: functions, dictionaries, modules, input validation, exception handling, CSV persistence, decimal calculations, manual testing, and version control with branches and pull requests.
