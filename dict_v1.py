import csv
from pathlib import Path

path = Path.cwd() / 'dict_new.csv'

with open(path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    mydict = {rows[0]: rows[1] for rows in reader}

# Search a Pali word in the Dictionary


def searching(search):
    print('This Pali word in Serbian means: ', mydict[search])
    return

# Adding a new Pali word to the Dictionary


def adding(add_pali, add_serbian):
    mydict[add_pali] = add_serbian
    print('Done!')

# Correcting a Pali word in the Dictionary


def correcting(error, correction):
    x = mydict.get(error)
    if x:
        mydict[correction] = mydict[error]
        del mydict[error]
        print(f'{error} replaced with {correction}')
    else:
        print(f'{error} is not in the dictionary')


ans = True
while ans:
    print("""
    1. Look Up Pali word
    2. Add a Pali word
    3. Correct a Pali word
    4. Exit/Quit
    """)
    ans = input("What would you like to do? ")
    if ans == "1":
        searching(input('Search for Pali word: '))
    elif ans == "2":
        adding(input('To add a new Pali word, type it here: '),
               input('Now type its meaning in Serbian: '))
    elif ans == "3":
        correcting(input('Type Pali word to be corrected: '),
                   input('Type correct version of the Pali word: '))
    elif ans == "4":
        print("\n Goodbye")
        break
    elif ans != "":
        print("\n Not Valid Choice Try again")


# Writing new status of the Dictionary
with open(path, mode='w', encoding='utf-8', newline='') as outfile:
    writer = csv.writer(outfile)
    for i in mydict.items():
        writer.writerow(i)

print("Writing complete")
