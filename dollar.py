

usd=lambda x: x*736
pound=lambda x: x*825
cad=lambda x: x*561
print('THIS PROGRAM CONVERTS USD, POUNDS AND CAD TO NAIRA')
x=float(input('ENTER VALUE TO CONVERT:'))
u=usd(x)
p=pound(x)
c=cad(x)

print('NAIRA EQUIVALENT OF USD='+ str(u))
print('NAIRA EQUIVALENT OF POUNDS='+ str(p))
print('NAIRA EQUIVALENT OF CAD='+ str(c))