donors = {
    'Yoo Hoo': [3000000, 13438902, 2532],
    'Elon Musk': [3, 6, 99],
    'Ronald Mcdonald': [200, 448, 500]
    }


def start():
    menu = ''' Choose from the following:\n
        T - Send a (T)hank You\n
        R - Create a (R)eport\n
        Quit - Quit the program\n
        F - Print letter to all donors to a (F)ile\n'''

    print('Welcome to Mailroom Madness')

    answer = input(menu)
    valid_input(answer)

    while answer:
        answer = input('Please enter a valid selection:\n' + menu)
        answer = valid_input(answer)


def valid_input(answer):
    bad_input = True

    try:
        answer = answer.lower()
        if answer == 'quit':
            exit()
        elif answer == 't':
            thanks()
        elif answer == 'r':
            report()
        elif answer == 'f':
            thanks_file(donors)
        else:
            return bad_input
    except TypeError:
                return bad_input


def thanks():
    menu = '''Please enter a name or choose from the following:\n
    list - Print a list of previous donors\n'
    quit - Quit the program, return to the main menu\n'''

    print(menu)

    choice = input()
    choice = choice.title()
    valid_thanks(choice)


def valid_thanks(choice):

    if choice == 'Quit':
        start()

    elif choice == 'List':
        print(', '.join(donors.keys()))
        thanks()
    try:
        if donors[choice]:
            new_donor(choice)
    except KeyError:
        new_donor(choice)


def new_donor(choice):
    if choice not in donors:
        donors[choice] = []
    donation = validate(choice)
    while not isinstance(donation, float) or donation < 0:
        donation = validate(choice)

    donors[choice].append(donation)
    send_thanks(choice, donation)


def validate(choice):
    donation = input("Enter donation amount for " + choice + ': ')
    try:
        return float(donation)
    except ValueError:
        print("That is not a number. Please enter a number. ")
        return None


def send_thanks(choice, donation):
    str(donation)
    input('''Dear {},

        Thank you so much for your kind donation of ${:.2f}.

        We here at the Foundation for Homeless Whales greatly appreciate it.

        Your money will go towards creating new oceans on the moon for whales
        to live in.

        Thanks again,

        Jim Grant

        Director, F.H.W.\n

        Press Enter to Continue...\n
        '''.format(choice, donation))
    start()


def report():
    print('{:^20} | {:^12}|{:^5}| {:^15}'.format("Donor Name", "Total",
            "#", "Average Amount"))
    print('{:_^50}'.format(''))
    for n in donors:
        total = 0
        num = len(donors[n])
        person = n
        for value in donors[n]:
            total += value
        avg = total/num
        print('{:^20} | ${:^11.2f}|{:^5} | ${:^15.2f}| '.format(person, total,
                        num, avg))
    input("Press enter to continue")
    start()


def thanks_file(donors):
    for k, v in donors.items():
        name = k
        outfile = k
        donation = v[-1]
        donation = str(donation)
        outfile = open(outfile, 'w')

        outfile.write(
            '''Dear {},

        Thank you so much for your kind donation of ${}.

        We here at the Foundation for Homeless Whales greatly appreciate it.

        Your money will go towards creating new oceans on the moon for whales
        to live in.

        Thanks again,

        Jim Grant

        Director, F.H.W.\n\n\n
            '''.format(name, donation))

        outfile.close()

if __name__ == '__main__':
    start()
