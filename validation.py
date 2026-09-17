def read_int(msg):
    while True:
        try:
            number = int(input(msg))
            return number
        except ValueError:
            print('Invalid input. Please enter an integer!')
