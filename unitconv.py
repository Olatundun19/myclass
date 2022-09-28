def m2km(v):
    return v / 1000
def km2m(u):
    return u*1000
def c2k(w):
    return w+273
def ft2m(x):
    return x/3.281
def yd2in(y):
    return y*36
def pa2kpa(z):
    return z*1000
def j2wh(s):
    return s/3600
def w2kw(t):
    return t/1000
def cm2mm(o):
    return o*10

print('This programme converts values')
print('1.m to km .2.km to m .3.c to k .4.ft to m .5.yd to in .6.pa to kpa .7.j to wh .8.w to kw .9.cm to mm')
opt=input('Enter option please:')
if opt=='1':
    a = float(input('Enter the value in m: '))
    print('The conversion in km = ' + str(m2km(a)))
elif opt=='2':
    b=  float(input('Enter the value in km: '))
    print('The conversion in m ='+str(km2m(b)))
elif opt=='3':
    c=  float(input('Enter the value in c: '))
    print('The conversion in k ='+str(c2k(c)))
elif opt=='4':
    d=  float(input('Enter the value in ft: '))
    print('The conversion in m ='+str(ft2m(d)))
elif opt=='5':
    e=  float(input('Enter the value in yd: '))
    print('The conversion in in ='+str(yd2in(e)))
elif opt=='6':
    f=  float(input('Enter the value in pa: '))
    print('The conversion in kpa ='+str(pa2kpa(f)))
elif opt=='7':
    g=  float(input('Enter the value in j: '))
    print('The conversion in wh ='+str(j2wh(g)))
elif opt=='8':
    h=  float(input('Enter the value in w: '))
    print('The conversion in kw ='+str(w2kw(h)))
elif opt=='9':
    i=  float(input('Enter the value in cm: '))
    print('The conversion in mm ='+str(cm2mm(i)))
else:
    print('WRONG OPTION')