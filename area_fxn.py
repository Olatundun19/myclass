
l = 0
b = 0


def res_prt(a,v,res,s):
    if s == 'a':
        print('The {} of the {} = {}cm^2'.format(a,v,res))
    elif s == 'p':
        print('The {} of the {} = {}cm'.format(a,v,res))

def val_input(s):
    global l, b, r, pi
    if s == 'r':
        l = float(input('Enter the Length of the rectangle: '))
        b = float(input('Enter the Breadth of the rectangle: '))
    elif s == 's':
        l = float(input('Enter the Length of the square: '))
    elif s == 'c':
        r=float(input('Enter the radius of the circle'))
        pi = 22/7

def area_rect():
    val_input('r')
    res = l * b
    res_prt('area','rectangle',res,'a')

def peri_rect():
    val_input('r')
    res = 2 * (l + b)
    res_prt('perimeter','rectangle',res,'p')

def area_squa():
    val_input('s')
    res= l*l
    res_prt('area','square',res,'a')

def peri_squa():
    val_input('s')
    res=4*l
    res_prt('perimeter','square',res,'p')

def area_cir():
    val_input('c')
    pi = 22/7
    res= pi*r*r
    res_prt('area','circle',res,'a')

def peri_cir():
    val_input('c')
    res= 2*pi*r
    res_prt('perimeter','circle',res,'p')

def intro(a,v):
    print('The {} of {} Computation Selected!!!'.format(a,v))


print('The program computes the Area and Perimeter of Rectangle/Square')
print('1. Area of Rectangle 2. Perimeter of Rectangle')
print('3. Area of Square    4. Perimeter of Square')
print('5. Area of Circle    6. Circumference of Circle')

opt = input('Enter your option: ')


if opt == '1':
    intro('area','rectangle')
    area_rect()
elif opt == '2':
    intro('perimeter','rectangle')
    peri_rect()
elif opt == '3':
    intro('area','square')
    area_squa()
elif opt =='4':
    intro('perimeter','square')
    peri_squa()
elif opt =='5':
    intro('area','circle')
    area_cir()
elif opt =='6':
    intro('perimeter','circle')
    peri_cir()
else:
    print('WRONG OPTION!!!TRY AGAIN PLEASE')