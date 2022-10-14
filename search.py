import os
import json

dictionfile = 'diction.json'


wd = input('Enter your word: ')
word = wd.lower()

chk = False

if os.path.exists(dictionfile):
    f = open(dictionfile,'r')
    x = f.read()
    f.close()
    diction = json.loads(x)
    for i in diction:
        if word == i:
            print(wd + ': ' + diction[i])
            chk = True
            break

if chk == False:
    print(wd + ', is not found in the dictionary!!!')

if not(os.path.exists(dictionfile)):
    print('Database Not Found, Pls contact the Admin!!!')

