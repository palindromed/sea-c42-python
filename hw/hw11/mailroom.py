donors = {
    'Bill Gates': [3000000, 13438902, 2532],
    'Elon Musk': [3, 6, 99],
    'Ronald Mcdonald': [200, 448, 500]
    }


def start():
    menu = ''' Choose from the following:\n
        T - Send a (T)hank You\n
        R - Create a (R)eport\n
        quit - Quit the program\n'''

    print('Welcome to Mailroom Madness')

    answer = input(menu)
    answer = answer.lower()

    while answer not in 'trquit':
        print('That is not a valid input. Please try again.\n' + menu)

    while answer == 'quit':
        break
    if answer == 't':
        thanks()
    elif answer == 'r':
        report()


def thanks():
    menu = '''Please enter a full name or choose from the following:\n
    list - Print a list of previous donors\n'
    quit - Quit the program\n'''

    print(menu)
    choice = input()
    choice = choice.lower()

    while choice == 'quit':
        break

    while choice == 'list':
        print(list_donors())
        choice = input(menu)
    try:
        donors[choice]
    except KeyError:
        new_donor(choice)


def new_donor(choice):
    donors[choice] = []
    donation = input("Enter donation amount for " + choice + ': ')
    while not isinstance(donation, float) or donation < 0:
        donation = validate()

    donors[choice].append(donation)

def validate():
    try:
        return float(input("Try again. Please enter a number: "))
    except ValueError:
        print("That is not a number. Please enter a number. ")
        return None



def list_donors():
    return donors.keys()


def report():
    print('report')

start()
#if __name__ == '__main__':
