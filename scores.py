x=float(input('Enter Number of Courses:'))
i=1
y=0
while i<=x:
    print('Enter course',i,':')
    j=float(input())
    if j>100 or j<0:
        print('INVALID SCORE,PLEASE TRY AGAIN')
    else:
        y=y+j
        i=i+1
k=y/x
print('Average=',k)
if k>=70:
    print('DISTINCTION')
elif k>=60:
    print('CREDIT')
elif k>=50:
    print('MERIT')
elif k>=45:
    print('PASS')
else:
    print('FAIL')