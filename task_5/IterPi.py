def pigen():
    pi = 4
    yield pi
    
    coof = -3

    while True:
        pi += 4 / coof
        coof *= -1
        coof += 2 if coof > 0 else -2
        
        yield pi

        
