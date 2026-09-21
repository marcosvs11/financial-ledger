import csv

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
        'amount': f'{amount:2f}',
    }

    columns = ['type', 'description', 'amount']

    with open(file_name, 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writerow(transaction)
    print(f'The {transaction_type} saved successfully!')
