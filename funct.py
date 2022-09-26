def prt(a,b,c,op):
    print('The {} of {} and {} is {}.'.format(op,a,b,c))

def sum(a,b):
    sum = a + b
    prt(a,b,sum,'Sum')
    

def mult(a,b):
    m = a * b
    prt(a,b,m,'Multiplication')

def div(a,b):
    m = a / b
    prt(a,b,m,'Division')


sum(3,4)
sum(5,6)
sum(7,9)
mult(6,9)
div(6,8)
