def dcheck(var,val):
    chk = False
    for x in var:
        if val == x:
            return True
    if chk == False:
        return False