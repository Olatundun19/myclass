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

def linear(a,b):
    return -b/a

def quad(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    d = (b ** 2) - (4 * a * c)
    if d == 0:
        x = -b / (2 * a)
        res = [str(x), str(x)] 
    elif d < 0:
        d = (-d) ** 0.5
        re = -b / (2 * a)
        im = d / (2 * a)
        res = [str(re) + '+j' + str(im), str(re) + '-j' + str(im)]
    else:
        d = (d ** 0.5)
        x1 = (-b + d) / (2 * a)
        x2 = (-b - d) / (2 * a)
        res = [str(x1),  str(x2)]
    return res

def sim(a,b,c,d,e,f):
    x=((c*e)-(b*f))/((a*e)-(b*d))
    y=((c*d)-(a*f))/((b*d)-(a*e))
    ans=['x=',str(x), 'y=',str(y)]
    return ans

def sure(a,b,x,y):
    c= (a*x)+(b*y)
    cas=('c=',str(c))
    return cas