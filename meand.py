n=int(input('ENTER THE NUMBER OF COURSES OFFERED: '))
courses = []
i=1
j=0
while i<=n:
    x=int(input('ENTER SCORE:'))
    if x<0 or x>100:
        print('ERROR!!!INVALID SCORE')
    else:
        courses.append(x)
        i=i+1
        j=j+x
k=j/n
p=len(courses)-1
i=0
a=0
while i<=p:
    x = abs(courses[i] - k)
    a=a+x
    i=i+1
md = a/n
print('Total score = {}\nAverage score = {}\nMean Deviation = {}'.format(j,k,md))



#print('Average score = {}'.format(k))
#print('Mean Deviation = {}'.format(md))