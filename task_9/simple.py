
def xehs(s):
    n = len(s)
    s = "0"*((4-n)%4) + s

    result = 0
    
    for i in range(0,n,4):
        d1 = ord(s[i]) - 32
        d2 = ord(s[i+1]) - 32
        d3 = ord(s[i+2]) - 32
        d4 = ord(s[i+3]) - 32
        d = ((d1*64 | d2)*64 | d3)*64 | d4
        result = result*16777216 | d

    return result


