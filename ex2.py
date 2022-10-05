fruits = ['mango','guava','apple','lemon']

a = 'pawpaw'
x = False

i = 0
n = len(fruits) - 1
while i <= n:
    if fruits[i] == a:
        x = True
        break
    i = i + 1
if x == True:
    print('{} is in the list, Located at index: {} and Length: {}'.format(a,i,i+1))
else:
    print('{} is not on the list!!!'.format(a))