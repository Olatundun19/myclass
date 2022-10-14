import os

def check(fn):
    if os.path.exists(fn):
        return True
    else:
        return False

def delete(fn):
    try:
        os.remove(fn)
        return True
    except:
        return False
