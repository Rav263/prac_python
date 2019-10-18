def BinPow(a, N, f):
    return a if N == 1 else f(BinPow(a, N // 2 if N % 2 == 0 else N // 2 + 1, f), BinPow(a, N // 2, f))


