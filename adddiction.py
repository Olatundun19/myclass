import os
import json


def write(diction,word,meaning,wd):
    diction[word] = meaning
    diction = json.dumps(diction,indent=4,sort_keys=True)
    f = open('diction.json','w')
    f.write(diction)
    f.close()
    print('{} added successfully!!!'.format(wd))

print('The program add more words to the dictionary!!!')

wd = input('Enter the word: ')
meaning = input('Enter the meaning: ')

word = wd.lower()

if os.path.exists('diction.json'):
    f = open('diction.json','r')
    diction = f.read()
    f.close()
    diction = json.loads(diction)
    for x in diction:
        if x == word:
            opt = input('Word exist in the dictionary, do you want to overwrite(y/n): ')
            opt = opt.lower()
            if opt == 'y':
                write(diction,word,meaning,wd)
            else:
                print('Operation cancelled!!!')
                break

else:
    diction = {}
    write(diction,word,meaning,wd)

