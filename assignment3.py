print('This programme converts the unit of values')
print('1. km to m 2. m to cm 3. cm to mm 4. inches to m 5. Feet to inches')
opt=input('Enter Option Below:')
try:
    x=float(input('Enter the value for conversion:'))
    print('The value for conversion is ' + str(x))
    if opt=='1':
       i=x*1000
       print(str(x) + 'km = ' + str(i) + 'm')
    elif opt=='2':
       i=x*100
       print(str(x) + 'm = ' + str(i) + 'cm')
    elif opt=='3':
       i=x*10
       print(str(x) + 'cm = ' + str(i) + 'mm')
    elif opt=='4':
       i=x/39.37
       print(str(x) + 'inches = ' + str(i) + 'm')
    elif opt=='5':
       i=x*12
       print(str(x) + 'Feet = ' + str(i) + 'inches')
    else:
       print('ERROR!!WRONG OPTION')
except:
    print('You have made a wrong entry, please try again')

