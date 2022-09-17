print('This program computes the area of different shapes')
print('1.Square 2.Rectangle 3.Circle 4.Trapezium 5.Triangle 6.Parallelogram')
opt= input('Enter your option:')
if opt=='1':
    print('Square was selected')
    l=float(input('Enter length of square:'))
    area=l*l
    print('The area of the square=',area)
elif opt=='2':
    print('Rectangle was selected')
    l=float(input('Enter length of rectangle:'))
    b=float(input('Enter breadth of breadth:'))
    area=l*b
    print('The area of the rectangle=',area)
elif opt=='3':
    print('Circle was selected')
    r=float(input('Enter the radius of the circle:'))
    pi=22/7
    area=pi*r*r
    print('The area of the circle=',area)
elif opt=='4':
    print('Trapezium was selected')
    t=float(input('Enter the top value of the trapezium:'))
    b=float(input('Enter the base of the trapezium:'))
    h=float(input('Enter the height of the trapezium:'))
    area=((t+b)/2)*h
    print('The area of the trapezium=',area)
elif opt=='5':
    print('Triangle was selected')
    b=float(input('Enter the base of the triangle:'))
    a=float(input('Enter the height of the triangle:'))
    area=(b*a)/2
    print('The area of the triangle=',area)
elif opt=='6':
    print('Parallelogram was selected')
    b=float(input('Enter base of parallelogram:'))
    h=float(input('Enter height of parallelogram:'))
    area=b*h
    print('The area of the parallelogram=',area)
else:
    print('Wrong option selected!!Try again please')
print('GOODBYE!!!!SEE YOU AGAIN')