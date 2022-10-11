print('The program collects the data of the user')
print('Pls enter your details below')

sname = input('Enter your surname: ')



f = open('details.txt',"w")
f.write('Surname: ' + sname + '.\n')
f.close()

print('Details saved successfully!!!')