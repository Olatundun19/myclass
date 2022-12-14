import os
import json


def write(diction,word,meaning,wd):
    diction[word] = meaning
    diction = json.dumps(diction,indent=4,sort_keys=True) #Convert from dictionary to JSON
    f = open('diction.json','w')
    f.write(diction)
    f.close()
    print('{} added successfully!!!'.format(wd))

print('The program add word to the dictionary!!!')

wd = input('Enter the word: ')
meaning = input('Enter the meaning: ')

word = wd.lower()

if os.path.exists('diction.json'):
    f = open('diction.json','r')
    diction = f.read()
    f.close()
    diction = json.loads(diction)#Conversion from JSON to dictionary
    chk = False
    for x in diction:
        if x == word:
            chk = True
            opt = input('Word exist in the dictionary, do you want to overwrite(y/n): ')
            opt = opt.lower()
            if opt == 'y':
                write(diction,word,meaning,wd)
                break
            else:
                print('Operation cancelled!!!')
                break

    if chk == False:
        write(diction,word,meaning,wd)


else:
    diction = {}
    write(diction,word,meaning,wd)

