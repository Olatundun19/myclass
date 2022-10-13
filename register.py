import json
import os
print('Register User')
print('The program stores the user details')

ag=int(input('Enter your age:'))
if ag<18:
    print('SORRY USER MUST BE 18 OR ABOVE')
else:
    lname = input('Enter your Last name: ')
    fname = input('Enter your First name: ')
    mname = input('Enter your Middle name: ')
    uname = input('Enter your Username: ')
    age = ag
    matric = input('Enter your Matric number: ')
    course = input('Enter your Course: ')

    while 1:
       pword = input('Enter your password: ')
       x = len(pword)

       if x <= 7:
          print('Password should be more that 7 characters!!!')
       else: 
          break

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
        
                }

   
    else:
      print('Incorrect Password entered, Pls Try again!!!')