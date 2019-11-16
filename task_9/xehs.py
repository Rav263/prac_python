def au_fun():
    n = 1
    while True:
        yield n
        n += 6

def xehs(s):
    ret = 0
    for i, k in zip(reversed(s), au_fun()):
        ret = ret | ((ord(i) - 32) << k)
    return ret
