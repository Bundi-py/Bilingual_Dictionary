import csv
from pathlib import Path

path_ps = Path.cwd() / 'dict_ps.csv'
with open(path_ps, newline='', encoding='utf-8') as csvfile_ps:
    reader_ps = csv.reader(csvfile_ps)
    mydict_ps = {rows[0]: rows[1] for rows in reader_ps}

path_sp = Path.cwd() / 'dict_sp.csv'
with open(path_sp, newline='', encoding='utf-8') as csvfile_sp:
    reader_sp = csv.reader(csvfile_sp)
    mydict_sp = {rows[0]: rows[1] for rows in reader_sp}


def mainMenu():
    print('''Welcome to the CodingNomads Dictionary!:
            1. Pali-Serbian
            2. Serbian-Pali
            3. Quit''')

    choice = input('Enter choice: ')
    if choice == '1':
        subMenu_ps()
    elif choice == '2':
        subMenu_sp()
    elif choice == '3':
        exit
    else:
        print('\nInvalid choice. Enter 1-3')
        mainMenu()


def subMenu_ps():
    print()
    print()
    print('''Welcome to the Pali-Serbian Dictionary:
            1. Search word
            2. Add word
            3. Change word
            4. List words starting with letters entered
            5. Back''')

    choice = input('Enter choice: ')
    if choice == '1':
        search_p = input('Enter search word: ')
        searching_p(search_p)
        subMenu_ps()
    elif choice == '2':
        add_pali = input('Enter Pali word: ')
        add_serbian = input('Enter Serbian word: ')
        adding_p(add_pali, add_serbian)
        subMenu_ps()
    elif choice == '3':
        error = input('Enter a wrong word: ')
        correction = input('Enter a correct word: ')
        correcting_p(error, correction)
        subMenu_ps()
    elif choice == '4':
        letter_ps = input('Enter inital letters to list the words: ')
        listing_ps(letter_ps)
        subMenu_ps()
    elif choice == '5':
        mainMenu()
    else:
        print('\nInvalid choice. Enter 1-5')
        subMenu_ps()

# Search a Pali word in the Dictionary


def searching_p(search_p):
    if search_p in mydict_ps:
        print('This Pali word in Serbian means: ', mydict_ps[search_p])
    else:
        print('This word is not in a dictionary')
    return

# Adding a new Pali word to the Dictionary


def adding_p(add_pali, add_serbian):
    mydict_ps[add_pali] = add_serbian
    print('Done!')

    # Writing new status of the Dictionary
    with open(path_ps, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        for i in mydict_ps.items():
            writer.writerow(i)

    print("Writing complete")


# Correcting a Pali word in the Dictionary
def correcting_p(error, correction):
    x = mydict_ps.get(error)
    if x:
        mydict_ps[correction] = mydict_ps[error]
        del mydict_ps[error]
        print(f'{error} replaced with {correction}')
    else:
        print(f'{error} is not in the dictionary')

    # Writing new status of the Dictionary
    with open(path_ps, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        for i in mydict_ps.items():
            writer.writerow(i)
    print("Writing complete")


# Listing words starting with letters
def listing_ps(letter_ps):
    for k, v in mydict_ps.items():
        if k.startswith(letter_ps):
            print(k, ' = ', v)

# Serbian-Pali


def subMenu_sp():
    print('''Welcome to the Serbian-Pali Dictionary:
            1. Search word
            2. Add word
            3. Change word
            4. List words starting with letters entered
            5. Back''')

    choice = input('Enter choice: ')
    if choice == '1':
        search_s = input('Enter search word: ')
        searching_s(search_s)
        subMenu_sp()
    elif choice == '2':
        add_serbian = input('Enter Serbian word: ')
        add_pali = input('Enter Pali word: ')
        adding_p(add_serbian, add_pali)
        subMenu_sp()
    elif choice == '3':
        error = input('Enter wrong word: ')
        correction = input('Enter correct word: ')
        correcting_s(error, correction)
        subMenu_sp()
    elif choice == '4':
        letter_sp = input('Enter inital letters to list the words: ')
        listing_sp(letter_sp)
        subMenu_sp()
    elif choice == '5':
        mainMenu()
    else:
        print('\nInvalid choice. Enter 1-4')
        mainMenu()

# Search a Serbian word in the Dictionary


def searching_s(search_s):
    if search_s in mydict_sp:
        print('This Pali word in Serbian means: ', mydict_sp[search_s])
    else:
        print('This word is not in a dictionary')
    return

# Adding a new Serbian word to the Dictionary


def adding_s(add_serbian, add_pali):
    mydict_sp[add_serbian] = add_pali
    print('Done!')

    # Writing new status of the Dictionary
    with open(path_sp, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        for i in mydict_sp.items():
            writer.writerow(i)

    print("Writing complete")


# Correcting a Serbian word in the Dictionary
def correcting_s(error, correction):
    x = mydict_sp.get(error)
    if x:
        mydict_sp[correction] = mydict_sp[error]
        del mydict_sp[error]
        print(f'{error} replaced with {correction}')
    else:
        print(f'{error} is not in the dictionary')

    # Writing new status of the Dictionary
    with open(path_sp, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        for i in mydict_sp.items():
            writer.writerow(i)
    print("Writing complete")

# Listing words starting with letters


def listing_sp(letter_sp):
    for k, v in mydict_sp.items():
        if k.startswith(letter_sp):
            print(k, ' = ', v)


# main routine
mainMenu()
