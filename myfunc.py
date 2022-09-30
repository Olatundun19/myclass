from tkinter import E


def abs(v):
    if v > 0:
        return v
    elif v < 0:
        return v * -1
    elif v == 0:
        return 0

def sq(v):
    return v ** 0.5

def sqr(v):
    if v > 0:
        return sq(v)
    elif v == 0:
        return 0
    elif v < 0:
        return 'j' + str(sq(abs(v)))

def pow(a,b):
    return a ** b

def pi():
    return 22 / 7

def quad(b,a,c):
    d= b**2 - 4*a*c
    h=(-1*b)
    e=(2*a)
    if d<0:
        g=(-1*d)**0.5
        re=h/e 
        im=g/e 
        f= print('X1=',re,'+j',im, 'X2=',re,'-j',im)
        return f
    elif d==0:
        g=h/e 
        k=print('X1=X2=',g)
        return k
    else:
        g= d**0.5
        x1=(h+g)/e 
        x2=(h-g)/e 
        m=print('X1=',x1,'  X2=',x2)
        return m
