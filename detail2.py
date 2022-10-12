code = 'print(\'The programe is from somewhere else\')'

f = open('hello.py','w')
f.write(code)
f.close()

import hello

