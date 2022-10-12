
a=input('Enter your name:')
b=input('Enter your age:')
c=input('Enter state of origin:')
d=input('Enter name of school:')
e=input('Enter allergies:')
f=input('Enter favourite colour:')
g=input('Enter home address:')
information= 'Her name is {0},she is {1} years old, she is fron {2} state, the name of her school is {3}, she is allergic to {4} and her favourite colour is {5} , incase of any allergic reaction please go to {6}   '
k= information.format(a,b,c,d,e,f,g)
print(k)
important= 'Her name is {},she is allergic to {}, her emergency address is {}'
m= important.format(a,e,g)
print(m)
#this programme gathers personal information and groups the important ones