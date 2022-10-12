import json

print('Login')

f = open('users.txt','r')
users = f.read()
f.close()

user = json.load(users)

#uname = input('Enter your username: ')
#pword = input('Enter your password: ')

print(user)





