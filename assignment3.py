print('This programme converts the unit of values')
print('1.Km to m, 2.m to cm, 3.cm to mm, 4.inches to m, 5.Feet to inches')
opt=input('Enter Option Below:')
x=float(input('Enter value for convertion:'))
if opt=='1':
    i=x*1000
    print(i)
elif opt=='2':
    i=x*100
    print(i)
elif opt=='3':
    i=x*10
    print(i)
elif opt=='4':
    i=x/39.37
    print(i)
elif opt=='5':
    i=x*12
    print(i)
else:
    print('ERROR!!WRONG OPTION')
