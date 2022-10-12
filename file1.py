code = 'print(\'The program sum two numbers\')\nfn=float(input(\'Enter the first number: \'))\nsn=float(input(\'Enter the second number: \'))\nsum=fn+sn\nprint(\'Sum = \'+str(sum))'

f = open('sum.py','w')

f.write(code)
f.close()

import sum
