import json

def write(var,fn):
    var = json.dumps(var,indent=4,sort_keys=True)
    f = open(fn,'w')
    f.write(var)
    f.close()
    return True

def fetch(fn):
    f = open(fn,'r')
    x = f.read()
    x = json.loads(x)
    return x

def confirm():
    opt = input('Do you want to overwrite (y/n): ')
    opt = opt.lower()
    if opt == 'y':
        return True
    else:
        return False
