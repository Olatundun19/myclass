import os

file = input('Enter the file to remove: ')
file = file + '.py'

if os.path.exists(file):
    os.remove(file)
    print('The operation is successful!!!')
else:
    print('File does not exist!!!')

os.rmdir('myfolder')
