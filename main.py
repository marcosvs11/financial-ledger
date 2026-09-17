from interface import show_menu, show_title
from validation import read_int

while True:
    show_menu('Financial Ledger', ['Add income', 'Add expense', 'List transactions', 'View summary', 'Exit'])
    option = read_int('Chose an option: ')
    if option == 1:
        show_title('ADD INCOME')
    elif option == 2:
        show_title('ADD EXPENSE')
    elif option == 3:
        show_title('LIST TRANSACTIONS')
    elif option == 4:
        show_title('VIEW SUMMARY')
    elif option == 5:
        show_title('EXITING...')
        break
    else:
        print('Invalid entry. Enter a number from 1 to 5!')
