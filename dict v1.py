import csv

with open('c:/FAJLOVI/Python_School/CodingNomads/dict/dict2.csv', newline = '', encoding = 'utf-8') as csvfile:
    reader = csv.reader(csvfile)
    mydict = {rows[0]:rows[1] for rows in reader}
    
#Adding a new Pali word to the Dictionary
add_pali = input('To add a new Pali word, type it here: ')
add_serbian = input('Now type its meaning in Serbian: ')
mydict[add_pali] = [add_serbian]
print('Done!')

#Search a Pali word in the Dictionary
search = input('Search for Pali word: ')
print('This Pali word in Serbian means the following: ', mydict[search])

#Correcting a Pali word in the Dictionary
error = input('Type Pali word to be corrected: ')
correction = input('Type correct version of the Pali word: ')
mydict[error] = [correction]
print('Corrected!', mydict[correction])

#Writing ne status of the Dictionary
with open('dict_new.csv', mode='w', encoding = 'utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(mydict)

print("Writing complete")
