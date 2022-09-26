print('1. ADDITION 2. SUBTRACTION 3. MULTIPLICATION 4. DIVISION')
opt= input('CHOOSE OPTION OF YOUR CHOICE:')
if opt=='1':
    f=float(input('ENTER FIRST NUMBER:'))
    s=float(input('ENTER SECOND NUMBER'))
    a=f+s
    print(a)
elif opt=='2':
    f=float(input('ENTER FIRST NUMBER:'))
    s=float(input('ENTER SECOND NUMBER'))
    a=f-s
    print(a)
elif opt=='3':
    f=float(input('ENTER FIRST NUMBER:'))
    s=float(input('ENTER SECOND NUMBER:'))
    a=f/s
    print(a)
elif opt=='4':
    f=float(input('ENTER FIRST NUMBER:'))
    s=float(input('ENTER SECOND NUMBER:'))
    a=f*s
    print(a)
else:
    print('WRONG OPTION!!!!TRY AGAIN')
