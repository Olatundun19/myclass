a = 'My name is Olatundun'
b = 'My age is 100'


def shw():
    global b
    b = a + ', I am smart!!!'
    print(b)


print(a)
shw()
print(b)