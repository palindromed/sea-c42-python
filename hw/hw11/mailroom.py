donors = {
    'Bill Gates': [3000000, 13438902, 2532],
    'Elon Musk': [3, 6, 99],
    'Ronald Mcdonald': [200, 448, 500]
    }

def start():
    menu = ''' Choose from the following:\n
        T - Send a (T)hank You\n
        R - Create a (R)eport\n
        quit - Quit the program'''

    print('Welcome to Mailroom Madness')

    print(menu)

    answer = input()
    answer.lower()
    while answer not in 'trquit':
        print('That is not a valid input. Please try again.\n' + menu)

    if answer == 't':
        thanks()
    elif answer == 'r':
        report()
    elif answer == 'quit':
        quit()


def thanks():
    menu = '''Please enter a full name or choose from the following:\n
    list - Print a list of previous donors\n'
    quit - Quit the program\n'''
    print(menu)
    choice = input()
    if choice.lower() == 'list':
        print(donors.keys())
        choice = input()
    try:
        print(donors[choice])

    except ValueError:
        choice = input('That name is not an existing donor.')



def quit():
    print('you quitter')


def report():
    print('report')



start()

#if __name__ == '__main__':
