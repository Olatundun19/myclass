a = '1'

v = 'i'
s = False
c = 0
b = 0

if a == 'True' or a == 'False':
    v = 'b'
else:
    for x in a:
        print(x)
        if x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9':
            b = b + 1
            pass
        if x == '.' and b > 0:
            v = 'f'
        else:
            s = True
            if c == 0:
                v = 'c'
            elif c > 0:
                v = 's'
            c = c + 1

if s == False and v == 'b':
    print('Boolean')
elif s == False and v == 'f':
    print('Float')
elif s == False and v == 'i':
    print('Integer')
elif s == True and v == 'c':
    print('Character')
elif s == True and v == 's':
    print('String')
