import csv
from decimal import Decimal

def initialize_file(file_name):
    try:
        with open(file_name, 'x', newline='', encoding='utf-8') as file:
            columns = ['type', 'description', 'amount']
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
    except FileExistsError:
        print('Arquivo encontrado com sucesso!')

    else:
        print(f'Arquivo {file_name} criado com sucesso!')


def add_transaction(transaction_type, description, amount, file_name):
    transaction = {
        'type': transaction_type,
        'description': description,
        'amount': amount,
    }

    columns = ['type', 'description', 'amount']

    with open(file_name, 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writerow(transaction)
    print(f'The {transaction_type} saved successfully!')

def list_transactions(file_name):
        with open(file_name, 'r', newline='', encoding='utf-8') as file:
            columns = ['type', 'description', 'amount']
            print(f'{columns[0]:<11}{columns[1]:<22}{columns[2]:<9}')
            print()
            reader = csv.DictReader(file)

            transaction_found = False

            for row in reader:

                description = row['description']
                amount = f'{Decimal(row['amount']):.2f}'

                if len(description) > 21:
                    description = description[:18] + '...'
                print(f'{row['type']:<11}{description:<22}R${amount:<9}')
                transaction_found = True

            if transaction_found == False:
                print('No transactions found.')

def view_summary(file_name):
    total_income = Decimal('0.00')
    total_expense = Decimal('0.00')

    with open(file_name, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            amount = Decimal(row['amount'])
            if row['type'] == 'income':
                total_income += amount
            elif row['type'] == 'expense':
                total_expense += amount
            else:
                print('Type invalid!')
                return

    print(f'Total amount income: R${total_income}')
    print(f'Total amount expense: R${total_expense}')
    balance = total_income - total_expense
    print(f'Balance: R${balance}')
