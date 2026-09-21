from interface import show_menu, show_title
from validation import read_description, read_amount, read_int
from file import add_transaction, initialize_file

file_name = 'financial_ledger.csv'
initialize_file(file_name)

while True:
    show_menu('Financial Ledger', ['Add income', 'Add expense', 'List transactions', 'View summary', 'Exit'])
    option = read_int('Chose an option: ')
    if option == 1:
        show_title('ADD INCOME')
        description = read_description('Enter the income description: ')
        amount = read_amount('Enter the amount received: R$')
        add_transaction('income', description, amount, file_name)

    elif option == 2:
        show_title('ADD EXPENSE')
        description = read_description('Enter the expense description: ')
        amount = read_amount('Enter the amount paid: R$')
        add_transaction('expense', description, amount, file_name)

    elif option == 3:
        show_title('LIST TRANSACTIONS')

    elif option == 4:
        show_title('VIEW SUMMARY')

    elif option == 5:
        show_title('EXITING...')
        break
    else:
        print('Invalid entry. Enter a number from 1 to 5!')
