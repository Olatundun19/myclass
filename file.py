f = open("new.txt","a")

ch = '\nI like reading novels\n'

f.write(ch)

f.close()

f = open("new.txt","r")

res = f.read()

print(res)

import detail