import json

print('Login')

with open('users.json') as f:
   users = json.load(f)

print(users)

#uname = input('Enter your username: ')
#pword = input('Enter your password: ')







