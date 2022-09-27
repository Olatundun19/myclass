
l = 0
b = 0


def res_prt(a,v,res,s):
    if s == 'a':
        print('The {} of the {} = {}cm^2'.format(a,v,res))
    elif s == 'p':
        print('The {} of the {} = {}cm'.format(a,v,res))

def val_input(s):
    global l, b
    if s == 'r':
        l = float(input('Enter the Length of the rectangle: '))
        b = float(input('Enter the Breadth of the rectangle: '))
    elif s == 's':
        l = float(input('Enter the Length of the square: '))

def area_rect():
    val_input('r')
    res = l * b
    res_prt('area','rectangle',res,'a')

def peri_rect():
    val_input('r')
    res = 2 * (l + b)
    res_prt('perimeter','rectangle',res,'p')

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