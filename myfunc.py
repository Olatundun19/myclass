def abs(v):
    if v > 0:
        return v
    elif v < 0:
        return v * -1
    elif v == 0:
        return 0

def sq(v):
    return v ** 0.5

def sqr(v):
    if v > 0:
        return sq(v)
    elif v == 0:
        return 0
    elif v < 0:
        return 'j' + str(sq(abs(v)))