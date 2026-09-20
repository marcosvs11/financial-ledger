from decimal import Decimal, InvalidContext, InvalidOperation
from unicodedata import decimal

def read_int(msg):
    while True:
        try:
            number = int(input(msg))
            return number
        except ValueError:
            print('Invalid input. Please enter an integer!')

def read_amount(msg):
    while True:
        try:
            text = str(input(msg)).strip()
            text = text.replace(',', '.')
            if '.' in text:
                parts = text.split('.')
                part_decimal = parts[1]
                if len(part_decimal) > 2:
                    raise InvalidOperation
            if not text.replace('.', '').isdecimal():
                raise InvalidOperation
            number = Decimal(text)
            if not number.is_finite() or number <= 0:
                raise InvalidOperation
            return number
        except InvalidOperation:
            print('Invalid input. Please enter a valid amount!')

def read_description(msg):
    while True:
        description = str(input(msg)).strip()
        if description == '':
            print('Invalid input, the description is empty!')
            continue
        else:
            return description
