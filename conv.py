dollar = lambda n: n * 706
pound = lambda n: n * 825
euro = lambda n: n * 704

print('The program convert naira to usd, pounds and euro')

n = float(input('Enter the Naira: '))

d = dollar(n)
p = pound(n)
e = euro(n)

print('The Dollar equivalent is ' + str(d))
print('The Pound equivalent is ' + str(p))
print('The Euro equivalent is ' + str(e))