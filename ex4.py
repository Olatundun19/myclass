n = int(input('Enter the number of fruits to sample: '))
fruits = []
i = 1
while i <= n:
    x = input('Enter the fruit: ')
    fruits.append(x)
    i = i + 1
opt = input('Enter the fruit to serach: ')
optl = opt.lower()
i = 0
n = len(fruits) - 1
x = False
while i <= n:
    a = fruits[i].lower()
    if optl == a:
        x = True
        break
    i = i + 1
if x == True:
    print('{} is in the list submitted, Located at index: {} and Length: {}'.format(opt,i,i+1))
else:
    print('{} is not on the list!!!'.format(opt))
print('The Fruits enetered are: ')
i = 0
while i <= n:
    print(fruits[i])
    i = i + 1
