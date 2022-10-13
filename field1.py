import json
import os


def create_field(*a):
    db = a[0]
    data = {}
    i = 1
    while i<=len(a)-1:
        data[a[i]] = []
        i = i + 1

    y = json.dumps(data,indent=4,sort_keys=True)
    if os.path.exists(db):
        opt = input('Database exists, Do you want to overwrite (y/n) or merge(m): ')
        opt = opt.lower()
        if opt == 'y':
            

            pass
        else:
            print('Operation cancelled')
            



    print(y)
    
    

def insert(*a):
    field = a[0]

    
        
        




create_field('user','score','school')
insert

