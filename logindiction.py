from pverify import verify
from upjson import confirm, write,fetch
from filechk import check,delete
from dictchk import dcheck


fn = 'userdiction.json'

print('1. Login Admin\t2. Create Admin\n3. Delete')
opt = input('Enter your option: ')
if opt == '2':
    name = input('Enter your name: ')
    uname = input('Enter your Username: ')
    pword = verify()
    cpword = input('Confirm the Password: ')

    if pword == cpword:
        fn = 'userdiction.json'
        var = {
                uname:[name,pword]
            }

        if check(fn):
            var = fetch(fn)
            if dcheck(var,uname):
                if confirm():
                    var[uname] = [name,pword]
                    if write(var,fn) == True:
                        print('User created successfully!!!')
            else:
                var[uname] = [name,pword]
                if write(var,fn) == True:
                    print('User created successfully!!!')
        else:
            if write(var,fn) == True:
                print('User created successfully!!!')
if opt == '3':
    if delete(fn):
        print('Database deleted!!!')
            




