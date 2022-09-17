name=input('Please enter your name:')
print(name)
cla=input('Please enter your class:')
score=float(input('Please enter your score:'))
if score>=101:
    print(name,'Score is above range,Try again')
elif score>=70:
    print(name,'you have an A')
elif score>=60:
    print(name,'you have a B')
elif score>=50:
    print(name,'you have a C')
elif score>=45:
    print(name,'you have a D')
elif score>=0:
    print(name,'you have an E')
else:
    print(name,'Score below normal range!!!Try again please')
print('Goodbye,see you soon!!')