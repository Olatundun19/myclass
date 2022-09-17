print('The program computes quadratic (ax^2+bx+c)')
a=float(input('Enter value of a: '))
b=float(input('Enter value of b: '))
c=float(input('Enter value of c: '))
d=(b**2)-(4*a*c)
h=-1*b
e=2*a
if d<0:
    d=d*-1
    g=d**0.5
    re=h/e
    im=g/e
    print('X1=',re,'+j',im)
    print('X2=',re,'-j',im)
elif d==0:
    g=h/e
    print('X1=X2=',g)
else:
    g=d**0.5
    x1=(h+g)/e
    x2=(h-g)/e
    print('X1=',x1)
    print('X2=',x2)
   