def show_title(msg):
    width = len(msg) + 24
    print(width * '-')
    print(msg.center(width, ' '))
    print(width * '-')

def show_menu(msg, options):
    show_title(msg)
    i = 1
    for item in options:
        print(f'{i} - {item}')
        i += 1
    width = len(msg) + 24
    print(width * '-')
