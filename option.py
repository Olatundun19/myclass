from tkinter import N


print('1. ADDITION 2. SUBTRACTION 3. MULTIPLICATION 4. DIVISION ')
opt= input('CHOOSE FUNCTION OF YOUR CHOICE:')
n=int(input('ENTER THE NUMBER OF NUMBERS:'))
y=0
p=1
x=1
if opt=='1':
    while x<=n:
        j=float(input('ENTER NUMBER:'))
        y=y+j
        x=x+1
    print(y)
elif opt=='2':
    while x<=n:
        j=float(input('ENTER NUMBER:'))
        y=j-y
        x=x+1
    print(y)
elif opt=='3':
    while x<=n:
        j=float(input('ENTER NUMBER:'))
        p=p*j
        x=x+1
    print(p)
elif opt=='4':
    while x<=n:
        j=float(input('ENTER NUMBER:'))
        p=j/p
        x=x+1
    print(p)
else:
    print('WRONG OPTION!!!PLEASE TRY AGAIN')