def maxfun(S, F1, *funs):
    max_sum = 0
    max_index = 0

    for num in S:
        max_sum += F1(num)

    for i,fun in enumerate(funs):
        now_sum = 0
        
        for num in S:
            now_sum += fun(num)

        if now_sum >= max_sum:
            max_sum = now_sum
            max_index = i + 1

    if max_index == 0:
        return F1
    else:
        return funs[max_index - 1]

from math import *
print(maxfun(range(-2,10), sin, cos, exp)(1))
