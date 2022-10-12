print('The program collects the data of the user')
print('Pls enter your details below')

sname = input('Enter your surname: ')
fname = input('Enter your first name:')
mname = input('Enter your middle name:')
age = input('Enter your age:')
matric = input('Enter your matric number:')
course = input('Enter your course:')



f = open('details.txt',"w")
f.write('Surname: ' + sname + '\n')
f.write('First name: ' + fname + '\n')
f.write('Middle name: ' + mname + '\n')
f.write('Age: ' + age + '\n')
f.write('Matric Number: ' + matric + '\n')
f.write('Course: ' + course + '\n')
f.close()

print('Details saved successfully!!!')