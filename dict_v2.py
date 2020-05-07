import csv
from pathlib import Path


path = Path.cwd() / 'dict_ps.csv'

with open(path, newline='', encoding='utf-8') as csvfile_ps:
    reader_ps = csv.reader(csvfile_ps)
    mydict_ps = {rows[0]: rows[1] for rows in reader_ps}


# Search a Pali word in the Dictionary


def searching_p(search):
    print('This Pali word in Serbian means: ', mydict_ps[search])
    return

# Adding a new Pali word to the Dictionary


def adding_p(add_pali, add_serbian):
    mydict[add_pali] = add_serbian
    print('Done!')

    # Writing new status of the Dictionary
    with open(path, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        for i in mydict_ps.items():
            writer.writerow(i)

    print("Writing complete")

# Correcting a Pali word in the Dictionary


def correcting_p(error, correction):
    x = mydict_ps.get(error)
    if x:
        mydict[correction] = mydict_ps[error]
        del mydict_ps[error]
        print(f'{error} replaced with {correction}')
    else:
        print(f'{error} is not in the dictionary')

    # Writing new status of the Dictionary
    with open(path, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        for i in mydict_ps.items():
            writer.writerow(i)

    print("Writing complete")


# Serbian-Pali

path = Path.cwd() / 'dict_sp.csv'

with open(path, newline='', encoding='utf-8') as csvfile_sp:
    reader_sp = csv.reader(csvfile_sp)
    mydict_sp = {rows[0]: rows[1] for rows in reader_sp}

# Search a Serbian word in the Dictionary


def searching_s(search):
    print('This Pali word in Serbian means: ', mydict_sp[search])
    return

# Adding a new Serbian word to the Dictionary


def adding_s(add_pali, add_serbian):
    mydict_sp[add_pali] = add_serbian
    print('Done!')

    # Writing new status of the Dictionary
    with open(path, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        for i in mydict_sp.items():
            writer.writerow(i)

    print("Writing complete")

# Correcting a Serbian word in the Dictionary


def correcting_s(error, correction):
    x = mydict_sp.get(error)
    if x:
        mydict[correction] = mydict_sp[error]
        del mydict_sp[error]
        print(f'{error} replaced with {correction}')
    else:
        print(f'{error} is not in the dictionary')

    # Writing new status of the Dictionary
    with open(path, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        for i in mydict_sp.items():
            writer.writerow(i)

    print("Writing complete")


mans = True
ans = ''
while mans:
    print('''
    a. Pali-Serbian Dictionary
    b. Serbian-Pali Dictionary
    c. Quit
    ''')
    mans = input('What dictionary would you like to retrieve? ')
    if mans == '1':
        print("""
            1. Look up Pali word
            2. Add a Pali word
            3. Correct a Pali word
            4. Exit/Quit
            """)
        ans = input("What would you like to do? ")
        if ans == "1":
            searching_p(input('Search for Pali word: '))
        elif ans == "2":
            adding_p(input('To add a new Pali word, type it here: '),
                     input('Now type its meaning in Serbian: '))
        elif ans == "3":
            correcting_p(input('Type Pali word to be corrected: '),
                         input('Type correct version of the Pali word: '))
        elif ans == "4":
            print("\n Goodbye")
            break
        elif ans != "":
            print("\n Not Valid Choice! Try again")
    elif mans == '2':
        print("""
            1. Look up Serbian word
            2. Add a Serbian word
            3. Correct a Serbian word
            4. Exit/Quit
            """)
        ans = input("What would you like to do? ")
        if ans == "1":
            searching_s(input('Search for Serbian word: '))
        elif ans == "2":
            adding_s(input('To add a new Serbian word, type it here: '),
                     input('Now type its meaning in Pali: '))
        elif ans == "3":
            correcting_s(input('Type Serbian word to be corrected: '),
                         input('Type correct version of the Serbian word: '))
        elif ans == "4":
            print("\n Goodbye")
            break
        elif ans != "":
            print("\n Not Valid Choice! Try again")
    else:
        break

print('Good bye!')
