print('The program collects the data of the user')
print('Pls enter your details below')

sname = input('Enter your surname: ')
fname = input('Enter your first name:')
mname = input('Enter your middle name:')
age = input('Enter your age:')
matric = input('Enter your matric number:')
course = input('Enter your course:')


detail = 'Surname: ' + sname + '\nFirst name: ' + fname + '\nMiddle name: ' + mname + '\nAge: ' + age + '\nMatric Number: ' + matric + '\nCourse: ' + course; 


f = open('details.txt',"w")
f.write(detail)
f.close()

print('Details saved successfully!!!')