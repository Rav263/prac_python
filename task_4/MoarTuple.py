def moar(a, b, n):
    return sum(1 if i % n == 0 else 0 for i in a) > sum(1 if i % n == 0 else 0 for i in b)
