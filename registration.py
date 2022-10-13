import json
print('Register User')
print('The program stores the user details')


lname = input('Enter your Last name: ')
fname = input('Enter your First name: ')
mname = input('Enter your Middle name: ')
uname = input('Enter your Username: ')
age = input('Enter your Age: ')
matric = input('Enter your Matric number: ')
course = input('Enter your Course: ')

pword = input('Enter your password: ')
if pword>7:
    cpword = input('Confirm your password: ')
    if pword == cpword:
        name = lname+ ' ' + fname + ' ' + mname
        detail = {
    
              'lname':lname,
              'fname':fname,
              'mname':mname,
              'name':name,
              'age':age,
              'matric':matric,
              'pword':pword,
              'uname':uname
              }
        x = json.dumps(detail,indent=4)

        f = open('yes.txt','p')
        f.write(x)
        f.close()
        print(name + ', details saved successfully!!!')
    else:
         print('Incorrect Password entered, Pls Try again!!!')
else:
    print('PASSWORD IS LESS THAN 8 CHARACTERS!!!PLEASE RETRY')